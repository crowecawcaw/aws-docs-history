# Pipeline configuration for Okta Auth0

Collects log data from Okta Auth0 using OAuth2 authentication.

Configure the Okta Auth0 source with the following parameters:

```
source:
  okta_auth0:
    domain: "<example-domain-name>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`domain` (required)

The Okta Auth0 domain name for your organization.

`authentication.oauth2.client_id` (required)

OAuth2 client ID for Okta Auth0 API authentication.

`authentication.oauth2.client_secret` (required)

OAuth2 client secret for Okta Auth0 API authentication.
