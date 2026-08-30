# Custom action Lambda execution block

The custom action Lambda execution block enables you to add a customized step to a
plan by using a Lambda function.

## Configuration

To configure a Lambda execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place.
For more information, see [Custom action Lambda execution block sample policy](security_iam_region_switch_lambda.md "security_iam_region_switch_lambda.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **ARN of the Lambda function to be invoked in
   _primary_ and _secondary_ Regions**: Specify the ARN of the Lambda function to run for this step.
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
