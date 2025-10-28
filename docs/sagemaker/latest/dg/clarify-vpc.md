# Give Amazon SageMaker Clarify Jobs Access to Resources in Your

Amazon VPC

To control access to your data and SageMaker Clarify jobs, we recommend that you create a private
Amazon VPC and configure it so that your jobs aren't accessible over the public internet. For
information about creating and configuring an Amazon VPC for processing jobs, see [Give SageMaker Processing Jobs
Access to Resources in Your Amazon VPC](process-vpc.md "process-vpc.md").

This document explains how to add additional Amazon VPC configurations that meet the
requirements for SageMaker Clarify jobs.

###### Topics

- [Configure a SageMaker Clarify Job for Amazon VPC Access](#clarify-vpc-config "#clarify-vpc-config")
- [Configure Your Private Amazon VPC for SageMaker Clarify
  jobs](#clarify-vpc-vpc "#clarify-vpc-vpc")

## Configure a SageMaker Clarify Job for Amazon VPC Access

You need to specify subnets and security groups when configuring your private
Amazon VPC for SageMaker Clarify jobs and to enable the job to get inferences from the SageMaker AI model
when computing post-training bias metrics and feature contributions that help
explain model predictions.

###### Topics

- [SageMaker Clarify Job Amazon VPC Subnets and Security
  Groups](#clarify-vpc-job "#clarify-vpc-job")
- [Configure a Model Amazon VPC for
  Inference](#clarify-vpc-model "#clarify-vpc-model")

### SageMaker Clarify Job Amazon VPC Subnets and Security

Groups

Subnets and security groups in your private Amazon VPC can be assigned to a SageMaker Clarify
job in various ways, depending on how you create the job.

- **SageMaker AI console**: Provide this
  information when you create the job in the **SageMaker AI
  Dashboard**. From the **Processing** menu,
  choose **Processing jobs**, then choose
  **Create processing job**. Select the
  **VPC** option in the **Network**
  panel and provide the subnets and security groups using the drop-down
  lists. Make sure network isolation option provided in this panel is
  turned off.
- **SageMaker API**: Use the
  `NetworkConfig.VpcConfig` request parameter of the [`CreateProcessingJob`](../APIReference/API_CreateProcessingJob.md "../APIReference/API_CreateProcessingJob.md") API, as shown in the
  following example:

```
"NetworkConfig": {
    "VpcConfig": {
        "Subnets": [
            "subnet-0123456789abcdef0",
            "subnet-0123456789abcdef1",
            "subnet-0123456789abcdef2"
        ],
        "SecurityGroupIds": [
            "sg-0123456789abcdef0"
        ]
    }
}
```

- **SageMaker Python SDK**: Use the
  `NetworkConfig` parameter of the [`SageMakerClarifyProcessor`](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.SageMakerClarifyProcessor "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.SageMakerClarifyProcessor") API or [`Processor`](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.processing.Processor "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.processing.Processor") API, as shown in the following
  example:

```
from sagemaker.network import NetworkConfig
network_config = NetworkConfig(
    subnets=[
        "subnet-0123456789abcdef0",
        "subnet-0123456789abcdef1",
        "subnet-0123456789abcdef2",
    ],
    security_group_ids=[
        "sg-0123456789abcdef0",
    ],
)
```

SageMaker AI uses the information to create network interfaces and attach them to the
SageMaker Clarify job. The network interfaces provide a SageMaker Clarify job with a network connection
within your Amazon VPC that is not connected to the public internet. They also enable
the SageMaker Clarify job to connect to resources in your private Amazon VPC.

###### Note

The network isolation option of the SageMaker Clarify job must be turned off (by
default the option is turned off) so that the SageMaker Clarify job can communicate with
the shadow endpoint.

### Configure a Model Amazon VPC for

Inference

In order to compute post-training bias metrics and explainability, the SageMaker Clarify
job needs to get inferences from the SageMaker AI model that is specified by the
`model_name` parameter of the [analysis configuration](clarify-configure-processing-jobs.md#clarify-processing-job-configure-analysis "clarify-configure-processing-jobs.md#clarify-processing-job-configure-analysis") for the SageMaker Clarify processing job. Alternatively,
if you use the `SageMakerClarifyProcessor` API in the SageMaker AI Python
SDK, the job needs to get the `model_name` specified by the [ModelConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.ModelConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.ModelConfig") class. To accomplish this, the SageMaker Clarify job creates an
ephemeral endpoint with the model, known as a _shadow
endpoint_, and then applies the Amazon VPC configuration of the model
to the shadow endpoint.

To specify subnets and security groups in your private Amazon VPC to the SageMaker AI
model, use the `VpcConfig` request parameter of the [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API or provide this information when
you create the model using the SageMaker AI dashboard in the console. The following is
an example of the `VpcConfig` parameter that you include in your call
to `CreateModel`:

```
"VpcConfig": {
    "Subnets": [
        "subnet-0123456789abcdef0",
        "subnet-0123456789abcdef1",
        "subnet-0123456789abcdef2"
    ],
    "SecurityGroupIds": [
        "sg-0123456789abcdef0"
    ]
}
```

You can specify the number of instances of the shadow endpoint to launch with
the `initial_instance_count` parameter of the [analysis configuration](clarify-configure-processing-jobs.md#clarify-processing-job-configure-analysis "clarify-configure-processing-jobs.md#clarify-processing-job-configure-analysis") for the SageMaker Clarify processing job. Alternatively,
if you use the `SageMakerClarifyProcessor` API in the SageMaker AI Python
SDK, the job needs to get the `instance_count` specified by the
[ModelConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.ModelConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.ModelConfig") class.

###### Note

Even if you only request one instance when creating the shadow endpoint,
you need at least two subnets in the model's [ModelConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.ModelConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.ModelConfig") in distinct availability zones. Otherwise the
shadow endpoint creation fails with the following error:

**`ClientError: Error hosting endpoint
 sagemaker-clarify-endpoint-XXX: Failed. Reason: Unable to locate at
 least 2 availability zone(s) with the requested instance type YYY that
 overlap with SageMaker AI subnets.`**

If your model requires model files in Amazon S3, then the model Amazon VPC needs to have
an Amazon S3 VPC endpoint. For more information about creating and configuring an
Amazon VPC for SageMaker AI models, see [Give SageMaker AI Hosted Endpoints Access to Resources in Your
Amazon VPC](host-vpc.md "host-vpc.md").

## Configure Your Private Amazon VPC for SageMaker Clarify

jobs

In general, you can follow the steps in [Configure Your
Private VPC for SageMaker Processing](process-vpc.md#process-vpc-vpc "process-vpc.md#process-vpc-vpc") to configure your private Amazon VPC for
SageMaker Clarify jobs. Here are some highlights and special requirements for SageMaker Clarify jobs.

###### Topics

- [Connect to Resources Outside Your
  Amazon VPC](#clarify-vpc-nat "#clarify-vpc-nat")
- [Configure the Amazon VPC Security
  Group](#clarify-vpc-security-group "#clarify-vpc-security-group")

### Connect to Resources Outside Your

Amazon VPC

If you configure your Amazon VPC so that it does not have public internet access,
then some additional setup is required to grant SageMaker Clarify jobs access to resources
and services outside of your Amazon VPC. For example, an Amazon S3 VPC endpoint is
required because a SageMaker Clarify job needs to load a dataset from an S3 bucket as well
as save the analysis results to an S3 bucket. For more information, see [Create an Amazon
S3 VPC Endpoint](process-vpc.md#process-vpc-s3 "process-vpc.md#process-vpc-s3") for the creation guide. In addition, if a SageMaker Clarify job
needs to get inferences from the shadow endpoint, then it needs to call several
more AWS services.

- **Create an Amazon SageMaker API service VPC
  endpoint**: The SageMaker Clarify job needs to call the Amazon SageMaker API
  service to manipulate the shadow endpoint, or to describe a SageMaker AI model
  for Amazon VPC validation. You can follow the guidance provided in the [Securing all Amazon SageMaker API calls with AWS
  PrivateLink](https://aws.amazon.com/blogs/machine-learning/securing-all-amazon-sagemaker-api-calls-with-aws-privatelink/ "https://aws.amazon.com/blogs/machine-learning/securing-all-amazon-sagemaker-api-calls-with-aws-privatelink/") blog to create an Amazon SageMaker API VPC endpoint that
  allows the SageMaker Clarify job to make the service calls. Note that the service
  name of Amazon SageMaker API service is
  `com.amazonaws.`region`.sagemaker.api`,
  where `region` is the name of the Region where
  your Amazon VPC resides.
- **Create an Amazon SageMaker AI Runtime VPC
  Endpoint**: The SageMaker Clarify job needs to call the Amazon SageMaker AI
  runtime service, which routes the invocations to the shadow endpoint.
  The setup steps are similar to those for the Amazon SageMaker API service. Note
  that the service name of Amazon SageMaker AI Runtime service is
  `com.amazonaws.`region`.sagemaker.runtime`,
  where `region` is the name of the Region where
  your Amazon VPC resides.

### Configure the Amazon VPC Security

Group

SageMaker Clarify jobs support distributed processing when two or more processing
instances are specified in one of the following ways:

- **SageMaker AI console**: The **Instance
  count** is specified in the **Resource
  configuration** part of the **Job
  settings** panel on the **Create processing
  job** page.
- **SageMaker API**: The
  `InstanceCount` is specified when you create the job with
  the [`CreateProcessingJob`](../APIReference/API_CreateProcessingJob.md "../APIReference/API_CreateProcessingJob.md") API.
- **SageMaker Python SDK**: The
  `instance_count` is specified when using the [SageMakerClarifyProcessor](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.SageMakerClarifyProcessor "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.clarify.SageMakerClarifyProcessor") API or the [Processor](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.processing.Processor "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html?highlight=Processor#sagemaker.processing.Processor") API.

In distributed processing, you must allow communication between the different
instances in the same processing job. To do that, configure a rule for your
security group that allows inbound connections between members of the same
security group. For information, see [Security group rules](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules").
