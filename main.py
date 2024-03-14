from flask import Flask, request, render_template, redirect, url_for
import os
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


os.environ['OPENAI_API_KEY'] = ""

app = Flask(__name__, static_url_path='/static')
app.secret_key = "secret"

UPLOAD_FOLDER = static_data_path = os.path.join(os.path.dirname(__file__), "uploads")
ALLOWED_EXTENSIONS = ['pdf']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_text_chunks():
    loader = PyPDFLoader(f"{UPLOAD_FOLDER}/{request.args['filename']}")
    data = loader.load()
    text_splitter = CharacterTextSplitter(
        separator= "\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    return text_splitter.split_documents(data)


@app.route("/", methods=['GET', 'POST'])
def upload_pdf_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for(".search_page", filename=filename))
    return render_template('pdf_downloader.html')


@app.route("/search", methods=['GET', 'POST'])
def search_page():
    data = get_text_chunks()
    if request.method == 'POST':
        query = request.form['question']
        embedding = OpenAIEmbeddings()
        docsearch = FAISS.from_documents(data, embedding)
        docs = docsearch.similarity_search(query)
        return docs[0].page_content
    return render_template('question_form.html')


# if __name__ == "__main__":
#     app.run(host="127.0.0.0", port=5000, debug=True)

