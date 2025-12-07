# CloudWatch pipelines configuration for Okta SSO

Collects log data from Okta SSO using OAuth2 authentication.

Configure the Okta SSO source with the following parameters:

```
source:
  okta_sso:
    domain: "<example-domain-name>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`domain` (required)

The Okta domain name for your organization.

`authentication.oauth2.client_id` (required)

OAuth2 client ID for Okta SSO API authentication.

`authentication.oauth2.client_secret` (required)

OAuth2 client secret for Okta SSO API authentication.
