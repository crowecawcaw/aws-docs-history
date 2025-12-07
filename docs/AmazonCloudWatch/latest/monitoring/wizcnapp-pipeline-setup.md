# CloudWatch pipelines configuration for WIZ

Collects cloud-native application protection platform (CNAPP) data from Wiz
using OAuth2 authentication.

Configure the Wiz CNAPP source with the following parameters:

```
source:
  wiz_cnapp:
    region: "<example-region>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`region` (required)

Wiz region for your organization.

`authentication.oauth2.client_id` (required)

OAuth2 client ID for Wiz API authentication.

`authentication.oauth2.client_secret` (required)

OAuth2 client secret for Wiz API authentication.
