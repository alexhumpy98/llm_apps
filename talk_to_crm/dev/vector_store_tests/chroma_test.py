from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma



embeddings = OpenAIEmbeddings(openai_api_key = "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")

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 200,
    chunk_overlap = 0
)

loader = TextLoader("facts.txt")

docs = loader.load_and_split(
    text_splitter = text_splitter
)

# creates chroma instance and calculates embeddings for all docs
db = Chroma.from_documents(
    docs, 
    embedding = embeddings,
    persist_directory = "embs_02" # persists embeddings in SQLite directory on computer
)

results = db.similarity_search( #Prompt is called to the db instance
    "What is an interesting fact about the English language",
    #k = 1 # Number of results you get back
    )


for result in results: # results returns an array of tuples (if you use similarity_search_with_score)
    print("\n")
    print(result.page_content)
    #print(result[1])
    #print(result[0].page_content)