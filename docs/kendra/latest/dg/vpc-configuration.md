# Configuring Amazon Kendra to use an Amazon VPC

Amazon Kendra can connect to a virtual private cloud (VPC) that you created with
Amazon Virtual Private Cloud to index content stored in data sources running in your
private cloud. When you create a data source connector, you can provide security group
and subnet identifiers for the subnet that contains your data source. With this
information, Amazon Kendra creates an elastic network interface that it uses to
securely communicate with your data source within your VPC.

To set up an Amazon Kendra data source connector with Amazon VPC, you can
use either the AWS Management Console or the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API operation. If you use the console, you connect a VPC
during the connector configuration process.

###### Note

The Amazon VPC feature is optional when setting up an Amazon Kendra
data source connector. If your data source is accessible from the public internet,
you don't need to enable the Amazon VPC feature. Not all Amazon Kendra
data source connectors support Amazon VPC.

If your data source isn't running on Amazon VPC and isn't accessible from the
public internet, you first connect your data source to your VPC using a virtual private
network (VPN). Then, you can connect your data source to Amazon Kendra by using a
combination of Amazon VPC and AWS Virtual Private Network. For information about setting up a VPN,
see the [Site-to-Site VPN
documentation](../../../vpn.md "../../../vpn.md").

###### Topics

- [Configuring Amazon VPC support for
  Amazon Kendra connectors](connector-vpc-steps.md "connector-vpc-steps.md")
- [Set up an Amazon Kendra data source to
  connect to Amazon VPC](connector-vpc-setup.md "connector-vpc-setup.md")
- [Connecting to a database in a VPC](vpc-example.md "vpc-example.md")
- [Troubleshooting VPC connection
  issues](vpc-connector-troubleshoot.md "vpc-connector-troubleshoot.md")
