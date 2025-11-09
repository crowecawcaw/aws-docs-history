Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete a variable

When you delete a variable, Amazon Fraud Detector permanently deletes that variable and the data is no longer stored in Amazon Fraud Detector.

You can't delete variables that are included in an event type in Amazon Fraud Detector. You will have to first delete the event type the variable is associated with and then delete the variable.

You can't delete Amazon Fraud Detector model output variables and SageMaker AI model output variables manually. Amazon Fraud Detector automatically deletes model output variables when you delete the model.

You can delete variable in Amazon Fraud Detector console, using the [delete-variable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-variable.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-variable.html") CLI command, using the [DeleteVariable](../api/API_DeleteVariable.md "../api/API_DeleteVariable.md") API, or using the AWS SDK for Python (Boto3)

## Delete variable using the console

###### To delete a variable,

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector").
2. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Resources**, then choose
   **Variables**.
3. Choose the variable that you want to delete.
4. Choose **Actions**, and then choose
   **Delete**.
5. Enter the variable name, and then choose **Delete
   variable**.

## Delete variable using the AWS SDK for Python (Boto3)

The following code sample deletes a variable _customer_name_ using the [DeleteVariable](../api/API_DeleteVariable.md "../api/API_DeleteVariable.md") API.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.delete_variable (

name = 'customer_name'

)

```
