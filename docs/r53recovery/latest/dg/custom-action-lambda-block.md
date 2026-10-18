

# Custom action Lambda execution block
<a name="custom-action-lambda-block"></a>

The custom action Lambda execution block enables you to add a customized step to a plan by using a Lambda function.

## Configuration
<a name="custom-action-lambda-block-config"></a>

To configure a Lambda execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Custom action Lambda execution block sample policy](security_iam_region_switch_lambda.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **ARN of the Lambda function to be invoked in *primary* and *secondary* Regions**: Specify the ARN of the Lambda function to run for this step.

1. **Payload (optional): **Enter a valid JSON payload to invoke the Lambda function with.

1. **Region to run Lambda function: **In the drop-down menu, choose the Region that you want to run the Lambda functions in.

1. **Timeout: **Enter a timeout value.

1. **Retry interval: **Enter a retry interval, to rerun the Lambda function if it does not succeed within this interval.

1. **Ungraceful execution (optional): **Choose whether to skip this execution block during ungraceful (unplanned) executions. If you don't choose to skip the block, Region switch invokes the Lambda function during ungraceful execution.

Then, choose **Save step.**

## How it works
<a name="custom-action-lambda-block-how"></a>

When the plan execution reaches this step, Region switch invokes the designated Lambda function. The invocation details (ARN of the Lambda invoked and the payload) are available in the execution event log corresponding to the step. After invocation, Region switch polls the Lambda to return a successful response until the step timeout is reached. If the Lambda encounters an error within the configured timeout period, the step fails and the execution pauses, waiting for you to retry, skip, or cancel.

When your payload is a JSON object (or when no payload is configured), Region switch adds the following execution metadata keys:
+ `InvokedBy`—always set to `RegionSwitch`.
+ `PlanArn`—the ARN of the plan.
+ `ExecutionId`—the execution identifier, in the form {{region}}/{{execution-id}}.
+ `StepName`—the name of the step.

This block supports both graceful and ungraceful execution modes. During ungraceful execution, Region switch skips the step only when you configure the ungraceful behavior to skip. If you don't configure ungraceful behavior, Region switch invokes the Lambda function by using the same configuration as graceful execution.

When you configure a payload for a Lambda execution block, Region switch handles execution metadata injection as follows:
+ **JSON object payloads:** Region switch merges its execution metadata keys (such as `PlanArn`, `ExecutionId`, and `StepName`) into the top level of your JSON object. If your payload contains a key with the same name as a metadata key, your value takes precedence and the conflicting metadata key is omitted. Note that key matching is case-sensitive—for example, a key `planArn` does not conflict with the metadata key `PlanArn`.
+ **Non-JSON-object payloads:** If your payload is a JSON string, number, boolean, or array, Region switch forwards your payload to the Lambda function unchanged and does not inject execution metadata.

To receive Region switch execution metadata in your Lambda function, ensure your payload is a JSON object. If your payload is any other type, metadata will not be included. Additionally, avoid using key names that match the metadata keys if you want to preserve the metadata values injected by Region switch.

**Deactivating Region dependency**  
When you create a custom action Lambda execution block, you must specify two Lambda functions, one in each of the plan's Regions. You can configure which Region the Lambda is invoked in during execution: the activating Region or the deactivating Region. If you configure your Lambda to execute in the deactivating Region, be aware that you are taking a dependency on that Region's availability—which may be unavailable during the failover. Consider enabling ungraceful mode for the block to allow you the option to skip this step if the deactivating Region is unavailable.

**Example: Payload with a key collision and a near-match**

Suppose you enter the following payload when configuring the execution block. Notice that `StepName` matches a metadata key exactly (case-sensitive collision), while `planArn` does not match `PlanArn` because the case differs:

```
{
  "action": "enable-maintenance-page",
  "environment": "production",
  "StepName": "my-custom-step-label",
  "planArn": "arn:aws:my-custom:value"
}
```

When Region switch invokes the Lambda function, it merges the execution metadata into your object. Because `StepName` collides, your value wins and the metadata `StepName` is omitted. Because `planArn` differs in case from `PlanArn`, both keys are present in the final payload:

```
{
  "action": "enable-maintenance-page",
  "environment": "production",
  "StepName": "my-custom-step-label",
  "planArn": "arn:aws:my-custom:value",
  "InvokedBy": "RegionSwitch",
  "PlanArn": "arn:aws:arc-region-switch:us-east-1:123456789012:plan/my-recovery-plan",
  "ExecutionId": "us-west-2/abc123-def456"
}
```

**Example: No payload configured**

If you don't configure a payload, Region switch sends only the execution metadata keys:

```
{
  "InvokedBy": "RegionSwitch",
  "PlanArn": "arn:aws:arc-region-switch:us-east-1:123456789012:plan/my-recovery-plan",
  "ExecutionId": "us-west-2/abc123-def456",
  "StepName": "Display maintenance page"
}
```

**Example: Non-JSON-object payload**

If your payload is not a JSON object, Region switch forwards it to the Lambda function unchanged and does not inject execution metadata. For example, if you enter the following string payload:

```
"enable-maintenance-page"
```

The Lambda function receives exactly that string—no metadata keys are added.