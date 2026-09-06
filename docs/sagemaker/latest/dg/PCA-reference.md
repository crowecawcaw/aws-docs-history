

# PCA Hyperparameters
<a name="PCA-reference"></a>

In the `CreateTrainingJob` request, you specify the training algorithm. You can also specify algorithm-specific HyperParameters as string-to-string maps. The following table lists the hyperparameters for the PCA training algorithm provided by Amazon SageMaker AI. For more information about how PCA works, see [How PCA Works](how-pca-works.md). 


| Parameter Name | Description | 
| --- | --- | 
| feature\_dim | Input dimension.<br />**Required**<br />Valid values: positive integer | 
| mini\_batch\_size | Number of rows in a mini-batch.<br />**Required**<br />Valid values: positive integer | 
| num\_components | The number of principal components to compute.<br />**Required**<br />Valid values: positive integer | 
| algorithm\_mode | Mode for computing the principal components. <br />**Optional**<br />Valid values: *regular* or *randomized*<br />Default value: *regular* | 
| extra\_components | As the value increases, the solution becomes more accurate but the runtime and memory consumption increase linearly. The default, -1, means the maximum of 10 and `num_components`. Valid for *randomized* mode only.<br />**Optional**<br />Valid values: Non-negative integer or -1<br />Default value: -1 | 
| subtract\_mean | Indicates whether the data should be unbiased both during training and at inference. <br />**Optional**<br />Valid values: One of *true* or *false*<br />Default value: *true* | 