# Access points

## Overview

AWS Backup now lets you access Amazon S3 backup data directly through S3 access points, without
initiating a restore. Using a backup access point, you can read S3 backup data immediately
using familiar S3 APIs such as `GetObject`, `HeadObject`,
`ListObjectsV2`, and `ListObjectVersions`.

Backup access points provide on-demand, read-only connections to recovery points. You
create a backup access point for a specific recovery point, and AWS Backup provisions an S3 access
point that routes S3 API calls to your backup data. This enables use cases such as targeted
file recovery, data validation, compliance auditing, and forensic investigation without
waiting for a full restore to complete.

While a backup access point is active for a recovery point, AWS Backup pauses lifecycle
transitions and blocks deletion of that recovery point. This protects your data from being
removed while applications are actively reading it. You must delete all backup access points
associated with a recovery point before the recovery point can be deleted or
lifecycled.

This page explains how to create, manage, and delete backup access points using the AWS Backup
console and AWS CLI.

###### Important

Access points provide read-only access to backup data. Write operations through backup
access points are not supported.

## How backup access points work

When you create a backup access point, AWS Backup performs the following steps:

1. Validates that the recovery point exists and is in a usable state (AVAILABLE, STOPPED,
   or COMPLETED)
2. Creates a backup access point resource in AWS Backup with status CREATING
3. Provisions an S3 access point on your behalf (asynchronously)
4. Pauses lifecycle for the associated recovery point
5. Updates the backup access point status to AVAILABLE

Once the backup access point is AVAILABLE, you call `DescribeBackupAccessPoint`
to retrieve the S3 access point ARN and alias. You then use the S3 access point alias or ARN
with standard S3 APIs to read your backup data.

When you are done, call `DeleteBackupAccessPoint`. AWS Backup deletes the S3 access
point and this resumes recovery point lifecycle transitions (if no other access points
remain).

### Access point statuses

| Status         | Description                                                                                                                      |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| CREATING       | Access point creation is in progress. S3 access point is being<br>provisioned.                                                   |
| AVAILABLE      | Access point is ready. Use `DescribeBackupAccessPoint` to get the S3<br>ARN and alias.                                           |
| DELETING       | Deletion is in progress.                                                                                                         |
| FAILED         | Creation or deletion failed. Use `DescribeBackupAccessPoint` to get<br>the error details.                                        |
| EXPIRED        | The backup access point is no longer usable.                                                                                     |
| DISASSOCIATING | Access is being revoked. The logically air-gapped vault is being unshared or<br>the restore access backup vault is being deleted |
| DISASSOCIATED  | Access has been revoked. The backup access point is no longer usable.                                                            |

### Continuous recovery points

For continuous (PITR) recovery points, you can specify an `AccessPointInTime`
timestamp when creating the access point. This determines the point-in-time view of your
backup data. The timestamp must be within the continuous backup retention window
_at the time of access point creation. As long as the access point exists, the
data for that point in time is retained and accessible, even if the timestamp later falls
outside the retention window._

## Prerequisites

Before creating/managing a backup access point, ensure:

- Your IAM role has the required permissions. You can use the managed policy [AWSBackupAccessPointOperatorAccess](../../../aws-managed-policy/latest/reference/AWSBackupAccessPointOperatorAccess.md "../../../aws-managed-policy/latest/reference/AWSBackupAccessPointOperatorAccess.md"), or ensure the following permissions are
  applied:

  - `backup:CreateBackupAccessPoint`
  - `backup:DescribeBackupAccessPoint`
  - `backup:DeleteBackupAccessPoint`
  - `backup:ListBackupAccessPoints`
  - `backup:ListBackupAccessPointsByRecoveryPoint`
  - `s3:GetAccessPoint` (required during create, describe, and
    delete)
  - `s3:CreateAccessPoint` (required during create)
  - `s3:DeleteAccessPoint` (required during delete)
  - `s3:PutAccessPointPolicy` (required only if an access point policy is
    included in the request)

## Creating a backup access point

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup/ "https://console.aws.amazon.com/backup/").
2. In the navigation pane, choose **Protected resources** or
   navigate to a recovery point through **Backup vaults**.
