# Create Windows VSS backups

With AWS Backup, you can back up and restore VSS (Volume Shadow Copy Service)-enabled Windows
applications running on Amazon EC2 instances. If the application has VSS writer registered with
Windows VSS, then AWS Backup creates a snapshot that will be consistent for that application.

You
can perform consistent restores, while using the same managed backup service that is used to
protect other AWS resources. With application-consistent Windows backups on EC2, you get
the same consistency settings and application awareness as traditional backup tools.

###### Note

AWS Backup only supports application-consistent backups of resources running on Amazon EC2,
specifically backup scenarios where application data can be restored by replacing an
existing instance with a new instance created from the backup. Not all instance types or
applications are supported for Windows VSS backups.

For more information, see [Create VSS
based snapshots](../../../AWSEC2/latest/UserGuide/create-vss-snaps.md "../../../AWSEC2/latest/UserGuide/create-vss-snaps.md") in the _Amazon EC2 User Guide_.

To back up and restore VSS-enabled Windows resources running Amazon EC2, follow these
steps to complete the required prerequisite tasks. For instructions, see
[Prerequisites to create Windows VSS based EBS snapshots](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-prereqs.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-prereqs.md") in the _Amazon EC2 User Guide_.

1.  Download, install, and configure the SSM agent in AWS Systems Manager. This step is required.
    For instructions, see [Working with SSM agent
    on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/ssm-agent-windows.md "../../../systems-manager/latest/userguide/ssm-agent-windows.md") in the _AWS Systems Manager User Guide_.
2.  Add an IAM policy to the IAM role and attach the role to the Amazon EC2 instance
    before you take the Windows VSS (Volume Shadow Copy Service) backup. For instructions,
    see [Use an IAM managed policy to grant permissions for VSS based snapshots](../../../AWSEC2/latest/UserGuide/vss-iam-reqs.md "../../../AWSEC2/latest/UserGuide/vss-iam-reqs.md") in the
    _Amazon EC2 User Guide_. For an example of the IAM policy, see [Managed policies for AWS Backup](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
3.  [Download and install VSS components](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-getting-started.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-getting-started.md") to the Windows on Amazon EC2 instance
4.  Enable VSS in AWS Backup:

        1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
        2. On the dashboard, choose the type of backup you want to create, either
         **Create an on-demand backup** or **Manage Backup
         plans**. Provide the information needed for your backup type.
        3. When you're assigning resources, choose **EC2**. Windows VSS
         backup is currently supported for EC2 instances only.
        4. In the **Advanced settings** section, choose **Windows
         VSS**. This enables you to take application-consistent Windows VSS
         backups.
        5. Create your backup.

    A backup job with a status of `Completed` does not guarantee that the VSS
    portion is successful; VSS inclusion is made on a best-effort basis. Proceed with the following
    steps to determine if a backup is application-consistent, crash-consistent, or failed:

5.  Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
6.  Under **My account** in the left navigation, click
    **Jobs**.
7.  A status of `Completed` indicates a successful job that is
    application-consistent (VSS).

A status of `Completed with issues` indicates that
the VSS operation has failed, so only a crash-consistent backup has been successful.
This status will also have a popover message
`"Windows VSS Backup Job Error encountered, trying for regular backup"`.

If the backup was unsuccessful, the status will be `Failed`. 4. To view additional details of the backup job, click on the individual job.
For example, the details may read `Windows VSS Backup attempt failed because of timeout 
 on VSS enabled snapshot creation`.
VSS-enabled backups with a target that is non-Windows or non-VSS component Windows that is
successful job will be crash-consistent without VSS.

## Unsupported Amazon EC2 instances

The following Amazon EC2 instance types are not supported for VSS-enabled Windows backups
because they are small instances and might not take the backup successfully.

- t3.nano
- t3.micro
- t3a.nano
- t3a.micro
- t2.nano
- t2.micro
