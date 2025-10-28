# Copying a DB cluster snapshot across accounts

You can enable other AWS accounts to copy DB cluster snapshots that you specify by using
the Amazon RDS API `ModifyDBClusterSnapshotAttribute` and
`CopyDBClusterSnapshot` actions. You can only
copy DB cluster snapshots across accounts in the same AWS Region. The cross-account copying
process works as follows, where Account A is making the snapshot available to copy, and
Account B is copying it.

1. Using Account A, call `ModifyDBClusterSnapshotAttribute`,
   specifying `restore` for the
   `AttributeName` parameter, and the ID for Account B for the
   `ValuesToAdd` parameter.
2. (If the snapshot is encrypted) Using Account A, update the key policy for the KMS key,
   first adding the ARN of Account B as a `Principal`, and then allow
   the `kms:CreateGrant` action.
3. (If the snapshot is encrypted) Using Account B, choose or create a user and
   attach an IAM policy to that user that allows it to copy an encrypted DB cluster snapshot
   using your KMS key.
4. Using Account B, call `CopyDBClusterSnapshot` and use the
   `SourceDBClusterSnapshotIdentifier` parameter to specify the ARN
   of the DB cluster snapshot to be copied, which must include the ID for Account
   A.
   To list all of the AWS accounts permitted to restore a DB cluster snapshot, use the [DescribeDBSnapshotAttributes](../APIReference/API_DescribeDBSnapshotAttributes.md "../APIReference/API_DescribeDBSnapshotAttributes.md") or [DescribeDBClusterSnapshotAttributes](../APIReference/API_DescribeDBClusterSnapshotAttributes.md "../APIReference/API_DescribeDBClusterSnapshotAttributes.md") API operation.

To remove sharing permission for an AWS account, use the
`ModifyDBSnapshotAttribute` or
`ModifyDBClusterSnapshotAttribute` action with `AttributeName`
set to `restore` and the ID of the account to remove in the
`ValuesToRemove` parameter.

Use the following procedure to copy an unencrypted DB cluster snapshot to another account in the same AWS Region.

1. In the source account for the DB cluster snapshot, call
   `ModifyDBClusterSnapshotAttribute`,
   specifying `restore` for the
   `AttributeName` parameter, and the ID for the target
   account for the `ValuesToAdd` parameter.

Running the following example using the account `987654321` permits two AWS
account identifiers, `123451234512` and
`123456789012`, to restore the DB cluster snapshot named
`manual-snapshot1`.

```
https://rds.us-west-2.amazonaws.com/
	?Action=ModifyDBClusterSnapshotAttribute
	&AttributeName=restore
	&DBClusterSnapshotIdentifier=manual-snapshot1
	&SignatureMethod=HmacSHA256&SignatureVersion=4
	&ValuesToAdd.member.1=123451234512
	&ValuesToAdd.member.2=123456789012
	&Version=2014-10-31
	&X-Amz-Algorithm=AWS4-HMAC-SHA256
	&X-Amz-Credential=AKIADQKE4SARGYLE/20150922/us-west-2/rds/aws4_request
	&X-Amz-Date=20150922T220515Z
	&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
	&X-Amz-Signature=ef38f1ce3dab4e1dbf113d8d2a265c67d17ece1999ffd36be85714ed36dddbb3
```

2. In the target account, call `CopyDBClusterSnapshot` and use
   the `SourceDBClusterSnapshotIdentifier` parameter to specify the
   ARN of the DB cluster snapshot to be copied, which must include the ID for
   the source account.

Running the following example using the account `123451234512` copies the DB
cluster snapshot `aurora-cluster1-snapshot-20130805` from account
`987654321` and creates a DB cluster snapshot named
`dbclustersnapshot1`.

```
https://rds.us-west-2.amazonaws.com/
   ?Action=CopyDBClusterSnapshot
   &CopyTags=true
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceDBClusterSnapshotIdentifier=arn:aws:rds:us-west-2:987654321:cluster-snapshot:aurora-cluster1-snapshot-20130805
   &TargetDBClusterSnapshotIdentifier=dbclustersnapshot1
   &Version=2013-09-09
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20150922/us-west-2/rds/aws4_request
   &X-Amz-Date=20140429T175351Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=9164337efa99caf850e874a1cb7ef62f3cea29d0b448b9e0e7c53b288ddffed2
```

Use the following procedure to copy an encrypted DB cluster snapshot to another
account in the same AWS Region.

1. In the source account for the DB cluster snapshot, call
   `ModifyDBClusterSnapshotAttribute`,
   specifying `restore` for the
   `AttributeName` parameter, and the ID for the target
   account for the `ValuesToAdd` parameter.

Running the following example using the account `987654321`
permits two AWS account identifiers, `123451234512` and
`123456789012`, to restore the DB cluster snapshot named
`manual-snapshot1`.

```
https://rds.us-west-2.amazonaws.com/
	?Action=ModifyDBClusterSnapshotAttribute
	&AttributeName=restore
	&DBClusterSnapshotIdentifier=manual-snapshot1
	&SignatureMethod=HmacSHA256&SignatureVersion=4
	&ValuesToAdd.member.1=123451234512
	&ValuesToAdd.member.2=123456789012
	&Version=2014-10-31
	&X-Amz-Algorithm=AWS4-HMAC-SHA256
	&X-Amz-Credential=AKIADQKE4SARGYLE/20150922/us-west-2/rds/aws4_request
	&X-Amz-Date=20150922T220515Z
	&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
	&X-Amz-Signature=ef38f1ce3dab4e1dbf113d8d2a265c67d17ece1999ffd36be85714ed36dddbb3
```

2. In the source account for the DB cluster snapshot, create a custom KMS key in the same AWS Region as the encrypted DB
   cluster snapshot. While creating the customer managed key, you give access to it for the target AWS account. For more
   information, see [Create a customer managed key and give access to it](share-encrypted-snapshot.md#share-encrypted-snapshot.cmk "share-encrypted-snapshot.md#share-encrypted-snapshot.cmk").
3. Copy and share the snapshot to the target AWS account. For more information, see [Copy and share the snapshot from the source account](share-encrypted-snapshot.md#share-encrypted-snapshot.share "share-encrypted-snapshot.md#share-encrypted-snapshot.share").
4. In the target account, call `CopyDBClusterSnapshot` and use the
   `SourceDBClusterSnapshotIdentifier` parameter to specify the
   ARN of the DB cluster snapshot to be copied, which must include the ID for
   the source account.

Running the following example using the account `123451234512` copies the DB
cluster snapshot `aurora-cluster1-snapshot-20130805` from account
`987654321` and creates a DB cluster snapshot named
`dbclustersnapshot1`.

```
https://rds.us-west-2.amazonaws.com/
   ?Action=CopyDBClusterSnapshot
   &CopyTags=true
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceDBClusterSnapshotIdentifier=arn:aws:rds:us-west-2:987654321:cluster-snapshot:aurora-cluster1-snapshot-20130805
   &TargetDBClusterSnapshotIdentifier=dbclustersnapshot1
   &Version=2013-09-09
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20150922/us-west-2/rds/aws4_request
   &X-Amz-Date=20140429T175351Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=9164337efa99caf850e874a1cb7ef62f3cea29d0b448b9e0e7c53b288ddffed2
```
