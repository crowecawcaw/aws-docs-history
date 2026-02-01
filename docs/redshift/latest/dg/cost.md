Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Costs for using Amazon Redshift ML

With Amazon Redshift, you can leverage machine learning capabilities to gain insights from
your data without the need for extensive data engineering or machine learning expertise.
The following sections describe the costs associated with using Amazon Redshift ML, helping you
plan and optimize your expenses while leveraging this powerful machine learning integration.

## Costs for using Amazon Redshift ML with SageMaker AI

Amazon Redshift ML for SageMaker AI uses your existing cluster resources for prediction so you can avoid
additional Amazon Redshift charges. There is no additional Amazon Redshift charge for creating or using a
model. Prediction happens locally in your Redshift cluster, so you don't have to pay
extra unless you need to resize your cluster. Amazon Redshift ML uses Amazon SageMaker AI for training your
model, which does have an additional associated cost.

There is no additional charge for prediction functions that run within your Amazon Redshift
cluster. The CREATE MODEL statement uses Amazon SageMaker AI and incurs an additional cost. The cost
increases with the number of cells in your training data. The number of cells is the
product of the number of records (in the training query or table times) times the number of
columns. For example, when a SELECT query of the CREATE MODEL statement creates 10,000
records and 5 columns, then the number of cells it creates is 50,000.

In some cases, the training data produced by the SELECT query of the CREATE MODEL
exceeds the MAX_CELLS limit that you provided (or the default 1 million if you didn't
provide a limit). In these cases, CREATE MODEL randomly chooses approximately MAX_CELLS
(that is the “number of columns” records from the training dataset). CREATE MODEL then
performs training using these randomly chosen tuples. The random sampling ensures that the
reduced training dataset doesn't have any bias. Thus, by setting the MAX_CELLS, you
can control your training costs.

When using the CREATE MODEL statement, you can use the MAX_CELLS and MAX_RUNTIME options
to control the costs, time, and potential model accuracy.

MAX_RUNTIME specifies the maximum amount of time the training can take in SageMaker AI when the
AUTO ON or OFF option is used. Training jobs often complete sooner than MAX_RUNTIME,
depending on the size of the dataset. After a model is trained, Amazon Redshift does additional
work in the background to compile and install your models in your cluster. Thus, CREATE
MODEL can take longer than MAX_RUNTIME to complete. However, MAX_RUNTIME limits the amount
of computation and time used in SageMaker AI to train your model. You can check the status of your
model at any time using SHOW MODEL.

When you run CREATE MODEL with AUTO ON, Amazon Redshift ML uses SageMaker AI Autopilot to automatically
and intelligently explore different models (or candidates) to find the best one.
MAX_RUNTIME limits the amount of time and computation spent. If MAX_RUNTIME is set too low,
there might not be enough time to explore even one candidate. If you see the error
"Autopilot candidate has no models," rerun the CREATE MODEL with a larger MAX_RUNTIME
value. For more information about this parameter, see [MaxAutoMLJobRuntimeInSeconds](../../../sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.md "../../../sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.md") in the _Amazon SageMaker AI API Reference_.

When you run CREATE MODEL with AUTO OFF, MAX_RUNTIME corresponds to a limit on how long
the training job is run in SageMaker AI. Training jobs often complete sooner, depending on the size
of the dataset and other parameters used, such as num_rounds in MODEL_TYPE XGBOOST.

You can also control costs or reduce training time by specifying a smaller MAX_CELLS
value when you run CREATE MODEL. A _cell_ is an entry in
the database. Each row corresponds to as many cells as there are columns, which can be of
fixed or varying width. MAX_CELLS limits the number of cells, and thus the number of
training examples used to train your model. By default, MAX_CELLS is set to 1 million
cells. Reducing MAX_CELLS reduces the number of rows from the result of the SELECT query in
CREATE MODEL that Amazon Redshift exports and sends to SageMaker AI to train a model. Reducing MAX_CELLS
thus reduces the size of the dataset used to train models both with AUTO ON and AUTO OFF.
This approach helps reduce the costs and time to train models. To see information about
training and billing times of a specific training job, choose **Training
jobs** in Amazon SageMaker AI.

Increasing MAX_RUNTIME and MAX_CELLS often improves model quality by allowing SageMaker AI to
explore more candidates. This way, SageMaker AI can take more time to train each candidate and use
more data to train better models. If you want faster iteration or exploration of your
dataset, use lower MAX_RUNTIME and MAX_CELLS. If you want improved accuracy of models, use
higher MAX_RUNTIME and MAX_CELLS.

For more information about costs associated with various cell numbers and free trial
details, see [Amazon Redshift
pricing](https://aws.amazon.com/redshift/pricing "https://aws.amazon.com/redshift/pricing").

## Costs for using Amazon Redshift ML with Amazon Bedrock

Using Amazon Redshift ML with Amazon Bedrock incurs additional costs. For more information,
see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
