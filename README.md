# RAG Application for Quiz Questions Generation

## Overview

**Quiz_Generator: Smarter Quizzes from Smarter Content**  
This application is built to transform your course materials into dynamic quiz questions using the power of **Retrieval-Augmented Generation (RAG)**. By combining your own content with advanced language models, it delivers questions that are both accurate and contextually rich.

Whether you're an **instructor crafting assessments** or a **student designing your own practice sets**, QuizGen makes the process intuitive and efficient.  
Just upload your materials → Let the RAG model work → Get high-quality, tailored quiz questions in seconds!

## Features

- **Document Loading**: Efficiently loads and processes documents from a specified directory.
- **Vector Space Creation**: Creates a vector space for document retrieval using embeddings.
- **Conversational Interface**: Interacts with users to generate quiz questions based on input queries.
- **Question Generation**: Generates exam-like questions.
- **Gradio interface**: provides and interactive chat through Gradio for better user experience.


## Requirements

The application requires Python 3.11 and the following packages:

- Langchain (including community modules)
- PyPdfReader
- OpenAI
- Ollama
- Gradio

Refer to `requirements.txt` for a complete list of dependencies.

## Usage /  Getting Started

1. Clone the repository.
2. **Set Up Environment**: Install the required packages using `pip install -r requirements.txt`.
3. **Prepare your resource documents** in the pdf format and add them to one folder inside your project directory.
4. **Run Application**: Execute the main script using `python main.py`.
5. **Interact**: Use the conversational interface, at 'http://127.0.0.1:7860' by default, to generate quiz questions by providing a query related to your course material.
6. **Exit**: Type 'exit' to terminate the application.

## File Structure
The root folder of the project contains:
- `main.py`: The entry point of the application.
- `src`: Contains the core modules such as `DataLoader`, `VectorSpaceCreator`, and `ChatModel`.
- `Questions_resources` directory stores the course material.
- `vector_db` directory stores the vectorized database used for generating the quiz questions. 

## Models
This project uses free modules from the LangChain community:
- **Embedding**: the `sentence-transformers/all-MiniLM-L6-v2` is employed to represent your documents in a semantic format, making it easier to retrieve the most relevant parts.
-**Text Generation**: the `llama3.2` is used produce contextually quiz questions based on the retrieved information.

## Gradio Interface
The application also offers a Gradio interface for a more interactive and user-friendly experience. To access the interface, simply run the following command in your terminal inside your project folder: `python main.py`

