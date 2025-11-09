Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_GEOMETRY_COLUMNS

Use SVV_GEOMETRY_COLUMNS to view the list of GEOMETRY columns in your data warehouse.
This list of columns includes columns from datashares.

SVV_GEOMETRY_COLUMNS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name       | Data type    | Description                                                               |
| ----------------- | ------------ | ------------------------------------------------------------------------- |
| f_table_catalog   | varchar(128) | The name of the database where the table with the GEOMETRY column exists. |
| f_table_schema    | varchar(128) | The name of the schema where the table with the GEOMETRY column exists.   |
| f_table_name      | varchar(128) | The name of the table where the GEOMETRY column exists.                   |
| f_geometry_column | varchar(128) | The name of the GEOMETRY column.                                          |
| coord_dimension   | integer      | The number of dimensions of the GEOMETRY data.                            |
| srid              | integer      | The spatial reference system identifier (SRID) of the GEOMETRY olumn.     |
| type              | varchar(128) | The spatial geometry type name.                                           |

## Sample query

The following example displays the result of the SVV_GEOMETRY_COLUMNS.

```
`SELECT * FROM svv_geometry_columns;`
`f_table_catalog | f_table_schema | f_table_name | f_geometry_column | coord_dimension | srid | type
-----------------+-----------------+---------------+---------------------+-----------------+------+--------------
dev | public | accomodations | shape | 2 | 0 | GEOMETRY
dev | public | zipcode | wkb_geometry | 2 | 0 | GEOMETRY`
```
