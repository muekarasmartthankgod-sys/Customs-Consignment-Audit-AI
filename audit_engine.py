# =============================================================
# REPOSITORY: Customs-Consignment-Audit-AI
# PURPOSE: Multimodal Fusion (YOLO Vision + Gemini Reasoning)
# GOAL: Generate Comprehensive Audit Reports in Seconds
# =============================================================

import os
from google import genai
from google.genai import types
from ultralytics import YOLO

# --- CONFIGURATION ---
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_KEY_HERE")
WEIGHTS_PATH = 'weights/yolov8_best.pt' 

client = genai.Client(api_key=API_KEY)

def generate_multimodal_audit(image_path, manifest_text):
    """
    The 'Superintendent's Workflow':
    1. YOLOv8 detects the physical reality.
    2. Gemini extracts manifest data and cross-references it with detection.
    3. Produces a final Comprehensive Audit Report.
    """
    
    # --- STAGE 1: VISION (YOLOv8) ---
    model = YOLO(WEIGHTS_PATH)
    results = model.predict(image_path, conf=0.25, imgsz=1024, verbose=False)
    
    detections = []
    for box in results[0].boxes:
        label = model.names[int(box.cls)]
        conf = box.conf[0].item()
        detections.append(f"{label} (Confidence: {conf:.2f})")
    
    vision_summary = ", ".join(detections) if detections else "No objects localized."

    # --- STAGE 2: REASONING (GEMINI 2.0 FLASH) ---
    with open(image_path, 'rb') as f:
        image_bytes = f.read()

    prompt = f"""
    ROLE: Senior Customs Auditor (UK Border Force Standard).
    
    TASK: Generate a Comprehensive Audit Report.
    
    INPUT DATA:
    1. MANIFEST DATA: {manifest_text}
    2. YOLOv8 DETECTIONS: {vision_summary}
    
    REPORT STRUCTURE:
    - DATA EXTRACTION: Extract HS Code, Value, Origin, and Weight from manifest.
    - DISCREPANCY ANALYSIS: Does the X-ray detection match the manifest? 
    - RISK LEVEL: (Low/Medium/High)
    - VERDICT: Final recommendation for the officer.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
                prompt
            ]
        )
        
        print("\n" + "="*60)
        print("          COMPREHENSIVE CARGO AUDIT REPORT")
        print("="*60)
        print(response.text)
        print("="*60)

    except Exception as e:
        print(f"Audit Generation Failed: {e}")

if __name__ == "__main__":
    # Simulate a manifest with the sensitive info you mentioned
    sample_manifest = """
    Document: Bill of Lading #44592
    Goods: Industrial Tyres (HS 4011)
    Exporter: Global Rubber Ltd (Origin: Brazil)
    Weight: 12,500 KG | Value: $45,000
    """
    generate_multimodal_audit("cargo_scan.jpg", sample_manifest)
