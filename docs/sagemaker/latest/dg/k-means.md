# K-Means Algorithm

K-means is an unsupervised learning algorithm. It attempts to find discrete groupings
within data, where members of a group are as similar as possible to one another and as
different as possible from members of other groups. You define the attributes that you want
the algorithm to use to determine similarity.

Amazon SageMaker AI uses a modified version of the web-scale k-means clustering algorithm. Compared
with the original version of the algorithm, the version used by Amazon SageMaker AI is more accurate.
Like the original algorithm, it scales to massive datasets and delivers improvements in
training time. To do this, the version used by Amazon SageMaker AI streams mini-batches (small, random
subsets) of the training data. For more information about mini-batch k-means, see [Web-scale k-means
Clustering](https://dl.acm.org/doi/10.1145/1772690.1772862 "https://dl.acm.org/doi/10.1145/1772690.1772862").

The k-means algorithm expects tabular data, where rows represent the observations that you
want to cluster, and the columns represent attributes of the observations. The _n_ attributes in each row represent a point in _n_-dimensional space. The Euclidean distance between these
points represents the similarity of the corresponding observations. The algorithm groups
observations with similar attribute values (the points corresponding to these observations
are closer together). For more information about how k-means works in Amazon SageMaker AI, see [How K-Means Clustering Works](algo-kmeans-tech-notes.md "algo-kmeans-tech-notes.md").

###### Topics

- [Input/Output Interface for the K-Means
  Algorithm](#km-inputoutput "#km-inputoutput")
- [EC2 Instance Recommendation for the K-Means
  Algorithm](#km-instances "#km-instances")
- [K-Means Sample Notebooks](#kmeans-sample-notebooks "#kmeans-sample-notebooks")
- [How K-Means Clustering Works](algo-kmeans-tech-notes.md "algo-kmeans-tech-notes.md")
- [K-Means Hyperparameters](k-means-api-config.md "k-means-api-config.md")
- [Tune a K-Means Model](k-means-tuning.md "k-means-tuning.md")
- [K-Means Response Formats](km-in-formats.md "km-in-formats.md")

## Input/Output Interface for the K-Means

Algorithm

For training, the k-means algorithm expects data to be provided in the
_train_ channel (recommended
`S3DataDistributionType=ShardedByS3Key`), with an optional
_test_ channel (recommended
`S3DataDistributionType=FullyReplicated`) to score the data on. Both
`recordIO-wrapped-protobuf` and `CSV` formats are supported
for training. You can use either File mode or Pipe mode to train models on data that is
formatted as `recordIO-wrapped-protobuf` or as `CSV`.

For inference, `text/csv`, `application/json`, and
`application/x-recordio-protobuf` are supported. k-means returns a
`closest_cluster` label and the `distance_to_cluster` for each
observation.

For more information on input and output file formats, see [K-Means Response Formats](km-in-formats.md "km-in-formats.md") for inference and the [K-Means Sample Notebooks](#kmeans-sample-notebooks "#kmeans-sample-notebooks"). The
k-means algorithm does not support multiple instance learning, in which the training set
consists of labeled “bags”, each of which is a collection of unlabeled instances.

## EC2 Instance Recommendation for the K-Means

Algorithm

We recommend training k-means on CPU instances. You can train on GPU instances, but
should limit GPU training to single-GPU instances (such as ml.g4dn.xlarge) because only one GPU is used per
instance. The k-means algorithm supports P2, P3, G4dn, and G5 instances for training and inference.

## K-Means Sample Notebooks

For a sample notebook that uses the SageMaker AI K-means algorithm to segment the population
of counties in the United States by attributes identified using principle component
analysis, see [Analyze US census data for population segmentation using Amazon SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/US-census_population_segmentation_PCA_Kmeans/sagemaker-countycensusclustering.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/US-census_population_segmentation_PCA_Kmeans/sagemaker-countycensusclustering.html").
For instructions how to create and access Jupyter notebook instances that you can use to
run the example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). Once you have
created a notebook instance and opened it, select the **SageMaker AI
Examples** tab to see a list of all the SageMaker AI samples. To open a notebook,
click on its **Use** tab and select **Create copy**.
