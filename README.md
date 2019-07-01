<img src="cimcb_logo.png" alt="drawing" width="400"/>

# cimcb_vis
cimcb_vis package containing the necessary tools for the visualisation of correlated data.

## Installation

### Dependencies
cimcb_vis requires:
- Python (>=3.5)
- NumPy (>=1.12)
- SciPy
- scikit-learn
- Pandas
- matplotlib
- seaborn
- networks
- cimcb

### User installation
The recommend way to install cimcb_vis and dependencies is to using ``conda``:
```console
conda install -c brett.chapman cimcb_vis
```
or ``pip``:
```console
pip install cimcb_vis
```
Alternatively, to install directly from github:
```console
pip install https://github.com/brettChapman/cimcb_vis/archive/master.zip
```

### API
For further detail on the usage refer to the docstring.

#### cimcb_vis
- [Edge](https://github.com/brettChapman//cimcb_vis/blob/master/cimcb_vis/Edge.py): Generates dataframe of edges prior to visualisation.
- [Network](https://github.com/brettChapman//cimcb_vis/blob/master/cimcb_vis/Network.py) Generates dataframe of edges, with network parameters and a networkx graph prior to visualisation.
- [edgeBundle](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/edgeBundle.py): Generates necessary Json structure and produces Hierarchical edge bundle plot.
- [plotNetwork](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/plotNetwork.py): Static spring plot using pygraphviz and networkx.
- [forceNetwork](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/forceNetwork.py): Interactive spring plot which inherits data from the networkx graph
- [clustermap](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/clustermap.py): HCA with dendrograms.
- [polarDendrogram](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/polarDendrogram.py): Polar dendrogram

#### cimcb_vis.utils
- [mergeBlocks](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/utils/mergeBlocks.py): Merges multiply diffent blocks into a single peak table and data table.
- [range_scale](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/utils/range_scale.py): Scales a range of values between user chosen values.
- [corrAnalysis](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/corrAnalysis.py): Correlation analysis with Spearman or Pearson.
- [cluster](https://github.com/brettChapman/cimcb_vis/blob/master/cimcb_vis/utils/spatialClustering.py): Clusters data using a linkage cluster method. If the data is correlated the correlations are first preprocessed, then clustered, otherwise a distance metric is applied to non-correlated data before clustering.

### License
cimcb_vis is licensed under the ___ license.

### Authors
- Brett Chapman
- https://scholar.google.com.au/citations?user=A_wYNAQAAAAJ&hl=en

### Correspondence
Dr. Brett Chapman, Post-doctoral Research Fellow at the Centre for Integrative Metabolomics & Computational Biology at Edith Cowan University.
E-mail: brett.chapman@ecu.edu.au

### Citation
If you would cite cimcb_vis in a scientific publication, you can use the following: ___
