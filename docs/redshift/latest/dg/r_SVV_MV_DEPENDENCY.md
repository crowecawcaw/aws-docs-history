

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_MV\_DEPENDENCY
<a name="r_SVV_MV_DEPENDENCY"></a>

The SVV\_MV\_DEPENDENCY table shows the dependencies of materialized views on other materialized views within Amazon Redshift. 

For more information about materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md).

SVV\_MV\_DEPENDENCY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SVV_MV_DEPENDENCY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| database\_name  | char(128)  | The database that contains the specified materialized view.  | 
| schema\_name  | char(128)  | The schema of the materialized view.  | 
| name  | char(128)  | The name of the materialized view.  | 
| dependent\_database\_name | char(128)  | The materialized view database on which this materialized view depends.  | 
| dependent\_schema\_name | char(128)  | The materialized view schema on which this materialized view depends.  | 
| dependent\_name | char(128)  | The name of the materialized view on which this materialized view depends. | 

## Sample query
<a name="r_SVV_MV_DEPENDENCY-sample-query"></a>

The following query returns an output row that indicates that the materialized view `mv_over_foo` uses the materialized view `mv_foo` in its definition as a dependency.

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