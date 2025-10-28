# Copying an encrypted DB cluster snapshot by using the AWS CLI or Amazon RDS API

Use the procedures in the following sections to copy an encrypted DB cluster snapshot by
using the AWS Management Console, AWS CLI, or Amazon RDS API.

To cancel a copy operation once it is in progress, delete the target DB cluster
snapshot identified by
`--target-db-cluster-snapshot-identifier` or
`TargetDBClusterSnapshotIdentifier` while that DB cluster snapshot is
in **copying** status.

To copy a DB cluster snapshot using the AWS Management Console, see [Copying a DB cluster snapshot with the AWS Management Console](USER_CopyDBClusterSnapshot.md "USER_CopyDBClusterSnapshot.md").

To copy a DB cluster snapshot, use the AWS CLI [copy-db-cluster-snapshot](../../../cli/latest/reference/rds/copy-db-cluster-snapshot.md "../../../cli/latest/reference/rds/copy-db-cluster-snapshot.md") command. If you are
copying the snapshot to another AWS Region, run the command in the AWS Region to which
the snapshot will be copied.

The following options are used to copy an encrypted DB cluster
snapshot:

- `--source-db-cluster-snapshot-identifier` – The identifier for the
  encrypted DB cluster snapshot to be copied. If you are copying the
  snapshot to another AWS Region, this identifier must be in the ARN
  format for the source AWS Region.
- `--target-db-cluster-snapshot-identifier`
  – The identifier for the new copy of the encrypted DB cluster
  snapshot.
- `--kms-key-id` – The KMS key identifier
  for the key to use to encrypt the copy of the DB cluster
  snapshot.

You can optionally use this option if the DB cluster snapshot is encrypted, you copy the
snapshot in the same AWS Region, and you want to specify a new KMS key
to encrypt the copy. Otherwise, the copy of the DB cluster snapshot is
encrypted with the same KMS key as the source DB cluster snapshot.

You must use this option if the DB cluster snapshot is encrypted and you are copying the
snapshot to another AWS Region. In that case, you must specify a KMS key
for the destination AWS Region.
The following code example copies the encrypted DB cluster snapshot from the US West (Oregon) Region to the US East (N. Virginia)
Region. The command is called in the US East (N. Virginia) Region.

###### Example

For Linux, macOS, or Unix:

```
aws rds copy-db-cluster-snapshot \
  --source-db-cluster-snapshot-identifier `arn:aws:rds:us-west-2:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20161115` \
  --target-db-cluster-snapshot-identifier `myclustersnapshotcopy` \
  --kms-key-id `my-us-east-1-key`
```

For Windows:

```
aws rds copy-db-cluster-snapshot ^
  --source-db-cluster-snapshot-identifier `arn:aws:rds:us-west-2:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20161115` ^
  --target-db-cluster-snapshot-identifier `myclustersnapshotcopy` ^
  --kms-key-id `my-us-east-1-key`
```

The `--source-region` parameter is required when you're copying an encrypted DB
cluster snapshot between the AWS GovCloud (US-East) and AWS GovCloud (US-West)
Regions. For `--source-region`, specify the AWS Region of the
source DB instance. The AWS Region specified in
`source-db-cluster-snapshot-identifier` must match the
AWS Region specified for `--source-region`.

If `--source-region` isn't specified, specify a
`--pre-signed-url` value. A _presigned
URL_ is a URL that contains a Signature Version 4 signed request
for the `copy-db-cluster-snapshot` command that's called in the
source AWS Region. To learn more about the `pre-signed-url` option,
see [copy-db-cluster-snapshot](../../../cli/latest/reference/rds/copy-db-cluster-snapshot.md "../../../cli/latest/reference/rds/copy-db-cluster-snapshot.md") in the _AWS CLI Command Reference_.

To copy a DB cluster snapshot, use the Amazon RDS API [CopyDBClusterSnapshot](../APIReference/API_CopyDBClusterSnapshot.md "../APIReference/API_CopyDBClusterSnapshot.md") operation. If you are
copying the snapshot to another AWS Region, perform the action in the AWS Region to
which the snapshot will be copied.

The following parameters are used to copy an encrypted DB cluster snapshot:

- `SourceDBClusterSnapshotIdentifier` – The
  identifier for the encrypted DB cluster snapshot to be copied. If you
  are copying the snapshot to another AWS Region, this identifier must be in
  the ARN format for the source AWS Region.
