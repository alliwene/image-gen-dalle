import gradio as gr

from backend import get_images, create_image_variation

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

        image = gr.Image(shape=(80, 80), source="upload", type="filepath")
        image_button = gr.Button(value="Create variations from image")

        gallery = gr.Gallery(
            height="auto",
            object_fit="contain",
            show_label=False,
        )

    image_button.click(fn=create_image_variation, inputs=[image, slider], outputs=gallery)

    button.click(fn=get_images, inputs=[textbox, slider], outputs=gallery)


if __name__ == "__main__":
    demo.launch()
