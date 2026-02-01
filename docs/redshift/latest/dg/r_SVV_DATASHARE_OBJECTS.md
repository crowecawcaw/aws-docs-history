Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_DATASHARE_OBJECTS

Use SVV_DATASHARE_OBJECTS to view a list of objects in all datashares created on the
cluster or shared with the cluster.

SVV_DATASHARE_OBJECTS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For information about viewing a list of datashares, see [SVV_DATASHARES](r_SVV_DATASHARES.md "r_SVV_DATASHARES.md").

## Table columns

| Column name        | Data type    | Description                                                                                                                                                                                                                                                                 |
| ------------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| share_type         | varchar(8)   | The type of the specified datashare. Possible<br>values are OUTBOUND and INBOUND.                                                                                                                                                                                           |
| share_name         | varchar(128) | The name of the datashare.                                                                                                                                                                                                                                                  |
| object_type        | varchar(64)  | The type of a specified object. Possible values<br>are schemas, tables, views, late binding views, materialized views,<br>and functions.                                                                                                                                    |
| object_name        | varchar(512) | The name of the object. The object name extends to<br>include the schema name, such as schema1.t1.                                                                                                                                                                          |
| producer_account   | varchar(16)  | The ID for the datashare producer account.                                                                                                                                                                                                                                  |
| producer_namespace | varchar(64)  | The unique cluster identifier for the datashare producer<br>cluster.                                                                                                                                                                                                        |
| include_new        | boolean      | The property that specifies whether to add any<br>future tables, views, or SQL user-defined functions (UDFs) created<br>in the specified schema to the datashare. This parameter is only<br>relevant for OUTBOUND datashares and only for schema types in the<br>datashare. |

## Sample query

The following examples return the output for SVV_DATASHARE_OBJECTS.

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
