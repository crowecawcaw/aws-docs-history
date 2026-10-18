

# AWS Systems Manager Run Command execution block
<a name="ssm-send-command-block"></a>

During failover, you might need to perform actions on self-managed databases or other application components that run on your Amazon EC2 instances—for example, to fail over a self-managed database (such as SQL Server, Oracle, or MySQL) or to run other application-specific failover or validation steps. With the AWS Systems Manager Run Command execution block, you can run an AWS Systems Manager command document on those instances as a step in your Region switch plan, and track its progress, completion, and retries within the plan.

This execution block supports only AWS Systems Manager documents of type `Command` (AWS Systems Manager Run Command), and it targets AWS Systems Manager managed nodes. It does not support other document types or other target resource types.

## Configuration
<a name="ssm-send-command-block-config"></a>

To configure a AWS Systems Manager Run Command execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [AWS Systems Manager Run Command execution block sample policy](security_iam_region_switch_ssm.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Document configuration for each Region: **For each Region in the plan, you provide the ARN of the AWS Systems Manager document to run. Region switch runs the command in the Region specified in that document ARN, which must be in the same partition as the plan and one of the plan's Regions.
   + **Document ARN: **Enter the Amazon Resource Name (ARN) of the AWS Systems Manager document to run. An ARN is required; a bare document name is not accepted. For example, `arn:aws:ssm:us-east-1:123456789012:document/MyDocument`. AWS owned public documents can omit the account ID.
   + **Document version (optional): **Enter the document version to run (`$DEFAULT`, `$LATEST`, or a version number). When you omit this value, AWS Systems Manager runs the document's default version.
   + **Targets: **Add up to 5 targets. Each target has a **Target key** (for example, `tag:Name` or `InstanceIds`) that selects how AWS Systems Manager chooses managed nodes. Each target also has **Target values** (comma-separated values that match the key, up to 50 values). Multiple values for a key are combined with `OR`.

1. **Parameters (optional): **Add up to 30 parameters to pass to the document. Each parameter has a **Parameter name** and **Parameter values**. Each parameter can have up to 50 values, each value can be up to 65,535 characters, and the combined parameters can be up to 64 KiB.

1. **Timeout: **Enter a timeout value.

1. **Retry interval: **Enter a retry interval, from 1 to 1,440 minutes, for Region switch to retry running the command if it returns a failure.

1. **Skip on ungraceful execution: **Choose whether to skip this step during ungraceful (unplanned) execution. When you select this option, Region switch skips this step during ungraceful execution.

Then, choose **Save step.**

This execution block supports cross-account resources. To run the command document in a Region that is in a different account, use the **Cross-account access** tab. For more information, see [Cross-account support in Region switch](cross-account-resources-rs.md).

## How it works
<a name="ssm-send-command-block-how"></a>

When plan execution reaches this step, Region switch calls the AWS Systems Manager `SendCommand` API in the Region specified in the document ARN, and passes the document version, targets, and parameters that you configured. To identify that the command was triggered by a Region switch plan, Region switch passes the plan ARN in the command's optional comment field.

Region switch runs the command by using the AWS Systems Manager `SendCommand` default values for `MaxConcurrency` (50) and `MaxErrors` (0). You can't modify these values.

After it invokes `SendCommand`, Region switch monitors the command by calling the `ListCommandInvocations` API until every invocation reaches a terminal state. Region switch then reports the step as a successful or failed execution.

**Successful execution.** The execution is successful when the command reaches the `Success` state on every targeted managed node. When the execution is successful, the step completes and the plan continues to the next step.

**Failed execution.** The execution fails when the command fails on one or more targeted managed nodes, or when Region switch can't start the command because of a request error, such as an invalid document, instance ID, or parameter.

**Retry behavior.** When an execution fails, Region switch automatically retries the command, re-running the same document against the same set of targets. Region switch continues to retry at the interval that you set, until the command succeeds or the step reaches its timeout. If the step reaches its timeout before the command succeeds, the step fails and the plan pauses on the failed step. Region switch does not retry deterministic AWS Systems Manager request errors—such as `InvalidDocument`, `InvalidInstanceId`, `InvalidParameters`, or validation errors—because the same request can't succeed; these errors fail the step immediately. You control how often Region switch retries with the **Retry interval** field, which corresponds to `retryIntervalMinutes` in the Region switch API.

**Pausing and resuming.** If you pause the plan while a command is running, Region switch takes no action on the command. The command continues to run on the managed nodes, and the plan remains paused until you resume or cancel it. When you resume, Region switch issues a new `SendCommand` call rather than resuming the previous command. For this reason, the command document should be idempotent.

**Canceling.** If you cancel the step while a command is running, Region switch makes a best-effort `CancelCommand` call. `CancelCommand` doesn't guarantee that commands that are already running on the managed nodes are stopped or paused.

**Ungraceful execution.** This block supports both graceful and ungraceful execution. If **Skip on ungraceful execution** is enabled, Region switch skips this step during ungraceful execution.