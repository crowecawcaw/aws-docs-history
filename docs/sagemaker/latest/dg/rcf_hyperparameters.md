

# RCF Hyperparameters
<a name="rcf_hyperparameters"></a>

In the [`CreateTrainingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) request, you specify the training algorithm. You can also specify algorithm-specific hyperparameters as string-to-string maps. The following table lists the hyperparameters for the Amazon SageMaker AI RCF algorithm. For more information, including recommendations on how to choose hyperparameters, see [How RCF Works](rcf_how-it-works.md).




| Parameter Name | Description | 
| --- | --- | 
| feature\_dim | The number of features in the data set. (If you use the [Random Cut Forest](https://sagemaker.readthedocs.io/en/stable/algorithms/unsupervised/randomcutforest.html) ModelTrainer, this value is calculated for you and need not be specified.)<br />**Required**<br />Valid values: Positive integer (min: 1, max: 10000) | 
| eval\_metrics | A list of metrics used to score a labeled test data set. The following metrics can be selected for output:+  `accuracy` - returns fraction of correct predictions. <br />+  `precision_recall_fscore` - returns the positive and negative precision, recall, and F1-scores. <br />**Optional**<br />Valid values: a list with possible values taken from `accuracy` or `precision_recall_fscore`. <br />Default value: Both `accuracy`, `precision_recall_fscore` are calculated. | 
| num\_samples\_per\_tree | Number of random samples given to each tree from the training data set.<br />**Optional**<br />Valid values: Positive integer (min: 1, max: 2048)<br />Default value: 256 | 
| num\_trees | Number of trees in the forest.<br />**Optional**<br />Valid values: Positive integer (min: 50, max: 1000)<br />Default value: 100 | 