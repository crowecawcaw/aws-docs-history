# Prerequisites for setting up a zero-ETL integration

Setting up an integration between the source and target require some prerequisites such as configuring IAM roles which AWS Glue uses to access data from the source and write to the target, and the use of KMS keys to encrypt the data in intermediate or the target location.

###### Topics

- [Setting up source resources](#zero-etl-setup-source-resources "#zero-etl-setup-source-resources")
- [Setting up target resources](#zero-etl-setup-target-resources "#zero-etl-setup-target-resources")
- [Creating an Amazon Redshift data warehouse](#zero-etl-setup-target-redshift-data-warehouse "#zero-etl-setup-target-redshift-data-warehouse")
- [Setting up a VPC for your zero-ETL integration](#zero-etl-setup-vpc "#zero-etl-setup-vpc")
- [Setting up a zero-ETL cross-account integration](#zero-etl-setup-cross-account-integration "#zero-etl-setup-cross-account-integration")

## Setting up source resources

Perform the following set up tasks as required for your source.

### Setting up the source role

This section describe how you pass a source role to allow the zero-ETL integration to access your connection. This is also applicable only for SaaS sources.

###### Note

To restrict access to only a few connections, you can first create the connection to obtain the connection ARN. See [Configuring a source for a zero-ETL integration](zero-etl-sources.md "zero-etl-sources.md").

Create a role which has permissions for the integration to access the connection:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GlueConnections",
 "Effect": "Allow",
 "Action": [
 "glue:GetConnections",
 "glue:GetConnection"
 ],
 "Resource": [
 "arn:aws:glue:*:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/*"
 ]
 },
 {
 "Sid": "GlueActionBasedPermissions",
 "Effect": "Allow",
 "Action": [
 "glue:ListEntities",
 "glue:RefreshOAuth2Tokens"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

Trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "glue.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Setting up target resources

Perform the following set up tasks as required for AWS Glue Data Catalog or Amazon Redshift data warehouse integration target.

For integrations with an AWS Glue database target:

- [Setting up an AWS Glue database](#zero-etl-setup-target-resources-glue-database "#zero-etl-setup-target-resources-glue-database")
- [Providing a catalog Resource Based Access (RBAC) policy](#zero-etl-setup-target-resources-rbac-policy "#zero-etl-setup-target-resources-rbac-policy")
- [Creating a target IAM role](#zero-etl-setup-target-resources-target-iam-role "#zero-etl-setup-target-resources-target-iam-role")

For integrations with an Amazon Redshift datawarehouse target:

- [https://docs.aws.amazon.com/glue/latest/dg/zero-etl-prerequisites.html#zero-etl-setup-target-redshift-data-warehouse](zero-etl-prerequisites.md#zero-etl-setup-target-redshift-data-warehouse "zero-etl-prerequisites.md#zero-etl-setup-target-redshift-data-warehouse")

### Setting up an AWS Glue database

For integrations that use an AWS Glue database:

To set up a target database in the AWS Glue Data Catalog with an Amazon S3 location:

1. In the AWS Glue console home page, select **Database** under Data Catalog.
2. Choose **Add database** in the top right corner. If you have already created a database, make sure that the location with Amazon S3 URI is set for the database.
3. Enter a name and **Location** (Amazon S3 URI). Note that the location is required for the zero-ETL integration. Click **Create database** when done.

###### Note

The Amazon S3 bucket must be in the same region as the AWS Glue database.

For information on creating a new database in AWS Glue, see [Getting started with the AWS Glue Data Catalog](start-data-catalog.md "start-data-catalog.md").

You can also use the [`create-database`](../../../cli/latest/reference/glue/create-database.md "../../../cli/latest/reference/glue/create-database.md") CLI to create the database in AWS Glue. Note that the `LocationUri` in `--database-input` is required.

#### Optimizing Iceberg tables

Once a table is created by AWS Glue in the target database, you can enable the compaction to speed up queries in Amazon Athena. For information on setting up the resources (IAM Role) for compaction, see [Table optimization prerequisites](optimization-prerequisites.md "optimization-prerequisites.md").

For more information on setting up compaction on the AWS Glue table created by the integration, see [Optimizing Iceberg tables](table-optimizers.md "table-optimizers.md").

### Providing a catalog Resource Based Access (RBAC) policy

For integrations that use an AWS Glue database, add the following permissions to the catalog RBAC Policy to allow for integrations between source and target.

###### Note

For cross-account integrations, both Alice (user creating the integration) role policy and catalog resource policy need to allow `glue:CreateInboundIntegration` on the resource. For same-account, either a resource policy or role policy allowing `glue:CreateInboundIntegration` on the resource is sufficient. Both scenarios do still need to allow `glue.amazonaws.com` to `glue:AuthorizeInboundIntegration`.

You can access the **Catalog settings** under **Data Catalog**. Then provide the following permissions and fill in the missing information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Principal": {
 "AWS": [
 "arn:aws:iam::`123456789012`:user/Alice"
 ]
 },
 "Effect": "Allow",
 "Action": [
 "glue:CreateInboundIntegration"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/DatabaseName"
 ],
 "Condition": {
 "StringLike": {
 "aws:SourceArn": "arn:aws:dynamodb:`us-east-1`:`444455556666`:table/<table-name>"
 }
 }
 },
 {
 "Principal": {
 "Service": [
 "glue.amazonaws.com"
 ]
 },
 "Effect": "Allow",
 "Action": [
 "glue:AuthorizeInboundIntegration"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/DatabaseName"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:dynamodb:`us-east-1`:`444455556666`:table/<table-name>"
 }
 }
 }
 ]
}`

```

### Creating a target IAM role

Create a target IAM role with the following permissions and trust relationships:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/prefix/*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "glue:GetDatabase"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/DatabaseName"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "glue:CreateTable",
 "glue:GetTable",
 "glue:GetTables",
 "glue:DeleteTable",
 "glue:UpdateTable",
 "glue:GetTableVersion",
 "glue:GetTableVersions",
 "glue:GetResourcePolicy"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/`DatabaseName`",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/`DatabaseName`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/Glue/ZeroETL"
 }
 },
 "Effect": "Allow"
 },
 {
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

Add the following trust policy to allow the AWS Glue service to assume the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Creating an Amazon Redshift data warehouse

When your zero-ETL integration target is an Amazon Redshift data warehouse, create the data warehouse if you don't already have one. To create an Amazon Redshift Serverless workgroup, see [Creating a workgroup with a namespace](../../../redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.md "../../../redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.md"). To create an Amazon Redshift cluster, see [Creating a cluster](../../../redshift/latest/mgmt/create-cluster.md "../../../redshift/latest/mgmt/create-cluster.md").

The target Amazon Redshift workgroup or cluster must have the `enable_case_sensitive_identifier` parameter turned on for the integration to be successful. For more information on enabling case sensitivity, see [Turn on case sensitivity for your data warehouse](../../../redshift/latest/mgmt/zero-etl-setting-up.md "../../../redshift/latest/mgmt/zero-etl-setting-up.md") in the Amazon Redshift management guide.

After the Amazon Redshift workgroup or cluster setup is complete, you need to configure your data warehouse. See [Getting started with zero-ETL integrations](../../../redshift/latest/mgmt/zero-etl-using.md "../../../redshift/latest/mgmt/zero-etl-using.md") in the Amazon Redshift Management Guide for more information.

## Setting up a VPC for your zero-ETL integration

To set up a VPC for your zero-ETL integration:

1. Go to **VPC** > Your VPCs and choose **Create VPC**.
   1. Select **VPC and more**.
   2. Set your VPC name.
   3. Set the IPv4 CIDR: 10.0.0.0/16.
   4. Set the number of AZ to 1.
   5. Set the number of public and private subnets to 1.
   6. Set **NAT gateways** to None.
   7. Set **VPC endpoints** to S3 Gateway.
   8. Enable DNS hostnames and DNS resolution.

2. Go to **Endpoints** and choose **Create Endpoint**.
3. Create endpoints for these services in the private subnet of your VPC (use the default security group):
   1. com.amazonaws.us-east-1.lambda
   2. com.amazonaws.us-east-1.glue
   3. com.amazonaws.us-east-1.sts

Create the AWS Glue connection:

1. Go to **AWS Glue** > **Data connections** and choose **Create connection**.
2. Select **Network**.
3. Select the VPC, Subnet (private), and default Security Group that you created.

### Setting up the target role for the VPC

The target role must have these permissions (in addition to the other permissions required by Zero-ETl integrations):

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CustomerVpc",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags",
 "ec2:DeleteTags",
 "ec2:DescribeRouteTables",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "glue:GetConnection"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

### Setting up the target leg resource properties

If you are using the CLI, set the target leg resource properties to the target AWS Glue database you created. Pass the target role ARN, as well as the AWS Glue connection name.

```
aws glue create-integration-resource-property \
--resource-arn arn:aws:glue:us-east-1:<account-id>:database/exampletarget \
--target-processing-properties '{"RoleArn" : "arn:aws:iam::<account-id>:role/example-role", "ConnectionName":"example-vpc-3"}' \
--endpoint-url https://example.amazonaws.com --region us-east-1


```

### Possible client errors

The following are possible client errors for an integration configured with a
VPC.

| Error message                                                                                                                                                           | Action required             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| Provided role is not authorized to perform<br>glue:GetConnection on connection. Add this permission to<br>role policy, and then wait for the integration to<br>recover. | Update role policy          |
| Provided role is not authorized to perform<br>ec2:DescribeSubnets. Add this permission to role policy, and<br>then wait for the integration to recover.                 | Update role policy          |
| Provided role is not authorized to perform<br>ec2:DescribeSecurityGroups. Add this permission to role<br>policy, and then wait for the integration to<br>recover.       | Update role policy          |
| Provided role is not authorized to perform<br>ec2:DescribeVpcEndpoints. Add this permission to role<br>policy, and then wait for the integration to<br>recover.         | Update role policy          |
| Provided role is not authorized to perform<br>ec2:DescribeRouteTables. Add this permission to role policy,<br>and then wait for the integration to recover.             | Update role policy          |
| Provided role is not authorized to perform<br>ec2:CreateTags. Add this permission to role policy, and then<br>wait for the integration to recover.                      | Update role policy          |
| Provided role is not authorized to perform<br>ec2:CreateNetworkInterface. Add this permission to role<br>policy, and then wait for the integration to<br>recover.       | Update role policy          |
| Provided connection subnet does not contain a valid S3 endpoint or NAT gateway. Update subnet, and then wait for the integration to recover.                            | Update VPC subnet endpoints |
| Connection subnet not found. Update connection subnet, and then wait for the integration to recover.                                                                    | Update AWS Glue connection  |
| Connection security group not found. Update connection security group, and then wait for the integration to recover.                                                    | Update AWS Glue connection  |
| Can't connect to S3 through provided VPC connection. Update subnet configurations, and then wait for the integration to recover.                                        | Update VPC subnet endpoints |
| Can't connect to Lambda through provided VPC connection. Update subnet configurations, and then wait for the integration to recover.                                    | Update VPC subnet endpoints |

## Setting up a zero-ETL cross-account integration

To set up a zero-ETL cross-account integration:

1. Configure a target Resource Policy as described in [Providing a catalog Resource Based Access (RBAC) policy](#zero-etl-setup-target-resources-rbac-policy "#zero-etl-setup-target-resources-rbac-policy"). Ensure that the source account role is explicitly allowed on the target resource.
2. Check that the source account role (the role used to create the integration) has the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt123456789012",
 "Action": [
 "glue:CreateInboundIntegration"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/DatabaseName"
 ]
 }
 ]
}`

```

3. Create the integration as described in [Creating an integration](zero-etl-common-integration-tasks.md#zero-etl-creating "zero-etl-common-integration-tasks.md#zero-etl-creating").
