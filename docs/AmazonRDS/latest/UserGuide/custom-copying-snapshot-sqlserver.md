# Copying an Amazon RDS Custom for SQL Server DB snapshot

With RDS Custom for SQL Server, you can copy automated backups and manual DB snapshots. After copying a
snapshot, the copy you create is a manual snapshot. You can make multiple copies of an
automated backup or manual snapshot but each copy must have a unique identifier.

You can only copy a snapshot within the same AWS account across different AWS Regions
where RDS Custom for SQL Server is available. The following operations are currently not supported:

- Copying DB snapshots within the same AWS Region.
- Copying DB snapshots across AWS accounts.
  RDS Custom for SQL Server supports incremental snapshot copying. For more information, see [Considerations for incremental snapshot copying](USER_CopySnapshot.md#USER_CopySnapshot.Incremental "USER_CopySnapshot.md#USER_CopySnapshot.Incremental").

###### Topics

- [Limitations](#custom-copying-snapshot-sqlserver.Limitations "#custom-copying-snapshot-sqlserver.Limitations")
- [Handling encryption](#custom-copying-snapshot-sqlserver.Encryption "#custom-copying-snapshot-sqlserver.Encryption")
- [Cross-Region copying](#custom-copying-snapshot-sqlserver.XRCopy "#custom-copying-snapshot-sqlserver.XRCopy")
- [Snapshots of DB instances created with Custom Engine Versions (CEV)](#custom-copying-snapshot-sqlserver.CEVSnap "#custom-copying-snapshot-sqlserver.CEVSnap")
- [Grant required permissions to your IAM principal](#custom-copying-snapshot-sqlserver.GrantPermIAM "#custom-copying-snapshot-sqlserver.GrantPermIAM")
- [Copying a DB snapshot](#custom-copying-snapshot-sqlserver.CopyingDBSnapshot "#custom-copying-snapshot-sqlserver.CopyingDBSnapshot")

## Limitations

The following limitations apply to copying a DB snapshot for RDS Custom for SQL Server:

- If you delete a source snapshot before the target snapshot becomes available,
  the snapshot copy might fail. Verify that the target snapshot has a status of
  `AVAILABLE` before you delete the source snapshot.
- You cannot specify an option group name or copy an options group in your DB
  snapshot copy request.
- If you delete any dependent AWS resources of the source DB snapshot before
  or during the copy process, your copy snapshot request could fail
  asynchronously.
  - If you delete the Service Master Key (SMK) backup file for your source
    DB instance stored in the RDS Custom managed S3 bucket in your account, the
    DB snapshot copy succeeds asynchronously. However, SQL Server features
    dependent on SMK such as TDE enabled databases run into issues. For more
    information, see [Troubleshooting PENDING_RECOVERY state for TDE enabled databases in RDS Custom for SQL Server](custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.pending_recovery "custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.pending_recovery").

- Copying DB snapshots within the same AWS Region is currently not
  supported.
- Copying DB snapshots across AWS accounts is currently not supported.

The limitations of copying a DB snapshot for Amazon RDS also apply to RDS Custom for SQL Server. For more
information, see [Limitations](USER_CopySnapshot.md#USER_CopySnapshot.Limitations "USER_CopySnapshot.md#USER_CopySnapshot.Limitations").

## Handling encryption

All RDS Custom for SQL Server DB instances and DB snapshots are encrypted with KMS keys. You can only copy an
encrypted snapshot to an encrypted snapshot, therefore you must specify a KMS key valid
in the destination AWS Region for your DB snapshot copy request.

The source snapshot remains encrypted throughout the copy process. Amazon RDS uses envelope
encryption to protect data during the copy operation with the specified destination
AWS Region KMS key. For more information, see [Envelope encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping")
in the _AWS Key Management Service Developer Guide_.

## Cross-Region copying

You can copy DB snapshots across AWS Regions. However, there are certain constraints
and considerations for cross-Region snapshot copying.

### Authorizing RDS to communicate across AWS Regions for snapshot copying

After a cross-Region DB snapshot copy request is processed successfully, RDS
starts the copy. An authorization request for RDS to access the source snapshot is
created. This authorization request links the source DB snapshot to the target DB
snapshot. This allows RDS to copy only to the specified target snapshot.

RDS verifies the authorization by using the
`rds:CrossRegionCommunication` permission in the service-linked IAM
role. If the copy is authorized, RDS can communicate with the source Region and
complete the copy operation.

RDS doesn’t have access to DB snapshots that weren't authorized previously by
a CopyDBSnapshot request. The authorization is revoked after the copy
completes.

RDS uses the service-linked role to verify the authorization in the source Region.
The copy fails if you delete the service-linked role during the copy process.

For more information, see [Using service-linked
roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in the _AWS Identity and Access Management User Guide_.

### Using AWS Security Token Service credentials

Session tokens from the global AWS Security Token Service (AWS STS) endpoint are valid only in
AWS Regions that are enabled by default (commercial Regions). If you use
credentials from the `assumeRole` API operation in AWS STS, use the
regional endpoint if the source Region is an opt-in Region. Otherwise, the request
fails. Your credentials must be valid in both Regions, which is true for opt-in
Regions only when you use the regional AWS STS endpoint.

To use the global endpoint, make sure that it's enabled for both Regions in
the operations. Set the global endpoint to `Valid` in all AWS Regions
in the AWS STS account settings.

For more information, see [Managing
AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md") in the _AWS Identity and Access Management User
Guide_.

## Snapshots of DB instances created with Custom Engine Versions (CEV)

For a DB snapshot of a DB instance using a [Custom Engine Version
(CEV)](custom-cev-sqlserver.md "custom-cev-sqlserver.md"), RDS associates the CEV with the DB snapshot. To copy a source DB
snapshot associated with a CEV across AWS Regions, RDS copies the CEV along with the
source DB snapshot to the destination region.

If you are copying multiple DB snapshots associated with the same CEV to the same
destination region, the first copy request copies the associated CEV. The copy process
of the following requests finds the initially copied CEV and associates it with the
following DB snapshot copies. The existing CEV copy must be in `AVAILABLE`
state to be associated with the DB snapshot copies.

To copy a DB snapshot associated with a CEV, the requester's IAM policy must
have the permissions to authorize both the DB snapshot copying and the associated CEV
copying. The following permissions are needed in your requester's IAM policy to
allow the associated CEV copying:

- `rds:CopyCustomDBEngineVersion` ‐ Your requester IAM
  principal needs to have the permission to copy the source CEV to the target
  region along with the source DB snapshot. The snapshot copy request fails due to
  authorization errors if your requester IAM principal is not authorized to copy
  the source CEV.
- `ec2:CreateTags` ‐ The underlying EC2 AMI of the source CEV is
  copied to the target region as a part of the CEV copy. RDS Custom attempts to tag
  the AMI with the `AWSRDSCustom` tag before copying the AMI. Make sure
  your requester IAM principal has the permission to create the tag against the
  AMI underlying the source CEV in the source region.

For more information about CEV copying permissions, see [Grant required permissions to your IAM principal](#custom-copying-snapshot-sqlserver.GrantPermIAM "#custom-copying-snapshot-sqlserver.GrantPermIAM").

## Grant required permissions to your IAM principal

Make sure that you have sufficient access to copy a RDS Custom for SQL Server DB snapshot. The IAM
role or user (referred to as the IAM principal) for copying a DB snapshot using the
console or CLI must have either of the following policies for successful DB instance
creation:

- The `AdministratorAccess` policy or,
- The `AmazonRDSFullAccess` policy with the following additional
  permissions:

```
s3:CreateBucket
s3:GetBucketPolicy
s3:PutBucketPolicy
kms:CreateGrant
kms:DescribeKey
ec2:CreateTags
```

RDS Custom uses these permissions during snapshot copying across AWS Regions. These
permissions configure resources in your account that are required for RDS Custom operations.
For more information about the `kms:CreateGrant` permission, see [AWS KMS key management](Overview.Encryption.md "Overview.Encryption.md").

The following sample JSON policy grants the required permissions in addition to
`AmazonRDSFullAccess` policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateS3BucketAndReadWriteBucketPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy"
 ],
 "Resource": "arn:aws:s3:::do-not-delete-rds-custom-*"
 },
 {
 "Sid": "CreateKmsGrant",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateEc2Tags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

Make sure that the listed permissions aren't restricted by service control
policies (SCPs), permission boundaries, or session policies associated with the
IAM principal.

If you use conditions with context keys in the requester's IAM policy, certain
conditions can cause the request to fail. For more information about common pitfalls due
to IAM policy conditions, see [Requesting a cross-Region DB snapshot copy](USER_CopySnapshot.md#USER_CopySnapshot.AcrossRegions.Policy "USER_CopySnapshot.md#USER_CopySnapshot.AcrossRegions.Policy").

## Copying a DB snapshot

Use the following procedures to copy a DB snapshot. For each AWS account, you can
copy up to 20 DB snapshots at a time from one AWS Region to another. If you copy a DB
snapshot to another AWS Region, you create a manual DB snapshot that is retained in
that AWS Region. Copying a DB snapshot out of the source AWS Region incurs Amazon RDS
data transfer charges. For more information about data transfer pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

After the DB snapshot copy has been created in the new AWS Region, the DB snapshot
copy behaves the same as all other DB snapshots in that AWS Region.

You can copy a DB snapshot using the AWS Management Console, AWS CLI, or the Amazon RDS API.

Console
The following procedure copies a RDS Custom for SQL Server DB snapshot by using the
AWS Management Console.

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose
   **Snapshots**.
3. Select the RDS Custom for SQL Server DB snapshot that you want to copy.
4. In the **Actions** dropwdown , choose
   **Copy snapshot**.

![The Copy snapshot page in the Amazon RDS console. The settings are loaded in the page.](images/XRSC-Snapshot-Copy.png) 5. To copy the DB snapshot to a different AWS Region, set
**Destination Region** to the required
value.

###### Note

The destination AWS Region must have the same database
engine version available as the source AWS Region. 6. For **New DB snapshot identifier**, enter a
unique name for the DB snapshot. You can make multiple copies of an
automated backup or manual snapshot but each copy must have a unique
identifier. 7. (Optional) Select **Copy Tags** to copy tags and
values from the snapshot to the copy of the snapshot. 8. For **Encryption**, specify the KMS key
identifier to use to encrypt the DB snapshot copy.

###### Note

RDS Custom for SQL Server encrypts all DB snapshots. You can't create an
unencrypted DB snapshot. 9. Choose **Copy snapshot**.

RDS Custom for SQL Server creates a DB snapshot copy of your DB instance in the
AWS Region of your selection.

AWS CLI
You can copy a RDS Custom for SQL Server DB snapshot by using the AWS CLI command [copy-db-snapshot](../../../cli/latest/reference/rds/copy-db-snapshot.md "../../../cli/latest/reference/rds/copy-db-snapshot.md"). If you are copying the
snapshot to a new AWS Region, run the command in the new AWS Region. The
following options are used to copy a DB snapshot. Not all options are
required for all scenarios.

- `--source-db-snapshot-identifier` ‐ The identifier
  for the source DB snapshot.
  - If the source snapshot is in a different AWS Region than
    the copy, specify a valid DB snapshot ARN. For example,
    `arn:aws:rds:us-west-2:123456789012:snapshot:instance1-snapshot-12345678`.

- `--target-db-snapshot-identifier` ‐ The identifier
  for the new copy of the DB snapshot.
- `--kms-key-id` ‐The KMS key identifier for an
  encrypted DB snapshot. The KMS key identifier is the Amazon
  Resource Name (ARN), key identifier, or key alias for the KMS
  key.
  - If you copy an encrypted snapshot to a different
    AWS Region, then you must specify a KMS key for the
    destination AWS Region. KMS keys are specific to the
    AWS Region that they are created in and you cannot use
    encryption keys from one AWS Region in another
    AWS Region unless a multi-Region key is used. For more
    information on multi-Region KMS keys, see [Using multi-Region keys in AWS KMS](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md").

- `--copy-tags` ‐ Include the tags and values from
  the source snapshot to the copy of the snapshot.

The following options are not supported for copying an RDS Custom for SQL Server DB
snapshot:

- `--copy-option-group`
- `--option-group-name`
- `--pre-signed-url`
- `--target-custom-availability-zone`

The following code example copies an encrypted DB snapshot from the
US West (Oregon) Region to the US East (N. Virginia) Region. Run the command
in the destination (us-east-1) Region.

For Linux, macOS, or Unix:

```
aws rds copy-db-snapshot \
     --region us-east-1 \
    --source-db-snapshot-identifier arn:aws:rds:us-west-2:123456789012:snapshot:instance1-snapshot-12345678 \
    --target-db-snapshot-identifier mydbsnapshotcopy \
    --kms-key-id a1b2c3d4-1234-5678-wxyz-a1b2c3d4d5e6

```

For Windows:

```
aws rds copy-db-snapshot ^
     --region us-east-1 ^
    --source-db-snapshot-identifier arn:aws:rds:us-west-2:123456789012:snapshot:instance1-snapshot-12345678 ^
    --target-db-snapshot-identifier mydbsnapshotcopy ^
    --kms-key-id a1b2c3d4-1234-5678-wxyz-a1b2c3d4d5e6
```

RDS API
You can copy a RDS Custom for SQL Server DB snapshot by using the Amazon RDS API operation
[CopyDBSnapshot](../APIReference/API_CopyDBSnapshot.md "../APIReference/API_CopyDBSnapshot.md"). If you are copying the snapshot to a new
AWS Region, perform the action in the new AWS Region. The following
parameters are used to copy a DB snapshot. Not all parameters are required:

- `SourceDBSnapshotIdentifier` ‐ The identifier for
  the source DB snapshot.
  - If the source snapshot is in a different AWS Region than
    the copy, specify a valid DB snapshot ARN. For example,
    `arn:aws:rds:us-west-2:123456789012:snapshot:instance1-snapshot-12345678`.

- `TargetDBSnapshotIdentifier` ‐ The identifier for
  the new copy of the DB snapshot.
- `KmsKeyId` ‐ The KMS key identifier for an
  encrypted DB snapshot. The KMS key identifier is the Amazon
  Resource Name (ARN), key identifier, or key alias for the KMS
  key.
  - If you copy an encrypted snapshot to a different
    AWS Region, then you must specify a KMS key for the
    destination AWS Region. KMS keys are specific to the
    AWS Region that they are created in and you cannot use
    encryption keys from one AWS Region in another
    AWS Region unless a multi-Region key is used. For more
    information on multi-Region KMS keys, see [Using multi-Region keys in AWS KMS](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md").

- `CopyTags` ‐ Set this parameter to
  `true` to copy tags and values from the source
  snapshot to the copy of the snapshot. The default is
  `false`.

The following options are not supported copying a RDS Custom for SQL Server DB
snapshot:

- `CopyOptionGroup`
- `OptionGroupName`
- `PreSignedUrl`
- `TargetCustomAvailabilityZone`

The following code creates a copy of a snapshot, with the new name
`mydbsnapshotcopy`, in the US East (N. Virginia) Region.

```
https://rds.us-east-1.amazonaws.com/
    ?Action=CopyDBSnapshot
    &KmsKeyId=a1b2c3d4-1234-5678-wxyz-a1b2c3d4d5e6
    &SourceDBSnapshotIdentifier=arn%3Aaws%3Ards%3Aus-west-2%3A123456789012%3Asnapshot%3Ainstance1-snapshot-12345678
    &TargetDBSnapshotIdentifier=mydbsnapshotcopy
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20161117/us-east-1/rds/aws4_request
    &X-Amz-Date=20161117T221704Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=da4f2da66739d2e722c85fcfd225dc27bba7e2b8dbea8d8612434378e52adccf
```
