

# Using service-specific insights
<a name="service-insights"></a>

## Chatting about telemetry and operations
<a name="operations-insights"></a>

The AWS assistant uses Amazon CloudWatch telemetry and operational data to answer questions about resource health and alarms. It can also help you troubleshoot. It might ask you for resource names and time ranges.

You can use this capability in the AWS Management Console.

**Service health**  
Ask whether your AWS Lambda functions, Amazon Elastic Container Service (Amazon ECS) clusters, Amazon DynamoDB tables, or other supported resources are healthy.

**Alarm troubleshooting**  
Find alarms in the `ALARM` state. Review the telemetry that triggered them.

**Application Signals**  
Check service-level objectives and indicators to see how healthy your application is.

Example prompts include:
+ Why is my alarm named {{alarm-name}} firing?
+ Is my service healthy in environment {{environment-name}}?

For information about investigations, see [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) in the *Amazon CloudWatch User Guide*.

## Chatting about message delivery
<a name="email-insights"></a>

With the AWS assistant, you can set up message sending in Amazon SES, improve delivery and engagement, and fix sending problems. To help, the AWS assistant uses information about your sending identities, configuration sets, sending patterns, and mailbox provider responses.

You can use this capability in the AWS Management Console.

You need permission to use the AWS assistant. You also need access to the Amazon SES resources in your question.

Example questions include:
+ Do I need to do anything to finish setting up Amazon SES?
+ Which sending identities have the highest deliverability?
+ How is my deliverability for messages sent to Yahoo?
+ How can I improve message delivery?
+ Were there recent events when my deliverability suddenly improved or got worse?