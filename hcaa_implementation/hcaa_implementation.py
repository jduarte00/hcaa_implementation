from scipy.cluster.hierarchy import linkage
import numpy as np
import scipy.spatial.distance as ssd

# Auxiliary function to get the node_id and the capital allocation for each cluster
def get_levels(n_clusters: int, n_filas: int, mat_Z: np.matrix):
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

# Auxiliary function to get the assets id's of each cluster 
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

# function to the appropiate number of groups given a cutoff point
def get_groups(Z_mat: np.matrix, cutoff_point: float)->int:
    distances = Z_mat[:,2]
    number_groups = int(distances.shape[0] - (sum(distances <= cutoff_point)) +1)
    return number_groups


# function to get the weight of the cluster.
def hcaa_alocation(mat_X: np.matrix, n_clusters:int = 0, custom_corr =np.corrcoef ,inverse_data = True, cutoff_point: float = None)->tuple:
    # Convertir matriz de datos en matriz de distancias
    if not inverse_data:
        E_matrix = custom_corr(mat_X)
    else:    
        E_matrix = custom_corr(mat_X.T)
    D_matrix = np.sqrt(2*(1- E_matrix))
    D_matrix = np.around(D_matrix, decimals=7)
    D_condensed = ssd.squareform(D_matrix)
    Z = linkage(D_condensed, 'ward', optimal_ordering = True)
    if cutoff_point:
        n_clusters = get_groups(Z, cutoff_point)
    n_filas = mat_X.shape[1]
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
            asset_weight = round(cluster_weight/len(assets), 6)
            index_asset += assets
            capital_all += [asset_weight] *len(assets)
    return (index_asset, capital_all)




    