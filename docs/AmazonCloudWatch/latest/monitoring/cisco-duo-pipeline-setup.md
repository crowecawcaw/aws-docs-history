

# CloudWatch pipelines configuration for Cisco Duo
<a name="cisco-duo-pipeline-setup"></a>

Collects log data from Cisco Duo using HMAC authentication through the Duo Admin API.

Configure the Cisco Duo source with the following parameters:

```
source:
  cisco_duo:
    api_host: "api-XXXXXXXX.duosecurity.com"
    authentication:
      hmac:
        integration_key: "${{aws_secrets:<secret-name>:integration_key}}"
        secret_key: "${{aws_secrets:<secret-name>:secret_key}}"
    range: "P30D"
```Parameters

`api_host` (required)  
The Duo API hostname for your organization (for example, `api-XXXXXXXX.duosecurity.com`).

`authentication.hmac.integration_key` (required)  
The Duo Admin API integration key, stored in AWS Secrets Manager.

`authentication.hmac.secret_key` (required)  
The Duo Admin API secret key, stored in AWS Secrets Manager.

`range` (optional)  
The historical time period for backfilling data. Uses ISO 8601 duration format. Minimum is `PT1H`, maximum is `P180D`. Default is `P180D`.