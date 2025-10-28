Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete entries from a list

You can delete one or more entries from your lists at any time. When you delete entries in your list you don’t need to update the rule
the list is associated with. The rule automatically incorporates the updated list.

You can delete entries from a list in the Amazon Fraud Detector console, using the API, using the AWS CLI or the AWS SDK.

## Delete entries from a list using the Amazon Fraud Detector console

###### To delete one or more entries from a list

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose
   **Lists**
3. In the **Lists** page, select the list that contains entries you want to delete.
4. In your list details page, select **List data** tab and select entries you want to delete.
5. Choose **Delete** and choose **Delete** again to confirm.

## Delete entries from a list using the AWS SDK for Python (Boto3)

In the following example the [UpdateList](../api/API_UpdateList.md "../api/API_UpdateList.md") API operation
deletes entries from `allow_email_ids` list.

```
import boto3
                        fraudDetector = boto3.client('frauddetector')
fraudDetector.update_list(
   name = 'allow_email_ids',
   updateMode = 'REMOVE',
   elements = ['emailId_4', 'emailId_12']
)

```
