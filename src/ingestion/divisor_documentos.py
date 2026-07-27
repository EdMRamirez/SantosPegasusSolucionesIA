from langchain_text_splitters import RecursiveCharacterTextSplitter

class DivisorDocumentos:
    def dividir(self, documentos):
        splitter = RecursiveCharacterTextSplitter(

            chunk_size=800,
            chunk_overlap=150,
            separators=[
                "\n\n",
                "\n",
                ".",
                " ",
                ""
            ]
        )

        return splitter.split_documents(documentos)