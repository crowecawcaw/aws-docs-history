

# CloudWatch pipelines configuration for Tenable Vulnerability Management
<a name="tenable-pipeline-setup"></a>

Collects vulnerability management data from Tenable using API key authentication.

Configure the Tenable Vulnerability Management source with the following parameters:

```
source:
  tenable_vulnerabilitymanagement:
    authentication:
      access_key: "${{aws_secrets:<secret-name>:access_key}}"
      secret_key: "${{aws_secrets:<secret-name>:secret_key}}"
    range: "P30D"
```Parameters

`authentication.access_key` (required)  
The Tenable API access key, stored in AWS Secrets Manager.

`authentication.secret_key` (required)  
The Tenable API secret key, stored in AWS Secrets Manager.

`range` (optional)  
The historical time period for backfilling data. Uses ISO 8601 duration format. Minimum is `P1D`, maximum is `P90D`. Default is `P30D`.