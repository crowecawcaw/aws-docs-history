Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_DATASHARES

Use SVV_DATASHARES to view a list of datashares created on the cluster, and datashares
shared with the cluster.

SVV_DATASHARES is visible to the following users:

- Superusers
- Datashare owners
- Users with ALTER or USAGE permissions on a datashare
  Other users can't see any rows. For information on the ALTER and USAGE permissions, see [GRANT](r_GRANT.md "r_GRANT.md").

## Table columns

| Column name         | Data type                   | Description                                                                                        |
| ------------------- | --------------------------- | -------------------------------------------------------------------------------------------------- |
| share_name          | varchar(128)                | The name of a datashare.                                                                           |
| share_id            | integer                     | The ID of the datashare.                                                                           |
| share_owner         | integer                     | The owner of the datashare.                                                                        |
| source_database     | varchar(128)                | The source database for this datashare.                                                            |
| consumer_database   | varchar(128)                | The consumer database that is created from this<br>datashare.                                      |
| share_type          | varchar(8)                  | The type of the datashare. Possible values are<br>INBOUND and OUTBOUND.                            |
| createdate          | timestamp without time zone | The date when datashare was created.                                                               |
| is_publicaccessible | boolean                     | The property that specifies whether a datashare<br>can be shared to a publicly accessible cluster. |
| share_acl           | varchar(256)                | The string that defines the permissions for the<br>specified user or user group for the datashare. |
| producer_account    | varchar(16)                 | The ID for the datashare producer account.                                                         |
| producer_namespace  | varchar(64)                 | The unique cluster identifier for the datashare producer<br>cluster.                               |
| managed_by          | varchar(64)                 | The property that specifies the AWS service that manages the datashare.                            |

## Usage notes

**Retrieving additional metadata** – Using the integer returned in the `share_owner` column, you can join with `usesysid`
in [SVL_USER_INFO](r_SVL_USER_INFO.md "r_SVL_USER_INFO.md") to get data about the datashare owner. This includes the name and
additional properties.

## Sample query

The following example returns the output for SVV_DATASHARES.

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

The following example returns the output for SVV_DATASHARES for outbound datashares.

```
SELECT share_name, share_owner, btrim(source_database), btrim(consumer_database), share_type, is_publicaccessible, share_acl, btrim(producer_account), btrim(producer_namespace), btrim(managed_by) FROM svv_datashares WHERE share_type = 'OUTBOUND';

   share_name   | share_owner | source_database | consumer_database | share_type | is_publicaccessible | share_acl | producer_account|         producer_namespace           | managed_by
----------------+-------------+-----------------+-------------------+------------+---------------------+-----------+-----------------+--------------------------------------+------------
    salesshare  |      1      |       dev       |                   |  OUTBOUND  |        True         |           |   123456789012  | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d |
 marketingshare |      1      |       dev       |                   |  OUTBOUND  |        True         |           |   123456789012  | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d |
```

The following example returns the output for SVV_DATASHARES for inbound datashares.

```
SELECT share_name, share_owner, btrim(source_database), btrim(consumer_database), share_type, is_publicaccessible, share_acl, btrim(producer_account), btrim(producer_namespace), btrim(managed_by) FROM svv_datashares WHERE share_type = 'INBOUND';

  share_name    | share_owner | source_database | consumer_database | share_type | is_publicaccessible | share_acl | producer_account |         producer_namespace           | managed_by
----------------+-------------+-----------------+-------------------+------------+---------------------+-----------+------------------+--------------------------------------+------------
  salesshare    |             |                 |                   |  INBOUND   |       False         |           |  123456789012    | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d |
 marketingshare |             |                 |                   |  INBOUND   |       False         |           |  123456789012    | 13b8833d-17c6-4f16-8fe4-1a018f5ed00d | ADX
```
