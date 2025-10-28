# Invoking Lambda with events from other AWS services

Some AWS services can directly invoke Lambda functions using _triggers_. These services push events to Lambda, and the function is invoked immediately when the specified event occurs. Triggers are suitable for discrete events and real-time processing. When you [create a trigger using the Lambda console](#lambda-invocation-trigger "#lambda-invocation-trigger"), the console interacts with the corresponding AWS service to configure the event notification on that service. The trigger is actually stored and managed by the service that generates the events, not by Lambda.

The events are data structured in JSON format. The JSON structure varies depending on the service that
generates it and the event type, but they all contain the data that the function needs to process the
event.

A function can have multiple triggers. Each trigger acts as a client invoking your function independently, and each event that
Lambda passes to your function has data from only one trigger. Lambda converts the event document into an object and passes it to your function handler.

Depending on the service, the event-driven invocation can be [synchronous](invocation-sync.md "invocation-sync.md") or [asynchronous](invocation-async.md "invocation-async.md").

- For synchronous invocation, the service that generates the event waits for the response from your
  function. That service defines the data that the function needs to return in the response. The service
  controls the error strategy, such as whether to retry on errors.
- For asynchronous invocation, Lambda queues the event before passing it to your function. When Lambda
  queues the event, it immediately sends a success response to the service that generated the event. After the
  function processes the event, Lambda doesn’t return a response to the event-generating service.

## Creating a trigger

The easiest way to create a trigger is to use the Lambda console. When you create a trigger using the console, Lambda automatically adds the required permissions to the function's [resource-based policy](access-control-resource-based.md "access-control-resource-based.md").

###### To create a trigger using the Lambda console

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the function you want to create a trigger for.
3. In the **Function overview** pane, choose
   **Add trigger**.
4. Select the AWS service you want to invoke your function.
5. Fill out the options in the **Trigger configuration** pane
   and choose **Add**. Depending on the AWS service you choose to
   invoke your function, the trigger configuration options will be different.

## Services that can invoke Lambda functions

The following table lists services that can invoke Lambda functions.

| Service                                                                                                                                                                                           | Method of invocation                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [Amazon Managed Streaming for Apache Kafka](with-msk.md "with-msk.md")                                                                                                                            | [Event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md")                       |
| [Self-managed Apache Kafka](with-kafka.md "with-kafka.md")                                                                                                                                        | [Event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md")                       |
| [Amazon API Gateway](services-apigateway.md "services-apigateway.md")                                                                                                                             | Event-driven; synchronous invocation                                                                              |
| [AWS CloudFormation](services-cloudformation.md "services-cloudformation.md")                                                                                                                     | Event-driven; asynchronous invocation                                                                             |
| [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/SubscriptionFilters.md#LambdaFunctionExample "../../../AmazonCloudWatch/latest/logs/SubscriptionFilters.md#LambdaFunctionExample") | Event-driven; asynchronous invocation                                                                             |
| [AWS CodeCommit](../../../codecommit/latest/userguide/how-to-notify-lambda-cc.md "../../../codecommit/latest/userguide/how-to-notify-lambda-cc.md")                                               | Event-driven; asynchronous invocation                                                                             |
| [AWS CodePipeline](../../../codepipeline/latest/userguide/actions-invoke-lambda-function.md "../../../codepipeline/latest/userguide/actions-invoke-lambda-function.md")                           | Event-driven; asynchronous invocation                                                                             |
| [Amazon Cognito](../../../cognito/latest/developerguide/cognito-events.md "../../../cognito/latest/developerguide/cognito-events.md")                                                             | Event-driven; synchronous invocation                                                                              |
| [AWS Config](governance-config.md "governance-config.md")                                                                                                                                         | Event-driven; asynchronous invocation                                                                             |
| [Amazon Connect](../../../connect/latest/adminguide/connect-lambda-functions.md "../../../connect/latest/adminguide/connect-lambda-functions.md")                                                 | Event-driven; synchronous invocation                                                                              |
| [Amazon DocumentDB](with-documentdb.md "with-documentdb.md")                                                                                                                                      | [Event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md")                       |
| [Amazon DynamoDB](with-ddb.md "with-ddb.md")                                                                                                                                                      | [Event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md")                       |
| [Elastic Load Balancing (Application Load Balancer)](services-alb.md "services-alb.md")                                                                                                           | Event-driven; synchronous invocation                                                                              |
| [Amazon EventBridge (CloudWatch Events)](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")                                               | Event-driven; asynchronous invocation (event buses), synchronous or asynchronous invocation (pipes and schedules) |
| [AWS IoT](services-iot.md "services-iot.md")                                                                                                                                                      | Event-driven; asynchronous invocation                                                                             |
| [Amazon Kinesis](with-kinesis.md "with-kinesis.md")                                                                                                                                               | [Event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md")                       |
| [Amazon Data Firehose](../../../firehose/latest/dev/data-transformation.md "../../../firehose/latest/dev/data-transformation.md")                                                                 | Event-driven; synchronous invocation                                                                              |
| [Amazon Lex](../../../lexv2/latest/dg/lambda.md "../../../lexv2/latest/dg/lambda.md")                                                                                                             | Event-driven; synchronous invocation                                                                              |
| [Amazon MQ](with-mq.md "with-mq.md")                                                                                                                                                              | [Event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md")                       |
| [Amazon Simple Email Service](../../../ses/latest/dg/receiving-email-action-lambda.md "../../../ses/latest/dg/receiving-email-action-lambda.md")                                                  | Event-driven; asynchronous invocation                                                                             |
| [Amazon Simple Notification Service](with-sns.md "with-sns.md")                                                                                                                                   | Event-driven; asynchronous invocation                                                                             |
| [Amazon Simple Queue Service](with-sqs.md "with-sqs.md")                                                                                                                                          | [Event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md")                       |
| [Amazon Simple Storage Service (Amazon S3)](with-s3.md "with-s3.md")                                                                                                                              | Event-driven; asynchronous invocation                                                                             |
| [Amazon Simple Storage Service Batch](services-s3-batch.md "services-s3-batch.md")                                                                                                                | Event-driven; synchronous invocation                                                                              |
| [Secrets Manager](../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md "../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md")                                          | Secret rotation                                                                                                   |
| [AWS Step Functions](../../../step-functions/latest/dg/connect-lambda.md "../../../step-functions/latest/dg/connect-lambda.md")                                                                   | Event-driven; synchronous or asynchronous invocation                                                              |
| [Amazon VPC Lattice](../../../vpc-lattice/latest/ug/lambda-functions.md "../../../vpc-lattice/latest/ug/lambda-functions.md")                                                                     | Event-driven; synchronous invocation                                                                              |
