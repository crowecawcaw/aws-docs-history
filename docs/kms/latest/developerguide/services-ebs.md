# How Amazon Elastic Block Store (Amazon EBS) uses AWS KMS

This topic discusses in detail how [Amazon Elastic Block Store
(Amazon EBS)](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") uses AWS KMS to encrypt volumes and snapshots. For basic instructions about
encrypting Amazon EBS volumes, see [Amazon EBS
Encryption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md").

###### Topics

- [Amazon EBS encryption](#ebs-encrypt "#ebs-encrypt")
- [Using KMS keys and data keys](#ebs-cmk "#ebs-cmk")
- [Amazon EBS encryption context](#ebs-encryption-context "#ebs-encryption-context")
- [Detecting Amazon EBS failures](#ebs-failures "#ebs-failures")
- [Using AWS CloudFormation to create encrypted
  Amazon EBS volumes](#ebs-encryption-using-cloudformation "#ebs-encryption-using-cloudformation")

## Amazon EBS encryption

When you attach an encrypted Amazon EBS volume to a [supported Amazon Elastic Compute Cloud (Amazon EC2) instance type](../../../ebs/latest/userguide/ebs-encryption-requirements.md#ebs-encryption_supported_instances "../../../ebs/latest/userguide/ebs-encryption-requirements.md#ebs-encryption_supported_instances"), data stored at rest on the volume, disk
I/O, and snapshots created from the volume are all encrypted. The encryption occurs on the
servers that host Amazon EC2 instances.

This feature is supported on all [Amazon EBS volume
types](../../../ebs-encryption-requirements.md#ebs-encryption-volume-types "../../../ebs-encryption-requirements.md#ebs-encryption-volume-types"). You access encrypted volumes the same way you access other volumes;
encryption and decryption are handled transparently and they require no additional action from
you, your EC2 instance, or your application. Snapshots of encrypted volumes are automatically
encrypted, and volumes that are created from encrypted snapshots are also automatically
encrypted.

The encryption status of an EBS volume is determined when you create the volume. You
cannot change the encryption status of an existing volume. However, you can [migrate data](../../../ebs/latest/userguide/how-ebs-encryption-works.md "../../../ebs/latest/userguide/how-ebs-encryption-works.md")
between encrypted and unencrypted volumes and apply a new encryption status while copying a
snapshot.

Amazon EBS supports optional encryption by default. You can enable encryption automatically on
all new EBS volumes and snapshot copies in your AWS account and Region. This configuration
setting doesn't affect existing volumes or snapshots. For details, see [Amazon EBS encryption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md#encryption-by-default "../../../AWSEC2/latest/UserGuide/EBSEncryption.md#encryption-by-default") in the
_Amazon EBS User Guide_.

## Using KMS keys and data keys

When you [create an encrypted Amazon EBS
volume](../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md "../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md"), you specify an AWS KMS key. By default, Amazon EBS uses the [AWS managed key](concepts.md#aws-managed-key "concepts.md#aws-managed-key") for Amazon EBS in your account
(`aws/ebs`). However, you can specify a [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key") that you create and manage.

To use a customer managed key, you must give Amazon EBS permission to use the KMS key on your behalf.
For more information , see [How Amazon EBS encryption works](../../../ebs/latest/userguide/how-ebs-encryption-works.md "../../../ebs/latest/userguide/how-ebs-encryption-works.md")
in _Amazon EBS User Guide_.

###### Important

Amazon EBS supports only [symmetric KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks"). You
cannot use an [asymmetric KMS key](symmetric-asymmetric.md "symmetric-asymmetric.md") to encrypt an
Amazon EBS volume. For help determining whether a KMS key is symmetric or asymmetric, see [Identify different key types](identify-key-types.md "identify-key-types.md").

For each volume, Amazon EBS asks AWS KMS to generate a unique data key encrypted under the
KMS key that you specify. Amazon EBS stores the encrypted data key with the volume. Then, when
you attach the volume to an Amazon EC2 instance, Amazon EBS calls AWS KMS to decrypt the data key. Amazon EBS
uses the plaintext data key in hypervisor memory to encrypt all disk I/O to the volume. For
details, see _How EBS encryption works_ in the [Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide/EBSEncryption.md#how-ebs-encryption-works "../../../AWSEC2/latest/UserGuide/EBSEncryption.md#how-ebs-encryption-works") or
[Amazon EC2 User Guide](../../../AWSEC2/latest/WindowsGuide/EBSEncryption.md#how-ebs-encryption-works "../../../AWSEC2/latest/WindowsGuide/EBSEncryption.md#how-ebs-encryption-works").

## Amazon EBS encryption context

In its [GenerateDataKeyWithoutPlaintext](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md") and [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md")
requests to AWS KMS, Amazon EBS uses an encryption context with a name-value pair that identifies the
volume or snapshot in the request. The name in the encryption context does not vary.

An [encryption context](encrypt_context.md "encrypt_context.md") is a set of key–value pairs
that contain arbitrary nonsecret data. When you include an encryption context in a request to
encrypt data, AWS KMS cryptographically binds the encryption context to the encrypted data. To
decrypt the data, you must pass in the same encryption context.

For all volumes and for encrypted snapshots created with the Amazon EBS [CreateSnapshot](../../../AWSEC2/latest/APIReference/API_CreateSnapshot.md "../../../AWSEC2/latest/APIReference/API_CreateSnapshot.md") operation, Amazon EBS uses the
volume ID as encryption context value. In the `requestParameters` field of a CloudTrail
log entry, the encryption context looks similar to the following:

```
"encryptionContext": {
  **"aws:ebs:id": "vol-0cfb133e847d28be9"**
}
```

For encrypted snapshots created with the Amazon EC2 [CopySnapshot](../../../AWSEC2/latest/APIReference/API_CopySnapshot.md "../../../AWSEC2/latest/APIReference/API_CopySnapshot.md") operation, Amazon EBS uses the
snapshot ID as encryption context value. In the `requestParameters` field of a CloudTrail
log entry, the encryption context looks similar to the following:

```
"encryptionContext": {
  **"aws:ebs:id": "snap-069a655b568de654f"**
}
```

## Detecting Amazon EBS failures

To create an encrypted EBS volume or attach the volume to an EC2 instance, Amazon EBS and the
Amazon EC2 infrastructure must be able to use the KMS key that you specified for EBS volume
encryption. When the KMS key is not usable—for example, when its [key state](key-state.md "key-state.md") is not `Enabled` —the volume creation
or volume attachment fails.

In this case, Amazon EBS sends an _event_ to Amazon EventBridge (formerly CloudWatch Events) to
notify you about the failure. In EventBridge, you can establish rules that trigger automatic actions
in response to these events. For more information, see [Amazon CloudWatch Events for
Amazon EBS](../../../AWSEC2/latest/UserGuide/ebs-cloud-watch-events.md "../../../AWSEC2/latest/UserGuide/ebs-cloud-watch-events.md") in the
_Amazon EBS User Guide_, especially the following sections:

- [Invalid
  Encryption Key on Volume Attach or Reattach](../../../AWSEC2/latest/UserGuide/ebs-cloud-watch-events.md#attach-fail-key "../../../AWSEC2/latest/UserGuide/ebs-cloud-watch-events.md#attach-fail-key")
- [Invalid
  Encryption Key on Create Volume](../../../AWSEC2/latest/UserGuide/ebs-cloud-watch-events.md#create-fail-key "../../../AWSEC2/latest/UserGuide/ebs-cloud-watch-events.md#create-fail-key")

To fix these failures, ensure that the KMS key that you specified for EBS volume
encryption is enabled. To do this, first [view the
KMS key](viewing-keys.md "viewing-keys.md") to determine its current key state (the **Status** column
in the AWS Management Console). Then, see the information at one of the following links:

- If the KMS key's key state is disabled, [enable
  it](enabling-keys.md "enabling-keys.md").
- If the KMS key's key state is pending import, [import
  key material](importing-keys.md "importing-keys.md").
- If the KMS key's key state is pending deletion, [cancel key deletion](deleting-keys-scheduling-key-deletion.md "deleting-keys-scheduling-key-deletion.md").

## Using AWS CloudFormation to create encrypted

Amazon EBS volumes

You can use [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md") to create
encrypted Amazon EBS volumes. For more information, see [AWS::EC2::Volume](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.md") in the
_AWS CloudFormation User Guide_.
