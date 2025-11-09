Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Add entries in a list

After you created your list you can add or append entries in your list at any time. When you add or append entries in your list,
you don’t need to update the rule the list is associated with. The rule automatically incorporates the newly added entries.

Your list can contain up to 100,000 unique entries and each entry can be up to 320 characters.

You can add entries in the Amazon Fraud Detector console, using the API, using the AWS CLI, or using the AWS SDK.

## Add entries in a list using the Amazon Fraud Detector console

###### To add one or more entries in a list

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose **Lists**.
3. In the **Lists** page, select the list that you want to add entries to.
4. In your list details page, select **List data** tab and choose **Add data**.
5. In the **Add list data** box, add one entry on each line or copy and paste entries from a spreadsheet. Make
   sure to not use comma to separate entries.
6. Choose **Add**.

## Add entries in a list using the AWS SDK for Python (Boto3)

The following example uses the [UpdateList](../api/API_UpdateList.md "../api/API_UpdateList.md") API operation
to add two new entries in the `allow_email_ids` list. Make sure that the entries you are adding are unique in the list.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.update_list (
     name = 'allow_email_ids',
     updateMode = 'APPEND'
     elements = ['emailId_11','emailId_12']

```
