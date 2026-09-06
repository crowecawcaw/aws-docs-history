

# Create a Log Alarm on high latency per endpoint
<a name="US_LogAlarmLatencyByEndpoint"></a>

You can create a multi-contributor Log Alarm that monitors average latency grouped by endpoint. The alarm transitions to `ALARM` state if any endpoint exceeds the latency threshold.

The following example creates a Log Alarm that enters `ALARM` state when any endpoint has average latency greater than 1000 ms in 3 out of 5 query executions.

```
aws cloudwatch put-log-alarm \
    --alarm-name "EndpointLatency" \
    --alarm-description "Alarm when any endpoint latency exceeds 1000ms" \
    --comparison-operator GreaterThanThreshold \
    --threshold 1000 \
    --query-results-to-evaluate 5 \
    --query-results-to-alarm 3 \
    --treat-missing-data missing \
    --alarm-actions "arn:aws:sns:{{region}}:{{account-id}}:{{topic-name}}" \
    --scheduled-query-configuration '{
        "QueryString": "parse @message /endpoint=(?<endpoint>\\S+).*latency=(?<latency>\\d+)/",
        "LogGroupIdentifiers": ["/aws/apigateway/{{my-api}}"],
        "ScheduledQueryRoleARN": "arn:aws:iam::{{account-id}}:role/{{ScheduledQueryRole}}",
        "AggregationExpression": "avg(latency) by endpoint",
        "ScheduleConfiguration": {
            "ScheduleExpression": "rate(5 minutes)",
            "StartTimeOffset": 300
        }
    }'
```

In this example, each unique value of `endpoint` becomes a contributor. If any contributor's average latency exceeds 1000 ms, the alarm transitions to `ALARM` state and sends a notification identifying which endpoint is breaching.