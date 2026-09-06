

# Customize chat with the Connect Customer open source example
<a name="download-chat-example"></a>

You can further customize the chat experience customers use to interact with agents. Use the [Connect Customer open source library](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/blob/master/cloudformationTemplates/startChatContactAPI/README.md) on GitHub. It's a platform to help you get started quickly. Here's how it works:
+ The GitHub repository links to a CloudFormation template, which starts the Amazon API Gateway endpoint that initiates a Lambda function. You can use this template as an example.
+ After you create the AWS CloudFormation stack, you can call this API from your app, import the pre-built communications widget, pass the response to the widget, and start chatting. 

For more information about customizing the chat experience, see: 
+ [Connect Customer Service API Documentation](https://docs.aws.amazon.com/connect/latest/APIReference/welcome.html), especially the [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API. 
+  [Connect Customer Participant Service API](https://docs.aws.amazon.com/connect-participant/latest/APIReference/Welcome.html). 
+  [Connect Customer Streams](https://github.com/aws/amazon-connect-streams). Use to integrate your existing apps with Connect Customer. You can embed the Contact Control Panel (CCP) components into your app. 
+ [Connect Customer Chat SDK and Sample Implementations](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/) 