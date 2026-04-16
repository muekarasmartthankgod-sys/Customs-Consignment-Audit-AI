# Customs Consignment Audit AI

**Smart Thankgod** *Chief Superintendent of Customs | MSc Computer Science Researcher — University of York | Certified Image Analyst (UK Border Force Trained)*

---

## 🎯 The Core Mission: Multimodal Audit Intelligence
Traditional consignment analysis is hindered by a manual bottleneck. Officers must spend valuable time searching for sensitive fields (HS Code, Weight, Value, Exporter) across multiple documents like the **Bill of Lading, Packing List, Invoice, and CCVO** before analyzing X-ray scans.

This project automates that workflow using **Multimodal Fusion**:
1. **Intelligence Extraction:** Instantly parses complex shipping documents for regulatory data.
2. **Spatial Detection:** Utilizes **YOLOv8** (Baseline) and **RT-DETR** (Future ViT Benchmark) to localize physical cargo.
3. **Cross-Referencing:** A **Gemini 2.0 Flash** reasoning engine compares the extracted manifest against detected visual data to generate a **Comprehensive Audit Report**.

---

## 🚀 Prototype & Live Demo
The current live environment showcases the **Document Intelligence** capability—extracting critical fields from manifests in seconds.

- **URL:** [Trade Audit AI Application](https://trade-audit-ai-kqefxmftigyq4lectascj2.streamlit.app/)
- **Access Code:** `EXPERT-2026`
- **Development Status:** The **Manifest Module** is fully operational for testing. The **Image Analysis Module** (multimodal fusion) is currently in development and accessible via the `audit_engine.py` script in this repository.

---

## 🔬 Research & Dataset
* **Dataset:** 480 original real-world anonymized X-ray scans, augmented to **1,230 images**.
* **Methodology:** Comparative analysis of CNNs (YOLO) vs. Vision Transformers (RT-DETR) for NII (Non-Intrusive Inspection).
* **Privacy:** Dataset and weights are restricted to protect research integrity for **IEEE journal submission**.

## 🤝 Connect
- [LinkedIn](https://www.linkedin.com/in/smart-thankgod-893ab3371) | [Email](mailto:muekarasmartthankgod@gmail.com)
