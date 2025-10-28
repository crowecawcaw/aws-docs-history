# Step 1: Create an IAM policy for the AWS Glue

service

For any operation that accesses data on another AWS resource, such as accessing your
objects in Amazon S3, AWS Glue needs permission to access the resource on your behalf. You
provide those permissions by using AWS Identity and Access Management (IAM).

###### Note

You can skip this step if you use the AWS managed policy `**AWSGlueServiceRole**`.

In this step, you create a policy that is similar to
`AWSGlueServiceRole`. You can find the most current version of
`AWSGlueServiceRole` on the IAM console.

###### To create an IAM policy for AWS Glue

This policy grants permission for some Amazon S3 actions to manage resources in your account
that are needed by AWS Glue when it assumes the role using this policy. Some of the
resources that are specified in this policy refer to default names that are used by
AWS Glue for Amazon S3 buckets, Amazon S3 ETL scripts, CloudWatch Logs, and Amazon EC2 resources. For
simplicity, AWS Glue writes some Amazon S3 objects into buckets in your account prefixed
with `aws-glue-*` by default.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Policies**.
3. Choose **Create Policy**.
4. On the **Create Policy** screen, navigate to a tab to edit JSON. Create a policy document with the following JSON statements,
   and then choose **Review policy**.

###### Note

Add any permissions needed for Amazon S3 resources. You might want to scope the resources section of your access policy to
only those resources that are required.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:*",
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:ListAllMyBuckets",
 "s3:GetBucketAcl",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeRouteTables",
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcAttribute",
 "iam:ListRolePolicies",
 "iam:GetRole",
 "iam:GetRolePolicy",
 "cloudwatch:PutMetricData"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:PutBucketPublicAccessBlock"
 ],
 "Resource": [
 "arn:aws:s3:::aws-glue-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::aws-glue-*/*",
 "arn:aws:s3:::*/*aws-glue-*/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::crawler-public*",
 "arn:aws:s3:::aws-glue-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:AssociateKmsKey"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws-glue/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags",
 "ec2:DeleteTags"
 ],
 "Condition": {
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "aws-glue-service-resource"
 ]
 }
 },
 "Resource": [
 "arn:aws:ec2:*:*:network-interface/*",
 "arn:aws:ec2:*:*:security-group/*",
 "arn:aws:ec2:*:*:instance/*"
 ]
 }
 ]
}`

```

The following table describes the permissions granted by this policy.

| **Action**                                                                                                                                                                                                                             | **Resource**                                                                                              | **Description**                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"glue:*"`                                                                                                                                                                                                                             | `"*"`                                                                                                     | Grants permission to run all AWS Glue API operations.                                                                                                                                                                                                        |
| `"s3:GetBucketLocation", "s3:ListBucket", "s3:ListAllMyBuckets", "s3:GetBucketAcl",`                                                                                                                                                   | `"*"`                                                                                                     | Allows listing of Amazon S3 buckets from crawlers, jobs, development endpoints, and notebook servers.                                                                                                                                                        |
| `"ec2:DescribeVpcEndpoints", "ec2:DescribeRouteTables", "ec2:CreateNetworkInterface", "ec2:DeleteNetworkInterface", "ec2:DescribeNetworkInterfaces", "ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVpcAttribute",` | `"*"`                                                                                                     | Allows the setup of Amazon EC2 network items, such as virtual private clouds (VPCs) when running jobs, crawlers, and development endpoints.                                                                                                                  |
| `"iam:ListRolePolicies", "iam:GetRole", "iam:GetRolePolicy"`                                                                                                                                                                           | `"*"`                                                                                                     | Allows listing IAM roles from crawlers, jobs, development endpoints, and notebook servers.                                                                                                                                                                   |
| `"cloudwatch:PutMetricData"`                                                                                                                                                                                                           | `"*"`                                                                                                     | Allows writing CloudWatch metrics for jobs.                                                                                                                                                                                                                  |
| `"s3:CreateBucket", "s3:PutBucketPublicAccessBlock"`                                                                                                                                                                                   | `"arn:aws:s3:::aws-glue-*"`                                                                               | Allows the creation of Amazon S3 buckets in your account from jobs and notebook servers. Naming convention: Uses Amazon S3 folders named **aws-glue-**. Enables AWS Glue to create buckets that block public access.                                         |
| `"s3:GetObject", "s3:PutObject", "s3:DeleteObject"`                                                                                                                                                                                    | `"arn:aws:s3:::aws-glue-*/*", "arn:aws:s3:::*/*aws-glue-*/*"`                                             | Allows get, put, and delete of Amazon S3 objects into your account when storing objects such as ETL scripts and notebook server locations. Naming convention: Grants permission to Amazon S3 buckets or folders whose names are prefixed with **aws-glue-**. |
| `"s3:GetObject"`                                                                                                                                                                                                                       | `"arn:aws:s3:::crawler-public*", "arn:aws:s3:::aws-glue-*"`                                               | Allows get of Amazon S3 objects used by examples and tutorials from crawlers and jobs. Naming convention: Amazon S3 bucket names begin with **crawler-public** and **aws-glue-**.                                                                            |
| `"logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"`                                                                                                                                                                   | `"arn:aws:logs:*:*:log-group:/aws-glue/*"`                                                                | Allows writing logs to CloudWatch Logs. Naming convention: AWS Glue writes logs to log groups whose names begin with **aws-glue**.                                                                                                                           |
| `"ec2:CreateTags", "ec2:DeleteTags"`                                                                                                                                                                                                   | `"arn:aws:ec2:*:*:network-interface/*", "arn:aws:ec2:*:*:security-group/*", "arn:aws:ec2:*:*:instance/*"` | Allows tagging of Amazon EC2 resources created for development endpoints. Naming convention: AWS Glue tags Amazon EC2 network interfaces, security groups, and instances with **aws-glue-service-resource**.                                                 | 5. On the **Review Policy** screen, enter your **Policy Name**, for example **GlueServiceRolePolicy**. Enter an optional description, and when you're satisfied with the policy, choose **Create policy**. |
