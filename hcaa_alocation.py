from scipy.cluster.hierarchy import linkage
from sklearn.datasets import make_blobs
import numpy as np

def get_levels(n_clusters, n_filas, mat_Z):
    nodos_id = []
    nivel_nodo = []
    filas_Z = mat_Z.shape[0]
    current_bif = mat_Z[-1]
    nodos_id.append(int(current_bif[0]))
    nivel_nodo.append(.5)
    nodos_id.append(int(current_bif[1]))
    nivel_nodo.append(.5)
    current_level = 2
    while(current_level < n_clusters):
        id_cluster = filas_Z+n_filas-current_level
        current_bif = mat_Z[-current_level]
        index_of_id = nodos_id.index(id_cluster)
        new_weight = nivel_nodo[index_of_id] / 2
        del nivel_nodo[index_of_id]
        del nodos_id[index_of_id]
        nodos_id.append(int(current_bif[0]))
        nivel_nodo.append(new_weight)
        nodos_id.append(int(current_bif[1]))
        nivel_nodo.append(new_weight)
        current_level += 1
    return(nodos_id, nivel_nodo)

def get_leaves(id_nodo, mat_Z, n_filas):
    if id_nodo <= n_filas -1:
        return [id_nodo]
    fila_Z = mat_Z[id_nodo - n_filas]
    id_nodo_1 = int(fila_Z[0])
    id_nodo_2 = int(fila_Z[1])
    el_1 =0
    el_2 = 0
    if (id_nodo_1 <= n_filas-1) and(id_nodo_2 <= n_filas-1):
        return([id_nodo_1, id_nodo_2])
    elif (id_nodo_1 > n_filas-1)and(id_nodo_2 > n_filas-1):
        el_1 = get_leaves(id_nodo_1, mat_Z, n_filas)
        el_2 = get_leaves(id_nodo_2, mat_Z, n_filas)
        return(el_1 + el_2)
    elif (id_nodo_1 > n_filas-1):
        el_1 = get_leaves(id_nodo_1, mat_Z, n_filas)
        el_1.append(id_nodo_2)
        return(el_1)
    else:
        el_2 = get_leaves(id_nodo_2, mat_Z, n_filas)
        el_2.append(id_nodo_1)
        return(el_2)

def hcaa_alocation(mat_X, n_clusters):
    Z = linkage(mat_X, 'ward', optimal_ordering = True)
    n_filas = mat_X.shape[0]
    levels = get_levels(n_clusters, n_filas, Z)
    index_asset = []
    capital_all = []
    for index, node_id in enumerate(levels[0]):
        if node_id <= n_filas-1:
            index_asset.append(node_id)
            capital_all.append(levels[1][index])
        else:
            assets = get_leaves(node_id, Z, n_filas)
            cluster_weight = levels[1][index]
            asset_weight = round(cluster_weight/len(assets), 4)
            index_asset += assets
            capital_all += [asset_weight] *len(assets)
    return (index_asset, capital_all)

X = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0]]
X = np.asarray(X)

test, y = make_blobs(n_samples=10, centers=3, n_features=2, random_state=0)
print(hcaa_alocation(test, 3))
    