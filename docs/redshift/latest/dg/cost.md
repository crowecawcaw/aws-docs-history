

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Costs for using Amazon Redshift ML
<a name="cost"></a>

With Amazon Redshift, you can leverage machine learning capabilities to gain insights from your data without the need for extensive data engineering or machine learning expertise. The following sections describe the costs associated with using Amazon Redshift ML, helping you plan and optimize your expenses while leveraging this powerful machine learning integration.

## Costs for using Amazon Redshift ML with SageMaker AI
<a name="cost_sm"></a>

Amazon Redshift ML for SageMaker AI uses your existing cluster resources for prediction so you can avoid additional Amazon Redshift charges. There is no additional Amazon Redshift charge for creating or using a model. Prediction happens locally in your Redshift cluster, so you don't have to pay extra unless you need to resize your cluster. Amazon Redshift ML uses Amazon SageMaker AI for training your model, which does have an additional associated cost.

There is no additional charge for prediction functions that run within your Amazon Redshift cluster. The CREATE MODEL statement uses Amazon SageMaker AI and incurs an additional cost. The cost increases with the number of cells in your training data. The number of cells is the product of the number of records (in the training query or table times) times the number of columns. For example, when a SELECT query of the CREATE MODEL statement creates 10,000 records and 5 columns, then the number of cells it creates is 50,000.

In some cases, the training data produced by the SELECT query of the CREATE MODEL exceeds the MAX\_CELLS limit that you provided (or the default 1 million if you didn't provide a limit). In these cases, CREATE MODEL randomly chooses approximately MAX\_CELLS (that is the “number of columns” records from the training dataset). CREATE MODEL then performs training using these randomly chosen tuples. The random sampling ensures that the reduced training dataset doesn't have any bias. Thus, by setting the MAX\_CELLS, you can control your training costs.

When using the CREATE MODEL statement, you can use the MAX\_CELLS and MAX\_RUNTIME options to control the costs, time, and potential model accuracy. 

MAX\_RUNTIME specifies the maximum amount of time the training can take in SageMaker AI when the AUTO ON or OFF option is used. Training jobs often complete sooner than MAX\_RUNTIME, depending on the size of the dataset. After a model is trained, Amazon Redshift does additional work in the background to compile and install your models in your cluster. Thus, CREATE MODEL can take longer than MAX\_RUNTIME to complete. However, MAX\_RUNTIME limits the amount of computation and time used in SageMaker AI to train your model. You can check the status of your model at any time using SHOW MODEL.

When you run CREATE MODEL with AUTO ON, Amazon Redshift ML uses SageMaker AI Autopilot to automatically and intelligently explore different models (or candidates) to find the best one. MAX\_RUNTIME limits the amount of time and computation spent. If MAX\_RUNTIME is set too low, there might not be enough time to explore even one candidate. If you see the error "Autopilot candidate has no models," rerun the CREATE MODEL with a larger MAX\_RUNTIME value. For more information about this parameter, see [MaxAutoMLJobRuntimeInSeconds](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.html) in the *Amazon SageMaker AI API Reference*.

When you run CREATE MODEL with AUTO OFF, MAX\_RUNTIME corresponds to a limit on how long the training job is run in SageMaker AI. Training jobs often complete sooner, depending on the size of the dataset and other parameters used, such as num\_rounds in MODEL\_TYPE XGBOOST.

You can also control costs or reduce training time by specifying a smaller MAX\_CELLS value when you run CREATE MODEL. A *cell* is an entry in the database. Each row corresponds to as many cells as there are columns, which can be of fixed or varying width. MAX\_CELLS limits the number of cells, and thus the number of training examples used to train your model. By default, MAX\_CELLS is set to 1 million cells. Reducing MAX\_CELLS reduces the number of rows from the result of the SELECT query in CREATE MODEL that Amazon Redshift exports and sends to SageMaker AI to train a model. Reducing MAX\_CELLS thus reduces the size of the dataset used to train models both with AUTO ON and AUTO OFF. This approach helps reduce the costs and time to train models. To see information about training and billing times of a specific training job, choose **Training jobs** in Amazon SageMaker AI.

Increasing MAX\_RUNTIME and MAX\_CELLS often improves model quality by allowing SageMaker AI to explore more candidates. This way, SageMaker AI can take more time to train each candidate and use more data to train better models. If you want faster iteration or exploration of your dataset, use lower MAX\_RUNTIME and MAX\_CELLS. If you want improved accuracy of models, use higher MAX\_RUNTIME and MAX\_CELLS.

For more information about costs associated with various cell numbers and free trial details, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing).

## Costs for using Amazon Redshift ML with Amazon Bedrock
<a name="cost_sm"></a>

Using Amazon Redshift ML with Amazon Bedrock incurs additional costs. For more information, see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/).