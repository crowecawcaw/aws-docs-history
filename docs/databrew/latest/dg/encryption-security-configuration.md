# Encrypting data written by DataBrew

jobs

DataBrew jobs can write to encrypted Amazon S3 targets and encrypted Amazon CloudWatch Logs.

###### Topics

- [Setting up DataBrew to use
  encryption](#encryption-setup-DataBrew "#encryption-setup-DataBrew")
- [Creating a route to AWS KMS for VPC
  jobs](#encryption-kms-vpc-endpoint "#encryption-kms-vpc-endpoint")
- [Setting up encryption with AWS KMS keys](#console-security-configurations-wizard "#console-security-configurations-wizard")

## Setting up DataBrew to use

encryption

Follow this procedure to set up your DataBrew environment to use encryption.

###### To set up your DataBrew environment to use encryption

1. Create or update your AWS KMS keys to give AWS KMS permissions to the
   AWS Identity and Access Management (IAM) roles that are passed to DataBrew jobs. These IAM roles are used to encrypt CloudWatch Logs and Amazon S3
   targets. For more information, see [Encrypt Log Data in
   CloudWatch Logs Using AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the
   _Amazon CloudWatch Logs User Guide_.

In the following example,
`"role1"`,
`"role2"`, and
`"role3"` are IAM roles
that are passed to DataBrew jobs. This policy statement describes a KMS key policy that
gives permission to the listed IAM roles to encrypt and decrypt with this KMS key.

```

   {
       "Effect": "Allow",
       "Principal": {
           "Service": "logs.`region`.amazonaws.com",
           "AWS": [
               "`role1`",
               "`role2`",
               "`role3`"
           ]
       },
       "Action": [
           "kms:Encrypt*",
           "kms:Decrypt*",
           "kms:ReEncrypt*",
           "kms:GenerateDataKey*",
           "kms:Describe*"
       ],
       "Resource": "*"
   }

```

The `Service` statement, shown as `"Service":
 "logs.`region`.amazonaws.com"`, is required if you
use the key to encrypt CloudWatch Logs. 2. Ensure that the AWS KMS key is set to `ENABLED` before it is
used.

For more information about specifying permissions using AWS KMS key policies, see
[Using key
policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md").

## Creating a route to AWS KMS for VPC

jobs

You can connect directly to AWS KMS
through a private endpoint in your virtual private cloud (VPC) instead of connecting over
the internet. When you use a VPC endpoint, communication between your VPC and AWS KMS is
conducted entirely within the AWS network.

You can create an AWS KMS VPC endpoint within a VPC. Without this step,
your DataBrew jobs might fail with a `kms timeout`. For detailed instructions, see [Connecting to AWS KMS Through a VPC
Endpoint](../../../kms/latest/developerguide/kms-vpc-endpoint.md "../../../kms/latest/developerguide/kms-vpc-endpoint.md") in the _AWS Key Management Service Developer Guide_.

As you follow these instructions, on the [VPC console](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc"), make sure to do the following:

- Choose **Enable Private DNS name**.
- For **Security group**, choose the security group (including a
  self-referencing rule) that you use for your DataBrew job that accesses
  Java Database Connectivity (JDBC).

When you run a DataBrew job that accesses JDBC data
stores, DataBrew must have a route to the AWS KMS endpoint. You can provide the route with a
network address translation (NAT) gateway or with an AWS KMS VPC endpoint. To create a NAT
gateway, see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
_Amazon VPC User Guide_.

## Setting up encryption with AWS KMS keys

When you enable encryption on a job, it applies to both Amazon S3 and CloudWatch. The IAM
role that is passed must have the following AWS KMS permissions.

For more information, see the following topics in the
_Amazon Simple Storage Service User Guide_:

- For information about `SSE-S3`, see [Protecting Data Using
  Server-Side Encryption with Amazon S3-Managed Encryption Keys
  (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md").
- For information about `SSE-KMS`, see [Protecting Data Using Server-Side
  Encryption with AWS KMS–Managed Keys (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").
