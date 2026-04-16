# =================================================================
# PROJECT: Trade Audit AI (NIIU Research Prototype)
# DEVELOPER: Smart Thankgod (MSc Research - University of York)
# PURPOSE: Multimodal X-Ray Classification & Manifest Verification
# =================================================================

import os
from google import genai
from ultralytics import YOLO
import cv2

# --- CONFIGURATION ---
# To run this, set your environment variable or replace 'YOUR_KEY_HERE'
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_KEY_HERE")
STRATEGIC_MODEL = "gemini-2.0-flash" 
WEIGHTS_PATH = 'weights/best.pt' # Path to your private model weights

client = genai.Client(api_key=API_KEY)

def run_trade_audit_ai(image_path, expected_manifest):
    """
    Executes a multimodal audit combining YOLOv8 vision and Gemini reasoning.
    """
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return

    if not os.path.exists(WEIGHTS_PATH):
        print(f"Note: Model weights ({WEIGHTS_PATH}) are restricted. Use a sample for testing.")
        return

    # --- STAGE 1: YOLOv8 OBJECT DETECTION ---
    vision_model = YOLO(WEIGHTS_PATH)
    results = vision_model.predict(image_path, conf=0.25, imgsz=1024, verbose=False)
    
    names = vision_model.names
    img_h, img_w = results[0].orig_shape
    total_area = img_h * img_w
    
    detections = []
    for box in results[0].boxes:
        label = names[int(box.cls)]
        conf = box.conf[0].item()
        
        # Spatial Analysis
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        area_pct = ((x2 - x1) * (y2 - y1) / total_area) * 100
        scale = "INDUSTRIAL" if area_pct > 10.0 else "PASSENGER"
        
        detections.append(f"{label} ({conf:.2f} conf, {scale})")

    summary = ", ".join(detections) if detections else "No items detected."

    # --- STAGE 2: DECISION INTELLIGENCE (GEMINI) ---
    prompt = f"""
    SYSTEM: Senior Customs Audit Officer (NIIU Specialist).
    TASK: Verify manifest against X-ray detections.
    
    STRICT COMPLIANCE RULES:
    1. CATEGORY: If manifest differs from detected category, flag as FRAUD.
    2. SCALE: If scale is inconsistent with declaration, flag as NON-CONFORMITY.
    
    DATA:
    - MANIFEST: {expected_manifest}
    - X-RAY DETECTIONS: {summary}
    """

    try:
        response = client.models.generate_content(model=STRATEGIC_MODEL, contents=prompt)
        print("\n" + "="*55)
        print("          TRADE AUDIT AI: VERIFICATION REPORT")
        print("="*55)
        print(f"FILE: {os.path.basename(image_path)}")
        print(f"ANALYSIS: {response.text}")
        print("="*55)
        
    except Exception as e:
        print(f"Audit failed at reasoning stage: {e}")

if __name__ == "__main__":
    # Standard Execution Call
    run_trade_audit_ai("test_image.jpg", "Large Truck Tyres")
