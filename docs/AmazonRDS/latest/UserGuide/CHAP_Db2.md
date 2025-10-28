# Amazon RDS for Db2

Amazon RDS supports DB instances that run the following editions of IBM Db2:

- Db2 Standard Edition
- Db2 Advanced Edition
  Amazon RDS supports DB instances that run the following versions of Db2:

- Db2 11.5
  For more information about minor version support, see [Db2 on Amazon RDS versions](Db2.Concepts.md "Db2.Concepts.md").

Before creating a DB instance, complete the steps in the [Setting up your Amazon RDS environment](CHAP_SettingUp.md "CHAP_SettingUp.md") section of this user guide. When you create a DB
instance using your master user, the user gets `DBADM` authority, with some
limitations. Use this user for administrative tasks such as creating additional database
accounts. You can't use `SYSADM`, `SYSCTRL`, `SYSMAINT`
instance-level authority, or `SECADM` database-level authority.

You can create the following:

- DB instances
- DB snapshots
- Point-in-time restores
- Automated storage backups
- Manual storage backups
  You can use DB instances running Db2 inside a virtual private cloud (VPC). You can also
  add features to your Amazon RDS for Db2 DB instance by enabling various options. Amazon RDS supports
  Multi-AZ deployments for RDS for Db2 as a high availability, failover solution.

###### Important

To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB
instances. It also restricts access to certain system procedures and tables that need
elevated privileges. You can access your database using standard SQL clients such as IBM Db2 CLP. However, you
can't access the host directly by using Telnet or Secure Shell (SSH).

###### Topics

- [Overview of Db2 on Amazon RDS](db2-overview.md "db2-overview.md")
- [Prerequisites for creating an Amazon RDS for Db2 DB
  instance](db2-db-instance-prereqs.md "db2-db-instance-prereqs.md")
- [Multiple databases on an Amazon RDS for Db2 DB
  instance](db2-multiple-databases.md "db2-multiple-databases.md")
- [Connecting to your Db2 DB instance](USER_ConnectToDb2DBInstance.md "USER_ConnectToDb2DBInstance.md")
- [Securing Amazon RDS for Db2 DB instance
  connections](Db2.Concepts.md "Db2.Concepts.md")
- [Administering your Amazon RDS for Db2 DB
  instance](db2-administering-db-instance.md "db2-administering-db-instance.md")
- [Integrating an Amazon RDS for Db2 DB instance with
  Amazon S3](db2-s3-integration.md "db2-s3-integration.md")
- [Migrating data to Amazon RDS for Db2](db2-migrating-data-to-rds.md "db2-migrating-data-to-rds.md")
- [Amazon RDS for Db2 federation](db2-federation.md "db2-federation.md")
- [Working with replicas for Amazon RDS for Db2](db2-replication.md "db2-replication.md")
- [Options for Amazon RDS for Db2 DB instances](Db2.md "Db2.md")
- [External stored procedures for
  Amazon RDS for Db2](db2-external-stored-procedures.md "db2-external-stored-procedures.md")
- [Known issues and limitations for
  Amazon RDS for Db2](db2-known-issues-limitations.md "db2-known-issues-limitations.md")
- [Amazon RDS for Db2 stored procedure reference](db2-stored-procedures.md "db2-stored-procedures.md")
- [Amazon RDS for Db2 user-defined function
  reference](db2-user-defined-functions.md "db2-user-defined-functions.md")
- [Troubleshooting for Amazon RDS for Db2](db2-troubleshooting.md "db2-troubleshooting.md")
