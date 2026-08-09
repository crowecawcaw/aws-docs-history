For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Encrypting resources with customer managed keys

Amazon Timestream for InfluxDB encrypts your data at rest by default using AWS owned encryption keys. You can
optionally specify a customer managed key (CMK) when creating a new DB instance or cluster to
control data encryption with your own AWS Key Management Service (AWS KMS) key.

## Overview

When you specify a customer managed key during resource creation, Amazon Timestream for InfluxDB uses your key
to encrypt the Amazon EBS volumes that store your database data.

Using a customer managed key gives you full control over the encryption key lifecycle,
including the ability to create, rotate, disable, and define access policies. You can also
audit key usage through AWS CloudTrail.

###### Important

You can only specify a customer managed key during resource creation. You cannot change
the encryption key after an instance or cluster has been created.

## Supported key types

Amazon Timestream for InfluxDB requires an AWS KMS symmetric encryption key (`SYMMETRIC_DEFAULT`).
The key must meet these requirements:

- Key type: Symmetric (`SYMMETRIC_DEFAULT`)
- Key usage: Encrypt and decrypt
- Key origin: AWS KMS (customer managed)
- Key Region: Same AWS Region as the database instance or cluster
- Multi-Region keys: Supported (the primary or replica key must be in the same Region as the database)

## Creating a database with a customer managed key

### Using the AWS CLI

To create a DB instance with a customer managed key, specify the
`--kms-key-id` parameter with the ARN of your AWS KMS key.

**InfluxDB 2 instance:**

```
aws timestream-influxdb create-db-instance \
    --name `my-influxdb-instance` \
    --db-instance-type db.influx.medium \
    --db-storage-type InfluxIOIncludedT1 \
    --allocated-storage 100 \
    --vpc-subnet-ids `subnet-0123456789abcdef0` `subnet-0123456789abcdef1` \
    --vpc-security-group-ids `sg-0123456789abcdef0` \
    --password `MySecurePassword123!` \
    --kms-key-id `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
```

**InfluxDB 2 Read Replicas cluster:**

```
aws timestream-influxdb create-db-cluster \
    --name `my-influxdb-cluster` \
    --db-instance-type db.influx.medium \
    --db-storage-type InfluxIOIncludedT1 \
    --allocated-storage 100 \
    --vpc-subnet-ids `subnet-0123456789abcdef0` `subnet-0123456789abcdef1` \
    --vpc-security-group-ids `sg-0123456789abcdef0` \
    --password `MySecurePassword123!` \
    --deployment-type MULTI_NODE_READ_REPLICAS \
    --failover-mode NO_FAILOVER \
    --kms-key-id `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
```

### Using the

1. Open the Amazon Timestream for InfluxDB console.
2. Choose **Create database**.
3. In the **Encryption** section, select **Customer managed key**.
4. Choose your AWS KMS key from the dropdown list, or enter the key ARN.
5. Complete the remaining configuration and choose **Create**.

## Setting up the KMS key policy

Before creating a database with a customer managed key, you must configure the key policy
to grant Amazon Timestream for InfluxDB the necessary permissions. The key policy requires two statements: one to
allow the calling role to create grants through the service, and one to allow the role to
describe the key.

Add the following statements to your key policy, replacing `account-id`,
`caller-role`, and `region` with your values:

```
{
    "Sid": "Allow Timestream InfluxDB to use the key for resource allocations",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`account-id`:role/`caller-role`"
    },
    "Action": "kms:CreateGrant",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "timestream-influxdb.`region`.amazonaws.com"
        },
        "ForAllValues:StringEquals": {
            "kms:GrantOperations": [
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "CreateGrant",
                "DescribeKey"
            ]
        },
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        }
    }
},
{
    "Sid": "Allow Timestream InfluxDB to describe the key for resource allocations",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`account-id`:role/`caller-role`"
    },
    "Action": "kms:DescribeKey",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "timestream-influxdb.`region`.amazonaws.com"
        }
    }
}
```

The first statement allows the caller's IAM role to create grants through the Amazon Timestream for InfluxDB service,
scoped to specific grant operations. The `kms:ViaService` condition ensures this
permission can only be exercised through the service, and `kms:GrantIsForAWSResource`
ensures grants are only created for AWS resources.

The second statement allows the caller's IAM role to describe the key through the service.

## Viewing the encryption key

To view the AWS KMS key used by a DB instance or cluster, use the `GetDbInstance`
or `GetDbCluster` API. The response includes the `kmsKeyId` field if a
customer managed key was specified during creation.

```
aws timestream-influxdb get-db-instance \
    --db-instance-identifier `my-influxdb-instance`
```

If no customer managed key was specified, the `kmsKeyId` field is not present
in the response, indicating that the database uses the default AWS owned key.

## Monitoring key usage with CloudTrail

When you use a customer managed key, AWS CloudTrail records all AWS KMS API calls made by
Amazon Timestream for InfluxDB. You can use these logs to audit key usage and monitor access patterns.

| Event                             | When it occurs                                                          |
| --------------------------------- | ----------------------------------------------------------------------- |
| `CreateGrant`                     | During instance or cluster creation, to allow Amazon EBS to use the key |
| `GenerateDataKeyWithoutPlaintext` | When Amazon EBS creates encrypted volumes                               |
| `Decrypt`                         | When Amazon EBS reads data from encrypted volumes                       |

The `invokedBy` field in these events shows
`timestream-influxdb.`region`.amazonaws.com`, identifying the service that initiated the request.

## Key revocation and deletion

If you disable or delete a customer managed key, or revoke the grants, Amazon Timestream for InfluxDB loses
access to the encrypted data. This results in the following behavior:

- The database instance or cluster becomes unavailable.
- Read and write operations fail.
- The database remains in a degraded state until key access is restored.

If you re-enable the key or restore the grants, the database automatically recovers and
becomes operational again.

###### Warning

If you permanently delete a customer managed key (after the AWS KMS waiting period), the
encrypted data is permanently unrecoverable. Always ensure that you no longer need access to
the data before scheduling key deletion.

**Service-managed backups:** Service-managed backups (Amazon EBS
snapshots) are encrypted with the same customer managed key. If the key is deleted, backups
cannot be restored.

## Migrating existing databases to use a customer managed key

Because you cannot change the encryption key after database creation, migrating an existing
database to use a customer managed key requires:

1. Create a new DB instance or cluster with the `--kms-key-id` parameter.
2. Migrate data from the existing database to the new database using the
   `influx backup` and `influx restore` CLI commands.
3. Update your application connection settings to point to the new database.
4. Delete the old database when migration is complete.

## Limitations

- Customer managed keys can only be specified during resource creation—not updated afterward.
- The AWS KMS key must be in the same AWS Region and account as the database.
- Only symmetric encryption keys (`SYMMETRIC_DEFAULT`) are supported.
- Root volumes (operating system) are not encrypted with the customer managed key—they continue to use service-managed encryption.

## Pricing

There is no additional Amazon Timestream for InfluxDB charge for using customer managed keys. Standard AWS KMS
pricing applies for your key and the API calls made by the service. For details, see
[AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").
