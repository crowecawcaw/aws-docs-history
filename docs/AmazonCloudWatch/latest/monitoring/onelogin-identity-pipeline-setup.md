

# CloudWatch pipelines configuration for OneLogin Identity
<a name="onelogin-identity-pipeline-setup"></a>

Collects event logs from OneLogin using OAuth2 authentication.

Configure the OneLogin Identity source with the following parameters:

```
source:
  onelogin_identity:
    range: "P7D"
    subdomain: "<your-subdomain>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```Parameters

`range` (optional)  
For pulling historical logs. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for the last 21 hours). The default is 0 hours, and the maximum is 90 days.

`subdomain` (required)  
Your OneLogin account subdomain. Must be alphanumeric with hyphens only, between 1–35 characters.

`authentication.oauth2.client_id` (required)  
OAuth2 client ID for OneLogin Events API authentication.

`authentication.oauth2.client_secret` (required)  
OAuth2 client secret for OneLogin Events API authentication.

**Note**  
The `client_id` and `client_secret` values are retrieved from AWS Secrets Manager. The above parameter information can be obtained from the API credentials generated while setting up your OneLogin application.