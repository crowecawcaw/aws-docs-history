

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVCS\_CONCURRENCY\_SCALING\_USAGE
<a name="r_SVCS_CONCURRENCY_SCALING_USAGE"></a>

Records the usage periods for concurrency scaling. Each usage period is a consecutive duration where an individual concurrency scaling cluster is actively processing queries.

SVCS\_CONCURRENCY\_SCALING\_USAGE This table is visible to superusers. The database's superuser can choose to open it up to all users. 

## Table columns
<a name="r_SVCS_CONCURRENCY_SCALING_USAGE-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| start\_time | timestamp without time zone | When the usage period starts. | 
| end\_time | timestamp without time zone | When the usage period ends. | 
| queries | bigint | Number of queries run during this usage period. | 
| usage\_in\_seconds  | numeric(27,0)  | Total seconds in this usage period. | 

## Sample queries
<a name="r_SVCS_CONCURRENCY_SCALING_USAGE-sample-queries"></a>

To view the usage duration in seconds for a specific period, enter the following query: 

```
select * from svcs_concurrency_scaling_usage order by start_time;

start_time | end_time | queries | usage_in_seconds
----------------------------+----------------------------+---------+------------------
2019-02-14 18:43:53.01063 | 2019-02-14 19:16:49.781649 | 48 | 1977
```