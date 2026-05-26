import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import os
import warnings

warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Generate concise prompt using GPT
def chatgpt_api(input_text):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f'Summarize this text "{input_text}" into a short and concise DALL-E prompt.'
            }
        ]
    )

    reply = response.choices[0].message.content
    return reply


# Generate image using DALL-E
def dall_e_api(dalle_prompt):

    response = client.images.generate(
        model="dall-e-2",
        prompt=dalle_prompt,
        size="512x512",
        n=1
    )

    image_url = response.data[0].url
    return image_url


# Convert speech to text
def whisper_transcribe(audio):

    with open(audio, "rb") as audio_file:

        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    speech_text = transcript.text

    # Generate optimized image prompt
    dalle_prompt = chatgpt_api(speech_text)

    # Generate image
    image_url = dall_e_api(dalle_prompt)

    return speech_text, image_url


# Outputs
output_1 = gr.Textbox(label="Speech to Text")
output_2 = gr.Image(label="Generated Image")


# Gradio Interface
speech_interface = gr.Interface(
    fn=whisper_transcribe,
    inputs=gr.Audio(sources="microphone", type="filepath"),
    outputs=[output_1, output_2],
    title="Generate Images using Voice"
)

speech_interface.launch(debug=True)
