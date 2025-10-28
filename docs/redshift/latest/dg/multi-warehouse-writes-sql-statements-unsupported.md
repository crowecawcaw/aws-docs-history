Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Unsupported SQL

statements for data sharing writes on consumers

The following aren't supported:

- Multi-statement queries to consumer warehouses when writing to
  producers.
- Multi-statement queries to consumer warehouses in a different database, if the
  previous command is a read statement.
- Object references other than three-dot notations, such as one.dot or two.dot
  notations, if not connected to shared database.
- Concurrency scaling queries writing from consumers to producers.
- Auto-copy jobs writing from consumers to producers.
- Streaming jobs writing from consumers to producers.
- Consumers creating zero-ETL integration tables on producer clusters. For more
  information about zero-ETL integrations, see [Working with zero-ETL
  integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md").
- Writing to a table with an interleaved sort key through a data share.
- Writing to a stored procedure through a data share.
- Writing to a SQL user-defined functions (UDF) through a data share. These
  include nested, Python, and Lambda UDFs.
- UPDATE, INSERT, or COPY statements on identity columns to consumer warehouses
  with more compute slices than producer.
- MERGE statements on non-RMS external tables to consumer warehouses, when
  writing to producers.
- CREATE TABLE statements with:
  - DEFAULT expression set to data type VARBYTE. The VARBYTE data type can't
    be implicitly converted to any other data type. For more information, see
    [CAST function](r_CAST_function.md "r_CAST_function.md").
  - AS OF SELECT statements with NULL parameter to consumer warehouses, when
    writing to producers.
