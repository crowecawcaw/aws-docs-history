# CloudWatch pipelines configuration for Jamf Pro

Collects device inventory data from Jamf Pro using OAuth 2.0 Client Credentials authentication through the Jamf Pro API.

Configure the Jamf Pro source with the following parameters:

```
source:
  jamf_pro:
    hostname: "yourcompany.jamfcloud.com"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`hostname` (required)

The Jamf Pro instance hostname (for example, `yourcompany.jamfcloud.com`).

`authentication.oauth2.client_id` (required)

The Jamf Pro API Client ID, stored in AWS Secrets Manager.

`authentication.oauth2.client_secret` (required)

The Jamf Pro API Client Secret, stored in AWS Secrets Manager.
