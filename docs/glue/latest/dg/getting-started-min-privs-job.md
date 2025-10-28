# Review IAM permissions needed for ETL

jobs

When you create a job using AWS Glue Studio, the job assumes the permissions of the IAM role
that you specify when you create it. This IAM role must have permission to extract
data from your data source, write data to your target, and access AWS Glue resources.

The name of the role that you create for the job must start with the string
`AWSGlueServiceRole` for it to be used correctly by AWS Glue Studio. For example,
you might name your role `AWSGlueServiceRole-FlightDataJob`.

## Data source and data target

permissions

An AWS Glue Studio job must have access to Amazon S3 for any sources, targets,
scripts, and temporary directories that you use in your job. You can create a policy
to provide fine-grained access to specific Amazon S3 resources.

- Data sources require `s3:ListBucket` and
  `s3:GetObject` permissions.
- Data targets require `s3:ListBucket`,
  `s3:PutObject`, and `s3:DeleteObject`
  permissions.

###### Note

Your IAM policy needs to allow `s3:GetObject` for the specific buckets used for hosting AWS Glue transforms.

The following buckets are owned by the AWS service account and is worldwide readable. These buckets serve
as a repository for the source code pertinent to a subset of transformations accessible via the AWS Glue Studio visual editor.
Permissions on the bucket are set up to deny any other API action on the bucket. Anybody can read those scripts we
provide for the transformations, but nobody outside our service team can "put" anything in them. When your AWS Glue job
runs, that file is pulled in as a local import so the file is downloaded to the local container. After that, there is
no further communication with that account.

Region: Bucket name

- af-south-1: aws-glue-studio-transforms-762339736633-prod-af-south-1
- ap-east-1: aws-glue-studio-transforms-125979764932-prod-ap-east-1
- ap-northeast-2: aws-glue-studio-transforms-673535381443-prod-ap-northeast-2
- ap-northeast-3: aws-glue-studio-transforms-149976050262-prod-ap-northeast-3
- ap-south-1: aws-glue-studio-transforms-584702181950-prod-ap-south-1
- ap-south-2: aws-glue-studio-transforms-380279651983-prod-ap-south-2
- ap-southeast-1: aws-glue-studio-transforms-737106620487-prod-ap-southeast-1
- ap-southeast-2: aws-glue-studio-transforms-234881715811-prod-ap-southeast-2
- ap-southeast-3: aws-glue-studio-transforms-151265630221-prod-ap-southeast-3
- ap-southeast-4: aws-glue-studio-transforms-052235663858-prod-ap-southeast-4
- ca-central-1: aws-glue-studio-transforms-622716468547-prod-ca-central-1
- ca-west-1: aws-glue-studio-transforms-915795495192-prod-ca-west-1
- eu-central-1: aws-glue-studio-transforms-560373232017-prod-eu-central-1
- eu-central-2: aws-glue-studio-transforms-907358657121-prod-eu-central-2
- eu-north-1: aws-glue-studio-transforms-312557305497-prod-eu-north-1
- eu-south-1: aws-glue-studio-transforms-939684186351-prod-eu-south-1
- eu-south-2: aws-glue-studio-transforms-239737454084-prod-eu-south-2
- eu-west-1: aws-glue-studio-transforms-244479516193-prod-eu-west-1
- eu-west-2: aws-glue-studio-transforms-804222392271-prod-eu-west-2
- eu-west-3: aws-glue-studio-transforms-371299348807-prod-eu-west-3
- il-central-1: aws-glue-studio-transforms-806964611811-prod-il-central-1
- me-central-1: aws-glue-studio-transforms-733304270342-prod-me-central-1
- me-south-1: aws-glue-studio-transforms-112120182341-prod-me-south-1
- sa-east-1: aws-glue-studio-transforms-881619130292-prod-sa-east-1
- us-east-1: aws-glue-studio-transforms-510798373988-prod-us-east-1
- us-east-2: aws-glue-studio-transforms-251189692203-prod-us-east-2
- us-west-1: aws-glue-studio-transforms-593230150239-prod-us-west-1
- us-west-2: aws-glue-studio-transforms-818035625594-prod-us-west-2
- ap-northeast-1: aws-glue-studio-transforms-200493242866-prod-ap-northeast-1
- cn-north-1: aws-glue-studio-transforms-071033555442-prod-cn-north-1
- cn-northwest-1: aws-glue-studio-transforms-070947029561-prod-cn-northwest-1
- us-gov-west-1: aws-glue-studio-transforms-227493901923-prod-us-gov-west-1-2604

If you choose Amazon Redshift as your data source, you can provide a role
for cluster permissions. Jobs that run against a Amazon Redshift cluster
issue commands that access Amazon S3 for temporary storage using temporary
credentials. If your job runs for more than an hour, these credentials will expire
causing the job to fail. To avoid this problem, you can assign a role to the
Amazon Redshift cluster itself that grants the necessary permissions to jobs
using temporary credentials. For more information, see [Moving Data to and from Amazon Redshift](aws-glue-programming-etl-redshift.md "aws-glue-programming-etl-redshift.md") in the
_AWS Glue Developer Guide_.

If the job uses data sources or targets other than Amazon S3, then you
must attach the necessary permissions to the IAM role used by the job to access
these data sources and targets. For more information, see [Setting Up Your
Environment to Access Data Stores](start-connecting.md "start-connecting.md") in the
_AWS Glue Developer Guide_.

If you're using connectors and connections for your data store, you need
additional permissions, as described in [Permissions required for
using connectors](#getting-started-min-privs-connectors "#getting-started-min-privs-connectors").

## Permissions required for deleting jobs

In AWS Glue Studio you can select multiple jobs in the console to delete. To perform this
action, you must have the `glue:BatchDeleteJob` permission. This is
different from the AWS Glue console, which requires the `glue:DeleteJob`
permission for deleting jobs.

## AWS Key Management Service permissions

If you plan to access Amazon S3 sources and targets that use server-side
encryption with AWS Key Management Service (AWS KMS), then attach a policy to the AWS Glue Studio role
used by the job that enables the job to decrypt the data. The job role needs the
`kms:ReEncrypt`, `kms:GenerateDataKey`, and
`kms:DescribeKey` permissions. Additionally, the job role needs the
`kms:Decrypt` permission to upload or download an Amazon S3
object that is encrypted with an AWS KMS customer master key (CMK).

There are additional charges for using AWS KMS CMKs. For more information, see
[AWS Key Management Service Concepts - Customer Master Keys
(CMKs)](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys") and [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing "https://aws.amazon.com/kms/pricing") in the
_AWS Key Management Service Developer Guide_.

## Permissions required for

using connectors

If you're using an AWS Glue Custom Connector and connection to access a data store,
the role used to run the AWS Glue ETL job needs additional permissions attached:

- The AWS managed policy `AmazonEC2ContainerRegistryReadOnly` for
  accessing connectors purchased from AWS Marketplace.
- The `glue:GetJob` and `glue:GetJobs`
  permissions.
- AWS Secrets Manager permissions for accessing secrets that are
  used with connections. Refer to [Example: Permission to retrieve secret values](../../../secretsmanager/latest/userguide/auth-and-access_examples.md#auth-and-access_examples_read "../../../secretsmanager/latest/userguide/auth-and-access_examples.md#auth-and-access_examples_read") for example IAM policies.

If your AWS Glue ETL job runs within a VPC running Amazon VPC, then the VPC must be
configured as described in [Configure a VPC for your ETL job](getting-started-vpc-config.md "getting-started-vpc-config.md").
