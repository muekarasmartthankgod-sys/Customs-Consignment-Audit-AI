# Trade Audit AI: Multimodal Consignment Verification

**Smart Thankgod** *Chief Superintendent of Customs | MSc Computer Science Researcher, University of York*

---

## 🛡️ Project Overview
This repository contains a prototype for **Decision Intelligence** in customs logistics. The system bridges the gap between physical inspection and digital documentation by combining **YOLOv8** computer vision with **Gemini 2.0 Flash** vision-language reasoning.

### Key Features
- **Object Detection:** Localizes and classifies items in X-ray imagery.
- **Spatial Reasoning:** Calculates cargo scale (Industrial vs. Passenger) relative to container volume.
- **Automated Audit:** Cross-references vision data with shipping manifests to detect Fraud or Non-Conformity.

---

## 📄 Data Availability & Research Integrity
**Notice:** This project utilizes a domain-specific dataset of **350+ anonymized real-world X-ray scans** from the Nigeria Customs Service.

To maintain research integrity for upcoming **IEEE publication**:
- **Dataset Status:** Imagery and ground-truth labels are currently **restricted**.
- **Weights:** Trained model weights (`best.pt`) are not included in the public repository to prevent unauthorized replication before publication.
- **Inquiries:** For academic benchmarking or collaboration, please contact the author at [muekarasmartthankgod@gmail.com](mailto:muekarasmartthankgod@gmail.com).

---

## 🚀 Getting Started
1. **Clone the repo:** `git clone https://github.com/muekarasmartthankgod-sys/Customs-Consignment-Audit-AI.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set API Key:** Ensure your `GEMINI_API_KEY` is set in your environment variables.
4. **Run Audit:** `python audit_engine.py`

---

## 🤝 Connect
- **LinkedIn:** [Smart Thankgod](https://www.linkedin.com/in/smart-thankgod-893ab3371)
- **Portfolio:** [Trade Audit AI Live Demo](https://trade-audit-ai-kqefxmftigyq4lectascj2.streamlit.app/)
