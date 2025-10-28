Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete label

When you delete a label, Amazon Fraud Detector permanently deletes that label and the data is no longer stored in Amazon Fraud Detector.

You cannot delete a label that is included in an event type in Amazon Fraud Detector. And you also cannot delete a label that is assigned to an event ID. You must first delete the relevant event ID.

You can delete labels in Amazon Fraud Detector console, using the [delete-label](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-label.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-label.html")
command, using the [DeleteLabel](../api/API_DeleteLabel.md "../api/API_DeleteLabel.md") API, or using the AWS SDK for Python (Boto3)

## Delete label using the console

###### To delete a label

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector").
2. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Resources**, then choose
   **Labels**.
3. Choose the label that you want to delete.
4. Choose **Actions**, and then choose
   **Delete**.
5. Enter the label name, and then choose **Delete
   label**.

## Delete a label using the AWS SDK for Python (Boto3)

The following AWS SDK for Python (Boto3) example code deletes a label _legit_ using the [DeleteLabel](../api/API_DeleteLabel.md "../api/API_DeleteLabel.md") API.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.delete_event_label (
    name = 'legit'
)

```
