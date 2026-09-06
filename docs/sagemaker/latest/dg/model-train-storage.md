

# Mapping of training storage paths managed by Amazon SageMaker AI
<a name="model-train-storage"></a>

This page provides a high-level summary of how the SageMaker training platform manages storage paths for training datasets, model artifacts, checkpoints, and outputs between AWS cloud storage and training jobs in SageMaker AI. Throughout this guide, you learn to identify the default paths set by the SageMaker AI platform and how the data channels can be streamlined with your data sources in Amazon Simple Storage Service (Amazon S3), FSx for Lustre, and Amazon EFS. For more information about various data channel input modes and storage options, see [Setting up training jobs to access datasets](model-access-training-data.md).

## Overview of how SageMaker AI maps storage paths
<a name="model-train-storage-overview"></a>

The following diagram shows an example of how SageMaker AI maps input and output paths when you run a training job using the SageMaker Python SDK [ModelTrainer](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) class. 

![An example of how SageMaker AI maps paths between the training job container and the storage when you run a training job using the SageMaker Python SDK ModelTrainer class and its train method.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/sagemaker-training-storage.png)


SageMaker AI maps storage paths between a storage (such as Amazon S3, Amazon FSx, and Amazon EFS) and the SageMaker training container based on the paths and input mode specified through a SageMaker AI ModelTrainer object. More information about how SageMaker AI reads from or writes to the paths and the purpose of the paths, see [SageMaker AI environment variables and the default paths for training storage locations](model-train-storage-env-var-summary.md).

You can use `OutputDataConfig` in the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API to save the results of model training to an S3 bucket. Use the [ModelArtifacts](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelArtifacts.html) API to find the S3 bucket that contains your model artifacts. See the [abalone\_build\_train\_deploy](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.ipynb) notebook for an example of output paths and how they are used in API calls.

For more information and examples of how SageMaker AI manages data source, input modes, and local paths in SageMaker training instances, see [Access Training Data](https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data.html).

**Topics**
+ [Overview of how SageMaker AI maps storage paths](#model-train-storage-overview)
+ [Uncompressed model output](model-train-storage-uncompressed.md)
+ [Managing storage paths for different types of instance local storage](model-train-storage-tips-considerations.md)
+ [SageMaker AI environment variables and the default paths for training storage locations](model-train-storage-env-var-summary.md)