Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVCS_CONCURRENCY_SCALING_USAGE

Records the usage periods for concurrency scaling. Each usage period is a consecutive duration where an individual concurrency scaling cluster is actively processing queries.

SVCS_CONCURRENCY_SCALING_USAGE This table is visible to superusers. The database's superuser can choose to open it up to all users.

## Table

columns

| Column name      | Data type                   | Description                                     |
| ---------------- | --------------------------- | ----------------------------------------------- |
| start_time       | timestamp without time zone | When the usage period starts.                   |
| end_time         | timestamp without time zone | When the usage period ends.                     |
| queries          | bigint                      | Number of queries run during this usage period. |
| usage_in_seconds | numeric(27,0)               | Total seconds in this usage period.             |

## Sample

queries

To view the usage duration in seconds for a specific period, enter the following query:

```

select * from svcs_concurrency_scaling_usage order by start_time;

start_time | end_time | queries | usage_in_seconds
----------------------------+----------------------------+---------+------------------
2019-02-14 18:43:53.01063 | 2019-02-14 19:16:49.781649 | 48 | 1977

```
