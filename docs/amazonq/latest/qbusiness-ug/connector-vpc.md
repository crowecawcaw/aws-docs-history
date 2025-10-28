# Using Amazon VPC with Amazon Q Business connectors

Amazon Q Business can connect to a virtual private cloud (VPC) that you
created with Amazon Virtual Private Cloud to index content stored in data sources running
in your private cloud. When you create a data source connector, you can provide
security group and subnet identifiers for the subnet that contains your data source.
With this information, Amazon Q Business creates an elastic network interface
that it uses to securely communicate with your data source within your VPC.

To set up an Amazon Q Business data source connector with Amazon VPC, you can use either the AWS Management Console or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API operation. If you use the
console, you connect a VPC during the connector configuration process.

###### Note

The Amazon VPC feature is optional when setting up an Amazon Q Business data source connector. If your data source is accessible
from the public internet, you don't need to enable the Amazon VPC
feature. Not all Amazon Q Business data source connectors support Amazon VPC.

If your data source isn't running on Amazon VPC and isn't accessible from
the public internet, you first connect your data source to your VPC using a virtual
private network (VPN). Then, you can connect your data source to Amazon Q Business by using a combination of Amazon VPC and AWS Virtual Private Network. For
information about setting up a VPN, see the [AWS VPN documentation](../../../vpn.md "../../../vpn.md").

###### Topics

- [Configuring Amazon VPC support for
  Amazon Q Business connectors](connector-vpc-steps.md "connector-vpc-steps.md")
- [Set up an Amazon Q Business data
  source to connect to Amazon VPC](connector-vpc-setup.md "connector-vpc-setup.md")
- [Viewing Amazon VPC
  identifiers](#viewing-vpc-identifiers "#viewing-vpc-identifiers")
- [Checking your data source IAM
  role](#vpc-iam-roles "#vpc-iam-roles")
- [Using Amazon VPC with an Amazon S3 data source](s3-vpc-example-1.md "s3-vpc-example-1.md")
- [Step 3. Configure your external
  data source and Amazon VPC](#connector-vpc-prerequisites-3 "#connector-vpc-prerequisites-3")

###### Topics

- [Viewing Amazon VPC
  identifiers](#viewing-vpc-identifiers "#viewing-vpc-identifiers")
- [Checking your data source IAM
  role](#vpc-iam-roles "#vpc-iam-roles")
- [Using Amazon VPC with an Amazon S3 data source](s3-vpc-example-1.md "s3-vpc-example-1.md")
- [Step 3. Configure your external
  data source and Amazon VPC](#connector-vpc-prerequisites-3 "#connector-vpc-prerequisites-3")

## Viewing Amazon VPC

identifiers

The identifiers for subnets and security groups are configured in the Amazon VPC console. To view the identifiers, use the following
procedures.

###### To view subnet identifiers

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. From the navigation pane, choose **Subnets**.
3. From the **Subnets** list, choose the subnet that
   contains your database server.
4. From the **Details** tab, make a note of the
   identifier in the **Subnet ID** field.

###### To view security group identifiers

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. From the navigation pane, choose **Security
   groups**.
3. From the security group list, choose the group that you want the
   identifier for.
4. From the **Details** tab, make a note of the
   identifier in the **Security Group ID** field.

## Checking your data source IAM

role

Make sure that your data source connector AWS Identity and Access Management IAM) role
contains permissions to access your Amazon VPC.

If you use the console to create a new role for your IAM role,
Amazon Q Business automatically adds the correct permissions to your
IAM role on your behalf. If you use the API, or use an
existing IAM role, check that your role contains permissions to
access Amazon VPC. To verify that you have the right permissions, see
[IAM roles for data
sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can modify an existing data source to use a different Amazon VPC
subnet. However, check your data source's IAM role and, if
necessary, modify it to reflect the change for the Amazon Q Business data
source connector to work properly.

## Step 3. Configure your external

data source and Amazon VPC

Make sure that your external data source has the correct permissions
configuration and network settings for Amazon Q Business to access it. You
can find detailed instructions on how to configure your data sources in the
prerequisites section of each connector page.

Also, check your Amazon VPC settings and make sure that your external
data source is reachable from the subnet you will assign to Amazon Q Business. To do this, we recommend that you create an Amazon EC2 instance in the same subnet with the same security groups and
test access to your data source from this Amazon EC2 instance. For more
information, see [Troubleshooting Amazon VPC connection](vpc-connector-troubleshoot.md "vpc-connector-troubleshoot.md").
