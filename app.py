import gradio as gr

from backend import get_images, create_image_variation

# inputs: textbox, button,
# output: gallery

with gr.Blocks() as demo:
    with gr.Column():
        with gr.Row():
            # prompt textbox
            textbox = gr.Textbox(
                show_label=False, placeholder="Please enter a prompt message"
            )
            # generate image button 
            img_gen_button = gr.Button(value="Generate images")
        # slider
        slider = gr.Slider(
            minimum=1, maximum=6, step=1, label="Number of images to generate", value=1
        )

        # upload image for creating image variations 
        image = gr.Image(shape=(128, 128), source="upload", type="filepath")
        # create image variation button 
        img_variation_button = gr.Button(value="Create variations from image")

        # gallery output 
        gallery = gr.Gallery(
            height="auto",
            object_fit="contain",
            show_label=False,
        )

    # generate image
    img_gen_button.click(fn=get_images, inputs=[textbox, slider], outputs=gallery)
    
    # create image variation 
    img_variation_button.click(fn=create_image_variation, inputs=[image, slider], outputs=gallery)


if __name__ == "__main__":
    demo.launch()
