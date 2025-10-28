# Run Training and Inference Containers in Internet-Free

Mode

SageMaker AI training and deployed inference containers are internet-enabled by default. This allows
containers to access external services and resources on the public internet as part of your training and
inference workloads. However, this could provide an avenue for unauthorized access to your data. For
example, a malicious user or code that you accidentally install on the container (in the form of a
publicly available source code library) could access your data and transfer it to a remote host.

If you use an Amazon VPC by specifying a value for the `VpcConfig` parameter when
you call [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md"), [`CreateHyperParameterTuningJob`](../APIReference/API_CreateHyperParameterTuningJob.md "../APIReference/API_CreateHyperParameterTuningJob.md"), or [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md"), you can protect your data and resources by
managing security groups and restricting internet access from your VPC. However, this
comes at the cost of additional network configuration, and has the risk of configuring
your network incorrectly. If you do not want SageMaker AI to provide external network access to
your training or inference containers, you can enable network isolation.

## Network Isolation

You can enable network isolation when you create your training job or model by setting
the value of the `EnableNetworkIsolation` parameter to `True`
when you call [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md"), [`CreateHyperParameterTuningJob`](../APIReference/API_CreateHyperParameterTuningJob.md "../APIReference/API_CreateHyperParameterTuningJob.md"), or [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md").

###### Note

Network isolation is required to run training jobs and models using resources from
AWS Marketplace. For additional security, AWS Marketplace images run within an Amazon VPC. They only have access to data within their local file systems.

When you enable network isolation, your training and inference containers can't make any outbound network
calls to any service, including Amazon S3. No AWS credentials
are made available to the container runtime environment. For training
jobs with multiple instances, network inbound and outbound traffic is limited to communication
between training container peers.

SageMaker AI still handles all necessary Amazon S3 download and upload operations
using your SageMaker AI execution role. This happens apart from your training and
inference containers, ensuring that your training data and model artifacts are still accessible
while maintaining container isolation.

The following managed SageMaker AI containers do not support network isolation because
they require access to Amazon S3:

- Chainer
- SageMaker AI Reinforcement Learning

### Network

isolation with a VPC

Network isolation can be used in conjunction with a VPC. In this scenario, the download
and upload of customer data and model artifacts are routed through your VPC
subnet. However, the training and inference containers themselves continue to be
isolated from the network, and do not have access to any resource within your
VPC or on the internet.
