# Getting started with AWS Schema Conversion Tool

You can use the AWS Schema Conversion Tool (AWS SCT) to convert the schema for a source database.
The source database can be a self-managed engine running on-premises or on an Amazon EC2 instance.
You can convert your source schema to a schema for any supported database that is hosted
by AWS. The AWS SCT application provides a project-based user interface.

Almost all work you do with AWS SCT starts with the following steps:

1. Install AWS SCT. For more information, see [Installing and Configuring AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").
2. Install an AWS SCT agent, if needed. AWS SCT agents are only required for
   certain migration scenarios, such as between heterogeneous sources and targets.
   For more information, see [Migrating data from on-premises data warehouse to Amazon Redshift with AWS Schema Conversion Tool](agents.md "agents.md").
3. Familiarize yourself with the user interface of AWS SCT. For more information, see
   [Navigating the user interface of the AWS SCT](CHAP_UserInterface.md "CHAP_UserInterface.md").
4. Create an AWS SCT project. Connect to your source and target databases. For more information
   about connecting to your source database,
   see [Connecting to source databases with the AWS Schema Conversion Tool](CHAP_Source.md "CHAP_Source.md").
5. Create mapping rules. For more information about mapping rules,
   see [Mapping data types in the AWS Schema Conversion Tool](CHAP_Mapping.md "CHAP_Mapping.md").
6. Run and then review the Database Migration Assessment Report. For more information
   about the assessment report, see [Viewing the Assessment Report in AWS Schema Conversion Tool](CHAP_UserInterface.md "CHAP_UserInterface.md").
7. Convert the source database schemas. There are several aspects of the conversion you
   need to keep in mind, such as what to do with items that don't convert, and how to map items
   that should be converted a particular way. For more information about converting a
   source schema, see
   [Converting database schemas in AWS Schema Conversion Tool](CHAP_Converting.md "CHAP_Converting.md").

If you are converting a data warehouse schema, there are also aspects you need to consider
before doing the conversion. For more information, see
[Converting data warehouse schemas to Amazon RDS using AWS SCT](CHAP_Converting.md "CHAP_Converting.md"). 8. Applying the schema conversion to your target.
For more information about applying a source
schema conversion, see [Applying converted schemas](CHAP_UserInterface.md "CHAP_UserInterface.md"). 9. You can also use AWS SCT to convert SQL stored procedures and other
application code. For more information,
see [Converting application SQL using AWS SCT](CHAP_Converting.md "CHAP_Converting.md")
You can also use AWS SCT to migrate your data from a source database to an Amazon-managed
database. For examples, see [Migrating data from on-premises data warehouse to Amazon Redshift with AWS Schema Conversion Tool](agents.md "agents.md").
