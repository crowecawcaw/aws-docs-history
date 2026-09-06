

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_GEOGRAPHY\_COLUMNS
<a name="r_SVV_GEOGRAPHY_COLUMNS"></a>

Use SVV\_GEOGRAPHY\_COLUMNS to view the list of GEOGRAPHY columns in your data warehouse. This list of columns includes columns from datashares.

SVV\_GEOGRAPHY\_COLUMNS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SVV_GEOGRAPHY_COLUMNS-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| f\_table\_catalog | varchar(128) | The name of the database where the table with the GEOGRAPHY column exists. | 
| f\_table\_schema | varchar(128) | The name of the schema where the table with the GEOGRAPHY column exists. | 
| f\_table\_name | varchar(128) | The name of the table where the GEOGRAPHY column exists. | 
| f\_geography\_column | varchar(128) | The name of the GEOGRAPHY column. | 
| coord\_dimension | integer | The number of dimensions of the GEOGRAPHY data. | 
| srid | integer | The spatial reference system identifier (SRID) of the GEOGRAPHY data. | 
| type | varchar(128) | The spatial geography data type name. | 

## Sample query
<a name="r_SVV_GEOGRAPHY_COLUMNS-sample-query"></a>

The following example displays the result of the SVV\_GEOGRAPHY\_COLUMNS.

```
SELECT * FROM svv_geography_columns;

f_table_catalog  | f_table_schema  | f_table_name  | f_geography_column  | coord_dimension | srid |  type
-----------------+-----------------+---------------+---------------------+-----------------+------+--------------
dev              | public          | spatial_test  | test_geography      | 2               | 0    | GEOGRAPHY
```