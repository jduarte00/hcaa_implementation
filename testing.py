
import pandas as pd
import hcaa_implementation
import csestimator
import rie_estimator
psi20 = pd.read_csv('/home/dum/Desktop/data/psi_20_returns.csv', index_col='Date')

def wrapper_function_cluster(X_matrix):
    return csestimator.get_shrinkage_est(X_matrix, alpha = 1)

lul = csestimator.get_shrinkage_est(psi20, alpha = 0.5)

index_assets_cluster, weight_assets_cluster = hcaa_implementation.hcaa_alocation(mat_X= psi20.values,n_clusters= 7, custom_corr= wrapper_function_cluster,inverse_data=False)
index_assets_rie, weight_assets_rie = hcaa_implementation.hcaa_alocation(mat_X= psi20.values,n_clusters= 7, custom_corr= rie_estimator.get_rie,inverse_data=False)

index_assets_corr, weight_assets_corr = hcaa_implementation.hcaa_alocation(mat_X= psi20.values,n_clusters= 7)

print(index_assets_cluster, weight_assets_cluster)
