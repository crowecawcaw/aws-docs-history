# Monitoring data loading

Aurora PostgreSQL Limitless Database provides several ways to monitor data loading jobs:

- [Listing data loading jobs](#limitless-load.monitor-list "#limitless-load.monitor-list")
- [Viewing details of data loading jobs using the job ID](#limitless-load.monitor-describe "#limitless-load.monitor-describe")
- [Monitoring the Amazon CloudWatch log group](#limitless-load.monitor-cwl "#limitless-load.monitor-cwl")
- [Monitoring RDS events](#limitless-load.monitor-events "#limitless-load.monitor-events")

## Listing data loading jobs

You can connect to the cluster endpoint and use the `rds_aurora.limitless_data_load_jobs` view to list data loading
jobs.

```
postgres_limitless=> SELECT * FROM rds_aurora.limitless_data_load_jobs LIMIT 6;

    job_id     |  status   | message |     source_db_identifier      | source_db_name | full_load_complete_time |                                                                progress_details                                                                 |       start_time       |   last_updated_time    |  streaming_mode   | source_engine_type | ignore_primary_key_conflict | is_dryrun
---------------+-----------+---------+-------------------------------+----------------+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------------+-------------------+--------------------+-----------------------------+-----------
 1725697520693 | COMPLETED |         | persistent-kdm-auto-source-01 | postgres       | 2024-09-07 08:48:15+00  | {"FULL_LOAD": {"STATUS": "COMPLETED", "DETAILS": "9 of 9 tables loaded", "COMPLETED_AT": "2024/09/07 08:48:15+00", "RECORDS_MIGRATED": 600003}} | 2024-09-07 08:47:13+00 | 2024-09-07 08:48:15+00 | full_load         | aurora_postgresql  | t                           | f
 1725696114225 | COMPLETED |         | persistent-kdm-auto-source-01 | postgres       | 2024-09-07 08:24:20+00  | {"FULL_LOAD": {"STATUS": "COMPLETED", "DETAILS": "3 of 3 tables loaded", "COMPLETED_AT": "2024/09/07 08:24:20+00", "RECORDS_MIGRATED": 200001}} | 2024-09-07 08:23:56+00 | 2024-09-07 08:24:20+00 | full_load         | aurora_postgresql  | t                           | f
 1725696067630 | COMPLETED |         | persistent-kdm-auto-source-01 | postgres       | 2024-09-07 08:23:45+00  | {"FULL_LOAD": {"STATUS": "COMPLETED", "DETAILS": "6 of 6 tables loaded", "COMPLETED_AT": "2024/09/07 08:23:45+00", "RECORDS_MIGRATED": 400002}} | 2024-09-07 08:23:10+00 | 2024-09-07 08:23:45+00 | full_load         | aurora_postgresql  | t                           | f
 1725694221753 | CANCELED  |         | persistent-kdm-auto-source-01 | postgres       |                         | {}                                                                                                                                              | 2024-09-07 07:31:18+00 | 2024-09-07 07:51:49+00 | full_load_and_cdc | aurora_postgresql  | t                           | f
 1725691698210 | COMPLETED |         | persistent-kdm-auto-source-01 | postgres       | 2024-09-07 07:10:51+00  | {"FULL_LOAD": {"STATUS": "COMPLETED", "DETAILS": "1 of 1 tables loaded", "COMPLETED_AT": "2024/09/07 07:10:51+00", "RECORDS_MIGRATED": 100000}} | 2024-09-07 07:10:42+00 | 2024-09-07 07:10:52+00 | full_load         | aurora_postgresql  | t                           | f
 1725691695049 | COMPLETED |         | persistent-kdm-auto-source-01 | postgres       | 2024-09-07 07:10:48+00  | {"FULL_LOAD": {"STATUS": "COMPLETED", "DETAILS": "1 of 1 tables loaded", "COMPLETED_AT": "2024/09/07 07:10:48+00", "RECORDS_MIGRATED": 100000}} | 2024-09-07 07:10:41+00 | 2024-09-07 07:10:48+00 | full_load         | aurora_postgresql  | t                           | f
(6 rows)
```

Job records are deleted after 90 days.

## Viewing details of data loading jobs using the job ID

If you know a job ID, you can connect to the cluster endpoint and use the `rds_aurora.limitless_data_load_job_details` view to
see the details of that data loading job, including the table name, job status, and number of rows loaded. You can get the job ID in the
responses to the data loading start functions, or from the `rds_aurora.limitless_data_load_jobs` view.

```
postgres_limitless=> SELECT * FROM rds_aurora.limitless_data_load_job_details WHERE job_id='1725696114225';

job_id        | destination_table_name | destination_schema_name | start_time             | status    | full_load_rows | full_load_total_rows | full_load_complete_time | cdc_insert | cdc_update | cdc_delete
--------------+------------------------+-------------------------+------------------------+-----------+----------------+----------------------+-------------------------+------------+------------+------------
1725696114225 | standard_1             | public                  | 2024-09-07 08:23:57+00 | COMPLETED | 100000         | 100000               | 2024-09-07 08:24:08+00  | 0          | 0          | 0
1725696114225 | standard_2             | public                  | 2024-09-07 08:24:08+00 | COMPLETED | 100000         | 100000               | 2024-09-07 08:24:17+00  | 0          | 0          | 0
1725696114225 | standard_3             | public                  | 2024-09-07 08:24:18+00 | COMPLETED | 1              | 1                    | 2024-09-07 08:24:20+00  | 0          | 0          | 0
1725696114225 | standard_4             | public                  | 2024-09-07 08:23:58+00 | PENDING   | 0              | 0                    |                         | 0          | 0          | 0
(4 rows)
```

Job records are deleted after 90 days.

## Monitoring the Amazon CloudWatch log group

After the data loading job status changes to `RUNNING`, you can check the runtime progress using Amazon CloudWatch Logs.

###### To monitor CloudWatch log streams

Sign in to the AWS Management Console and open the CloudWatch console at
[https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").

1. Navigate to **Logs**, then **Log groups**.
2. Choose the **/aws/rds/aurora-limitless-database** log group.
3. Search for the log stream of your data loading job by **job_id**.

The log stream has the pattern **Data-Load-Job-`job_id`**. 4. Choose the log stream to see the log events.

Each log stream shows events containing the job status and the number of rows loaded to the Aurora PostgreSQL Limitless Database destination tables. If a data loading
job fails, an error log is also created that shows the failure status and the reason.

Job records are deleted after 90 days.

## Monitoring RDS events

The data loading job also publishes RDS events, for example when a job succeeds, fails, or is canceled. You can view the events from the
destination database.

For more information, see [DB shard group events](USER_Events.md#USER_Events.Messages.shard-group "USER_Events.md#USER_Events.Messages.shard-group").
