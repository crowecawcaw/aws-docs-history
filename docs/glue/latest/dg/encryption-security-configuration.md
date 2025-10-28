# Encrypting data written by

AWS Glue

A _security configuration_ is a set of security properties that can be
used by AWS Glue. You can use a security configuration to encrypt data at rest. The following
scenarios show some of the ways that you can use a security configuration.

- Attach a security configuration to an AWS Glue crawler to write encrypted
  Amazon CloudWatch Logs. For more information about attaching security configurations to crawlers, see [Step 3: Configure security settings](define-crawler-configure-security-settings.md "define-crawler-configure-security-settings.md").
- Attach a security configuration to an extract, transform, and load (ETL) job to write
  encrypted Amazon Simple Storage Service (Amazon S3) targets and encrypted CloudWatch Logs.
- Attach a security configuration to an ETL job to write its jobs bookmarks as encrypted
  Amazon S3 data.
- Attach a security configuration to a development endpoint to write encrypted Amazon S3 targets.

###### Important

Currently, a security configuration overrides any server-side encryption
(SSE-S3) setting that is passed as an ETL job parameter. Thus, if both a
security configuration and an SSE-S3 parameter are associated with a job, the
SSE-S3 parameter is ignored.

For more information about security configurations,
see [Managing security configurations on
the AWS Glue console](console-security-configurations.md "console-security-configurations.md").

###### Topics

- [Setting Up AWS Glue to use security
  configurations](#encryption-setup-Glue "#encryption-setup-Glue")
- [Creating a route to AWS KMS for VPC jobs and
  crawlers](#encryption-kms-vpc-endpoint "#encryption-kms-vpc-endpoint")
- [Managing security configurations on
  the AWS Glue console](console-security-configurations.md "console-security-configurations.md")

## Setting Up AWS Glue to use security

configurations

Follow these steps to set up your AWS Glue environment to use security
configurations.

1. Create or update your AWS Key Management Service (AWS KMS) keys to grant AWS KMS
   permissions to the IAM roles that are passed to AWS Glue crawlers and
   jobs to encrypt CloudWatch Logs. For more information, see [Encrypt Log Data in
   CloudWatch Logs Using AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the
   _Amazon CloudWatch Logs User Guide_.

In the following example, `"role1"`,
`"role2"`, and
`"role3"` are IAM roles that are passed
to crawlers and jobs.

```
{
       "Effect": "Allow",
       "Principal": { "Service": "logs.`region`.amazonaws.com",
       "AWS": [
                `"role1"`,
                `"role2"`,
                `"role3"`
             ] },
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
use the key to encrypt CloudWatch Logs. 2. Ensure that the AWS KMS key is `ENABLED` before it is used.

###### Note

If you are using Iceberg as your data lake framework, Iceberg tables have their own mechanisms to enable server-side encryption. You should enable these configuration in addition to AWS Glue's security configurations. To enable server-side encryption on Iceberg tables, review the guidance from [Iceberg documentation](https://iceberg.apache.org/docs/latest/aws/#s3-server-side-encryption "https://iceberg.apache.org/docs/latest/aws/#s3-server-side-encryption").

## Creating a route to AWS KMS for VPC jobs and

crawlers

You can connect directly to AWS KMS
through a private endpoint in your virtual private cloud (VPC) instead of connecting over
the internet. When you use a VPC endpoint, communication between your VPC and AWS KMS is
conducted entirely within the AWS network.

You can create an AWS KMS VPC endpoint within a VPC. Without this step,
your jobs or crawlers might fail with a `kms timeout` on jobs or an
`internal service exception` on crawlers. For detailed instructions, see [Connecting to AWS KMS Through a VPC
Endpoint](../../../kms/latest/developerguide/kms-vpc-endpoint.md "../../../kms/latest/developerguide/kms-vpc-endpoint.md") in the _AWS Key Management Service Developer Guide_.

As you follow these instructions, on the [VPC
console](https://console.aws.amazon.com//vpc "https://console.aws.amazon.com//vpc"), you must do the following:

- Select **Enable Private DNS name**.
- Choose the **Security group** (with self-referencing rule) that you use for
  your job or crawler that accesses Java Database Connectivity (JDBC). For more
  information about AWS Glue connections, see [Connecting to data](glue-connections.md "glue-connections.md").

When you add a security configuration to a crawler or job that accesses JDBC data
stores, AWS Glue must have a route to the AWS KMS endpoint. You can provide the route with a
network address translation (NAT) gateway or with an AWS KMS VPC endpoint. To create a NAT
gateway, see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
_Amazon VPC User Guide_.
