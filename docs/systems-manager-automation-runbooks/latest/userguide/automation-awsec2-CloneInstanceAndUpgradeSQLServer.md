# `AWSEC2-CloneInstanceAndUpgradeSQLServer`

**Description**

Create an AMI from an EC2 instance for Windows Server running SQL Server 2008 or
later, and then upgrade the AMI to a later version of SQL Server. Only English versions of SQL Server are supported.

The following upgrade paths are supported:

- SQL Server 2008 to SQL Server 2017, 2016, or 2014
- SQL Server 2008 R2 to SQL Server 2017, 2016, or 2014
- SQL Server 2012 to SQL Server 2019, 2017, 2016, or 2014
- SQL Server 2014 to SQL Server 2019, 2017, or 2016
- SQL Server 2016 to SQL Server 2019 or 2017
  If you are using an earlier version of Windows Server that is incompatible with
  SQL Server 2019, the automation document must upgrade your Windows Server version to

2016.

The upgrade is a multi-step process that can take 2 hours to complete. The
automation creates the AMI from the instance, and then launches a temporary instance
from the new AMI in the specified `SubnetID`. The security groups
associated with your original instance are applied to the temporary instance. The
automation then performs an in-place upgrade to the `TargetSQLVersion` on
the temporary instance. After the upgrade, the automation creates a new AMI from
the temporary instance and then terminates the temporary instance.

You can test application functionality by launching the new AMI in your VPC.
After you finish testing, and before you perform another upgrade, schedule
application downtime before completely switching over to the upgraded
instance.

###### Note

If you want to modify the computer name of the EC2 instance launched from the
new AMI , see [Rename a Computer that Hosts a Stand-Alone Instance of SQL
Server](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/rename-a-computer-that-hosts-a-stand-alone-instance-of-sql-server?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/database-engine/install-windows/rename-a-computer-that-hosts-a-stand-alone-instance-of-sql-server?view=sql-server-2017").

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSEC2-CloneInstanceAndUpgradeSQLServer "https://console.aws.amazon.com/systems-manager/automation/execute/AWSEC2-CloneInstanceAndUpgradeSQLServer")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Windows

**Parameters**

**Prerequisites**

- TLS version 1.2.
- Only English versions of SQL Server are supported.
- The EC2 instance must use a version of Windows Server that is Windows Server 2008 R2
  (or later) and SQL Server 2008 (or later).
- Verify that SSM Agent is installed on your instance. For more information,
  see [Installing and
  configuring SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/sysman-install-ssm-win.md "../../../systems-manager/latest/userguide/sysman-install-ssm-win.md").
- Configure the instance to use an AWS Identity and Access Management (IAM) instance profile role.
  For more information, see [Create an IAM instance
  profile for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-profile.md "../../../systems-manager/latest/userguide/setup-instance-profile.md").
- Verify that the instance has 20 GB of free disk space in the instance boot
  disk.
- For instances that use a Bring Your Own License (BYOL) SQL Server version,
  the following additional prerequisites apply:

      + Provide an EBS snapshot ID that includes the target SQL Server
       installation media. To do this:



      	1. Verify that the EC2 instance is running Windows Server
      	 2008 R2 or later.
      	2. Create a 6 GB EBS volume in the same Availability Zone
      	 where the instance is running. Attach the volume to the
      	 instance. Mount it, for example, as drive D.
      	3. Right-click the ISO and mount it to an instance as, for
      	 example, drive E.
      	4. Copy the content of the ISO from drive E:\ to drive
      	 D:\
      	5. Create an EBS snapshot of the 6 GB volume created in step
      	 2.

  **Limitations**

- The upgrade can be performed on only a SQL Server using Windows
  authentication.
- Verify that no security patch updates are pending on the instances. Open
  **Control Panel**, then choose **Check for
  updates**.
- SQL Server deployments in HA and mirroring mode are not supported.

**Parameters**

- IamInstanceProfile

Type: String

Description: (Required) The IAM instance profile.

- InstanceId

Type: String

Description: (Required) The instance running Windows Server 2008 R2 (or later)
and SQL Server 2008 (or later).

- KeepPreUpgradeImageBackUp

Type: String

Description: (Optional) If set to `true`, the automation doesn't delete the
AMI created from the instance before the upgrade. If set to `true`, then you
must delete the AMI. By default, the AMI is deleted.

- SubnetId

Type: String

Description: (Required) Provide a subnet for the upgrade process. Verify
that the subnet has outbound connectivity to AWS services, Amazon S3, and
Microsoft (to download patches).

- SQLServerSnapshotId

Type: String

Description: (Conditional) Snapshot ID for target SQL Server installation
media. This parameter is required for instances that use a BYOL SQL Server
version. This parameter is optional for SQL Server license-included
instances (instances launched using an AWS provided Amazon Machine Image
for Windows Server with Microsoft SQL Server).

- RebootInstanceBeforeTakingImage

Type: String

Description: (Optional) If set to `true`, the automation reboots the
instance before creating a pre-upgrade AMI. By default, the automation
doesn't reboot before upgrade.

- TargetSQLVersion

Type: String

Description: (Optional) Select the target SQL Server version.

Possible targets:

    + SQL Server 2019
    + SQL Server 2017
    + SQL Server 2016
    + SQL Server 2014

Default target: SQL Server 2016
**Outputs**

AMIId: The ID of the AMI created from the instance that was upgraded to a later
version of SQL Server.
