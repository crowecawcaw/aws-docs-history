

# Serverless Notifications for Mobile Games with Step Functions
<a name="serverless-notifications-step-functions"></a>

Publication date: **March 10, 2021 ([Diagram history](#notif-sf-history))**

This architecture creates a serverless data flow to ingest, store, process, and send push notifications to subscribers. Use this pipeline for flash offers, in-game event notifications, and campaign-specific notifications targeting segmented audiences with efficiency tracking.

## Serverless Notifications with Step Functions diagram
<a name="notif-sf-diagram"></a>

![Reference architecture diagram showing how to build a serverless notification pipeline for mobile games by using AWS Step Functions, Amazon SNS, and Amazon Translate.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/serverless-notifications-mobile-games/images/serverless-notifications-mobile-games-1.png)


The following steps describe the architecture:

1. When the game client launches, it sends registration information to an [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) REST endpoint. The game client can also send direct notification information through REST.

1. API Gateway requests the [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) registration flow that performs additional logic like device registration and storing [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) endpoint data in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. As the game client sends information to the game server, the server triggers the Step Functions notification workflow that processes messages.

1. To run campaigns or send single notifications, a marketing employee can also manually request the Lambda Step Functions flow through API Gateway. Authorization is handled through [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/).

1. The notification flow performs actions like translation (by using [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html)), message payload enrichment, and storing and obtaining endpoint data from DynamoDB. This data defines direct users or segments to send messages to.

1. Step Functions uses Amazon Translate for quick translation of notification content.

1. Amazon SNS uses the push notification service credentials and mobile device tokens. After receiving the message, all topic subscribers receive the push notification through providers like Firebase or Apple push notification service.

1. Raw data is sent to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for cold data analytics.

## Further reading
<a name="notif-sf-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="notif-sf-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#notif-sf-history) | Reference architecture diagram first published. | March 10, 2021 | 
| [Initial publication](serverless-notifications-pinpoint.md#notif-pin-history) | Reference architecture diagram first published. | March 10, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.