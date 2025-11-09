Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete a list

You can delete a list that isn't used in any rule. When you delete a list, Amazon Fraud Detector permanently deletes that list and all entries in the list.

You can delete a list in the Amazon Fraud Detector console, using the API, using the AWS CLI or the AWS SDK.

## Delete list using the Amazon Fraud Detector console

###### To delete a list

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose
   **Lists**
3. In the **Lists** page, select the list you want to delete.
4. In your list details page, choose **Actions** and select **Delete list**.
5. Choose **Delete list**.

## Delete list using the AWS SDK for Python (Boto3)

The following example uses the [DeleteList](../api/API_DeleteList.md "../api/API_DeleteList.md") API operation to delete
`allow_email_ids`.

```
import boto3
                        fraudDetector = boto3.client('frauddetector')
fraudDetector.delete_list(
   name = 'allow_email_ids'
)

```
