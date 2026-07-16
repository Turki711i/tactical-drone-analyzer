# 🚁 Tactical Drone Reconnaissance Analyzer

## Overview
An AI-driven inspection tool engineered for autonomous drone operators. It utilizes a dual-layer multimodal vision-language pipeline to translate raw, real-time aerial feeds into immediate, text-based situational awareness, accelerating tactical decision-making in security and surveillance operations.

## Architecture & Features
- **Event-Driven UI:** Decoupled execution logic using Gradio to mimic real-world tactical workflows.
- **Macro-Analysis (Scene Comprehension):** Automatically generates a contextual description the moment an aerial view is uploaded (`.upload`).
- **Micro-Analysis (Dynamic VQA):** Allows operators to execute multiple consecutive Visual Question Answering queries (`.click` & `.submit`) without the computational overhead of regenerating the global caption.
- **Hardware Optimization:** Bypasses standard `pipeline` wrappers for direct memory control. Forces `torch.float16` precision and GPU mapping (`cuda`) for stable T4 execution.
- **Trustworthy AI:** Rigorous exception-handling blocks intercept invalid inputs (empty images/queries) directly within the UI, preventing backend (Error 500) crashes.

## Prerequisites
- Python 3.10+
- A CUDA-enabled GPU is highly recommended for optimal inference speed.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
