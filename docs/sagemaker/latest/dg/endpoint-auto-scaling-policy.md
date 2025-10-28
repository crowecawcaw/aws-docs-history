# Auto scaling policy overview

To use auto scaling, you define a scaling policy that adds and removes the number of
instances for your production variant in response to actual workloads.

To automatically scale as workload changes occur, you have two options: target
tracking and step scaling policies.

In most cases, we recommend using target tracking scaling policies. With target
tracking, you choose an Amazon CloudWatch metric and target value. Auto scaling creates and
manages the CloudWatch alarms for the scaling policy and calculates the scaling adjustment
based on the metric and the target value. The policy adds and removes the number of
instances as required to keep the metric at, or close to, the specified target value.
For example, a scaling policy that uses the predefined
`InvocationsPerInstance` metric with a target value of 70 can keep
`InvocationsPerInstance` at, or close to 70. For more information, see
[Target tracking scaling policies](../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md "../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md") in the
_Application Auto Scaling User Guide_.

You can use step scaling when you require an advanced configuration, such as
specifying how many instances to deploy under what conditions. For example, you must use
step scaling if you want to enable an endpoint to scale out from zero active instances.
For an overview of step scaling policies and how they work, see [Step scaling policies](../../../autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.md "../../../autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.md") in the _Application Auto Scaling User Guide_.

To create a target tracking scaling policy, you specify the following:

- Metric — The CloudWatch metric to track, such
  as average number of invocations per instance.
- Target value — The target value for the
  metric, such as 70 invocations per instance per minute.
  You can create target tracking scaling policies with either predefined metrics or
  custom metrics. A predefined metric is defined in an enumeration so that you can specify
  it by name in code or use it in the SageMaker AI console. Alternatively, you can use either the
  AWS CLI or the Application Auto Scaling API to apply a target tracking scaling policy based on a
  predefined or custom metric.

Note that scaling activities are performed with cooldown periods between them to
prevent rapid fluctuations in capacity. You can optionally configure the cooldown
periods for your scaling policy.

For more information about the key concepts of auto scaling, see the following
section.

## Schedule-based scaling

You can also create scheduled actions to perform scaling activities at specific
times. You can create scheduled actions that scale one time only or that scale on a
recurring schedule. After a scheduled action runs, your scaling policy can continue
to make decisions about whether to scale dynamically as workload changes occur.
Scheduled scaling can be managed only from the AWS CLI or the Application Auto Scaling API. For
more information, see [Scheduled scaling](../../../autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.md "../../../autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.md") in the _Application Auto Scaling User Guide_.

## Minimum and maximum scaling

limits

When configuring auto scaling, you must specify your scaling limits before
creating a scaling policy. You set limits separately for the minimum and maximum
values.

The minimum value must be at least 1, and equal to or less than the value
specified for the maximum value.

The maximum value must be equal to or greater than the value specified for the
minimum value. SageMaker AI auto scaling does not enforce a limit for this value.

To determine the scaling limits that you need for typical traffic, test your auto
scaling configuration with the expected rate of traffic to your model.

If a variant’s traffic becomes zero, SageMaker AI automatically scales in to the minimum
number of instances specified. In this case, SageMaker AI emits metrics with a value of
zero.

There are three options for specifying the minimum and maximum capacity:

1. Use the console to update the **Minimum instance count**
   and **Maximum instance count** settings.
2. Use the AWS CLI and include the `--min-capacity` and
   `--max-capacity` options when running the [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command.
3. Call the [RegisterScalableTarget](../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md "../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md") API and specify the
   `MinCapacity` and `MaxCapacity` parameters.

###### Tip

You can manually scale out by increasing the minimum value, or manually scale
in by decreasing the maximum value.

## Cooldown period

A _cooldown period_ is used to protect against
over-scaling when your model is scaling in (reducing capacity) or scaling out
(increasing capacity). It does this by slowing down subsequent scaling activities
until the period expires. Specifically, it blocks the deletion of instances for
scale-in requests, and limits the creation of instances for scale-out requests. For
more information, see [Define cooldown periods](../../../autoscaling/application/userguide/target-tracking-scaling-policy-overview.md#target-tracking-cooldown "../../../autoscaling/application/userguide/target-tracking-scaling-policy-overview.md#target-tracking-cooldown") in the _Application Auto Scaling User Guide_.

You configure the cooldown period in your scaling policy.

If you don't specify a scale-in or a scale-out cooldown period, your scaling
policy uses the default, which is 300 seconds for each.

If instances are being added or removed too quickly when you test your scaling
configuration, consider increasing this value. You might see this behavior if the
traffic to your model has a lot of spikes, or if you have multiple scaling policies
defined for a variant.

If instances are not being added quickly enough to address increased traffic,
consider decreasing this value.

## Related resources

For more information about configuring auto scaling, see the following
resources:

- [application-autoscaling](../../../cli/latest/reference/application-autoscaling.md "../../../cli/latest/reference/application-autoscaling.md") section of the
  _AWS CLI Command Reference_
- [Application Auto Scaling API Reference](../../../autoscaling/application/APIReference.md "../../../autoscaling/application/APIReference.md")
- [Application Auto Scaling User Guide](../../../autoscaling/application/userguide.md "../../../autoscaling/application/userguide.md")

###### Note

SageMaker AI recently introduced new inference capabilities built on real-time
inference endpoints. You create a SageMaker AI endpoint with an endpoint configuration
that defines the instance type and initial instance count for the endpoint.
Then, create an inference component, which is a SageMaker AI hosting object that you can
use to deploy a model to an endpoint. For information about scaling inference
components, see [SageMaker AI adds new inference capabilities to help reduce foundation model
deployment costs and latency](https://aws.amazon.com/blogs/aws/amazon-sagemaker-adds-new-inference-capabilities-to-help-reduce-foundation-model-deployment-costs-and-latency/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-adds-new-inference-capabilities-to-help-reduce-foundation-model-deployment-costs-and-latency/") and [Reduce model deployment costs by 50% on average using the latest
features of SageMaker AI](https://aws.amazon.com/blogs/machine-learning/reduce-model-deployment-costs-by-50-on-average-using-sagemakers-latest-features/ "https://aws.amazon.com/blogs/machine-learning/reduce-model-deployment-costs-by-50-on-average-using-sagemakers-latest-features/") on the AWS Blog.
