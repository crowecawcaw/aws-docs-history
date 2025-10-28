# Backup search

## Overview

With AWS Backup, you can create backups, also known as recovery points, of AWS resources. You
can search for backups of certain resource types such as Amazon S3 and Amazon EBS, as well as items
and files within those backups using the AWS Backup console or the command line.

AWS Backup offers the ability for you to search the metadata of your backups of supported
resource types at a granular level for files or objects that match the properties you define
in your search, such as size, creation date, and resource type. You can dive even deeper by
defining the properties of the items you want to locate.

First, create a backup index you want to be able to include in a future search. Backup
index creation can be automated through a backup plan or you can manually create one for any
existing recovery point. When you’re ready to search, set the backup and item properties you
want to see in the search results. Optionally, you can restore the backup or item you sought
in the search.

This document outlines the steps to create a backup index, search indexed backups,
restore from your search results, and troubleshoot any issues with the index and search
functions in AWS Backup.

## Use cases for backup indexes and search

You may be an administrator who wants to recover a specific file or object. Instead of
manually identifying or guessing which backups contain the data, you can search the metadata
of your recovery points and restore the exact backup, files, or objects you need.

Restoring a full backup just to find the specific item that might be in it can take
hours or days. Instead, with a backup search, you can find and restore just the specific file
or object you require.

Backup searches are useful for backup administrators, backup operators, data owners, and
other IT professionals who interact with data backup, restore, and compliance.

## Access

Before you create an index and a search, your account must have required permissions for
the operations.

**Index permissions**

For index operations, AWS Backup authenticates based on the IAM role, not user
credentials (for IAM user and IAM role
specifics, see [Authentication](authentication.md "authentication.md")).

The following permissions are required to create an index of an EBS backup.
These permissions are contained in the managed policy
[AWSBackupServiceRolePolicyForIndexing](security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForIndexing "security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForIndexing"):

- `ec2:DescribeSnapshots`
- `ebs:ListSnapshotBlocks`
- `ebs:GetSnapshotBlock`
- `kms:Decrypt`

No index permissions are required to create an S3 index.

**Search permissions**

