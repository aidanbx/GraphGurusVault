import os
import json
import string
from itertools import chain
import openai
import nltk
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

openai.api_key = os.environ["OPENAI_API_KEY"]


# tenacity helps with rate limits
# checkout here: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_handle_rate_limits.ipynb
@retry(wait=wait_random_exponential(min=5, max=60), stop=stop_after_attempt(10))
def createEmbedding(block):
    # returns array of size 1536
    return openai.Embedding.create(input = [block], model="text-embedding-ada-002")['data'][0]['embedding']

def preprocessText(text):
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    cleanText = [nltk.word_tokenize(s.translate(str.maketrans('', '', string.punctuation))) for par in text.split("\n\n") for s in sent_tokenizer.tokenize(par.strip())]
    return ' '.join(chain.from_iterable(cleanText))

def walkDir(path):
    # recursively walk through dir to get all markdown files
    # returns a dictionary where {filename1: content1, filename2: content2, ...}
    embeddings = {}
    # only getting a subset of the directories and files because it's a lot
    for item in os.listdir(path):
        print(item)
        content = os.path.join(path, item)
        if os.path.isdir(content):
            embeddings.update(walkDir(content))
        elif content.endswith(".md"):
            fp = open(content)
            fContent = preprocessText(fp.read())
            embeddings[item] = createEmbedding(fContent)
            fp.close()
    return embeddings

def getAllEmbeddings():
    embeddings = walkDir("./my-second-brain")
    with open('./embeddings.json', 'w') as fp:
        json.dump(embeddings, fp)

if __name__ == "__main__":
    getAllEmbeddings()