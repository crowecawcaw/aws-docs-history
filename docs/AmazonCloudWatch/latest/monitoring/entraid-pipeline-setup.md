

# CloudWatch pipelines configuration for Microsoft Entra ID
<a name="entraid-pipeline-setup"></a>

Collects log data from Microsoft Entra ID (formerly Azure Active Directory) using OAuth2 authentication.

Configure the Microsoft Entra ID source with the following parameters:

```
source:
  microsoft_entraid:
    tenant_id: "<example-tenant-ID>"
    delay_throttle: "PT15M"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```Parameters

`tenant_id` (required)  
The Microsoft Entra ID tenant ID for your organization.

`authentication.oauth2.client_id` (required)  
OAuth2 client ID for Microsoft Graph API authentication.

`authentication.oauth2.client_secret` (required)  
OAuth2 client secret for Microsoft Graph API authentication.

`delay_throttle` (optional)  
Specifies how far behind the current time the pipeline collects log records to compensate for event latency. Uses ISO 8601 duration format (for example, `PT15M` for 15 minutes). Minimum is `PT5M`, maximum is `PT60M`. Defaults to `PT10M`. Values outside this range are rejected. A longer delay gives late-arriving records more time to become available, but increases the time before logs appear in your destination. A shorter delay delivers logs sooner. For more information about event latency, see [Microsoft Entra ID log latency](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-log-latency) on the Microsoft Learn website.