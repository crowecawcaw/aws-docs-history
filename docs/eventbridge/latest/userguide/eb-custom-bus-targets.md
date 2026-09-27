

# Targets for a Custom Event Bus subscriber
<a name="eb-custom-bus-targets"></a>

A subscriber delivers to one target. Set `InvokeConfiguration.TargetArn` to the target's ARN, add the parameter block for that target type, for example `SqsParameters` for a queue, and give the delivery role the action the target needs, for example `sqs:SendMessage`. Every parameter value can be a fixed string or a JSONata expression in `{% %}` that reads the event, so a queue's `MessageGroupId` can be `{% $events.SystemMetadata.EventGroupId %}`.

The following pages describe each target type. For an AWS API action that has no bespoke target, use a universal target.
+ [Amazon SQS queue target](eb-custom-bus-target-sqs.md)
+ [Lambda function target](eb-custom-bus-target-lambda.md)
+ [Amazon SNS topic target](eb-custom-bus-target-sns.md)
+ [Kinesis stream target](eb-custom-bus-target-kinesis.md)
+ [Amazon Data Firehose stream target](eb-custom-bus-target-firehose.md)
+ [Step Functions state machine target](eb-custom-bus-target-sfn.md)
+ [HTTP targets: API Gateway and API destinations](eb-custom-bus-target-http.md)
+ [Event bus target: bus to bus](eb-custom-bus-target-bus.md)
+ [Universal targets for a Custom Event Bus](eb-custom-bus-universal-targets.md)