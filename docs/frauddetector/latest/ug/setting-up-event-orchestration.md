Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Setting up event orchestration

Setting up event orchestration for your events requires you to set up processes in your target service, configure Amazon EventBridge to receive and send event data, and create rules in Amazon EventBridge that specifies the conditions for starting the downstream processes.
Complete the following steps to set up event orchestration:

###### To set up event orchestration

1. Go to [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") and learn how to use Amazon EventBridge.
   Make sure to learn how to create [Rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in Amazon EventBridge for your use case.
2. Follow instructions to [Enable event orchestration in Amazon Fraud Detector](enable-event-orchestration.md "enable-event-orchestration.md").

###### Note

The event orchestration for your event is _disabled_ by default. 3. Set up your target service to receive and process the event data. For example, if your downstream process involves sending notifications and you want to use Amazon SNS,
go to Amazon SNS console, create an SNS topic, and then subscribe an endpoint to the topic. 4. Follow instructions to [Create Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md").

###### Important

When building the event pattern in Amazon EventBridge, make sure to provide `aws.frauddetector` for the _source_ field and `Event Prediction Result Returned` for the _detail-type_ field.
