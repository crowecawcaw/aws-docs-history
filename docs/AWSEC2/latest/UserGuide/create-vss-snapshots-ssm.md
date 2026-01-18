# Use Systems Manager command documents to create VSS based snapshots

You can use AWS Systems Manager command documents to create VSS based snapshots.
The following content introduces the command documents that are available, and the
runtime parameters that the documents use to create your snapshots.

Before you use any of the Systems Manager command documents, ensure that you've met all
[Prerequisites to create Windows VSS
based EBS snapshots](application-consistent-snapshots-prereqs.md "application-consistent-snapshots-prereqs.md").

###### Topics

- [Parameters for Systems Manager VSS snapshot
  documents](#create-vss-snapshots-ssm-params "#create-vss-snapshots-ssm-params")
- [Run Systems Manager VSS snapshot
  command documents](#create-vss-snapshots-ssm-methods "#create-vss-snapshots-ssm-methods")

## Parameters for Systems Manager VSS snapshot

documents

The Systems Manager documents that create VSS snapshots all use the following parameters, except
where noted:

**AmiName** (string, optional)

If the **CreateAmi** option is set to
`True`, specify the name of the AMI that the backup creates.

**description** (string, optional)

Specify a description for the snapshots or image that this process creates.

**CollectDiagnosticLogs** (string, optional)

To collect more information during snapshot and AMI creation steps, set this
parameter to "`True`". The default value for this parameter is
"`False`". Consolidated diagnostic logs are saved as a `.zip` format
archive at the following location on your instance:

`C:\ProgramData\Amazon\AwsVss\Logs\`timestamp`.zip`

**CopyOnly** (string, optional)

If you use the native SQL Server backup in addition to AWS VSS, performing a
Copy-only backup prevents AWS VSS from breaking the native differential
backup chain. To perform a Copy-only backup operation, set this parameter to
`True`.

The default value for this parameter is `False`, which causes AWS VSS
to perform a full backup operation.

**CreateAmi** (string, optional)

To create a VSS based Amazon Machine Image (AMI) to back up your instance,
set this parameter to `True`. The default value for this parameter is
`False`, which backs up your instance with an EBS snapshot instead.

For more information about creating an AMI from an instance, see
[Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").

**executionTimeout** (string, optional)

Specify the maximum time in seconds to run the snapshot creation process on the
instance, or to create an AMI from the instance. Increasing this timeout allows the
command to wait longer for VSS to start its freeze and complete tagging of the resources
it creates. This timeout only applies to the snapshot or AMI creation steps. The initial
step to install or update the `AwsVssComponents` package is not
included in the timeout.

**ExcludeBootVolume** (string, optional)

This setting excludes boot volumes from the backup process if you
create snapshots. To exclude boot volumes from your snapshots, set
**ExcludeBootVolume** to `True`,
and **CreateAmi** to `False`.

If you create an AMI for your backup, this parameter should be set
to `False`. The default value for this parameter is
`False`.

**NoWriters** (string, optional)

To exclude application VSS writers from the snapshot process, set this parameter
to `True`. Excluding application VSS writers can help you resolve
conflicts with third-party VSS backup components. The default value for this
parameter is `False`.

If `SaveVssMetadata` is `True`, this parameter must be
set to `False`.

**SaveVssMetadata** (string, optional)

To save VSS metadata files during every snapshot, set this parameter to
`True`. The default value is `False`. These files
help provide insights into which components or writers were included in a backup
operation, and the associated files and volumes for each snapshot. The metadata files
are used when restoring a SQL database using VSS restore solution. For more information
on how to restore a SQL database from VSS snapshots, see
[Use an automation runbook to restore your database from AWS VSS solution snapshots](../../../sql-server-ec2/latest/userguide/ms-ssdb-ec2-restore-vss.md "../../../sql-server-ec2/latest/userguide/ms-ssdb-ec2-restore-vss.md").

Metadata files have the associated snapshot set id in their names. You can find
them at the following location on your instance:

```
`C:\ProgramData\Amazon\AwsVss\VssMetadata\`
```

###### Warning

- Saving VSS metadata files requires `AwsVssComponents`
  package version 2.4.0 or later. If your instance has an earlier version
  installed, setting `SaveVssMetadata` to `True`
  causes the snapshot creation to fail.
- The `NoWriters` and `SaveVssMetadata` parameters
  are mutually exclusive. If both are set to `True` then
  snapshot creation fails.

**tags** (string, optional)

We recommend that you tag your snapshots and images to help you locate and
manage your resources, for example, to restore volumes from a list of snapshots.
The system adds the `Name` key, with a blank value where you can specify
the name that you want to apply to your output snapshots or images.

If you want to specify additional tags, separate tags with a semicolon in between.
For example, `Key=Environment,Value=Test;Key=User,Value=TestUser1`.

###### Note

Tag keys and values must only contain alphanumeric characters and the following
special characters: `() ./\-"'@_+:={}`.

By default, the system adds the following reserved tags for VSS based snapshots
and images.

- **Device** – For VSS based snapshots,
  this is the device name of the EBS volume that the snapshot captures.
- **AppConsistent** – This tag indicates
  the successful creation of a VSS based snapshot or AMI.
- **AwsVssConfig** – This identifies
  snapshots and AMIs that are created with VSS enabled. The tag includes meta
  information such as the `AwsVssComponents` version, and the
  Snapshot Set ID.

###### Warning

Specifying any of these reserved tags in your parameter list will
cause an error.

**VssVersion** (string, optional)

For the `AWSEC2-VssInstallAndSnapshot` document only, you can specify
the `VssVersion` parameter to install a specific version of
`AwsVssComponents` package on your instance. Leave this parameter
blank to install the recommended default version.

If the specified version of the `AwsVssComponents` package
is already installed, the script skips the install step and moves on to the
backup step. For a list of `AwsVssComponents` package versions
and operating support, see [AWS VSS solution version history](vss-comps-history.md "vss-comps-history.md").

## Run Systems Manager VSS snapshot

command documents

You can create VSS based EBS snapshots with AWS Systems Manager command documents as follows.

When you use AWS Systems Manager to run the `AWSEC2-VssInstallAndSnapshot` document,
the script runs the following steps.

1. The script first installs or updates the `AwsVssComponents`
   package on your instance, depending on whether it's already installed.
2. The script creates the application-consistent snapshots after the first
   step completes.
   To run the `AWSEC2-VssInstallAndSnapshot` document, follow the steps for
   your preferred environment.

Console

###### Create VSS based EBS snapshots from the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Run Command** from the navigation pane.
   This shows a list of commands that are currently running in your account,
   if applicable.
3. Choose **Run command**. This opens a list of command
   documents that you have access to.
4. Select `AWSEC2-VssInstallAndSnapshot` from the list
   of command documents. To streamline results, you can enter all or part of
   the document name. You can also filter by the owner, by platform types,
   or by tags.

When you select a command document, details populate below the list. 5. Select `Default version at runtime` from the
**Document version** list. 6. Configure the **Command parameters** to define how
`AWSEC2-VssInstallAndSnapshot` will install the
`AwsVssComponents` package and back up with VSS snapshots
or an AMI. For parameter details, see [Parameters for Systems Manager VSS snapshot
documents](#create-vss-snapshots-ssm-params "#create-vss-snapshots-ssm-params"). 7. For **Target selection**, specify tags or select
instances manually to identify the instances on which to run this operation.

###### Note

If you select instances manually, and an instance you expect to see is not
included in the list, see [Where Are My Instances?](../../../systems-manager/latest/userguide/troubleshooting-remote-commands.md#where-are-instances "../../../systems-manager/latest/userguide/troubleshooting-remote-commands.md#where-are-instances") for troubleshooting tips. 8. For additional parameters to define Systems Manager Run Command behavior such as
**Rate control**, enter values as described in
[Running commands from the console](../../../systems-manager/latest/userguide/running-commands-console.md "../../../systems-manager/latest/userguide/running-commands-console.md"). 9. Choose **Run**.

If successful, the command populates the list of EBS snapshots with the
new snapshots. You can locate these snapshots in the list of EBS snapshots
by searching for the tags you specified, or by searching for
`AppConsistent`. If the command execution failed, view the
Systems Manager command output for details about why the execution failed. If the
command successfully completed, but a specific volume backup failed, you can
troubleshoot the failure in the list of EBS volumes.

AWS CLI
You can run the following commands in the AWS CLI to create VSS based
EBS snapshots and get the status of your snapshot creation.

###### Create VSS based EBS snapshots

Run the following command to create VSS based EBS snapshots. To
create the snapshots, you must identify the instances with the
`--instance-ids` parameter. For more information about
other parameters that you can use, see [Parameters for Systems Manager VSS snapshot
documents](#create-vss-snapshots-ssm-params "#create-vss-snapshots-ssm-params").

```
aws ssm send-command \
	--document-name "AWSEC2-VssInstallAndSnapshot" \
	--instance-ids "`i-01234567890abcdef`" \
	--parameters '{"ExcludeBootVolume":["False"],"description":["Description"],"tags":["Key=`key_name`,Value=`tag_value`"],"VssVersion":[""]}'
```

If successful, the command document populates the list of EBS
snapshots with the new snapshots. You can locate these snapshots in
the list of EBS snapshots by searching for the tags you specified, or
by searching for `AppConsistent`. If the command execution
failed, view the command output for details about why the execution
failed.

###### Get command status

To get the current status of the snapshots, run the following command
using the command ID returned from **send-command**.

```
aws ssm get-command-invocation
	--instance-ids "`i-01234567890abcdef`" \
	--command-id "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`" \
	--plugin-name "CreateVssSnapshot"
```

PowerShell
Run the following commands with AWS Tools for Windows PowerShell to create VSS based EBS snapshots
and get the current runtime status for the creation of your output.
Specify parameters described in the prior list to modify the behavior of the
snapshot process.

###### Create VSS based EBS snapshots with Tools for Windows PowerShell

Run the following command to create VSS based EBS snapshots
or AMIs.

```
Send-SSMCommand -DocumentName "AWSEC2-VssInstallAndSnapshot" -InstanceId "`i-01234567890abcdef`" -Parameter @{'ExcludeBootVolume'='False';'description'='`a_description`'
	;'tags'='Key=`key_name`,Value=`tag_value`';'VssVersion'=''}
```

###### Get command status

To get the current status of the snapshots, run the following command
using the command ID returned from **Send-SSMCommand**.

```
Get-SSMCommandInvocationDetail -InstanceId "`i-01234567890abcdef`" -CommandId "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`" -PluginName "CreateVssSnapshot"
```

If successful, the command populates the list of EBS snapshots with the new
snapshots. You can locate these snapshots in the list of EBS snapshots by
searching for the tags you specified, or by searching for
`AppConsistent`. If the command execution failed, view the
command output for details about why the execution failed.

To run the `AWSEC2-CreateVssSnapshot` document, follow the steps for
your preferred environment.

Console

###### Create VSS based EBS snapshots from the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Run Command** from the navigation pane.
   This shows a list of commands that are currently running in your account,
   if applicable.
3. Choose **Run command**. This opens a list of command
   documents that you have access to.
4. Select `AWSEC2-CreateVssSnapshot` from the list
   of command documents. To streamline results, you can enter all or part of
   the document name. You can also filter by the owner, by platform types,
   or by tags.

When you select a command document, details populate below the list. 5. Select `Default version at runtime` from the
**Document version** list. 6. Configure the **Command parameters** to define how
`AWSEC2-CreateVssSnapshot` will back up with VSS snapshots
or an AMI. For parameter details, see [Parameters for Systems Manager VSS snapshot
documents](#create-vss-snapshots-ssm-params "#create-vss-snapshots-ssm-params"). 7. For **Target selection**, specify tags or select
instances manually to identify the instances on which to run this operation.

###### Note

If you select instances manually, and an instance you expect to see is not
included in the list, see [Where Are My Instances?](../../../systems-manager/latest/userguide/troubleshooting-remote-commands.md#where-are-instances "../../../systems-manager/latest/userguide/troubleshooting-remote-commands.md#where-are-instances") for troubleshooting tips. 8. For additional parameters to define Systems Manager Run Command behavior such as
**Rate control**, enter values as described in
[Running commands from the console](../../../systems-manager/latest/userguide/running-commands-console.md "../../../systems-manager/latest/userguide/running-commands-console.md"). 9. Choose **Run**.

If successful, the command populates the list of EBS snapshots with the
new snapshots. You can locate these snapshots in the list of EBS snapshots
by searching for the tags you specified, or by searching for
`AppConsistent`. If the command execution failed, view the
Systems Manager command output for details about why the execution failed. If the
command successfully completed, but a specific volume backup failed, you can
troubleshoot the failure in the list of EBS volumes.

AWS CLI
You can run the following command in the AWS CLI to create VSS based
EBS snapshots.

###### Create VSS based EBS snapshots

Run the following command to create VSS based EBS snapshots. To
create the snapshots, you must identify the instances with the
`--instance-ids` parameter. For more information about
other parameters that you can use, see [Parameters for Systems Manager VSS snapshot
documents](#create-vss-snapshots-ssm-params "#create-vss-snapshots-ssm-params").

```
aws ssm send-command \
	--document-name "AWSEC2-CreateVssSnapshot" \
	--instance-ids "`i-01234567890abcdef`" \
	--parameters '{"ExcludeBootVolume":["False"],"description":["Description"],"tags":["Key=`key_name`,Value=`tag_value`"]}'
```

If successful, the command document populates the list of EBS
snapshots with the new snapshots. You can locate these snapshots in
the list of EBS snapshots by searching for the tags you specified, or
by searching for `AppConsistent`. If the command execution
failed, view the command output for details about why the execution
failed.

PowerShell
Run the following command with AWS Tools for Windows PowerShell to create VSS based EBS snapshots.

###### Create VSS based EBS snapshots with Tools for Windows PowerShell

Run the following command to create VSS based EBS snapshots. To
create the snapshots, you must identify the instances with the
`InstanceId` parameter. You can specify more than one instance
to create snapshots for. For more information about
other parameters that you can use, see [Parameters for Systems Manager VSS snapshot
documents](#create-vss-snapshots-ssm-params "#create-vss-snapshots-ssm-params").

```
Send-SSMCommand -DocumentName AWSEC2-CreateVssSnapshot -InstanceId "`i-01234567890abcdef`" -Parameter @{'ExcludeBootVolume'='False';'description'='`a_description`'
	;'tags'='Key=`key_name`,Value=`tag_value`'}
```

If successful, the command populates the list of EBS snapshots with the new
snapshots. You can locate these snapshots in the list of EBS snapshots by
searching for the tags you specified, or by searching for
`AppConsistent`. If the command execution failed, view the
command output for details about why the execution failed. If the command
successfully completed, but a specific volume backup failed, you can
troubleshoot the failure in the list of EBS snapshots.

You can use any of the command line procedures described in the previous section
to create a VSS based snapshot. The command document
(`AWSEC2-VssInstallAndSnapshot` or `AWSEC2-CreateVssSnapshot`)
must run on the primary node in your cluster. The document will fail
on the secondary nodes as they don't have access to the shared disks. If your
primary and secondary change dynamically, you can run the AWS Systems Manager Run Command
document on multiple nodes with the expectation that the command will succeed on
the primary node and fail on secondary nodes.

###### Note

To automate backups, you can create an AWS Systems Manager maintenance window task that uses the
`AWSEC2-VssInstallAndSnapshot` document. For more information, see
[Working with Maintenance Windows (Console)](../../../systems-manager/latest/userguide/sysman-maintenance-working.md "../../../systems-manager/latest/userguide/sysman-maintenance-working.md") in the
_AWS Systems Manager User Guide_.
