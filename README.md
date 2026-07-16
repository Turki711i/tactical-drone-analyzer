Markdown
# 🚁 Tactical Drone Reconnaissance Analyzer

An AI-driven inspection tool engineered for autonomous drone operators. It utilizes a dual-layer multimodal vision-language pipeline to translate raw, real-time aerial feeds into immediate, text-based situational awareness, accelerating tactical decision-making in security and surveillance operations.

## 🚀 Key Features
- **Event-Driven UI:** Decoupled execution logic using Gradio to mimic real-world tactical workflows.
- **Macro-Analysis:** Automatically generates a contextual scene description the moment an aerial view is uploaded.
- **Micro-Analysis:** Enables dynamic Visual Question Answering (VQA) queries on the same image without re-uploading.
- **Hardware Optimization:** Direct memory control (bypassing `pipeline` wrappers) with `torch.float16` and GPU (`cuda`) mapping for stable T4 execution.
- **Trustworthy AI:** Rigorous exception-handling blocks intercept invalid inputs (empty images/queries) to prevent backend crashes.

## 📖 How to Use
1. **Upload:** Drag and drop your aerial reconnaissance image into the **Aerial Image Upload** box. The system will automatically generate a contextual description in the **"Automated Scene Description"** field.
2. **Query:** Once the image is processed, type your tactical question (e.g., "Are there any vehicles?") in the **"Tactical Question"** box.
3. **Analyze:** Click the **"Submit Query"** button. The result appears in the **"VQA Extraction Result"** field. You can perform multiple queries on the same image context seamlessly.

## 🛠 Setup & Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/Turki711i/tactical-drone-analyzer.git](https://github.com/Turki711i/tactical-drone-analyzer.git)
cd tactical-drone-analyzer
2. Install dependencies:

Bash
pip install -r requirements.txt
3. Run the application:

Bash
python app.py
Once the server starts, open the generated local URL (e.g., http://127.0.0.1:7860) in your browser.

⚠️ Honest Limitations
Perspective Bias: BLIP models are trained on eye-level datasets; they occasionally misinterpret scale in top-down aerial imagery (e.g., classifying a single vehicle as a "large parking lot").

Compound Queries: The current VQA architecture lacks sequential reasoning for nested prompts (e.g., "How many cars and how many people?"). It truncates processing after the first entity.

Spatial Localization: The model processes global pixel blobs but lacks an inherent object detection mechanism to compute precise bounding boxes.

🔮 Future Scope
Integration of a dedicated Object Detection network (e.g., YOLO) to generate precise bounding boxes prior to VQA processing. This will eliminate spatial hallucinations and provide pinpoint tactical intelligence.

Developer: Turki Zafer Al-Bahish

Institution: Najran University - Computer Information Systems
