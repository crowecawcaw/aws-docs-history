# Using queries to filter log entries

You can use CloudWatch queries to filter and identify log entries for Transfer Family. This section
contains some examples.

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. You can create queries or rules.
   - To create a **Logs Insights** query, choose
     **Logs Insights** from the left navigation panel,
     and then enter the details for your query.
   - To create a **Contributor Insights** rule, choose
     Insights > Contributor Insights from the left navigation panel and then
     enter the details for your rule.

3. Run the query or rule that you created.

View the top authentication failure
contributors

In your structured logs, an authentication failure log entry looks similar to the
following:

```
{
  "method":"password",
  "activity-type":"AUTH_FAILURE",
  "source-ip":"999.999.999.999",
  "resource-arn":"arn:aws:transfer:us-east-1:999999999999:server/s-0123456789abcdef",
  "message":"Invalid user name or password",
  "user":"exampleUser"
}
```

Run the following query to view the top contributors to authentication
failures.

```
filter @logStream = 'ERRORS'
| filter `activity-type` = 'AUTH_FAILURE'
| stats count() as AuthFailures by user, method
| sort by AuthFailures desc
| limit 10
```

Rather than using **CloudWatch Logs Insights**, you can create a
**CloudWatch Contributors Insights** rule to view authentication
failures. Create a rule similar to the following.

```
{
    "AggregateOn": "Count",
    "Contribution": {
        "Filters": [
            {
                "Match": "$.activity-type",
                "In": [
                    "AUTH_FAILURE"
                ]
            }
        ],
        "Keys": [
            "$.user"
        ]
    },
    "LogFormat": "JSON",
    "Schema": {
        "Name": "CloudWatchLogRule",
        "Version": 1
    },
    "LogGroupARNs": [
        "arn:aws:logs:us-east-1:999999999999:log-group:/customer/structured_logs"
    ]
}
```

View log entries where a file was opened

In your structured logs, a file read log entry looks similar to the following:

```
{
  "mode":"READ",
  "path":"/fs-0df669c89d9bf7f45/avtester/example",
  "activity-type":"OPEN",
  "resource-arn":"arn:aws:transfer:us-east-1:999999999999:server/s-0123456789abcdef",
  "session-id":"0049cd844c7536c06a89"
}
```

Run the following query to view log entries that indicate a file was opened.

```
filter `activity-type` = 'OPEN'
| display @timestamp, @logStream, `session-id`, mode, path

```
