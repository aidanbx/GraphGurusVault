import openai
import os

openai.api_key = "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"

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