# Migrating an Oracle Database to PostgreSQL

Using this walkthrough, you can learn how to migrate an Oracle database to a PostgreSQL database using AWS Database Migration Service (AWS DMS) and the AWS Schema Conversion Tool (AWS SCT).

AWS DMS migrates your data from your Oracle source into your PostgreSQL target. AWS DMS also captures data manipulation language (DML) and [supported data definition language (DDL)](../userguide/CHAP_Introduction.md "../userguide/CHAP_Introduction.md") changes that happen on your source database and applies these changes to your target database. This way, AWS DMS keeps your source and target databases in sync with each other. To facilitate the data migration, AWS SCT creates the migrated schemas on the target database, including the tables and primary key indexes on the target if necessary.

AWS DMS doesn’t migrate your secondary indexes, sequences, default values, stored procedures, triggers, synonyms, views, and other schema objects not specifically related to data migration. To migrate these objects to your PostgreSQL target, use AWS SCT.

###### Topics

- [Prerequisites for migrating from an Oracle database to PostgreSQL](chap-rdsoracle2postgresql.md "chap-rdsoracle2postgresql.md")
- [Step-by-step Oracle database to PostgreSQL migration walkthrough](chap-rdsoracle2postgresql.md "chap-rdsoracle2postgresql.md")
- [Rolling Back the Migration](chap-oracle2postgresql.md "chap-oracle2postgresql.md")
- [Oracle database migration to PostgreSQL troubleshooting](chap-oracle2postgresql.md "chap-oracle2postgresql.md")
