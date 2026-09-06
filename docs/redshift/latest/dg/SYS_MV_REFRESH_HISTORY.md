

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_MV\_REFRESH\_HISTORY
<a name="SYS_MV_REFRESH_HISTORY"></a>

The results include information about the refresh history of all materialized views. The results include the refresh type, such as manual or auto, and the status of the most recent refresh. 

SYS\_MV\_REFRESH\_HISTORY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_MV_REFRESH_HISTORY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | The identifier of the user who submitted the refresh. | 
| session\_id | integer | The process identifier for the process running the materialized view refresh. | 
| transaction\_id | bigint | The transaction identifier. | 
| database\_name | char(128) | The database that contains the materialized view. | 
| schema\_name | char(128) | The schema of the materialized view. | 
| mv\_id | bigint | Object ID of the materialized view. | 
| mv\_name | char(128) | The materialized view name. | 
| refresh\_type | char(32) | The type of refresh, such as manual or auto. | 
| status | text | The status of the refresh. For detailed information about statuses, see the status column for [SVL\_MV\_REFRESH\_STATUS](r_SVL_MV_REFRESH_STATUS.md). | 
| start\_time | timestamp | The start time of the refresh. | 
| end\_time | timestamp | The end time of the refresh. | 
| duration | bigint | The amount of time in microseconds it took to refresh the materialized view. | 
| consumer\_account | char(12) | The AWS account ID of the consumer cluster that initiated the refresh. This field is populated when the refresh is initiated from a consumer cluster in a data sharing setup.  | 
| consumer\_region | char(32) | The AWS Region of the consumer cluster that initiated the refresh. This field is populated when the refresh is initiated from a consumer cluster in a data sharing setup.  | 
| consumer\_namespace | char(36) | The namespace identifier of the consumer cluster that initiated the refresh. This field is populated when the refresh is initiated from a consumer cluster in a data sharing setup.  | 

## Sample queries
<a name="SYS_MV_REFRESH_HISTORY-sample-queries"></a>

The following query shows the refresh history for materialized views.

```
SELECT user_id, 
     session_id, 
     transaction_id, 
     database_name, 
     schema_name, 
     mv_id, 
     mv_name,
     refresh_type,
     status,
     start_time,
     end_time,
     duration,
     consumer_account,
     consumer_region,
     consumer_namespace
     from sys_mv_refresh_history;
```

The query returns the following sample output:

```
 user_id | session_id | transaction_id | database_name | schema_name                | mv_id  |  mv_name           |  refresh_type  |  status                                                                                              |  start_time                |  end_time                  |  duration | consumer_account | consumer_region | consumer_namespace
---------+------------+----------------+---------------+----------------------------+--------+--------------------+----------------+------------------------------------------------------------------------------------------------------+----------------------------+----------------------------+-----------+------------------+-----------------+------------------------------------
       1 | 1073815659 |          15066 | dev           | test_stl_mv_refresh_schema | 203762 | mv_incremental     | Manual         | MV was already updated                                                                               | 2023-10-26 15:59:20.952179 | 2023-10-26 15:59:20.952866 |      687 |                  |                 |
       1 | 1073815659 |          15068 | dev           | test_stl_mv_refresh_schema | 203771 | mv_nonincremental  | Manual         | MV was already updated                                                                               | 2023-10-26 15:59:21.008049 | 2023-10-26 15:59:21.008658 |      609 |                  |                 |
       1 | 1073815659 |          15070 | ext_db        | producer_schema            | 203779 | producer_mv        | Manual         | Refresh successfully updated MV incrementally                                                        | 2023-10-26 15:59:21.064252 | 2023-10-26 15:59:21.064885 |      633 | 0123456789       | us-east-1       | 623d8ff2-4391-4381-83d7-177caa6767af
       1 | 1073815659 |          15074 | dev           | test_stl_mv_refresh_schema | 203762 | mv_incremental     | Manual         | Refresh successfully updated MV incrementally                                                        | 2023-10-26 15:59:29.693329 | 2023-10-26 15:59:43.482842 | 13789513 |                  |                 |
       1 | 1073815659 |          15076 | dev           | test_stl_mv_refresh_schema | 203771 | mv_nonincremental  | Manual         | Refresh successfully recomputed MV from scratch                                                      | 2023-10-26 15:59:43.550184 | 2023-10-26 15:59:47.880833 |  4330649 |                  |                 |
       1 | 1073815659 |          15078 | dev           | test_stl_mv_refresh_schema | 203779 | mv_refresh_error   | Manual         | Refresh failed due to an internal error                                                              | 2023-10-26 15:59:47.949052 | 2023-10-26 15:59:52.494681 |  4545629 |                  |                 |
       1 | 1073815659 |          15071 | dev           | test_stl_mv_refresh_schema | 203778 | mv_test            | Manual         | Cascade refresh failed because materialized view test_stl_mv_refresh_schema.child was not refreshed. | 2023-10-26 15:30:21.432252 | 2023-10-26 15:30:21.432252 |      532 |                  |                 |
       1 | 1073815659 |          15071 | dev           | test_stl_mv_refresh_schema | 203761 | child              | Manual         | Refresh failed due to an internal error.                                                             | 2023-10-26 15:30:21.432252 | 2023-10-26 15:30:21.432252 |      532 |                  |                 |
       1 | 1073815659 |          15069 | dev           | test_stl_mv_refresh_schema | 203778 | mv_test            | Manual         | Cascade refresh skipped because materialized view test_stl_mv_refresh_schema.child was not refreshed.| 2023-10-26 15:21:43.550369 | 2023-10-26 15:21:43.550369 |      633
       1 | 1073815659 |          15069 | dev           | test_stl_mv_refresh_schema | 203761 | child              | Manual         | Refresh failed due to an internal error.                                                             | 2023-10-26 15:21:43.550369 | 2023-10-26 15:21:43.550369 |      633
(10 rows)
```