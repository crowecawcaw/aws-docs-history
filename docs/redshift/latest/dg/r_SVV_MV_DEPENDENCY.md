Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_MV_DEPENDENCY

The SVV_MV_DEPENDENCY table shows the dependencies of materialized views on other
materialized views within Amazon Redshift.

For more information about materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md "materialized-view-overview.md").

SVV_MV_DEPENDENCY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name             | Data type | Description                                                                   |
| ----------------------- | --------- | ----------------------------------------------------------------------------- |
| database_name           | char(128) | The database that contains the specified<br>materialized view.                |
| schema_name             | char(128) | The schema of the materialized view.                                          |
| name                    | char(128) | The name of the materialized view.                                            |
| dependent_database_name | char(128) | The materialized view database on which this<br>materialized view depends.    |
| dependent_schema_name   | char(128) | The materialized view schema on which this<br>materialized view depends.      |
| dependent_name          | char(128) | The name of the materialized view on which this<br>materialized view depends. |

## Sample query

The following query returns an output row that indicates that the materialized
view `mv_over_foo` uses the materialized view `mv_foo` in its
definition as a
dependency.

```
CREATE SCHEMA test_ivm_setup;
CREATE TABLE test_ivm_setup.foo(a INT);
CREATE MATERIALIZED VIEW test_ivm_setup.mv_foo AS SELECT * FROM test_ivm_setup.foo;
CREATE MATERIALIZED VIEW test_ivm_setup.mv_over_foo AS SELECT * FROM test_ivm_setup.mv_foo;

SELECT * FROM svv_mv_dependency;

 database_name | schema_name          | name        | dependent_database_name | dependent_schema_name     | dependent_name
---------------+----------------------+-------------+-------------------------+---------------------------+----------
 dev           | test_ivm_setup       | mv_over_foo |                     dev | test_ivm_setup            | mv_foo
```
