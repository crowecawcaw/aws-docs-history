# Converting database schemas in AWS Schema Conversion Tool

You can use the AWS Schema Conversion Tool (AWS SCT) to convert your existing database schemas from one
database engine to another. Converting a database using the AWS SCT user interface can be
fairly simple, but there are several things to consider before you do the conversion.

For example, you can use AWS SCT to do the following:

- You can use AWS SCT to copy an existing on-premises database schema to an Amazon RDS DB instance
  running the same engine. You can use this feature to analyze potential cost savings
  of moving to the cloud and of changing your license type.
- In some cases, database features can't be converted to equivalent Amazon RDS features. If you host
  and self-manage a database on the Amazon Elastic Compute Cloud (Amazon EC2) platform, you can emulate these
  features by substituting AWS services for them.
- AWS SCT automates much of the process of converting your
  online transaction processing (OLTP) database schema to an
  Amazon Relational Database Service (Amazon RDS) MySQL DB instance, an Amazon Aurora DB cluster, or a PostgreSQL DB
  instance.
  The source and target database engines contain many different features and capabilities,
  and AWS SCT attempts to create an equivalent schema in your Amazon RDS DB instance
  wherever possible. If no direct conversion is possible, AWS SCT provides a list of
  possible actions for you to take.

###### Topics

- [Applying migration rules in AWS Schema Conversion Tool](CHAP_Converting.md "CHAP_Converting.md")
- [Converting schemas using AWS SCT](CHAP_Converting.md "CHAP_Converting.md")
- [Manually converting schemas in AWS SCT](CHAP_Converting.md "CHAP_Converting.md")
- [Updating and refreshing converted schemas in AWS SCT](CHAP_Converting.md "CHAP_Converting.md")
- [Saving and applying converted schemas in AWS SCT](CHAP_Converting.md "CHAP_Converting.md")
- [Comparing schemas in AWS Schema Conversion Tool](CHAP_Converting.md "CHAP_Converting.md")
- [Viewing related transformed objects in AWS Schema Conversion Tool](CHAP_Converting.md "CHAP_Converting.md")
  AWS SCT supports the following online transaction processing (OLTP) conversions.

| Source database                                            | Target database                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IBM Db2 for z/OS (version 12)                              | Amazon Aurora MySQL-Compatible Edition, Amazon Aurora PostgreSQL-Compatible Edition, MySQL, PostgreSQL                                                                                                                                                                                                               |
| IBM Db2 LUW (versions 9.1, 9.5, 9.7, 10.5, 11.1, and 11.5) | Aurora MySQL, Aurora PostgreSQL, MariaDB, MySQL, PostgreSQL                                                                                                                                                                                                                                                          |
| Microsoft Azure SQL Database                               | Aurora MySQL, Aurora PostgreSQL, MySQL, PostgreSQL                                                                                                                                                                                                                                                                   |
| Microsoft SQL Server (version 2008 R2 and higher)          | Aurora MySQL, Aurora PostgreSQL, Babelfish for Aurora PostgreSQL, MariaDB,<br>Microsoft SQL Server, MySQL, PostgreSQL                                                                                                                                                                                                |
| MySQL (version 5.5 and higher)                             | Aurora PostgreSQL, MySQL, PostgreSQL<br>You can migrate schema and data from MySQL to an Aurora MySQL<br>DB cluster without using AWS SCT. For more information, see [Migrating data to an Amazon Aurora DB cluster](../../../AmazonRDS/latest/UserGuide/Aurora.md "../../../AmazonRDS/latest/UserGuide/Aurora.md"). |
| Oracle (version 10.2 and higher)                           | Aurora MySQL, Aurora PostgreSQL, MariaDB, MySQL, Oracle, PostgreSQL                                                                                                                                                                                                                                                  |
| PostgreSQL (version 9.1 and higher)                        | Aurora MySQL, Aurora PostgreSQL, MySQL, PostgreSQL                                                                                                                                                                                                                                                                   |
| SAP ASE (12.5, 15.0, 15.5, 15.7, and 16.0)                 | Aurora MySQL, Aurora PostgreSQL, MariaDB, MySQL, PostgreSQL                                                                                                                                                                                                                                                          |

For information about converting a data warehouse schema, see [Converting data warehouse schemas to Amazon RDS using AWS SCT](CHAP_Converting.md "CHAP_Converting.md").

To convert your database schema to Amazon RDS, you take the following high-level steps:

- [Creating migration rules in AWS SCT](CHAP_Converting.md "CHAP_Converting.md") –
  Before you convert your schema with AWS SCT,
  you can set up rules that
  change the data type of columns,
  move objects from one schema to another,
  and change the names of objects.
- [Converting schemas using AWS SCT](CHAP_Converting.md "CHAP_Converting.md") –
  AWS SCT creates a local version of the converted schema for you to review,
  but it doesn't apply it to your target DB instance until you are ready.
- [Using the assessment report in the AWS Schema Conversion Tool](CHAP_AssessmentReport.md "CHAP_AssessmentReport.md") –
  AWS SCT creates a database migration assessment report
  that details the schema elements that can't be converted automatically.
  You can use this report to identify where you need to create a schema
  in your Amazon RDS DB instance that is compatible with your source database.
- [Converting schemas using AWS SCT](CHAP_Converting.md "CHAP_Converting.md") –
  If you have schema elements that can't be converted automatically, you have two
  choices: update the source schema and then convert again, or create equivalent
  schema elements in your target Amazon RDS DB instance.
- [Updating and refreshing converted schemas in AWS SCT](CHAP_Converting.md "CHAP_Converting.md") –
  You can update your AWS SCT project with the most
  recent schema from your source database.
- [Saving and applying converted schemas in AWS SCT](CHAP_Converting.md "CHAP_Converting.md") –
  When you are ready,
  have AWS SCT apply the converted schema
  in your local project to your target Amazon RDS DB instance.
