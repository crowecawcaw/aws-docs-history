# Creating IAM resources for homogeneous migrations

Aurora uses AWS DMS to migrate your data.
To access your databases and to migrate data, AWS DMS creates a serverless environment for homogeneous data migrations.
In this environment, AWS DMS requires access to VPC peering, route tables, security groups, and other AWS resources.
Also, AWS DMS stores logs, metrics, and progress for each data migration in Amazon CloudWatch.
To create a data migration project, AWS DMS needs access to these services.

Also, AWS DMS requires access to the secrets that respresent a set of user credentials to authenticate
the database connection for the source and target connection.

###### Note

By using the **Migrate data from EC2 instance** action, you can use the
Aurora console to generate these IAM resources.
Skip this step if you use the console generated IAM resources.

You need the following IAM resources for this process:

###### Topics

- [Creating an IAM policy for homogeneous data migrations](#USER_DMS_migration-IAM.iam-policy "#USER_DMS_migration-IAM.iam-policy")
- [Creating an IAM role for homogeneous data migrations](#USER_DMS_migration-IAM.iam-role "#USER_DMS_migration-IAM.iam-role")
- [Creating a secret access policy and role](USER_DMS_migration-IAM.md "USER_DMS_migration-IAM.md")
- [Creating an IAM role for AWS DMS to manage Amazon VPC](USER_DMS_migration-IAM.md "USER_DMS_migration-IAM.md")

## Creating an IAM policy for homogeneous data migrations

In this step, you create an IAM policy that provides AWS DMS with access to Amazon EC2 and CloudWatch
resources. Next, create an IAM role and attach this policy.

###### To create an IAM policy for data migration

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In the **Create policy** page, choose the **JSON**
   tab.
5. Paste the following JSON into the editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeVpcPeeringConnections",
 "ec2:DescribeVpcs",
 "ec2:DescribePrefixLists",
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "servicequotas:GetServiceQuota"
 ],
 "Resource": "arn:aws:servicequotas:*:*:vpc/L-0EA8095F"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:DescribeLogStreams"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:dms-data-migration-*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:dms-data-migration-*:log-stream:dms-data-migration-*"
 },
 {
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateRoute",
 "ec2:DeleteRoute"
 ],
 "Resource": "arn:aws:ec2:*:*:route-table/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:security-group/*",
 "arn:aws:ec2:*:*:security-group-rule/*",
 "arn:aws:ec2:*:*:route-table/*",
 "arn:aws:ec2:*:*:vpc-peering-connection/*",
 "arn:aws:ec2:*:*:vpc/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress"
 ],
 "Resource": "arn:aws:ec2:*:*:security-group-rule/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress"
 ],
 "Resource": "arn:aws:ec2:*:*:security-group/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AcceptVpcPeeringConnection",
 "ec2:ModifyVpcPeeringConnectionOptions"
 ],
 "Resource": "arn:aws:ec2:*:*:vpc-peering-connection/*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:AcceptVpcPeeringConnection",
 "Resource": "arn:aws:ec2:*:*:vpc/*"
 }
 ]
}`

```

6. Choose **Next: Tags** and **Next: Review.**
7. Enter `HomogeneousDataMigrationsPolicy` for **Name\***,
   and choose **Create policy**.

## Creating an IAM role for homogeneous data migrations

In this step, you create an IAM role that provides access to AWS Secrets Manager, Amazon EC2, and CloudWatch.

###### To create an IAM role for data migrations

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. On the **Select trusted entity** page, for **Trusted entity
   type**, choose **AWS Service**. For **Use cases for other
   AWS services**, choose **DMS**.
5. Select the **DMS** check box and choose **Next**.
6. On the **Add permissions** page, choose **HomogeneousDataMigrationsPolicy**
   that you created before. Choose **Next**.
7. On the **Name, review, and create** page, enter
   `HomogeneousDataMigrationsRole` for **Role name**, and
   choose **Create role**.
8. On the **Roles** page, enter `HomogeneousDataMigrationsRole`
   for **Role name**. Choose **HomogeneousDataMigrationsRole**.
9. On the **HomogeneousDataMigrationsRole** page, choose the **Trust relationships**
   tab. Choose **Edit trust policy**.
10. On the **Edit trust policy** page, paste the following JSON into the editor,
    replacing the existing text.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "dms-data-migrations.amazonaws.com",
 "dms.`your_region`.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

In the preceding example, replace `your_region` with the name of
your AWS Region.

The preceding resource-based policy provides AWS DMS service principals with permissions to perform tasks
according to the customer managed **HomogeneousDataMigrationsPolicy** policy. 11. Choose **Update policy**.
