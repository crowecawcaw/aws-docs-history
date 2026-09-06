

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete an outcome
<a name="delete-outcome"></a>

You cannot delete an outcome that is used in a rule version.

When you delete an outcome, Amazon Fraud Detector permanently deletes that outcome and the data is no longer stored in Amazon Fraud Detector.

You can delete an outcome in the Amazon Fraud Detector console, using the [delete-outcome](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-outcome.html) command, using the [DeleteOutcome](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteOutcome.html) API, or using the AWS SDK for Python (Boto3)

## Delete an outcome in the Amazon Fraud Detector console
<a name="delete-outcome-console"></a>

**To delete an outcome**

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector).

1. In the left navigation pane of the Amazon Fraud Detector console, choose **Resources**, and then choose **Outcomes**.

1. Choose the outcome that you want to delete.

1. Choose **Actions**, and then choose **Delete**.

1. Enter the outcome name, and then choose **Delete outcome**.

## Delete an outcome using the AWS SDK for Python (Boto3)
<a name="delete-outcome-using-the-aws-python-sdk"></a>

The following example uses the [DeleteOutcome](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteOutcome.html) API to delete the `verify_customer` outcome. After the outcome is deleted, you can no longer assign it to a rule. 

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.delete_outcome(
name = 'verify_customer'
)
```