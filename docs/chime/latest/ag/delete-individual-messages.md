**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Deleting chat messages

To comply with data retention policies, Amazon Chime retains all chat messages, and it
prevents end users from deleting the messages that they send. However, Amazon Chime system
administrators can use a pair of APIs to delete individual messages from conversations
and chat rooms. The messages must reside in the administrator's Amazon Chime account.

Users can request message deletion by sending you a message ID and a corresponding
conversation or chat room ID. The topic [Using chat features](../ug/chat-features.md "../ug/chat-features.md"), in the
_Amazon Chime User Guide_, explains how.

When you get a deletion request, you can write code or use the AWS CLI to invoke the
following APIs.

###### To remove a message

- Do one of the following:
  - For conversation messages – Use
    the [RedactConversationMessage](../APIReference/API_RedactConversationMessage.md "../APIReference/API_RedactConversationMessage.md") API.

  In the CLI, run the following command:

  `aws chime redact-conversation-message --conversation-id
 `id_string`--message-id
`id_string``
  - For chat room messages – Use the
    [RedactRoomMessage](../APIReference/API_RedactRoomMessage.md "../APIReference/API_RedactRoomMessage.md") API.

  In the CLI, run the following command:

  `aws chime redact-room-message --room-id
 `id_string`--message-id
`id_string``
