# Updating a scheduled query

Modify your scheduled query configuration to change the query string, schedule,
destinations, or execution role as your requirements evolve.

You can update any aspect of a scheduled query, including the query string, schedule
expression, destinations, and execution role. Changes take effect immediately for future
executions.

Console

###### To update a scheduled query (console)

1. In the CloudWatch Logs console, choose **Scheduled queries**.
2. Select the scheduled query you want to update.
3. Choose **Edit**.
4. Modify the configuration as needed.
5. Choose **Save changes**.

AWS CLI

###### To update a scheduled query (AWS CLI)

- Use the `update-scheduled-query` command to modify an existing scheduled query:

```
aws logs update-scheduled-query \
    --identifier "arn:aws:logs:us-east-1:111122223333:scheduled-query:5e0c0228-1c29-4d26-904f-59f1f1ba3c8f" \
    --description "Monitor for ERROR level logs daily" \
    --query-language "LogsQL" \
    --query-string "fields @timestamp, @message | filter @message like /ERROR/" \
    --log-group-identifiers "/aws/lambda/my-function-1" "/aws/lambda/my-function-2"
```

API

###### To update a scheduled query (API)

1. Use the `UpdateScheduledQuery` action to modify scheduled query configuration:

```
{
    "identifier": "arn:aws:logs:us-east-1:111122223333:scheduled-query:5e0c0228-1c29-4d26-904f-59f1f1ba3c8f",
    "queryString": "fields @timestamp, @message | filter @message like /WARNING|ERROR/ | stats count() by bin(5m)",
    "scheduleExpression": "cron(0 */2 * * ? *)",
    "state": "ENABLED"
}
```

2. To update multiple configuration parameters at once:

```
{
    "identifier": "arn:aws:logs:us-east-1:111122223333:scheduled-query:5e0c0228-1c29-4d26-904f-59f1f1ba3c8f",
    "queryString": "fields @timestamp, @message, @level | filter @level = 'ERROR'",
    "scheduleExpression": "cron(0 8,12,16 * * ? *)",
    "executionRoleArn": "arn:aws:iam::111122223333:role/UpdatedScheduledQueryRole",
    "logGroupIdentifiers": ["/aws/lambda/my-function", "/aws/lambda/another-function"],
    "destinationConfiguration": {
        "s3Configuration": {
            "destinationIdentifier": "s3://111122223333-sqn-results-bucket/processed-results",
            "roleArn": "arn:aws:iam::111122223333:role/Admin"
        }
    }
}
```
