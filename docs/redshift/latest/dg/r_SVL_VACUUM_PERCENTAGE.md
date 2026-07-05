Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVL\_VACUUM\_PERCENTAGE

The SVL\_VACUUM\_PERCENTAGE view reports the percentage of data blocks allocated to a
table after performing a vacuum. This percentage number shows how much disk space was
reclaimed. See the [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md")
command for more information about the vacuum utility.

SVL\_VACUUM\_PERCENTAGE is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_VACUUM\_HISTORY](SYS_VACUUM_HISTORY.md "SYS_VACUUM_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name | Data type | Description                                                                                                            |
| ----------- | --------- | ---------------------------------------------------------------------------------------------------------------------- |
| xid         | bigint    | Transaction ID for the vacuum statement.                                                                               |
| table\_id   | integer   | Table ID for the vacuumed table.                                                                                       |
| percentage  | bigint    | Percentage of data blocks after a vacuum (relative<br>to the number of blocks in the table before the vacuum was run). |

## Sample query

The following query displays the percentage for a specific operation on table
100238:

```
select * from svl_vacuum_percentage
where table_id=100238 and xid=2200;

xid  | table_id | percentage
-----+----------+------------
1337 |   100238 |         60
(1 row)
```

After this vacuum operation, the table contained 60 percent of the original
blocks.
