

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete all entries from a list
<a name="delete-all-entries-list"></a>

You can delete all entries in your list, if the list isn’t being used in a rule. You can delete all the entries that are in the list and later add entries in the same list. 

You can delete entries from a list in the Amazon Fraud Detector console, using the API, using the AWS CLI or the AWS SDK. 

## Delete all entries from a list using the Amazon Fraud Detector console
<a name="delete-all-entries-list-console"></a>

**To delete all entries from a list**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

1. In the left navigation pane, choose **Lists**

1. In the **Lists** page, select the list that contains entries you want to delete.

1. In your list details page, select **List data** tab and choose **Delete all**.

1. In the **Delete all** box, type `delete all` to confirm and then choose **Delete all list data**.

## Delete all entries from a list using the AWS SDK for Python (Boto3)
<a name="delete-all-entries-list-sdk"></a>

In the following example the [UpdateList](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateList.html) API operation deletes all entries from `allow_email_ids` list.

```
import boto3
                        fraudDetector = boto3.client('frauddetector')
fraudDetector.update_list(
   name = 'allow_email_ids',
   updateMode = 'REPLACE',
   elements = []
)
```