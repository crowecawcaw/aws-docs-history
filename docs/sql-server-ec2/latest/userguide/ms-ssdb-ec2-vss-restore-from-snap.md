# Restore your SQL Server database from VSS snapshots

The `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook provides a
streamlined process to restore your SQL Server databases. This guide outlines the
automation runbook functionality and explains the parameters that you can customize to
suit your specific restoration needs.

Before you run the `AWSEC2-RestoreSqlServerDatabaseWithVss` automation
runbook, ensure that you've met all prerequisites to create application consistent
snapshots with the AWS VSS solution. For more information, see [Prerequisites to create Windows VSS based EBS snapshots](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-prereqs.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-prereqs.md") in the
_Amazon EC2 User Guide_.

The `AWSEC2-RestoreSqlServerDatabaseWithVss` process consists of several key
steps, as follows.

1. The first step uses `AWS-ConfigureAwsPackage` to upgrade or
   install the latest version of the `AwsVssComponents` component package.
2. The next step invokes `AWSEC2-PrepareVssRestore` to verify that prerequisites
   are met and that the input parameters include a valid value for the VSS Snapshot Set ID.
3. The process then creates new EBS volumes from the snapshots and attaches them to the
   instance.
4. Finally, the process invokes `AWSEC2-RunVssRestoreForSqlDatabase`, which
   runs the Amazon EC2 VSS Agent to restore the database on the instance, and returns volume IDs
   and their usage status by the restored database, the final restore operation status, and
   Amazon EC2 VSS Agent logs.

## Parameters for the SQL Server database restore runbook

The `AWSEC2-RestoreSqlServerDatabaseWithVss` automation runbook uses the
following input parameters:

###### Note

You can provide one of the following parameters to use a specific snapshot:

- `SnapshotSetId`
- `RestorePointOfTime`
  If both parameters are empty, the restore uses the most recent snapshot set.

**InstanceId** (string, required)

The ID of the Amazon EC2 instance where the restore is performed.

**SourceDatabaseName** (string, required)

The name of the database that's included in the snapshots.

**TargetDatabaseName** (string, optional)

The restore process creates a new database, and restores the data from the
snapshots to the new database from the snapshots. You can optionally set
the name, or leave this parameter empty to use the default name for the new
database (`Db_Restored`). The old database files are removed from
the volume after the process completes.

**SnapshotSetId** (string, optional)

The Snapshot Set ID of the snapshot to use for recovery.

**RestorePointOfTime** (string, optional)

If this parameter is specified, the restore process uses the last Snapshot Set
that was created before the provided point in time value. This parameter
uses the following string format: **MM-dd-yyyy:hh-mm**.

**RestoreWithNorecovery** (string, required)

If this parameter is set to `True` the restore process leaves the
database in restoring state so that you can apply transaction logs after the
database restore is completed. To bring the database online immediately after
the restore is completed, set this parameter to `False`.

**MetadataPath** (string, optional)

The fully qualified path to the directory where the VSS metadata files are
stored. If not specified, the system uses the following default location,
where metadata files are automatically saved during snapshot operations. Use
this parameter to indicate a custom storage location if you've relocated the files.

`%PROGRAMDATA%\Amazon\AwsVss\VssMetadata`.

**AutomationAssumeRole** (string, conditional)

The ARN of the IAM role for the automation to assume.

- _Console:_ If this parameter is not specified, the
  restore process uses the IAM role for the current console session.
- _Command line:_ If this parameter is not specified, the
  restore process uses the IAM role for your current session.

**ExecutionTimeout** (string, optional)

The amount of time, in seconds, that the `RunVssRestoreForSqlDatabase`
step can run before it fails. If this value is not specified, the default timeout is
600 seconds.

## Run the SQL Server database restore process

1. ###### Always On databases: Remove the source database from the SQL Server availability group

If your database is the primary database in an Always On availability group, you must
remove the database from the availability group before you run the restore process.

    1. To remove the database from the availability group, follow the steps described in
     [Remove a primary database from an Always On availability group](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/remove-a-primary-database-from-an-availability-group-sql-server?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/remove-a-primary-database-from-an-availability-group-sql-server?view=sql-server-ver16") on
     the *Microsoft Learn* website.
    2. Verify that the database remains online, and is not in a `Synchronized` state.

2. ###### Execute AWSEC2-RestoreSqlServerDatabaseWithVss Automation Runbook

To view instructions, select the tab that matches your environment.

AWS Management Console
To run the restore in the AWS Management Console, follow these steps:

    1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
    2. Select **Automation** from the navigation pane, under
     **Change Management Tools**. This shows a list of automation
     executions in your account, if applicable.
    3. Choose **Execute automation**. This opens the **Choose
     runbook** page.
    4. In the **Owned by Amazon** tab, search for
     `AWSEC2-RestoreSqlServerDatabaseWithVss`, and select it from the
     results. This opens the **Runbook details** panel.
    5. Select **Default version at runtime**
     from the **Runbook version** list.
    6. Choose **Next**. This opens the page where you can
     configure the settings and enter input parameters for the runbook.
    7. Enter values for the **Input parameters** to configure
     runtime settings for the restore process. For parameter details, see
     [Parameters for the SQL Server database restore runbook](#ms-ssdb-ec2-vss-restore-params "#ms-ssdb-ec2-vss-restore-params").
    8. Choose **Execute** to run the automation.

To review the execution status, navigate to the **Executed Steps**
section within the automation execution details. This section displays all of the steps
that ran, along with their runtime status. If the automation execution failed, follow
the troubleshooting steps outlined in .

    * Locate the command execution ID in the step details.
    * Select the linked ID to access the execution details.
    * Inspect the command output and return code for further
     troubleshooting.

AWS CLI
Run the following command to restore a Microsoft SQL Server database on an instance.
Replace or add parameters based on your specific use case. For parameter details,
see [Parameters for the SQL Server database restore runbook](#ms-ssdb-ec2-vss-restore-params "#ms-ssdb-ec2-vss-restore-params").

```
aws ssm start-automation-execution \
	--document-name "AWSEC2-RestoreSqlServerDatabaseWithVss" \
	--parameters '{"InstanceId":"`i-1234567890abcdef0`","SourceDatabaseName":"`DB_Source`","TargetDatabaseName":"`DB_Restored`"}'
