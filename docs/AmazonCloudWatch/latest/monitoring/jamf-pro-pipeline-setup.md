# CloudWatch pipelines configuration for Jamf Pro

Collects computer inventory data from Jamf Pro using OAuth2 Client Credentials authentication.

Configure the Jamf Pro source with the following parameters:

```
source:
  jamf_pro:
    hostname: "<<your-instance>>.jamfcloud.com"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:jamf-pro-credentials:client_id}}"
        client_secret: "${{aws_secrets:jamf-pro-credentials:client_secret}}"
```

###### Parameters

`hostname` (required)

The Jamf Pro instance hostname for your tenant. For Jamf Cloud deployments, this follows the format `<instance_name>.jamfcloud.com`. For on-premises deployments, use your self-hosted Jamf Pro server hostname. Do not include `https://`.

`authentication.oauth2.client_id` (required)

The OAuth2 Client ID generated in the Jamf Pro Console. Stored in AWS Secrets Manager.

`authentication.oauth2.client_secret` (required)

The OAuth2 Client Secret generated in the Jamf Pro Console. Stored in AWS Secrets Manager.

###### Note

The `client_id` and `client_secret` values are retrieved from AWS Secrets Manager. These credentials can be generated in the Jamf Pro Console under Settings > System > API Roles and Clients. The OAuth2 token is valid for 20 minutes and is automatically refreshed by the pipeline.
