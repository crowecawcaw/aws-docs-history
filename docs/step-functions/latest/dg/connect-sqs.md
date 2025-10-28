# Send messages to an Amazon SQS queue with Step Functions

You can to send messages to an Amazon SQS queue using the following Amazon SQS API actions and
example `Task` state code for Step Functions workflows.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

To learn more about receiving messages in Amazon SQS, see [Receive and
Delete Your Message](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/step-receive-delete-message.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/step-receive-delete-message.md") in the _Amazon Simple Queue Service Developer Guide_.

The following sample includes a `Task` state (JSONata) that sends an Amazon Simple Queue Service (Amazon SQS)
message with optional **MessageAttributes**:

```
{
 "StartAt": "Send to SQS",
 "States": {
   "Send to SQS": {
     "Type": "Task",
     "Resource": "arn:aws:states:::sqs:sendMessage",
     "Arguments": {
       "QueueUrl": "https://sqs.us-east-1.amazonaws.com/`account-id`/myQueue",
       "MessageBody": "{% $states.input.message %}",
       "MessageAttributes": {
         "my_attribute_no_1": {
           "DataType": "String",
           "StringValue": "`attribute1`"
         },
         "my_attribute_no_2": {
           "DataType": "String",
           "StringValue": "`attribute2`"
         }
       }
     },
     "End": true
    }
  }
}
```

The following state machine includes a `Task` state that publishes to an Amazon SQS queue, and
then waits for the task token to be returned. See [Wait for a Callback with Task Token](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token").

```
{
   "StartAt":"Send message to SQS",
   "States":{
      "Send message to SQS":{
         "Type":"Task",
         "Resource":"arn:aws:states:::sqs:sendMessage.waitForTaskToken",
         "Arguments":{
            "QueueUrl":"https://sqs.us-east-1.amazonaws.com/`account-id`/myQueue",
            "MessageBody":{
               "Input" : "{% $states.input.message %}",
               "MyTaskToken" : "{% $states.context.Task.Token %}"
            }
         },
         "End":true
      }
   }
}
```

## Optimized Amazon SQS APIs

- [`SendMessage`](../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md")

###### Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`.

###### Quota for input or result data

When sending or receiving data between services, the maximum input or result for a task is 256 KiB of data as a UTF-8 encoded string. See [Quotas related to state
machine executions](service-quotas.md#service-limits-state-machine-executions "service-quotas.md#service-limits-state-machine-executions").

## IAM policies for calling Amazon SQS

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sqs:SendMessage"
 ],
 "Resource": [
 "arn:aws:sqs:`us-east-1`:`123456789012`:myQueueName"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sqs:SendMessage"
 ],
 "Resource": "*"
 }
 ]
}`

```
