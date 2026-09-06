

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete a list
<a name="delete-list"></a>

You can delete a list that isn't used in any rule. When you delete a list, Amazon Fraud Detector permanently deletes that list and all entries in the list. 

You can delete a list in the Amazon Fraud Detector console, using the API, using the AWS CLI or the AWS SDK. 

## Delete list using the Amazon Fraud Detector console
<a name="delete-list-console"></a>

**To delete a list**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

1. In the left navigation pane, choose **Lists**

1. In the **Lists** page, select the list you want to delete.

1. In your list details page, choose **Actions** and select **Delete list**.

1. Choose **Delete list**.

## Delete list using the AWS SDK for Python (Boto3)
<a name="delete-list-sdk"></a>

The following example uses the [DeleteList](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteList.html) API operation to delete `allow_email_ids`.

```
import boto3
                        fraudDetector = boto3.client('frauddetector')
fraudDetector.delete_list(
   name = 'allow_email_ids' 
)
```