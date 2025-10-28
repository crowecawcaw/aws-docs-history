Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create a list

You can create a list containing input data (entries) of a variable in your event dataset and use the list in rule expression.
The entries in the list can be managed dynamically without updating the rule that is using the list.

To create a list, you must first specify a name and then optionally associate the list with a [Variable types](variables.md#variable-types "variables.md#variable-types") supported by Amazon Fraud Detector.
By default, Amazon Fraud Detector assumes the list to be of FREE_FORM_TEXT variable type.

You can create a list in the Amazon Fraud Detector console, using the API, using the AWS CLI, or using the AWS SDK.

## Create list using the Amazon Fraud Detector console

###### To create a list

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose **Lists**.
3. Under **Lists** details
   1. In the **List name**, enter a name for your list.
   2. In the **Description**, optionally, enter a description.
   3. (Optional) In the **Variable type**, select a variable type for your list.

   ###### Important

   If your list contains IP addresses, make sure to select **IP_ADDRESS** as the variable type. If you don’t
   select a variable type, Amazon Fraud Detector assumes the list to be of **FREE_FORM_TEXT** variable type.

4. In the **Add list data**, add list entries, one entry in each line. You can also copy and paste entries from a spreadsheet.

###### Note

Make sure that the entries aren’t separated using a comma and are unique in the list. If two identical entries are entered, only one will be added. 5. Choose **Create**.

## Create list using the AWS SDK for Python (Boto3)

You create a list by specifying a list name. You can optionally provide a description, associate a variable type, or add entries to
your list when you are creating a list. Or, you can update the list later on by adding entries or a description. You can assign a variable type
to the list later if you haven't assigned it when at the time of list creation. Variable type of a list cannot be changed after it is assigned.

###### Important

If your list contains IP addresses, make sure to assign **IP_ADDRESS** as the variable type. If you don’t
assign a variable type, Amazon Fraud Detector assumes the list to be of **FREE_FORM_TEXT** variable type.

The following example uses [CreateList](../api/API_CreateList.md "../api/API_CreateList.md") API operation to create
an `allow_email_ids` list by providing a description, a variable type, and by adding four list entries.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_list (
     name = 'allow_email_ids',
     description = 'legitimate email_ids'
     variableType = 'EMAIL_ADDRESS',
     elements = ['emailId _1', 'emailId_2', 'emailId_3','emailId_4']
     )


```
