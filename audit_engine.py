# =============================================================
# REPOSITORY: Customs-Consignment-Audit-AI
# DEVELOPER: Smart Thankgod (UK Border Force Trained Analyst)
# INSTITUTION: MSc Research - University of York
# PURPOSE: Multimodal X-Ray Classification (YOLOv8) + 
#          Cognitive Manifest Verification (Gemini)
# =============================================================

import os
from google import genai
from ultralytics import YOLO

# --- CONFIGURATION ---
# Use environment variables for security
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_KEY_HERE")
STRATEGIC_MODEL = "gemini-2.0-flash" 

# Current Baseline: YOLOv8 
# Future Benchmark: RT-DETR (for Global Context Attention)
WEIGHTS_PATH = 'weights/yolov8_best.pt' 

client = genai.Client(api_key=API_KEY)

def run_trade_audit_ai(image_path, expected_manifest):
    """
    Executes a multimodal audit combining spatial CNN detection 
    with Vision-Language Model reasoning.
    """
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return

    if not os.path.exists(WEIGHTS_PATH):
        print(f"Note: Restricted Weights. Researching YOLOv8 vs RT-DETR.")
        return

    # --- STAGE 1: CNN SPATIAL ANALYSIS ---
    vision_model = YOLO(WEIGHTS_PATH)
    results = vision_model.predict(image_path, conf=0.25, imgsz=1024, verbose=False)
    
    detections = []
    for box in results[0].boxes:
        label = vision_model.names[int(box.cls)]
        conf = box.conf[0].item()
        detections.append(f"{label} ({conf:.2f} conf)")

    summary = ", ".join(detections) if detections else "No anomalies detected."

    # --- STAGE 2: COGNITIVE VERIFICATION (UK BORDER FORCE LOGIC) ---
    prompt = f"""
    SYSTEM: Senior Customs Auditor & Trained Image Analyst.
    TASK: Formal manifest verification. Compare declared goods against X-ray detections.
    DATA:
    - DECLARED (Manifest): {expected_manifest}
    - DETECTED (X-ray): {summary}
    RULES: Flag category mismatches as FRAUD and scale inconsistencies as NON-CONFORMITY.
    """

    try:
        response = client.models.generate_content(model=STRATEGIC_MODEL, contents=prompt)
        print("\n" + "="*55)
        print("      CUSTOMS CONSIGNMENT AUDIT: OFFICIAL REPORT")
        print("="*55)
        print(response.text)
        print("="*55)
    except Exception as e:
        print(f"Verification failed: {e}")

if __name__ == "__main__":
    run_trade_audit_ai("test_scan.jpg", "Large Truck Tyres")
