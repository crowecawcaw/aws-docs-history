Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create a variable

You can create variables in the Amazon Fraud Detector console, using the [create-variable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-variable.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-variable.html") command,
using the [CreateVariable](../api/API_CreateVariable.md "../api/API_CreateVariable.md"), or using the AWS SDK for Python (Boto3)

## Create a variable using the Amazon Fraud Detector console

This example creates two variables, `email_address` and
`ip_address`, and assigns them to the corresponding variable types
(`EMAIL_ADDRESS` and `IP_ADDRESS`). These variables are used as examples.
If you are creating variables to use for your model training, use the variables from your dataset that are appropriate for your use case. Make sure to read about [Variable types](variables.md#variable-types "variables.md#variable-types") and
[Variable enrichments](variables.md#variable-enrichments "variables.md#variable-enrichments") before you create your variables.

###### To create a variable,

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
2. Navigate to Amazon Fraud Detector, choose
   **Variables** in the left navigation, then choose **Create**.
3. In the **New variable** page, enter `email_address` as the variable name.
   Optionally, enter a description of the variable.
4. In the **Variable type**, choose **Email Address**.
5. Amazon Fraud Detector automatically selects the data type for this variable type because this variable type is predefined. If your variable is not automatically assigned a variable type,
   select a variable type from the list. For more information,
   see [Variable types](variables.md#variable-types "variables.md#variable-types").
6. If you want to provide a default value for your variable,
   select **Define a custom default value** and enter a default value for your variable. Skip this step if you are following this example.
7. Choose **Create**.
8. In the **email_address** overview page, confirm the details of the variable you just created.

If you need to update, choose **Edit** and provide the updates. Choose **Save changes**. 9. Repeat the process to create another variable `ip_address` and choose **IP Address** for the variable type. 10. The **Variables** page shows the newly created variables.

###### Important

We recommend that you create as many variables as you want from your dataset. You can decide later when creating your event type which variables you want to include for training your model to detect fraud and to generate fraud detections.

## Create a variable using

the AWS SDK for Python (Boto3)

The following example shows requests for the [CreateVariable](../api/API_CreateVariable.md "../api/API_CreateVariable.md")
API. The example creates two variables, `email_address` and
`ip_address`, and assigns them to the corresponding variable types
(`EMAIL_ADDRESS` and `IP_ADDRESS`).

These variables are used as examples. If you are creating variables to use for your model training, use the variables
from your dataset that are appropriate for your use case. Make sure to read about [Variable types](variables.md#variable-types "variables.md#variable-types") and
[Variable enrichments](variables.md#variable-enrichments "variables.md#variable-enrichments") before you create your variables.

Be sure to specify a variable source. It helps to identify where the variable value is derived. If the variable source is **EVENT**,
the variable value is sent as part of the [GetEventPrediction](../api/API_GetEventPrediction.md "../api/API_GetEventPrediction.md") request.
If the variable value is `MODEL_SCORE`, it's populated by an Amazon Fraud Detector. If `EXTERNAL_MODEL_SCORE`, the variable value is populated by an imported SageMaker AI model.

```
import boto3
fraudDetector = boto3.client('frauddetector')

 #Create variable email_address
   fraudDetector.create_variable(
     name = 'email_address',
     variableType = 'EMAIL_ADDRESS',
     dataSource = 'EVENT',
     dataType = 'STRING',
     defaultValue = '<unknown>'
     )

#Create variable ip_address
   fraudDetector.create_variable(
     name = 'ip_address',
     variableType = 'IP_ADDRESS',
     dataSource = 'EVENT',
     dataType = 'STRING',
     defaultValue = '<unknown>'
     )

```
