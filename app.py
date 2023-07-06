import gradio as gr

from backend import get_images

# inputs: textbox, button,
# output: gallery

with gr.Blocks() as demo:
    with gr.Column():
        with gr.Row():
            textbox = gr.Textbox(
                show_label=False, placeholder="Please enter a prompt message"
            )
            button = gr.Button(value="Generate images")
        slider = gr.Slider(
            minimum=0, maximum=6, step=1, label="Number of images to generate", value=1
        )
        gallery = gr.Gallery(
            height="auto",
            object_fit="contain",
            show_label=False,
        )

    button.click(fn=get_images, inputs=[textbox, slider], outputs=gallery)
