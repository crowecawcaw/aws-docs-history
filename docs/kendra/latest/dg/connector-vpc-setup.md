

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Set up an Amazon Kendra data source to connect to Amazon VPC
<a name="connector-vpc-setup"></a>

When you add a new data source in Amazon Kendra, you can use the Amazon VPC feature if the selected data source connector supports this feature. 

You can set up a new Amazon Kendra data source with Amazon VPC enabled by using the AWS Management Console or the Amazon Kendra API. Specifically, use the [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) API operation, and then use the `VpcConfiguration` parameter to provide the following information:
+ `SubnetIds` – A list of identifiers of Amazon VPC subnets
+ `SecurityGroupIds` – A list of identifiers of Amazon VPC security groups

If you use the console, you provide the required Amazon VPC information during connector configuration. To use the console to enable the Amazon VPC feature for a connector, you first choose an Amazon VPC. Then, you provide identifiers of any Amazon VPC subnets and identifiers of any Amazon VPC security groups. You can choose the Amazon VPC subnets and Amazon VPC security groups that you created in [Configuring Amazon VPC](https://docs.aws.amazon.com/kendra/latest/dg/connector-vpc-steps.html), or use any existing ones.

**Topics**
+ [Viewing Amazon VPC identifiers](#viewing-vpc-identifiers)
+ [Checking your data source IAM role](#vpc-iam-roles)

## Viewing Amazon VPC identifiers
<a name="viewing-vpc-identifiers"></a>

The identifiers for subnets and security groups are configured in the Amazon VPC console. To view the identifiers, use the following procedures.

**To view subnet identifiers**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. From the navigation pane, choose **Subnets**.

1. From the **Subnets** list, choose the subnet that contains your database server.

1. From the **Details** tab, make a note of the identifier in the **Subnet ID** field.

**To view security group identifiers**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. From the navigation pane, choose **Security groups**.

1. From the security group list, choose the group that you want the identifier for.

1. From the **Details** tab, make a note of the identifier in the **Security Group ID** field.

## Checking your data source IAM role
<a name="vpc-iam-roles"></a>

Make sure that your data source connector AWS Identity and Access Management IAM) role contains permissions to access your Amazon VPC.

If you use the console to create a new role for your IAM role, Amazon Kendra automatically adds the correct permissions to your IAM role on your behalf. If you use the API, or use an existing IAM role, check that your role contains permissions to access Amazon VPC. To verify that you have the right permissions, see [IAM roles for VPC](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-vpc).

You can modify an existing data source to use a different Amazon VPC subnet. However, check your data source's IAM role and, if necessary, modify it to reflect the change for the Amazon Kendra data source connector to work properly.