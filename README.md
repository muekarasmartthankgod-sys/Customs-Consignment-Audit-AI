# Customs Consignment Audit AI: Multimodal Intelligence

**Smart Thankgod** *Chief Superintendent of Customs | MSc Researcher (University of York) | UK Border Force Trained Analyst*

---

## 🎯 The Core Mission: Eliminating Manual Friction
Traditional consignment analysis is hindered by a "Manual Bottleneck." Officers must spend valuable time cross-referencing shipping documents (**Bill of Lading, Packing List, Invoice, CCVO**) against X-ray imagery. 

This project replaces manual search with **Multimodal Fusion**. By uploading both the manifest and the image, the system instantly:
1. **Extracts** critical regulatory data (HS Codes, Value, Weight, Origin, etc.).
2. **Detects** physical objects within the cargo using **YOLOv8** (Baseline) / **RT-DETR** (Future ViT Benchmark).
3. **Reasons** between the two data streams using **Gemini 2.0 Flash** to identify fraud, misclassification, or concealment.

## ⚡ Comprehensive Audit Reporting
The output is not just a "box" or "text"—it is a professional **Comprehensive Audit Report** that compares:
- **EXPECTED:** Data extracted from manifest (HS Code 8708, Gross Weight 5000kg, etc.)
- **DETECTED:** Findings from the Object Detection model (Spatial analysis, scale, and classification).
- **VERDICT:** High-speed reasoning on discrepancies (e.g., "Manifest declares Tyres, but high-density organic shielding detected").

## 🔬 Technical Roadmap
* **Vision (YOLOv8):** Currently handling spatial analysis on our **1,230-image augmented dataset**.
* **Reasoning (Gemini API):** Handling the complex logic of manifest-to-image verification.
* **Scale (RT-DETR):** Moving toward NMS-free, Global Context Attention for superior overlapping object resolution.

---

## 📄 Data & Research Integrity
- **Original Dataset:** 480 real-world anonymized X-ray scans (NCS).
- **Augmented Dataset:** 1,230 images.
- **Privacy:** Weights and raw scans are restricted for **IEEE publication** integrity.

## 🤝 Connect
[LinkedIn](https://www.linkedin.com/in/smart-thankgod-893ab3371) | [Live Logic Demo](https://trade-audit-ai-kqefxmftigyq4lectascj2.streamlit.app/)
