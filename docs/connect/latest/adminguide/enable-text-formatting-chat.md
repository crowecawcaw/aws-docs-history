# Enable text formatting in Amazon Connect for your

customer's chat experience

With Amazon Connect message formatting, you can enable your customers and agents to quickly add
structure and clarity to their chat messages.

###### Contents

- [Supported formatting types](#supported-format-types "#supported-format-types")
- [Enable message
  formatting](#how-to-enable-message-formatting "#how-to-enable-message-formatting")
- [How to add email and phone links](#add-email-phone-links "#add-email-phone-links")
- [How to add chatbot messages](#add-bot-messages "#add-bot-messages")

## Supported formatting types

You can provide the following types of formatting on both the chat user interface and the
agent application using markdown:

- Bold
- Italic
- Bulleted list
- Numbered list
- Hyperlinks
- Emoji
- Attachments. To enable attachments, follow [Enable attachments in your CCP so customers and
  agents can share and upload files](enable-attachments.md "enable-attachments.md").

## How to enable message

formatting

1. When you create a new [chat user
   interface](add-chat-to-website.md "add-chat-to-website.md"), rich text formatting is enabled out of the box. No
   additional configuration is required.
2. To add text formatting capabilities to an existing [chat user interface](add-chat-to-website.md "add-chat-to-website.md"), update the [communications widget code](add-chat-to-website.md "add-chat-to-website.md") with the following
   code that is highlighted in bold:

```

    (function(w, d, x, id){
        s=d.createElement('script');
        s.src='https://`your-instance-alias`.my.connect.aws/connectwidget/static/amazon-connect-chat-interface-client.js';
        s.async=1;
        s.id=id;
        d.getElementsByTagName('head')[0].appendChild(s);
        w[x] =  w[x] || function() { (w[x].ac = w[x].ac || []).push(arguments) };
    })(window, document, 'amazon_connect', '`widget-id`');
    amazon_connect('styles', { openChat: { color: '`white`', backgroundColor: '`#123456`'}, closeChat: { color: '`white`', backgroundColor: '`#123456`'} });
    amazon_connect('snippetId', '`snippet-id`');
    **amazon\_connect('supportedMessagingContentTypes', [ '`text/plain`', '`text/markdown`' ])**;

```

The code that is highlighted in red is set to the correct values when you get
the snippet from the Amazon Connect console. The only content you choose to add or remove
is the last line in bold for `supportedMessagingContentTypes`. 3. To add text formatting capabilities to your own custom chat user interface
(for example, [Chat
Interface](https://github.com/amazon-connect/amazon-connect-chat-interface "https://github.com/amazon-connect/amazon-connect-chat-interface") or your own UI solution on top of [ChatJS](https://github.com/amazon-connect/amazon-connect-chatjs "https://github.com/amazon-connect/amazon-connect-chatjs")), follow these steps:

    1. Call the [StartChatContact](../APIReference/API_StartChatContact.md "../APIReference/API_StartChatContact.md") API. When calling
     `StartChatContact`, add the
     `SupportedMessagingContentTypes` parameter as shown in
     bold in the following example:



    ```
    // Amazon Connect StartChatContact API
    {
        "Attributes": {
            "string" : "`string`"
        },
        "ClientToken": "`string`",
        "ContactFlowId": "`your flow ID`",
        "InitialMessage": {
            "Content": "`string`",
            "ContentType": "`string`"
        },
        "InstanceId": "`your instance ID`",
        "ParticipantDetails": {
            "DisplayName": "`string`"
        }

        // optional
       **"SupportedMessagingContentTypes": [ "`text/plain`", "`text/markdown`" ]**
    }
    ```
    2. Import `chatjs` as an object, as shown in the following
     example:



    ```
    import "`amazon-connect-chatjs`";

    this.session = connect.ChatSession.create({
          ...
        });

    this.session.sendMessage({
          message: "`message-in-markdown-format`",
          contentType: "`text/markdown`"
    });
    ```

    If you don't use ChatJs, see these topics for information about
     sending markdown text through Amazon Connect APIs: [StartChatContact](../APIReference/API_StartChatContact.md "../APIReference/API_StartChatContact.md") and [SendMessage](../../../connect-participant/latest/APIReference/API_SendMessage.md "../../../connect-participant/latest/APIReference/API_SendMessage.md").
    3. Send messages with markdown. See the previous code snippet for
     importing `chatjs` as an object for an example of how to send
     messages. You can use simple markdown for formatting text in chats. If
     you're already [using chatjs today to send plaintext messages](https://github.com/amazon-connect/amazon-connect-chatjs/blob/master/src/core/chatController.js#L66 "https://github.com/amazon-connect/amazon-connect-chatjs/blob/master/src/core/chatController.js#L66") you can
     modify your existing logic to call [SendMessage](../../../connect-participant/latest/APIReference/API_SendMessage.md "../../../connect-participant/latest/APIReference/API_SendMessage.md") with `text/markdown` as
     `contentType` instead of `text/plain` when you
     want to send markdown messages. Be sure to update the
     `sendMessage` parameter to have the markdown format of
     your messages. For more information, see [Markdown Guide
     Basic Syntax](https://www.markdownguide.org/basic-syntax/ "https://www.markdownguide.org/basic-syntax/").
    4. Implement your own logic in the UI package to render markdown messages
     in the input area and chat transcript. If you use React, you can use
     [react-markdown](https://github.com/remarkjs/react-markdown "https://github.com/remarkjs/react-markdown") as a reference.

###### Note

- Text formatting capabilities appear to your agent only if the feature has been
  enabled for your customer in the chat user interface. If text formatting is not
  supported or enabled on the customer chat user interface, the agent will not have
  the ability to compose and send messages with text formatting.
- All text formatting capabilities except attachments are available for
  [quick responses](create-quick-responses.md "create-quick-responses.md").

## How to add email and phone links

The following example shows how to add clickable and callable links to your web and mobile applications.

```
Call us today: [+1 (123) 456-7890](tel:+11234567890)
[Call Us](tel:+11234567890)
[Skype Us](callto:+91123-456-7890)
[Fax Us](fax:+91123-456-7890)
[Text Us](SMS:+91123-456-7890)
[Email Us](mailto:name@email.com)
```

## How to add chatbot messages

When you enable markdown for chat messages, you can use rich text formatting for the following types of chatbot messages:

- [Play prompt](play.md "play.md") flows
- [Get customer input](get-customer-input.md "get-customer-input.md") flows
- `SYSTEM_MESSAGE`
- `Lex BOT`
- `Third Party BOT`
- `Lex BOT Lambda`

The following image shows how to enable a prompt manually in a [Play prompt](play.md "play.md") flow block:

![Image of a flow block and a prompt with 2 links, one for an FAQ and another for a phone number.](images/chat-rtf-play-prompt-flow-1.png)

The following image shows how to enable a prompt manually in the a [Get customer input](get-customer-input.md "get-customer-input.md") flow block, then associate the flow block with
an Amazon Lex bot:

![Image of a flow block and a prompt with 2 links, one for an FAQ and another for a phone number.](images/chat-rtf-get-customer-flow.png)

The following image shows how the prompt appears in the SYSTEM_MESSAGE and various BOT message types:

![Image showing "Review our FAQ" and "give us a call" links in SYSTEM and BOT messages.](images/chat-rtf-sys-bot-messages.png)

The following image shows how to set up a prompt in an Amazon Lex bot intent:

![Image of an Amazon Lex intent containing a prompt with 2 links, one for an FAQ and another for a phone number.](images/chat-rtf-lex-flow.png)

For more information about intents, see [Adding intents](../../../lexv2/latest/dg/add-intents.md "../../../lexv2/latest/dg/add-intents.md") in the
_Amazon Lex V2 Developer Guide_. For more information about Lambda messages, see
[Enabling custom logic with AWS Lambda functions](../../../lexv2/latest/dg/lambda.md "../../../lexv2/latest/dg/lambda.md"), also in the _Amazon Lex V2 Developer Guide_.
