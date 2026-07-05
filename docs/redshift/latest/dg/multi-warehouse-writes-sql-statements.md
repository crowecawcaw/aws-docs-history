Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Supported SQL statements for data sharing writes on consumers

The following Data Definition Language (DDL) statements are supported for data
sharing with writes:

- ALTER TABLE RENAME TO
- ALTER TABLE RENAME COLUMN TO
- ALTER TABLE ADD/DROP COLUMN
- ALTER SCHEMA RENAME TO
- { CREATE | DROP } SCHEMA
- { CREATE | DROP | SHOW } TABLE
- CREATE TABLE table\_name AS
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

- { GRANT | REVOKE } privilege\_name ON OBJECT\_TYPE object\_name TO consumer\_user
- SHOW GRANTS. For more information, see [SHOW GRANTS](r_SHOW_GRANTS.md "r_SHOW_GRANTS.md").
