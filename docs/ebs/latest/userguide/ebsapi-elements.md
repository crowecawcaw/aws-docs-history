# Concepts for EBS direct APIs

The following are the key concepts that you should understand before getting started with
the EBS direct APIs.

## Snapshots

Snapshots are the primary means to back up data from your EBS volumes. With the
EBS direct APIs, you can also back up data from your on-premises disks to snapshots. To save
storage costs, successive snapshots are incremental, containing only the volume data that
changed since the previous snapshot. For more information, see [Amazon EBS snapshots](ebs-snapshots.md "ebs-snapshots.md").

###### Note

EBS direct APIs does not support public snapshots and local snapshots on AWS Outposts.

## Blocks

A block is a fragment of data within a snapshot. Each snapshot can contain thousands of
blocks. All blocks in a snapshot are of a fixed size.

## Block indexes

A block index is a logical index in units of `512` KiB blocks. To identify
the block index, divide the logical offset of the data in the logical volume by the block
size (logical offset of data/`524288`). The logical offset of the data must be
`512` KiB aligned.

## Block tokens

A block token is the identifying hash of a block within a snapshot, and it is used to
locate the block data. Block tokens returned by EBS direct APIs are temporary. They change on the
expiry timestamp specified for them, or if you run another ListSnapshotBlocks or
ListChangedBlocks request for the same snapshot.

## Checksum

A checksum is a small-sized datum derived from a block of data for the purpose of
detecting errors that were introduced during its transmission or storage. The EBS direct APIs use
checksums to validate data integrity. When you read data from an EBS snapshot, the service
provides Base64-encoded SHA256 checksums for each block of data transmitted, which you can
use for validation. When you write data to an EBS snapshot, you must provide a Base64
encoded SHA256 checksum for each block of data transmitted. The service validates the data
received using the checksum provided. For more information, see [Use EBS direct APIs checksums to validate snapshot data](ebsapis-using-checksums.md "ebsapis-using-checksums.md") later in this
guide.

## Encryption

Encryption protects your data by converting it into unreadable code that can be
deciphered only by people who have access to the KMS key used to encrypt it. You can use the
EBS direct APIs to read and write encrypted snapshots, but there are some limitations. For more
information, see [Encryption outcomes for EBS direct APIs](ebsapis-using-encryption.md "ebsapis-using-encryption.md") later in this guide.

## API actions

The EBS direct APIs consists of six actions. There are three read actions and three write
actions. The read actions are:

- **ListSnapshotBlocks** — returns the block
  indexes and block tokens of blocks in the specified snapshot
- **ListChangedBlocks** — returns the block
  indexes and block tokens of blocks that are different between two specified
  snapshots of the same volume and snapshot lineage.
- **GetSnapshotBlock** — returns the data in
  a block for the specified snapshot ID, block index, and block token.

The write actions are:

- **StartSnapshot** — starts a snapshot, either
  as an incremental snapshot of an existing one or as a new snapshot. The started
  snapshot remains in a pending state until it is completed using the CompleteSnapshot
  action.
- **PutSnapshotBlock** — adds data to a started
  snapshot in the form of individual blocks. You must specify a Base64-encoded SHA256
  checksum for the block of data transmitted. The service validates the checksum after
  the transmission is completed. The request fails if the checksum computed by the
  service doesn’t match what you specified.
- **CompleteSnapshot** — completes a started
  snapshot that is in a pending state. The snapshot is then changed to a completed
  state.

## Signature Version 4 signing

Signature Version 4 is the process to add authentication information to AWS requests
sent by HTTP. For security, most requests to AWS must be signed with an access key, which
consists of an access key ID and secret access key. These two keys are commonly referred to
as your security credentials. For information about how to obtain credentials for your
account, see [AWS security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md").

If you intend to manually create HTTP requests, you must learn how to sign them. When
you use the AWS Command Line Interface (AWS CLI) or one of the AWS SDKs to make requests to AWS,
these tools automatically sign the requests for you with the access key that you
specify when you configure the tools. When you use these tools, you don't need to learn how
to sign requests yourself.

For more information, see [Signing AWS API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
in the _IAM User Guide_.
