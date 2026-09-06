

# Enable Two-Way SMS in Amazon Connect
<a name="enable-two-way-sms-amazon-connect"></a>

Publication date: **November 23, 2021 ([Diagram history](#diagram-history))**

This reference architecture diagram shows how to add SMS support to your contact center. It uses [Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html) Chat's Message Streaming APIs and [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html) two-way SMS.

## Enable Two-Way SMS in Amazon Connect
<a name="diagram1"></a>

![Reference architecture diagram showing how to enable two-way SMS in Amazon Connect by using Amazon Pinpoint, AWS Lambda, Amazon DynamoDB, and Amazon Simple Notification Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/enable-two-way-sms-amazon-connect/images/enable-two-way-sms-amazon-connect.png)


1. Customer sends a text message to the Amazon Pinpoint phone number.

1. Amazon Pinpoint publishes the message to [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) (Amazon SNS).

1. Amazon SNS invokes [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

1. Lambda queries [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) for the chat contact context.

1. If this is the first message for the contact, Lambda calls the StartChatContact, StartContactStreaming, and CreateParticipantConnection APIs. If there is an existing chat, Lambda sends the message to Amazon Connect.

1. Amazon Connect streams Agent and System messages to Amazon SNS.

1. Amazon SNS invokes Lambda.

1. Lambda queries DynamoDB for chat contact context.

1. Lambda invokes the Amazon Pinpoint SendMessage API to send the text message.

1. Amazon Pinpoint delivers the reply message to the customer through SMS.

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