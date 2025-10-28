# Working with self-managed Active Directory with an Amazon RDS for SQL Server

DB instance

Amazon RDS for SQL Server seamlessly integrates with your self-managed Active Directory (AD) domain,
regardless of where your AD is hosted - whether in your data center, on Amazon EC2, or with other cloud providers.
This integration enables direct user authentication through NTLM or Kerberos protocols, eliminating the need
for complex intermediary domains or forest trusts. When you connect to your RDS SQL Server DB instance,
authentication requests are securely forwarded to your designated AD domain, maintaining your existing
identity management structure while leveraging Amazon RDS's managed database capabilities.

###### Topics

- [Region and version availability](#USER_SQLServer_SelfManagedActiveDirectory.RegionVersionAvailability "#USER_SQLServer_SelfManagedActiveDirectory.RegionVersionAvailability")
- [Requirements](USER_SQLServer_SelfManagedActiveDirectory.md "USER_SQLServer_SelfManagedActiveDirectory.md")
- [Considerations](#USER_SQLServer_SelfManagedActiveDirectory.Limitations "#USER_SQLServer_SelfManagedActiveDirectory.Limitations")
- [Setting up self-managed Active Directory](USER_SQLServer_SelfManagedActiveDirectory.md "USER_SQLServer_SelfManagedActiveDirectory.md")
- [Joining your DB instance to self-managed Active Directory](USER_SQLServer_SelfManagedActiveDirectory.md "USER_SQLServer_SelfManagedActiveDirectory.md")
- [Managing a DB instance in a self-managed Active Directory
  Domain](USER_SQLServer_SelfManagedActiveDirectory.md "USER_SQLServer_SelfManagedActiveDirectory.md")
- [Understanding
  self-managed Active Directory Domain membership](#USER_SQLServer_SelfManagedActiveDirectory.Understanding "#USER_SQLServer_SelfManagedActiveDirectory.Understanding")
- [Troubleshooting self-managed Active Directory](USER_SQLServer_SelfManagedActiveDirectory.md "USER_SQLServer_SelfManagedActiveDirectory.md")
- [Restoring a SQL Server DB instance and then adding it to a self-managed Active Directory domain](#USER_SQLServer_SelfManagedActiveDirectory.Restore "#USER_SQLServer_SelfManagedActiveDirectory.Restore")

## Region and version availability

Amazon RDS supports self-managed AD for SQL Server using NTLM and Kerberos
in all commercial AWS Regions and AWS GovCloud (US) Regions.

## Considerations

When adding an RDS for SQL Server DB instance to a self-managed AD, keep the consider the following:

- Your DB instances sync with AWS's NTP service and not the AD domain's time server.
  For database connections between linked SQL Server instances within your AD domain,
  you can only SQL authentication and not Windows authentication.
- Group Policy Object settings from your self-managed AD domain
  are not be propagated to your RDS for SQL Server instances.

## Understanding

self-managed Active Directory Domain membership

After you create or modify your DB instance while specifying AD details, the instance
becomes a member of the self-managed AD domain. The AWS console indicates the status
of the self-managed Active Directory domain membership for the DB instance. The status
of the DB instance can be one of the following:

- **joined** – The instance is a member of the AD domain.
- **joining** – The instance is in the process of becoming a member of the AD domain.
- **pending-join** – The instance membership is pending.
- **pending-maintenance-join** – AWS will attempt to make the instance a member of
  the AD domain during the next scheduled maintenance window.
- **pending-removal** – The removal of the instance from the AD domain is
  pending.
- **pending-maintenance-removal** – AWS will attempt to remove the instance from
  the AD domain during the next scheduled maintenance window.
- **failed** – A configuration problem has prevented the instance from joining the
  AD domain. Check and fix your configuration before reissuing the instance modify command.
- **removing** – The instance is being removed from the self-managed AD domain.

###### Important

A request to become a member of a self-managed AD domain can fail because of a
network connectivity issue. For example, you might create a DB instance or modify an
existing instance and have the attempt fail for the DB instance to become a member
of a self-managed AD domain. In this case, either reissue the command to create or
modify the DB instance or modify the newly created instance to join the self-managed
AD domain.

## Restoring a SQL Server DB instance and then adding it to a self-managed Active Directory domain

You can restore a DB snapshot or do point-in-time recovery (PITR) for a SQL Server DB instance and then add it to a self-managed Active Directory domain. Once
the DB instance is restored, modify the instance using the process explained in [Step 1: Create or modify a SQL Server DB instance](USER_SQLServer_SelfManagedActiveDirectory.md#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateModify "USER_SQLServer_SelfManagedActiveDirectory.md#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateModify") to add
the DB instance to a self-managed AD domain.
