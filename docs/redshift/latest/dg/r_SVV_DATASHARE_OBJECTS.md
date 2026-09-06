

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_DATASHARE\_OBJECTS
<a name="r_SVV_DATASHARE_OBJECTS"></a>

Use SVV\_DATASHARE\_OBJECTS to view a list of objects in all datashares created on the cluster or shared with the cluster. 

SVV\_DATASHARE\_OBJECTS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

For information about viewing a list of datashares, see [SVV\_DATASHARES](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_DATASHARES.html).

## Table columns
<a name="r_SVV_DATASHARE_OBJECTS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| share\_type | varchar(8) | The type of the specified datashare. Possible values are OUTBOUND and INBOUND. | 
| share\_name | varchar(128) | The name of the datashare. | 
| object\_type | varchar(64) | The type of a specified object. Possible values are schemas, tables, views, late binding views, materialized views, and functions. | 
| object\_name | varchar(512) | The name of the object. The object name extends to include the schema name, such as schema1.t1. | 
| producer\_account | varchar(16) | The ID for the datashare producer account. | 
| producer\_namespace | varchar(64) | The unique cluster identifier for the datashare producer cluster. | 
| include\_new | boolean | The property that specifies whether to add any future tables, views, or SQL user-defined functions (UDFs) created in the specified schema to the datashare. This parameter is only relevant for OUTBOUND datashares and only for schema types in the datashare. | 

## Sample query
<a name="r_SVV_DATASHARE_OBJECTS-sample-query"></a>

The following examples return the output for SVV\_DATASHARE\_OBJECTS.

```
SELECT share_type,
    btrim(share_name)::varchar(16) AS share_name,
    object_type,
    object_name
FROM svv_datashare_objects
WHERE share_name LIKE 'tickit_datashare%'
AND object_name LIKE '%tickit%'
ORDER BY object_name
LIMIT 5;

 share_type |     share_name     | object_type |          object_name
------------+--------------------+-------------+---------------------------------
 OUTBOUND   |  tickit_datashare  |    table    |  public.tickit_category_redshift
 OUTBOUND   |  tickit_datashare  |    table    |  public.tickit_date_redshift
 OUTBOUND   |  tickit_datashare  |    table    |  public.tickit_event_redshift
 OUTBOUND   |  tickit_datashare  |    table    |  public.tickit_listing_redshift
 OUTBOUND   |  tickit_datashare  |    table    |  public.tickit_sales_redshift
```

```
SELECT * FROM SVV_DATASHARE_OBJECTS WHERE share_name like 'sales%';

share_type | share_name | object_type | object_name  | producer_account |          producer_namespace          | include_new
-----------+------------+-------------+--------------+------------------+--------------------------------------+-------------
 OUTBOUND  | salesshare | schema      | public       | 123456789012     | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d |      t
 OUTBOUND  | salesshare | table       | public.sales | 123456789012     | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d |
```