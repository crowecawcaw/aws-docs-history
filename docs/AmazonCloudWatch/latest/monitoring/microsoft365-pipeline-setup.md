# CloudWatch pipelines configuration for Microsoft 365

Collects log data from Microsoft Office 365 Management API using OAuth2
authentication.

Configure the Microsoft Office 365 source with the following
parameters:

```
source:
  microsoft_office365:
    tenant_id: "<example-tenant-ID>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`tenant_id` (required)

The Microsoft Entra ID tenant ID for your Office 365
organization.

`authentication.oauth2.client_id` (required)

OAuth2 client ID for Microsoft Office 365 Management API
authentication. Can reference AWS Secrets Manager using
`${{aws_secrets:secret-name:key}}` syntax.

`authentication.oauth2.client_secret` (required)

OAuth2 client secret for Microsoft Office 365 Management API
authentication. Can reference AWS Secrets Manager using
`${{aws_secrets:secret-name:key}}` syntax.

###### Note

Store sensitive credentials like client IDs and secrets in AWS Secrets
Manager and reference them using the
`${{aws_secrets:secret-name:key}}` syntax in your
configuration.
