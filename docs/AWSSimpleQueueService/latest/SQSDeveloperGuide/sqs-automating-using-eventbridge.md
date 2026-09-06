

# Automating notifications from AWS services to Amazon SQS using Amazon EventBridge
<a name="sqs-automating-using-eventbridge"></a>

Amazon EventBridge allows you to automate AWS services and respond to events, such as application issues or resource changes, in near real-time.
+ You can create rules to filter specific events and define automated actions when a rule matches an event.
+ EventBridge supports multiple targets, including Amazon SQS standard and FIFO queues, which receive events in JSON format.

For more information, see [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) in the *[Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/)*.