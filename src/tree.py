import numpy as np
import pandas as pd
import json
from sklearn.cluster import *
from scipy.cluster.hierarchy import dendrogram, linkage, to_tree
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import queue

class MyNode:
    def __init__(self):
        self.files= []
        self.left = None
        self.right = None
    def get_children(self):
        return len(self.files)

def get_data(embedding_file):
    f = open(embedding_file, "r")
    embeddings = json.load(f)
    f.close()
    vector_to_file = {}
    vectors = []
    for f in embeddings:
        vector_to_file[tuple(embeddings[f])] = f
        vectors.append(embeddings[f])
    return vectors, vector_to_file

def traverse_CF_tree2(tree, vector_names):
    if tree.is_leaf():
        new_node= MyNode()
        new_node.files.append(vector_names[tree.get_id()])
        return new_node
    else:
        new_node=MyNode()
        if tree.get_left() is not None:
            left = traverse_CF_tree2(tree.get_left(), vector_names)
            new_node.files += left.files
            new_node.left=left
        if tree.get_right() is not None:
            right = traverse_CF_tree2(tree.get_right(), vector_names)
            new_node.files += right.files
            new_node.right = right
        return new_node

def create_tree(vectors, vector_names):
    linked = linkage(vectors, 'single')
    rootnode = to_tree(linked)
    return traverse_CF_tree2(rootnode, vector_names)

def build_tree(embedding_file = "./embeddings.json"):
    vectors, vector_to_file = get_data(embedding_file)
    vectors_names = [vector_to_file[tuple(x)] for x in vectors]
    tree = create_tree(vectors, vectors_names)
    return tree

def get_centroid(files, df):
    centroid = df.loc[df['filename'].isin(files)][["x", "y"]].mean()
    centroid_x = centroid["x"]
    centroid_y = centroid["y"]
    return(centroid_x, centroid_y)

def get_all_centroids(tree, reduced_dim = "reduced_embeddings_2d.csv"):
    df = pd.read_csv(reduced_dim)
    q = queue.Queue()
    q.put(tree)
    q.put("M")
    levels = []
    centroids = []
    while not q.empty():
        val = q.get()
        if val == "M":
            levels.append(centroids)
            centroids = []
            if not q.empty():
                q.put("M")
        else:
            centroids.append(get_centroid(val.files, df))
            if val.left is not None:
                q.put(val.left)
            if val.right is not None:
                q.put(val.right)
    return levels

def main():
    tree = build_tree()
    print(get_all_centroids(tree))

if __name__ == "__main__":
    main()