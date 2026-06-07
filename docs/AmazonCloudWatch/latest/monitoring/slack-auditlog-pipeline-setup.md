# CloudWatch pipelines configuration for Slack Audit Log

Collects event logs from Slack using API token authentication.

Configure the Slack source with the following parameters:

```
source:
  slack_auditlog:
    authentication:
        api_token: "${{aws_secrets:slack-account-credentials:apiToken}}"
    # Provide the time range (e.g., P7D for the last 7 days)
    backfill: "P7D"
    # Prevent data loss by only considering logs to be processed successfully after they are received by the sink
    acknowledgments: true
```

###### Parameters

`authentication` (required)

Block containing Slack authentication settings. Contains the nested
parameters listed in the following entry.

`api_token` (required)

Slack API token (`xoxp-...`) with the
`auditlogs:read` scope. Typically sourced from
AWS Secrets Manager using the
`${{aws_secrets:<secret-name>:<key>}}`
reference syntax.

`acknowledgments` (optional)

Prevents data loss by only considering logs successfully processed after
they are received by the sink. Accepts `true` or
`false`. Default: `true`.

`backfill` (optional)

Defines how far back to backfill audit logs on first run (or after state
reset). Uses ISO 8601 duration format (for example, `P7D` for
the last 7 days, `PT12H` for 12 hours). Must be a positive
duration or null; null disables backfill entirely. Slack's Audit Logs API
retains at most 90 days of history. Default: `P90D`.

###### Note

The `api_token` value is retrieved from AWS Secrets Manager. The preceding
parameter information can be obtained from the API credentials generated while
setting up your Slack application.
