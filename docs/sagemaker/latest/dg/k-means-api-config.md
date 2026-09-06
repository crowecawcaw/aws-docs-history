

# K-Means Hyperparameters
<a name="k-means-api-config"></a>

In the [`CreateTrainingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) request, you specify the training algorithm that you want to use. You can also specify algorithm-specific hyperparameters as string-to-string maps. The following table lists the hyperparameters for the k-means training algorithm provided by Amazon SageMaker AI. For more information about how k-means clustering works, see [How K-Means Clustering Works](algo-kmeans-tech-notes.md).


| Parameter Name | Description | 
| --- | --- | 
| feature\_dim | The number of features in the input data.<br />**Required**<br />Valid values: Positive integer | 
| k | The number of required clusters.<br />**Required**<br />Valid values: Positive integer | 
| epochs | The number of passes done over the training data.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 1 | 
| eval\_metrics | A JSON list of metric types used to report a score for the model. Allowed values are `msd` for Means Square Deviation and `ssd` for Sum of Square Distance. If test data is provided, the score is reported for each of the metrics requested.<br />**Optional**<br />Valid values: Either `[\"msd\"]` or `[\"ssd\"]` or `[\"msd\",\"ssd\"]` .<br />Default value: `[\"msd\"]` | 
| extra\_center\_factor | The algorithm creates K centers = `num_clusters` \* `extra_center_factor` as it runs and reduces the number of centers from K to `k` when finalizing the model.<br />**Optional**<br />Valid values: Either a positive integer or `auto`.<br />Default value: `auto` | 
| half\_life\_time\_size | Used to determine the weight given to an observation when computing a cluster mean. This weight decays exponentially as more points are observed. When a point is first observed, it is assigned a weight of 1 when computing the cluster mean. The decay constant for the exponential decay function is chosen so that after observing `half_life_time_size` points, its weight is 1/2. If set to 0, there is no decay.<br />**Optional**<br />Valid values: Non-negative integer<br />Default value: 0 | 
| init\_method | Method by which the algorithm chooses the initial cluster centers. The standard k-means approach chooses them at random. An alternative k-means\+\+ method chooses the first cluster center at random. Then it spreads out the position of the remaining initial clusters by weighting the selection of centers with a probability distribution that is proportional to the square of the distance of the remaining data points from existing centers.<br />**Optional**<br />Valid values: Either `random` or `kmeans++`.<br />Default value: `random` | 
| local\_lloyd\_init\_method | The initialization method for Lloyd's expectation-maximization (EM) procedure used to build the final model containing `k` centers.<br />**Optional**<br />Valid values: Either `random` or `kmeans++`.<br />Default value: `kmeans++` | 
| local\_lloyd\_max\_iter | The maximum number of iterations for Lloyd's expectation-maximization (EM) procedure used to build the final model containing `k` centers.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 300 | 
| local\_lloyd\_num\_trials | The number of times the Lloyd's expectation-maximization (EM) procedure with the least loss is run when building the final model containing `k` centers.<br />**Optional**<br />Valid values: Either a positive integer or `auto`.<br />Default value: `auto` | 
| local\_lloyd\_tol | The tolerance for change in loss for early stopping of Lloyd's expectation-maximization (EM) procedure used to build the final model containing `k` centers.<br />**Optional**<br />Valid values: Float. Range in [0, 1].<br />Default value: 0.0001 | 
| mini\_batch\_size | The number of observations per mini-batch for the data iterator.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 5000 | 