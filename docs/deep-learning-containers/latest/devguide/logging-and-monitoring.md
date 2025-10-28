# Monitoring and Usage Tracking in AWS Deep Learning Containers

Your AWS Deep Learning Containers do not come with monitoring utilities. For information on monitoring, see
[GPU Monitoring
and Optimization](../../../dlami/latest/devguide/tutorial-gpu.md "../../../dlami/latest/devguide/tutorial-gpu.md"),
[Monitoring Amazon EC2](../../../AWSEC2/latest/UserGuide/monitoring_ec2.md "../../../AWSEC2/latest/UserGuide/monitoring_ec2.md"),
[Monitoring Amazon ECS](../../../AmazonECS/latest/developerguide/ecs-logging-monitoring.md "../../../AmazonECS/latest/developerguide/ecs-logging-monitoring.md"),
[Monitoring Amazon EKS](../../../eks/latest/userguide/logging-monitoring.md "../../../eks/latest/userguide/logging-monitoring.md"),
and
[Monitoring Amazon SageMaker Studio](../../../sagemaker/latest/dg/sagemaker-incident-response.md "../../../sagemaker/latest/dg/sagemaker-incident-response.md").

## Usage Tracking

AWS uses customer feedback and usage information to improve the quality
of the services and software we offer to customers.
We have added usage data collection to the supported AWS Deep Learning Containers
in order to better understand customer usage and guide future improvements.
Usage tracking for Deep Learning Containers is activated by default.
Customers can change their settings at any point of time to
activate or deactivate usage tracking.

Usage tracking for AWS Deep Learning Containers collects the _instance
ID_, _frameworks_, _framework versions_, _container
types_, and _Python versions_ used for
the containers. AWS also logs the event time in which it receives this
metadata.

No information on the commands used within the containers is collected or retained. No
other information about the containers is collected or retained.

To opt out of usage tracking, set the `OPT_OUT_TRACKING` environment
variable to true.

```
OPT_OUT_TRACKING=true
```

## Failure Rate Tracking

When using a first-party Amazon SageMaker AI AWS Deep Learning Containers
[container](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only"),
the SageMaker AI team will collect failure rate metadata to improve the quality of AWS Deep Learning Containers.
Failure rate tracking for AWS Deep Learning Containers is active by default. Customers can change their
settings to activate or deactivate failure rate tracking when creating an Amazon SageMaker AI endpoint.

Failure rate tracking for AWS Deep Learning Containers collects the _Instance ID_,
_ModelServer name_, _ModelServer version_,
_ErrorType_, and _ErrorCode_.
AWS also logs the event time in which it receives this metadata.

No information on the commands used within the containers is collected or retained. No other
information about the containers is collected or retained.

To opt out of failure rate tracking, set the `OPT_OUT_TRACKING` environment variable to `true`.

```
OPT_OUT_TRACKING=true
```

## Usage Tracking in the

following Framework Versions

While we recommend updating to supported Deep Learning Containers,
to opt-out of usage tracking for Deep Learning Containers that use these frameworks,
set the `OPT_OUT_TRACKING` environment variable to true **and**
use a custom entry point to disable the call for the following services:

- [Amazon EC2 Custom Entrypoints](../../../dlami/latest/devguide/deep-learning-containers-ec2-tutorials-custom-entry.md "../../../dlami/latest/devguide/deep-learning-containers-ec2-tutorials-custom-entry.md")
- [Amazon ECS Custom Entrypoints](../../../dlami/latest/devguide/deep-learning-containers-ecs-tutorials-custom-entry.md "../../../dlami/latest/devguide/deep-learning-containers-ecs-tutorials-custom-entry.md")
- [Amazon EKS Custom Entrypoints](../../../dlami/latest/devguide/deep-learning-containers-eks-tutorials-custom-entry.md "../../../dlami/latest/devguide/deep-learning-containers-eks-tutorials-custom-entry.md")
