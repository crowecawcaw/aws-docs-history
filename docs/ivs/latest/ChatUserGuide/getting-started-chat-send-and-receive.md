# Step 4: Send and Receive Your

First Message

Use your chat token to connect to a chat room and send your first message. Sample
JavaScript code is provided below. IVS client SDKs also are available: see [Chat SDK: Android Guide](chat-sdk-android.md "chat-sdk-android.md"), [Chat SDK: iOS Guide](chat-sdk-ios.md "chat-sdk-ios.md"), and [Chat SDK: JavaScript Guide](chat-sdk-js.md "chat-sdk-js.md").

**Regional service:** The sample code below refers to
your "supported region of choice." Amazon IVS Chat offers regional endpoints that you
can use to make your requests. For the Amazon IVS Chat Messaging API, the general syntax
of a regional endpoint is:

- wss://edge.ivschat.<region-code>.amazonaws.com
  For example, wss://edge.ivschat.us-west-2.amazonaws.com is the endpoint in the US West
  (Oregon) region. For a list of supported regions, see the Amazon IVS Chat information on
  the [Amazon IVS
  page](../../../general/latest/gr/ivs.md "../../../general/latest/gr/ivs.md") in the _AWS General Reference_.

```
/*
1. To connect to a chat room, you need to create a Secure-WebSocket connection
using the client token you created in the previous steps. Use one of the provided
endpoints in the Chat Messaging API, depending on your AWS region.
*/
const chatClientToken = "GENERATED_CHAT_CLIENT_TOKEN_HERE";
const socket = "wss://edge.ivschat.us-west-2.amazonaws.com"; // Replace “us-west-2” with supported region of choice.
const connection = new WebSocket(socket, chatClientToken);

/*
2. You can send your first message by listening to user input
in the UI and sending messages to the WebSocket connection.
*/
const payload = {
  "Action": "SEND_MESSAGE",
  "RequestId": "OPTIONAL_ID_YOU_CAN_SPECIFY_TO_TRACK_THE_REQUEST",
  "Content": "text message",
  "Attributes": {
    "CustomMetadata": "test metadata"
  }
}
connection.send(JSON.stringify(payload));

/*
3. To listen to incoming chat messages from this WebSocket connection
and display them in your UI, you must add some event listeners.
*/
connection.onmessage = (event) => {
  const data = JSON.parse(event.data);
  displayMessages({
    display_name: data.Sender.Attributes.DisplayName,
    message: data.Content,
    timestamp: data.SendTime
  });
}

function displayMessages(message) {
  // Modify this function to display messages in your chat UI however you like.
  console.log(message);
}

/*
4. Delete a chat message by sending the DELETE_MESSAGE action to the WebSocket
connection. The connected user must have the "DELETE_MESSAGE" permission to
perform this action.
*/

function deleteMessage(messageId) {
  const deletePayload = {
    "Action": "DELETE_MESSAGE",
    "Reason": "Deleted by moderator",
    "Id": "${messageId}"
  }
  connection.send(deletePayload);
}
```

Congratulations, you are all set! You now have a simple chat application that can send
or receive messages.
