# Responding to an event with Amazon SNS

This section shows how to configure Amazon SNS to send a text notification whenever
ACM generates a health event.

Complete the following procedure to configure a response.

###### To create a Amazon EventBridge rule and trigger an action

1. Create an Amazon EventBridge rule. For more information, see [Creating Amazon EventBridge
   rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md").
   1. In the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/"), navigate to the
      **Events** > **Rules**
      page and choose **Create rule**.
   2. On the **Create rule** page, select
      **Event Pattern**.
   3. For **Service Name**, choose
      **Health** from the menu.
   4. For **Event Type**, choose **Specific
      Health events**.
   5. Select **Specific service(s)** and choose
      **ACM** from the menu.
   6. Select **Specific event type category(s)**
      and choose **accountNotification**.
   7. Choose **Any event type code**.
   8. Choose **Any resource**.
   9. In the **Event pattern preview** editor,
      paste the JSON pattern emitted by the event. This example uses
      the pattern from the [AWS health events](supported-events.md#health-event "supported-events.md#health-event") section.

```
{
   "source":[
      "aws.health"
   ],
   "detail-type":[
      "AWS Health Event"
   ],
   "detail":{
      "service":[
         "ACM"
      ],
      "eventTypeCategory":[
         "scheduledChange"
      ],
      "eventTypeCode":[
         "AWS_ACM_RENEWAL_STATE_CHANGE"
      ]
   }
}
```

2. Configure an action.

In the **Targets** section, you can choose from among
many services that can immediately consume your event, such as Amazon Simple Notification Service
(SNS), or you can choose **Lambda function** to pass
the event to customized executable code. For an example of an AWS Lambda
implementation, see [Responding to an event with a Lambda function](event-lambda-response.md "event-lambda-response.md").
