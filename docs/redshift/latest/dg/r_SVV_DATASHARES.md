

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_DATASHARES
<a name="r_SVV_DATASHARES"></a>

Use SVV\_DATASHARES to view a list of datashares created on the cluster, and datashares shared with the cluster. 

SVV\_DATASHARES is visible to the following users:
+ Superusers
+ Datashare owners
+ Users with ALTER or USAGE permissions on a datashare

Other users can't see any rows. For information on the ALTER and USAGE permissions, see [GRANT](r_GRANT.md).

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW DATASHARES](r_SHOW_DATASHARES.md) command for datashare discovery. SHOW DATASHARES is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_DATASHARES-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| share\_name | varchar(128) | The name of a datashare. | 
| share\_id | integer | The ID of the datashare.  | 
| share\_owner | integer | The owner of the datashare.  | 
| source\_database | varchar(128) | The source database for this datashare. | 
| consumer\_database | varchar(128) | The consumer database that is created from this datashare. | 
| share\_type | varchar(8) | The type of the datashare. Possible values are INBOUND and OUTBOUND. | 
| createdate | timestamp without time zone  | The date when datashare was created. | 
| is\_publicaccessible | boolean | The property that specifies whether a datashare can be shared to a publicly accessible cluster. | 
| share\_acl | varchar(256)  | The string that defines the permissions for the specified user or user group for the datashare. | 
| producer\_account | varchar(16) | The ID for the datashare producer account. | 
| producer\_namespace | varchar(64) | The unique cluster identifier for the datashare producer cluster.  | 
| managed\_by | varchar(64) | The property that specifies the AWS service that manages the datashare.  | 

## Usage notes
<a name="r_SVV_DATASHARES-usage"></a>

**Retrieving additional metadata** – Using the integer returned in the `share_owner` column, you can join with `usesysid` in [SVL\_USER\_INFO](r_SVL_USER_INFO.md) to get data about the datashare owner. This includes the name and additional properties.

## Sample query
<a name="r_SVV_DATASHARES-sample-query"></a>

The following example returns the output for SVV\_DATASHARES.

```
SELECT share_owner, source_database, share_type, is_publicaccessible
FROM svv_datashares
WHERE share_name LIKE 'tickit_datashare%'
AND source_database = 'dev';
    
  share_owner | source_database | share_type  | is_publicaccessible  
--------------+-----------------+-------------+----------------------
     100      |      dev        |   OUTBOUND  |        True
(1 rows)
```

The following example returns the output for SVV\_DATASHARES for outbound datashares.

```
SELECT share_name, share_owner, btrim(source_database), btrim(consumer_database), share_type, is_publicaccessible, share_acl, btrim(producer_account), btrim(producer_namespace), btrim(managed_by) FROM svv_datashares WHERE share_type = 'OUTBOUND';
                
   share_name   | share_owner | source_database | consumer_database | share_type | is_publicaccessible | share_acl | producer_account|         producer_namespace           | managed_by 
----------------+-------------+-----------------+-------------------+------------+---------------------+-----------+-----------------+--------------------------------------+------------
    salesshare  |      1      |       dev       |                   |  OUTBOUND  |        True         |           |   123456789012  | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d |    
 marketingshare |      1      |       dev       |                   |  OUTBOUND  |        True         |           |   123456789012  | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d |
```

The following example returns the output for SVV\_DATASHARES for inbound datashares.

```
SELECT share_name, share_owner, btrim(source_database), btrim(consumer_database), share_type, is_publicaccessible, share_acl, btrim(producer_account), btrim(producer_namespace), btrim(managed_by) FROM svv_datashares WHERE share_type = 'INBOUND';
                
  share_name    | share_owner | source_database | consumer_database | share_type | is_publicaccessible | share_acl | producer_account |         producer_namespace           | managed_by 
----------------+-------------+-----------------+-------------------+------------+---------------------+-----------+------------------+--------------------------------------+------------
  salesshare    |             |                 |                   |  INBOUND   |       False         |           |  123456789012    | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | 
 marketingshare |             |                 |                   |  INBOUND   |       False         |           |  123456789012    | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | ADX
```