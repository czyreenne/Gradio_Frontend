import gradio as gr

with gr.Blocks() as demo:
    with gr.Sidebar():
        gr.Textbox()
        gr.Button()
        
demo.launch()
