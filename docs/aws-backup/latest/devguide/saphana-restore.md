# Restore an SAP HANA database on an Amazon EC2 instance

SAP HANA databases on EC2 instances can be restored using the AWS Backup console, using API,
or using AWS CLI.

###### Topics

- [Restore an SAP HANA database with the AWS Backup console](#w141aac17c29c43b9 "#w141aac17c29c43b9")
- [StartRestoreJob API
  for SAP HANA on EC2](#w141aac17c29c43c11 "#w141aac17c29c43c11")
- [CLI for SAP HANA on EC2](#w141aac17c29c43c13 "#w141aac17c29c43c13")
- [SAP HANA High Availability (HA) restore](#saphanarestoreha "#saphanarestoreha")
- [Troubleshooting](#saphanarestoretroubleshooting "#saphanarestoretroubleshooting")

## Restore an SAP HANA database with the AWS Backup console

Note that backup jobs and restore jobs involving the same database cannot occur
concurrently. When an SAP HANA database restore job is occurring, attempts to back up the
same database will likely result in an error: "Database cannot be backed up while it is
stopped."

1. Access the AWS Backup console using the credentials from prerequisites.
2. Under the **Target restore location** dropdown menu, choose a
   database to overwrite with the recovery point you are using to restore (note that the
   instance hosting the restore target database must also have the permissions from the
   prerequisites).

###### Important

SAP HANA database restores are destructive. Restoring a database will overwrite
the database at the specified target restore location. 3. Complete this step only if you are performing a system copy restore; otherwise,
skip to step 4.

System copy restores are restore jobs which restore to a target database different
from the source database which generated the recovery point. For system copy restores,
notice the `aws ssm-sap put-resource-permission` command provided for you
on the console. This command must be copied, pasted, and executed on the machine that
completed the prerequisites. When running the command, use the credentials from the
role in the prerequisite where you set up the required permissions for registering
applications.

```
// Example command
aws ssm-sap put-resource-permission \
--region `us-east-1` \
--action-type RESTORE \
--source-resource-arn `arn:aws:ssm-sap-east-1:112233445566:HANA/Foo/DB/HDB` \
--resource-arn `arn:aws:ssm-sap:us-east-1:112233445566:HANA/Bar/DB/HDB`
```

4. Once you choose the restore location, you can see the target database’s
   **Resource ID**, **Application name**,
   **Database type**, and the **EC2
   instance**.
5. _Optionally_, you may expand **Advanced restore
   settings** to change your catalog restore option. Available options vary
   based on selected restore settings.
6. Click **Restore backup**.
7. The target location will be overwritten during restore (**"destructive
   restore"**), so you must provide confirmation that you permit this in the
   next pop-up dialog box.
   1. To proceed, you must understand that the existing database will be overwritten
      by the one you are restoring.
   2. Once this is understood, you must acknowledge the existing data will be
      overwritten. To acknowledge this and to proceed, type
      **overwrite** into the text input field.

8. Click **Restore backup**.

If the procedure was successful, a blue banner will appear at the top of the console.
This signifies that the restore job is in progress. You will be automatically redirected
to the Jobs page where your restore job will appear in the list of restore jobs. This most
recent job will have a status of `Pending`. You can search for and then click
on the restore job ID too see details of each restore job. You can refresh the restore
jobs list by clicking the refresh button to view changes to the restore job status.

## [StartRestoreJob API](API_StartRestoreJob.md "API_StartRestoreJob.md")

for SAP HANA on EC2

This action recovers the saved resource identified by an Amazon Resource Name
(ARN).

**Request Syntax**

```
PUT /restore-jobs HTTP/1.1
Content-type: application/json
{
   "IdempotencyToken": "string",
   "Metadata": {
      "string" : "string"
   },
   "RecoveryPointArn": "string",
   "ResourceType": "string"
}
```

**URI Request Parameters**: The request does not use any URI
parameters.

**Request Body**: The request accepts the following data in JSON
format:

**IdempotencyToken**A customer-chosen string that you can use to
distinguish between otherwise identical calls to `StartRestoreJob`. Retrying a
successful request with the same idempotency token results in a success message with no
action taken.

Type: String

Required: No

**Metadata**

A set of metadata key-value pairs. Contains information, such as a resource name,
required to restore a recovery point. You can get configuration metadata about a resource
at the time it was backed up by calling `GetRecoveryPointRestoreMetadata`.
However, values in addition to those provided by
`GetRecoveryPointRestoreMetadata` might be required to restore a resource.
For example, you might need to provide a new resource name if the original already
exists.

You need to include specific metadata to restore an SAP HANA on Amazon EC2 instance. See
[StartRestoreJob metadata](API_StartRestoreJob.md#API_StartRestoreJob_RequestBody "API_StartRestoreJob.md#API_StartRestoreJob_RequestBody") for SAP HANA-specific items.

To retrieve the relevant metadata, you can use the call [`GetRecoveryPointRestoreMetadata`](API_GetRecoveryPointRestoreMetadata.md "API_GetRecoveryPointRestoreMetadata.md").

Example of a standard SAP HANA database recovery point:

```
"RestoreMetadata": {
        "BackupSize": "1660948480",
        "DatabaseName": "`DATABASENAME`",
        "DatabaseType": "SYSTEM",
        "HanaBackupEndTime": "1674838362",
        "HanaBackupId": "1234567890123",
        "HanaBackupPrefix": "1234567890123_SYSTEMDB_FULL",
        "HanaBackupStartTime": "1674838349",
        "HanaVersion": "2.00.040.00.1553674765",
        "IsCompressedBySap": "FALSE",
        "IsEncryptedBySap": "FALSE",
        "SourceDatabaseArn": "arn:aws:ssm-sap:`region`:`accountID`:HANA/`applicationID`/DB/`DATABASENAME`",
        "SystemDatabaseSid": "HDB",
        "aws:backup:request-id": "46bbtt4q-7unr-2897-m486-yn378k2mrw9c"
    }
```

Example of a continuous SAP HANA database recovery point:

```
"RestoreMetadata": {
        "AvailableRestoreBases": "[1234567890123,9876543210987,1472583691472,7418529637418,1678942598761]",
        "BackupSize": "1711284224",
        "DatabaseName": "`DATABASENAME`",
        "DatabaseType": "TENANT",
        "EarliestRestorablePitrTimestamp": "1674764799789",
        "HanaBackupEndTime": "1668032687",
        "HanaBackupId": "1234567890123",
        "HanaBackupPrefix": "1234567890123_HDB_FULL",
        "HanaBackupStartTime": "1668032667",
        "HanaVersion": "2.00.040.00.1553674765",
        "IsCompressedBySap": "FALSE",
        "IsEncryptedBySap": "FALSE",
        "LatestRestorablePitrTimestamp": "1674850299789",
        "SourceDatabaseArn": "arn:aws:ssm-sap:`region`:`accountID`:HANA/`applicationID`/DB/`SystemDatabaseSid`",
        "SystemDatabaseSid": "HDB",
        "aws:backup:request-id": "46bbtt4q-7unr-2897-m486-yn378k2mrw9d"
    }
```

## CLI for SAP HANA on EC2

The command `start-restore-job` recovers the saved resource identified by
an Amazon Resource Name (ARN). CLI will follow the API guideline above.

**Synopsis:**

```
start-restore-job
--recovery-point-arn `value`
--metadata `value`
--aws:backup:request-id `value`
[--idempotency-token `value`]
[--resource-type `value`]
[--cli-input-json `value`]
[--generate-cli-skeleton `value`]
[--debug]
[--endpoint-url `value`]
[--no-verify-ssl]
[--no-paginate]
[--output `value`]
[--query `value`]
[--profile `value`]
[--region `value`]
[--version `value`]
[--color `value`]
[--no-sign-request]
[--ca-bundle `value`]
[--cli-read-timeout `value`]
[--cli-connect-timeout `value`]
```

**Options**

`--recovery-point-arn` (string) is a string in the form of an Amazon
Resource Number (ARN) that uniquely identifies a recovery point; for example
`arn:aws:backup:`region`:123456789012:recovery-point:46bbtt4q-7unr-2897-m486-yn378k2mrw9d`

`--metadata` (map): A set of metadata key-value pairs. Contains
information, such as a resource name, required to restore a recovery point. You can get
configuration metadata about a resource at the time it was backed up by calling
`GetRecoveryPointRestoreMetadata` . However, values in addition to those
provided by `GetRecoveryPointRestoreMetadata` might be required to restore a
resource. You need to specify specific metadata to restore an SAP HANA on Amazon EC2
instance:

- `aws:backup:request-id`: This is any UUID string used for idempotency.
  It does not alter your restore experience in any way.
- `aws:backup:TargetDatabaseArn`: Specify the database to which you want
  to restore. This is the SAP HANA on Amazon EC2 database ARN.
- `CatalogRestoreOption`: Specify where to restore your catalog from. One
  of `NO_CATALOG`, `LATEST_CATALOG_FROM_AWS_BACKUP`,
  `CATALOG_FROM_LOCAL_PATH`
- `LocalCatalogPath`: If CatalogRestoreOption metadata value is
  `CATALOG_FROM_LOCAL_PATH`, then specify the path to local catalog on your
  EC2 instance. This should be a valid file path in your EC2 instance.
- `RecoveryType`: Currently, `FULL_DATA_BACKUP_RECOVERY`,
  `POINT_IN_TIME_RECOVERY`, and `MOST_RECENT_TIME_RECOVERY`
  recovery types are supported.

key = (string); value = (string). Shorthand syntax:

```
KeyName1=string,KeyName2=string
```

JSON syntax:

```
{"string": "string"
  ...}
```

`--idempotency-token` is a user-chosen string that you can use to
distinguish between otherwise identical calls to `StartRestoreJob`. Retrying a
successful request with the same idempotency token results in a success message with no
action taken.

`--resource-type` is a string that starts a job to restore a recovery point
for one of the following resources: `SAP HANA on Amazon EC2` for SAP HANA on
Amazon EC2. _Optionally_, SAP HANA resources can be tagged using the
command `aws ssm-sap tag-resource`

**Output**: `RestoreJobId` is a string that uniquely
identifies the job that restores a recovery point.

## SAP HANA High Availability (HA) restore

There are important considerations and additional steps to include when you are
restoring a high availability (HA) system of SAP HANA. Expand the section below that best
aligns your use case.

Restore scenario:

Before you restore to the target (destination) SAP HANA HA system,

1. If a cluster is installed, put all cluster notes in Maintenance mode.
2. Stop the SAP HANA database on all nodes, including primary and
   secondary.
3. _(Recommended)_ Disable any backup plans to ensure they
   don't interfere with the restore operation.
   After the restore job completes, go to the restored SAP HANA HA system,
   then:

4. Start the SAP HANA database on the primary mode.
5. Manually start any tenant database in which the system database was restored
   but its tenants were not restored.
6. Re-establish SAP HANA system replication (HSR) between the primary and
   secondary nodes.
7. Start the SAP HANA database on the secondary node.
8. If a cluster is installed, ensure all cluster nodes are online.
9. Enable any backup plans you disabled prior to the restore operation.
   _(Optional)_ You can keep the application in sync on [AWS
   Systems Manager for SAP](../../../ssm-sap/latest/userguide/what-is-ssm-for-sap.md "../../../ssm-sap/latest/userguide/what-is-ssm-for-sap.md") by calling [`StartApplicationRefresh`](../../../ssmsap/latest/APIReference/API_StartApplicationRefresh.md "../../../ssmsap/latest/APIReference/API_StartApplicationRefresh.md"), or you can wait for the scheduled
   application refresh that will bring the latest SAP metadata.

Before you begin a restore job, go to the target single-node SAP HANA system,
then:

1. Stop the SAP HANA database on the target SAP HANA system.
2. _(Recommended)_ Disable any backup plans to ensure they
   don't interfere with the restore operation.
   After the restore job completes, go to the target single-node SAP HANA system,
   then:

3. Start SAP HANA on the target SAP HANA system.
4. Manually start each tenant database on the target node.
5. Enable any backup plans you disabled prior to the restore operation.
   _(Optional)_ You can keep the application in sync on [AWS
   Systems Manager for SAP](../../../ssm-sap/latest/userguide/what-is-ssm-for-sap.md "../../../ssm-sap/latest/userguide/what-is-ssm-for-sap.md") by calling [`StartApplicationRefresh`](../../../ssmsap/latest/APIReference/API_StartApplicationRefresh.md "../../../ssmsap/latest/APIReference/API_StartApplicationRefresh.md"), or you can wait for the scheduled
   application refresh that will bring the latest SAP metadata.

Before you start a restore job, go to the target SAP HANA system, then:

1. _(Optional, but recommended)_ Put any installed clusters
   into maintenance mode to avoid an unexpected takeover during the restore
   operation.
2. Ensure the system database is running on the target SAP HANA system.
3. _(Recommended)_ Disable any backup plans to ensure they
   don't interfere with the restore operation.
   After the restore job completes:

- Enable any backup plans you disabled prior to the restore operation.

## Troubleshooting

If any of the following errors occur while attempting a backup operation, see the
associated resolution.

- **Error:** Continuous backup log error

To maintain recovery points for continuous backups, logs are created by SAP HANA
for all changes. When the logs are unavailable, the status of each of these continuous
recovery points is `STOPPED`. The last certain viable recovery point that
can be used to restore is one that has the status of `AVAILABLE`. If the
log data is missing for the time between recovery points with a `STOPPED`
status and points with `AVAILABLE`, these times cannot be guaranteed to
have a successful restore. If you input a date and time within this range, AWS Backup will
attempt the backup, but will use the closest available restorable time. This error
will be shown by the message `“Encountered an issue with log backups. Please
 check SAP HANA for details."`

**Resolution:** In the console, the most recent restorable time,
based on the logs, is displayed. You can input a time more recent than the time shown.
However, if the data for this time is unavailable from the logs, AWS Backup will use the
most recent restorable time.

- **Error:**
  `Internal error`

**Resolution:** Create a support case from your console or
contact Support with the details of your restore such as the restore job ID.

- **Error:**
  `The provided role
 arn:aws:iam::`ACCOUNT_ID`:role/ServiceLinkedRole cannot be
 assumed by AWS Backup`

**Resolution:** Ensure that the role assumed when calling the
restore has the required permissions to create service linked roles.

- **Error:**
  `User:
 arn:aws:sts::`ACCOUNT_ID`:assumed-role/ServiceLinkedRole/AWSBackup-ServiceLinkedRole
 is not authorized to perform: ssm-sap:GetOperation on resource:
 arn:aws:ssm-sap:us-east-1:`ACCOUNT_ID`:...`

**Resolution:** Ensure that the role assumed when calling the
restore permissions outlined in the prerequisites is entered correctly.

- **Error:**
  `b* 449: recovery strategy could not be determined: [111014] The backup with
 backup id '1660627536506' cannot be used for recovery SQLSTATE:
 HY000\n`

**Resolution:** Ensure that Backint agent was properly installed.
Check all the prerequisites, particularly [Install
AWS BackInt Agent and AWS Systems Manager for SAP](../../../sap/latest/sap-hana/aws-backint-agent-installing-configuring.md "../../../sap/latest/sap-hana/aws-backint-agent-installing-configuring.md") on your SAP application server and
then retry installing the BackInt Agent again.

- **Error:**
  `IllegalArgumentException: Restore job provided is not ready to return chunks,
 current restore job status is: CANCELLED`

**Resolution:** Restore job was cancelled by the service
workflow. Retry restore job.

- **Error:** Encountered an issue restore a tenant database on an
  SAP HANA High Availability system: `b* -10709: Connection failed (RTE:[89006]
System call 'connect' failed, rc=111:Connection refused ([::1]:40404 →
localhost:30013))\n`

**Resolution:** Check SAP HANA to ensure that the SYSTEMDB is up
and running.

- **Error:**
  `b'* 448: recovery could not be completed: [301102] exception 301153: Sending
 root key to secondary failed: connection refused. This may be caused by a stopped
 system replication secondary. Please keep the secondary online to receive the
 restored root key. Alternatively you could unregister the secondary site in case of
 an urgent recovery.\n SQLSTATE: HY000\n'`

**Resolution:** On a SAP HANA High Availability system, SAP HANA
may not be running on the secondary node while an active restore operation is running.
Start SAP HANA on the secondary node, then retry the restore job again.

- **Error:**
  `RequestError: send request failed\ncaused by: read tcp
 10.0.131.4:40482->35.84.99.47:443: read: connection timed out"`

**Resolution:** Transient network instability is occurring on the
instance. Retry the restore. If this issue happens consistently, try adding
`ForceRetry: "true"` to agent config file at
`/hana/shared/aws-backint-agent/aws-backint-agent-config.yaml.`

For any other AWS Backint agent related issue, refer to [Troubleshoot AWS
Backint Agent For SAP HANA](../../../sap/latest/sap-hana/aws-backint-agent-troubleshooting.md "../../../sap/latest/sap-hana/aws-backint-agent-troubleshooting.md").
