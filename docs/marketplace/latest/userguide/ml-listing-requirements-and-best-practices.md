# Requirements and best practices for

creating machine learning products

It is important that your buyers find it easy to test your model package and algorithm
products. The following sections describe best practices for ML products. For a complete summary
of requirements and recommendations, see the [Summary of requirements
and recommendations for ML product listings](#ml-summary-table-of-requirements-and-recommendations "#ml-summary-table-of-requirements-and-recommendations").

###### Note

An AWS Marketplace representative might contact you to help you meet these requirements if your
published products don't meet them.

###### Topics

- [General best practices for ML products](#ml-general-best-practices "#ml-general-best-practices")
- [Requirements for usage
  information](#ml-requirements-for-usage-information "#ml-requirements-for-usage-information")
- [Requirements for inputs and
  outputs](#ml-requirements-for-inputs-and-outputs "#ml-requirements-for-inputs-and-outputs")
- [Requirements for Jupyter
  notebook](#ml-requirements-for-jupyter-notebook "#ml-requirements-for-jupyter-notebook")
- [Summary of requirements
  and recommendations for ML product listings](#ml-summary-table-of-requirements-and-recommendations "#ml-summary-table-of-requirements-and-recommendations")

## General best practices for ML products

Provide the following information for your machine learning product:

- For product descriptions, include the following:
  - What your model does
  - Who the target customer is
  - What the most important use case is
  - How your model was trained or the amount of data that was used
  - What the performance metrics are and the validation data used
  - If medical, whether or not your model is for diagnostic use

- By default, machine learning products are configured to have public visibility.
  However, you can create a product with limited visibility. For more information, see [Step 7: Configure allowlist](configure-allowlist.md "configure-allowlist.md").
- (Optional) For paid products, offer a free trial of 14–30 days for customers
  to try your product. For more information, see [Machine learning product pricing for AWS Marketplace](machine-learning-pricing.md "machine-learning-pricing.md").

## Requirements for usage

information

Clear usage information that describes the expected inputs and outputs of your product
(with examples) is crucial for driving a positive buyer experience.

With each new version of your resource that you add to your product listing, you must
provide usage information.

To edit the existing usage information for a specific version, see [Updating version information](ml-manage-product-version.md#ml-updating-versions "ml-manage-product-version.md#ml-updating-versions").

## Requirements for inputs and

outputs

A clear explanation of supported input parameters and returned output parameters with
examples is important to help your buyers to understand and use your product. This
understanding helps your buyers to perform any necessary transformations on the input data to
get the best inference results.

You will be prompted for the following when adding your Amazon SageMaker AI resource to your product
listing.

### Inference inputs and outputs

For inference input, provide a description of the input data your product expects for
both real-time endpoint and batch transform job. Include code snippets for any necessary
preprocessing of the data. Include limitations, if applicable. Provide input samples hosted
on [GitHub](https://github.com "https://github.com").

For inference output, provide a description of the output data your product returns for
both real-time endpoint and batch transform job. Include limitations, if applicable. Provide
output samples hosted on [GitHub](https://github.com "https://github.com").

For samples, provide input files that work with your product. If your model performs
multiclass classification, provide at least one sample input file for each class.

### Training inputs

In the **Information to train a model** section, provide the input data
format and code snippets for any necessary preprocessing of the data. Include a description
of values and limitations, if applicable. Provide input samples hosted on [GitHub](https://github.com "https://github.com").

Explain both optional and mandatory features that can be provided by the buyer, and
specify whether the `PIPE` input mode is supported. If [distributed training](../../../sagemaker/latest/dg/your-algorithms-training-algo-running-container.md#your-algorithms-training-algo-running-container-dist-training "../../../sagemaker/latest/dg/your-algorithms-training-algo-running-container.md#your-algorithms-training-algo-running-container-dist-training") (training with more than 1 CPU/GPU instance) is supported,
specify this. For tuning, list the recommend hyperparameters.

## Requirements for Jupyter

notebook

When adding your SageMaker AI resource to your product listing, provide a link to a sample Jupyter
notebook hosted on [GitHub](https://github.com "https://github.com") that demonstrates the
complete workflow without asking the buyer to upload or find any data.

Use the AWS SDK for Python (Boto). A well-developed sample notebook makes it easier for buyers to try
and use your listing.

For model package products, your sample notebook demonstrates the preparation of input
data, creation of an endpoint for real-time inference, and performance of batch-transform
jobs. For more information, see [Model Package listing and Sample notebook](https://github.com/aws/amazon-sagemaker-examples/tree/main/aws_marketplace/curating_aws_marketplace_listing_and_sample_notebook/ModelPackage "https://github.com/aws/amazon-sagemaker-examples/tree/main/aws_marketplace/curating_aws_marketplace_listing_and_sample_notebook/ModelPackage") on GitHub. For a sample notebook, see
[auto_insurance](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/aws_marketplace/using_model_packages/auto_insurance "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/aws_marketplace/using_model_packages/auto_insurance"). The notebook works in all AWS Regions, without entering any
parameters and without a buyer needing to locate sample data.

###### Note

An underdeveloped sample Jupyter notebook that does not show multiple possible inputs
and data preprocessing steps might make it difficult for the buyer to fully understand your
product's value proposition.

For algorithm products, the sample notebook demonstrates complete training, tuning, model
creation, the creation of an endpoint for real-time inference, and the performance of
batch-transform jobs. For more information, see [Algorithm listing and Sample notebook](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/aws_marketplace/curating_aws_marketplace_listing_and_sample_notebook/Algorithm "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/aws_marketplace/curating_aws_marketplace_listing_and_sample_notebook/Algorithm") on GitHub. For sample notebooks, see [amazon_demo_product](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/aws_marketplace/using_algorithms/amazon_demo_product "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/aws_marketplace/using_algorithms/amazon_demo_product") and [automl](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/aws_marketplace/using_algorithms/automl "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/aws_marketplace/using_algorithms/automl") on GitHub. These sample notebooks work in all Regions without entering any
parameters and without a buyer needing to locate sample data.

###### Note

A lack of example training data might prevent your buyer from running the Jupyter
notebook successfully. An underdeveloped sample notebook might prevent your buyers from
using your product and hinder adoption.

## Summary of requirements

and recommendations for ML product listings

The following table provides a summary of the requirements and recommendations for a
machine learning product listing page.

| **Details**                                                                                                                                                                                                                                                                                                                    | **For model package listings** | **For algorithm listings**                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------- |
| **Product descriptions**                                                                                                                                                                                                                                                                                                       |                                | Explain in detail what the product does for supported content types (for example, “detects X in images").                                                                                                                                                                                    | Required | Required |
| Provide compelling and differentiating information about the product (avoid adjectives like "best" or unsubstantiated claims).                                                                                                                                                                                                 | Recommended                    | Recommended                                                                                                                                                                                                                                                                                  |
| List most important use case(s) for this product.                                                                                                                                                                                                                                                                              | Required                       | Required                                                                                                                                                                                                                                                                                     |
| Describe the data (source and size) it was trained on and list any known limitations.                                                                                                                                                                                                                                          | Required                       | Not applicable                                                                                                                                                                                                                                                                               |
| Describe the core framework that the model was built on.                                                                                                                                                                                                                                                                       | Recommended                    | Recommended                                                                                                                                                                                                                                                                                  |
| Summarize model performance metric on validation data (for example, "XX.YY percent accuracy benchmarked using the Z dataset").                                                                                                                                                                                                 | Required                       | Not applicable                                                                                                                                                                                                                                                                               |
| Summarize model latency and/or throughput metrics on recommended instance type.                                                                                                                                                                                                                                                | Required                       | Not applicable                                                                                                                                                                                                                                                                               |
| Describe the algorithm category. For example, “This decision forest regression algorithm is based on an ensemble of tree-structured classifiers that are built using the general technique of bootstrap aggregation and a random choice of features.”                                                                          | Not applicable                 | Required                                                                                                                                                                                                                                                                                     |
| **Usage information**                                                                                                                                                                                                                                                                                                          |                                | For inference, provide a description of the expected input format for both the real-time endpoint and batch transform job. Include limitations, if applicable. See [Requirements for inputs and outputs](#ml-requirements-for-inputs-and-outputs "#ml-requirements-for-inputs-and-outputs"). | Required | Required |
| For inference, provide input samples for both the real-time endpoint and batch transform job. Samples must be hosted on GitHub. See [Requirements for inputs and outputs](#ml-requirements-for-inputs-and-outputs "#ml-requirements-for-inputs-and-outputs").                                                                  | Required                       | Required                                                                                                                                                                                                                                                                                     |
| For inference, provide the name and description of each input parameter. Provide details about the its limitations and specify if it is required or optional.                                                                                                                                                                  | Recommended                    | Recommended                                                                                                                                                                                                                                                                                  |
| For inference, provide details about the output data your product returns for both the real-time endpoint and batch transform job. Include any limitations, if applicable. See [Requirements for inputs and outputs](#ml-requirements-for-inputs-and-outputs "#ml-requirements-for-inputs-and-outputs").                       | Required                       | Required                                                                                                                                                                                                                                                                                     |
| For inference, provide output samples for both the real-time endpoint and batch transform job. Samples must be hosted on GitHub. See [Requirements for inputs and outputs](#ml-requirements-for-inputs-and-outputs "#ml-requirements-for-inputs-and-outputs").                                                                 | Required                       | Required                                                                                                                                                                                                                                                                                     |
| For inference, provide an example of using an endpoint or batch transform job. Include a code example using the AWS Command Line Interface (AWS CLI) commands or using an AWS SDK.                                                                                                                                             | Required                       | Required                                                                                                                                                                                                                                                                                     |
| For inference, provide the name and description of each output parameter. Specify if it is always returned.                                                                                                                                                                                                                    | Recommended                    | Recommended                                                                                                                                                                                                                                                                                  |
| For training, provide details about necessary information to train the model such as minimum rows of data required. See [Requirements for inputs and outputs](#ml-requirements-for-inputs-and-outputs "#ml-requirements-for-inputs-and-outputs").                                                                              | Not applicable                 | Required                                                                                                                                                                                                                                                                                     |
| For training, provide input samples hosted on GitHub. See [Requirements for inputs and outputs](#ml-requirements-for-inputs-and-outputs "#ml-requirements-for-inputs-and-outputs").                                                                                                                                            | Not applicable                 | Required                                                                                                                                                                                                                                                                                     |
| For training, provide an example of performing training jobs. Describe the supported hyperparameters, their ranges, and their overall impact. Specify if the algorithm supports hyperparameter tuning, distributed training, or GPU instances. Include code example such as AWS CLI commands or using an AWS SDK, for example. | Not applicable                 | Required                                                                                                                                                                                                                                                                                     |
| Provide a Jupyter notebook hosted on GitHub demonstrating complete use of your product. See [Requirements for Jupyter notebook](#ml-requirements-for-jupyter-notebook "#ml-requirements-for-jupyter-notebook").                                                                                                                | Required                       | Required                                                                                                                                                                                                                                                                                     |
| Provide technical information related to the usage of the product, including user manuals and sample data.                                                                                                                                                                                                                     | Recommended                    | Recommended                                                                                                                                                                                                                                                                                  |
