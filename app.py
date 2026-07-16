import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration, BlipForQuestionAnswering
import torch
from PIL import Image

# 1. إعداد المعالج وتحسين الأداء
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if torch.cuda.is_available() else torch.float32

print("Loading core models directly. Please wait...")

# تحميل نموذج الوصف
caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base", torch_dtype=dtype).to(device)

# تحميل نموذج الاستجواب البصري (VQA)
vqa_processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
vqa_model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base", torch_dtype=dtype).to(device)

# 2. دالة توليد الوصف التلقائي فور رفع الصورة
def generate_scene_caption(image):
    if image is None:
        return "⚠️ Error: Please upload an aerial reconnaissance image."
    try:
        raw_image = image.convert('RGB')
        caption_inputs = caption_processor(raw_image, return_tensors="pt").to(device, dtype)
        out_caption = caption_model.generate(**caption_inputs)
        return caption_processor.decode(out_caption[0], skip_special_tokens=True)
    except Exception as e:
        return f"⚠️ Captioning Failure: {str(e)}"

# 3. دالة الإجابة على الأسئلة التكتيكية (تعمل بشكل منفصل وديناميكي)
def answer_tactical_question(image, question):
    if image is None:
        return "⚠️ Error: Image context is missing."
    if not question or question.strip() == "":
        return "⚠️ Error: Tactical question cannot be empty."
    try:
        raw_image = image.convert('RGB')
        vqa_inputs = vqa_processor(raw_image, question, return_tensors="pt").to(device, dtype)
        out_vqa = vqa_model.generate(**vqa_inputs)
        return vqa_processor.decode(out_vqa[0], skip_special_tokens=True)
    except Exception as e:
        return f"⚠️ VQA Failure: {str(e)}"

# 4. بناء الواجهة المحدثة (Decoupled UI Workflow)
with gr.Blocks(theme=gr.themes.Soft(primary_hue="slate", neutral_hue="gray")) as demo:
    gr.Markdown("# 🚁 Tactical Drone Reconnaissance Analyzer")
    gr.Markdown("Upload an aerial image for immediate macro-analysis, then input specific queries for targeted VQA extraction.")

    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(type="pil", label="Aerial Image Upload")
            input_question = gr.Textbox(label="Tactical Question (e.g., 'Are there any vehicles?')")
            analyze_btn = gr.Button("Submit Query", variant="primary")

        with gr.Column(scale=1):
            output_caption = gr.Textbox(label="1. Automated Scene Description (Generated on Upload)")
            output_answer = gr.Textbox(label="2. VQA Extraction Result")

    # [حدث الرفع]: تشغيل نموذج الوصف تلقائياً بمجرد إسقاط أو رفع الصورة
    input_image.upload(fn=generate_scene_caption, inputs=input_image, outputs=output_caption)

    # [حدث الاستجواب]: تشغيل نموذج الـ VQA عند الضغط على الزر أو الضغط على Enter داخل مربع النص
    analyze_btn.click(fn=answer_tactical_question, inputs=[input_image, input_question], outputs=output_answer)
    input_question.submit(fn=answer_tactical_question, inputs=[input_image, input_question], outputs=output_answer)

demo.launch(share=True)
