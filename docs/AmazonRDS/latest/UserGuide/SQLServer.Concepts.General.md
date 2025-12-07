# Change data capture support for Microsoft SQL Server DB instances

Amazon RDS supports change data capture (CDC) for your DB instances running Microsoft SQL
Server. CDC captures changes that are made to the data in your tables, and stores
metadata about each change that you can access later. For more information, see [Change data capture](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server#Capture "https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server#Capture") in the Microsoft documentation.

Amazon RDS supports CDC for the following SQL Server editions and versions:

- Microsoft SQL Server Enterprise Edition (All versions)
- Microsoft SQL Server Standard Edition:

      + 2022
      + 2019
      + 2017
      + 2016 version 13.00.4422.0 SP1 CU2 and later

  To use CDC with your Amazon RDS DB instances, first enable or disable CDC at the database
  level by using RDS-provided stored procedures. After that, any user that has the
  `db_owner` role for that database can use the native Microsoft stored
  procedures to control CDC on that database. For more information, see [Using change data capture for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md").

You can use CDC and AWS Database Migration Service to enable ongoing replication from SQL Server DB
instances.
