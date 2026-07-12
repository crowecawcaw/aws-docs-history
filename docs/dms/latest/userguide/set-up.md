# Complete prerequisites for working with DMS Schema Conversion

Before you create an instance profile, add data providers, and create a
migration project, complete the following prerequisite tasks. These tasks
configure the AWS resources that DMS Schema Conversion needs, such as a VPC, an Amazon S3
bucket, AWS Secrets Manager secrets, and IAM roles with permissions policies.

###### Console automates resource creation

When you create a migration project using the AWS Management Console,
AWS DMS can automatically create the required IAM roles and Amazon S3 bucket on
your behalf. If you prefer to create these resources manually, or if you
use the AWS CLI or API, complete the following steps. For more information
about creating migration projects, see [Creating migration projects](migration-projects-create.md "migration-projects-create.md").

###### Topics

- [Configure VPC, Amazon S3, and Secrets Manager](#set-up-aws-resources "#set-up-aws-resources")
- [Create IAM roles and policies](#set-up-iam "#set-up-iam")

## Configure VPC, Amazon S3, and Secrets Manager

Before you create IAM roles and policies, you need the following AWS
resources for your migration project.

###### Amazon Virtual Private Cloud

You need a VPC with connectivity to your source and target
databases from subnets in at least two Availability Zones. You can use an
existing VPC that meets these requirements, or create a new one, for
example named `sc-vpc`. For more information about network
configuration, see [Setting up a network for DMS Schema Conversion](instance-profiles-network.md "instance-profiles-network.md").

###### Amazon S3

You need an Amazon S3 bucket with versioning enabled to store
assessment reports, converted SQL code, and database schema metadata.
Create an Amazon S3 bucket in the same Region as your migration project, for
example named `amzn-s3-demo-bucket`, or use an existing bucket that
meets these requirements. DMS Schema Conversion supports only Amazon S3 buckets that use
Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3). DMS Schema Conversion
doesn't support SSE-KMS, SSE-C, or Client-Side Encryption. For
instructions on creating a bucket, see [Creating a
bucket](../../../AmazonS3/latest/userguide/creating-bucket.md "../../../AmazonS3/latest/userguide/creating-bucket.md") in the _Amazon S3 User
Guide_.

###### AWS Secrets Manager

Create JSON secrets in AWS Secrets Manager that contain
`username` and `password` key-value pairs for
your source and target databases, for example named
`sc-source-secret` and `sc-target-secret`. Your
secrets must be in the same AWS Region as your migration project. If
you already have secrets that meet these requirements, you can reuse
them. For instructions on creating secrets, see [Create an
AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User
Guide_.

## Create IAM roles and policies

To use DMS Schema Conversion, create the following five IAM roles. Each role must use a
trust policy that allows the AWS DMS service to assume the role.

| Role name                  | Permissions policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sc-s3-role`               | Allows DMS Schema Conversion to store assessment reports,<br>converted SQL code, and metadata in the Amazon S3<br>bucket:<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"s3:ListBucket",<br>"s3:GetBucketLocation",<br>"s3:GetBucketVersioning"<br>],<br>"Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",<br>"Condition": {<br>"StringEquals": {<br>"aws:ResourceAccount": "`111122223333`"<br>}<br>}<br>},<br>{<br>"Effect": "Allow",<br>"Action": [<br>"s3:PutObject",<br>"s3:GetObject",<br>"s3:GetObjectVersion"<br>],<br>"Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",<br>"Condition": {<br>"StringEquals": {<br>"aws:ResourceAccount": "`111122223333`"<br>}<br>}<br>}<br>]<br>}`<br>`` |
| `sc-source-secret-role`    | Allows DMS Schema Conversion to retrieve your source<br>database credentials:<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"secretsmanager:GetSecretValue",<br>"secretsmanager:DescribeSecret"<br>],<br>"Resource": "arn:aws:secretsmanager:us-east-1:`111122223333`:secret:`sc-source-secret`*"<br>}<br>]<br>}`<br>``                                                                                                                                                                                                                                                                                                                                                                              |
| `sc-target-secret-role`    | Allows DMS Schema Conversion to retrieve your target<br>database credentials:<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"secretsmanager:GetSecretValue",<br>"secretsmanager:DescribeSecret"<br>],<br>"Resource": "arn:aws:secretsmanager:us-east-1:`111122223333`:secret:`sc-target-secret`*"<br>}<br>]<br>}`<br>``                                                                                                                                                                                                                                                                                                                                                                              |
| `dms-vpc-role`             | `AmazonDMSVPCManagementRole` (AWS<br>managed policy). See [Creating the IAM roles to use with AWS DMS](security-iam.md#CHAP_Security.APIRole "security-iam.md#CHAP_Security.APIRole").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `dms-cloudwatch-logs-role` | `AmazonDMSCloudWatchLogsRole` (AWS<br>managed policy). See [Creating the IAM roles to use with AWS DMS](security-iam.md#CHAP_Security.APIRole "security-iam.md#CHAP_Security.APIRole").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Each role requires the following trust policy:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dms.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

To create these resources, first create the policies, then create the roles
and attach the corresponding policies. For instructions, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and [Creating a role
for an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User
Guide_.
