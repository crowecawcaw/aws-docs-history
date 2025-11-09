# Amazon Connect

Amazon Connect is an omnichannel cloud contact center. You can set up a
contact center in a few steps, add agents located anywhere, and
start engaging with your customers. For more information, see
[Get started with Amazon Connect](../../../connect/latest/adminguide/amazon-connect-get-started.md "../../../connect/latest/adminguide/amazon-connect-get-started.md") in the _Amazon Connect
administrator guide_.

You can create personalized experiences for your customers using
omnichannel communications. For example, you can offer chat and
voice contact based on customer preference and estimated wait
times. Meanwhile agents can handle all customers from just one
interface. For example, they can chat with customers, and create
or respond to tasks as they are routed to them.

You can use Amazon Connect for audio interactions with your customers,
or Amazon Connect Chat for text-only interactions.

For more information, see the following topics in the
_Amazon Connect administrator guide_.

- [What is Amazon Connect](../../../connect/latest/adminguide/what-is-amazon-connect.md "../../../connect/latest/adminguide/what-is-amazon-connect.md")
- [Add
  an Amazon Lex V2 bot](../../../connect/latest/adminguide/amazon-lex.md "../../../connect/latest/adminguide/amazon-lex.md")
- [Amazon Connect get customer input contact
  block](../../../connect/latest/adminguide/get-customer-input.md "../../../connect/latest/adminguide/get-customer-input.md")
  When a contact center sends a request to Amazon Lex V2, it includes
  platform-specific information as a request attribute to your
  Lambda function and conversation logs. Use this information to
  determine which contact center application is sending traffic to
  your bot.

| Common request attributes for Amazon Connect | Attribute                                                       | Value |
| -------------------------------------------- | --------------------------------------------------------------- | ----- |
| x-amz-lex:channels:platform                  | One of the following values:<br>• `Connect`<br>• `Connect Chat` |