- `TargetDBClusterSnapshotIdentifier` – The
  identifier for the new copy of the encrypted DB cluster snapshot.
- `KmsKeyId` – The KMS key identifier for
  the key to use to encrypt the copy of the DB cluster snapshot.

You can optionally use this parameter if the DB cluster snapshot is encrypted, you copy
the snapshot in the same AWS Region, and you specify a new KMS key to
use to encrypt the copy. Otherwise, the copy of the DB cluster snapshot
is encrypted with the same KMS key as the source DB cluster snapshot.

You must use this parameter if the DB cluster snapshot is encrypted and you are copying
the snapshot to another AWS Region. In that case, you must specify a KMS key
for the destination AWS Region.

- `PreSignedUrl` – If you are copying the
  snapshot to another AWS Region, you must specify the
  `PreSignedUrl` parameter. The `PreSignedUrl`
  value must be a URL that contains a Signature Version 4 signed request
  for the `CopyDBClusterSnapshot` action to be called in the
  source AWS Region where the DB cluster snapshot is copied from. To learn
  more about using a presigned URL, see [CopyDBClusterSnapshot](../APIReference/API_CopyDBClusterSnapshot.md "../APIReference/API_CopyDBClusterSnapshot.md").
  The following code example copies the encrypted DB cluster snapshot from the US West (Oregon) Region to the US East (N. Virginia)
  Region. The action is called in the US East (N. Virginia) Region.

###### Example

```
https://rds.us-east-1.amazonaws.com/
    ?Action=CopyDBClusterSnapshot
    &KmsKeyId=my-us-east-1-key
    &PreSignedUrl=https%253A%252F%252Frds.us-west-2.amazonaws.com%252F
         %253FAction%253DCopyDBClusterSnapshot
         %2526DestinationRegion%253Dus-east-1
         %2526KmsKeyId%253Dmy-us-east-1-key
         %2526SourceDBClusterSnapshotIdentifier%253Darn%25253Aaws%25253Ards%25253Aus-west-2%25253A123456789012%25253Acluster-snapshot%25253Aaurora-cluster1-snapshot-20161115
         %2526SignatureMethod%253DHmacSHA256
         %2526SignatureVersion%253D4
         %2526Version%253D2014-10-31
         %2526X-Amz-Algorithm%253DAWS4-HMAC-SHA256
         %2526X-Amz-Credential%253DAKIADQKE4SARGYLE%252F20161117%252Fus-west-2%252Frds%252Faws4_request
         %2526X-Amz-Date%253D20161117T215409Z
         %2526X-Amz-Expires%253D3600
         %2526X-Amz-SignedHeaders%253Dcontent-type%253Bhost%253Buser-agent%253Bx-amz-content-sha256%253Bx-amz-date
         %2526X-Amz-Signature%253D255a0f17b4e717d3b67fad163c3ec26573b882c03a65523522cf890a67fca613
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &SourceDBClusterSnapshotIdentifier=arn%3Aaws%3Ards%3Aus-west-2%3A123456789012%3Acluster-snapshot%3Aaurora-cluster1-snapshot-20161115
    &TargetDBClusterSnapshotIdentifier=myclustersnapshotcopy
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20161117/us-east-1/rds/aws4_request
    &X-Amz-Date=20161117T221704Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=da4f2da66739d2e722c85fcfd225dc27bba7e2b8dbea8d8612434378e52adccf

```

The `PreSignedUrl` parameter is required when you are copying an encrypted DB
cluster snapshot between the AWS GovCloud (US-East) and AWS GovCloud (US-West)
Regions. The `PreSignedUrl` value must be a URL that contains a
Signature Version 4 signed request for the `CopyDBClusterSnapshot`
operation to be called in the source AWS Region where the DB cluster snapshot
is copied from. To learn more about using a presigned URL, see [CopyDBClusterSnapshot](../APIReference/API_CopyDBClusterSnapshot.md "../APIReference/API_CopyDBClusterSnapshot.md") in the _Amazon RDS API Reference_.

To automatically rather than manually generate a presigned URL, use the AWS CLI [copy-db-cluster-snapshot](../../../cli/latest/reference/rds/copy-db-cluster-snapshot.md "../../../cli/latest/reference/rds/copy-db-cluster-snapshot.md") command with the
`--source-region` option instead.
