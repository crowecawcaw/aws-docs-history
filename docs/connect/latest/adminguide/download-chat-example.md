# Customize chat with the Amazon Connect open source

example

You can further customize the chat experience customers use to interact with agents.
Use the [Amazon Connect open source library](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/tree/master/cloudformationTemplates/asyncCustomerChatUX "https://github.com/amazon-connect/amazon-connect-chat-ui-examples/tree/master/cloudformationTemplates/asyncCustomerChatUX") on GitHub. It's a platform to help you get
started quickly. Here's how it works:

- The GitHub repository links to a CloudFormation template, which starts the
  Amazon API Gateway endpoint that initiates a Lambda function. You can use this template as
  an example.
- After you create the AWS CloudFormation stack, you can call this API from your app,
  import the pre-built communications widget, pass the response to the widget, and start
  chatting.
  For more information about customizing the chat experience, see:

- [Amazon Connect Service API
  Documentation](../APIReference/welcome.md "../APIReference/welcome.md"), especially the [StartChatContact](../APIReference/API_StartChatContact.md "../APIReference/API_StartChatContact.md") API.
- [Amazon Connect Participant
  Service API](../../../connect-participant/latest/APIReference/Welcome.md "../../../connect-participant/latest/APIReference/Welcome.md").
- [Amazon Connect
  Streams](https://github.com/aws/amazon-connect-streams "https://github.com/aws/amazon-connect-streams"). Use to integrate your existing apps with Amazon Connect. You can embed
  the Contact Control Panel (CCP) components into your app.
- [Amazon Connect Chat SDK and Sample Implementations](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/ "https://github.com/amazon-connect/amazon-connect-chat-ui-examples/")
