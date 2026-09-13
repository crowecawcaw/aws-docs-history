

# Copy an Amazon EBS volume
<a name="ebs-copying-volume"></a>

A volume copy is a crash-consistent, point-in-time copy of the source volume. It includes all the data blocks written to the source volume at the time the volume copy initialization begins. The volume copy gets its own unique volume ID. Volume copies are created immediately and can be attached to an Amazon EC2 instance once it reaches the `available` state. Using volume copies, you can quickly copy your production data for test and development environments.

You can also create copies from volumes shared with you by other AWS accounts. To copy a volume from another account, the source volume must be shared with you through AWS Resource Access Manager (AWS RAM). For more information, see [Share a volume](share-volume.md).

## Initialization
<a name="copy-volume-initialization"></a>

Volume copies are initialized after creation. During initialization, the data blocks are copied from the source volume and written to the volume copy in the background. The volume remains in the `initializing` state until initialization completes.

**Performance during initialization**  
Copy operations don't affect the performance of the source volume. You can continue using the source volume normally during the copy process. Copied volumes can be accessed instantly without waiting for the data to be copied from the source volume. Volume copies provide instant access to data with single-digit millisecond latency. However, actual latency might vary depending on the volume type. During initialization, the volume copy delivers **baseline performance** equal to the lowest of the following three values:
+ 3,000 input/output operations per second (IOPS) and 125 MiB/s
+ The provisioned performance for the **source volume**
+ The provisioned performance for the **volume copy**

The volume copy can exceed the baseline performance when the following criteria are met:

1. Both the source volume and volume copy are provisioned with more than 3,000 IOPS and 125 MiB/s.

1. The source volume has unutilized performance capacity (driven performance is less than provisioned performance).

For example, if the source volume is provisioned with 10,000 IOPS and your workload is currently driving only 5,000 IOPS, and the volume copy is provisioned with 10,000 IOPS, the volume copy can achieve performance higher than the 3,000 IOPS baseline performance during initialization by using the source volume's unutilized 5,000 IOPS.

**Initialization duration**  
The time it takes to initialize a volume copy depends on the size of the block data written to the source volume at the time of creating the volume copy. Volume copies are initialized on a best-effort basis, with the following general guidelines. For the first 1 TiB of data blocks, volume initialization takes up to 6 hours. For each subsequent 1 TiB of data blocks up to 16 TiB, initialization takes 1.2 hours per TiB. For written data larger than 16 TiB, initialization takes 24 hours.

**Monitor initialization progress**  
You can monitor the initialization progress using the [describe-volume-status](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volume-status.html) AWS CLI command or Amazon EventBridge. For more information, see [Monitor the status of Amazon EBS volume initialization](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-initialize-monitor.html).

## Encryption
<a name="copy-volume-encryption"></a>

When you copy a volume, the encryption of the copy depends on the encryption state of the source volume, your account's encryption by default setting, and the `Encrypted` and `KmsKeyId` parameters you specify in the copy request.

### Unencrypted source volumes
<a name="copy-volume-encryption-unencrypted"></a>

If the source volume is unencrypted and encryption by default is disabled for your account, the copy is unencrypted. You can encrypt the copy by setting the `Encrypted` parameter to `true`. If you don't specify a KMS key, your account's default Amazon EBS encryption key is used.

If the source volume is unencrypted and encryption by default is enabled for your account, the copy is automatically encrypted. If you don't specify a KMS key, your account's default Amazon EBS encryption key is used.

### Encrypted source volumes
<a name="copy-volume-encryption-encrypted"></a>

If the source volume is encrypted, the copy is always encrypted. You can't create an unencrypted copy from an encrypted source volume.

For same-account copies, the copy uses the same KMS key as the source volume by default. You can specify a different customer managed key to re-encrypt the copy.

For cross-account copies, the copy uses your account's default Amazon EBS encryption key by default. You can specify a different customer managed key in the `KmsKeyId` parameter. You can use the source account's KMS key to encrypt the volume copy if that key has been shared with your account.

### Cross-account encryption requirements
<a name="copy-volume-encryption-cross-account"></a>

To copy a shared volume that is encrypted with a customer managed key, the volume owner must share the KMS key with your account. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the AWS Key Management Service Developer Guide.

Volumes encrypted with the default AWS managed key for Amazon EBS can't be shared or copied across accounts.

### Encryption outcomes
<a name="copy-volume-encryption-outcomes"></a>


**Unencrypted source volumes**  

| Encryption by default | You specify a KMS key | Result | 
| --- | --- | --- | 
| Disabled | No | Copy is unencrypted | 
| Disabled | Yes | Copy encrypted with the specified key | 
| Enabled | No | Copy encrypted with your account's default Amazon EBS encryption key | 
| Enabled | Yes | Copy encrypted with the specified key | 


**Encrypted source volumes (same-account)**  

| You specify a KMS key | Result | 
| --- | --- | 
| No | Copy encrypted with the same key as the source volume | 
| Yes | Copy re-encrypted with the specified key | 


**Encrypted source volumes (cross-account)**  

| You specify a KMS key | Result | 
| --- | --- | 
| No | Copy encrypted with your account's default Amazon EBS encryption key | 
| Yes | Copy encrypted with the specified key | 

Cross-account copies never reuse the source account's KMS key by default. If you want to use a key from the source account, it must be shared with your account.

