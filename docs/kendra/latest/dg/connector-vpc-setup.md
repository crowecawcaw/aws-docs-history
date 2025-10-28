# Set up an Amazon Kendra data source to

connect to Amazon VPC

When you add a new data source in Amazon Kendra, you can use the Amazon VPC feature if the selected data source connector supports this feature.

You can set up a new Amazon Kendra data source with Amazon VPC
enabled by using the AWS Management Console or the Amazon Kendra API. Specifically, use the
[CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API operation, and
then use the `VpcConfiguration` parameter to provide the following
information:

- `SubnetIds` – A list of identifiers of Amazon VPC subnets
- `SecurityGroupIds` – A list of identifiers of Amazon VPC security groups
  If you use the console, you provide the required Amazon VPC information
  during connector configuration. To use the console to enable the Amazon VPC feature for a
  connector, you first choose an Amazon VPC. Then, you provide identifiers of any Amazon VPC
  subnets and identifiers of any Amazon VPC security groups. You can choose the Amazon VPC
  subnets and Amazon VPC security groups that you created in [Configuring
  Amazon VPC](connector-vpc-steps.md "connector-vpc-steps.md"), or use any existing ones.

###### Topics

- [Viewing Amazon VPC
  identifiers](#viewing-vpc-identifiers "#viewing-vpc-identifiers")
- [Checking your data source IAM
  role](#vpc-iam-roles "#vpc-iam-roles")

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
Amazon Kendra automatically adds the correct permissions to your
IAM role on your behalf. If you use the API, or use an
existing IAM role, check that your role contains permissions to
access Amazon VPC. To verify that you have the right permissions, see
[IAM roles for VPC](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

You can modify an existing data source to use a different Amazon VPC
subnet. However, check your data source's IAM role and, if
necessary, modify it to reflect the change for the Amazon Kendra data
source connector to work properly.
