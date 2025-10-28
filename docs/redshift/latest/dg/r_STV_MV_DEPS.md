Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_MV_DEPS

The STV_MV_DEPS table shows the dependencies of materialized views on other
materialized views within Amazon Redshift.

For more information about materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md "materialized-view-overview.md").

STV_MV_DEPS is visible to all users. Superusers can see all rows; regular users can
only list materialized views residing in schemas they have access to. For more
information, see [Visibility
of data insystem tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name       | Data type | Description                                                                |
| ----------------- | --------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------- | -------------- | ----------- | -------------- | ------ | ------- |
| db_name           | char(128) | The database that contains the specified materialized view.                |
| schema            | char(128) | The schema of the materialized view.                                       |
| name              | char(128) | The name of the materialized view.                                         |
| ref_schema        | char(128) | The materialized view schema on which this materialized view depends.      |
| ref_name          | char(128) | The name of the materialized view on which this materialized view depends. |
| ref_database_name | char(128) | The name of the database on which this materialized view depends.          | ## Sample query The following query returns an output row that indicates that the materialized view `mv_over_foo` uses the materialized view `mv_foo` in its definition as a dependency. ``` CREATE SCHEMA test_ivm_setup; CREATE TABLE test_ivm_setup.foo(a INT); CREATE MATERIALIZED VIEW test_ivm_setup.mv_foo AS SELECT _ FROM test_ivm_setup.foo; CREATE MATERIALIZED VIEW test_ivm_setup.mv_over_foo AS SELECT _ FROM test_ivm_setup.mv_foo; SELECT \* FROM stv_mv_deps; db_name | schema | name | ref_schema | ref_name | ref_database_name ---------+-----------------+-------------+----------------+----------+------------------ dev | test_ivm_setup | mv_over_foo | test_ivm_setup | mv_foo | dev ``` |
