# Set up your customer's chat experience in Amazon Connect

You can provide a chat experience to your customers by using one of the following methods:

- [Add a chat user interface to your website hosted by
  Amazon Connect](add-chat-to-website.md "add-chat-to-website.md").
- [Customize chat with the Amazon Connect open source
  example](download-chat-example.md "download-chat-example.md").
- [Customize your solution using
  Amazon Connect APIs](integrate-with-startchatcontact-api.md "integrate-with-startchatcontact-api.md"). We recommend starting with the Amazon Connect ChatJS open source
  library when customizing your own chat experiences. For more information, see the
  [Amazon Connect
  ChatJS](https://github.com/amazon-connect/amazon-connect-chatjs "https://github.com/amazon-connect/amazon-connect-chatjs") repo on Github.

## More resources to customize the chat

experience

- Interactive messages provide customers with a prompt and pre-configured
  display options that they can select from. These messages are powered by Amazon Lex
  and configured through Amazon Lex using a Lambda. For instructions about how to add
  interactive messages through Amazon Lex, see this blog: [Set up interactive messages for your Amazon Connect chatbot](https://aws.amazon.com/blogs/contact-center/easily-set-up-interactive-messages-for-your-amazon-connect-chatbot/ "https://aws.amazon.com/blogs/contact-center/easily-set-up-interactive-messages-for-your-amazon-connect-chatbot/").

Amazon Connect supports the following templates: a list picker and a time picker. For
more information, see [Add Amazon Lex interactive messages for customers in
chat](interactive-messages.md "interactive-messages.md").

- [Enable Apple Messages for Business with Amazon Connect](apple-messages-for-business.md "apple-messages-for-business.md")
- [Amazon Connect Service API Documentation](../APIReference.md "../APIReference.md"), especially the
  [StartChatContact](../APIReference/API_StartChatContact.md "../APIReference/API_StartChatContact.md") API.
- [Amazon Connect Participant Service API](../../../connect-participant/latest/APIReference/Welcome.md "../../../connect-participant/latest/APIReference/Welcome.md").
- [Amazon Connect Chat SDK and Sample Implementations](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/ "https://github.com/amazon-connect/amazon-connect-chat-ui-examples/")
- [Amazon Connect
  Streams](https://github.com/aws/amazon-connect-streams "https://github.com/aws/amazon-connect-streams"). Use to integrate your existing apps with Amazon Connect. You can embed
  the Contact Control Panel (CCP) components into your app.
- [Enable message streaming for AI-powered
  chat](message-streaming-ai-chat.md "message-streaming-ai-chat.md")
