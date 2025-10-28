# Using universal targets in EventBridge Scheduler

A _universal target_ is a customizable set of parameters that allow you to invoke a wider set of API operation for many AWS services.
For example, you can use a universal target parameter (UTP) to create a new Amazon SQS queue using the [`CreateQueue`](../../../AWSSimpleQueueService/latest/APIReference/API_CreateQueue.md "../../../AWSSimpleQueueService/latest/APIReference/API_CreateQueue.md")
operation.

To configure a universal target for your schedule using the AWS CLI, or one of the EventBridge Scheduler SDKs, you need to specify the following information:

- RoleArn – The ARN for the execution role you want to use for the target. The execution role you specify must have the permissions to call the API operation
  you want your schedule to target.
- Arn – The complete service ARN, including the API operation you want to target, in the following format:
  `arn:aws:scheduler:::aws-sdk:`service`:`apiAction``.

For example, for Amazon SQS, the service name you specify is `arn:aws:scheduler:::aws-sdk:`sqs`:`sendMessage``.

- Input – A well-formed JSON you specify with the request parameters that EventBridge Scheduler sends to the target API. The parameters and shape of the JSON you set in `Input`
  are determined by the service API your schedule invokes. To find this information, see the API reference for the service you want to target.

## Unsupported actions

EventBridge Scheduler does not support read-only API actions, such as common `GET` operations, that begin with the following list of prefixes:

```
get
describe
list
poll
receive
search
scan
query
select
read
lookup
discover
validate
batchGet
batchDescribe
batchRead
transactGet
adminGet
adminList
testMigration
retrieve
testConnection
translateDocument
isAuthorized
invokeModel
```

For example, the service ARN for the [`GetQueueUrl`](../../../AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.md "../../../AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.md") API action would be the following:
`arn:aws:scheduler:::aws-sdk:sqs:`getQueueURL``. Since the API action starts with the `get` prefix, EventBridge Scheduler does not support this target.
 Similairly, the Amazon MQ action [`ListBrokers`](../../../amazon-mq/latest/api-reference/brokers.md#ListBrokers "../../../amazon-mq/latest/api-reference/brokers.md#ListBrokers") is not supported as a
 target because the operation begins with the prefix `list`.

## Examples using the universal target

The parameters you pass in the schedule `Input` field depend on the request parameterts that the service API you want to invoke accepts.
For example, to target Lambda [`Invoke`](../../../lambda/latest/dg/API_Invoke.md "../../../lambda/latest/dg/API_Invoke.md"),
you can set the the parameters listed in [AWS Lambda API Reference](../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestParameters "../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestParameters").
This includes the optional JSON [payload](../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestBody "../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestBody") that you can pass to a Lambda function.

To determine the parameters you can set for different APIs, see the API reference for that service. Similar to Lambda `Invoke`, some APIs accept URI parameters, as well as a request body payload.
In such cases, you specify the URI path parameters as well as the JSON payload in your schedule `Input`.

The following examples show how you to use the universal target to invoke common API operations with Lambda, Amazon SQS, and Step Functions.

###### Example Lambda

```
`$` `aws scheduler create-schedule --name lambda-universal-schedule --schedule-expression 'rate(5 minutes)' \
--target '{"RoleArn": "`ROLE_ARN`", "Arn":"arn:aws:scheduler:::aws-sdk:lambda:invoke" "Input": "{\"FunctionName\":\"arn:aws:lambda:`REGION`:123456789012:function:HelloWorld\",\"InvocationType\":\"Event\",\"Payload\":\"{\\\"message\\\":\\\"testing function\\\"}\"}" }' \
--flexible-time-window '{ "Mode": "OFF"}'`
```

###### Example Amazon SQS

```
import boto3
scheduler = boto3.client('scheduler')

flex_window = { "Mode": "OFF" }

sqs_universal= {
    "RoleArn": "<ROLE_ARN>",
    "Arn": "arn:aws:scheduler:::aws-sdk:sqs:sendMessage",
    "Input": "{\"MessageBody\":\"My message\",\"QueueUrl\":\"<QUEUE_URL>\"}"}
}

scheduler.create_schedule(
    Name="sqs-sdk-test",
    ScheduleExpression="rate(5 minutes)",
    Target=sqs_universal,
    FlexibleTimeWindow=flex_window)
```

###### Example Step Functions

```
package com.example;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.scheduler.SchedulerClient;
import software.amazon.awssdk.services.scheduler.model.*;


public class MySchedulerApp {

    public static void main(String[] args) {

        final SchedulerClient client = SchedulerClient.builder()
                .region(Region.US_WEST_2)
                .build();

        Target stepFunctionsUniversalTarget = Target.builder()
                .roleArn("<ROLE_ARN>")
                .arn("arn:aws:scheduler:::aws-sdk:sfn:startExecution")
                .input("{\"Input\":\"{}\",\"StateMachineArn\":\"<STATE_MACHINE_ARN>\"}")
                .build();

        CreateScheduleRequest createScheduleRequest = CreateScheduleRequest.builder()
                .name("<SCHEDULE_NAME>")
                .scheduleExpression("rate(10 minutes)")
                .target(stepFunctionsUniversalTarget)
                .flexibleTimeWindow(FlexibleTimeWindow.builder()
                        .mode(FlexibleTimeWindowMode.OFF)
                        .build())
                .clientToken("<Token GUID>")
                .build();

        client.createSchedule(createScheduleRequest);
        System.out.println("Created schedule with rate expression and Step Function universal target");
    }
}
```
