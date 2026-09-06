

# Amazon CloudWatch Logs
<a name="msk-data-delivery-iceberg-cw-logs"></a>

A Channel can publish operational logs to a Amazon CloudWatch Logs log group, including schema resolution events, delivery attempts and outcomes, and error details for failed deliveries.

**Enabling Amazon CloudWatch Logs** — specify the log destination when creating or updating a Channel:

```
aws kafka create-channel \
    --cluster-arn "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123" \
    --channel-name "orders-channel" \
    --topic-configuration-list '[ ... ]' \
    --iceberg-destination-configuration '{ ... }' \
    --logging-info '{
        "CloudWatchLogs": {
            "Enabled": true,
            "LogGroup": "/aws/msk/data-channel"
        }
    }'
```

**Required permissions for logging** — add to the service role:

```
{
    "Sid": "CloudWatchLogsAccess",
    "Effect": "Allow",
    "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
    ],
    "Resource": "arn:aws:logs:REGION:ACCOUNT_ID:log-group:/aws/msk/data-channel:*"
}
```

Logging also supports Amazon Data Firehose and Amazon S3 destinations; configure those as needed.