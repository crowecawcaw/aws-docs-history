# Copying an unencrypted DB cluster snapshot by using the AWS CLI or Amazon RDS API

Use the procedures in the following sections to copy an unencrypted DB cluster snapshot by
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

The following options are used to copy an unencrypted DB cluster
snapshot:

- `--source-db-cluster-snapshot-identifier` – The identifier
  for the DB cluster snapshot to be copied. If you are copying the
  snapshot to another AWS Region, this identifier must be in the ARN format
  for the source AWS Region.
- `--target-db-cluster-snapshot-identifier` – The identifier
  for the new copy of the DB cluster snapshot.
  The following code creates a copy of DB cluster snapshot
  `arn:aws:rds:us-east-1:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20130805`
  named `myclustersnapshotcopy` in the AWS Region in which the command is
  run. When the copy is made, all tags on the original snapshot are copied to the
  snapshot copy.

###### Example

For Linux, macOS, or Unix:

```
aws rds copy-db-cluster-snapshot \
  --source-db-cluster-snapshot-identifier `arn:aws:rds:us-east-1:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20130805` \
  --target-db-cluster-snapshot-identifier `myclustersnapshotcopy` \
  --copy-tags

```

For Windows:

```
aws rds copy-db-cluster-snapshot ^
  --source-db-cluster-snapshot-identifier `arn:aws:rds:us-east-1:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20130805` ^
  --target-db-cluster-snapshot-identifier `myclustersnapshotcopy` ^
  --copy-tags

```

To copy a DB cluster snapshot, use the Amazon RDS API [CopyDBClusterSnapshot](../APIReference/API_CopyDBClusterSnapshot.md "../APIReference/API_CopyDBClusterSnapshot.md") operation. If you are
copying the snapshot to another AWS Region, perform the action in the AWS Region to
which the snapshot will be copied.

The following parameters are used to copy an unencrypted DB cluster
snapshot:

- `SourceDBClusterSnapshotIdentifier` – The identifier for the
  DB cluster snapshot to be copied. If you are copying the snapshot to
  another AWS Region, this identifier must be in the ARN format for the source
  AWS Region.
- `TargetDBClusterSnapshotIdentifier` – The identifier for the
  new copy of the DB cluster snapshot.
  The following code creates a copy of a snapshot
  `arn:aws:rds:us-east-1:123456789012:cluster-snapshot:aurora-cluster1-snapshot-20130805` named
  `myclustersnapshotcopy` in the US West (N. California) Region. When the copy is made, all tags on the original
  snapshot are copied to the snapshot copy.

###### Example

```
https://rds.us-west-1.amazonaws.com/
   ?Action=CopyDBClusterSnapshot
   &CopyTags=`true`
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceDBSnapshotIdentifier=`arn%3Aaws%3Ards%3Aus-east-1%3A123456789012%3Acluster-snapshot%3Aaurora-cluster1-snapshot-20130805`
   &TargetDBSnapshotIdentifier=`myclustersnapshotcopy`
   &Version=2013-09-09
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140429/us-west-1/rds/aws4_request
   &X-Amz-Date=20140429T175351Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=9164337efa99caf850e874a1cb7ef62f3cea29d0b448b9e0e7c53b288ddffed2
```
