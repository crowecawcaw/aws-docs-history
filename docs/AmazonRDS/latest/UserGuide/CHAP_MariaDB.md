# Amazon RDS for MariaDB

Amazon RDS supports several versions of MariaDB for DB instances. For complete information about the supported versions, see [MariaDB on Amazon RDS versions](MariaDB.Concepts.md "MariaDB.Concepts.md").

To create a MariaDB DB instance, use the Amazon RDS management tools or interfaces. You can
then use the Amazon RDS tools to perform management actions for the DB instance. These include
actions such as the following:

- Reconfiguring or resizing the DB instance
- Authorizing connections to the DB instance
- Creating and restoring from backups or snapshots
- Creating Multi-AZ secondaries
- Creating read replicas
- Monitoring the performance of your DB instance
  To store and access the data in your DB instance, use standard MariaDB utilities and
  applications.

MariaDB is available in all of the AWS Regions.
For more information about AWS Regions, see
[Regions, Availability Zones, and Local Zones](Concepts.md "Concepts.md").

You can use Amazon RDS for MariaDB databases to build HIPAA-compliant applications.
You can store healthcare-related information,
including protected health information (PHI),
under a Business Associate Agreement (BAA) with AWS.
For more information, see
[HIPAA compliance](https://aws.amazon.com/compliance/hipaa-compliance/ "https://aws.amazon.com/compliance/hipaa-compliance/").
AWS Services in Scope have been fully assessed by a third-party auditor
and result in a certification, attestation of compliance, or Authority to Operate (ATO).
For more information, see
[AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

Before creating a DB instance, complete the steps in [Setting up your Amazon RDS environment](CHAP_SettingUp.md "CHAP_SettingUp.md"). When you create a DB instance, the RDS master user
gets DBA privileges, with some limitations. Use this account for
administrative tasks such as creating additional database accounts.

You can create the following:

- DB instances
- DB snapshots
- Point-in-time restores
- Automated backups
- Manual backups
  You can use DB instances running MariaDB inside a virtual private cloud (VPC) based on Amazon VPC. You can
  also add features to your MariaDB DB instance by enabling various options. Amazon RDS supports
  Multi-AZ deployments for MariaDB as a high-availability, failover solution.

###### Important

To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances. It also
restricts access to certain system procedures and tables that need advanced privileges. You can access your
database using standard SQL clients such as the mysql client. However, you can't access the host directly by using
Telnet or Secure Shell (SSH).

###### Topics

- [MariaDB feature support on Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md")
- [MariaDB on Amazon RDS versions](MariaDB.Concepts.md "MariaDB.Concepts.md")
- [Connecting to your MariaDB DB instance](USER_ConnectToMariaDBInstance.md "USER_ConnectToMariaDBInstance.md")
- [Securing MariaDB DB instance connections](securing-mariadb-connections.md "securing-mariadb-connections.md")
- [Improving query performance for RDS for MariaDB with Amazon RDS Optimized Reads](rds-optimized-reads-mariadb.md "rds-optimized-reads-mariadb.md")
- [Improving write performance with Amazon RDS
  Optimized Writes for MariaDB](rds-optimized-writes-mariadb.md "rds-optimized-writes-mariadb.md")
- [Upgrades of the MariaDB DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Upgrading a MariaDB DB snapshot engine
  version](mariadb-upgrade-snapshot.md "mariadb-upgrade-snapshot.md")
- [Importing data into an Amazon RDS for MariaDB DB
  instance](MariaDB.Procedural.md "MariaDB.Procedural.md")
- [Working with MariaDB replication in Amazon RDS](USER_MariaDB.md "USER_MariaDB.md")
- [Options for MariaDB database engine](Appendix.MariaDB.md "Appendix.MariaDB.md")
- [Parameters for MariaDB](Appendix.MariaDB.md "Appendix.MariaDB.md")
- [Migrating data from a MySQL DB snapshot to a MariaDB DB instance](USER_Migrate_MariaDB.md "USER_Migrate_MariaDB.md")
- [MariaDB on Amazon RDS SQL reference](Appendix.MariaDB.md "Appendix.MariaDB.md")
- [Local time zone for MariaDB DB instances](MariaDB.Concepts.md "MariaDB.Concepts.md")
- [Known issues and limitations for RDS for MariaDB](CHAP_MariaDB.md "CHAP_MariaDB.md")
