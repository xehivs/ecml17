---
layout: default
---

# Abstract
> Recently, the problem of imbalanced data is the focus of intense research of machine learning community. Following work tries to utilize an approach of transforming the data space into another where classification task may become easier. Paper contains a proposition of a tool, based on a photographic metaphor to build a classifier ensemble, combined with a random subspace approach. It is a naturally naive parallel, insensitive to a sample size, robust to dimension increase, which allows a regularization of feature space, to reduce the impact of biased classes. The proposed approach was evaluated on the basis of the computer experiments carried out on the benchmark datasets.

# Benchmark data

<canvas id="benchmark" height="40em" width="100%"></canvas>
<script>
var ctx_benchmark = document.getElementById("benchmark").getContext('2d');
var myChart = new Chart(ctx_benchmark, { type: 'bar', data: {"labels": ["balance", "yeast3", "wisconsin", "ionosphere"], "datasets": [{"data": ["0.736", "0.889", "0.970", "0.878"], "backgroundColor": ["#e53935", "#e53935", "#e53935", "#e53935"], "label": "ECE"}, {"data": ["0.774", "0.801", "0.945", "0.730"], "backgroundColor": ["#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8"], "label": "KNN"}, {"data": ["0.768", "0.558", "0.956", "0.837"], "backgroundColor": ["#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6"], "label": "GNB"}, {"data": ["0.727", "0.816", "0.901", "0.830"], "backgroundColor": ["#dce775", "#dce775", "#dce775", "#dce775"], "label": "DTC"}, {"data": ["0.640", "0.834", "0.500", "0.664"], "backgroundColor": ["#81c784", "#81c784", "#81c784", "#81c784"], "label": "MLP"}, {"data": ["0.778", "0.500", "0.951", "0.581"], "backgroundColor": ["#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d"], "label": "SVC"}]}, options: {"scales": {"yAxes": [{"ticks": {"max": 1, "min": 0}, "stacked": false, "display": true}]}} });
</script>
dataset   |features|classes|samples|ratio|             tags              
----------|-------:|------:|------:|-----|-------------------------------
balance   |       4|      3|    625|6:1  |multi-class imbalanced         
yeast3    |       8|      2|   1484|8:1  |binary multi-feature imbalanced
wisconsin |       9|      2|    699|2:1  |binary multi-feature           
ionosphere|      34|      2|    351|2:1  |binary multi-feature           




# `balance`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.653|0.699
0.2|0.500|0.653|0.699|0.701
0.3|0.690|0.705|0.704|0.720
0.4|0.690|0.730|0.735|0.736
0.5|0.724|0.732|0.730|0.728

# `yeast3`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.708|0.817
0.2|0.500|0.771|0.869|0.881
0.3|0.832|0.840|0.873|0.880
0.4|0.830|0.848|0.874|0.883
0.5|0.852|0.855|0.884|0.889

# `wisconsin`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.927|0.957
0.2|0.500|0.955|0.965|0.964
0.3|0.959|0.968|0.969|0.969
0.4|0.958|0.967|0.968|0.970
0.5|0.967|0.966|0.970|0.970

# `ionosphere`

.  |4.0 | 8.0 |16.0 |32.0 
--:|---:|----:|----:|----:
0.1|0.50|0.500|0.500|0.863
0.2|0.50|0.763|0.842|0.859
0.3|0.50|0.794|0.863|0.878
0.4|0.50|0.824|0.797|0.840
0.5|0.71|0.740|0.757|0.752

# Synthetic data

