Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_DATASHARE\_CONSUMERS

Use SVV\_DATASHARE\_CONSUMERS to view a list of consumers for a datashare created on a
cluster.

SVV\_DATASHARE\_CONSUMERS is visible to the following users:

- Superusers
- Datashare owners
- Users with ALTER or USAGE permissions on a datashare
  Other users can't see any rows. For information on the ALTER and USAGE permissions, see [GRANT](r_GRANT.md "r_GRANT.md").

## Table columns

| Column name         | Data type                   | Description                                                         |
| ------------------- | --------------------------- | ------------------------------------------------------------------- |
| share\_name         | varchar(128)                | The name of the datashare.                                          |
| consumer\_account   | varchar(16)                 | The account ID for the datashare consumer.                          |
| consumer\_namespace | varchar(64)                 | The unique cluster identifier of the datashare consumer<br>cluster. |
| share\_date         | timestamp without time zone | The date that the datashare was shared.                             |

## Sample query

The following example returns the output for SVV\_DATASHARE\_CONSUMERS.

```
SELECT count(*)
FROM svv_datashare_consumers
WHERE share_name LIKE 'tickit_datashare%';

1
```
