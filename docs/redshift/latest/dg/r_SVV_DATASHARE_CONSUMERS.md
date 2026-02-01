Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_DATASHARE_CONSUMERS

Use SVV_DATASHARE_CONSUMERS to view a list of consumers for a datashare created on a
cluster.

SVV_DATASHARE_CONSUMERS is visible to the following users:

- Superusers
- Datashare owners
- Users with ALTER or USAGE permissions on a datashare
  Other users can't see any rows. For information on the ALTER and USAGE permissions, see [GRANT](r_GRANT.md "r_GRANT.md").

## Table columns

| Column name        | Data type                   | Description                                                         |
| ------------------ | --------------------------- | ------------------------------------------------------------------- |
| share_name         | varchar(128)                | The name of the datashare.                                          |
| consumer_account   | varchar(16)                 | The account ID for the datashare consumer.                          |
| consumer_namespace | varchar(64)                 | The unique cluster identifier of the datashare consumer<br>cluster. |
| share_date         | timestamp without time zone | The date that the datashare was shared.                             |

## Sample query

The following example returns the output for SVV_DATASHARE_CONSUMERS.

```
SELECT count(*)
FROM svv_datashare_consumers
WHERE share_name LIKE 'tickit_datashare%';

1
```
