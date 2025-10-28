# Custom action Lambda execution block

The custom action Lambda execution block enables you to add a customized step to a
plan by using a Lambda function.

## Configuration

To configure a Lambda execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Custom action Lambda execution block sample policy](security_iam_region_switch_lambda.md "security_iam_region_switch_lambda.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Lambda function ARN to be invoked when activating or deactivating
   _Region_**: Specify the ARN of the Lambda function to run for this step.
4. **Region to run Lambda function:** In the drop-down menu, choose
   the Region that you want to run the Lambda functions in.
5. **Timeout:** Enter a timeout value.
6. **Retry interval:** Enter a retry interval, to rerun the
   Lambda function if it does not succeed within this interval.

Then, choose **Save step.**

## How it works

- When you create a custom action Lambda execution block, you're required to
  specify two Lambda functions for the step to execute—one in each of the plan's Regions.
- You can configure which Region you want the Lambda to run in, for example,
  in the activating Region or in the deactivating Region. However, if you execute in the deactivating
  Region, you take a dependency on that Region. We do not recommend that you take a dependency on the
  deactivating Region.

This block supports both graceful and ungraceful execution modes. In ungraceful execution mode,
Region switch skips the Lambda execution block step.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your Lambda execution block configuration
and permissions. Region switch verifies that the following is correct:

- The Lambda functions specified in the configuration exist.
- The concurrency settings of Lambda functions are not throttled, including verifying the
  following:
  - Concurrency is not set to 0.
  - At least one concurrent execution is available, or that unreserved concurrency exists.

Region switch performs a dry run of the Lambda function to validate the specified parameters and permissions,
without executing the actual function logic. The standard Lambda costs are incurred when you perform a dry run.

Region switch also validates that the plan's IAM role has the required permissions for Lambda execution.
For more information about the required permissions for Region switch execution
blocks, see [Identity-based policy
examples for Region switch in ARC](security_iam_id-based-policy-examples-region-switch.md "security_iam_id-based-policy-examples-region-switch.md").

The correct IAM permissions are essential for the proper functioning of the Lambda execution block. If
any of these validations fail, Region switch returns warnings that there are issues, and provides specific error messages to help
you resolve the permissions or configuration issues. This ensures that your plan has the necessary access to manage
and interact with the Lambda during when this step runs during a plan execution.
