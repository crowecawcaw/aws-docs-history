# Use an automation runbook to restore your database from AWS VSS solution snapshots

This guide explains how to use the `AWSEC2-RestoreSqlServerDatabaseWithVss`
automation runbook to restore a Microsoft SQL Server database running on an EC2 instance from
application-consistent snapshots created by the AWS VSS solution. You can tailor the restoration
parameters to your specific needs, such as setting the database to restore mode after restoration.
By leveraging Windows VSS technology, this solution offers the following advantages:

- Fast restoration times.
- The ability to perform the restore without shutting down or pausing the Microsoft SQL Server
  application.
  For more information about the AWS VSS solution, see [Application consistent Windows VSS based Amazon EBS snapshots](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md") in the
  _Amazon EC2 User Guide_.

###### Contents

- [Pricing](#ms-ssdb-ec2-vss-restore-pricing "#ms-ssdb-ec2-vss-restore-pricing")
- [VSS based database restore solution change history](#ms-ssdb-ec2-vss-restore-history "#ms-ssdb-ec2-vss-restore-history")
- [VSS snapshot restore prerequisites](ms-ssdb-ec2-vss-restore-prereq.md "ms-ssdb-ec2-vss-restore-prereq.md")
- [Restore your SQL Server database from VSS snapshots](ms-ssdb-ec2-vss-restore-from-snap.md "ms-ssdb-ec2-vss-restore-from-snap.md")

## Pricing

The AWS VSS solution uses AWS Systems Manager automation runbooks with EBS resources to restore a Microsoft SQL Server
database on an EC2 instance. Associated costs include the following:

**Systems Manager Automation**

With Systems Manager automation runbooks, you pay only for what you use and are charged based on
the number and duration of steps, which includes a free tier per account. If you created an
organization, your free tier usage is shared across all accounts in the Consolidated Billing
family. For more information about Systems Manager automation pricing, see [Automation](https://aws.amazon.com/systems-manager/pricing/#Automation "https://aws.amazon.com/systems-manager/pricing/#Automation").

**Amazon EBS**

During restore steps, the AWS VSS solution creates a new EBS volume and restores data from VSS based
EBS snapshots. With Amazon EBS resources, you pay only for what you provision. For more information,
see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

## VSS based database restore solution change history

The following table includes release and change history for the AWS VSS restore solution.

| Release date     | Details                                                                                                                                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| January 14, 2026 | Enhanced restore solution to create new Amazon EBS volumes only from snapshots that contain source database files to be restored,<br>reducing cleanup overhead and improving the overall reliability of restore operations. |
| April 22, 2025   | Fixed an issue where the restore process times out when disk partition<br>information is not available, improving reliability of restore operations.                                                                        |
| January 24, 2025 | • Updated automation document description to improve clarity<br>• Minor bug fixes and stability improvements                                                                                                                |
| January 15, 2025 | Initial release of the VSS restore solution.                                                                                                                                                                                |
