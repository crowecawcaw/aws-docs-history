# Troubleshoot issues with message

streaming in Amazon Connect

## Messages are not getting published to

SNS

When this happens, we recommend checking the information in [Step 1: Create a standard SNS topic](chat-message-streaming.md#step1-chat-streaming "chat-message-streaming.md#step1-chat-streaming"):

- Make sure you are using standard SNS and not [Amazon SNS FIFO (first in, first
  out)](../../../sns/latest/dg/sns-fifo-topics.md "../../../sns/latest/dg/sns-fifo-topics.md"). Currently, the message streaming APIs support only
  standard SNS for real-time streaming of messages.
- Make sure an SNS resource-based permission is applied correctly in your
  account.
  - If server-side encryption is enabled, you need to give the same
    Amazon Connect service principal permission for encrypt and decrypt.

## Flow doesn't start

If you're using the message streaming APIs in place of websockets, send a
connection acknowledgment event; see [Step 4: Create the participant connection](chat-message-streaming.md#step4-chat-streaming "chat-message-streaming.md#step4-chat-streaming"). This is synonymous to connecting to
websocket. The flow begins only after that the connection acknowledgement
event.

Call [CreateParticipantConnection](../../../connect-participant/latest/APIReference/API_CreateParticipantConnection.md "../../../connect-participant/latest/APIReference/API_CreateParticipantConnection.md") after [StartContactStreaming](../APIReference/API_StartContactStreaming.md "../APIReference/API_StartContactStreaming.md") to mark `Customer` as connected; see
[Step 3: Enable message streaming on the
contact](chat-message-streaming.md#step3-chat-streaming "chat-message-streaming.md#step3-chat-streaming").
This ensures messages are sent after you have confirmed that the customer is ready
to receive them.

## Issue not resolved?

If after trying the previous solutions you still have issues with message
streaming, contact Support for help.

Amazon Connect administrators can choose one of the following options to contact support:

- If you have an AWS Support account, go to [Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") and submit a ticket.
- Otherwise, open the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/")
  and choose **Amazon Connect**, **Support**, **Create case**.

It is helpful to provide the following information:

- Your contact center instance ID/ARN. To find your instance ARN, see [Find your Amazon Connect instance ID or ARN](find-instance-arn.md "find-instance-arn.md").
- Your Region.
- A detailed description of the issue.