The following permissions are required to create a search. These permissions
are contained in the managed policy [AWSBackupSearchOperatorAccess](security-iam-awsmanpol.md#AWSBackupSearchOperatorAccess "security-iam-awsmanpol.md#AWSBackupSearchOperatorAccess"):

- `backup:ListIndexedRecoveryPointsForSearch`
- `backup:SearchRecoveryPoint`

If you choose to encrypt the search results with a customer managed AWS KMS key, ensure
the following permissions are in the key:

- `kms:GenerateDataKey`
- `kms:Decrypt`

## Process Flow

A backup search involves three steps, plus an optional fourth restore step for when you
want to restore the items returned in your search.

**Index your backups:** Enable indexing in your backup plan(s) or
manually create a backup index through the console or CLI for each existing backup (recovery
point) you want to be eligible for searches.

**Search backup metadata for a recovery point, file or, object:**
Specify the properties of the backups and items you want to find in your search, such as
your searching your S3 buckets created between April 2 and 6. with tags of
`Administration` and for objects greater than 100 MB with the key name
containing `Admin`.

**Review search results:** If you find the recovery point or item you
were seeking, you have the option to restore it. If you haven’t found the recovery point or
item, you can refine the backup properties and item properties, then initiate a new
search.

**Restore specific items _(optional)_:** Specify
file paths or items to restore, as well as the restore conditions.

## Backup indexes

To be searchable, a backup (recovery point) must first have a corresponding index.

Backup index creation can be enabled in a backup plan so that each future backup will
also have an associated backup index. You can also create an index as you create an
on-demand backup.

Alternatively, you can retroactively create an index for an existing recovery point,
either from the Vault recovery point detail screen in the AWS Backup console or through
AWS CLI.

Recovery points of supported resource types can have a backup index if they are stored
in a standard backup vault (recovery points in a logical air-gapped vault do not currently support
backup indexes).

**S3 backup indexes**

An S3 backup can be periodic, where it is scheduled at a fixed interval according to
your backup plan. Each time a periodic backup is created, a backup index is created for it.
An S3 backup can also be continuous, where each change in the backup is logged. Since there
can be numerous changes daily, only one backup index is created daily for a continuous
backup.

The first backup index that is created for a continuous S3 recovery point is full;
subsequent indexes for the same recovery point may be incremental.

**EBS backup indexes**

Each backup index created for an EBS recovery point is full (not incremental).

AWS Backup attempts to automatically repair snapshot issues during the creation
of a backup index. If a file system was in a dirty state when the recovery point was
created, AWS Backup will automatically attempt to recovery the file system. If this recovery
fails, the index creation job will also fail.

The nature of the snapshot determines if it can be indexed:

**Can** be indexed:

- File systems: ext2, ext3, ext4, vfat, xfs, and ntfs

**Cannot** be indexed:

- Snapshots in archive tier (cold storage)
- RAID and other multi disk storage options
- Symbolic links
- Hard links

**Backup index creation steps**

Console

###### Add backup index creation to your backup plan.

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Select **Backup plans** under **My account**
   in the left navigation bar.
3. Select the link in the **Backup plans** pane with the name of
   the plan where you want to add index creation.
4. In the second pane **Backup rules**, select **Add
   backup rule**.
5. Scroll down to the pane **Backup indexes**. Check the box
   next to the resource type(s) for which you want to create an index.

With each new backup this plan creates, a corresponding index for that
recovery point will also be concurrently created.

###### Create an index for an existing recovery point

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Select **Vault** in the left navigation bar.
3. Select the link of under the **Vault** name column in which
   the backup where you want to make a backup index is stored.
4. Place a checkmark next to the recovery point for which you want to create a
   backup index.
5. Select the **Action** button, and then select
   **Create index**.

While the index is being created, it will have the index status of
`In progress`. Once the status has transitioned to
`Available`, the recovery point can be included in a search.

###### Create an index as you create an on demand backup.

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. See the steps for [Creating an on-demand backup using AWS Backup](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md") Creating an on demand
   backup using AWS Backup.
3. In **Settings**, if you have chosen resource type that
   supports index and search, the line item **Backup search index**
   will be display. Toggle on **Create backup search** index to have
   an index be created concurrently with this on-demand backup.

AWS CLI
Create a backup index through CLI

Use the AWS CLI command [`create-backup-plan`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html") to make a new backup plan. Or, use [`update-backup-plan`](https://amazonaws.com/documentation/api/latest/reference/backup/update-backup-plan.html "https://amazonaws.com/documentation/api/latest/reference/backup/update-backup-plan.html") to modify an existing plan.

For either operation, within the parameter `--backup-plan -rules`,
include `IndexActions`.

See [`IndexActions`](API_IndexAction.md "API_IndexAction.md") in [`BackupRuleInput`](API_BackupRuleInput.md "API_BackupRuleInput.md") in the _AWS Backup API Reference
Guide_ for more information.

Once a recovery point has an index, you can update its settings.

Example:

```
aws backup update-recovery-point-index-settings
--recovery-point-arn arn:aws:ec2:us-west-2::snapshot/snap-012345678901234567
--backup-vault-name `[vaultname]` //
--index ENABLED
--endpoint-url `[URL]`
--iam-role-arn `arn:aws:iam::012345678901:role/Admin`
```

## Searches

Once you have one or more backups with an index, you can search those indexed backups
through the AWS Backup console or through AWS CLI.

As you create a search, you’ll select one resource type. The results will only return
recovery points containing that type, such as S3 buckets or EBS snapshots.

You then specify the properties of the backups (recovery points) you wish to include in
the search. You can specify up to 9 properties. Property types included more than once will
return results that match all included values.

Specify the properties of the items you wish to find within the returned recovery
points, such as bucket name or file size. Narrow your results by including multiple
properties.

If one value for an item property is included when you create a search through the AWS Backup
console, the results will return only items that match that item property (AND logic). If
you repeat the same item property, but with different values, the results will return all
items that match _any_ of the included values (OR logic). For example, if
you include two EBS file paths, all items of recovery points that are included in the search
that match _either_ file path will be in the search results.

- S3 item properties include creation time, Etags, object key, object size, and
  version ID.
- EBS item properties you can use to help filter your search include creation time,
  file path, last modification time, and size.

Optionally, you can include an AWS KMS key ID to encrypt your results. If a key is not
included, AWS Backup will use a service-owned key to encrypt results.

Console

###### Search for items in your backups

There are multiple paths to create a search of indexed backups:

You can find your preferred recovery point by navigating to **Backup
vaults** and selecting the specific recovery point you wish to search.
Then, select **Search**. You can also start a search from the
**Recovery point details** page.

During a restore where you have specific items you wish to include, you can
search your backups to help locate the URL(s) or file paths that contain the
items.

To search through more than one backup, review the following steps:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to **Search** in the left navigation menu.
3. Select **Create search** in the Search history section.
4. Select a **resource type**. You must select one resource type for each search. If
   you change the resource type after additional fields have been entered, your
   entries will be lost and you will need to re-enter them.
5. Choose 1 to 9 **backup properties** to help narrow the
   recovery points that will be returned in your search.

AWS Backup will scan all of your backups that have an index. It will return only
recovery points that match all different backup properties. For example,
`backup tag = "savings"` and `backup creation date = May 20,
 2019 through May 23, 2019`, inclusive.

You may include multiple values of the same property, such as three different
tags. If the property is repeated with different values, the search will return
all items that match any of the values specified (known as "OR" logic). For
example, `backup tag = "savings"`; `backup tag =
 "checking"`; `backup creation date = May 20, 2019 through May 23,
 2019`, inclusive; and `backup creation date = May 20, 2020 through
 May 23, 2020`, inclusive.

A backup creation date range counts as one backup property. Only one backup
creation date range can be included as a backup property. 6. Choose 1 to 9 **item properties** to help further narrow the returns in your search.

You may include multiple values of the same property. If the property is repeated with different values, the search will return all items that match any of the values specified. 7. _Optional_: To encrypt your search results, you can specify an extant AWS KMS key by the dropdown menu or ARN, or you can create a new KMS key. 8. AWS Backup recommends creating a unique search job name. 9. Select **Start search**.

You may see a warning saying that your search may include a large number of
recovery points. The best practice is to go back to the backup properties and
select additional criteria to narrow the search. Fewer backups in a search
may result in lower costs.

AWS CLI
Use the AWS CLI command [start-search-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/start-search-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/start-search-job.html").

Required parameters:

```
--search-scope // defines the backup properties you wish to include in the search
```

Optional parameters:

```
--client-token // string
--encryption-key-arn // if not included, AWS Backup uses service-owned key to encrypt results
--item-filters // accepted keys and values depend on which resource type is included in the search
--name // If not included, AWS Backup auto-assigns a name
```

Accepted S3 item filters include:

```
--object-keys // string
--sizes // long condition
--creation-times // time condition
--version-ids // string
--etags // string
```

Accepted EBS item filters include:

```
--file-paths //
--sizes //
--creation-times //
--last-modification-time //
```

### Stop a search

You can stop a search job if is in status `RUNNING`.

A search job will continue until it reaches `COMPLETED` status (or
`FAILED` status if there is an error). You can interrupt a
`RUNNING` search job if you wish to end an in-progress search job, which may
be desirable if you have found the backup or item you were seeking before the job
completed.

- In the AWS Backup console, Select the **Stop search job**
  button.
- In the CLI, send the operation `stop-search-job` with the search job
  identifier you want to stop.

## Search results

Once a search job has begun, it will begin aggregating results even while has an `Running` status. While a search job is running and until it completes, partial results are available:

- In the console, results will display as they are retrieved during the search.
  Results do not auto-refresh, but you can view the latest results by selecting the
  refresh button. To view results beyond the first 1,000 items, select **Export
  results**.
- The CLI operations [get-search-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/get-search-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/get-search-job.html") and [list-search-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/list-search-jobs.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/list-search-jobs.html") return search job statuses. If the job
  status is `RUNNING`, the operation returns an incomplete list.

Results from a search job are available in the console and through CLI for 7 days once a
search is stopped or has completed. During this time, you can export the results to your
preferred Amazon S3 bucket so you can access the results past this timeframe.

Each search job contains detailed information, available in the console or through CLI,
including which recovery points were searched, the search name and status, its description,
its creation and completion date and time, and information about the objects or items
returned as well as the number of items and recovery points scanned.

If the results do not contain the recovery point, item, or object you were seeking, you can create a new search with different backup and item properties. Each search is charged individually.

Each resource type has unique considerations for the results the search returns:

- A search of S3 recovery points will not return delete markers as part of its search
  result, even if those objects match the search’s specified item properties.
- Results of an EBS search may have a null value for creation time for file systems
  in which that field is unsupported. Those file systems may include, but are not limited
  to, vfat, ext2/3, and versions of XFS prior to v5.

## Export search results to an S3 bucket

AWS Backup retains search results for 7 days, starting with the completion time and date.
These results are viewable in the AWS Backup console or retrievable through the CLI operation
list-search-job-results.

A best practice is to export your search results to an S3 bucket to retain results
beyond the 7 day retention. The export job will create a folder named `Export Job
 ID` in your designated bucket, then export the results to that folder. Once the
results are exported there, they are available for as long as you retain the bucket.

You can export the search results of any supported resource type, not just an S3 search.

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to **Jobs > Search jobs**.
3. Select **search job results**.
4. Place a checkmark next to the result(s) you wish to export.
5. Select **Export to S3**.
6. Choose the destination S3 bucket for the export job.
7. Once you have configured all the fields, select **Export**.

The export action creates an export job. These are viewable in **Jobs >
Export jobs**. Once an export job has reached `COMPLETED`
status, the search result information is available in the S3 bucket to retrieve or to
download as one or more .csv files.

AWS CLI
Use the AWS CLI command [start-search-result-export-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/start-search-result-export-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/start-search-result-export-job.html").

Required parameters:

```
--search-job-identifier
--export-specification
```

Optional parameters:

```
--client-token
--role-arn
--tags
```

Operation will return `ExportJobArn` and `ExportJobIdentifier`.

Use [list-search-result-export-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/list-search-result-export-jobs.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backupsearch/list-search-result-export-jobs.html") to retrieve the statuses of
export jobs.

## Cost considerations and best practices

Each backup index creation and each search job incurs a charge. Each backup index has a
storage charge. Each restore from search results (as with all other all restore jobs) is
charged. Learn more at [AWS Backup pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/").

You can narrow the possible returned results of a search job by including multiple
backup and item properties; this may result in a lower cost than a search than spans all
possible recovery points.

## Restore from search

Many customers choose to search through their backups - and the objects or files within
them - to find a specific recovery point or items to restore. See [Restore a backup by resource type](restoring-a-backup.md "restoring-a-backup.md") for information on
restores in general.

You can restore from your search results in the AWS Backup console by navigating to
**Jobs > Search job results > Restore**. To restore through AWS CLI, use
[`start-restore-job`](API_StartRestoreJob.md "API_StartRestoreJob.md") with metadata specific to the resource type,
recovery point, and items involved in the restore.

See [Restore S3 data using AWS Backup](restoring-s3.md "restoring-s3.md") for information on how
to restore a recovery point with S3 data, to restore an S3 bucket, or to restore up to five
objects or folders with an S3 bucket.

See [Restore an Amazon EBS volume](restoring-ebs.md "restoring-ebs.md") for information about
restoring an EBS snapshot to a new volume that attaches to an EC2 instance.