3. Select the S3 recovery point you want to access.
4. Choose **Create access point**.
5. For **Access point name**, enter a unique name. This name is
   shared with the S3 access point namespace, so it must not conflict with existing S3
   access points in the same Region and account. _Note: For naming rules,
   see_
   [_Naming rules for Amazon S3 access
   points_](../../../AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.md#access-points-names "../../../AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.md#access-points-names")_._
6. (Optional) For continuous recovery points, specify the **Access point in
   time** to set the point-in-time view.
7. (Optional) Add access point policy.
8. (Optional) Add tags.
9. Choose **Create access point**.
10. The backup access point status shows CREATING. When status changes to AVAILABLE,
    choose the backup access point to view the S3 access point ARN and alias.

AWS CLI

```
aws backup create-backup-access-point \
  --recovery-point-arn "arn:aws:backup:us-east-1:123456789012:recovery-point:rp-1234567890abcdef0" \
  --name "my-access-point" \
  --access-point-metadata '{"AccessPointInTime": "2026-07-01T12:00:00Z"}'
```

Response:

```
{
  "AccessPointArn": "arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point",
  "Status": "CREATING"
}
```

After creation, describe the access point to get the S3 ARN and alias:

```
aws backup describe-backup-access-point \
  --access-point-arn "arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point"
```

Response (when AVAILABLE):

```
{
  "AccessPointArn": "arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point",
  "AccessPointMetadata": {
    "S3AccessPointAlias": "my-access-point-abc123-ext-s3alias",
    "S3AccessPointArn": "arn:aws:s3:us-east-1:123456789012:accesspoint/my-access-point"
  },
  "BackupVaultName": "MyVault",
  "CreationTime": "2026-07-28T12:00:25.938000-07:00",
  "Name": "my-access-point",
  "RecoveryPointArn": "arn:aws:backup:us-east-1:123456789012:recovery-point:rp-1234567890abcdef0",
  "ResourceArn": "arn:aws:s3:::my-bucket",
  "ResourceType": "S3",
  "Status": "AVAILABLE"
}
```

## Accessing backup data through the access point

Once the access point is in AVAILABLE status, use the S3 access point alias or ARN with S3
APIs to read backup data.

### Using the alias

```
# List objects in the backup
aws s3api list-objects-v2 \
  --bucket "my-access-point-abc123-ext-s3alias"

# Get a specific object
aws s3api get-object \
  --bucket "my-access-point-abc123-ext-s3alias" \
  --key "path/to/my-file.txt" \
  output-file.txt

# Head an object (metadata only)
aws s3api head-object \
  --bucket "my-access-point-abc123-ext-s3alias" \
  --key "path/to/my-file.txt"
```

### Using the S3 access point ARN

```
aws s3api list-objects-v2 \
  --bucket "arn:aws:s3:us-east-1:123456789012:accesspoint/my-access-point"
```

## Managing access points

### Listing access points

List all backup access points in your account:

```
aws backup list-backup-access-points
```

List backup access points for a specific recovery point:

###### Note

If you are the recovery point owner and have shared the recovery point with other
accounts, the response includes access points created by those accounts.

```
aws backup list-backup-access-points-by-recovery-point \
  --recovery-point-arn "arn:aws:backup:us-east-1:123456789012:recovery-point:rp-1234567890abcdef0"
```

List backup access points for a specific resource:

```
aws backup list-backup-access-points-by-resource \
  --resource-arn "arn:aws:s3:::my-bucket"
```

### Deleting an access point

```
aws backup delete-backup-access-point \
  --access-point-arn "arn:aws:backup:us-east-1:123456789012:accesspoint/my-access-point"
```

When you delete a backup access point:

- The S3 access point is deleted
- Recovery point lifecycle resumes (if no other access points remain for that recovery
  point)
- The backup access point resource is removed from AWS Backup

###### Important

Always delete backup access points using the `DeleteBackupAccessPoint` API
or the AWS Backup console. Do not delete the underlying S3 access point directly through S3
APIs. Deleting the S3 access point directly leaves the backup access point in EXPIRED
status and lifecycle protection remains in place until you delete the orphaned backup
access point.

## Access point policies

Each access point can have its own resource-based access point policy. Access point
policies control how objects in the backup data source can be accessed through the access
point by resource, user, or conditions.

### How access point policies work

When you create a backup access point, the S3 access point is created without an access
point policy by default. Without a policy, access to backup data through the access point is
governed by the caller's IAM permissions.

You can optionally specify a policy during creation or add one afterward to:

- Grant read access to additional IAM principals in your account
- Restrict access by source IP address or VPC endpoint
- Add conditions such as requiring MFA or specific tags

Restrictions that you include in an access point policy apply only to requests made
through that access point. An access point policy grants permissions only if the underlying
data source also allows the same access.

### Editing an access point policy

You can edit an access point policy through the AWS Backup console or the S3
`PutAccessPointPolicy` API.

Console

1. Open the AWS Backup console.
2. Navigate to **Access points** and select your access
   point.
3. Choose the **Access point policy** tab.
4. Choose **Edit**.
5. Modify the JSON policy.
6. Choose **Save changes**.

When you edit a policy, AWS Identity and Access Management Access Analyzer runs
policy checks to validate your policy against IAM policy grammar and best practices.
Resolve security warnings, errors, and suggestions before saving.

AWS CLI

```
aws s3control put-access-point-policy \
  --account-id 123456789012 \
  --name "my-access-point" \
  --policy '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam::123456789012:role/DataAnalyst"
        },
        "Action": ["s3:GetObject", "s3:ListBucket"],
        "Resource": [
          "arn:aws:s3:us-east-1:123456789012:accesspoint/my-access-point",
          "arn:aws:s3:us-east-1:123456789012:accesspoint/my-access-point/object/*"
        ]
      }
    ]
  }'
```

### Block Public Access

Amazon S3 Block Public Access settings apply to backup access points. If Block Public Access
is turned on for your account, public access through backup access points is blocked
regardless of the access point policy. To check your settings, review your account-level
Block Public Access configuration.

### Learn more

- [Configuring IAM policies
  for using access points](../../../AmazonS3/latest/userguide/access-points-policies.md "../../../AmazonS3/latest/userguide/access-points-policies.md")
- [Amazon
  S3 Access Points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md")
- [IAM Access Analyzer
  policy validation](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md")
- [Using Amazon S3
  Block Public Access](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md")

## Supported S3 operations

The following table shows which S3 API operations are compatible with backup access
points. Backup access points are read-only, so all write, delete, and multipart upload
operations are not supported.

| S3 operation              | Backup access point |
| ------------------------- | ------------------- |
| `GetObject`               | Supported           |
| `HeadObject`              | Supported           |
| `GetObjectAttributes`     | Supported           |
| `GetObjectTagging`        | Supported           |
| `GetBucketLocation`       | Supported           |
| `ListObjectsV2`           | Supported           |
| `ListObjects`             | Supported           |
| `ListObjectVersions`      | Supported           |
| `PutObject`               | Not supported       |
| `DeleteObject`            | Not supported       |
| `DeleteObjects`           | Not supported       |
| `CopyObject`              | Not supported       |
| `CreateMultipartUpload`   | Not supported       |
| `UploadPart`              | Not supported       |
| `CompleteMultipartUpload` | Not supported       |
| `AbortMultipartUpload`    | Not supported       |
| `PutObjectTagging`        | Not supported       |
| `DeleteObjectTagging`     | Not supported       |
| `PutObjectAcl`            | Not supported       |
| `GetObjectAcl`            | Not supported       |
| `GetObjectLegalHold`      | Not supported       |
| `GetObjectRetention`      | Not supported       |

## Recovery point lifecycle protection

While one or more active access points exist for a recovery point:

- **Scheduled lifecycle transitions are paused.** The
  recovery point will not be automatically deleted by lifecycle rules.
- **Manual deletion is blocked.** Calls to
  `DeleteRecoveryPoint` return an error until all access points are
  deleted.

You can still update the recovery point lifecycle (for example, changing the
delete-after-days value), but the deletion will not be enforced until all backup access points
for the recovery point are removed.

Once all access points for a recovery point are deleted, lifecycle processing resumes
automatically.

###### Note

Each account can have up to 5 backup access points per recovery point, regardless of
their status. To create a new backup access point when the limit is reached, delete an
existing one (including any in FAILED or EXPIRED status).

## Access points for recovery points in logically air-gapped vaults

You can create backup access points for recovery points stored in logically air-gapped
vaults. Access points can be created by the vault-owning account directly, or from another
account that has been granted access through AWS Resource Access Manager (RAM) sharing or a restore access
backup vault (via Multi-Party Approval).

**Same-account access**

The account that owns the logically air-gapped vault can create access points for recovery
points in that vault, the same way as for standard backup vaults.

**RAM sharing**

When a logically air-gapped vault is shared with an account via RAM, that account can
create access points for recovery points in the shared vault. The RAM permission
`AWSRAMPermissionBackupVaultReadOnly` includes
`backup:CreateBackupAccessPoint`. Vault owners can restrict this by adding a
vault access policy that denies `backup:CreateBackupAccessPoint`.

For more information, see [Share a logically
air-gapped vault](logicallyairgappedvault.md#lag-share "logicallyairgappedvault.md#lag-share").

**Restore access backup vaults (Multi-Party Approval)**

An account that has a restore access backup vault for a logically air-gapped vault can
create backup access points for recovery points accessible through that vault.

For more information, see [Multi-party approval for logically
air-gapped vaults](multipartyapproval.md "multipartyapproval.md").

**When access is revoked**

If access is removed (logically air-gapped vault unshared via RAM, or restore access
backup vault deleted or revoked):

- All backup access points created by the formerly authorized account transition to
  DISASSOCIATED status
- Lifecycle protection for associated recovery points is removed if the recovery point
  has no more associated access points.
- S3 API calls through existing S3 access points fail

## Monitoring and notifications

AWS Backup emits CloudTrail events, EventBridge events, and Amazon SNS notifications for backup access point
status changes (creation, deletion, failure etc.). For details on event formats and how to
subscribe, see [Monitoring AWS Backup](monitoring.md "monitoring.md").

## Supported features and limitations

### Supported features

- **Recovery point types**: Both snapshot and continuous
  (PITR) recovery points
- **Vault types**: Standard backup vaults and logically
  air-gapped vaults
- **Cross-account**: Access points can be created for
  recovery points shared through RAM

### Limitations

- **Read-only**: Only read operations (GET, HEAD, LIST)
  are supported. Write operations are not available.
- **S3 only**: Access points are supported for Amazon S3
  recovery points only.
- **Access point limit**: Up to 5 access points per
  recovery point in an account.
- **Name uniqueness**: Access point names share the S3
  access point namespace within a Region and account. Names cannot conflict with existing
  S3 access points.
- **No scheduled deletion**: Access points do not have a
  delete-after-days setting. You must delete them manually.
- **External deletion**: If the S3 access point is deleted
  directly through S3 APIs, the backup access point moves to EXPIRED status and becomes
  unusable.
- **Access**: The access point creator's account must
  have access to the recovery point (either owns it, has RAM share access or has a restore
  access backup vault for the logically air-gapped vault via Multi-Party Approval).
- **Access point name**: After you delete a backup access
  point, wait for sometime before you attempt to create a new backup access point with the
  same name in the same account and Region. Attempting to reuse the name before it becomes
  available returns a `ConflictException`.
- **S3 object key restrictions**: Objects named
  `.` or `..` are not accessible through backup access points. Object
  keys that start with `./` or `../`, contain `/./` or
  `/../`, contain consecutive slashes (`//`), or end with
  `/.`, `/..`, or `/` are also inaccessible. Attempting to
  access any object with these keys through a backup access point will return an
  `InvalidKey` error.

## Troubleshooting

**Common issues**

`InvalidParameterValueException` when creating

- Verify the recovery point is in `AVAILABLE`, `STOPPED`, or
  `COMPLETED` state.
- For continuous recovery points, ensure `AccessPointInTime` is within the
  retention window.
- Verify the access point name follows S3 naming rules (lowercase, no underscores, 3-50
  characters).

Cannot delete recovery point

- Check if active access points exist for the recovery point using
  `list-backup-access-points-by-recovery-point`.
- Delete all access points before attempting to delete the recovery point.

Access point in `EXPIRED` status

- The backup access point is no longer usable. Delete the expired backup access point
  using `DeleteBackupAccessPoint`, then create a new one if needed.

S3 API calls return `409 InvalidBucketState`

- The backup access point is not yet in `AVAILABLE` status. Wait for creation
  to complete, then retry.

`LimitExceededException`

- You have reached the maximum of 5 access points for this recovery point. Delete an
  existing access point (including any in `FAILED` or `EXPIRED` status)
  before creating a new one.

`ConflictException` when creating

- You are attempting to create a backup access point with a name that was recently
  deleted. Wait for the name to become available, or choose a different name.
