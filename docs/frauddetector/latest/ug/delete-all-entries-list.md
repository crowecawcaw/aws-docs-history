Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete all entries from a list

You can delete all entries in your list, if the list isn’t being used in a rule. You can delete all
the entries that are in the list and later add entries in the same list.

You can delete entries from a list in the Amazon Fraud Detector console, using the API, using the AWS CLI or the AWS SDK.

## Delete all entries from a list using the Amazon Fraud Detector console

###### To delete all entries from a list

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose
   **Lists**
3. In the **Lists** page, select the list that contains entries you want to delete.
4. In your list details page, select **List data** tab and choose **Delete all**.
5. In the **Delete all** box, type `delete all` to confirm and then choose **Delete all list data**.

## Delete all entries from a list using the AWS SDK for Python (Boto3)

In the following example the [UpdateList](../api/API_UpdateList.md "../api/API_UpdateList.md") API operation
deletes all entries from `allow_email_ids` list.

```
import boto3
                        fraudDetector = boto3.client('frauddetector')
fraudDetector.update_list(
   name = 'allow_email_ids',
   updateMode = 'REPLACE',
   elements = []
)

```
