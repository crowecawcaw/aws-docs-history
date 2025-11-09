# AWS Fargate usage metrics

You can use CloudWatch usage metrics to provide visibility into your accounts usage of
resources. Use these metrics to visualize your current service usage on CloudWatch graphs and
dashboards.

AWS Fargate usage metrics correspond to AWS service quotas. You can configure alarms
that alert you when your usage approaches a service quota. For more information about
Fargate service quotas, [Amazon ECS endpoints and quotas](../../../general/latest/gr/ecs-service.md "../../../general/latest/gr/ecs-service.md") in the _Amazon Web Services General Reference_..

AWS Fargate publishes the following metrics in the `AWS/Usage`
namespace.

| Metric          | Description                                                                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `ResourceCount` | The total number of the specified resource running on your account.<br>The resource is defined by the dimensions associated with the<br>metric. |

The following dimensions are used to refine the usage metrics that are published by
AWS Fargate.

| Dimension  | Description                                                                                                                                                                                                                      |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Service`  | The name of the AWS service containing the resource. For<br>AWS Fargate usage metrics, the value for this dimension is<br>`Fargate`.                                                                                             |
| `Type`     | The type of entity that is being reported. Currently, the only valid<br>value for AWS Fargate usage metrics is `Resource`.                                                                                                       |
| `Resource` | The type of resource that is running. The type of resource that is<br>running. Currently, the only valid value for AWS Fargate usage metrics<br>is `vCPU` which returns information about the running<br>instances.              |
| `Class`    | The class of resource being tracked. The class of resource being<br>tracked. For AWS Fargate usage metrics with vCPU as the value of the<br>Resource dimension, the valid values are `Standard/OnDemand`<br>and `Standard/Spot`. |

You can use the Service Quotas console to visualize your usage on a graph and configure alarms
that alert you when your AWS Fargate usage approaches a service quota. For information
about how to create a CloudWatch alarm to notify you when you're close to a quota value threshold,
see [Service Quotas and Amazon CloudWatch](../../../servicequotas/latest/userguide/configure-cloudwatch.md "../../../servicequotas/latest/userguide/configure-cloudwatch.md") alarms in the _Service Quotas User
Guide_

.
