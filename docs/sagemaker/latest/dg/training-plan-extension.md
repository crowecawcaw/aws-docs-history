

# Training plans extension
<a name="training-plan-extension"></a>

SageMaker training plans allow you to extend your existing training plans to avoid workload interruptions. When a training plan is approaching expiration, you can extend it directly through the SageMaker AI console or programmatically using the API or AWS CLI. This eliminates the need to create a new plan and reconfigure your workload with a new training plan ARN.

With training plan extensions, your running SageMaker training jobs or SageMaker HyperPod clusters continue to work seamlessly without interruption once the plan is extended. The extended plan reflects the new end date, and you can retrieve the history of all extensions for your training plan.

**Important**  
Please note extensions cannot be cancelled or modified to add or remove instances.

## Key features
<a name="training-plan-extension-features"></a>
+ Extend training plans through the console or API
+ Extend plans by 1-day increments up to 14 days, or 7-day increments up to 182 days
+ Extend a plan any number of times
+ View/ List extension history for your training plans in the console or through the API
+ Seamless continuation of running workloads in SageMaker AI without reconfiguration

## Prerequisites
<a name="training-plan-extension-prerequisites"></a>

Before extending a training plan, ensure the following:
+ The training plan must have a status of `Active` or `Scheduled`.
+ The plan must not have any extensions in `Payment Pending` status.
+ Extensions can be requested up to a minimum of 1 hour or a maximum of 57 days before the plan expires.

**Topics**
+ [Key features](#training-plan-extension-features)
+ [Prerequisites](#training-plan-extension-prerequisites)
+ [Extend a training plan using the SageMaker AI console](training-plan-extension-using-console.md)
+ [Extend a training plan using the SageMaker API or AWS CLI](training-plan-extension-using-api-cli-sdk.md)