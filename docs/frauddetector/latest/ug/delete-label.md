

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete label
<a name="delete-label"></a>

When you delete a label, Amazon Fraud Detector permanently deletes that label and the data is no longer stored in Amazon Fraud Detector.

You cannot delete a label that is included in an event type in Amazon Fraud Detector. And you also cannot delete a label that is assigned to an event ID. You must first delete the relevant event ID. 

You can delete labels in Amazon Fraud Detector console, using the [delete-label](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-label.html) command, using the [DeleteLabel](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteLabel.html) API, or using the AWS SDK for Python (Boto3)

## Delete label using the console
<a name="delete-label-console"></a>

**To delete a label**

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector).

1. In the left navigation pane of the Amazon Fraud Detector console, choose **Resources**, then choose **Labels**.

1. Choose the label that you want to delete.

1. Choose **Actions**, and then choose **Delete**.

1. Enter the label name, and then choose **Delete label**.

## Delete a label using the AWS SDK for Python (Boto3)
<a name="delete-label-using-the-aws-python-sdk"></a>

The following AWS SDK for Python (Boto3) example code deletes a label *legit* using the [DeleteLabel](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteLabel.html) API.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.delete_event_label (
    name = 'legit'
)
```