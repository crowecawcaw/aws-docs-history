

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_QUERY\_METRICS
<a name="r_SVL_QUERY_METRICS"></a>

The SVL\_QUERY\_METRICS view shows the metrics for completed queries. This view is derived from the [STL\_QUERY\_METRICS](r_STL_QUERY_METRICS.md) system table. Use the values in this view as an aid to determine threshold values for defining query monitoring rules. For more information, see [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md).

SVL\_QUERY\_METRICS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_QUERY\_DETAIL](SYS_QUERY_DETAIL.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_SVL_QUERY_METRICS-table-rows2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid  | integer  | ID of the user that ran the query that generated the entry.  | 
| query | integer  | Query ID. The query column can be used to join other system tables and views. | 
| service\_class  | integer  | ID for the WLM query queue (service class). Query queues are defined in the WLM configuration. Metrics are reported only for user-defined queues. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids). | 
| dimension  | varchar(24) | Dimension on which the metric is reported. Possible values are query, segment, and step.  | 
| segment  | integer  | Segment number. A query consists of multiple segments, and each segment consists of one or more steps. Query segments can run in parallel. Each segment runs in a single process. If the segment value is 0, metrics segment values are rolled up to the query level. | 
| step | integer  | ID for the type of step performed. The description for the step type is shown in the step\_label column. .  | 
| step\_label |  varchar(30) | Type of step performed.  | 
| query\_cpu\_time  | bigint  | CPU time used by the query, in seconds. CPU time is distinct from query run time.  | 
| query\_blocks\_read | bigint  | Number of 1 MB blocks read by the query.  | 
| query\_execution\_time | bigint  | Elapsed execution time for a query, in seconds. Execution time doesn’t include time spent waiting in a queue. See query\_queue\_time for the time queued.  | 
| query\_cpu\_usage\_percent | bigint  | Percent of CPU capacity used by the query. | 
| query\_temp\_blocks\_to\_disk  | bigint  | The amount of disk space used by a query to write intermediate results, in MB. | 
| segment\_execution\_time | bigint  | Elapsed execution time for a single segment, in seconds. | 
| cpu\_skew | numeric(38,2) | The ratio of maximum CPU usage for any slice to average CPU usage for all slices. This metric is defined at the segment level. | 
| io\_skew | numeric(38,2) | The ratio of maximum blocks read (I/O) for any slice to average blocks read for all slices.  | 
| scan\_row\_count | bigint | The number of rows in a scan step. The row count is the total number of rows emitted before filtering rows marked for deletion (ghost rows) and before applying user-defined query filters. | 
| join\_row\_count | bigint | The number of rows processed in a join step. | 
| nested\_loop\_join\_row\_count | bigint | The number of rows in a nested loop join. | 
| return\_row\_count | bigint | The number of rows returned by the query. | 
| spectrum\_scan\_row\_count | bigint | The number of rows scanned by Amazon Redshift Spectrum in Amazon S3. | 
| spectrum\_scan\_size\_mb | bigint | The amount of data, in MB, scanned by Amazon Redshift Spectrum in Amazon S3. | 
| query\_queue\_time | bigint  | The amount of time in seconds that the query was queued.  | 