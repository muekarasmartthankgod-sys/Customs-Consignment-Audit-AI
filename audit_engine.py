# =============================================================
# REPOSITORY: Customs-Consignment-Audit-AI
# PURPOSE: Multimodal Fusion (YOLO Vision + Gemini Reasoning)
# SECURITY: Environment Variable for API Key | Mock Data for Docs
# =============================================================

import os
import sys
from google import genai
from google.genai import types
from ultralytics import YOLO

# --- CONFIGURATION (SECURE) ---
# We retrieve the key from the system environment. No hardcoded keys.
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the key exists before starting
if not API_KEY:
    print("❌ ERROR: 'GEMINI_API_KEY' not found in Environment Variables.")
    print("Please set it using: export GEMINI_API_KEY='your_key_here' (Linux/Mac) or setx GEMINI_API_KEY 'your_key_here' (Windows)")
    sys.exit(1)

# Path to your trained weights (keep this out of GitHub if >100MB)
WEIGHTS_PATH = 'weights/yolov8_best.pt' 

# Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

def generate_multimodal_audit(image_path, manifest_text):
    """
    Core Research Logic:
    1. YOLOv8 for physical object localization.
    2. Gemini 2.0 Flash for statutory cross-referencing.
    """
    
    if not os.path.exists(image_path):
        print(f"❌ ERROR: Scan image not found at {image_path}")
        return

    # --- STAGE 1: DEEP LEARNING VISION (YOLOv8) ---
    try:
        model = YOLO(WEIGHTS_PATH)
        results = model.predict(image_path, conf=0.25, imgsz=1024, verbose=False)
        
        detections = []
        for box in results[0].boxes:
            label = model.names[int(box.cls)]
            conf = box.conf[0].item()
            detections.append(f"{label} ({conf:.2f})")
        
        vision_summary = ", ".join(detections) if detections else "No objects detected."
    except Exception as e:
        vision_summary = "Vision Layer Error: Model file may be missing."

    # --- STAGE 2: DECISION INTELLIGENCE (GEMINI) ---
    with open(image_path, 'rb') as f:
        image_bytes = f.read()

    # Optimized Prompt: Removing "Reasoning" - Factual Discrepancy Only
    prompt = f"""
    ROLE: Senior Customs Auditor.
    TASK: Generate a Statutory Discrepancy Report.
    
    INPUT DATA:
    - DOCUMENTATION: {manifest_text}
    - PHYSICAL DETECTION (YOLOv8): {vision_summary}
    
    MANDATORY FORMAT:
    1. STATUS: (CONFORMITY or NON-CONFORMITY)
    2. STATUTORY DISCREPANCY:
       - Declared: [Item name from manifest]
       - Detected: [Item name from vision]
       - Infraction: [State the nature of the breach]
    3. RECOMMENDED ACTION: [e.g., 100% Physical Examination]
    
    NOTE: Do not provide conversational reasoning. Provide factual comparison only.
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
        print("         COMPREHENSIVE CARGO AUDIT REPORT")
        print("="*60)
        print(response.text)
        print("="*60)

    except Exception as e:
        print(f"Audit Generation Failed: {e}")

if __name__ == "__main__":
    # --- ANONYMIZED TEST DATA ---
    # Using generic placeholders to ensure no real customs data is leaked.
    sample_manifest = """
    Bill of Lading: #REF-9901
    Declared Goods: New Pneumatic Tyres
    HS Code: 4011
    Quantity: 500 Units
    """
    
    # Ensure you have a 'cargo_scan.jpg' in your folder for testing.
    generate_multimodal_audit("test_scan.jpg", sample_manifest)
