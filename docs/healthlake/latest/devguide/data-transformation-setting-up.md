# Setting up

In this chapter, you use the AWS Management Console to set up the required permissions to start
using AWS HealthLake Data transformation and running data transformation jobs.

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating
an AWS account, see [Getting started with an
AWS account](../../../accounts/latest/reference/welcome-first-time-user.md "../../../accounts/latest/reference/welcome-first-time-user.md") in the _AWS Account Management Reference
Guide_.

## Configure an IAM user or role to use HealthLake Data Transformation

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "healthlake:CreateDataTransformationProfile",
        "healthlake:GetDataTransformationProfile",
        "healthlake:UpdateDataTransformationProfile",
        "healthlake:PublishDataTransformationProfile",
        "healthlake:ListDataTransformationProfileVersions",
        "healthlake:UpdateProfileWithAgent",
        "healthlake:TransformData",
        "healthlake:ValidateSource",
        "healthlake:StartDataTransformationJob",
        "healthlake:DescribeDataTransformationJob",
        "healthlake:DeleteDataTransformationProfile",
        "healthlake:ListDataTransformationProfiles",
        "healthlake:ListDataTransformationJobs"
      ],
      "Resource": "*"
    }
  ]
}
```

For production, scope Resource to specific profile and job ARNs rather than \*.

## Setting up permissions to do data transformation jobs

Before you run a bulk data transformation job, you must grant HealthLake permission to
access your source and output Amazon Amazon S3 buckets. To grant HealthLake access, you
create an IAM service role, add a trust policy that allows HealthLake to assume the
role, and attach a permissions policy that grants read access to your source data and
write access to your output location.

When you start a data transformation job, you specify the Amazon Resource Name (ARN)
of this role for the DataAccessRoleArn parameter. For more information about IAM roles
and trust policies, see [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md").

If you already created a data access role for HealthLake import or export jobs, you
can reuse it: add the permissions listed in step 3 below for your source and
output Amazon S3 buckets.

###### Note

This role is used for both standalone transformation jobs
(StartDataTransformationJob) and composite convert-and-ingest jobs
(StartFHIRImportJob with a ProfileId).

To set up data transformation job permissions

1. If you haven't already, create source and output Amazon Amazon S3 buckets. The
   Amazon S3 buckets must be in the same AWS Region as the service, and Block Public
   Access must be turned on for all options. To learn more, see [Using
   Amazon Amazon S3 block public access](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md"). A customer-managed AWS KMS key must be
   used to encrypt job output. To learn more about using AWS KMS keys, see [Amazon Key
   Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
2. Create a data access service role for HealthLake and give the HealthLake
   service permission to assume it with the following trust policy.

###### Note

Replace 123456789012 with your AWS account ID.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "healthlake.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                }
            }
        }
    ]
}
```

3. Add a permissions policy to the data access role that grants read access to
   your source bucket, write access to your output bucket, and the required AWS KMS
   permissions to encrypt and decrypt data. Replace the bucket names and AWS KMS key
   ARN with your own values.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadSourceData",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-source-bucket",
                "arn:aws:s3:::amzn-s3-demo-source-bucket/*"
            ]
        },
        {
            "Sid": "WriteOutputData",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-output-bucket",
                "arn:aws:s3:::amzn-s3-demo-output-bucket/*"
            ]
        },
        {
            "Sid": "KMSPermissions",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:us-west-2:123456789012:key/your-kms-key-id"
        }
    ]
}
```

Explanation of permissions:

- s3:GetObject and s3:ListBucket on the source bucket: allows HealthLake
  to read your input files.
- s3:PutObject on the output bucket: allows HealthLake to write
  converted FHIR files, error reports, the manifest, and drift reports.
- s3:GetObject and s3:ListBucket on the output bucket: allows HealthLake
  to read intermediate conversion results during multi-step processing.
- kms:Decrypt: allows HealthLake to decrypt source files if your source
  bucket uses a customer-managed AWS KMS key.
- kms:GenerateDataKey: allows HealthLake to encrypt output files with
  the AWS KMS key you specify in
  OutputDataConfig.S3Configuration.KmsKeyId.
- kms:DescribeKey: allows HealthLake to verify the AWS KMS key is valid
  and accessible.

###### Important

If your source and output are the same bucket, you can combine the Amazon S3 statements
into one. If they use different AWS KMS keys, add a separate AWS KMS statement for each
key ARN.

###### Tip

For production, scope the Resource values as narrowly as possible: specify
the exact Amazon S3 prefixes your jobs use rather than granting access to the entire
bucket.

For detailed datastore setup, refer [Setting up
AWS HealthLake](getting-started-setting-up.md "getting-started-setting-up.md").
