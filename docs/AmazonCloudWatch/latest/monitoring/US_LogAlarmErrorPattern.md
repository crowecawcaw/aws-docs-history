

# Create a Log Alarm on error patterns
<a name="US_LogAlarmErrorPattern"></a>

You can create a Log Alarm that monitors your logs for error patterns and sends a notification when the error count exceeds a threshold.

The following example creates a Log Alarm that transitions to `ALARM` state when more than 10 ERROR messages appear in 3 out of 5 query executions.

```
aws cloudwatch put-log-alarm \
    --alarm-name "LambdaErrors" \
    --alarm-description "Alarm when Lambda error count exceeds 10" \
    --comparison-operator GreaterThanThreshold \
    --threshold 10 \
    --query-results-to-evaluate 5 \
    --query-results-to-alarm 3 \
    --treat-missing-data notBreaching \
    --alarm-actions "arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}}" \
    --scheduled-query-configuration '{
        "QueryString": "fields @timestamp, @message | filter @message like /ERROR/",
        "LogGroupIdentifiers": ["/aws/lambda/{{my-function}}"],
        "ScheduledQueryRoleARN": "arn:aws:iam::{{account-id}}:role/{{ScheduledQueryRole}}",
        "AggregationExpression": "count(*)",
        "ScheduleConfiguration": {
            "ScheduleExpression": "rate(5 minutes)",
            "StartTimeOffset": 300
        }
    }'
```