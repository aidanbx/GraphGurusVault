import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

def get_embedding(block):
    # returns array of size 1536
    return openai.Embedding.create(input = [block], model="text-embedding-ada-002")['data'][0]['embedding']

def extract_mds(path):
    # walk through dir to get all markdown files
    # returns a dictionary where {filename1: content1, filename2: content2, ...}
    pass




# Define the text to be embedded
text = "This is a sample text."
word_embeddings = get_embedding(text)
print(len(word_embeddings))