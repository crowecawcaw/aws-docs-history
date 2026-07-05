This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Data retention modules for AWS Wickr

AWS Wickr Data retention can retain all conversations in network. This includes
direct message conversations and conversations in Groups or Rooms between in-network
(internal) members and those with other teams (external) with whom your network is
federated. Data retention is only available to AWS Wickr Premium plan users and
enterprise customers who opt in for data retention. For more information on the Premium
plan, see [Wickr
Pricing](https://aws.amazon.com/wickr/pricing/ "https://aws.amazon.com/wickr/pricing/")

When a network administrator configures and activates data retention for their
network, all messages and files shared by users in their network are archived to a
specified location (E.g., local storage, Amazon S3 bucket), where they can be reviewed,
processed and retained as desired.

###### Note

AWS cannot access end-to-end encrypted message content in Wickr. If your
organization requires access to your end-users’ message content, you must deploy a
data retention bot.

###### Topics

- [Bot-based data retention](bot-data-retention.md "bot-data-retention.md")
- [Serverless data retention for AWS Wickr](serverless-method.md "serverless-method.md")
