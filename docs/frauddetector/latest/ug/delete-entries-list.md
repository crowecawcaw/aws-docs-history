

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete entries from a list
<a name="delete-entries-list"></a>

You can delete one or more entries from your lists at any time. When you delete entries in your list you don’t need to update the rule the list is associated with. The rule automatically incorporates the updated list.

You can delete entries from a list in the Amazon Fraud Detector console, using the API, using the AWS CLI or the AWS SDK. 

## Delete entries from a list using the Amazon Fraud Detector console
<a name="delete-entries-list-console"></a>

**To delete one or more entries from a list**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

1. In the left navigation pane, choose **Lists**

1. In the **Lists** page, select the list that contains entries you want to delete.

1. In your list details page, select **List data** tab and select entries you want to delete.

1. Choose **Delete** and choose **Delete** again to confirm.

## Delete entries from a list using the AWS SDK for Python (Boto3)
<a name="delete-entries-list-sdk"></a>

In the following example the [UpdateList](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateList.html) API operation deletes entries from `allow_email_ids` list.

```
import boto3
                        fraudDetector = boto3.client('frauddetector')
fraudDetector.update_list(
   name = 'allow_email_ids',
   updateMode = 'REMOVE',
   elements = ['emailId_4', 'emailId_12']
)
```