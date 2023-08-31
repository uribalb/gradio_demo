import gradio as gr

demo = gr.load("srinivajan/Classification", src="models")

demo.launch()