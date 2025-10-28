# Using additional chat features

The following sections list additional Amazon Chime chat features and explain how to use them.

###### Topics

- [Features and actions](#features-list "#features-list")
- [Sending markdown messages](#send-chat-markdown "#send-chat-markdown")
- [Sending code blocks in messages](#send-chat-blocks "#send-chat-blocks")

## Features and actions

The following list describes additional features that you can use, and actions that you can take, when using Amazon Chime chat.

**Search as you type**

Searches your contacts, conversations, and chat rooms and starts
displaying results as you type in the search bar. Press
**Enter** to search all content.

**External content URL previews**

Shows a preview of content, such as titles, descriptions, and thumbnails,
when pasting URLs to external sites.

**Message actions**

Message actions appear in the menu next to a message. Choose
**Copy** to copy the message to your clipboard. Choose
**Quote message** to insert the selected message into
your compose message field as a quotation. To report a message to your
administrator for removal, choose **Copy message ID** to
copy the message ID information to your clipboard, then send the information
to your administrator.

**Rich text support for markdown and code blocks**

Use [markdown syntax](http://commonmark.org/help "http://commonmark.org/help") to
format text using bold font, lists, and heading levels, and other options.
Amazon Chime also supports sending code blocks. For more information, see [Sending markdown messages](#send-chat-markdown "#send-chat-markdown") and
[Sending code blocks in messages](#send-chat-blocks "#send-chat-blocks").

**Emoji and .gif support**

To insert an emoji in regular Amazon Chime chat—not the chat in a
meeting—choose **Pick an emoji** next to the chat
input field. You can also choose **Attach a file** to
upload a saved .gif file into the chat input field and play it inline, or
use markdown to display .gif files from the web.

You can also send emojis in chat messages during meetings, but the method
you use depends on your machine and how you run Chime. If you run the Amazon Chime
desktop client on a PC or a Mac, you use _emoji
codes_, words or numbers surrounded by colons. If you run
Amazon Chime in a browser, or on iOS and Android machines, you use an emoji picker.
For more information about using markdown, see [Sending markdown messages](#send-chat-markdown "#send-chat-markdown"). For
more information about using emoji codes in meeting chats, see [Adding emojis to in-meeting chat messages](add-meeting-emojis.md "add-meeting-emojis.md").

**Drag and drop files**

Drag and drop files into the chat pane, or copy and paste images directly
from your clipboard.

## Sending markdown messages

To send an Amazon Chime chat message using [markdown syntax](http://commonmark.org/help "http://commonmark.org/help"), enter `/md` followed by a space at the
beginning of your message. Compose your message using markdown syntax. Press
**Enter** to send.

The following example demonstrates how to format an Amazon Chime chat message using
markdown syntax.

```
/md **Hello world!**
```

The message looks like this when sent.

```
**Hello world!**
```

The markdown syntax in the following example shows how to format a link to a .gif
file. This link displays the .gif file in your Amazon Chime chat message.

```
/md ![](https://`example.com`/`filename`.gif)
```

## Sending code blocks in messages

To send a code block in an Amazon Chime chat message, enter `/code` followed
by a space at the beginning of your message. Copy and paste your code block into the
message. Press **Enter** to send.

The following example demonstrates how to send a code block in an Amazon Chime chat
message.

```
/code CreateBotRequest createBotRequest = new CreateBotRequest()
    .withAccountId("`chimeAccountId`")
    .withDisplayName("`exampleBot`")
    .withDomain("`example.com`");
    chime.createBot(createBotRequest);
```

The following example demonstrates how the sent message appears in Amazon Chime.

```
CreateBotRequest createBotRequest = new CreateBotRequest()
    .withAccountId("chimeAccountId")
    .withDisplayName("exampleBot")
    .withDomain("example.com");
    chime.createBot(createBotRequest);
```
