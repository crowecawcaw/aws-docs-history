# Viewing and managing scheduled

queries

The following information is available for each query:

**Name**

The unique name you assigned to the scheduled query. Select the name to
view detailed configuration and execution history.

**Creation date**

The date when the scheduled query was created, displayed in YYYY-MM-DD
format.

**Status of last run**

The execution status of the most recent query run. Possible values
include:

- **Complete** - The query executed successfully
  and results were delivered to all configured destinations.
- **Failed** - The query execution or result
  delivery failed. Check the execution history for error
  details.
- **Invalid Query** - The query is invalid and has syntactical issues
- **Timeout** - The query has timed out. A query times out automatically after 60 mins

**Last triggered time**

The date and time when the query was last executed, displayed in
YYYY-MM-DD HH:MM:SS format. Shows **Never** if the query
has not yet run.

**Repeating every**

The schedule frequency for the query. Shows **Custom**
for queries using cron expressions or specific frequency descriptions for
simpler schedules.

The **Scheduled queries** page provides an overview of all your scheduled queries, showing
their current status and execution history so that you can view, monitor, and manage all your scheduled queries from a centralized
location. Use this information to monitor query
performance, identify issues, and manage your automated log analysis workflows.

Console

###### To view scheduled queries (console)

1. Open the CloudWatch Logs console at [https://console.aws.amazon.com/cloudwatch/home#logsV2:](https://console.aws.amazon.com/cloudwatch/home#logsV2: "https://console.aws.amazon.com/cloudwatch/home#logsV2:").
2. In the navigation pane, choose **Scheduled
   queries**.

AWS CLI

###### To list scheduled queries (AWS CLI)

- Use the `list-scheduled-queries` command to list all
  scheduled queries:

```
aws logs list-scheduled-queries --max-results 10
```

API

###### To list scheduled queries (API)

- Use the `ListScheduledQueries` action to retrieve all
  scheduled queries:

```
{
    "maxResults": 10
}
```

The **Scheduled queries** page header shows the total number of scheduled queries in your account, helping
you track your usage and manage your automated log analysis workflows
effectively.
