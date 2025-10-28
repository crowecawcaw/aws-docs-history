# Apache Spark with Amazon SageMaker AI

Amazon SageMaker AI Spark is an open source Spark library that helps you build Spark machine learning
(ML) pipelines with SageMaker AI. This simplifies the integration of Spark ML stages with SageMaker AI
stages, like model training and hosting. For information about SageMaker AI Spark, see the [SageMaker AI Spark](https://github.com/aws/sagemaker-spark "https://github.com/aws/sagemaker-spark") GitHub repository. The
following topics provide information to learn how to use Apache Spark with SageMaker AI.

The SageMaker AI Spark library is available in Python and Scala. You can use SageMaker AI Spark to train
models in SageMaker AI using `org.apache.spark.sql.DataFrame` data frames in your Spark
clusters. After model training, you can also host the model using SageMaker AI hosting services.

The SageMaker AI Spark library, `com.amazonaws.services.sagemaker.sparksdk`, provides
the following classes, among others:

- `SageMakerEstimator`—Extends the
  `org.apache.spark.ml.Estimator` interface. You can use this estimator
  for model training in SageMaker AI.
- `KMeansSageMakerEstimator`, `PCASageMakerEstimator`, and
  `XGBoostSageMakerEstimator`—Extend the
  `SageMakerEstimator` class.
- `SageMakerModel`—Extends the
  `org.apache.spark.ml.Model` class. You can use this
  `SageMakerModel` for model hosting and getting inferences in
  SageMaker AI.
  You can download the source code for both Python Spark (PySpark) and Scala libraries from
  the [SageMaker AI Spark](https://github.com/aws/sagemaker-spark "https://github.com/aws/sagemaker-spark") GitHub
  repository.

For installation and examples of the SageMaker AI Spark library, see [SageMaker AI Spark for Scala examples](apache-spark-example1.md "apache-spark-example1.md") or [Resources for using SageMaker AI Spark for
Python (PySpark) examples](apache-spark-additional-examples.md "apache-spark-additional-examples.md").

If you use Amazon EMR on AWS to manage Spark clusters, see [Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/"). For more information on using Amazon EMR in
SageMaker AI, see [Data preparation using Amazon EMR](studio-notebooks-emr-cluster.md "studio-notebooks-emr-cluster.md").

###### Topics

- [Integrate your Apache Spark application with
  SageMaker AI](#spark-sdk-common-process "#spark-sdk-common-process")
- [SageMaker AI Spark for Scala examples](apache-spark-example1.md "apache-spark-example1.md")
- [Resources for using SageMaker AI Spark for
  Python (PySpark) examples](apache-spark-additional-examples.md "apache-spark-additional-examples.md")

## Integrate your Apache Spark application with

SageMaker AI

The following is high-level summary of the steps for integrating your Apache Spark
application with SageMaker AI.

1. Continue data preprocessing using the Apache Spark library that you are
   familiar with. Your dataset remains a `DataFrame` in your Spark
   cluster. Load your data into a `DataFrame`. Preprocess it so that you
   have a `features` column with
   `org.apache.spark.ml.linalg.Vector` of `Doubles`, and
   an optional `label` column with values of
   `Double`​ type.
2. Use the estimator in the SageMaker AI Spark library to train your model. For example,
   if you choose the k-means algorithm provided by SageMaker AI for model training, call
   the `KMeansSageMakerEstimator.fit` method.

Provide your `DataFrame` as input. The estimator returns a
`SageMakerModel` object.

###### Note

`SageMakerModel` extends the
`org.apache.spark.ml.Model`.

The `fit` method does the following:

    1. Converts the input `DataFrame` to the protobuf format. It
     does so by selecting the `features` and
     `label` columns from the input
     `DataFrame`. It then uploads the protobuf data to
     an Amazon S3 bucket. The protobuf format is efficient for model training in
     SageMaker AI.
    2. Starts model training in SageMaker AI by sending a SageMaker AI [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") request. After model training
     has completed, SageMaker AI saves the model artifacts to an S3 bucket.


    SageMaker AI assumes the IAM role that you specified for model training to
     perform tasks on your behalf. For example, it uses the role to read
     training data from an S3 bucket and to write model artifacts to a
     bucket.
    3. Creates and returns a `SageMakerModel` object. The
     constructor does the following tasks, which are related to deploying
     your model to SageMaker AI.


    	1. Sends a [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") request to SageMaker AI.
    	2. Sends a [`CreateEndpointConfig`](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md") request to
    	 SageMaker AI.
    	3. Sends a [`CreateEndpoint`](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") request to SageMaker AI, which
    	 then launches the specified resources, and hosts the model on
    	 them.

3. You can get inferences from your model hosted in SageMaker AI with the
   `SageMakerModel.transform`.

Provide an input `DataFrame` with features as input. The
`transform` method transforms it to a `DataFrame`
containing inferences. Internally, the `transform` method sends a
request to the [`InvokeEndpoint`](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md") SageMaker API to get inferences. The
`transform` method appends the inferences to the input
`DataFrame`.
