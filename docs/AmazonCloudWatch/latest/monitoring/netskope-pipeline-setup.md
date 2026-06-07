# CloudWatch pipelines configuration for Netskope

Collects security events and alerts from Netskope using REST API v2 token-based
authentication.

Configure the Netskope source with the following parameters:

```
source:
  netskope:
    tenant_url: "<<your-tenant-url>>"
    authentication:
      api_token: "${{aws_secrets:netskope-account-credentials:apiToken}}"
```

###### Parameters

`tenant_url` (required)

Netskope tenant URL (for example, mycompany.goskope.com).

`authentication.api_token` (required)

REST API v2 token generated from the Netskope Service Account under
RBACv3.
