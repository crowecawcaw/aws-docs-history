

# CloudWatch pipelines configuration for Entrust IDaaS
<a name="entrust-idaas-pipeline-setup"></a>

Collects identity and access management audit logs from Entrust IDaaS using OAuth2 authentication.

Configure the Entrust IDaaS source with the following parameters:

```
source:
  entrust_idaas:
    hostname: "<hostname>"
    range: "P7D"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```Parameters

`hostname` (required)  
Entrust IDaaS tenant hostname (for example, `entrust.us.trustedauth.com`). Do not include the `https://` prefix.

`authentication.oauth2.client_id` (required)  
OAuth2 client ID for Entrust IDaaS Administration API authentication.

`authentication.oauth2.client_secret` (required)  
OAuth2 client secret for Entrust IDaaS Administration API authentication.

`range` (optional)  
The time range for log collection. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for 21 hours). Default is 0 hours, and the maximum is 90 days.

**Note**  
The parameter information should correspond to values received in the Authenticating with Entrust IDaaS section.