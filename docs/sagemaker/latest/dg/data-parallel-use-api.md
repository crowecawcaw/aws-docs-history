# Launching distributed training jobs with SMDDP using the

SageMaker Python SDK

To run a distributed training job with your adapted script from [Adapting your training script
to use the SMDDP collective operations](data-parallel-modify-sdp-select-framework.md "data-parallel-modify-sdp-select-framework.md"), use the SageMaker Python SDK's
framework or generic estimators by specifying the prepared training script as an entry point
script and the distributed training configuration.

This page walks you through how to use the [SageMaker AI Python
SDK](https://sagemaker.readthedocs.io/en/stable/api/training/index.html "https://sagemaker.readthedocs.io/en/stable/api/training/index.html") in two ways.

- If you want to achieve a quick adoption of your distributed training job in SageMaker AI,
  configure a SageMaker AI [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#sagemaker.pytorch.estimator.PyTorch "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#sagemaker.pytorch.estimator.PyTorch") or [TensorFlow](https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator "https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/sagemaker.tensorflow.html#tensorflow-estimator") framework estimator class. The framework estimator picks up your
  training script and automatically matches the right image URI of the [pre-built PyTorch or TensorFlow Deep Learning Containers (DLC)](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only"), given the value
  specified to the `framework_version` parameter.
- If you want to extend one of the pre-built containers or build a custom container to
  create your own ML environment with SageMaker AI, use the SageMaker AI generic `Estimator` class
  and specify the image URI of the custom Docker container hosted in your Amazon Elastic Container Registry (Amazon ECR).
  Your training datasets should be stored in Amazon S3 or [Amazon FSx for Lustre](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md") in the AWS Region in which
  you are launching your training job. If you use Jupyter notebooks, you should have a SageMaker notebook
  instance or a SageMaker Studio Classic app running in the same AWS Region. For more information about
  storing your training data, see the [SageMaker Python SDK data inputs](https://sagemaker.readthedocs.io/en/stable/overview.html#use-file-systems-as-training-input "https://sagemaker.readthedocs.io/en/stable/overview.html#use-file-systems-as-training-input") documentation.

###### Tip

We recommend that you use Amazon FSx for Lustre instead of Amazon S3 to improve training performance.
Amazon FSx has higher throughput and lower latency than Amazon S3.

###### Tip

To properly run distributed training on the EFA-enabled instance types, you should enables
traffic between the instances by setting up the security group of your VPC to allow all
inbound and outbound traffic to and from the security group itself. To learn how to set up the
security group rules, see [Step 1: Prepare an EFA-enabled security group](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security") in the _Amazon EC2
User Guide_.

Choose one of the following topics for instructions on how to run a distributed training job
of your training script. After you launch a training job, you can monitor system utilization and
model performance using [Amazon SageMaker Debugger](train-debugger.md "train-debugger.md") or
Amazon CloudWatch.

While you follow instructions in the following topics to learn more about technical details,
we also recommend that you try the [Amazon SageMaker AI data parallelism library
examples](distributed-data-parallel-v2-examples.md "distributed-data-parallel-v2-examples.md") to get started.

###### Topics

- [Use the PyTorch framework estimators in
  the SageMaker Python SDK](data-parallel-framework-estimator.md "data-parallel-framework-estimator.md")
- [Use the SageMaker AI generic estimator to extend
  pre-built DLC containers](data-parallel-use-python-skd-api.md "data-parallel-use-python-skd-api.md")
- [Create your own Docker container with
  the SageMaker AI distributed data parallel library](data-parallel-bring-your-own-container.md "data-parallel-bring-your-own-container.md")
