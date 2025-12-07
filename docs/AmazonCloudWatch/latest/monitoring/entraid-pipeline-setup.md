# CloudWatch pipelines configuration for Microsoft Entra

ID

Collects log data from Microsoft Entra ID (formerly Azure Active Directory)
using OAuth2 authentication.

Configure the Microsoft Entra ID source with the following parameters:

```
source:
  microsoft_entra_id:
    tenant_id: "<example-tenant-ID>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`tenant_id` (required)

The Microsoft Entra ID tenant ID for your organization.

`authentication.oauth2.client_id` (required)

OAuth2 client ID for Microsoft Graph API authentication.

`authentication.oauth2.client_secret` (required)

OAuth2 client secret for Microsoft Graph API
authentication.
