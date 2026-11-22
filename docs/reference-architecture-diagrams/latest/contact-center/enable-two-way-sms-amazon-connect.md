

# Enable Two-Way SMS in Amazon Connect Customer

Publication date: **November 23, 2021 ([Diagram history](diagram-history.md))**

This reference architecture diagram shows how to add SMS support to your contact center. It uses the chat message streaming APIs in [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/) and [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/) two-way SMS.

## Enable Two-Way SMS in Amazon Connect Customer diagram
<a name="enable-two-way-sms-amazon-connect-diagram1"></a>

![Reference architecture diagram showing how to enable two-way SMS in Amazon Connect Customer by using Amazon Pinpoint, AWS Lambda, Amazon DynamoDB, and Amazon Simple Notification Service.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/contact-center/images/enable-two-way-sms-amazon-connect.png)


1. Customer sends a text message to the Amazon Pinpoint phone number.

1. Amazon Pinpoint publishes the message to [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS).

1. Amazon SNS invokes [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/).

1. Lambda queries [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for the chat contact context.

1. If this is the first message for the contact, Lambda calls the StartChatContact, StartContactStreaming, and CreateParticipantConnection APIs. If there is an existing chat, Lambda sends the message to Connect Customer.

1. Connect Customer streams Agent and System messages to Amazon SNS.

1. Amazon SNS invokes Lambda.

1. Lambda queries DynamoDB for chat contact context.

1. Lambda invokes the Amazon Pinpoint SendMessage API to send the text message.

1. Amazon Pinpoint delivers the reply message to the customer through SMS.

## Further reading
<a name="enable-two-way-sms-amazon-connect-further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Connect Customer product page](https://aws.amazon.com/connect/)