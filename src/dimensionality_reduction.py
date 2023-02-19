from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import json

def reduce_dimensions(vec_embeddings):
    pca = PCA(n_components=2)
    pca.fit(vec_embeddings)
    pca_encodings = pca.transform(vec_embeddings)
    return pca_encodings

def plot_space(labels, vectors):
    fig, ax = plt.subplots()
    x = vectors[:,0]
    y = vectors[:,1]
    ax.scatter(x, y)
    plt.rc('font', size=7)
    for i, label in enumerate(labels):
        ax.annotate(label, (x[i], y[i]))
    plt.show()

def runReduction():
    with open('embeddings.json','r') as infile:
        data = json.load(infile)
    embedding_labels = list(data.keys())
    embedding_size = len(data[embedding_labels[0]])
    embeddings = np.array([data[label] for label in embedding_labels])
    latent_space = reduce_dimensions(embeddings)
    plot_space(embedding_labels, latent_space)

if __name__ == '__main__':
    runReduction()