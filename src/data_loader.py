from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from pypdf.errors import PdfReadError


class DataLoader:
    def __init__(
            self,
            folder: str = 'Questions_resources/',
            glob: str = '**/*.pdf'):
        self.documnets = None
        self.folder = folder
        self.glob_par = glob
        self.chunks = None

    def load_data(self):
        self.documents = []
        try:
            loader = DirectoryLoader(
                path=self.folder,
                glob=self.glob_par,
                loader_cls=PyPDFLoader,
                show_progress=True
            )
        except PdfReadError as e:
            print(f"Error reading PDF {e}")
        # Log the error or skip the file
        folder_docs = loader.load()
        for doc in folder_docs:
            self.documents.append(doc)
        print("Number of documents: ", len(self.documents))

    def remove_metadata(self):
        keys_to_remove = [
            'producer',
            'author',
            'creator',
            'creationdate',
            'moddate',
            'page_label'
        ]
        for doc in self.documents:
            for key in keys_to_remove:
                if key in doc.metadata:
                    del doc.metadata[key]
        print(self.documents[0].metadata)

    def generate_chunks(self,
                        chunk_s: int = 400,
                        chunk_o: int = 200):
        text_splitter = CharacterTextSplitter(chunk_size=chunk_s,
                                              chunk_overlap=chunk_o)
        self.chunks = text_splitter.split_documents(self.documents)
        print('*'*100)
        print("number of generated chuncks: ", len(self.chunks))
        print('*'*100)

    def get_chunks(self):
        if self.chunks is None:
            if self.documnets is None:
                self.load_data()
                self.remove_metadata()
            self.generate_chunks()
        return self.chunks
