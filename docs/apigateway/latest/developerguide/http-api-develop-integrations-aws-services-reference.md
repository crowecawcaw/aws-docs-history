# Integration subtype reference

The following
[integration subtypes](../../../apigatewayv2/latest/api-reference/apis-apiid-integrations-integrationid.md#apis-apiid-integrations-integrationid-prop-integration-integrationsubtype "../../../apigatewayv2/latest/api-reference/apis-apiid-integrations-integrationid.md#apis-apiid-integrations-integrationid-prop-integration-integrationsubtype") are supported for HTTP APIs.

###### Integration subtypes

- [EventBridge-PutEvents 1.0](#EventBridge-PutEvents "#EventBridge-PutEvents")
- [SQS-SendMessage 1.0](#SQS-SendMessage "#SQS-SendMessage")
- [SQS-ReceiveMessage 1.0](#SQS-ReceiveMessage "#SQS-ReceiveMessage")
- [SQS-DeleteMessage 1.0](#SQS-DeleteMessage "#SQS-DeleteMessage")
- [SQS-PurgeQueue 1.0](#SQS-PurgeQueue "#SQS-PurgeQueue")
- [AppConfig-GetConfiguration 1.0](#AppConfig-GetConfiguration "#AppConfig-GetConfiguration")
- [Kinesis-PutRecord 1.0](#Kinesis-PutRecord "#Kinesis-PutRecord")
- [StepFunctions-StartExecution 1.0](#StepFunctions-StartExecution "#StepFunctions-StartExecution")
- [StepFunctions-StartSyncExecution 1.0](#StepFunctions-StartSyncExecution "#StepFunctions-StartSyncExecution")
- [StepFunctions-StopExecution 1.0](#StepFunctions-StopExecution "#StepFunctions-StopExecution")

## EventBridge-PutEvents 1.0

Sends custom events to Amazon EventBridge so that they can be matched to rules.

| Parameter    | Required |
| ------------ | -------- |
| Detail       | True     |
| DetailType   | True     |
| Source       | True     |
| Time         | False    |
| EventBusName | False    |
| Resources    | False    |
| Region       | False    |
| TraceHeader  | False    |

To learn more, see [PutEvents](../../../eventbridge/latest/APIReference/API_PutEvents.md "../../../eventbridge/latest/APIReference/API_PutEvents.md") in the
_Amazon EventBridge API Reference_.

## SQS-SendMessage 1.0

Delivers a message to the specified queue.

| Parameter               | Required |
| ----------------------- | -------- |
| QueueUrl                | True     |
| MessageBody             | True     |
| DelaySeconds            | False    |
| MessageAttributes       | False    |
| MessageDeduplicationId  | False    |
| MessageGroupId          | False    |
| MessageSystemAttributes | False    |
| Region                  | False    |

To learn more, see [SendMessage](../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md") in the
_Amazon Simple Queue Service API Reference_.

## SQS-ReceiveMessage 1.0

Retrieves one or more messages (up to 10), from the specified queue.

| Parameter               | Required |
| ----------------------- | -------- |
| QueueUrl                | True     |
| AttributeNames          | False    |
| MaxNumberOfMessages     | False    |
| MessageAttributeNames   | False    |
| ReceiveRequestAttemptId | False    |
| VisibilityTimeout       | False    |
| WaitTimeSeconds         | False    |
| Region                  | False    |

To learn more, see [ReceiveMessage](../../../AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.md") in
the _Amazon Simple Queue Service API Reference_.

## SQS-DeleteMessage 1.0

Deletes the specified message from the specified queue.

| Parameter     | Required |
| ------------- | -------- |
| ReceiptHandle | True     |
| QueueUrl      | True     |
| Region        | False    |

To learn more, see [DeleteMessage](../../../AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.md") in the
_Amazon Simple Queue Service API Reference_.

## SQS-PurgeQueue 1.0

Deletes all messages in the specified queue.

| Parameter | Required |
| --------- | -------- |
| QueueUrl  | True     |
| Region    | False    |

To learn more, see [PurgeQueue](../../../AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.md "../../../AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.md") in the
_Amazon Simple Queue Service API Reference_.

## AppConfig-GetConfiguration 1.0

Receive information about a configuration.

| Parameter                  | Required |
| -------------------------- | -------- |
| Application                | True     |
| Environment                | True     |
| Configuration              | True     |
| ClientId                   | True     |
| ClientConfigurationVersion | False    |
| Region                     | False    |

To learn more, see [GetConfiguration](../../../appconfig/2019-10-09/APIReference/API_GetConfiguration.md "../../../appconfig/2019-10-09/APIReference/API_GetConfiguration.md") in
the _AWS AppConfig API Reference_.

## Kinesis-PutRecord 1.0

Writes a single data record into an Amazon Kinesis data stream.

| Parameter                 | Required |
| ------------------------- | -------- |
| StreamName                | True     |
| Data                      | True     |
| PartitionKey              | True     |
| SequenceNumberForOrdering | False    |
| ExplicitHashKey           | False    |
| Region                    | False    |

To learn more, see [PutRecord](../../../kinesis/latest/APIReference/API_PutRecord.md "../../../kinesis/latest/APIReference/API_PutRecord.md") in the
_Amazon Kinesis Data Streams API Reference_.

## StepFunctions-StartExecution 1.0

Starts a state machine execution.

| Parameter       | Required |
| --------------- | -------- |
| StateMachineArn | True     |
| Name            | False    |
| Input           | False    |
| Region          | False    |

To learn more, see [StartExecution](../../../step-functions/latest/apireference/API_StartExecution.md "../../../step-functions/latest/apireference/API_StartExecution.md") in
the _AWS Step Functions API Reference_.

## StepFunctions-StartSyncExecution 1.0

Starts a synchronous state machine execution.

| Parameter       | Required |
| --------------- | -------- |
| StateMachineArn | True     |
| Name            | False    |
| Input           | False    |
| Region          | False    |
| TraceHeader     | False    |

To learn more, see [StartSyncExecution](../../../step-functions/latest/apireference/API_StartSyncExecution.md "../../../step-functions/latest/apireference/API_StartSyncExecution.md") in the
_AWS Step Functions API Reference_.

## StepFunctions-StopExecution 1.0

Stops an execution.

| Parameter    | Required |
| ------------ | -------- |
| ExecutionArn | True     |
| Cause        | False    |
| Error        | False    |
| Region       | False    |

To learn more, see [StopExecution](../../../step-functions/latest/apireference/API_StopExecution.md "../../../step-functions/latest/apireference/API_StopExecution.md") in the
_AWS Step Functions API Reference_.
