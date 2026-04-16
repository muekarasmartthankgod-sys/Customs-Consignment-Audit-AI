# Customs Consignment Audit AI

**Smart Thankgod** *Chief Superintendent of Customs* *MSc Computer Science Researcher — University of York* *Certified Image Analyst (UK Border Force Trained)*

---

## 🛡️ Project Overview
This repository hosts the development prototype for **Decision Intelligence** in cargo security. The system integrates real-time object detection with generative reasoning to automate the verification of shipping manifests against X-ray imagery.

## 🔬 Research Methodology: CNN vs. Transformer
My current research benchmarks different architectures for Non-Intrusive Inspection (NII):
* **YOLOv8/YOLO12 (CNN):** Our current baseline, utilized for its high inductive bias and efficiency on the current domain-specific dataset.
* **RT-DETR (ViT):** The future target for this project. Once the dataset scales, we will utilize **RT-DETR** for its **Global Context Attention** and **NMS-free** end-to-end detection, which is superior for resolving overlapping items in dense containers.

## 📄 Data Availability & Ethics
**Notice:** The project utilizes a unique dataset of **1,230+ real-world anonymized X-ray scans** from the Nigeria Customs Service.
- **Dataset Status:** Restricted. Imagery and ground-truth labels are withheld to protect research integrity for upcoming **IEEE publication**.
- **Model Weights:** The `best.pt` weights are kept private to prevent unauthorized replication of research results.
- **Inquiries:** Contact the author at [muekarasmartthankgod@gmail.com](mailto:muekarasmartthankgod@gmail.com).

## 🚀 Impact & Traction
- **Global Interest:** Significant traffic with over 130+ clones in recent development cycles.
- **Operational Logic:** Detection thresholds and reasoning prompts are informed by professional **UK Border Force** image analysis standards.

---

## 📫 Connect
- **LinkedIn:** [Smart Thankgod](https://www.linkedin.com/in/smart-thankgod-893ab3371)
- **Live Demo:** [Trade Audit AI Application](https://trade-audit-ai-kqefxmftigyq4lectascj2.streamlit.app/)
