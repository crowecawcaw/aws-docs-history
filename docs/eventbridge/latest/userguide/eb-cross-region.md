

# Sending and receiving events between AWS Regions in Amazon EventBridge
<a name="eb-cross-region"></a>

You can configure EventBridge to send and receive [events](eb-events.md) between AWS Regions. You can also allow or deny events from specific Regions, specific [rules](eb-rules.md) associated with the event bus, or events from specific sources. For more information, see [Introducing cross-Region event routing with Amazon EventBridge](https://aws.amazon.com/blogs/compute/introducing-cross-region-event-routing-with-amazon-eventbridge/)

 The following video covers routing events between Regions using the [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/), AWS CloudFormation, and AWS Serverless Application Model:




## Creating rules that send events to a different AWS Region
<a name="eb-create-rule-cross-region-target"></a>

Specifying an event bus in another AWS Region as a target is part of creating the rule.

**To create a rule that sends events to a different AWS account using the console**

1. Follow the steps in the [Creating rules using the Enhanced Builder](eb-create-rule-visual.md) procedure.

1. In the [Select targets](eb-create-rule-wizard.md#eb-create-rule-target) step, when prompted to choose a target type:

   1. Select **EventBridge event bus**.

   1. Select **Event bus in a different account or Region**.

   1. For **Event bus as target**, enter the ARN of the event bus you want to use.

1. Complete creating the rule following the procedure steps.