## Considerations
<a name="copy-volume-consids"></a>
+ A volume copy captures a crash-consistent, point-in-time state of the source volume. It includes only the data that has been written to the volume at the time of the copy request. It doesn't include data cached by applications or the operating system. To achieve application-consistent copies, pause writes to the volume or quiesce the application before creating the copy. For databases, use the appropriate mechanism to flush dirty pages and freeze I/O (such as `fsfreeze` on Linux or VSS on Windows). You can resume writes after the copy request returns.
+ You can create only one volume copy from a source volume at a time. You can create subsequent copies of the same source volume only once the previous volume copy has been fully initialized.
+ You can have a maximum of 5 in-progress volume copies per Region. If you exceed this quota, you get the `CopyVolumesLimitExceeded` error. You can [request a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) if needed.
+ The volume copy must be created in the same Availability Zone as the source volume.
+ The size of the volume copy must be equal to or greater than the size of the source volume.
+ You can't copy a volume copy while it is being created or initialized.
+ To create a volume copy, the source volume must be in the `available` or `in-use` state, and volume modifications must be in the `completed` or `optimizing` state.
+ Volume copies are subject to the same account and Regional storage and IOPS quotas as regular Amazon EBS volumes. For more information, see [Amazon EBS quotas](https://docs.aws.amazon.com/general/latest/gr/ebs-service.html#limits_ebs).
+ If you delete the source volume while the copy operation is in progress, the copy operation still completes.
+ Tags assigned to the source volume aren't assigned to the volume copy.
+ You can't create copies from volumes on Outposts or in Wavelength Zones.

## Pricing
<a name="copy-volume-pricing"></a>

When you create a copy of a source volume, you are charged for the copy operation. The copy operation charge is based on the size of the data blocks written to the source volume at the time of copy creation. The newly created volume is charged the same way as any other Amazon EBS volume. For more information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/).

## Copy a volume
<a name="copy-volume-copy"></a>

Use one of the following methods to copy an Amazon EBS volume.

------
#### [ Console ]

**To copy a volume**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Volumes**.

1. Select the volume to copy and choose **Actions**, **Copy volume**.

1. For **Volume type**, choose the volume type for the copy. The default volume type is **gp3**.

1. For **Size**, enter the size for the volume copy, in GiBs. The size must be equal to or greater than the size of the source volume.

1. (*`io1`, `io2`, and `gp3` only*) For **IOPS**, enter the maximum number of input/output operations per second (IOPS) for the volume copy.

1. (*`gp3` only*) For **Throughput**, enter the throughput for the volume copy, in MiB/s.

1. (*`io1` and `io2` only*) To enable the volume copy for Amazon EBS Multi-Attach, select **Enable Multi-Attach**.

1. For **Encryption**, the default depends on the source volume and your account settings. For same-account copies, the copy inherits the source volume's encryption key. For cross-account copies, your account's default Amazon EBS encryption key is used. You can choose a different customer managed key.

1. (*Optional*) To assign custom tags to the volume copy, in the **Tags** section, choose **Add tag**, and then enter a tag key and value pair.

1. Choose **Copy volume**.

1. The copied volume enters the `creating` state and then transitions to `available` shortly after. You can then attach it to an Amazon EC2 instance in the same Availability Zone.

------
#### [ AWS CLI ]

**To copy a volume**  
Use the [copy-volumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-volumes.html) command.

The following example creates a volume copy of `vol-01234567890abcdef` with the `gp3` volume type, a size of `100` GiB, and throughput of `250` MiB/s.

```
aws ec2 copy-volumes \
--source-volume-id {{vol-01234567890abcdef}} \
--volume-type {{gp3}} \
--size {{100}} \
--throughput {{250}}
```

**To encrypt an unencrypted volume during copy**  
Use the copy-volumes command with the `--encrypted` and `--kms-key-id` parameters.

```
aws ec2 copy-volumes \
--source-volume-id {{vol-01234567890abcdef}} \
--encrypted \
--kms-key-id {{alias/my-key}}
```

**To re-encrypt with a different customer managed key**  
Use the copy-volumes command with the `--kms-key-id` parameter to specify a different key.

```
aws ec2 copy-volumes \
--source-volume-id {{vol-01234567890abcdef}} \
--kms-key-id {{arn:aws:kms:us-east-1:222222222222:key/abcd1234-a123-456a-a12b-a123b4cd56ef}}
```

------
#### [ PowerShell ]

**To copy a volume**  
Use the [Copy-EC2Volume](https://docs.aws.amazon.com/powershell/latest/reference/items/Copy-EC2Volume.html) cmdlet.

The following example creates a volume copy of `vol-01234567890abcdef` with the `gp3` volume type, a size of `100` GiB, and throughput of `250` MiB/s.

```
Copy-EC2Volume `
-SourceVolumeId {{vol-01234567890abcdef}} `
-VolumeType {{gp3}} `
-Size {{100}} `
-Throughput {{250}}
```

**To encrypt an unencrypted volume during copy**  
Use the Copy-EC2Volume cmdlet with the `-Encrypted` and `-KmsKeyId` parameters.

```
Copy-EC2Volume `
-SourceVolumeId {{vol-01234567890abcdef}} `
-Encrypted $true `
-KmsKeyId {{"alias/my-key"}}
```

**To re-encrypt with a different customer managed key**  
Use the Copy-EC2Volume cmdlet with the `-KmsKeyId` parameter to specify a different key.

```
Copy-EC2Volume `
-SourceVolumeId {{vol-01234567890abcdef}} `
-KmsKeyId {{"arn:aws:kms:us-east-1:222222222222:key/abcd1234-a123-456a-a12b-a123b4cd56ef"}}
```

------