# Get started with AWS Launch Wizard for SQL

Server

This section contains information to help you set up your environment to deploy SQL
Server with Launch Wizard, including:

- Active Directory permissions
- How to create an IAM policy and assign the permissions
- OS and SQL version requirements
- Configuration settings
  When your environment is set up, you can deploy a SQL Server Always On application with
  Launch Wizard by following the [steps and parameter
  specification details](launch-wizard-deploying.md "launch-wizard-deploying.md") provided in this section.

###### Topics

- [AWS Identity and Access Management (IAM)](#launch-wizard-iam "#launch-wizard-iam")
- [Active Directory (Windows deployment)](#launch-wizard-ad "#launch-wizard-ad")
- [Requirements for Windows and Linux AMIs](#launch-wizard-amis "#launch-wizard-amis")
- [Requirements for using
  Amazon FSx](#launch-wizard-sql-prerequisites-fsx "#launch-wizard-sql-prerequisites-fsx")
- [Configuration settings (deployment on
  Windows)](#launch-wizard-config "#launch-wizard-config")

## AWS Identity and Access Management (IAM)

The following steps to establish the AWS Identity and Access Management (IAM) role and set up the user for
permissions are typically performed by an IAM administrator for your organization.

###### Topics

- [Sign up for an AWS account](#launch-wizard-sql-aws-account "#launch-wizard-sql-aws-account")
- [Assign permissions to use Launch Wizard](#launch-wizard-user-setup "#launch-wizard-user-setup")
- [One-time creation of IAM Role](#launch-wizard-iam-role "#launch-wizard-iam-role")
- [AWS Secrets Manager
  permissions](#launch-wizard-sql-prerequisites-secrets-manager "#launch-wizard-sql-prerequisites-secrets-manager")

### Sign up for an AWS account

#### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

#### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

### Assign permissions to use Launch Wizard

To deploy a SQL Server Always On application with Launch Wizard, your user must have the
permissions provided by the `AmazonLaunchWizardFullAccessV2` policy. The
following guidance is provided for IAM administrators to provide permissions for
users to access and deploy applications from Launch Wizard using the
`AmazonLaunchWizardFullAccessV2` policy.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### Important

Log in with the user associated with the above policy when you use Launch Wizard.

### One-time creation of IAM Role

On the **Choose Application** page of Launch Wizard, under
**Permissions**, Launch Wizard displays the IAM role required for the
Amazon EC2 instances created by Launch Wizard to access other AWS services on your behalf. When
you select **Next**, Launch Wizard attempts to discover the IAM role in
your account. If the role exists, it is attached to the instance profile for the EC2
instances that Launch Wizard will launch into your account. If the role does not exist, Launch Wizard
attempts to create the role with the same name,
`AmazonEC2RoleForLaunchWizard`. This role is comprised of two IAM
managed policies: `AmazonSSMManagedInstanceCore` and
`AmazonEC2RolePolicyForLaunchWizard`. After the role is created, the
IAM administrator can delegate the application deployment process to another user
who, in turn, must have the Launch Wizard IAM managed policy described in the following
section.

### AWS Secrets Manager

permissions

Launch Wizard uses AWS Secrets Manager to manage your domain and SQL Server account passwords. Your
username and password is stored in Secrets Manager and is retrieved during the build
process. The following resource policy is added to the secret so that the
`AmazonEC2RoleForLaunchWizard` IAM role used by Launch Wizard can retrieve
the secret. For more information about Secrets Manager, see the [AWS Secrets Manager
User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS":
 "arn:aws:iam::`111122223333`:role/service-role/AmazonEC2RoleForLaunchWizard"
 },
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:CreateSecret",
 "secretsmanager:GetRandomPassword"
 ],
 "Resource": "*"
 }
 ]
}`

```

[Show moreShow less](# "#")

## Active Directory (Windows deployment)

Launch Wizard can deploy SQL Server using AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD), or your
Self Managed Active Directory.

###### Topics

If you are deploying SQL Server into an existing VPC with an existing
Active Directory, Launch Wizard uses your Managed Active Directory
(AD) domain user credentials to set up a fully functional SQL Server Always On
Availability Group in the Active Directory. Launch Wizard supports this deployment option
only for AWS Managed Active Directory. Your Managed Active Directory does not
have to be in the same VPC as the one in which SQL Server Always On is deployed.
If it is in a different VPC than the one in which SQL Server Always On is
deployed, verify that you set up connectivity between the two VPCs. The domain
user requires the following permissions in the [Active Directory Default organizational unit (OU)](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-an-organizational-unit-design "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-an-organizational-unit-design") to enable Launch
Wizard to perform the deployment successfully:

- `Reset password`
- `Write userAccountControl`
- `Create user accounts`
- `Create computer objects`
- `Read all properties`
- `Modify permissions`
  The following key operations are performed against your Active Directory by
  Launch Wizard. These operations result in the creation of new records or entries in
  Active Directory.

- SQL Server service user added as a new Active Directory user if it
  does not already exist in Active Directory.
- SQL Server instance and Remote Desktop Gateway Access instance joined
  to the Active Directory domain.
- `CreateChild` role added to Windows Server Failover Cluster
  as part of `ActiveDirectoryAccessRule`.
- `FullControl` role added to SQL Server Service user as part
  of `FileSystemRights`.

If you are deploying SQL Server into an existing VPC across multiple
Availability Zones and connecting to a Self Managed Active Directory or deploying SQL Server into an existing VPC on a single node
and connecting to a Self Managed Active Directory, verify the
following prerequisites.

- If your Self Managed Active Directory resides in another network than
  where you are deploying SQL Server, make sure you have connectivity
  between your VPC and the Self Managed Active Directory network. You must
  also be able to connect to any DNS servers you specify during deployment
  from your VPC. For more information, see [Network-to-Amazon VPC connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md").
- Your SQL Server resources must be able to perform DNS resolution from
  within the VPC to any DNS servers you specify. For options on how to set
  this up, see [How to Set Up DNS Resolution Between On-Premises Networks and
  AWS Using AWS Directory Service and Amazon Route 53](https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-amazon-route-53/ "https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-amazon-route-53/") or [How to Set Up DNS Resolution Between On-Premises Networks and AWS
  Using AWS Directory Service and Microsoft Active Directory](https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-microsoft-active-directory/ "https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-using-aws-directory-service-and-microsoft-active-directory/").
- The domain functional level of your Active Directory domain controller
  must be Windows Server 2019 or later.
- The firewall on the Active Directory domain controllers should allow
  the connections from the Amazon VPC from which you will create the Launch Wizard
  deployment. At a minimum, your configuration should include the ports
  mentioned in [How to configure a firewall for Active Directory domains and
  trusts](https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts "https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts").
- The domain user requires the following permissions in the [Active Directory Default organizational unit (OU)](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-an-organizational-unit-design "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-an-organizational-unit-design") to enable
  Launch Wizard to perform the deployment successfully:
  - `Reset password`
  - `Write userAccountControl`
  - `Create user accounts`
  - `Create computer objects`
  - `Read all properties`
  - `Modify permissions`

## Requirements for Windows and Linux AMIs

Launch Wizard has requirements for using custom Windows and Linux AMIs as well as Windows
license-included AMIs in certain deployment scenarios.

###### Topics

When you use Windows license-included AMIs, note the following:

- You can use Windows license-included AMIs with SQL
  Bring-Your-Own-License (BYOL).
- Your SQL media must meet certain requirements to use Windows
  license-included AMIs with SQL BYOL. The SQL media must be:

      + An ISO file.
      + Hosted in an Amazon S3 bucket prefixed with
       `LaunchWizard-*`.
      + Included in a folder within the Amazon S3 bucket.
      + Included in a public folder so that Launch Wizard can download and
       install the media.

  We recommend that you use Amazon Windows license-included AMIs whenever
  possible. There are scenarios for which you may want to use a custom Windows
  AMI. For example, you may have existing licenses (BYOL), or you may have made
  changes to one of our public images and re-imaged it.

If you use Amazon Windows license-included AMIs, you are not required to
perform any pre-checks on the AMI to ensure that it meets Launch Wizard
requirements.

Launch Wizard relies on user data to begin the process of configuring SQL Server or RGW
instances to launch in your account. For more information, see [User Data Scripts](../../../AWSEC2/latest/UserGuide/user-data.md "../../../AWSEC2/latest/UserGuide/user-data.md"). By default, all AWS Windows AMIs have user
data execution enabled for the initial launch. To ensure that your custom AMIs
are set up to run the User Data script at launch, follow the AWS recommended
method to prepare your AMIs using [EC2Launch v2](../../../AWSEC2/latest/UserGuide/ec2launch-v2.md "../../../AWSEC2/latest/UserGuide/ec2launch-v2.md"). For
more information about how to prepare your custom AMI using the options to
`Shutdown with Sysprep` or `Shutdown without Sysprep`,
see [Create a Standard Amazon Machine Image Using Sysprep](../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md#ami-create-standard "../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md#ami-create-standard") or [EC2Launch v2 and Sysprep](../../../AWSEC2/latest/WindowsGuide/ec2launch.md#ec2launch-v2-sysprep "../../../AWSEC2/latest/WindowsGuide/ec2launch.md#ec2launch-v2-sysprep"). If you want to directly enable user data
as part of the custom AMI creation process, follow the steps for
`Subsequent Reboots` or `Starts` under [Run commands on your EC2 instance at launch](../../../AWSEC2/latest/UserGuide/user-data.md "../../../AWSEC2/latest/UserGuide/user-data.md").

If you use a custom Windows AMI, the volume drive letter for the root
partition should be `C:` because EC2Launch v2 relies on
this configuration to install the components.

While not exhaustive, the following requirements cover most of the
configurations whose alteration might impact the successful deployment of a SQL
Server Always On application using Launch Wizard.

| Support matrix  | SQL Server Version | Windows Server 2019 | Windows Server 2022 | Windows Server 2025 |
| --------------- | ------------------ | ------------------- | ------------------- | ------------------- |
| SQL Server 2019 | YES                | YES                 | YES                 |
| SQL Server 2022 | YES                | YES                 | YES                 |
| SQL Server 2025 | YES                | YES                 | YES                 |

###### OS and SQL requirements

- Windows Server 2019 (Datacenter) (64-bit only)
- Windows Server 2022 (Datacenter) (64-bit only)
- MBR-partitioned volumes and GUID Partition Table (GPT) partitioned
  volumes that are formatted using the NTFS file system
- English language pack only
- SQL Server Enterprise Edition 2019 or Standard Edition 2019
- SQL Server Enterprise Edition 2022, Standard Edition 2022, or Developer Edition 2022
- SQL Server Standard Developer Edition 2025
- SQL Server Enterprise Developer Edition 2025
- The root volume drive for the custom AMI should be
  `C:`
- SQL Server is installed on the root drive

###### AWS software and drivers

- EC2Launch v2
- AWS SSM ([SSM agent must be installed](../../../systems-manager/latest/userguide/sysman-install-win.md "../../../systems-manager/latest/userguide/sysman-install-win.md"))
- AWS Tools for Windows PowerShell
- Network drivers (SRIOV, ENA)
- Storage drivers (NVMe, AWS PV)
  There are occasions when you may want to use a custom Linux AMI. For example,
  you may have existing licenses (BYOL), or you may have made changes to one of
  our public images and re-imaged it.

If you use a custom Linux AMI, you must adhere to the following
requirements:

- The operating system must be Ubuntu version 18.04 LTS.
- The system installer and administrator must be a sudo user and be able
  to log in to the cluster nodes using SSH.
- SQL Server for Linux must be a default installation.
- The SQL Server for Linux version must be 2019.
- The latest Microsoft SQL tools must be installed.

## Requirements for using

Amazon FSx

Launch Wizard uses continuously available Amazon FSx file shares to host clustered databases. The
Amazon FSx file shares are accessible from within an instance joined to the domain. You can
either create a new Active Directory or connect to an existing Active Directory (managed
or Self Managed). If you connect to an existing Active Directory, you can use
preexisting security groups . The security groups must satisfy port and security
requirements for FSx to communicate with the domain, as described in [Using Amazon
FSx with your Self Managed Microsoft Active Directory](../../../fsx/latest/WindowsGuide/Self Managed-AD.md "../../../fsx/latest/WindowsGuide/Self Managed-AD.md") and [Using
Amazon FSx with AWS Directory Service for Microsoft Active
Directory](../../../fsx/latest/WindowsGuide/fsx-aws-managed-ad.md "../../../fsx/latest/WindowsGuide/fsx-aws-managed-ad.md").

If you are using an existing AWS Managed Active Directory instance, you must specify
the ID of the managed Active Directory instance for FSx to be able to join the domain.
The account must have the same access rights in the domain as described in [Using Amazon
FSx with your Self Managed Microsoft Active Directory](../../../fsx/latest/WindowsGuide/self-managed-AD.md "../../../fsx/latest/WindowsGuide/self-managed-AD.md") and [Using
Amazon FSx with AWS Directory Service for Microsoft Active
Directory](../../../fsx/latest/WindowsGuide/fsx-aws-managed-ad.md "../../../fsx/latest/WindowsGuide/fsx-aws-managed-ad.md").

For Amazon FSx using NetApp ONTAP, Launch Wizard creates security groups in order to access the
ONTAP file system and to set up failover clustering. For port requirements, see [File System Access Control with Amazon VPC](../../../fsx/latest/ONTAPGuide/limit-access-security-groups.md "../../../fsx/latest/ONTAPGuide/limit-access-security-groups.md") in the _Amazon FSx for NetApp ONTAP
User Guide_.

###### Note

This Launch Wizard deployment relies on the instances that are being deployed to be able to
connect to your ONTAP endpoint from within the VPC. For more information on the
connectivity requirements, see [Accessing data from within
AWS](../../../fsx/latest/ONTAPGuide/access-environments.md "../../../fsx/latest/ONTAPGuide/access-environments.md") in the _Amazon FSx for NetApp ONTAP User Guide_.

###### Backup schedule

Launch Wizard uses FSx defaults for setting up the backup schedule. You can change the
default settings in the FSx console after the build completes.

The `WeeklyMaintenanceStartime` follows the format `day of the
 week:time`, where Monday is indicated by `1`. The maintenance start
time is set to begin on Saturday at 10pm.

```
WeeklyMaintenanceStartTime: '6:22:00'
DailyAutomaticBackupStartTime: '01:00'
AutomaticBackupRetentionDays: 7
```

###### Amazon FSx using NetApp ONTAP

Amazon FSx using NetApp ONTAP creates a new ONTAP file system for use with your
Launch Wizard SQL deployment. We use the formulas in the following table to calculate volume
and LUN storage for optimal performance.

These values can be modified post deployment.

| Storage type      | Size in GB | Sizing calculations                              |
| ----------------- | ---------- | ------------------------------------------------ |
| FSx storage       | 1024       | Size in GB                                       |
| Volume storage    | 870.4      | 85% of total storage FSx capacity                |
| LUN storage       | 696.32     | 80% of volume storage (65% of total FSx storage) |
| SQL data LUN size | 522.24     | 60% of LUN storage                               |
| SQL log LUN size  | 139.264    | 20% of SQL Data LUN size                         |

###### Backup schedule for ONTAP

By default, ONTAP backups are disabled during builds. You can set your own backup
schedule from the Amazon FSx console. Choose the **Backup** tab. Then,
choose **Update** to update the backup settings.

###### Note

When you delete a Launch Wizard deployment that uses ONTAP, FSx creates a backup of the
ONTAP volume before deleting the file system. You can delete the backup from the
Amazon FSx console if it is not required. For more information, see [Deleting
backups](../../../fsx/latest/ONTAPGuide/using-backups.md#delete-backups "../../../fsx/latest/ONTAPGuide/using-backups.md#delete-backups") in the _FSx for ONTAP User Guide_.

## Configuration settings (deployment on

Windows)

The following configuration settings are applied when deploying a SQL Server Always On
application with Launch Wizard.

| Setting                                                                                                                                                                                                                                | Applies to                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Current EC2Launch v2 and SSM Agent                                                                                                                                                                                                     | Windows Server 2022 and 2019\*                           |
| Current EC2Launch and SSM Agent                                                                                                                                                                                                        | Windows Server 2019\*                                    |
| Current AWS PV, ENA, and NVMe drivers                                                                                                                                                                                                  | Windows Server 2022 and 2019                             |
| Current SRIOV drivers                                                                                                                                                                                                                  | Windows Server 2022 and 2019                             |
| Microsoft SQL Server:<br>Latest service pack<br>SQL Service configured to start automatically<br>SQL Service running<br>`BUILTIN\Administrators` added to the<br>`SysAdmin` server role<br>TCP port `1433` and UDP port `1434`<br>open | Windows Server 2022 and 2019                             |
| Allow ICMP traffic through the firewall                                                                                                                                                                                                | Windows Server 2022 and 2019                             |
| Allow RDP traffic through host firewall                                                                                                                                                                                                | Windows Server 2022 and 2019                             |
| `RealTimeIsUniversal` registry key set                                                                                                                                                                                                 | Windows Server 2022 and 2019                             |
| SQL Server FCI                                                                                                                                                                                                                         | Windows Server 2022 and 2019<br>SQL Server 2022 and 2019 |

\* Windows Server 2019 can use either EC2Launch or EC2Launch v2 depending on
what is configured in the AMI. For more information, see [Supported AMIs](../../../AWSEC2/latest/UserGuide/ec2launch-v2.md "../../../AWSEC2/latest/UserGuide/ec2launch-v2.md").

###### The following AMI settings can impact the Launch Wizard deployment:

**System Time**

**RealTimeIsUniversal**. If disabled, Windows
system time drifts when the time zone is set to a value other than
UTC.

**Windows Firewall**

In most cases, Launch Wizard configures the correct protocols and ports. However,
custom Windows Firewall rules could impact the cluster service. To ensure
that your custom AMI works with Launch Wizard, see [Service overview and network port requirements for
Windows](https://support.microsoft.com/en-us/help/832017/service-overview-and-network-port-requirements-for-windows "https://support.microsoft.com/en-us/help/832017/service-overview-and-network-port-requirements-for-windows").

**Remote Desktop**

**Service Start**. Remote Desktop service
must be enabled.

**Remote Desktop Connections**. Must be
enabled.

**Network Interface**

**DHCP Service Startup**. DHCP service should
be enabled.

**DHCP on Ethernet**. DHCP should be
enabled.

**Microsoft SQL Server**

**TCPIP**. Must be enabled for protocols in
SQL Configuration Manager.

**PowerShell**

**Execution Policy**. The execution policy in
all AWS license-included AMIs is set to `Unrestricted`. We
recommend that you set this policy to `Unrestricted` when you set
up SQL Server Always On Availability Groups using Launch Wizard. You can change the
policy when setup is complete.
