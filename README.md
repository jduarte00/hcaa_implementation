This package is a python implementation from the Hierarchical
Clustering-Based Asset Allocation (HCAA) method as introduced by Thomas Raffinot in The Journal of Portafolio Management in 2017 that can be found [here] (https://jpm.pm-research.com/content/44/2/89).

This method uses hierarchical aglomerative clustering to construct a dendogram that can later be used to distribute capital between groups of assets (Scikit learn is used to perform this clustering). This method is flexible enough to use different linkages, but this implementation uses Ward linkage, which is defined as follows: 

$$ d_{C_i, C_j} = \frac{m_i m_j}{m_i + m_j} || c_i - c_j||^2 $$

where $c_i$ and $c_j$ are the centroids of two clusters. 

This algorithm also requires the definition of a distance between assets in order to meassure similarities between them. The following distance between an asset $i$ and an asset $j$ was introduced by Mantegna in 1999 and is defined as follows:

$$ D_{i,j} = \sqrt{2 (1 - \rho_{i,j})}$$

where $\rho_{i.j}$ is the correlation between asset $i$ and asset $j$ calculated over the returns of both assets. This implementation uses the pearson correlation coefficient by default, but is also capable of using a custom correlation function (e.g. the RIE estimator, which I've also implemented in python and you can find in [here.](https://github.com/jduarte00/rie_estimator). 

Althought this is still some documentation missing, the implementation is complete, so feel free to use it and reach to me if you have any doubts, I'll be adding documentation and some usage examples in the future. 


