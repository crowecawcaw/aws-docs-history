# Amazon SageMaker AI in AWS GovCloud (US)

Amazon SageMaker AI is a fully managed machine learning service. With Amazon SageMaker AI, data scientists and developers can quickly and easily build and train machine learning models, and then directly deploy them into a production-ready hosted environment. It provides an integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don’t have to manage servers. It also provides common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment. With native support for bring-your-own-algorithms and frameworks, Amazon SageMaker AI provides flexible distributed training options that adjust to your specific workflows.

###### Topics

- [How Amazon SageMaker AI differs for AWS GovCloud (US)](#govcloud-sm-diffs "#govcloud-sm-diffs")
- [Documentation for Amazon SageMaker AI](#govcloud-sm-docs "#govcloud-sm-docs")
- [Export-controlled content](#govcloud-sagemaker-itar "#govcloud-sagemaker-itar")

## How Amazon SageMaker AI differs for AWS GovCloud (US)

- Only the following features are available. API calls to unavailable features will fail with a 4xx message indicating "The requested operation is not supported in the called region".
  - Notebook instances
  - Training
  - Pipelines
  - SageMaker JumpStart
  - Hosting
  - Batch Transform
  - Processing
  - Neo
  - SageMaker Search
  - SageMaker Debugger and Profiler
  - Model Tuning
  - SageMaker Studio and Studio Classic
    - Authentication using AWS Identity and Access Management is supported; authentication using IAM Identity Center is not supported
    - Scheduling a notebook job is not supported
    - AWS Glue interactive sessions is supported only in AWS GovCloud (US-West)

  - SageMaker Studio notebooks

###### Note

SageMaker Jumpstart in GovCloud only provides support for open-weight models. You can only access SageMaker Jumpstart with SageMaker AI Python SDK.

## Documentation for Amazon SageMaker AI

[Amazon SageMaker AI documentation](https://aws.amazon.com/documentation/sagemaker/ "https://aws.amazon.com/documentation/sagemaker/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon SageMaker AI metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your NotebookInstances, NotebookInstanceLifecycleConfigs, Endpoints, Models, EndpointConfigs, TrainingJobs, HyperParameterTuningJobs, and BatchTransformJobs.

Do not enter export-controlled data in the following console fields:

    + NotebookInstance Name
    + NotebookInstanceLifecycleConfig Name
    + Model Name
    + Model Container Hostname
    + Model Environment names and values
    + Endpoint Name
    + Endpoint Config Name
    + Endpoint Config Production Variant names
    + Endpoint Config
    + TrainingJob Name
    + BatchTransformJob Name
    + Hyperparameter Names or values
    + Input Channel Name
    + Any resource tag or value
    + Names of any metrics emitted by algorithms
    + Names of any training or inference container environment variables
