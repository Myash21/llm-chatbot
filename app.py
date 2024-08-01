import gradio as gr
from langchain.llms import Ollama
from gradio_client import Client

def generate_response(user_message):
    ollama = Ollama(base_url="http://localhost:11434", model="agri-mate")
    response = ollama.invoke(user_message)
    return response

iface = gr.Interface(
    fn=generate_response,
    inputs="textbox",
    outputs="textbox",
    title="Agri-Mate Chatbot",
    description="Ask your agriculture questions here!"
)

iface.launch()
