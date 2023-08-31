### HuggingFace and Gradio integration demo

The model trained in the [/training](./training) folder has been fine-tuned from a distilled version of BERT in order to classify articles by theme (business, politics, tech, entertainment, sport) and has been uploaded to: [https://huggingface.co/srinivajan/Classification](https://huggingface.co/srinivajan/Classification)

![Training Output on Colab](imgs/training_output.png "Training Output")


To try it, either run [demo.py](demo.py) and visit [http://127.0.0.1:7860](http://127.0.0.1:7860), or just run the single cell in the notebook [demo.ipynb](demo.ipynb)

![Example Inference](imgs/example_inference.png "Example of an inference on a short paragraph")