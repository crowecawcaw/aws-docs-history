

# Using templated targets in EventBridge Scheduler
<a name="managing-targets-templated"></a>

 *Templated targets* are a set of common API operations across a group of core AWS services, such as Amazon SQS, Lambda, and Step Functions. For example, you can target Lambda's [`Invoke`](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke) operation by providing the function ARN, or Amazon SQS's [`SendMessage`](https://docs.aws.amazon.com/) operation using the queue ARN. To configure a templated target, you must also grant permissions to the schedule's execution role to perform the targeted API operation. 

 To configure a templated target programatically using the AWS CLI or one of the EventBridge Scheduler SDKs, you need to specify the ARN of the execution role, the ARN for target resource, an optional input that you want EventBridge Scheduler to deliver to the target, and for some templated targets, a unique set of parameters with additional configuration options for that target. When you specify the ARN for a templated target resource, EventBridge Scheduler automatically assumes that you want to call the supported API operation for that service. If you want EventBridge Scheduler to target a different API operation for the service, you must configure the target as a [universal target](managing-targets-universal.md). 

 The following is a complete list of all templated targets that EventBridge Scheduler supports, and if applicable, each target's unique set of associated parameters. Choose the link for each parameter set to see the required, and optional, fields in the *EventBridge Scheduler API Reference*. 
+ **CodeBuild** – [`StartBuild`](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuild.html)
+ **CodePipeline** – [`StartPipelineExecution`](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StartPipelineExecution.html)
+ **Amazon ECS** – [`RunTask`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html)
  + Parameters: [`EcsParameters`](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_EcsParameters.html)
+ **EventBridge** – [`PutEvents`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)
  + Parameters: [`EventBridgeParameters`](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_EventBridgeParameters.html)
**Important**  
EventBridge Scheduler does not support cross-Region delivery when using EventBridge `PutEvents` as a templated target. You can use this target to send events to an event bus in a different AWS account only if the event bus is in the same AWS Region as the schedule. To send events to an event bus in a different Region, create a schedule in the Region where the target event bus is located.
+ **Amazon Inspector** – [`StartAssessmentRun`](https://docs.aws.amazon.com/inspector/v1/APIReference/API_StartAssessmentRun.html)
+ **Kinesis** – [`PutRecord`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html)
  + Parameters: [`KinesisParameters`](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_KinesisParameters.html)
+ **Firehose** – [`PutRecord`](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecord.html)
+ **Lambda** – [`Invoke`](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html)
+ **SageMaker AI** – [`StartPipelineExecution`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html)
  + Parameters: [`SageMakerPipelineParameters`](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_SageMakerPipelineParameters.html)
+ **Amazon SNS** – [`Publish`](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html)
+ **Amazon SQS** – [`SendMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html)
  + Parameters: [`SqsParameters`](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_SqsParameters.html)
+ **Step Functions** – [`StartExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html)

 Use the following examples to learn how to configure different templated targets, and the required IAM permissions for each described target. 

## Amazon SQS `SendMessage`
<a name="managing-targets-templated-sqs"></a>

**Example Permission policy for execution role**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "sqs:SendMessage"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

**Example AWS CLI**  

```
$ aws scheduler create-schedule --name sqs-templated --schedule-expression 'rate(5 minutes)' \
--target '{"RoleArn": "{{ROLE_ARN}}", "Arn":"{{QUEUE_ARN}}", "Input": "Message for scheduleArn: '<aws.scheduler.schedule-arn>', scheduledTime: '<aws.scheduler.scheduled-time>'" }' \
--flexible-time-window '{ "Mode": "OFF"}'
```

**Example Python SDK**  

```
import boto3
scheduler = boto3.client('scheduler')

flex_window = { "Mode": "OFF" }

sqs_templated = {
    "RoleArn": "<ROLE_ARN>",
    "Arn": "<QUEUE_ARN>",
    "Input": "Message for scheduleArn: '<aws.scheduler.schedule-arn>', scheduledTime: '<aws.scheduler.scheduled-time>'"
}

scheduler.create_schedule(
    Name="sqs-python-templated",
    ScheduleExpression="rate(5 minutes)",
    Target=sqs_templated,
    FlexibleTimeWindow=flex_window)
```

**Example Java SDK**  

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
        
        Target sqsTarget = Target.builder()
                .roleArn("<ROLE_ARN>")
                .arn("<QUEUE_ARN>")
                .input("Message for scheduleArn: '<aws.scheduler.schedule-arn>', scheduledTime: '<aws.scheduler.scheduled-time>'")
                .build();
        
        CreateScheduleRequest createScheduleRequest = CreateScheduleRequest.builder()
                .name("<SCHEDULE NAME>")
                .scheduleExpression("rate(10 minutes)")
                .target(sqsTarget)
                .flexibleTimeWindow(FlexibleTimeWindow.builder()
                        .mode(FlexibleTimeWindowMode.OFF)
                        .build())
                .build();
                
        client.createSchedule(createScheduleRequest);
        System.out.println("Created schedule with rate expression and an Amazon SQS templated target");
    }
}
```

## Lambda `Invoke`
<a name="managing-targets-templated-lambda"></a>

**Example Permission policy for execution role**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

**Example AWS CLI**  

```
$ aws scheduler create-schedule --name lambda-templated-schedule --schedule-expression 'rate(5 minutes)' \
--target '{"RoleArn": "{{ROLE_ARN}}", "Arn":"{{FUNCTION_ARN}}", "Input": "{ \"Payload\": \"TEST_PAYLOAD\" }" }' \
--flexible-time-window '{ "Mode": "OFF"}'
```

**Example Python SDK**  

```
import boto3
scheduler = boto3.client('scheduler')

