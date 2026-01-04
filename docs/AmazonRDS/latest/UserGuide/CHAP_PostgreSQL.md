# Amazon RDS for PostgreSQL

Amazon RDS supports DB instances running several versions of PostgreSQL. For a list of
available versions, see [Available PostgreSQL database
versions](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md").

You can create DB instances and DB snapshots, point-in-time restores and backups. DB
instances running PostgreSQL support Multi-AZ deployments, read replicas, Provisioned IOPS,
and can be created inside a virtual private cloud (VPC). You can also use Secure Socket
Layer (SSL) to connect to a DB instance running PostgreSQL.

Before creating a DB instance, make sure to complete the steps in [Setting up your Amazon RDS environment](CHAP_SettingUp.md "CHAP_SettingUp.md").

You can use any standard SQL client application to run commands for the instance from your
client computer. Such applications include pgAdmin, a popular Open Source administration and
development tool for PostgreSQL, or psql, a command line utility that is part of a
PostgreSQL installation. To deliver a managed service experience, Amazon RDS doesn't provide
host access to DB instances. Also, it restricts access to certain system procedures and
tables that require advanced privileges. Amazon RDS supports access to databases on a DB instance
using any standard SQL client application. Amazon RDS doesn't allow direct host access to a
DB instance by using Telnet or Secure Shell (SSH).

Amazon RDS for PostgreSQL is compliant with many industry standards. For example, you can use
Amazon RDS for PostgreSQL databases to build HIPAA-compliant applications and to store
healthcare-related information. This includes storage for protected health information (PHI)
under a completed Business Associate Agreement (BAA) with AWS. Amazon RDS for PostgreSQL also
meets Federal Risk and Authorization Management Program (FedRAMP) security requirements.
Amazon RDS for PostgreSQL has received a FedRAMP Joint Authorization Board (JAB) Provisional
Authority to Operate (P-ATO) at the FedRAMP HIGH Baseline within the AWS GovCloud (US) Regions.
For more information on supported compliance standards, see [AWS cloud compliance](https://aws.amazon.com/compliance/ "https://aws.amazon.com/compliance/").

To import PostgreSQL data into a DB instance, follow the information in the [Importing data into PostgreSQL on
Amazon RDS](PostgreSQL.Procedural.md "PostgreSQL.Procedural.md") section.

###### Important

If you encounter an issue with your RDS for PostgreSQL DB instance, your AWS support agent
might need more information about the health of your databases. The goal is to ensure
that AWS Support gets the required information as soon as possible.

You can use PG Collector to help gather valuable database information in a
consolidated HTML file. For more information on PG Collector, how to run it, and how to
download the HTML report, see [PG
Collector](https://github.com/awslabs/pg-collector "https://github.com/awslabs/pg-collector").

Upon successful completion, and unless otherwise noted, the script returns output in a
readable HTML format. The script is designed to exclude any data or security details
from the HTML that might compromise your business. It also makes no modifications to
your database or its environment. However, if you find any information in the HTML that
you are uncomfortable sharing, feel free to remove the problematic information before
uploading the HTML. When the HTML is acceptable, upload it using the attachments section
in the case details of your support case.

###### Topics

- [Common management tasks for
  Amazon RDS for PostgreSQL](CHAP_PostgreSQL.md "CHAP_PostgreSQL.md")
- [Working with the
  Database Preview environment](working-with-the-database-preview-environment.md "working-with-the-database-preview-environment.md")
- [Available PostgreSQL database
  versions](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md")
- [Understanding the
  RDS for PostgreSQL incremental release process](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md")
- [Supported
  PostgreSQL extension versions](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md")
- [Working with PostgreSQL
  features supported by Amazon RDS for PostgreSQL](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md")
- [Connecting to a DB instance running the
  PostgreSQL database engine](USER_ConnectToPostgreSQLInstance.md "USER_ConnectToPostgreSQLInstance.md")
- [Securing connections to
  RDS for PostgreSQL with SSL/TLS](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md")
- [Using Kerberos authentication with Amazon RDS for
  PostgreSQL](postgresql-kerberos.md "postgresql-kerberos.md")
- [Using a custom DNS server
  for outbound network access](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Upgrades of the RDS for PostgreSQL DB
  engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Upgrading a PostgreSQL DB snapshot
  engine version](USER_UpgradeDBSnapshot.md "USER_UpgradeDBSnapshot.md")
- [Working with read replicas for
  Amazon RDS for PostgreSQL](USER_PostgreSQL.Replication.md "USER_PostgreSQL.Replication.md")
- [Improving query performance for RDS for PostgreSQL with Amazon RDS Optimized Reads](USER_PostgreSQL.md "USER_PostgreSQL.md")
- [Importing data into PostgreSQL on
  Amazon RDS](PostgreSQL.Procedural.md "PostgreSQL.Procedural.md")
- [Exporting data from an RDS for PostgreSQL
  DB instance to Amazon S3](postgresql-s3-export.md "postgresql-s3-export.md")
- [Invoking an AWS Lambda function from an
  RDS for PostgreSQL DB instance](PostgreSQL-Lambda.md "PostgreSQL-Lambda.md")
- [Common DBA tasks for
  Amazon RDS for PostgreSQL](Appendix.PostgreSQL.md "Appendix.PostgreSQL.md")
- [Tuning with wait events for RDS for PostgreSQL](PostgreSQL.md "PostgreSQL.md")
- [Tuning RDS for PostgreSQL with Amazon DevOps Guru proactive insights](PostgreSQL.md "PostgreSQL.md")
- [Using PostgreSQL extensions with
  Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Working
  with the supported foreign data wrappers for Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Extensions.md "Appendix.PostgreSQL.CommonDBATasks.Extensions.md")
- [Working with Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension.md "PostgreSQL_trusted_language_extension.md")
