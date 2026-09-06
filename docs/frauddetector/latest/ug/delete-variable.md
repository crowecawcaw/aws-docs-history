

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete a variable
<a name="delete-variable"></a>

When you delete a variable, Amazon Fraud Detector permanently deletes that variable and the data is no longer stored in Amazon Fraud Detector.

You can't delete variables that are included in an event type in Amazon Fraud Detector. You will have to first delete the event type the variable is associated with and then delete the variable.

You can't delete Amazon Fraud Detector model output variables and SageMaker AI model output variables manually. Amazon Fraud Detector automatically deletes model output variables when you delete the model.

You can delete variable in Amazon Fraud Detector console, using the [delete-variable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-variable.html) CLI command, using the [DeleteVariable](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteVariable.html) API, or using the AWS SDK for Python (Boto3)

## Delete variable using the console
<a name="delete-variable-console"></a>

**To delete a variable,**

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector).

1. In the left navigation pane of the Amazon Fraud Detector console, choose **Resources**, then choose **Variables**.

1. Choose the variable that you want to delete.

1. Choose **Actions**, and then choose **Delete**.

1. Enter the variable name, and then choose **Delete variable**.

## Delete variable using the AWS SDK for Python (Boto3)
<a name="delete-variable-using-the-aws-python-sdk"></a>

The following code sample deletes a variable *customer\_name* using the [DeleteVariable](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteVariable.html) API.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.delete_variable (

name = 'customer_name'

)
```