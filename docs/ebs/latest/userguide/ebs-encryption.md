# Amazon EBS encryption

Use Amazon EBS encryption as a straight-forward encryption solution for your Amazon EBS resources
associated with your Amazon EC2 instances. With Amazon EBS encryption, you aren't required to build,
maintain, and secure your own key management infrastructure. Amazon EBS encryption uses
AWS KMS keys when creating encrypted volumes and snapshots.

Encryption operations occur on the servers that host EC2 instances, ensuring the security
of both data-at-rest and data-in-transit between an instance and its attached EBS storage.

You can attach both encrypted and unencrypted volumes to an instance simultaneously. All
Amazon EC2 instance types support Amazon EBS encryption.

###### Contents

- [How Amazon EBS encryption works](how-ebs-encryption-works.md "how-ebs-encryption-works.md")
- [Requirements for Amazon EBS encryption](ebs-encryption-requirements.md "ebs-encryption-requirements.md")
- [Enable Amazon EBS encryption by default](encryption-by-default.md "encryption-by-default.md")
- [Encrypt EBS resources](#encryption-parameters "#encryption-parameters")
- [Rotate AWS KMS keys used for Amazon EBS encryption](kms-key-rotation.md "kms-key-rotation.md")
- [Amazon EBS encryption examples](encryption-examples.md "encryption-examples.md")

## Encrypt EBS resources

You encrypt EBS volumes by enabling encryption, either using [encryption by default](encryption-by-default.md "encryption-by-default.md") or by
enabling encryption when you create a volume that you want to encrypt.

When you encrypt a volume, you can specify the symmetric encryption KMS key to use to encrypt the
volume. If you do not specify a KMS key, the KMS key that is used for encryption depends on the
encryption state of the source snapshot and its ownership. For more information, see the
[encryption outcomes
table](encryption-examples.md#ebs-volume-encryption-outcomes "encryption-examples.md#ebs-volume-encryption-outcomes").

###### Note

If you are using the API or AWS CLI to specify a KMS key, be aware that AWS authenticates
the KMS key asynchronously. If you specify a KMS key ID, an alias, or an ARN that is not valid, the
action can appear to complete, but it eventually fails.

You cannot change the KMS key that is associated with an existing snapshot or volume.
However, you can associate a different KMS key during a snapshot copy operation so that
the resulting copied snapshot is encrypted by the new KMS key.

### Encrypt an empty volume on creation

When you create a new, empty EBS volume, you can encrypt it by enabling encryption
for the specific volume creation operation. If you enabled EBS encryption by
default, the volume is automatically encrypted using your default KMS key for EBS encryption.
Alternatively, you can specify a different symmetric encryption KMS key for the specific volume creation
operation. The volume is encrypted by the time it is first available, so your data is
always secured. For detailed procedures, see [Create an Amazon EBS volume](ebs-creating-volume.md "ebs-creating-volume.md").

By default, the KMS key that you selected when creating a volume encrypts the
snapshots that you make from the volume and the volumes that you restore from
those encrypted snapshots. You cannot remove encryption from an encrypted volume
or snapshot, which means that a volume restored from an encrypted snapshot, or
a copy of an encrypted snapshot, is always encrypted.

Public snapshots of encrypted volumes are not supported, but you can share an
encrypted snapshot with specific accounts. For detailed directions, see [Share an Amazon EBS snapshot with other AWS accounts](ebs-modifying-snapshot-permissions.md "ebs-modifying-snapshot-permissions.md").

### Encrypt unencrypted resources

You can't directly encrypt existing unencrypted volumes or snapshots.

To encrypt an unencrypted volume, create a snapshot of that volume, and then
use the snapshot to create a new encrypted volume. For more information, see
[Create snapshots](ebs-create-snapshot.md "ebs-create-snapshot.md")
and [Create a volume](ebs-creating-volume.md "ebs-creating-volume.md").

To encrypt an unencrypted snapshot, create an encrypted copy of that snapshot.
For more information, see [Copy a snapshot](ebs-copy-snapshot.md "ebs-copy-snapshot.md").

If you enable your account for encryption by default, volumes and snapshot copies
created from unencrypted snapshots are always encrypted. Otherwise, you must specify
the encryption parameters in the request. For more information, see [Enable encryption by default](encryption-by-default.md "encryption-by-default.md").
