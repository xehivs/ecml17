---
layout: default
---

# Abstract
> Recently, the problem of imbalanced data is the focus of intense research of machine learning community. Following work tries to utilize an approach of transforming the data space into another where classification task may become easier. Paper contains a proposition of a tool, based on a photographic metaphor to build a classifier ensemble, combined with a random subspace approach. It is a naturally naive parallel, insensitive to a sample size, robust to dimension increase, which allows a regularization of feature space, to reduce the impact of biased classes. The proposed approach was evaluated on the basis of the computer experiments carried out on the benchmark datasets.

# Benchmark data
<canvas id="benchmark" height="40em" width="100%"></canvas>
<script>
var ctx_benchmark = document.getElementById("benchmark").getContext('2d');
var myChart = new Chart(ctx_benchmark, { type: 'bar', data: {"labels": ["balance", "ionosphere", "wisconsin", "yeast3"], "datasets": [{"data": ["0.738", "0.834", "0.965", "0.907"], "backgroundColor": ["#e53935", "#e53935", "#e53935", "#e53935"], "label": "ECE"}, {"data": ["0.774", "0.730", "0.945", "0.801"], "backgroundColor": ["#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8"], "label": "KNN"}, {"data": ["0.768", "0.837", "0.956", "0.558"], "backgroundColor": ["#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6"], "label": "GNB"}, {"data": ["0.716", "0.848", "0.908", "0.819"], "backgroundColor": ["#dce775", "#dce775", "#dce775", "#dce775"], "label": "DTC"}, {"data": ["0.640", "0.664", "0.500", "0.834"], "backgroundColor": ["#81c784", "#81c784", "#81c784", "#81c784"], "label": "MLP"}, {"data": ["0.778", "0.581", "0.951", "0.500"], "backgroundColor": ["#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d"], "label": "SVC"}]}, options: {"scales": {"yAxes": [{"ticks": {"max": 1, "min": 0}, "stacked": false, "display": true}]}} });
</script>
# Synthetic data
<canvas id="synthetic" height="40em" width="100%"></canvas>
<script>
var ctx_benchmark = document.getElementById("synthetic").getContext('2d');
var myChart = new Chart(ctx_benchmark, { type: 'bar', data: {"labels": ["syntetic5f", "syntetic10f", "syntetic20f", "syntetic50f", "syntetic100f", "syntetic200f", "syntetic500f"], "datasets": [{"data": ["0.953", "0.855", "0.860", "0.906", "0.907", "0.868", "0.659"], "backgroundColor": ["#e53935", "#e53935", "#e53935", "#e53935", "#e53935", "#e53935", "#e53935"], "label": "ECE"}, {"data": ["0.924", "0.704", "0.559", "0.539", "0.549", "0.509", "0.510"], "backgroundColor": ["#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8"], "label": "KNN"}, {"data": ["0.948", "0.848", "0.748", "0.760", "0.776", "0.630", "0.502"], "backgroundColor": ["#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6"], "label": "GNB"}, {"data": ["0.918", "0.792", "0.670", "0.830", "0.785", "0.896", "0.661"], "backgroundColor": ["#dce775", "#dce775", "#dce775", "#dce775", "#dce775", "#dce775", "#dce775"], "label": "DTC"}, {"data": ["0.936", "0.794", "0.705", "0.500", "0.747", "0.500", "0.500"], "backgroundColor": ["#81c784", "#81c784", "#81c784", "#81c784", "#81c784", "#81c784", "#81c784"], "label": "MLP"}, {"data": ["0.739", "0.500", "0.500", "0.500", "0.500", "0.500", "0.500"], "backgroundColor": ["#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d"], "label": "SVC"}]}, options: {"scales": {"yAxes": [{"ticks": {"max": 1, "min": 0}, "stacked": false, "display": true}]}} });
</script>
# Result tables
# `syntetic5f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.930|0.953
0.2|0.500|0.937|0.950|0.951
0.3|0.943|0.938|0.949|0.951
0.4|0.943|0.943|0.946|0.947
0.5|0.836|0.941|0.943|0.944

# `syntetic10f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.756|0.824
0.2|0.500|0.782|0.855|0.852
0.3|0.837|0.854|0.844|0.851
0.4|0.837|0.843|0.853|0.850
0.5|0.843|0.836|0.849|0.849

# `syntetic20f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.595|0.836
0.2|0.500|0.734|0.833|0.810
0.3|0.813|0.833|0.844|0.856
0.4|0.819|0.833|0.860|0.839
0.5|0.734|0.849|0.840|0.851

# `syntetic50f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.570|0.826
0.2|0.500|0.503|0.859|0.841
0.3|0.606|0.851|0.794|0.906
0.4|0.711|0.901|0.843|0.905
0.5|0.858|0.785|0.890|0.858

# `balance`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.663|0.696
0.2|0.500|0.663|0.691|0.709
0.3|0.707|0.705|0.698|0.705
0.4|0.707|0.724|0.727|0.725
0.5|0.738|0.732|0.731|0.730

# `ionosphere`

.  |4.0 | 8.0 |16.0 |32.0 
--:|---:|----:|----:|----:
0.1|0.50|0.500|0.500|0.830
0.2|0.50|0.500|0.813|0.834
0.3|0.50|0.789|0.828|0.784
0.4|0.50|0.776|0.784|0.779
0.5|0.75|0.740|0.729|0.807

# `wisconsin`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.942|0.965
0.2|0.500|0.957|0.963|0.963
0.3|0.961|0.951|0.956|0.952
0.4|0.961|0.939|0.938|0.935
0.5|0.915|0.919|0.912|0.913

# `yeast3`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.834|0.880
0.2|0.500|0.819|0.900|0.907
0.3|0.802|0.815|0.898|0.899
0.4|0.790|0.773|0.880|0.889
0.5|0.574|0.670|0.856|0.841

