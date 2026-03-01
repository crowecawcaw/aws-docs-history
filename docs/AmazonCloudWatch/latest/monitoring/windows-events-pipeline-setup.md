# CloudWatch pipelines configuration for Microsoft Windows Events

Collects log data from Microsoft Windows Event logs using OAuth2
authentication.

Configure the Microsoft Windows Event source with the following parameters:

```
source:
  microsoft_windows_event:
    tenant_id: "<example-tenant-ID>"
    workspace_id: "<example-workspace-ID>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`tenant_id` (required)

The Microsoft tenant ID for your organization.

`workspace_id` (required)

The Microsoft Log Analytics workspace ID.

`authentication.oauth2.client_id` (required)

OAuth2 client ID for Log Analytics workspace API
authentication.

`authentication.oauth2.client_secret` (required)

OAuth2 client secret for Log Analytics workspace API
authentication.
