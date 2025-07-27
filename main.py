from src.vector_space_creator import VectorSpaceCreator
from src.data_loader import DataLoader
from src.chat_model import ChatModel
import gradio as gr

import warnings
warnings.filterwarnings("ignore")


def main():

    DL = DataLoader(folder='Questions_resources/',
                    glob='**/*.pdf')
    VSC = VectorSpaceCreator(DL=DL)
    # VSC.create_vector_sapce() #to rereate it from the documents
    vectorstore = VSC.get_vector_store()  # to load it if already exists

    chat = ChatModel(vectorstore)
    chat.init_chat()

    def chat_interface(user_input):
        if user_input.lower() == "exit":
            return "Exiting program as requested."
        res = chat.get_response(user_input)
        return res + "\n" + "-"*100 + "\nIs there anything else"\
            "I can help you with?"

    with gr.Blocks() as demo:
        gr.Markdown("## I am your Quiz Preparing Assistant")
        gr.Markdown("Type your question or topic below. Type `'exit'` to end"
                    " the session.")
        input_box = gr.Textbox(label="Your input",
                               placeholder="e.g., Generate two new exam-like"
                               " multiple-choice questions about DES, the data"
                               " encryption standard.")
        output_box = gr.Textbox(label="Response", lines=10)
        send_btn = gr.Button("Submit")

        send_btn.click(fn=chat_interface, inputs=input_box, outputs=output_box)
    demo.launch()


if __name__ == '__main__':
    main()
