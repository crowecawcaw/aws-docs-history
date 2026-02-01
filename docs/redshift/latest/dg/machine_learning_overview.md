Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Machine learning overview

With Amazon Redshift, you can leverage machine learning capabilities to gain valuable insights
from your data. This Machine Learning (ML) overview shows you how to explore, visualize, and
prepare your data for ML model training and deployment. The following sections will guide
you through the process of utilizing Amazon Redshift ML to unlock the potential of your data through
machine learning.

By using Amazon Redshift ML, you can train machine learning models using SQL statements and
invoke them in SQL queries for prediction.

To help you learn how to use Amazon Redshift ML, you can watch the following
video.

For information about the prerequisites for setting up your Redshift cluster or Serverless workgroup,
permissions, and ownership for using Amazon Redshift ML, read the following sections. These
sections also describe how simple training and predictions work in Amazon Redshift ML.

## How machine learning can solve a problem

A machine learning model generates predictions by finding patterns in your training
data and then applying these patterns to new data. In machine learning, you train these
models by learning the patterns that best explain your data. Then you use the models to
make predictions (also called inferences) on new data. Machine learning is typically an
iterative process where you can continue to improve the accuracy of the predictions by
changing parameters and improving your training data. If data changes, retraining new
models with the new dataset happens.

To address various business goals, there are different fundamental machine learning
approaches.

### Supervised learning in Amazon Redshift ML

Amazon Redshift supports supervised learning, which is the most common approach to
advanced enterprise analytics. Supervised learning is the preferred machine learning
approach when you have an established set of data and an understanding of how
specific input data predicts various business outcomes. These outcomes are sometimes
called labels. In particular, your dataset is a table with attributes that comprise
features (inputs) and targets (outputs). For example, suppose that you have a table
that provides the age and postal code for past and present customers. Suppose that
you also have a field “active” that is true for present customers and false for
customers who have suspended their membership. The goal of supervised machine
learning is to spot the patterns of age and postal code leading to customer churn, as
represented by customers whose targets are “False.” You can use this model to predict
customers who are likely to churn, such as suspending their membership, and
potentially offer retention incentives.

Amazon Redshift supports supervised learning that includes regression, binary
classification, and multiclass classification. Regression refers to the problem of
predicting continuous values, such as the total spending of customers. Binary
classification refers to the problem of predicting one of two outcomes, such as
predicting whether a customer churns or not. Multiclass classification refers to the
problem of predicting one of many outcomes, such as predicting the item a customer
might be interested. Data analysts and data scientists can use it to perform
supervised learning to tackle problems ranging from forecasting, personalization, or
customer churn prediction. You can also use supervised learning in problems such as
prediction of which sales will close, revenue prediction, fraud detection, and
customer life-time value prediction.

### Unsupervised learning in Amazon Redshift ML

Unsupervised learning uses machine learning algorithms to analyze and group
unlabeled training data. The algorithms discover hidden patterns or groupings. The
goal is to model the underlying structure or distribution in the data to learn more
about the data.

Amazon Redshift supports the K-Means clustering algorithm to solve an unsupervised
learning problem. This algorithm solves clustering problems where you want to
discover groupings in the data. The K-Means algorithm attempts to find discrete
groupings within the data. Unclassified data is grouped and partitioned based on its
similarities and differences. By grouping, the K-Means algorithm iteratively
determines the best centroids and assigns each member to the closest centroid.
Members nearest the same centroid belong to the same group. Members of a group are as
similar as possible to other members in the same group, and as different as possible
from members of other groups. For example, the K-Means clustering algorithm can be
used to classify cities impacted by a pandemic or classify cities based on the
popularity of consumer products.

When using the K-Means algorithm, you specify an input `k` that
specifies the number of clusters to find in the data. The output of this algorithm is
a set of k centroids. Each data point belongs to one of the k clusters that is
closest to it. Each cluster is described by its centroid. The centroid can be thought
of as the multi-dimensional average of the cluster. The K-Means algorithm compares
the distances to see how different the clusters are from each other. A larger
distance generally indicates a greater difference between the clusters.