flex_window = { "Mode": "OFF" }

lambda_templated = {
    "RoleArn": "<ROLE_ARN>",
    "Arn": "<LAMBDA_ARN>",
    "Input": "{ 'Payload': 'TEST_PAYLOAD' }"}
}

scheduler.create_schedule(
    Name="lambda-python-templated",
    ScheduleExpression="rate(5 minutes)",
    Target=lambda_templated,
    FlexibleTimeWindow=flex_window)
```

**Example Java SDK**  

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
                
        Target lambdaTarget = Target.builder()
                .roleArn("<ROLE_ARN>")
                .arn("<Lambda ARN>")
                .input("{ 'Payload': 'TEST_PAYLOAD' }")
                .build();
        
        CreateScheduleRequest createScheduleRequest = CreateScheduleRequest.builder()
                .name("<SCHEDULE_NAME>")
                .scheduleExpression("rate(10 minutes)")
                .target(lambdaTarget)
                .flexibleTimeWindow(FlexibleTimeWindow.builder()
                        .mode(FlexibleTimeWindowMode.OFF)
                        .build())
                .clientToken("<Token GUID>")
                .build();
                
        client.createSchedule(createScheduleRequest);
        System.out.println("Created schedule with rate expression and Lambda templated target");        
    }
}
```

## Step Functions `StartExecution`
<a name="managing-targets-templated-sfn"></a>

**Example Permission policy for execution role**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "states:StartExecution"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

**Example AWS CLI**  

```
$ aws scheduler create-schedule --name sfn-templated-schedule --schedule-expression 'rate(5 minutes)' \
--target '{"RoleArn": "{{ROLE_ARN}}", "Arn":"{{STATE_MACHINE_ARN}}", "Input": "{ \"Payload\": \"TEST_PAYLOAD\" }" }' \
--flexible-time-window '{ "Mode": "OFF"}'
```

**Example Python SDK**  

```
import boto3
scheduler = boto3.client('scheduler')

flex_window = { "Mode": "OFF" }

sfn_templated= {
    "RoleArn": "<ROLE_ARN>",
    "Arn": "<STATE_MACHINE_ARN>",
    "Input": "{ 'Payload': 'TEST_PAYLOAD' }"
}

scheduler.create_schedule(Name="sfn-python-templated",
    ScheduleExpression="rate(5 minutes)",
    Target=sfn_templated,
    FlexibleTimeWindow=flex_window)
```

**Example Java SDK**  

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
                
        Target stepFunctionsTarget = Target.builder()
                .roleArn("<ROLE_ARN>")
                .arn("<STATE_MACHINE_ARN>")
                .input("{ 'Payload': 'TEST_PAYLOAD' }")
                .build();
        
        CreateScheduleRequest createScheduleRequest = CreateScheduleRequest.builder()
                .name("<SCHEDULE_NAME>")
                .scheduleExpression("rate(10 minutes)")
                .target(stepFunctionsTarget)
                .flexibleTimeWindow(FlexibleTimeWindow.builder()
                        .mode(FlexibleTimeWindowMode.OFF)
                        .build())
                .clientToken("<Token GUID>")
                .build();
                
        client.createSchedule(createScheduleRequest);
        System.out.println("Created schedule with rate expression and Step Function templated target");
    }
}
```