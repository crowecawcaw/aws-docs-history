# Code examples for Amazon SQS using AWS SDKs

The following code examples show how to use Amazon SQS with an AWS software development kit (SDK).

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SQS with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Amazon SQS](example_sqs_Hello_section.md "example_sqs_Hello_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [AddPermission](example_sqs_AddPermission_section.md "example_sqs_AddPermission_section.md")
    - [ChangeMessageVisibility](example_sqs_ChangeMessageVisibility_section.md "example_sqs_ChangeMessageVisibility_section.md")
    - [ChangeMessageVisibilityBatch](example_sqs_ChangeMessageVisibilityBatch_section.md "example_sqs_ChangeMessageVisibilityBatch_section.md")
    - [CreateQueue](example_sqs_CreateQueue_section.md "example_sqs_CreateQueue_section.md")
    - [DeleteMessage](example_sqs_DeleteMessage_section.md "example_sqs_DeleteMessage_section.md")
    - [DeleteMessageBatch](example_sqs_DeleteMessageBatch_section.md "example_sqs_DeleteMessageBatch_section.md")
    - [DeleteQueue](example_sqs_DeleteQueue_section.md "example_sqs_DeleteQueue_section.md")
    - [GetQueueAttributes](example_sqs_GetQueueAttributes_section.md "example_sqs_GetQueueAttributes_section.md")
    - [GetQueueUrl](example_sqs_GetQueueUrl_section.md "example_sqs_GetQueueUrl_section.md")
    - [ListDeadLetterSourceQueues](example_sqs_ListDeadLetterSourceQueues_section.md "example_sqs_ListDeadLetterSourceQueues_section.md")
    - [ListQueues](example_sqs_ListQueues_section.md "example_sqs_ListQueues_section.md")
    - [PurgeQueue](example_sqs_PurgeQueue_section.md "example_sqs_PurgeQueue_section.md")
    - [ReceiveMessage](example_sqs_ReceiveMessage_section.md "example_sqs_ReceiveMessage_section.md")
    - [RemovePermission](example_sqs_RemovePermission_section.md "example_sqs_RemovePermission_section.md")
    - [SendMessage](example_sqs_SendMessage_section.md "example_sqs_SendMessage_section.md")
    - [SendMessageBatch](example_sqs_SendMessageBatch_section.md "example_sqs_SendMessageBatch_section.md")
    - [SetQueueAttributes](example_sqs_SetQueueAttributes_section.md "example_sqs_SetQueueAttributes_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Create a messaging application](example_cross_SQSMessageApp_section.md "example_cross_SQSMessageApp_section.md")
  - [Create a messenger application](example_cross_StepFunctionsMessenger_section.md "example_cross_StepFunctionsMessenger_section.md")
  - [Create an Amazon Textract explorer application](example_cross_TextractExplorer_section.md "example_cross_TextractExplorer_section.md")
  - [Create and publish to a FIFO topic](example_sns_PublishFifoTopic_section.md "example_sns_PublishFifoTopic_section.md")
  - [Detect people and objects in a video](example_cross_RekognitionVideoDetection_section.md "example_cross_RekognitionVideoDetection_section.md")
  - [Manage large messages using S3](example_sqs_Scenario_SqsExtendedClient_section.md "example_sqs_Scenario_SqsExtendedClient_section.md")
  - [Process S3 event notifications](example_s3_Scenario_ProcessS3EventNotification_section.md "example_s3_Scenario_ProcessS3EventNotification_section.md")
  - [Publish messages to queues](example_sqs_Scenario_TopicsAndQueues_section.md "example_sqs_Scenario_TopicsAndQueues_section.md")
  - [Send and receive batches of messages](example_sqs_Scenario_SendReceiveBatch_section.md "example_sqs_Scenario_SendReceiveBatch_section.md")
  - [Use the AWS Message Processing Framework for .NET with Amazon SQS](example_cross_MessageProcessingFrameworkTutorial_section.md "example_cross_MessageProcessingFrameworkTutorial_section.md")
  - [Use the Amazon SQS Java Messaging Library to work with the JMS interface](example_sqs_Scenario_UseJMS_section.md "example_sqs_Scenario_UseJMS_section.md")
  - [Work with queue tags](example_sqs_Scenario_WorkWithTags_section.md "example_sqs_Scenario_WorkWithTags_section.md")

- [Serverless examples](service_code_examples_serverless_examples.md "service_code_examples_serverless_examples.md")
  - [Invoke a Lambda function from an Amazon SQS trigger](example_serverless_SQS_Lambda_section.md "example_serverless_SQS_Lambda_section.md")
  - [Reporting batch item failures for Lambda functions with an Amazon SQS trigger](example_serverless_SQS_Lambda_batch_item_failures_section.md "example_serverless_SQS_Lambda_batch_item_failures_section.md")
