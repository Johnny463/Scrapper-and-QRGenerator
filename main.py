import cv2
import numpy as np
import sys
import time

from langchain_community.vectorstores import DeepLake
from langchain_openai import OpenAIEmbeddings
from langchain.utilities import ApifyWrapper
from langchain.text_splitter import CharacterTextSplitter
#from langchain.document_loaders.base import Document
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# Set API tokens
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['ACTIVELOOP_TOKEN'] = os.getenv('ACTIVELOOP_TOKEN')
os.environ["APIFY_API_TOKEN"] = os.getenv('APIFY_API_TOKEN')


# We use crawler from ApifyWrapper(), which is available in Langchain
# For convenience, we set 20 maximum pages to crawl with a timeout of 300 seconds.
apify = ApifyWrapper()
loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={"startUrls": [{"url": "https://www.activeloop.ai/"}], "maxCrawlPages": 20},
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
    timeout_secs=300,
)

# Now the pages are loaded and split into chunks with a maximum size of 1000 tokens
pages = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator = ".")
docs = text_splitter.split_documents(pages)
print(docs)
activeloop_org = "johnny463"
# initialize the embedding model
embeddings = OpenAIEmbeddings()

# initialize the database, can also be used to load the database
db = DeepLake(
    dataset_path=f"hub://{activeloop_org}/scraped-websites",
    embedding=embeddings,
    overwrite=False,
)

# save the documents
db.add_documents(docs)

query_for_company = 'Business core of the company'

result = db.similarity_search(query_for_company, k=10)
print(result)
retriever = db.as_retriever(
    search_kwargs={"k":10}
)
llm = OpenAI(temperature=0.5)
query = "You are a prompt generator. Based on the content, write a detailed one sentence description that can be used to generate an image"

prompt_template = """{query}:

Content: {text}
"""

# set the prompt template
PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["text"],
    partial_variables={"query": query}
)
# Initialize the chain
chain = LLMChain(llm=llm, prompt=PROMPT)

# Filter the most relevant documents
result = db.similarity_search(query_for_company, k=10)
# Run the Chain
image_prompt = chain.invoke(result)
image_prompt = image_prompt["text"]
image_prompt

# qa = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type='stuff',
#     retriever=retriever
# )

# chain_answer = qa.invoke("Explain what is Deep Lake")
# chain_answer
answer = llm(prompt=PROMPT.format(text=image_prompt))
