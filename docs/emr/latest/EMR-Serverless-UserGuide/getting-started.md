# Getting started with Amazon EMR Serverless

This tutorial helps you get started with EMR Serverless when you deploy a sample Spark or
Hive workload. You'll create, run, and debug your own application. We show default options in
most parts of this tutorial.

Before you launch an EMR Serverless application, complete the following tasks.

###### Topics

- [Grant permissions to use EMR Serverless](#gs-permissions "#gs-permissions")
- [Prepare storage for EMR Serverless](#gs-prepare-storage "#gs-prepare-storage")
- [Create an EMR Studio to run interactive
  workloads](#gs-interactive "#gs-interactive")
- [Create a job runtime role](#gs-runtime-role "#gs-runtime-role")
- [Getting started with EMR Serverless from the console](gs-console.md "gs-console.md")
- [Getting started from the AWS CLI](gs-cli.md "gs-cli.md")

## Grant permissions to use EMR Serverless

To use EMR Serverless, you need a user or IAM role with an attached policy that
grants permissions for EMR Serverless. To create a user and attach the appropriate policy
to that user, follow the instructions in [Grant permissions](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").

## Prepare storage for EMR Serverless

In this tutorial, you'll use an S3 bucket to store output files and logs from the sample
Spark or Hive workload that you'll run using an EMR Serverless application. To create a
bucket, follow the instructions in [Creating a bucket](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md") in the
_Amazon Simple Storage Service Console User Guide_. Replace any further reference to
`amzn-s3-demo-bucket` with the name of the newly
created bucket.

## Create an EMR Studio to run interactive

workloads

If you want to use EMR Serverless to execute interactive queries through notebooks that
are hosted in EMR Studio, you need to specify an S3 bucket and the [minimum service role for EMR Serverless](../ManagementGuide/emr-studio-service-role.md#emr-studio-service-role-serverless "../ManagementGuide/emr-studio-service-role.md#emr-studio-service-role-serverless") to create a Workspace. For steps to get
set up, see [Set up an EMR Studio](../ManagementGuide/emr-studio-set-up.md "../ManagementGuide/emr-studio-set-up.md")
in the _Amazon EMR Management Guide_. For more information on interactive workloads,
see [Run interactive workloads with EMR Serverless through
EMR Studio](interactive-workloads.md "interactive-workloads.md").

## Create a job runtime role

Job runs in EMR Serverless use a runtime role that provides granular permissions to
specific AWS services and resources at runtime. In this tutorial, a public S3 bucket hosts
the data and scripts. The bucket `amzn-s3-demo-bucket`
stores the output.

To set up a job runtime role, first create a runtime role with a trust policy so that
EMR Serverless can use the new role. Next, attach the required S3 access policy to that
role. The following steps guide you through the process.

Console

1. Navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Policies**.
3. Choose **Create Policy**.
4. The **Create policy** page opens on a new tab. Select the **Policy editor** as Json and Paste the
   policy JSON below.

###### Important

Replace `amzn-s3-demo-bucket` in the
policy below with the actual bucket name created in [Prepare storage for EMR Serverless](#gs-prepare-storage "#gs-prepare-storage"). This is a
basic policy for S3 access. For more job runtime role examples, see [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md "security-iam-runtime-role.md").

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadAccessForEMRSamples",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::*.elasticmapreduce",
 "arn:aws:s3:::*.elasticmapreduce/*"
 ]
 },
 {
 "Sid": "FullAccessToOutputBucket",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Sid": "GlueCreateAndReadDataCatalog",
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:CreateDatabase",
 "glue:GetDataBases",
 "glue:CreateTable",
 "glue:GetTable",
 "glue:UpdateTable",
 "glue:DeleteTable",
 "glue:GetTables",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:CreatePartition",
 "glue:BatchCreatePartition",
 "glue:GetUserDefinedFunctions"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

5. Choose **Next** to enter a name for your policy,
   such as `EMRServerlessS3AndGlueAccessPolicy` and **Create policy**
6. In the left navigation pane of IAM console , choose **Roles**.
7. Choose **Create role**.
8. For role type, choose **Custom trust policy** and paste the
   following trust policy. This allows jobs submitted to your Amazon EMR Serverless
   applications to access other AWS services on your behalf.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::123456789012:role/EMRServerlessExecutionRole",
 "Sid": "AllowSTSAssumerole"
 }
 ]
}`

```

9. Choose **Next** to navigate to the **Add
   permissions** page, then choose **EMRServerlessS3AndGlueAccessPolicy**.
10. In the **Name, review, and create** page, for **Role
    name**, enter a name for your role, for example,
    `EMRServerlessS3RuntimeRole`. To create this IAM role, choose
    **Create role**.

CLI

1. Create a file named `emr-serverless-trust-policy.json` that
   contains the trust policy to use for the IAM role. The file should contain the
   following policy.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EMRServerlessTrustPolicy",
 "Action": [
 "sts:AssumeRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::123456789012:role/EMRServerlessExecutionRole"
 }
 ]
}`

```

2. Create an IAM role named `EMRServerlessS3RuntimeRole`. Use the
   trust policy that you created in the previous step.

```
aws iam create-role \
    --role-name EMRServerlessS3RuntimeRole \
    --assume-role-policy-document file://emr-serverless-trust-policy.json
```

Note the ARN in the output. You use the ARN of the new role during job
submission, referred to after this as the
`job-role-arn`. 3. Create a file named `emr-sample-access-policy.json` that defines
the IAM policy for your workload. This provides read access to the script and
data stored in public S3 buckets and read-write access to
`amzn-s3-demo-bucket`.

###### Important

Replace `amzn-s3-demo-bucket` in the
policy below with the actual bucket name created in [Prepare storage for EMR Serverless](#gs-prepare-storage "#gs-prepare-storage").. This is a
basic policy for AWS Glue and S3 access. For more job runtime role examples, see
[Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md "security-iam-runtime-role.md").

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadAccessForEMRSamples",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::*.elasticmapreduce",
 "arn:aws:s3:::*.elasticmapreduce/*"
 ]
 },
 {
 "Sid": "FullAccessToOutputBucket",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Sid": "GlueCreateAndReadDataCatalog",
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:CreateDatabase",
 "glue:GetDataBases",
 "glue:CreateTable",
 "glue:GetTable",
 "glue:UpdateTable",
 "glue:DeleteTable",
 "glue:GetTables",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:CreatePartition",
 "glue:BatchCreatePartition",
 "glue:GetUserDefinedFunctions"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

4. Create an IAM policy named `EMRServerlessS3AndGlueAccessPolicy`
   with the policy file that you created in **Step 3**. Take note of
   the ARN in the output, as you will use the ARN of the new policy in the next step.

```
aws iam create-policy \
    --policy-name EMRServerlessS3AndGlueAccessPolicy \
    --policy-document file://emr-sample-access-policy.json
```

Note the new policy's ARN in the output. You'll substitute it for
`policy-arn` in the next step. 5. Attach the IAM policy `EMRServerlessS3AndGlueAccessPolicy` to the
job runtime role `EMRServerlessS3RuntimeRole`.

```
aws iam attach-role-policy \
    --role-name EMRServerlessS3RuntimeRole \
    --policy-arn `policy-arn`
```
