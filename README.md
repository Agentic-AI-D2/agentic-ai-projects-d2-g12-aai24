# 🤖 Multimodal Education Creator (Agentic AI)

A **Multi-Agent AI system** that generates **educational content + diagrams** using **LLMs and Stable Diffusion**.

---

## 🚀 Overview

This project is a **Multimodal Education Content Generator** built using a **Multi-Agent architecture**.
It combines **text generation** and **image generation** to create rich educational material.

The system uses:

* AI agents for research and content creation
* Stable Diffusion for diagram generation
* Streamlit for interactive UI

---

## 🧠 Architecture

```
User Input
   ↓
Research Agent
   ↓
Writer Agent
   ↓
Image Prompt Agent
   ↓
Stable Diffusion Turbo (Image Generation)
   ↓
Review Agent
   ↓
Streamlit Output (Text + Image)
```

---

## 🤖 Agents in the System

| Agent                  | Role                                     |
| ---------------------- | ---------------------------------------- |
| 🔍 Research Agent      | Collects information about topic         |
| ✍️ Writer Agent        | Generates structured educational content |
| 🖼️ Image Prompt Agent | Creates prompt for diagram               |
| ✅ Review Agent         | Improves and refines output              |

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Multi-Agent Framework:** CrewAI
* **LLM:** Gemini / Groq (LLaMA)
* **Image Generation:** Stable Diffusion Turbo
* **Libraries:** Torch, Diffusers, Transformers

---

## 📁 Project Structure

```
multi_agent_education/
│
├── app.py                # Streamlit UI
├── crew.py               # Agent workflow
├── agents.py             # Agent definitions
├── tasks.py              # Task assignments
├── image_generator.py    # Image generation (Stable Diffusion)
├── requirements.txt      # Dependencies
├── .env                  # API keys
```

---

## 🔧 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/multimodal-education-creator.git
cd multimodal-education-creator
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 🖥️ Output

The system generates:

* 📘 Educational Content
* 🖼️ Educational Diagram

---

## 🎓 Use Case

* Students learning concepts visually
* Teachers generating teaching material
* AI-based education tools
* Multimodal learning systems

---

## 💡 Features

* Multi-Agent AI workflow
* Automated educational content generation
* AI-generated diagrams
* Simple Streamlit interface
* Fast inference using Turbo models

---

## 🧠 How It Works

1. User enters a topic
2. Research Agent gathers information
3. Writer Agent creates structured notes
4. Image Prompt Agent creates diagram prompt
5. Stable Diffusion generates diagram
6. Review Agent refines output
7. Streamlit displays final result

---

## 📌 Future Improvements

* PDF export
* Voice-based input
* Multi-language support
* Vector database integration
* Better diagram accuracy

---

## 🙌 Acknowledgements

* CrewAI
* HuggingFace Diffusers
* Streamlit
* Google Gemini / Groq

---
