---
layout: default
---

# Abstract
> Recently, the problem of imbalanced data is the focus of intense research of machine learning community. Following work tries to utilize an approach of transforming the data space into another where classification task may become easier. Paper contains a proposition of a tool, based on a photographic metaphor to build a classifier ensemble, combined with a random subspace approach. It is a naturally naive parallel, insensitive to a sample size, robust to dimension increase, which allows a regularization of feature space, to reduce the impact of biased classes. The proposed approach was evaluated on the basis of the computer experiments carried out on the benchmark datasets.

# Benchmark data
<canvas id="benchmark" height="40em" width="100%"></canvas>
<script>
var ctx_benchmark = document.getElementById("benchmark").getContext('2d');
var myChart = new Chart(ctx_benchmark, { type: 'bar', data: {"labels": ["balance", "ionosphere", "wisconsin", "yeast3"], "datasets": [{"data": ["0.736", "0.878", "0.970", "0.889"], "backgroundColor": ["#e53935", "#e53935", "#e53935", "#e53935"], "label": "ECE"}, {"data": ["0.771", "0.729", "0.949", "0.824"], "backgroundColor": ["#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8"], "label": "KNN"}, {"data": ["0.766", "0.862", "0.957", "0.557"], "backgroundColor": ["#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6"], "label": "GNB"}, {"data": ["0.721", "0.833", "0.911", "0.843"], "backgroundColor": ["#dce775", "#dce775", "#dce775", "#dce775"], "label": "DTC"}, {"data": ["0.640", "0.638", "0.500", "0.770"], "backgroundColor": ["#81c784", "#81c784", "#81c784", "#81c784"], "label": "MLP"}, {"data": ["0.781", "0.608", "0.954", "0.500"], "backgroundColor": ["#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d"], "label": "SVC"}]}, options: {"scales": {"yAxes": [{"ticks": {"max": 1, "min": 0}, "stacked": false, "display": true}]}} });
</script>
# Synthetic data
<canvas id="synthetic" height="40em" width="100%"></canvas>
<script>
var ctx_benchmark = document.getElementById("synthetic").getContext('2d');
var myChart = new Chart(ctx_benchmark, { type: 'bar', data: {"labels": ["syntetic5f", "syntetic10f", "syntetic20f", "syntetic50f", "syntetic100f", "syntetic200f"], "datasets": [{"data": ["0.955", "0.860", "0.880", "0.887", "0.890", "0.816"], "backgroundColor": ["#e53935", "#e53935", "#e53935", "#e53935", "#e53935", "#e53935"], "label": "ECE"}, {"data": ["0.927", "0.709", "0.562", "0.547", "0.561", "0.511"], "backgroundColor": ["#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8"], "label": "KNN"}, {"data": ["0.948", "0.845", "0.771", "0.775", "0.767", "0.623"], "backgroundColor": ["#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6"], "label": "GNB"}, {"data": ["0.924", "0.764", "0.699", "0.871", "0.788", "0.881"], "backgroundColor": ["#dce775", "#dce775", "#dce775", "#dce775", "#dce775", "#dce775"], "label": "DTC"}, {"data": ["0.926", "0.771", "0.722", "0.500", "0.789", "0.500"], "backgroundColor": ["#81c784", "#81c784", "#81c784", "#81c784", "#81c784", "#81c784"], "label": "MLP"}, {"data": ["0.716", "0.500", "0.500", "0.500", "0.500", "0.500"], "backgroundColor": ["#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d"], "label": "SVC"}]}, options: {"scales": {"yAxes": [{"ticks": {"max": 1, "min": 0}, "stacked": false, "display": true}]}} });
</script>
# Result tables
# `syntetic5f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.926|0.955
0.2|0.500|0.935|0.951|0.954
0.3|0.888|0.938|0.951|0.950
0.4|0.888|0.937|0.950|0.949
0.5|0.920|0.936|0.944|0.946

# `syntetic10f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.692|0.776
0.2|0.500|0.789|0.831|0.834
0.3|0.779|0.842|0.844|0.828
0.4|0.843|0.842|0.843|0.846
0.5|0.853|0.857|0.860|0.856

# `syntetic20f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.548|0.527
0.2|0.500|0.583|0.696|0.613
0.3|0.642|0.650|0.760|0.818
0.4|0.744|0.839|0.839|0.880
0.5|0.764|0.816|0.838|0.840

# `syntetic50f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.512|0.503
0.2|0.500|0.530|0.615|0.687
0.3|0.583|0.508|0.771|0.699
0.4|0.661|0.802|0.833|0.732
0.5|0.677|0.798|0.764|0.887

# `balance`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.653|0.699
0.2|0.500|0.653|0.699|0.701
0.3|0.690|0.705|0.704|0.720
0.4|0.690|0.730|0.735|0.736
0.5|0.724|0.732|0.730|0.728

# `ionosphere`

.  |4.0 | 8.0 |16.0 |32.0 
--:|---:|----:|----:|----:
0.1|0.50|0.500|0.500|0.863
0.2|0.50|0.763|0.842|0.859
0.3|0.50|0.794|0.863|0.878
0.4|0.50|0.824|0.797|0.840
0.5|0.71|0.740|0.757|0.752

# `wisconsin`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.927|0.957
0.2|0.500|0.955|0.965|0.964
0.3|0.959|0.968|0.969|0.969
0.4|0.958|0.967|0.968|0.970
0.5|0.967|0.966|0.970|0.970

# `yeast3`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.708|0.817
0.2|0.500|0.771|0.869|0.881
0.3|0.832|0.840|0.873|0.880
0.4|0.830|0.848|0.874|0.883
0.5|0.852|0.855|0.884|0.889

