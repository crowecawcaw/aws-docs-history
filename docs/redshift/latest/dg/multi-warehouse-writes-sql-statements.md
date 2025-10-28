Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Supported SQL statements for

data sharing writes on consumers

The following Data Definition Language (DDL) statements are supported for data
sharing with writes:

- ALTER TABLE RENAME TO
- ALTER TABLE RENAME COLUMN TO
- ALTER TABLE ADD/DROP COLUMN
- ALTER SCHEMA RENAME TO
- { CREATE | DROP } SCHEMA
- { CREATE | DROP | SHOW } TABLE
- CREATE TABLE table_name AS
- BEGIN | START TRANSACTION
- END | COMMIT | ROLLBACK
- TRUNCATE
  The following Data Manipulation Language (DML) statements are supported for data
  sharing with writes:

- SELECT
- INSERT
- INSERT INTO SELECT
- UPDATE
- DELETE
- MERGE
- COPY without COMPUPDATE
  The following analyze statements are supported for data sharing with writes:

- ANALYZE. The consumer runs USER ANALYZE and sends the stats to the producer.
- Analyze activated by CTAS/COPY running on the consumer. This iIncludes
  multiplexing for small consumers.
- Auto-analyze run on the producer after COPY.
  The following permission statements are supported for data sharing with
  writes:

- { GRANT | REVOKE } privilege_name ON OBJECT_TYPE object_name TO consumer_user
- SHOW GRANTS. For more information, see [SHOW GRANTS](r_SHOW_GRANTS.md "r_SHOW_GRANTS.md").
