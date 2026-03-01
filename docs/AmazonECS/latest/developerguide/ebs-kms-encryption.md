# Encrypt data stored in Amazon EBS volumes attached to Amazon ECS tasks

You can use AWS Key Management Service (AWS KMS) to make and manage cryptographic keys that protect your
data. Amazon EBS volumes are encrypted at rest by using AWS KMS keys. The following types
of data are encrypted:

- Data stored at rest on the volume
- Disk I/O
- Snapshots created from the volume
- New volumes created from encrypted snapshots
  Amazon EBS volumes that are attached to tasks can be encrypted by using either a default
  AWS managed key with the alias `alias/aws/ebs`, or a symmetric customer managed key
  specified in the volume configuration. Default AWS managed keys are unique to each
  AWS account per AWS Region and are created automatically. To create a symmetric
  customer managed key, follow the steps in [Creating
  symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS KMS Developer
  Guide_.

You can configure Amazon EBS encryption by default so that all new volumes created and
attached to a task in a specific AWS Region are encrypted by using the KMS key that
you specify for your account. For more information about Amazon EBS encryption and encryption
by default, see [Amazon EBS encryption](../../../ebs/latest/userguide/ebs-encryption.md "../../../ebs/latest/userguide/ebs-encryption.md") in the
_Amazon EBS User Guide_.

## Amazon ECS Managed Instances behavior

You encrypt Amazon EBS volumes by enabling encryption, either using encryption by
default or by enabling encryption when you create a volume that you want to encrypt.
For information about how to enable encryption by default (at the account-level, see
[Encryption by
default](../../../ebs/latest/userguide/encryption-by-default.md "../../../ebs/latest/userguide/encryption-by-default.md") in the _Amazon EBS User
Guide_.

You can configure any combination of these keys. The order of precedence of KMS keys
is as follows:

1. The KMS key specified in the volume configuration. When you specify a
   KMS key in the volume configuration, it overrides the Amazon EBS default and
   any KMS key that is specified at the account level.
2. The KMS key specified at the account level. When you specify a KMS key
   for cluster-level encryption of Amazon ECS managed storage, it overrides Amazon EBS
   default encryption but does not override any KMS key that is specified in
   the volume configuration.
3. Amazon EBS default encryption. Default encryption applies when you don't specify
   either a account-level KMS key or a key in the volume configuration. If
   you enable Amazon EBS encryption by default, the default is the KMS key you
   specify for encryption by default. Otherwise, the default is the
   AWS managed key with the alias `alias/aws/ebs`.

###### Note

If you set `encrypted` to `false` in your volume
configuration, specify no account-level KMS key, and enable Amazon EBS
encryption by default, the volume will still be encrypted with the key
specified for Amazon EBS encryption by default.

## Non-Amazon ECS Managed Instances behavior

You can also set up Amazon ECS cluster-level encryption for Amazon ECS managed storage when you
create or update a cluster. Cluster-level encryption takes effect at the task level and can be used to encrypt the Amazon EBS
volumes attached to each task running in a specific cluster by using the specified KMS key. For more information about configuring encryption at the cluster
level for each task, see [ManagedStorageConfiguration](../APIReference/API_ManagedStorageConfiguration.md "../APIReference/API_ManagedStorageConfiguration.md") in the _Amazon ECS API
reference_.

You can configure any combination of these keys. The order of precedence of KMS keys
is as follows:

1. The KMS key specified in the volume configuration. When you specify a
   KMS key in the volume configuration, it overrides the Amazon EBS default and any
   KMS key that is specified at the cluster level.
2. The KMS key specified at the cluster level. When you specify a KMS key for
   cluster-level encryption of Amazon ECS managed storage, it overrides Amazon EBS default
   encryption but does not override any KMS key that is specified in the volume
   configuration.
3. Amazon EBS default encryption. Default encryption applies when you don't specify
   either a cluster-level KMS key or a key in the volume configuration. If you
   enable Amazon EBS encryption by default, the default is the KMS key you specify for
   encryption by default. Otherwise, the default is the AWS managed key with the
   alias `alias/aws/ebs`.

###### Note

If you set `encrypted` to `false` in your volume
configuration, specify no cluster-level KMS key, and enable Amazon EBS
encryption by default, the volume will still be encrypted with the key
specified for Amazon EBS encryption by default.

## Customer managed KMS key policy

To encrypt an EBS volume that's attached to your task by using a customer managed key, you
must configure your KMS key policy to ensure that the IAM role that you use for
volume configuration has the necessary permissions to use the key. The key policy
must include the `kms:CreateGrant` and `kms:GenerateDataKey*`
permissions. The `kms:ReEncryptTo` and `kms:ReEncryptFrom`
permissions are necessary for encrypting volumes that are created using snapshots.
If you want to configure and encrypt only new, empty volumes for attachment, you can
exclude the `kms:ReEncryptTo` and `kms:ReEncryptFrom`
permissions.

The following JSON snippet shows key policy statements that you can attach to your
KMS key policy. Using these statements will provide access for Amazon ECS to use the
key for encrypting the EBS volume. To use the example policy statements, replace the
`user input placeholders` with your
own information. As always, only configure the permissions that you need.

```
{
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::`111122223333`:role/ecsInfrastructureRole" },
      "Action": "kms:DescribeKey",
      "Resource":"*"
    },
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::`111122223333`:role/ecsInfrastructureRole" },
      "Action": [
      "kms:GenerateDataKey*",
      "kms:ReEncryptTo",
      "kms:ReEncryptFrom"
      ],
      "Resource":"*",
      "Condition": {
        "StringEquals": {
          "kms:CallerAccount": "`aws_account_id`",
          "kms:ViaService": "ec2.`region`.amazonaws.com"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:ebs:id"
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::`111122223333`:role/`ecsInfrastructureRole`" },
      "Action": "kms:CreateGrant",
      "Resource":"*",
      "Condition": {
        "StringEquals": {
          "kms:CallerAccount": "`aws_account_id`",
          "kms:ViaService": "ec2.`region`.amazonaws.com"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:ebs:id"
        },
        "Bool": {
          "kms:GrantIsForAWSResource": true
        }
      }
    }
```

For more information about key policies and permissions, see [Key
policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") and [AWS KMS
permissions](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md") in the _AWS KMS Developer Guide_. For
troubleshooting EBS volume attachment issues related to key permissions, see [Troubleshooting Amazon EBS volume attachments to Amazon ECS tasks](troubleshoot-ebs-volumes.md "troubleshoot-ebs-volumes.md").
