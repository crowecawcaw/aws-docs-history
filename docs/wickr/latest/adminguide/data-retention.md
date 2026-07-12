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

AWS Wickr offers two data retention deployment options. The following table compares
the two methods to help you choose the one that best fits your organization's
infrastructure and compliance requirements.

| Feature        | Bot-based data retention                                                                                                                           | Serverless data retention                                                                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deployment     | This method requires a complex setup with physical or virtual<br>hardware and Docker expertise.                                                    | You can deploy this method through a console-guided setup with<br>minimal steps.                                                                                                                         |
| Infrastructure | You maintain full control over the infrastructure and deployment<br>environment. You maintain the bot, monitor its health, and handle<br>failures. | You don't need to maintain any infrastructure.                                                                                                                                                           |
| Decryption     | You can decrypt messages at any location of your choice, including<br>on-premises.                                                                 | Wickr decrypts messages on AWS infrastructure, within secure<br>AWS Nitro Enclaves that use your customer managed keys.                                                                                  |
| Scaling        | Scaling and upgrades require manual processes.                                                                                                     | This method scales automatically and provides fault<br>tolerance.                                                                                                                                        |
| Monitoring     | This method does not include built-in monitoring or<br>alerting.                                                                                   | This method provides pre-configured monitoring and<br>alerting.                                                                                                                                          |
| Data storage   | You can store data unencrypted on customer-controlled<br>hardware.                                                                                 | Wickr stores decrypted messages in an Amazon S3 bucket. Wickr<br>encrypts the bucket contents with your customer managed key. To read<br>the bucket contents, use the provided decryption Λ<br>function. |

###### Topics

- [Bot-based data retention](bot-data-retention.md "bot-data-retention.md")
- [Serverless data retention for AWS Wickr](serverless-method.md "serverless-method.md")
- [Data retention data format](dataretention-data-formats.md "dataretention-data-formats.md")
