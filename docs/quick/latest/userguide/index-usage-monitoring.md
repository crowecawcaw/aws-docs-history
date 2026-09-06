

# Monitor index storage usage
<a name="index-usage-monitoring"></a>

Index usage logs provide visibility into how your Amazon Quick index storage is consumed across knowledge bases and Spaces, including file uploads. You can use these logs to track growth trends, identify the largest sources, detect unexpected spikes, and plan capacity.

Before you query index usage data, you must configure `INDEX_USAGE_LOGS` delivery. For instructions on setting up delivery, see [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md).

## Log schema
<a name="index-usage-monitoring-schema"></a>

Each index usage log event includes the common fields that are shared across all Amazon Quick log types, such as `resource_arn`, `event_timestamp`, `log_type`, `account_id`, and `user_arn`. The event also includes the following index-specific fields:


**Index usage log fields**  

| Field | Type | Description | 
| --- | --- | --- | 
| consumed\_index\_size | Integer | Total size (in bytes) consumed by the entire index. This is the authoritative total. | 
| source\_type | String | SPACE or KB. | 
| source\_name | String | Display name of the Space or knowledge base. | 
| source\_arn | String | Full ARN of the source. | 
| consumed\_source\_size | Integer | Size (in bytes) consumed by this individual source. | 
| consumed\_source\_doc\_count | Integer | Number of documents in this source. | 

**Note**  
Events are published per source on change. Not all sources emit events every day. To reconstruct the current state, use the most recent event per `source_arn`.

## CloudWatch Logs Insights queries
<a name="index-usage-monitoring-queries"></a>

The following CloudWatch Logs Insights queries help you analyze index usage data. All queries use the pattern `stats latest(field) by source_arn` to get the most recent state per source. The queries then aggregate as needed. Replace {{YOUR\_LOG\_GROUP}} with your log group name.

### Size by source type (knowledge bases compared to Spaces)
<a name="index-usage-query-kb-vs-spaces"></a>

Shows the total size split between knowledge bases and Spaces.

```
fields @timestamp, source_type, source_arn, consumed_source_size
| stats latest(consumed_source_size) as latest_size, latest(source_type) as type by source_arn
| stats sum(latest_size) as total_size by type
```

### Total index size over time
<a name="index-usage-query-total-over-time"></a>

Shows the index size trend by using the `consumed_index_size` field.

```
fields @timestamp, consumed_index_size
| stats latest(consumed_index_size) as total_index_size by bin(1d) as day
| sort day asc
```

### Top knowledge bases by size
<a name="index-usage-query-top-kb"></a>

Shows the top 20 knowledge bases ranked by size.

```
fields @timestamp, source_type, source_arn, source_name, consumed_source_size
| filter source_type = "KB"
| stats latest(consumed_source_size) as latest_size, latest(source_name) as name by source_arn
| sort latest_size desc
| limit 20
```

### Top Spaces by size
<a name="index-usage-query-top-spaces"></a>

Shows the top 20 Spaces ranked by size.

```
fields @timestamp, source_type, source_arn, source_name, consumed_source_size
| filter source_type = "SPACE"
| stats latest(consumed_source_size) as latest_size, latest(source_name) as name by source_arn
| sort latest_size desc
| limit 20
```

### All sources detail
<a name="index-usage-query-all-sources"></a>

Shows the latest state of every source with size, type, name, document count, and last update time.

```
fields @timestamp, source_type, source_name, consumed_source_size, consumed_source_doc_count, source_arn
| stats latest(consumed_source_size) as latest_size, latest(source_type) as type, latest(source_name) as name, latest(consumed_source_doc_count) as doc_count, latest(@timestamp) as last_updated by source_arn
| sort latest_size desc
| limit 100
```

### Top users by total size
<a name="index-usage-query-top-users"></a>

Shows the top 20 users ranked by total source size across all their sources.

```
fields @timestamp, user_arn, source_arn, consumed_source_size
| parse user_arn "*:user/*/*" as @prefix, @namespace, @username
| stats latest(consumed_source_size) as latest_size, latest(@username) as user by source_arn
| stats sum(latest_size) as total_size by user
| sort total_size desc
| limit 20
```

## Create a CloudWatch dashboard
<a name="index-usage-monitoring-dashboard"></a>

You can create a CloudWatch dashboard to visualize index usage metrics. Use the CloudWatch console to create a dashboard and add Logs Insights widgets by using the queries from the preceding section.

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch).

1. In the navigation pane, choose **Dashboards**.

1. Choose **Create dashboard** and enter a name (for example, `IndexUsageMetrics`).

1. Add widgets by using the **Logs** widget type. Select your index usage log group and paste the queries from the preceding section.

**Tip**  
Use the pie chart visualization for the source type breakdown. Use the line chart for size over time. Use the bar chart for top sources. The table visualization works well for the all-sources detail query.