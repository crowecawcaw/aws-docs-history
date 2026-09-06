

# Connect Customer
<a name="contact-center-connect"></a>

Connect Customer is an omnichannel cloud contact center. You can set up a contact center in a few steps, add agents located anywhere, and start engaging with your customers. For more information, see [ Get started with Connect Customer ](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-get-started.html) in the *Connect Customer administrator guide*.

You can create personalized experiences for your customers using omnichannel communications. For example, you can offer chat and voice contact based on customer preference and estimated wait times. Meanwhile agents can handle all customers from just one interface. For example, they can chat with customers, and create or respond to tasks as they are routed to them.

You can use Connect Customer for audio interactions with your customers, or Connect Customer Chat for text-only interactions.

For more information, see the following topics in the *Connect Customer administrator guide*.
+ [What is Connect Customer ](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html)
+ [Add an Amazon Lex V2 bot ](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-lex.html)
+ [Connect Customer get customer input contact block](https://docs.aws.amazon.com/connect/latest/adminguide/get-customer-input.html)

When a contact center sends a request to Amazon Lex V2, it includes platform-specific information as a request attribute to your Lambda function and conversation logs. Use this information to determine which contact center application is sending traffic to your bot.


**Common request attributes for Amazon Connect**  

| Attribute | Value | 
| --- | --- | 
| x-amz-lex:channels:platform | One of the following values:+  `Connect` <br />+  `Connect Chat`  | 