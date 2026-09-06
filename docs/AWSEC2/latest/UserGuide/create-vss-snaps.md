

# Create VSS based EBS snapshots for your EC2 Windows instance
<a name="create-vss-snaps"></a>

After you've met all of the [Prerequisites to create Windows VSS based EBS snapshots](application-consistent-snapshots-prereqs.md), you can use any of the following methods to create VSS based snapshots from your EC2 instance.

**AWS Systems Manager command documents**  
[Use Systems Manager command documents](create-vss-snapshots-ssm.md) to create VSS based snapshots.  
To automate backups, you can create an AWS Systems Manager maintenance window task that uses the `AWSEC2-VssInstallAndSnapshot` command document. For more information, see [Working with Maintenance Windows (Console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-working.html) in the *AWS Systems Manager User Guide*.

**AWS Backup**  
You can create a VSS backup when using AWS Backup by enabling VSS in the console or CLI. For more information, see [Creating Windows VSS backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html) in the *AWS Backup Developer Guide*.  
AWS Backup doesn’t automatically install the `AwsVssComponents` package on your instance. You must perform a manual install on your instance. For more information, see [Manually install the VSS components on an EC2 Windows instance](application-consistent-snapshots-getting-started.md#install-vss-comps).

**Amazon Data Lifecycle Manager**  
You can create VSS snapshots using Amazon Data Lifecycle Manager by enabling pre and post scripts in your snapshot lifecycle policies. For more information, see [Automating application-consistent snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/automate-app-consistent-backups.html) in the *Amazon EBS User Guide*.  
Amazon Data Lifecycle Manager doesn’t automatically install the `AwsVssComponents` package on your instance. You must perform a manual install on your instance. For more information, see [Manually install the VSS components on an EC2 Windows instance](application-consistent-snapshots-getting-started.md#install-vss-comps).