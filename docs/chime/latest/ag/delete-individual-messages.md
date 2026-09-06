

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Deleting chat messages
<a name="delete-individual-messages"></a>

To comply with data retention policies, Amazon Chime retains all chat messages, and it prevents end users from deleting the messages that they send. However, Amazon Chime system administrators can use a pair of APIs to delete individual messages from conversations and chat rooms. The messages must reside in the administrator's Amazon Chime account.

Users can request message deletion by sending you a message ID and a corresponding conversation or chat room ID. The topic [Using chat features](https://docs.aws.amazon.com/chime/latest/ug/chat-features.html), in the *Amazon Chime User Guide*, explains how.

When you get a deletion request, you can write code or use the AWS CLI to invoke the following APIs.

**To remove a message**
+ Do one of the following:
  + **For conversation messages** – Use the [RedactConversationMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_RedactConversationMessage.html) API.

    In the CLI, run the following command:

    `aws chime redact-conversation-message --conversation-id {{id_string}} --message-id {{id_string}}`
  + **For chat room messages** – Use the [RedactRoomMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_RedactRoomMessage.html) API.

    In the CLI, run the following command:

    `aws chime redact-room-message --room-id {{id_string}} --message-id {{id_string}}`