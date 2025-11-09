# Amazon SageMaker Feature Store resources

The following lists the available resources for Amazon SageMaker Feature Store users. For the Feature Store main page, see
[Amazon SageMaker Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/").

## Feature Store example notebooks and workshops

To get started using Amazon SageMaker Feature Store, you can choose from a variety of example Jupyter notebooks from
the following table. If this is your first time using Feature Store, try out the Introduction to Feature Store
notebook. To run any these notebooks, you must attach this policy to your IAM execution role:
`AmazonSageMakerFeatureStoreAccess`.

See [IAM Roles](https://console.aws.amazon.com/iam/home#/roles "https://console.aws.amazon.com/iam/home#/roles") to access your role and
attach this policy. For a walkthrough on how to view the policies attached to a role and how to
add a policy to your role, see [Adding policies to your IAM
role](feature-store-adding-policies.md "feature-store-adding-policies.md").

The following table lists a variety of resources to help you get started with Feature Store. This
table contains examples, instructions, and example notebooks to guide you in how to use Feature Store for
the first time to specific use cases. The code in these resources use the SageMaker AI SDK for Python (Boto3).

| **Page**                                                                                                                                                                                                                                                              | **Description**                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [Get<br>started with Amazon SageMaker Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/ "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/") in Read the Docs.                                     | A list of example notebooks to introduce you to Feature Store and its features to help you get<br>started.                                  |
| [Amazon SageMaker Feature Store guide](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_featurestore.html "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_featurestore.html") in Read the Docs.                                               | A Feature Store guide on how to set up, create a feature group, load data into a feature group,<br>and how to use Feature Store in general. |
| [Amazon SageMaker Feature Store end-to-end workshop](https://github.com/aws-samples/amazon-sagemaker-feature-store-end-to-end-workshop "https://github.com/aws-samples/amazon-sagemaker-feature-store-end-to-end-workshop") in the `aws-samples` Github<br>repository | An end-to-end Feature Store workshop.                                                                                                       |
| [Feature Store example notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-featurestore "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-featurestore") in the SageMaker AI example notebooks repository.            | Specific use case example notebooks for Feature Store.                                                                                      |

## Feature Store Python SDK and API

Python Software Development Kit (SDK) and Application Programming Interface (API) are tools
used for creating software applications. The Feature Store SDK for Python (Boto3) and API are listed in the following
table.

| **Page**                                                                                                                                                                                                                                                                                                                       | **Description**                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Feature Store<br>APIs](https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html "https://sagemaker.readthedocs.io/en/stable/api/prep_data/feature_store.html") in the Amazon SageMaker Python SDK Read the Docs                                                                                            | The Feature Store APIs in Read the Docs.                                                                                                                                  |
| [Feature Store Python SDK](https://github.com/aws/sagemaker-python-sdk/tree/master/src/sagemaker/feature_store "https://github.com/aws/sagemaker-python-sdk/tree/master/src/sagemaker/feature_store") in the Amazon SageMaker Python SDK Github repository                                                                     | The Feature Store Python SDK Github repository.                                                                                                                           |
| [Feature Store Runtime operations and data types](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime.html") in the SDK for Python (Boto3) documentation | Feature Store Runtime client that contains all data plane API operations and data types for<br>Feature Store.                                                             |
| [Amazon SageMaker Feature Store Runtime](../APIReference/Welcome.md#Welcome_Amazon_SageMaker_Feature_Store_Runtime "../APIReference/Welcome.md#Welcome_Amazon_SageMaker_Feature_Store_Runtime") in the Amazon SageMaker API Reference                                                                                          | Some feature group level actions supported by Feature Store. If the API operation or data type<br>you are looking for is not listed here, please use search in the guide. |
| [Amazon SageMaker Feature Store Runtime](../APIReference/API_Operations_Amazon_SageMaker_Feature_Store_Runtime.md "../APIReference/API_Operations_Amazon_SageMaker_Feature_Store_Runtime.md") in the Amazon SageMaker API Reference                                                                                            | Record level actions supported by Feature Store. If the API operation or data type you are<br>looking for is not listed here, please use search in the guide.             |
