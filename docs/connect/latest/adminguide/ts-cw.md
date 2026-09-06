

# Troubleshoot issues with your Connect Customer communications widget
<a name="ts-cw"></a>

This topic is for developers who need to investigate issues that might occur when configuring a communications widget in the Connect Customer admin website. 

**Topics**
+ ["Something went wrong"](#sww)
+ [Customers not receiving agent messages: Network or WebSocket disconnected](#mam)
+ [Bypassing CORS when opening third-party links](#bcwotpl)

## "Something went wrong"
<a name="sww"></a>

If you see the following **Something went wrong** error message when loading your communications widget, open the browser tools to view the error logs. 

![An error message that says Something went wrong.](http://docs.aws.amazon.com/connect/latest/adminguide/images/chatwidget-error-message.png)


Following are common issues that cause this error.

### 400 Invalid request
<a name="400-invalid-request"></a>

If the logs mention a 400 invalid request, there are a few possible causes:
+ Your communications widget is not being served on an allowed domain. You must specifically state the domains where you will host your widget.
+ The request to the endpoint is not properly formatted. This usually occurs only if the contents of the embed snippet have been modified.

### 401 Unauthorized
<a name="401-unauthorized"></a>

![The Something went wrong error message.](http://docs.aws.amazon.com/connect/latest/adminguide/images/something-went-wrong.png)


If the logs mention a 401 unauthorized, this is a problem with the JSON Web Token (JWT) authentication. It displays the above error page.

After you have the JWT, you need to implement it in the `authenticate` callback function. The following example shows how to implement it if you're trying to fetch your token and then use it: 

```
amazon_connect('authenticate', function(callback) {
  window.fetch('/token').then(res => {
    res.json().then(data => {
      callback(data.data);
    });
  });
});
```

Here is a more basic version of what needs to be implemented:

```
amazon_connect('authenticate', function(callback) {
   callback(token);
});
```

For instructions on implementing JWT, see [Step 3: Confirm and copy communications widget code and security keys](add-chat-to-website.md#confirm-and-copy-chat-widget-script).

If you have implemented the callback already, the following scenarios might still cause a 401:
+ Invalid signature
+ Expired token

### 404 Not found
<a name="404-not-found"></a>

A 404 status code is typically caused when the requested resource doesn't exist:
+ An invalid widgetId is specified in the API request
+ The widgetId is valid but the associated flow has been deleted or archived
+ The widget hasn't been published, or it has been deleted

Verify that your snippet is exactly how it was copied from the Connect Customer admin website, and none of the identifiers have changed.

If the identifiers have not changed and you are seeing a 404, contact AWS Support. 

### 500 Internal server error
<a name="500-internalservererror-chatwidget"></a>

This can be caused by your service-linked role not having the required permissions to start chat. This happens if your Connect Customer instance was created before October 2018 because you don’t have service-linked roles set up.

**Solution**: Add the `connect:*` policy on the role that is associated with your Connect Customer instance. For more information, see [Use service-linked roles and role permissions for Connect Customer](connect-slr.md).

If your service-linked role has the correct permissions, contact AWS Support.

## Customers not receiving agent messages: Network or WebSocket disconnected
<a name="mam"></a>

During a chat session, a customer who is using a chat application loses their network/WebSocket connection. They quickly re-gain connection, but messages that were sent by the agent during that time aren't rendered in the customer's chat interface. 

The following image shows an example of the customer's chat interface and agent's Contact Control Panel side-by-side. A message the agent sent is not rendered in the customer's chat session. However, it appears to the agent as though the customer has received it.

![A message in the CCP that is not sent to the contact.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tw-cw-001-message-not-sent.png)


If the customer's chat application loses it's network/WebSocket connection, the chat user interface must do the following to retrieve future messages as well as messages that were sent to it while disconnected: 
+ Re-establish the WebSocket connection to receive future incoming messages again.
+ Make a [chatSession.getTranscript](https://github.com/amazon-connect/amazon-connect-chatjs?tab=readme-ov-file#chatsessiongettranscript) ([getTranscripts](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_GetTranscript.html) API) request to retrieve all missing messages that were sent while the customer was disconnected.

If the agent sends a message while the customer's chat user interface is disconnected, the message is successfully stored in the Connect Customer back end: the CCP is working as expected and messages are all recorded in transcript, but the customer's device is unable to receive messages. When the client reconnects to the WebSocket, there is a gap in messages. Future incoming messages will appear again from the WebSocket. However, the gap messages are still missing unless the code explicitly makes a call to the [GetTranscript](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_GetTranscript.html) API.

### Solution
<a name="solution-network-disconnected"></a>

Use the [chatSession.onConnectionEstablished](https://github.com/amazon-connect/amazon-connect-chatjs?tab=readme-ov-file#chatsessiononconnectionestablished) event handler to call the [GetTranscript](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_GetTranscript.html) API. The `chatSession.onConnectionEstablished` event handler is triggered when the WebSocket re-connects. ChatJS has built-in heartbeat and retry logic for the WebSocket connection. Because ChatJS is not storing the transcript, however, you must add custom code to the chat user interface to manually fetch the transcript again.

The following code sample shows how to implement `onConnectionEstablished` to call `GetTranscript`.

```
import "amazon-connect-chatjs";

const chatSession = connect.ChatSession.create({
  chatDetails: {
    ContactId: "{{the ID of the contact}}",
    ParticipantId: "{{the ID of the chat participant}}",
    ParticipantToken: "{{the participant token}}",
  },
  type: "CUSTOMER",
  options: { region: "us-west-2" },
});

// Triggered when the websocket reconnects
chatSession.onConnectionEstablished(() => {
  chatSession.getTranscript({
    scanDirection: "BACKWARD",
    sortOrder: "ASCENDING",
    maxResults: 15,
    // nextToken?: nextToken - OPTIONAL, for pagination
  })
    .then((response) => {
      const { initialContactId, nextToken, transcript } = response.data;
      // ...
    })
    .catch(() => {})
});
```

```
function loadLatestTranscript(args) {
    // Documentation: https://github.com/amazon-connect/amazon-connect-chatjs?tab=readme-ov-file#chatsessiongettranscript
    return chatSession.getTranscript({
        scanDirection: "BACKWARD",
        sortOrder: "ASCENDING",
        maxResults: 15,
        // nextToken?: nextToken - OPTIONAL, for pagination
      })
      .then((response) => {
        const { initialContactId, nextToken, transcript } = response.data;
        
        const exampleMessageObj = transcript[0];
        const {
          DisplayName,
          ParticipantId,
          ParticipantRole, // CUSTOMER, AGENT, SUPERVISOR, SYSTEM
          Content,
          ContentType,
          Id,
          Type,
          AbsoluteTime, // sentTime = new Date(item.AbsoluteTime).getTime() / 1000
          MessageMetadata, // { Receipts: [{ RecipientParticipantId: "asdf" }] }
          Attachments,
          RelatedContactid,
        } = exampleMessageObj;

        return transcript // TODO - store the new transcript somewhere
      })
      .catch((err) => {
        console.log("CustomerUI", "ChatSession", "transcript fetch error: ", err);
      });
}
```

For another example, see this [open source implementation on GitHub](https://github.com/amazon-connect/amazon-connect-chat-interface/blob/c88f854073fe6dd45546585c3bfa363d3659d73f/src/components/Chat/ChatSession.js#L408). 

## Bypassing CORS when opening third-party links
<a name="bcwotpl"></a>

To enhance security, the communications widget operates within a sandbox environment. As a result, third-party links shared within the widget cannot be opened.

**Solution**

There are two options for bypassing CORS to allow third-party links to be opened.
+ **(Recommended)**

  Update the sandbox attribute to allow opening links in new tab which can be done by adding the following attribute to the code snippet:

  ```
  amazon_connect('updateSandboxAttributes', 'allow-scripts allow-same-origin allow-popups allow-downloads allow-top-navigation-by-user-activation allow-popups-to-escape-sandbox')
  ```
**Note**  
The attribute value can be updated as needed to allow for specific actions. This is an example for how to allow opening links in new tab.
+ Remove the sandbox attribute which can be done by adding the following attribute to the code snippet:

  ```
  amazon_connect('removeSandboxAttribute', true)
  ```