# Customs Consignment Audit AI

**Smart Thankgod** *Chief Superintendent of Customs* | *MSc Computer Science Researcher — University of York* | *Certified Image Analyst (UK Border Force Trained)*

---

## 🛡️ Operational Impact: Automation vs. Manual Audit
The core mission of this project is to solve the "Information Overload" in Customs logistics. Manual verification of shipping documents—**Bill of Lading, Packing List, Invoice, CCVO, and Manifests**—is time-intensive and prone to human oversight.

### ⚡ Speed-to-Intelligence
This AI framework extracts and cross-references critical data points in **seconds**, a task that traditionally takes officers significantly longer. The system focuses on:
* **Regulatory Compliance:** HS Codes, Country of Origin, and Country of Dispatch.
* **Economic Protection:** Unit Price, Total Value of Goods, and Quantity.
* **Logistics Accuracy:** Gross/Net Weight, Exporter/Importer details, and Unit of Measurement.

## 🚀 Prototype & Live Demo
- **Current Live Demo:** [Trade Audit AI (Logic Alpha)](https://trade-audit-ai-kqefxmftigyq4lectascj2.streamlit.app/)
- **Demo Scope:** This version demonstrates the **Automated Document Intelligence** module, showing how AI reads and analyzes complex manifest data instantly.
- **Roadmap:** Integration of the Multimodal Image Analysis module (X-ray scanning) is currently in development.

## 🔬 Research Methodology
* **CNN Baseline:** YOLOv8/YOLO12 utilized for local feature extraction on a **1,230-image augmented dataset** (480 original real-world NII scans).
* **Transformer Target:** **RT-DETR (ViT)** implementation for global context attention and NMS-free end-to-end detection.

## 📄 Data Availability & Ethics
**Notice:** This research utilizes a unique dataset of **480 original real-world anonymized X-ray scans** from the Nigeria Customs Service. 
- **Integrity:** Raw imagery and weights are restricted to protect the "first-to-publish" integrity for upcoming **IEEE journal submission**.
