

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Setting up event orchestration
<a name="setting-up-event-orchestration"></a>

Setting up event orchestration for your events requires you to set up processes in your target service, configure Amazon EventBridge to receive and send event data, and create rules in Amazon EventBridge that specifies the conditions for starting the downstream processes. Complete the following steps to set up event orchestration:

**To set up event orchestration**

1. Go to [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) and learn how to use Amazon EventBridge. Make sure to learn how to create [Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in Amazon EventBridge for your use case.

1. Follow instructions to [Enable event orchestration in Amazon Fraud Detector](enable-event-orchestration.md).
**Note**  
The event orchestration for your event is *disabled* by default.

1. Set up your target service to receive and process the event data. For example, if your downstream process involves sending notifications and you want to use Amazon SNS, go to Amazon SNS console, create an SNS topic, and then subscribe an endpoint to the topic.

1. Follow instructions to [Create Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html).
**Important**  
When building the event pattern in Amazon EventBridge, make sure to provide `aws.frauddetector` for the *source* field and `Event Prediction Result Returned` for the *detail-type* field.