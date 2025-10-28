# Best practice 4.5 – Track data and database changes

Data auditing involves monitoring a database to track the
actions of a user or process, and to audit the changes that
have occurred to the data.

## Suggestion 4.5.1 – Database triggering for data auditing

A database trigger is procedural code that is
automatically run in response to certain events on a
particular table or view in a database. Database triggers
can then be used to update an audit table with the changes
that have occurred. The types of information that should
be included in the auditing process include: the original
and updated value of what has been updated, the process or
stored procedure that made the update, and the time and
date the update occurred.

## Suggestion 4.5.2 – Enable advanced auditing

If your database engine supports auditing as a native
feature, you should enable the feature to record and audit
database events such as connections, disconnections,
tables queried, or types of queries issued.

## Suggestion 4.5.3 – AWS Lake Formation time travel queries

Apache Iceberg and Apache Hudi provide a high-performance data lake table format that works just like a SQL table. Iceberg and Hudi make it simple to manage your data lake information and support SQL type analytics. Data that is managed by Iceberg or Hudi is version-controlled, therefore there is a complete history of all data updates. A good example is if you need to know the status of an individual at a certain time, then a time travel query allows you to select a date range to return the value that existed at that time, rather than the current value.

For more details, see [Use the AWS Glue connector to read and write Apache Iceberg tables with ACID transactions and perform time travel](https://aws.amazon.com/blogs/big-data/use-aws-glue-to-read-and-write-apache-iceberg-tables-with-acid-transactions-and-perform-time-travel/ "https://aws.amazon.com/blogs/big-data/use-aws-glue-to-read-and-write-apache-iceberg-tables-with-acid-transactions-and-perform-time-travel/").

## Suggestion 4.5.4 – Change Data Capture (CDC)

CDC records `INSERT`s, `UPDATE`s, and `DELETE`s
applied to relational database tables, and makes a log available of which relational
database objects changed, where, and when. These change tables contain columns that
reflect the column structure of the source table you have chosen to track, along with the
metadata required to understand the changes that have been made.

For more details, refer to the following information:

- AWS CloudTrail -
  [Secure
  Standardized Logging](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- Amazon RDS Aurora -
  [Advanced
  Auditing with an Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md")
- Amazon RDS Aurora -
  [Configuring
  an audit log to capture database activities for Amazon RDS](https://aws.amazon.com/blogs/database/configuring-an-audit-log-to-capture-database-activities-for-amazon-rds-for-mysql-and-amazon-aurora-with-mysql-compatibility/ "https://aws.amazon.com/blogs/database/configuring-an-audit-log-to-capture-database-activities-for-amazon-rds-for-mysql-and-amazon-aurora-with-mysql-compatibility/")
- AWS Database Migration Service (AWS DMS)
  [AWS Database Migration Service](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/")
