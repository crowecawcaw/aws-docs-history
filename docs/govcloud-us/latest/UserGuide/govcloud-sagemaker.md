

# Amazon SageMaker AI in AWS GovCloud (US)
<a name="govcloud-sagemaker"></a>

{smlong} is a fully managed machine learning service. With {smlong}, data scientists and developers can quickly and easily build and train machine learning models, and then directly deploy them into a production-ready hosted environment. It provides an integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don’t have to manage servers. It also provides common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment. With native support for bring-your-own-algorithms and frameworks, {smlong} provides flexible distributed training options that adjust to your specific workflows.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon SageMaker AI differs
<a name="govcloud-sm-diffs"></a>

The following differences apply to Amazon SageMaker AI:
+ Only the following features are available. API calls to unavailable features will fail with a 4xx message indicating "The requested operation is not available in the called region".
  + Notebook instances
  + Training
  + Pipelines
  + SageMaker JumpStart
  + Hosting
  + Batch Transform
  + Processing
  + Neo
  + SageMaker Search
  + SageMaker Debugger and Profiler
  + Model Tuning
  + SageMaker Studio and Studio Classic
    + Authentication using AWS Identity and Access Management is supported; authentication using IAM Identity Center is not available
    + Scheduling a notebook job is not available
    +  AWS Glue interactive sessions is supported only in AWS GovCloud (US-West) 
  + SageMaker Studio notebooks
  +  AWS Deep Learning Containers (DLC) - Images are published to private Amazon ECR registries. The registry account differs by Region and image type. Use the following information to authenticate to the applicable registry and construct image URIs:
    + Registry accounts:
      + Deep Learning Containers framework images (for example, `base` and vLLM):

         AWS GovCloud (US-West) - `442386744353.dkr.ecr.us-gov-west-1.amazonaws.com` 

         AWS GovCloud (US-East) - `446045086412.dkr.ecr.us-gov-east-1.amazonaws.com` 
      +  `sagemaker-scikit-learn` and `sagemaker-xgboost`:

         AWS GovCloud (US-West) - `414596584902.dkr.ecr.us-gov-west-1.amazonaws.com` 

         AWS GovCloud (US-East) - `237065988967.dkr.ecr.us-gov-east-1.amazonaws.com` 
    + ECR login - authenticate to the applicable account from the preceding list. For example, for the framework account in AWS GovCloud (US-West):

      ```
      aws ecr get-login-password --region us-gov-west-1 | docker login --username AWS --password-stdin 442386744353.dkr.ecr.us-gov-west-1.amazonaws.com
      ```
    + Image URI format:

      ```
      <ACCOUNT>.dkr.ecr.<REGION>.amazonaws.com/<REPOSITORY>:<TAG>
      ```

      For example, the `sagemaker-xgboost` repository with the tag `3.0-5` in AWS GovCloud (US-West):

      ```
      414596584902.dkr.ecr.us-gov-west-1.amazonaws.com/sagemaker-xgboost:3.0-5
      ```
    + Available tags - only mutable tags are available in these Regions. A mutable tag can be repointed to a newer image when a version is patched or updated, so pulling the same tag at a later date may return different image content. Immutable tags, which pin to a fixed, unchanging build, are generally not published, apart from a few exceptions required by specific consumers (for example, the vLLM `-v1.x` SageMaker tags). To illustrate the mutable-tag scheme:
      + Ubuntu-based vLLM - available tags: `0.25.1-gpu-py312-cu130-ubuntu22.04-ec2`, `0.25.1-gpu-py312-ec2`. Immutable tags such as `0.25.1-gpu-py312-cu130-ubuntu22.04-ec2-v1.2-2026-07-20-21-30-05` and `0.25-gpu-py312-cu130-ubuntu22.04-ec2-v1` are not available.
      + AL2023-based vLLM - available tags: `server-cuda-v2.1`, `server-cuda-v2`, `server-cuda`. Immutable tags such as `server-cuda-v2.1.3` are not available.
      + For the full, current list of tags in a repository, use the standard Amazon ECR CLI commands (`aws ecr list-images` / `aws ecr describe-images`) against the applicable Region.
    + Not all framework versions are actively patched. Versions follow the standard DLC Support Policy - use a currently supported version to ensure you continue receiving security patches.

**Note**  
SageMaker Jumpstart in GovCloud only provides support for open-weight models. You can only access SageMaker Jumpstart with SageMaker AI Python SDK.

## Documentation
<a name="govcloud-sm-docs"></a>
+  [Amazon SageMaker AI documentation](https://docs.aws.amazon.com/documentation/sagemaker/) 

## Export-controlled content
<a name="govcloud-sagemaker-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon SageMaker AI metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your NotebookInstances, NotebookInstanceLifecycleConfigs, Endpoints, Models, EndpointConfigs, TrainingJobs, HyperParameterTuningJobs, and BatchTransformJobs.

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