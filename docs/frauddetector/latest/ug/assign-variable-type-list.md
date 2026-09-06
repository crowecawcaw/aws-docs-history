

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Assign a variable type to a list
<a name="assign-variable-type-list"></a>

Every list you use in a rule must be associated with an Amazon Fraud Detector's [Variable types](variables.md#variable-types) variable type. By default, Amazon Fraud Detector assumes the list to be of FREE\_FORM\_TEXT variable type. It is important to note that a list that consists of IP addresses must be associated with IP\_ADDRESS variable type.

You can associate your list with a variable type either at the time of list creation or anytime later. If you already associated your list with a variable type and want to change it later, you must create a new list. You can’t change the variable type of a list. 

You can assign a variable type in the Amazon Fraud Detector console, using the API, using the AWS CLI, or using the AWS SDK. 

## Assign variable type to a list using the Amazon Fraud Detector console
<a name="assign-variable-type-list-console"></a>

**To assign a variable type to a list**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

1. In the left navigation pane, choose **Lists**.

1. In the **Lists** page, select the list that you want to assign a variable type.

1. In your list details page, choose **Actions** and select **Edit list**.

1. In the **Edit list** box, select the variable type for your list.

1. Choose **Save**.

## Assign variable type to a list using the AWS SDK for Python (Boto3)
<a name="assign-variable-type-list-sdk"></a>

The following example uses the [UpdateList](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateList.html) API operation to assign a variable type to `allow_ip_address` list.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.update_list (
     name = 'allow_ip_address',
     variableType = 'IP_ADDRESS'     
)
```