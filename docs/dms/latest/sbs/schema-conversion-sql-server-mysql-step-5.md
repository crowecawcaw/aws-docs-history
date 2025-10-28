# Step 5: Create an Instance Profile

Before you create an instance profile, configure a subnet group for your instance profile.

**To create a subnet group**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose your AWS Region.
3. In the navigation pane, choose **Subnet groups**, and then choose **Create subnet group**.
4. For **Name**, enter `PrivateSubnetGroup`.
5. For **Description**, enter `A group of private subnets`.
6. For **VPC**, choose `sc-vpc`. You created this VPC in [Step 1](schema-conversion-sql-server-mysql-step-1.md "schema-conversion-sql-server-mysql-step-1.md").
7. For **Add subnets**, choose two private subnet IDs. You noted these private subnet IDs in [Step 1](schema-conversion-sql-server-mysql-step-1.md "schema-conversion-sql-server-mysql-step-1.md").
8. Choose **Create subnet group**.
   Before you create your migration project in DMS Schema Conversion, you set up an instance profile. An instance profile specifies network and security settings for DMS Schema Conversion.

**To create an instance profile**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose your AWS Region.
3. In the navigation pane, choose **Instance profiles**, and then choose **Create instance profile**.
4. For **Name**, enter a unique name for your instance profile. For example, enter `sc-instance`.
5. For **Virtual private cloud (VPC)**, choose `sc-vpc`. You created this VPC in [Step 1](schema-conversion-sql-server-mysql-step-1.md "schema-conversion-sql-server-mysql-step-1.md").
6. For **Subnet group**, choose the `PrivateSubnetGroup` subnet group that you created before.
7. For **S3 bucket** under **Schema conversion settings - optional**, choose an Amazon S3 bucket that you created in [Step 1](schema-conversion-sql-server-mysql-step-1.md "schema-conversion-sql-server-mysql-step-1.md").
8. For **IAM role**, choose the AWS Identity and Access Management (IAM) role that grants access to Amazon S3. You created this role in [Step 1](schema-conversion-sql-server-mysql-step-1.md "schema-conversion-sql-server-mysql-step-1.md").
9. Choose **Create instance profile**.
   Use this instance profile when you create your migration project in [Step 7](schema-conversion-sql-server-mysql-step-7.md "schema-conversion-sql-server-mysql-step-7.md").