```

###### Get execution status

To get the status of the automation execution, run the following command
using the execution ID returned from `start-automation-execution`.

```
aws ssm get-automation-execution \
	--automation-execution-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

PowerShell
Run the following PowerShell commands with AWS Tools for Windows PowerShell to restore a SQL Server database
on an instance. Replace or add parameters based on your specific use case. For
parameter details, see [Parameters for the SQL Server database restore runbook](#ms-ssdb-ec2-vss-restore-params "#ms-ssdb-ec2-vss-restore-params").

```
Start-SSMAutomationExecution `
-DocumentName "AWSEC2-RestoreSqlServerDatabaseWithVss" `
-Parameter @{"InstanceId" = @($InstanceId); "SourceDatabaseName" = @("DB_Source"); "TargetDatabaseName" = @("DB_Restored"); "RestoreWithNorecovery" = @($True); "AutomationAssumeRole" = @("Arn:of:role")}
```

###### Get execution status

To get the status of the automation execution and the status of each
action step, run the following command using the execution ID returned from
`Start-SSMAutomationExecution`.

```
Get-SSMAutomationExecution -AutomationExecutionId $ExecutionId | Select-Object -ExpandProperty StepExecutions | Select-Object -Property StepName, StepStatus | Out-String
```

3. ###### Clean up unused EBS volumes after the automation execution succeeds

The `AWSEC2-RestoreSqlServerDatabaseWithVss` automation creates
a new EBS volume for each volume snapshot within a VSS snapshot set. These volumes are
then attached to the target instance. The database files may not be located on all
volumes, so you can detach and delete the unused ones.

    1. In the **Execution detail** page, choose the
     **RunVssRestoreForSqlDatabase** step (this is the last step).
    2. Choose the **CommandId** link in the **Outputs**
     section, and then choose the instance id to view the run command output.
    3. At the end of the output is a list of all volumes created and attached to the instance
     for restore purposes, and the status for each one. The status is either `in-use`
     or `unused`. To detach and delete the volumes, see [Detach an Amazon EBS volume from an
     Amazon EC2 instance](../../../ebs/latest/userguide/ebs-detaching-volume.md "../../../ebs/latest/userguide/ebs-detaching-volume.md") in the *Amazon EBS User Guide*.
