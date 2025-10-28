# Use the AWS VSS solution to restore

data for your instance

You can restore EBS volumes for a Windows instance from VSS based snapshots created
by the AWS VSS solution. If your AWS VSS solution snapshots contain backups of a Microsoft SQL Server database,
you can restore the database using the `AWSEC2-RestoreSqlServerDatabaseWithVss`
AWS Systems Manager Automation runbook.

The database restore runbook automates the entire restore process, including
creating volumes from the snapshots and attaching them to the instance. The automation leverages
VSS technology to restore the database, allowing you to restore without stopping your
SQL Server application or disconnecting any active connections.

For detailed instructions on how to use the Microsoft SQL Server database runbook, see [Restore
from VSS based snapshots](../../../sql-server-ec2/latest/userguide/ms-ssdb-ec2-restore-vss.md "../../../sql-server-ec2/latest/userguide/ms-ssdb-ec2-restore-vss.md") in the _Microsoft SQL Server on Amazon EC2 User Guide_.

## Customize a script to restore EBS volumes from

AWS VSS solution snapshots

You can use the `RestoreVssSnapshotSampleScript.ps1` script as a
model to create your own custom script that restores EBS volumes from AWS VSS solution snapshots.
The sample script performs the following tasks:

- Stops an instance
- Removes all existing drives from the instance (except the boot volume, if it
  was excluded)
- Creates new volumes from the snapshots
- Attaches the volumes to the instance by using the device ID tag on the
  snapshot
- Restarts the instance

###### Important

The following script detaches all volumes attached to an instance, and then
creates new volumes from a snapshot. Make sure that you have properly backed-up the
instance. The old volumes are not deleted. If you want, you can edit the script to
delete the old volumes.

###### To restore volumes from VSS based EBS snapshots

1. Download the [RestoreVssSnapshotSampleScript.zip](../../../systems-manager/latest/userguide/samples/RestoreVssSnapshotSampleScript.md "../../../systems-manager/latest/userguide/samples/RestoreVssSnapshotSampleScript.md") file and extract the file
   contents.
2. Open `RestoreVssSnapshotSampleScript.ps1` in a text
   editor and edit the sample call at the bottom of the script with a valid
   EC2 instance ID and EBS snapshot ID, and then run the script from PowerShell.