<canvas id="synthetic" height="40em" width="100%"></canvas>
<script>
var ctx_benchmark = document.getElementById("synthetic").getContext('2d');
var myChart = new Chart(ctx_benchmark, { type: 'bar', data: {"labels": ["syntetic5f", "syntetic10f", "syntetic20f", "syntetic50f"], "datasets": [{"data": ["0.955", "0.860", "0.880", "0.887"], "backgroundColor": ["#e53935", "#e53935", "#e53935", "#e53935"], "label": "ECE"}, {"data": ["0.924", "0.704", "0.559", "0.539"], "backgroundColor": ["#ba68c8", "#ba68c8", "#ba68c8", "#ba68c8"], "label": "KNN"}, {"data": ["0.948", "0.848", "0.748", "0.760"], "backgroundColor": ["#64b5f6", "#64b5f6", "#64b5f6", "#64b5f6"], "label": "GNB"}, {"data": ["0.917", "0.792", "0.679", "0.867"], "backgroundColor": ["#dce775", "#dce775", "#dce775", "#dce775"], "label": "DTC"}, {"data": ["0.936", "0.794", "0.705", "0.500"], "backgroundColor": ["#81c784", "#81c784", "#81c784", "#81c784"], "label": "MLP"}, {"data": ["0.739", "0.500", "0.500", "0.500"], "backgroundColor": ["#ffb74d", "#ffb74d", "#ffb74d", "#ffb74d"], "label": "SVC"}]}, options: {"scales": {"yAxes": [{"ticks": {"max": 1, "min": 0}, "stacked": false, "display": true}]}} });
</script>
dataset    |features|classes|samples|ratio|             tags              
-----------|-------:|------:|------:|-----|-------------------------------
syntetic5f |       5|      2|   1000|9:1  |binary imbalanced              
syntetic10f|      10|      2|   1000|8:1  |binary multi-feature imbalanced
syntetic20f|      20|      2|   1000|9:1  |binary multi-feature imbalanced
syntetic50f|      50|      2|   1000|9:1  |binary multi-feature imbalanced





---

<canvas id="synthetic2" height="40em" width="100%"></canvas>
<script>
var ctx_benchmark = document.getElementById("synthetic2").getContext('2d');
var myChart = new Chart(ctx_benchmark, { type: 'bar', data: {"labels": ["syntetic100f", "syntetic200f", "syntetic500f"], "datasets": [{"data": ["0.890", "0.816", "0.679"], "backgroundColor": ["#e53935", "#e53935", "#e53935"], "label": "ECE"}, {"data": ["0.549", "0.509", "0.510"], "backgroundColor": ["#ba68c8", "#ba68c8", "#ba68c8"], "label": "KNN"}, {"data": ["0.776", "0.630", "0.502"], "backgroundColor": ["#64b5f6", "#64b5f6", "#64b5f6"], "label": "GNB"}, {"data": ["0.778", "0.907", "0.666"], "backgroundColor": ["#dce775", "#dce775", "#dce775"], "label": "DTC"}, {"data": ["0.747", "0.500", "0.500"], "backgroundColor": ["#81c784", "#81c784", "#81c784"], "label": "MLP"}, {"data": ["0.500", "0.500", "0.500"], "backgroundColor": ["#ffb74d", "#ffb74d", "#ffb74d"], "label": "SVC"}]}, options: {"scales": {"yAxes": [{"ticks": {"max": 1, "min": 0}, "stacked": false, "display": true}]}} });
</script>
dataset     |features|classes|samples|ratio|             tags              
------------|-------:|------:|------:|-----|-------------------------------
syntetic100f|     100|      2|   1000|9:1  |binary multi-feature imbalanced
syntetic200f|     200|      2|   1000|9:1  |binary multi-feature imbalanced
syntetic500f|     500|      2|   1000|9:1  |binary multi-feature imbalanced




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

# `syntetic100f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.507|0.500
0.2|0.500|0.537|0.621|0.577
0.3|0.560|0.827|0.620|0.868
0.4|0.521|0.843|0.593|0.513
0.5|0.611|0.739|0.873|0.890

# `syntetic200f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.501|0.500
0.2|0.500|0.500|0.510|0.501
0.3|0.533|0.529|0.504|0.662
0.4|0.506|0.661|0.694|0.494
0.5|0.532|0.635|0.602|0.816

# `syntetic500f`

.  | 4.0 | 8.0 |16.0 |32.0 
--:|----:|----:|----:|----:
0.1|0.500|0.500|0.500|0.500
0.2|0.500|0.505|0.506|0.503
0.3|0.498|0.510|0.501|0.489
0.4|0.499|0.502|0.622|0.494
0.5|0.501|0.505|0.679|0.516

