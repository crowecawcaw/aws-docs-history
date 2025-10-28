# Feature Processing

with Spark ML and Scikit-learn

Before training a model with either Amazon SageMaker AI built-in algorithms or custom algorithms,
you can use Spark and scikit-learn preprocessors to transform your data and engineer
features.

## Feature Processing with Spark ML

You can run Spark ML jobs with [AWS
Glue](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md"), a serverless ETL (extract, transform, load) service, from your
SageMaker AI notebook. You can also connect to existing EMR clusters to run Spark ML jobs
with [Amazon EMR](../../../emr/latest/ManagementGuide/emr-what-is-emr.md "../../../emr/latest/ManagementGuide/emr-what-is-emr.md"). To do this, you need an AWS Identity and Access Management (IAM) role that grants
permission for making calls from your SageMaker AI notebook to AWS Glue.

###### Note

To see which Python and Spark versions AWS Glue supports, refer to [AWS Glue Release
Notes](../../../glue/latest/dg/release-notes.md "../../../glue/latest/dg/release-notes.md").

After engineering features, you package and serialize Spark ML jobs with MLeap
into MLeap containers that you can add to an inference pipeline. You don't need to
use externally managed Spark clusters. With this approach, you can seamlessly scale
from a sample of rows to terabytes of data. The same transformers work for both
training and inference, so you don't need to duplicate preprocessing and feature
engineering logic or develop a one-time solution to make the models persist. With
inference pipelines, you don't need to maintain outside infrastructure, and you can
make predictions directly from data inputs.

When you run a Spark ML job on AWS Glue, a Spark ML pipeline is serialized into
[MLeap](https://github.com/combust/mleap "https://github.com/combust/mleap") format. Then, you
can use the job with the [SparkML Model
Serving Container](https://github.com/aws/sagemaker-sparkml-serving-container "https://github.com/aws/sagemaker-sparkml-serving-container") in a SageMaker AI Inference Pipeline. _MLeap_ is a serialization format and execution engine for machine
learning pipelines. It supports Spark, Scikit-learn, and TensorFlow for training
pipelines and exporting them to a serialized pipeline called an MLeap Bundle. You
can deserialize Bundles back into Spark for batch-mode scoring or into the MLeap
runtime to power real-time API services.

For an example that shows how to feature process with Spark ML, see the [Train an ML Model using Apache Spark in Amazon EMR and deploy in SageMaker AI](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-python-sdk/sparkml_serving_emr_mleap_abalone "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-python-sdk/sparkml_serving_emr_mleap_abalone") sample
notebook.

## Feature Processing with

Scikit-Learn

You can run and package scikit-learn jobs into containers directly in Amazon SageMaker AI.
For an example of Python code for building a scikit-learn featurizer model that
trains on [Fisher's Iris
flower data set](http://archive.ics.uci.edu/ml/datasets/Iris "http://archive.ics.uci.edu/ml/datasets/Iris") and predicts the species of Iris based on morphological
measurements, see [IRIS Training and Prediction with Sagemaker Scikit-learn](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_iris "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_iris").
