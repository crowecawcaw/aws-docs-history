# Understanding IBM Db2 for z/OS to Amazon RDS for PostgreSQL conversion settings

###### Note

The AWS Management Console does not support creating migration projects in DMS Schema Conversion that use IBM Db2 for z/OS as a source data provider
with Amazon RDS for PostgreSQL as a target data provider. Use the AWS CLI or DMS Schema Conversion API instead.

IBM Db2 for z/OS to Amazon RDS for PostgreSQL conversion settings in DMS Schema Conversion include the following:

- **Comments in converted SQL code**: This
  setting includes comments in the converted code for the action items of the
  selected severity and higher. This setting supports the following values:
  - Errors only
  - Errors and warnings
  - All messages
