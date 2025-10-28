Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Import

a SageMaker AI model

You can optionally import SageMaker AI-hosted models to Amazon Fraud Detector. Similar to models, SageMaker AI models can be added to detectors and generate fraud predictions using the `GetEventPrediction` API. As part of the `GetEventPrediction` request, Amazon Fraud Detector will invoke your SageMaker AI endpoint and pass the results to your rules.

You can configure Amazon Fraud Detector to use the event variables sent as part of the `GetEventPrediction` request. If you choose to use event variables, you must provide an input template. Amazon Fraud Detector will use this template to transform your event variables into the required input payload to invoke the SageMaker AI endpoint. Alternatively, you can configure your SageMaker AI model to use a byteBuffer that is sent as part of the `GetEventPrediction` request.

Amazon Fraud Detector supports importing SageMaker AI algorithms that use JSON or CSV input formats and JSON or CSV output formats. Examples of supported SageMaker AI algorithms include XGBoost, Linear Learner, and Random Cut Forest.

## Import a SageMaker AI model using the AWS SDK for Python (Boto3)

To import a SageMaker AI model, use the `PutExternalModel` API. The following example assumes the SageMaker AI endpoint `sagemaker-transaction-model` has been deployed, is `InService` status, and uses the XGBoost algorithm.

The input configuration specifies that will use the event variables to construct the model input (`useEventVariables` is set to `TRUE`). The input format is TEXT_CSV, given XGBoost requires a CSV input. The csvInputTemplate specifies how to construct the CSV input from the variables sent as part of the `GetEventPrediction` request. This example assumes you have created the variables `order_amt`, `prev_amt`, `hist_amt` and `payment_type`.

The output configuration specifies the response format of the SageMaker AI model, and maps the appropriate CSV index to the Amazon Fraud Detector variable `sagemaker_output_score`. Once configured, you can use the output variable in rules.

###### Note

The output from a SageMaker AI model must be mapped to a variable with source `EXTERNAL_MODEL_SCORE`. You cannot create these variables in the console using **Variables**. You must instead create them when you configure your model import.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_external_model (
modelSource = 'SAGEMAKER',
modelEndpoint = 'sagemaker-transaction-model',
invokeModelEndpointRoleArn = 'your_SagemakerExecutionRole_arn',
inputConfiguration = {
    'useEventVariables' : True,
    'eventTypeName' : 'sample_transaction',
    'format' : 'TEXT_CSV',
    'csvInputTemplate' : '{{order_amt}}, {{prev_amt}}, {{hist_amt}}, {{payment_type}}'
},

outputConfiguration = {
    'format' : 'TEXT_CSV',
    'csvIndexToVariableMap' : {
        '0' : 'sagemaker_output_score'
    }
},

modelEndpointStatus = 'ASSOCIATED'
)

```
