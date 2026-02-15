# Viewing scheduled query execution

history

Use the execution history to monitor the performance of your scheduled queries and
troubleshoot any issues with query execution or result delivery.

The execution history shows the status of each query run, including successful
executions, failures, and destination processing results. You can use this information
to identify patterns, diagnose problems, and verify that your queries are running as
expected.

Console

###### To view execution history (console)

1. In the CloudWatch Logs console, choose **Scheduled query**, **View scheduled queries**.
2. Select the scheduled query you want to examine.
3. Choose the **Execution history** tab.

AWS CLI

###### To view execution history (AWS CLI)

1. Use the `get-scheduled-query-history` command to retrieve execution history for a scheduled query:

```
aws logs get-scheduled-query-history \
    --identifier "DailyErrorMonitoring" \
    --start-time 1743379200 \
    --end-time 1743465600 \
    --max-results 10
```

2. To filter by execution status, add the `--execution-statuses` parameter:

```
aws logs get-scheduled-query-history \
    --identifier "DailyErrorMonitoring" \
    --start-time 1743379200 \
    --end-time 1743465600 \
    --max-results 1 \
    --execution-statuses "SUCCEEDED"
```

API

###### To view execution history (API)

- Use the `GetScheduledQueryHistory` action to retrieve execution history:

```
{
    "identifier": "DailyErrorMonitoring",
    "startTime": 1743379200,
    "endTime": 1743465600,
    "maxResults": 10,
    "executionStatuses": ["SUCCEEDED", "FAILED"]
}
```

The execution history displays:

- **Execution status** - Running, Complete, Failed, Timeout, or InvalidQuery
- **Triggered time** - When the query was executed
- **Destinations** - Processing status for each configured
  destination including S3 and EventBridge
- **Error messages** - Details about any failures in query execution or destination processing