Preprocessing the data is important for K-Means, as it ensures that the features
of the model stay on the same scale and produce reliable results. Amazon Redshift supports
some K-Means preprocessors for the CREATE MODEL statement, such as StandardScaler,
MinMax, and NumericPassthrough. If you don't want to apply any preprocessing for
K-means, choose NumericPassthrough explicitly as a transformer. For more information
about K-Means parameters, see [CREATE MODEL with K-MEANS
parameters](r_create_model_use_cases.md#r_k-means-create-model-parameters "r_create_model_use_cases.md#r_k-means-create-model-parameters").

To help you learn how to perform unsupervised training with
K-Means clustering, you can watch the following video.

## Terms and concepts for Amazon Redshift ML

The following terms are used to describe some Amazon Redshift ML concepts:

- _Machine learning_ in Amazon Redshift trains a model
  with one SQL command. Amazon Redshift ML and Amazon SageMaker AI manage all the data conversions,
  permissions, resource usage, and discovery of the proper model.
- _Training_ is the phase when Amazon Redshift creates
  a machine learning model by running a specified subset of data into the model.
  Amazon Redshift automatically launches a training job in Amazon SageMaker AI and generates a model.
- _Prediction_ (also called _inference_) is the use of the model in Amazon Redshift SQL
  queries to predict outcomes. At inference time, Amazon Redshift uses a model-based
  prediction function as part of a larger query to produce predictions. The
  predictions are computed locally, at the Redshift cluster, thus providing high
  throughput, low latency, and zero additional cost.
- With _bring your own model (BYOM)_, you can
  use a model trained outside of Amazon Redshift with Amazon SageMaker AI for in-database inference
  locally in Amazon Redshift. Amazon Redshift ML supports using BYOM in
  local inference.
- _Local inference_ is used when models are
  pretrained in Amazon SageMaker AI, compiled by Amazon SageMaker AI Neo, and localized in Amazon Redshift ML. To
  import models that are supported for local inference to Amazon Redshift, use the CREATE
  MODEL command. Amazon Redshift imports the pretrained SageMaker AI models by calling Amazon SageMaker AI
  Neo. You compile the model there and import the compiled model into Amazon Redshift. Use
  local inference for faster speed and lower costs.
- _Remote inference_ is used when Amazon Redshift
  invokes a model endpoint deployed in SageMaker AI. Remote inference provides the
  flexibility to invoke all types of custom models and deep learning models, such as
  TensorFlow models that you built and deployed in Amazon SageMaker AI.

Also important are the following:

- _Amazon SageMaker AI_ is a fully managed machine learning
  service. With Amazon SageMaker AI, data scientists and developers can easily build, train,
  and directly deploy models into a production-ready hosted environment. For
  information about Amazon SageMaker AI, see [What is Amazon SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md") in the
  _Amazon SageMaker AI Developer Guide_.
- _Amazon SageMaker AI Autopilot_ is a feature set that
  automatically trains and tunes the best machine learning models for classification
  or regression, based on your data. You maintain full control and visibility.
  Amazon SageMaker AI Autopilot supports input data in tabular format. Amazon SageMaker AI Autopilot
  provides automatic data cleaning and preprocessing, automatic algorithm selection
  for linear regression, binary classification, and multiclass classification. It
  also supports automatic hyperparameter optimization (HPO), distributed training,
  automatic instance, and cluster size selection. For information about Amazon SageMaker AI
  Autopilot, see [Automate
  model development with Amazon SageMaker AI Autopilot](../../../sagemaker/latest/dg/autopilot-automate-model-development.md "../../../sagemaker/latest/dg/autopilot-automate-model-development.md") in the
  _Amazon SageMaker AI Developer Guide_.
- _Amazon Bedrock_ is a fully managed service that offers a choice
  of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic,
  Cohere, Meta, Mistral AI, Stability AI, and Amazon via a single API, along with a broad set of
  capabilities needed to build generative AI applications.
