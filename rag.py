import os

# use the new langchain-openai package for embeddings
from langchain_openai import OpenAIEmbeddings
# use LangChain’s ChatOpenAI instead of openai.ChatCompletion
from langchain.chat_models import ChatOpenAI

from langchain.document_loaders import WebBaseLoader, SitemapLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# ────────────────────────────
# 0. Configure your API key
# ────────────────────────────
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# ────────────────────────────
# 1. Load & chunk your docs
# ────────────────────────────
docs_shapes = WebBaseLoader("https://acegikmo.com/shapes/docs").load()
docs_unity  = SitemapLoader("https://docs.unity.com/sitemap.xml").load()
all_docs    = docs_shapes + docs_unity

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks   = splitter.split_documents(all_docs)

# ────────────────────────────
# 2. Embed & index chunks
# ────────────────────────────
embedder    = OpenAIEmbeddings(model="text-embedding-ada-002")
vectorstore = FAISS.from_documents(chunks, embedder)

# ────────────────────────────
# 3. Build a RetrievalQA chain
# ────────────────────────────
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",                      # “stuff” = concat all docs into one prompt
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
)

# ────────────────────────────
# 4. Ask a question (new style)
# ────────────────────────────
result = qa_chain({"query": "Can you give me a C# unity script that uses the shape assets library to make a red arrow"})
print(result["result"])
