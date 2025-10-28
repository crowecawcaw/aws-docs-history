# Console Instructions for Creating an IVS Chat Room

These steps are divided into phases, starting with initial room setup and ending
with final room creation.

Optionally, you can set up a room so messages are reviewed. For example, you can
update message content or metadata, deny messages to prevent them from being sent,
or let the original message through. This is covered in [Set Up to Review Room Messages
(Optional)](#create-room-console-review-messages "#create-room-console-review-messages").

Also optionally, you can set up a room so that messages are logged. For example,
if you have messages being sent to a chat room, you can log them to an Amazon S3
bucket, Amazon CloudWatch, or Amazon Kinesis Data Firehose. This is covered in [Set Up to Log Messages
(Optional)](#create-room-console-log-messages "#create-room-console-log-messages").

## Initial Room Setup

1. Open the [Amazon
   IVS Chat console](https://console.aws.amazon.com/ivs/chat "https://console.aws.amazon.com/ivs/chat").

(You also can access the Amazon IVS console through the [AWS Management
Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").) 2. From the navigation bar, use the **Select a
Region** drop-down to choose a region. Your new room will
be created in this region. 3. In the **Get started** box (top right),
choose **Amazon IVS Chat Room**. The
**Create room** window appears.

![Creating a Chat Room.](images/Chat_Create_Room.png) 4. Under **Setup**, optionally specify a
**Room name**. Room names are not
unique, but they provide a way for you to distinguish rooms other than
the room ARN (Amazon Resource Name). 5. Under **Setup > Room configuration**,
either accept the **Default
configuration**, or select **Custom
configuration** and then configure the **Maximum message length** and/or **Maximum message rate**. 6. If you want to review messages, continue with [Set Up to Review Room
Messages (Optional)](#create-room-console-review-messages "#create-room-console-review-messages") below. Otherwise, skip that (i.e., accept
**Message Review Handler > Disabled**)
and proceed directly to [Final
Room Creation](#create-room-console-final "#create-room-console-final").

## Set Up to Review Room

Messages (Optional)

1. Under **Message Review Handler**, select
   **Handle with AWS Lambda**. The
   **Message Review Handler** section
   expands to show additional options.
2. Configure the **Fallback result** to
   **Allow** or **Deny** the message if the handler does not return a valid
   response, encounters an error, or exceeds the timeout period.
3. Specify your existing **Lambda function**
   or use **Create Lambda function** to create
   a new function.

The lambda function must be in the same AWS account and the same AWS
regions as the chat room. You should give the Amazon Chat SDK service
permission to invoke your lambda resource. The resource-based policy
will be automatically created for the lambda function you selected. For
more information about permissions, see
[Resource-Based Policy for Amazon IVS Chat](security-iam.md#security-chat-policy-examples "security-iam.md#security-chat-policy-examples").

## Set Up to Log Messages

(Optional)

1. Under **Message logging**, select
   **Automatically log chat messages**.
   The **Message logging** section expands to
   show additional options. You can either add an existing logging
   configuration to this room or create a new logging configuration by
   selecting **Create logging
   configuration**.
2. If you choose an existing logging configuration, a dropdown menu
   appears and shows all logging configurations that you already created.
   Select one from the list and your chat messages automatically will log
   to this destination.
3. If you choose **Create logging
   configuration**, a modal window appears which allows you to
   create and customize a new logging configuration.
   1. Optionally specify a **Logging
      configuration name**. Logging-configuration names,
      like room names, are not unique, but they provide a way for you
      to distinguish logging configurations other than the logging
      configuration ARN.
   2. Under **Destination**, select
      **CloudWatch log group**,
      **Kinesis firehose delivery
      stream**, or **Amazon S3
      bucket** to choose the destination for your
      logs.
   3. Depending on your Destination, select the option to create a
      new or use an existing **CloudWatch log
      group**, **Kinesis firehose
      delivery stream**, or **Amazon
      S3 bucket**.
   4. After reviewing, choose **Create** to create a new logging configuration
      with a unique ARN. This automatically attaches the new logging
      configuration to the chat room.

## Final Room Creation

1. After reviewing, choose **Create chat
   room** to create a new chat room with a unique ARN.
