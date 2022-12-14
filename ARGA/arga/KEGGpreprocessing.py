import numpy as np
import pandas as pd
import scipy.sparse as sp
import pickle
import os

# read all csv files into one single dataframe
def read_all_csv(dataDirectory):
    data = pd.DataFrame()

    # Looping over all files inside the directory
    for filename in os.listdir(dataDirectory):
        f = os.path.join(dataDirectory, filename)
        if os.path.isfile(f):
            df = pd.read_csv(f, sep='\t')
            data = pd.concat([data, df])

    return data

def get_adj(data, dataset):
    # filter out all rows not starting with mmu
    data = data[data.entry1.str.match(dataset)]
    data = data[data.entry2.str.match(dataset)]

    nodes = set(data.entry1).union(set(data.entry2))
    nodesDict = dict(zip(nodes, range(len(nodes)))) # use dict for node index
    num_nodes = len(nodes)
    print('num nodes:', num_nodes)

    adj = np.zeros((num_nodes, num_nodes), dtype=int)

    for index, row in data.iterrows():
        ind1 = nodesDict[row['entry1']]
        ind2 = nodesDict[row['entry2']]
        adj[ind1][ind2] = 1
        adj[ind2][ind1] = 1

    return adj


# Change only in this line for a different dataset from mmu or hsa or rno
dataset = 'rno'


dataDirectory = 'kegg_pathways/gene_network_' + dataset
dfPickle = 'KEGG_pickles/' + dataset + '_df.pickle'
adjPickle = 'KEGG_pickles/' + dataset + '_adjacency.pickle'


# data = read_all_csv(dataDirectory)
# f = open(dfPickle, 'wb') # save the dataframe
# pickle.dump(data, f)
# f.close()

# f = open(dfPickle, 'rb') # read the saved dataframe
# data = pickle.load(f)

# adj = get_adj(data, dataset)
# f = open(adjPickle,'wb') # save the adj matrix
# pickle.dump(adj, f)
# f.close()


f = open(adjPickle, 'rb') # read the saved adj matrix
adj = pickle.load(f)
print(adj.shape)