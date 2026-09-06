

# Serverless Notifications for Mobile Games with Amazon Pinpoint
<a name="serverless-notifications-pinpoint"></a>

Publication date: **March 10, 2021 ([Diagram history](#notif-pin-history))**

This architecture provides an alternative notification flow that uses [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/) for campaign-based messaging, A/B testing, and segmented audience targeting with built-in streaming analytics.

## Serverless Notifications with Amazon Pinpoint diagram
<a name="notif-pin-diagram"></a>

![Reference architecture diagram showing how to build a serverless notifications pipeline for mobile games by using Amazon Pinpoint for campaigns and segmented messaging.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/serverless-notifications-mobile-games/images/serverless-notifications-mobile-games-2.png)


The following steps describe the architecture:

1. The game client sends notification information to an [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) REST endpoint. You can update the API version and scale to handle large numbers of requests automatically.

1. To access underlying AWS services through the SDK, the mobile game client requests temporary credentials from [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) Identity pools.

1. The mobile game client can also use the AWS Mobile SDK to invoke Amazon Pinpoint directly with a payload. The device can register or update endpoints dynamically.

1. API Gateway requests Amazon Pinpoint, which performs additional logic like message token translation, segmented message delivery, and streaming analytics for further analysis.

1. [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) uses the push notification service credentials and mobile device tokens. After receiving the message, all subscribers receive the push notification through providers like Firebase or Apple push notification service.

1. An [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function subscribes to [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) Streams to sync users to Amazon Pinpoint.

1. A marketing employee can initiate a campaign, personal message, or A/B testing through the AWS console for Amazon Pinpoint.

1. Campaign and message sending data is streamed to Amazon Kinesis for streaming event analytics or to be stored for later insights in a data lake.

## Further reading
<a name="notif-pin-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="notif-pin-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](serverless-notifications-step-functions.md#notif-sf-history) | Reference architecture diagram first published. | March 10, 2021 | 
| [Initial publication](#notif-pin-history) | Reference architecture diagram first published. | March 10, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.