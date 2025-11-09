Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete an outcome

You cannot delete an outcome that is used in a rule version.

When you delete an outcome, Amazon Fraud Detector permanently deletes that outcome and the data is no longer stored in Amazon Fraud Detector.

You can delete an outcome in the Amazon Fraud Detector console, using the [delete-outcome](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-outcome.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-outcome.html") command,
using the [DeleteOutcome](../api/API_DeleteOutcome.md "../api/API_DeleteOutcome.md") API, or using the AWS SDK for Python (Boto3)

## Delete an outcome in the Amazon Fraud Detector console

###### To delete an outcome

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector").
2. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Resources**, and then choose
   **Outcomes**.
3. Choose the outcome that you want to delete.
4. Choose **Actions**, and then choose
   **Delete**.
5. Enter the outcome name, and then choose **Delete
   outcome**.

## Delete an outcome using the AWS SDK for Python (Boto3)

The following example uses the [DeleteOutcome](../api/API_DeleteOutcome.md "../api/API_DeleteOutcome.md") API to delete the `verify_customer` outcome.
After the outcome is deleted, you can no longer assign it to a rule.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.delete_outcome(
name = 'verify_customer'
)

```
