import gradio as gr

from config import *
from model_inference import run_inference
from utils import clear, get_image_examples

# front-end
with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown(description)

    with gr.Row():
        model_name = gr.Textbox(label="image2image model", value=repo)
        device = gr.Dropdown(["cpu", "cuda"], value=device, label="Select Device")
    with gr.Tab(label="Image"):
        with gr.Row().style(equal_height=True):
            # input image
            with gr.Column():
                original_image = gr.State(Value=None)
                input_image = gr.Image(type="pil")
                radio = gr.inputs.Radio(
                    version_list, type="value",
                    default=version_list[0], label='version')

                with gr.Row():
                    clear_button = gr.Button("Clear")
                    button = gr.Button("Commit")

            # output image
            output_image = gr.Image(type='pil')

        image_examples = get_image_examples()
        example = gr.Examples(
            examples=image_examples,
            inputs=[input_image],
            outputs=[input_image],
        )

    clear_button.click(clear, inputs=None,
                       outputs=[input_image, output_image]
                       )
    button.click(run_inference,
                 inputs=[input_image, radio],
                 outputs=[output_image])
    demo.queue().launch(debug=True, enable_queue=True)
