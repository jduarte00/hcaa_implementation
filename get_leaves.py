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