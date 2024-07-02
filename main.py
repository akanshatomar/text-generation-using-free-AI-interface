from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import chroma
#from groq import Groq
# client = Groq(
#     api_key="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"
#     ) 
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader
import os
import nltk 
import magic