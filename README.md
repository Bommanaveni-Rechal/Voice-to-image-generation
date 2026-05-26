# Voice-to-image-generation
An AI-powered application that transforms spoken input into AI-generated images using advanced speech recognition, natural language processing, and generative AI models. The system captures voice commands, converts them into meaningful text prompts, enhances them using NLP techniques, and generates visually rich images in real time.


# Features

- Speech-to-text conversion using Whisper
- Prompt enhancement using GPT-3.5
- AI image generation using DALL·E 2
- Real-time voice-to-image pipeline
- Interactive Gradio UI

---

# Technologies Used

- Python
- Gradio
- OpenAI Whisper
- GPT-3.5 Turbo
- DALL·E 2
- Python Dotenv

---

# Project Structure

```bash
Voice-to-Image-Generator/
│
├── main.py
├── requirements.txt
├── README.md
├── Project_Documentation.md
├── .env
└── .gitignore
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Voice-to-Image-Generator.git
```

---

## 2. Navigate to Project Folder

```bash
cd Voice-to-Image-Generator
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup API Key

Create a `.env` file in the root directory.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Run the Project

```bash
python main.py
```

---

# How It Works

1. User gives voice input
2. Whisper converts speech to text
3. GPT-3.5 enhances the prompt
4. DALL·E generates the image
5. Output image is displayed in Gradio UI

---

# Sample Workflow

Voice Input → Speech Recognition → Prompt Processing → AI Image Generation

---

# Future Enhancements

- Multi-language support
- Image style customization
- Download generated images
- Mobile-friendly UI
- Real-time streaming transcription
- Cloud deployment

---

# Use Cases

- AI-assisted digital art
- Accessibility tools
- Voice-driven creative applications
- Educational AI projects

---

# Author

## Rechal Suhasini Bommanaveni

AI Engineer | Generative AI Enthusiast | Backend Developer

---

# Support

If you like this project, give it a star on GitHub.
