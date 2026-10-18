

# Troubleshoot issues with message streaming in Connect Customer
<a name="troubleshoot-message-streaming"></a>

## Messages are not getting published to SNS
<a name="message-not-published-to-sns"></a>

When this happens, we recommend checking the information in [Step 1: Create a standard SNS topic](chat-message-streaming.md#step1-chat-streaming):
+ Make sure you are using standard SNS and not [Amazon SNS FIFO (first in, first out)](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html). Currently, the message streaming APIs support only standard SNS for real-time streaming of messages.
+ Make sure an SNS resource-based permission is applied correctly in your account.
  + If server-side encryption is enabled, you need to give the same Connect Customer service principal permission for encrypt and decrypt.

## Flow doesn't start
<a name="contact-flow-not-starting"></a>

The flow begins only after the customer is connected. If you're using the message streaming APIs in place of websockets, send a connection acknowledgment event. This is synonymous to connecting to websocket. For instructions, see [Step 4: Create the participant connection](chat-message-streaming.md#step4-chat-streaming).

Call [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) with `ConnectParticipant` set to true to mark `Customer` as connected. This works only after streaming is enabled on the contact. For instructions, see [Step 3: Enable message streaming on the contact](chat-message-streaming.md#step3-chat-streaming). Marking `Customer` as connected ensures messages are sent after you have confirmed that the customer is ready to receive them.

Setting `ChatStreamingConfiguration` on [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) does not connect the customer. Neither does a response that returns only a connection token.

## Issue not resolved?
<a name="other-issues-message-streaming"></a>

If after trying the previous solutions you still have issues with message streaming, contact Support for help. 

Connect Customer administrators can choose one of the following options to contact support:
+ If you have an AWS Support account, go to [Support Center](https://console.aws.amazon.com/support/home) and submit a ticket.
+ Otherwise, open the [AWS Management Console](https://console.aws.amazon.com/) and choose **Connect Customer**, **Support**, **Create case**.

It is helpful to provide the following information:
+ Your contact center instance ID/ARN. To find your instance ARN, see [Find your Connect Customer instance ID or ARN](find-instance-arn.md). 
+ Your Region. 
+ A detailed description of the issue.