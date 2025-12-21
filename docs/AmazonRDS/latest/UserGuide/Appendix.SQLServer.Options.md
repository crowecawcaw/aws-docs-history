# Support for Transparent Data Encryption in SQL Server

Amazon RDS supports using Transparent Data Encryption (TDE) to encrypt stored data on your DB instances running Microsoft SQL Server.
TDE automatically encrypts data before it is written to storage, and automatically decrypts data when the data is read from storage.

Amazon RDS supports TDE for the following SQL Server versions and editions:

- SQL Server 2022 Standard and Enterprise Editions
- SQL Server 2019 Standard and Enterprise Editions
- SQL Server 2017 Enterprise Edition
- SQL Server 2016 Enterprise Edition

###### Note

RDS for SQL Server does not support TDE for read-only databases.

Transparent Data Encryption for SQL Server provides encryption key management by using a two-tier key architecture. A certificate,
which is generated from the database master key, is used to protect the data encryption keys. The database encryption key performs
the actual encryption and decryption of data on the user database. Amazon RDS backs up and manages the database master key and the TDE
certificate.

Transparent Data Encryption is used in scenarios where you need to encrypt sensitive data. For example, you might want to provide
data files and backups to a third party, or address security-related regulatory compliance issues. You can't encrypt the system
databases for SQL Server, such as the `model` or `master` databases.

A detailed discussion of Transparent Data Encryption is beyond the scope of this guide,
but make sure that you understand the security strengths and weaknesses of each encryption
algorithm and key. For information about Transparent Data Encryption for SQL Server, see
[Transparent Data
Encryption (TDE)](http://msdn.microsoft.com/en-us/library/bb934049.aspx "http://msdn.microsoft.com/en-us/library/bb934049.aspx") in the Microsoft documentation.

###### Topics

- [Turning on TDE for RDS for SQL Server](#TDE.Enabling "#TDE.Enabling")
- [Encrypting data on RDS for SQL Server](TDE.md "TDE.md")
- [Backing up and restoring TDE certificates on RDS for SQL Server](TDE.md "TDE.md")
- [Backing up and restoring TDE certificates for on-premises databases](TDE.md "TDE.md")
- [Turning off TDE for RDS for SQL Server](TDE.md "TDE.md")

## Turning on TDE for RDS for SQL Server

To turn on Transparent Data Encryption for an RDS for SQL Server DB instance, specify the TDE
option in an RDS option group that's associated with that DB instance:

1. Determine whether your DB instance is already associated with an option group
   that has the TDE option. To view the option group that a DB instance is
   associated with, use the RDS console, the [describe-db-instance](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") AWS CLI command, or the API operation [DescribeDBInstances](../APIReference/API_DescribeDBInstances.md "../APIReference/API_DescribeDBInstances.md").
2. If the DB instance isn't associated with an option group that has TDE turned on, you have two choices. You can
   create an option group and add the TDE option, or you can modify the associated option group to add it.

###### Note

In the RDS console, the option is named `TRANSPARENT_DATA_ENCRYPTION`. In the AWS CLI and RDS API, it's
named `TDE`.

For information about creating or modifying an option group, see [Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md"). For information about adding an option to an option group, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption"). 3. Associate the DB instance with the option group that has the TDE option. For information about associating a DB
instance with an option group, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

### Option group considerations

The TDE option is a persistent option. You can't remove it from an option
group unless all DB instances and backups are no longer associated with the option
group. After you add the TDE option to an option group, the option group can be
associated only with DB instances that use TDE. For more information about
persistent options in an option group, see [Option groups overview](USER_WorkingWithOptionGroups.md#Overview.OptionGroups "USER_WorkingWithOptionGroups.md#Overview.OptionGroups").

Because the TDE option is a persistent option, you can have a conflict between the option group and an associated DB
instance. You can have a conflict in the following situations:

- The current option group has the TDE option, and you replace it with an
  option group that doesn't have the TDE option.
- You restore from a DB snapshot to a new DB instance that doesn't have an option group that contains the TDE
  option. For more information about this scenario, see [Considerations for option groups](USER_CopySnapshot.md#USER_CopySnapshot.Options "USER_CopySnapshot.md#USER_CopySnapshot.Options").

### SQL Server performance considerations

Using Transparent Data Encryption can affect the performance of a SQL Server DB
instance.

Performance for unencrypted databases can also be degraded if the databases are on a DB instance that has at least one
encrypted database. As a result, we recommend that you keep encrypted and unencrypted databases on separate DB
instances.
