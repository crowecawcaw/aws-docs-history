# Step 4: Create an IAM policy for notebook

servers

If you plan to use notebooks with development endpoints, you must specify permissions when
you create the notebook server. You provide those permissions by using AWS Identity and Access Management
(IAM).

This policy grants permission for some Amazon S3 actions to manage resources in your account
that are needed by AWS Glue when it assumes the role using this policy. Some of the
resources that are specified in this policy refer to default names used by AWS Glue for
Amazon S3 buckets, Amazon S3 ETL scripts, and Amazon EC2 resources. For simplicity, AWS Glue defaults
writing some Amazon S3 objects into buckets in your account prefixed with
`aws-glue-*`.

###### Note

You can skip this step if you use the AWS managed policy **`AWSGlueServiceNotebookRole`**.

In this step, you create a policy that is similar to
`AWSGlueServiceNotebookRole`. You can find the most current version of
`AWSGlueServiceNotebookRole` on the IAM console.

###### To create an IAM policy for notebooks

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Policies**.
3. Choose **Create Policy**.
4. On the **Create Policy** screen, navigate to a tab to edit JSON. Create a policy document with the following JSON statements,
   and then choose **Review policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateDatabase",
 "glue:CreatePartition",
 "glue:CreateTable",
 "glue:DeleteDatabase",
 "glue:DeletePartition",
 "glue:DeleteTable",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:GetTable",
 "glue:GetTableVersions",
 "glue:GetTables",
 "glue:UpdateDatabase",
 "glue:UpdatePartition",
 "glue:UpdateTable",
 "glue:GetJobBookmark",
 "glue:ResetJobBookmark",
 "glue:CreateConnection",
 "glue:CreateJob",
 "glue:DeleteConnection",
 "glue:DeleteJob",
 "glue:GetConnection",
 "glue:GetConnections",
 "glue:GetDevEndpoint",
 "glue:GetDevEndpoints",
 "glue:GetJob",
 "glue:GetJobs",
 "glue:UpdateJob",
 "glue:BatchDeleteConnection",
 "glue:UpdateConnection",
 "glue:GetUserDefinedFunction",
 "glue:UpdateUserDefinedFunction",
 "glue:GetUserDefinedFunctions",
 "glue:DeleteUserDefinedFunction",
 "glue:CreateUserDefinedFunction",
 "glue:BatchGetPartition",
 "glue:BatchDeletePartition",
 "glue:BatchCreatePartition",
 "glue:BatchDeleteTable",
 "glue:UpdateDevEndpoint",
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:ListAllMyBuckets",
 "s3:GetBucketAcl"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::crawler-public*",
 "arn:aws:s3:::aws-glue*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::aws-glue*"
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

| **Action**                                                                          | **Resource**                                                                                              | **Description**                                                                                                                                                           |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"glue:*"`                                                                          | `"*"`                                                                                                     | Grants permission to run all AWS Glue API operations.                                                                                                                     |
| `"s3:GetBucketLocation", "s3:ListBucket", "s3:ListAllMyBuckets", "s3:GetBucketAcl"` | `"*"`                                                                                                     | Allows listing of Amazon S3 buckets from notebook servers.                                                                                                                |
| `"s3:GetObject"`                                                                    | `"arn:aws:s3:::crawler-public*", "arn:aws:s3:::aws-glue-*"`                                               | Allows get of Amazon S3 objects used by examples and tutorials from notebooks. Naming convention: Amazon S3 bucket names begin with **crawler-public** and **aws-glue-**. |
| `"s3:PutObject", "s3:DeleteObject"`                                                 | `"arn:aws:s3:::aws-glue*"`                                                                                | Allows put and delete of Amazon S3 objects into your account from notebooks. Naming convention: Uses Amazon S3 folders named **aws-glue**.                                |
| `"ec2:CreateTags", "ec2:DeleteTags"`                                                | `"arn:aws:ec2:*:*:network-interface/*", "arn:aws:ec2:*:*:security-group/*", "arn:aws:ec2:*:*:instance/*"` | Allows tagging of Amazon EC2 resources created for notebook servers. Naming convention: AWS Glue tags Amazon EC2 instances with **aws-glue-service-resource**.            | 5. On the **Review Policy** screen, enter your **Policy Name**, for example **GlueServiceNotebookPolicyDefault**. Enter an optional description, and when you're satisfied with the policy, choose **Create policy**. |
