# CloudWatch pipelines configuration for Entrust IDaaS

Collects identity and access management audit logs from Entrust IDaaS using OAuth2 authentication.

Configure the Entrust IDaaS source with the following parameters:

```
source:
  entrust_idaas:
    hostname: "<hostname>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`hostname` (required)

Entrust IDaaS tenant hostname (for example, `entrust.us.trustedauth.com`). Do not include the `https://` prefix.

`authentication.oauth2.client_id` (required)

OAuth2 client ID for Entrust IDaaS Administration API authentication.

`authentication.oauth2.client_secret` (required)

OAuth2 client secret for Entrust IDaaS Administration API authentication.

###### Note

The parameter information should correspond to values received in the Authenticating with Entrust IDaaS section.
