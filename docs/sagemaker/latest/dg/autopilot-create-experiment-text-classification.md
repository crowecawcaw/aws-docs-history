

# Create an AutoML job for text classification using the API
<a name="autopilot-create-experiment-text-classification"></a>

The following instructions show how to create an Amazon SageMaker Autopilot job as a pilot experiment for text classification problem types using SageMaker [API Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-reference.html).

**Note**  
Tasks such as text and image classification, time-series forecasting, and fine-tuning of large language models are exclusively available through the version 2 of the [AutoML REST API](autopilot-reference.md). If your language of choice is Python, you can refer to [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_auto_ml_job_v2.html) or the [AutoMLV2 object](https://sagemaker.readthedocs.io/en/stable/api/training/automlv2.html#sagemaker.automl.automlv2.AutoMLV2) of the Amazon SageMaker Python SDK directly.  
Users who prefer the convenience of a user interface can use [Amazon SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html) to access pre-trained models and generative AI foundation models, or create custom models tailored for specific text, image classification, forecasting needs, or generative AI.

You can create an Autopilot text classification experiment programmatically by calling the [`CreateAutoMLJobV2`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) API action in any language supported by Amazon SageMaker Autopilot or the AWS CLI.

For information on how this API action translates into a function in the language of your choice, see the [ See Also](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#API_CreateAutoMLJobV2_SeeAlso) section of `CreateAutoMLJobV2` and choose an SDK. As an example, for Python users, see the full request syntax of `[create\_auto\_ml\_job\_v2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job_v2)` in AWS SDK for Python (Boto3).

The following is a collection of mandatory and optional input request parameters for the `CreateAutoMLJobV2` API action used in text classification.

## Required parameters
<a name="text-classification-api-required-params"></a>

When calling `[CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html)` to create an Autopilot experiment for text classification, you must provide the following values:
+ An `[AutoMLJobName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#API_CreateAutoMLJobV2_RequestSyntax)` to specify the name of your job.
+ At least one `[AutoMLJobChannel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html)` in `[AutoMLJobInputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig)` to specify your data source.
+ An `[AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig)` of type `[TextClassificationJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextClassificationJobConfig.html)`. 
+ An `[OutputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html)` to specify the Amazon S3 output path to store the artifacts of your AutoML job.
+ A `[RoleArn](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-RoleArn)` to specify the ARN of the role used to access your data.

All other parameters are optional.

## Optional parameters
<a name="text-classification-api-optional-params"></a>

The following sections provide details of some optional parameters that you can pass to your text classification AutoML job.

### How to specify the training and validation datasets of an AutoML job
<a name="text-classification-data-training-or-validation"></a>

You can provide your own validation dataset and custom data split ratio, or let Autopilot split the dataset automatically.

Each [`AutoMLJobChannel`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html) object (see the required parameter [AutoMLJobInputDataConfig](https://docs.aws.amazon.com/sagemaker-api/src/AWSSageMakerAPIDoc/build/server-root/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig)) has a `ChannelType`, which can be set to either `training` or `validation` values that specify how the data is to be used when building a machine learning model. 

At least one data source must be provided and a maximum of two data sources is allowed: one for training data and one for validation data. How you split the data into training and validation datasets depends on whether you have one or two data sources. 

How you split the data into training and validation datasets depends on whether you have one or two data sources.
+ If you only have **one data source**, the `ChannelType` is set to `training` by default and must have this value.
  + If the `ValidationFraction` value in [`AutoMLDataSplitConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSplitConfig.html) is not set, 0.2 (20%) of the data from this source is used for validation by default. 
  + If the `ValidationFraction` is set to a value between 0 and 1, the dataset is split based on the value specified, where the value specifies the fraction of the dataset used for validation.
+ If you have **two data sources**, the `ChannelType` of one of the `AutoMLJobChannel` objects must be set to `training`, the default value. The `ChannelType` of the other data source must be set to `validation`. The two data sources must have the same format, either CSV or Parquet, and the same schema. You must not set the value for the `ValidationFraction` in this case because all of the data from each source is used for either training or validation. Setting this value causes an error.

### How to specify the automatic model deployment configuration for an AutoML job
<a name="text-classification-auto-model-deployment"></a>

To enable automatic deployment for the best model candidate of an AutoML job, include a `[ModelDeployConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-ModelDeployConfig)` in the AutoML job request. This will allow the deployment of the best model to a SageMaker AI endpoint. Below are the available configurations for customization.
+ To let Autopilotgenerate the endpoint name, set `[AutoGenerateEndpointName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployConfig.html#API_ModelDeployConfig_Contents)` to `True`.
+ To provide your own name for the endpoint, set `[AutoGenerateEndpointName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployConfig.html#API_ModelDeployConfig_Contents) to False and provide a name of your choice in [EndpointName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployConfig.html#API_ModelDeployConfig_Contents)`.