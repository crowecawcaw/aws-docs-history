# Creating a scheduled query

Create a scheduled query that automatically runs CloudWatch Logs Insights queries and delivers
results to your chosen destinations.

## Prerequisites

Before creating a scheduled query, ensure you have the following:

- **Log groups** - One or more log groups
  containing the data you want to analyze
- **Execution IAM role** - An IAM role
  with the following permissions:
  - `logs:StartQuery` - Permission to start CloudWatch Logs Insights
    queries
  - `logs:GetQueryResults` - Permission to retrieve
    query results
  - `logs:DescribeLogGroups` - Permission to access log
    group information. This is only required for prefix based log groups for log group discovery

- **Destination permissions** - Additional
  IAM permissions for your chosen destination:
  - For Amazon S3 destinations: `s3:PutObject`

- **For AWS CLI and API usage** - Configured
  AWS credentials with permissions to call CloudWatch Logs APIs

For detailed IAM policy examples, see [Identity and access management for
Amazon CloudWatch Logs](auth-and-access-control-cwl.md "auth-and-access-control-cwl.md"). Also to be noted you can have only 1000 scheduled queries per account.

Console

###### To create a scheduled query (console)

1. Open the CloudWatch Logs console at [https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:logs-insights](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:logs-insights "https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:logs-insights").
2. In the navigation pane, choose **Logs
   Insights**.
3. Choose **Create scheduled query**.
4. In the **Query definition** section:
   1. For **Query language**, choose the
      query language to use from the list.
   2. For **Query string**, enter your
      CloudWatch Logs Insights query in the box.
   3. For **Log groups**, select the log
      groups to query from the list.

5. In the **Schedule setup** section:
   1. For **Schedule expression**,
      configure when the query runs. Choose from predefined
      options or enter a custom cron expression.
   2. For **Effective upon creation**,
      specify when the schedule becomes active. Choose to
      start immediately or at a specific date and time using
      YYYY/MM/DD format.
   3. For **Time range**, specify the
      lookback period for each query execution. Enter the
      duration in minutes that defines how far back from the
      execution time to query.
   4. For **Continue indefinitely**,
      specify when the schedule ends. Choose to run
      indefinitely or until a specific date and time using
      YYYY/MM/DD format.

6. The console displays the next three scheduled query runs based
   on your configuration, showing the exact dates and times in UTC
   when the query will execute.
7. In the **Post query results to S3 -
   optional** section (if using S3
   destination):
   1. For **Amazon S3 URI**, enter the Amazon S3
      bucket and prefix where results will be stored (for
      example,
      `s3://my-bucket/query-results/`).
   2. Choose **View Amazon S3** to open the Amazon S3
      console in a new tab and verify the bucket
      configuration.
   3. Choose **Browse Amazon S3** to select an
      existing Amazon S3 location using the Amazon S3 browser.

8. In the **IAM role for posting query results to
   Amazon S3** section:
   1. For **Select an IAM role**, choose
      an existing IAM role with the required policies, or
      choose **create a new role in IAM
      console** to create a new role.
   2. Use the search field to find and select the
      appropriate IAM role from the list.

9. In the **IAM role for scheduled query
   execution** section:
   1. For **Select an IAM role**, choose
      an existing IAM role with the required policies, or
      choose **create a new role in IAM
      console** to create a new role.
   2. Use the search field to find and select the
      appropriate IAM role from the list.

10. Choose **Create schedule** to create the
    scheduled query.

AWS CLI

###### To create a scheduled query (AWS CLI)

- Use the `create-scheduled-query` command to create
  a new scheduled query:

```
aws logs create-scheduled-query \
    --name "ErrorAnalysisQuery" \
    --query-language "CWLI" \
    --query-string "fields @timestamp, @message | filter @message like /ERROR/ | stats count() by bin(5m)" \
    --schedule-expression "cron(8 * * * ? *)" \
    --execution-role-arn "arn:aws:iam::123456789012:role/CloudWatchLogsScheduledQueryRole" \
    --log-group-identifiers "/aws/lambda/my-function" "/aws/apigateway/my-api" \
    --state "ENABLED"
```

API

###### To create a scheduled query (API)

- Use the `CreateScheduledQuery` action to create a
  new scheduled query. The following example creates a scheduled
  query that runs every hour:

```
{
    "name": "ErrorAnalysisQuery",
    "queryLanguage": "CWLI",
    "queryString": "fields @timestamp, @message | filter @message like /ERROR/ | stats count() by bin(5m)",
    "scheduleExpression": "cron(8 * * * ? *)",
    "executionRoleArn": "arn:aws:iam::123456789012:role/CloudWatchLogsScheduledQueryRole",
    "logGroupIdentifiers": ["/aws/lambda/my-function", "/aws/apigateway/my-api"],
    "state": "ENABLED"
}
```

After creating the scheduled query, you can view and manage it from the
**Scheduled queries** page and using ListScheduledQueries API, which shows all your scheduled
queries with their names, creation dates, status of last run, last triggered time,
and repeat frequency.
