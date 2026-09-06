

# Serverless services
<a name="sns-event-sources-serverless"></a>

The following table describes how Amazon SNS integrates with services like Amazon DynamoDB, Amazon EventBridge, and Lambda to send notifications for key events such as maintenance updates, real-time data streams, and Lambda function outputs. 

These integrations help you to efficiently monitor and manage your applications by receiving timely alerts on critical operations and automating responses to these events.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) – Provides fast and predictable performance with seamless scalability in this fully managed NoSQL database service. | Receive notifications when maintenance events occur. For more information, see [Customizing DAX cluster settings](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings) in the *Amazon DynamoDB Developer Guide*. | 
| [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html) – Delivers a stream of real-time data from your own applications, software-as-a-service (SaaS) applications, and AWS services and routes that data to targets, including Amazon SNS. EventBridge was formerly called CloudWatch Events. | Receive notifications of EventBridge events. For more information, see [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-targets.html) in the *Amazon EventBridge User Guide*. | 
| [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – Lets you run code without provisioning or managing servers. | Receive function output data by setting an SNS topic as a Lambda dead-letter queue or a Lambda destination. For more information, see [Asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) in the *AWS Lambda Developer Guide*. | 