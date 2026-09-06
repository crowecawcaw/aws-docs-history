

# CloudWatch pipelines configuration for Slack Audit Log
<a name="slack-auditlog-pipeline-setup"></a>

Collects event logs from Slack using API token authentication.

Configure the Slack source with the following parameters:

```
source:
  slack_auditlogs:
    authentication:
        api_token: "${{aws_secrets:slack-account-credentials:apiToken}}"
    # Provide the time range (e.g., P7D for the last 7 days)
    range: "P7D"
```Parameters

`authentication` (required)  
Block containing Slack authentication settings. Contains the nested parameters listed in the following entry.    
`api_token` (required)  
Slack API token (`xoxp-...`) with the `auditlogs:read` scope. Typically sourced from AWS Secrets Manager using the `${{aws_secrets:<secret-name>:<key>}}` reference syntax.

`range` (optional)  
The time range for log collection. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for 21 hours). Default is 0 hours, and the maximum is 90 days.

**Note**  
The `api_token` value is retrieved from AWS Secrets Manager. The preceding parameter information can be obtained from the API credentials generated while setting up your Slack application.