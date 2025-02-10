import gradio as gr

def upload_file(file, notes):
    if file is not None:
        return f"File '{file.name}' uploaded successfully with notes: {notes}"
    return "No file uploaded."

def search_action(query):
    return f"Searching for: {query}"

with gr.Blocks(css="""
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700&display=swap');

    * {
        font-family: 'Manrope', sans-serif !important;
        font-size: 16px !important;
    }

    .logo {
        font-family: 'Arial', sans-serif !important;
        color: white !important;
        font-size: 40px !important;
        font-weight: bold !important;
    }

    .top-bar {
        display: flex;
        align-items: center;
        background-color: #cc0000;
        padding: 10px 20px;
        height: 110px;
    }

    .search-box-container {
        gap: 10px;
        display: flex;            
        flex-grow: 1; /* Allow it to take up more space */
    }

    .search-box {
        width: 160px !important;
        height: 50px !important;
        border-radius: 20px !important;
        border: 1px solid #ddd !important;
        padding: 5px 15px !important;
        font-size: 14px !important;
    }

    .search-button {
        border: none !important;
        font-size: 14px !important;
        padding: 10px 20px !important;
        border-radius: 20px !important;
        cursor: pointer !important;
        transition: background 0.3s ease !important;
    }

    .profile-section {
        display: flex;
        align-items: center;
        margin-left: 50px; /* Moves it slightly left to balance */
    }


    .profile-button {
        border-radius: 50%;
        border: none;
        background-color: transparent;
        cursor: pointer;
        padding: 0;
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .profile-button i {
        font-size: 24px;
        color: white;
    }

    .profile-name {
        font-size: 16px;
        font-weight: bold;
        margin-right: 20px; /* Increase spacing from the right */
    }

    .logout-button-container {
        position: fixed;
        bottom: 20px;
        left: 20px;
        width: 160px;
    }

""") as demo:

    with gr.Row(elem_classes="top-bar"):
        gr.Markdown("**NOMURA**", elem_classes="logo")
        
        with gr.Row(elem_classes="search-box-container", equal_height=True):
            search_input = gr.Textbox(placeholder="Search...", show_label=False, elem_classes="search-box")
            search_button = gr.Button("Search", elem_classes="search-button")
        
        with gr.Row(elem_classes="profile-section"):
            gr.HTML("""<button class="profile-button"><i class="fas fa-user-circle"></i></button>""")
            gr.Markdown("<span class='profile-name'>Welcome back!<br><b>Xavier Lee</b></span>")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Home")
            gr.Markdown("### Search")
            gr.Markdown("### Saved Documents")
            gr.Markdown("### Settings")

        with gr.Column(scale=4):
            gr.Markdown("### Upload your Document(s) here")
            file_uploader = gr.File(label="Upload your document", type="filepath")
            notes = gr.Textbox(placeholder="Write any comments you have about your document(s) here.")
            
            upload_button = gr.Button("Upload Document(s)", elem_id="upload-button")
            reset_button = gr.Button("Reset")

            output_text = gr.Textbox(label="Upload Status", interactive=False)
            upload_button.click(upload_file, inputs=[file_uploader, notes], outputs=output_text)

    with gr.Row(elem_classes="logout-button-container"):
        logout_button = gr.Button("Log out")

    search_button.click(search_action, inputs=[search_input], outputs=[])

demo.launch()
