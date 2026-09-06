

# Enable Digital Messaging Channels in Amazon Connect
<a name="enable-digital-messaging-amazon-connect"></a>

Publication date: **November 23, 2021 ([Diagram history](#diagram-history))**

This reference architecture diagram shows how to add support for digital messaging channels (such as Facebook Messenger and Slack) to your contact center. It uses [Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html) Chat's Message Streaming APIs and serverless services on AWS.

## Enable Digital Messaging Channels in Amazon Connect
<a name="diagram1"></a>

![Reference architecture diagram showing how to enable digital messaging channels in Amazon Connect by using Amazon API Gateway, AWS Lambda, DynamoDB, and Amazon Simple Notification Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/enable-digital-messaging-amazon-connect/images/enable-digital-messaging-amazon-connect.png)


1. Customer sends a message from the digital messaging channel to the webhook hosted on [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

1. API Gateway sends the message to [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

1. Lambda writes the chat contact context to [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).

1. If this is the first message for the contact, Lambda calls the StartChatContact, StartContactStreaming, and CreateParticipantConnection APIs. If there is an existing chat, Lambda sends the message to Amazon Connect.

1. Amazon Connect streams Agent and System messages to [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) (Amazon SNS).

1. Amazon SNS invokes Lambda.

1. Lambda queries DynamoDB for chat contact context.

1. Lambda delivers the reply message to the customer through APIs from the source channel.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Connect product page](https://aws.amazon.com/connect/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 23, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.