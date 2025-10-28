# Supported Amazon EBS volumes for malware

scan

In all of the AWS Regions where GuardDuty supports the Malware Protection for EC2 feature, you can scan the
Amazon EBS volumes that are unencrypted or encrypted. You can have Amazon EBS volumes that are encrypted
with either [AWS managed key](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") or
[customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk"). Presently, some of the Regions where Malware Protection for EC2 is available, may support
both the ways to encrypt your Amazon EBS volumes, while others support only customer managed key. For
information about supported Regions, see
and [GuardDuty service accounts by
AWS Region](gdu-service-account-region-list.md "gdu-service-account-region-list.md").
For information about Regions where GuardDuty is available but Malware Protection for EC2 is not available, see
[Region-specific feature
availability](guardduty_regions.md#gd-regional-feature-availability "guardduty_regions.md#gd-regional-feature-availability").

The following list describes the key that GuardDuty uses whether or not your Amazon EBS volumes are
encrypted:

- **Amazon EBS volumes that are either unencrypted or encrypted with
  AWS managed key** – GuardDuty uses its own key to encrypt the replica
  Amazon EBS volumes.

If your Region doesn't support scanning Amazon EBS volumes that are encrypted with
[Amazon EBS encryption by default](../../../ebs/latest/userguide/encryption-by-default.md "../../../ebs/latest/userguide/encryption-by-default.md"), then you need to
modify the default key to be a customer managed key. This will help GuardDuty access these EBS volumes. By modifying the
key, even the future EBS volumes will get created with the updated key so that GuardDuty can support malware
scans. For steps to modify the default key, see [Modify default AWS KMS key ID of
an Amazon EBS volume](#regional-parity-supported-volumes-encrypt "#regional-parity-supported-volumes-encrypt") in next section.

- **Amazon EBS volumes that are encrypted with customer managed key**
  – GuardDuty uses the same key to encrypt the replica EBS volume. For information about
  what AWS KMS encryption related policies are supported, see [Service-linked role permissions for
  Malware Protection for EC2](slr-permissions-malware-protection.md "slr-permissions-malware-protection.md").

## Modify default AWS KMS key ID of

an Amazon EBS volume

When you use create an Amazon EBS volume by using [Amazon EBS encryption](../../../ebs/latest/userguide/ebs-encryption.md#encryption-parameters "../../../ebs/latest/userguide/ebs-encryption.md#encryption-parameters"),
and do not specify AWS KMS key ID, your Amazon EBS volume gets encrypted with a
[default
key for encryption](../../../ebs/latest/userguide/encryption-by-default.md "../../../ebs/latest/userguide/encryption-by-default.md"). When you enable
encryption by default, Amazon EBS will automatically encrypt new volumes and snapshots by using your default KMS key
for Amazon EBS encryption.

You can modify the default encryption key and use a customer managed key for Amazon EBS encryption. This will help GuardDuty
access these Amazon EBS volumes. To modify the EBS default key ID, add the following necessary permission to your IAM
policy – `ec2:modifyEbsDefaultKmsKeyId`. Any newly-created Amazon EBS volume
that you choose to be encrypted but don't specify an associated KMS key ID, will use the
default key ID. Use one of the following methods to update the EBS default key ID:

###### To modify default KMS key ID of an Amazon EBS volume

Do one of the following:

- **Using an API** – You can use the [ModifyEbsDefaultKmsKeyId](../../../AWSEC2/latest/APIReference/API_ModifyEbsDefaultKmsKeyId.md "../../../AWSEC2/latest/APIReference/API_ModifyEbsDefaultKmsKeyId.md") API. For information about how you can view the
  encryption status of your volume, see [Create Amazon EBS
  volume](../../../index.md "../../../index.md").
- **Using AWS CLI command** – The following example
  modifies the default KMS key ID that will encrypt Amazon EBS volumes if you don't provide a
  KMS key ID. Make sure to replace the Region with the AWS Region of your KM key
  ID.

```
aws ec2 modify-ebs-default-kms-key-id --region `us-west-2` --kms-key-id `AKIAIOSFODNN7EXAMPLE`
```

The above command will generate an output similar to the following output:

```
{
  "KmsKeyId": "arn:aws:kms:`us-west-2`:`444455556666`:key/`AKIAIOSFODNN7EXAMPLE`"
}
```

For more information, see [modify-ebs-default-kms-key-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ebs-default-kms-key-id.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ebs-default-kms-key-id.html").
