# Supported frameworks and

algorithms

The following table shows SageMaker AI machine learning frameworks and algorithms supported by
Debugger.

| **SageMaker AI-supported frameworks and<br>algorithms**                                                                                                                             | **Debugging output tensors**                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [TensorFlow](https://sagemaker.readthedocs.io/en/stable/using_tf.html "https://sagemaker.readthedocs.io/en/stable/using_tf.html")                                                   | [AWS TensorFlow deep learning containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers") 1.15.4 or<br>later |
| [PyTorch](https://sagemaker.readthedocs.io/en/stable/using_pytorch.html "https://sagemaker.readthedocs.io/en/stable/using_pytorch.html")                                            | [AWS PyTorch deep learning containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers") 1.5.0 or<br>later     |
| [MXNet](https://sagemaker.readthedocs.io/en/stable/using_mxnet.html "https://sagemaker.readthedocs.io/en/stable/using_mxnet.html")                                                  | [AWS MXNet deep learning containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers") 1.6.0 or<br>later       |
| [XGBoost](https://sagemaker.readthedocs.io/en/stable/frameworks/xgboost/using_xgboost.html "https://sagemaker.readthedocs.io/en/stable/frameworks/xgboost/using_xgboost.html")      | 1.0-1, 1.2-1, 1.3-1                                                                                                                                                                                                                                                                       |
| [SageMaker AI generic estimator](https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html "https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html") | [Custom training<br>containers](debugger-bring-your-own-container.md "debugger-bring-your-own-container.md") (available for TensorFlow, PyTorch, MXNet, and<br>XGBoost with manual hook registration)                                                                                     |

- **Debugging output tensors** – Track and debug model
  parameters, such as weights, gradients, biases, and scalar values of your
  training job. Available deep learning frameworks are Apache MXNet, TensorFlow,
  PyTorch, and XGBoost.

###### Important

For the TensorFlow framework with Keras, SageMaker Debugger deprecates the zero code
change support for debugging models built using the `tf.keras`
modules of TensorFlow 2.6 and later. This is due to breaking changes
announced in the [TensorFlow 2.6.0 release note](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.0 "https://github.com/tensorflow/tensorflow/releases/tag/v2.6.0"). For instructions on how to
update your training script, see [Adapt your TensorFlow training
script](debugger-modify-script-tensorflow.md "debugger-modify-script-tensorflow.md").

###### Important

From PyTorch v1.12.0 and later, SageMaker Debugger deprecates the zero code change
support for debugging models.

This is due to breaking changes that cause SageMaker Debugger to interfere with the
`torch.jit` functionality. For instructions on how to update
your training script, see [Adapt your PyTorch training
script](debugger-modify-script-pytorch.md "debugger-modify-script-pytorch.md").
If the framework or algorithm that you want to train and debug is not listed in the
table, go to the [AWS Discussion
Forum](https://forums.aws.amazon.com/ "https://forums.aws.amazon.com/") and leave feedback on SageMaker Debugger.

## AWS Regions

Amazon SageMaker Debugger is available in all regions where Amazon SageMaker AI is in service except the following region.

- Asia Pacific (Jakarta): `ap-southeast-3`

To find if Amazon SageMaker AI is in service in your AWS Region, see [AWS Regional
Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

## Use Debugger with Custom Training

Containers

Bring your training containers to SageMaker AI and gain insights into your training jobs
using Debugger. Maximize your work efficiency by optimizing your model on Amazon EC2
instances using the monitoring and debugging features.

For more information about how to build your training container with the
`sagemaker-debugger` client library, push it to the Amazon Elastic Container Registry
(Amazon ECR), and monitor and debug, see [Use Debugger with custom training
containers](debugger-bring-your-own-container.md "debugger-bring-your-own-container.md").

## Debugger Open-Source GitHub Repositories

Debugger APIs are provided through the SageMaker Python SDK and designed to construct
Debugger hook and rule configurations for the SageMaker AI [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") and [DescribeTrainingJob](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md") API operations. The `sagemaker-debugger`
client library provides tools to register _hooks_ and access the
training data through its _trial_ feature, all through its
flexible and powerful API operations. It supports the machine learning frameworks
TensorFlow, PyTorch, MXNet, and XGBoost on Python 3.6 and later.

For direct resources about the Debugger and `sagemaker-debugger` API
operations, see the following links:

- [The Amazon SageMaker Python SDK documentation](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_debugger.html "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_debugger.html")
- [The Amazon SageMaker Python SDK - Debugger APIs](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html "https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html")
- [The `sagemaker-debugger` Python SDK documentation](https://sagemaker-debugger.readthedocs.io/en/website/index.html "https://sagemaker-debugger.readthedocs.io/en/website/index.html")
  for [the Amazon SageMaker Debugger open source client library](https://github.com/awslabs/sagemaker-debugger#amazon-sagemaker-debugger "https://github.com/awslabs/sagemaker-debugger#amazon-sagemaker-debugger")
- [The
  `sagemaker-debugger` PyPI](https://pypi.org/project/smdebug/ "https://pypi.org/project/smdebug/")

If you use the SDK for Java to conduct SageMaker training jobs and want to configure Debugger
APIs, see the following references:

- [Amazon SageMaker Debugger APIs](debugger-reference.md#debugger-apis "debugger-reference.md#debugger-apis")
- [Configure Debugger using SageMaker API](debugger-createtrainingjob-api.md "debugger-createtrainingjob-api.md")
