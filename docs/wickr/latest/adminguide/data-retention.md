This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Data retention for AWS Wickr

AWS Wickr Data retention can retain all conversations in network. This includes
direct message conversations and conversations in Groups or Rooms between in-network
(internal) members and those with other teams (external) with whom your network is
federated. Data retention is only available to AWS Wickr Premium plan users and
enterprise customers who opt in for data retention. For more information on the Premium
plan, see [Wickr
Pricing](https://aws.amazon.com/wickr/pricing/ "https://aws.amazon.com/wickr/pricing/")

When a network administrator configures and activates data retention for their
network, all messages and files shared in their network are retained in accordance with
the organization's compliance policies. These .txt file outputs are accessible by the
network administrator in an external location (eg: local storage, Amazon S3
bucket, or any other storage as per user's choice), from where they can be analyzed,
erased, or transferred.

###### Note

Wickr never accesses your messages and files. Therefore, it is your
responsibility to configure a data retention system.

###### Topics

- [View data retention details in
  AWS Wickr](view-data-retention-details.md "view-data-retention-details.md")
- [Configure data retention for
  AWS Wickr](configure-data-retention.md "configure-data-retention.md")
- [Get the data retention logs for your
  Wickr network](getting-data-retention-logs.md "getting-data-retention-logs.md")
- [Data retention metrics and events for your Wickr
  network](metrics-events.md "metrics-events.md")
