

# Integration subtype reference
<a name="http-api-develop-integrations-aws-services-reference"></a>

The following [integration subtypes](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-integrations-integrationid.html#apis-apiid-integrations-integrationid-prop-integration-integrationsubtype) are supported for HTTP APIs.

**Topics**
+ [EventBridge-PutEvents 1.0](#EventBridge-PutEvents)
+ [SQS-SendMessage 1.0](#SQS-SendMessage)
+ [SQS-ReceiveMessage 1.0](#SQS-ReceiveMessage)
+ [SQS-DeleteMessage 1.0](#SQS-DeleteMessage)
+ [SQS-PurgeQueue 1.0](#SQS-PurgeQueue)
+ [AppConfig-GetConfiguration 1.0](#AppConfig-GetConfiguration)
+ [Kinesis-PutRecord 1.0](#Kinesis-PutRecord)
+ [StepFunctions-StartExecution 1.0](#StepFunctions-StartExecution)
+ [StepFunctions-StartSyncExecution 1.0](#StepFunctions-StartSyncExecution)
+ [StepFunctions-StopExecution 1.0](#StepFunctions-StopExecution)

## EventBridge-PutEvents 1.0
<a name="EventBridge-PutEvents"></a>

Sends custom events to Amazon EventBridge so that they can be matched to rules.


| Parameter | Required | 
| --- | --- | 
| Detail | True | 
| DetailType | True | 
| Source | True | 
| Time | False | 
| EventBusName | False | 
| Resources | False | 
| Region | False | 
| TraceHeader | False | 

To learn more, see [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) in the *Amazon EventBridge API Reference*.

## SQS-SendMessage 1.0
<a name="SQS-SendMessage"></a>

Delivers a message to the specified queue.


| Parameter | Required | 
| --- | --- | 
| QueueUrl | True | 
| MessageBody | True | 
| DelaySeconds | False | 
| MessageAttributes | False | 
| MessageDeduplicationId | False | 
| MessageGroupId | False | 
| MessageSystemAttributes | False | 
| Region | False | 

To learn more, see [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) in the *Amazon Simple Queue Service API Reference*.

## SQS-ReceiveMessage 1.0
<a name="SQS-ReceiveMessage"></a>

Retrieves one or more messages (up to 10), from the specified queue.


| Parameter | Required | 
| --- | --- | 
| QueueUrl | True | 
| AttributeNames | False | 
| MaxNumberOfMessages | False | 
| MessageAttributeNames | False | 
| ReceiveRequestAttemptId | False | 
| VisibilityTimeout | False | 
| WaitTimeSeconds | False | 
| Region | False | 

To learn more, see [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) in the *Amazon Simple Queue Service API Reference*.

## SQS-DeleteMessage 1.0
<a name="SQS-DeleteMessage"></a>

Deletes the specified message from the specified queue.


| Parameter | Required | 
| --- | --- | 
| ReceiptHandle | True | 
| QueueUrl | True | 
| Region | False | 

To learn more, see [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html) in the *Amazon Simple Queue Service API Reference*.

## SQS-PurgeQueue 1.0
<a name="SQS-PurgeQueue"></a>

Deletes all messages in the specified queue.


| Parameter | Required | 
| --- | --- | 
| QueueUrl | True | 
| Region | False | 

To learn more, see [PurgeQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.html) in the *Amazon Simple Queue Service API Reference*.

## AppConfig-GetConfiguration 1.0
<a name="AppConfig-GetConfiguration"></a>

Receive information about a configuration.


| Parameter | Required | 
| --- | --- | 
| Application | True | 
| Environment | True | 
| Configuration | True | 
| ClientId | True | 
| ClientConfigurationVersion | False | 
| Region | False | 

To learn more, see [GetConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfiguration.html) in the *AWS AppConfig API Reference*.

## Kinesis-PutRecord 1.0
<a name="Kinesis-PutRecord"></a>

Writes a single data record into an Amazon Kinesis data stream.


| Parameter | Required | 
| --- | --- | 
| StreamName | True | 
| Data | True | 
| PartitionKey | True | 
| SequenceNumberForOrdering | False | 
| ExplicitHashKey | False | 
| Region | False | 

To learn more, see [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) in the *Amazon Kinesis Data Streams API Reference*.

## StepFunctions-StartExecution 1.0
<a name="StepFunctions-StartExecution"></a>

Starts a state machine execution.


| Parameter | Required | 
| --- | --- | 
| StateMachineArn | True | 
| Name | False | 
| Input | False | 
| Region | False | 

To learn more, see [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) in the *AWS Step Functions API Reference*.

## StepFunctions-StartSyncExecution 1.0
<a name="StepFunctions-StartSyncExecution"></a>

Starts a synchronous state machine execution.


| Parameter | Required | 
| --- | --- | 
| StateMachineArn | True | 
| Name | False | 
| Input | False | 
| Region | False | 
| TraceHeader | False | 

To learn more, see [StartSyncExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html) in the *AWS Step Functions API Reference*.

## StepFunctions-StopExecution 1.0
<a name="StepFunctions-StopExecution"></a>

Stops an execution.


| Parameter | Required | 
| --- | --- | 
| ExecutionArn | True | 
| Cause | False | 
| Error | False | 
| Region | False | 

To learn more, see [StopExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StopExecution.html) in the *AWS Step Functions API Reference*.