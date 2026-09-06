

# CloudWatch pipelines configuration for Proofpoint TAP
<a name="proofpoint-tap-pipeline-setup"></a>

Collects email security event data from Proofpoint TAP using HTTP Basic authentication.

Configure the Proofpoint TAP source with the following parameters:

```
source:
  proofpoint_tap:
    authentication:
      basic:
        service_principal: "${{aws_secrets:proofpoint-tap-account-credentials:servicePrincipal}}"
        secret: "${{aws_secrets:proofpoint-tap-account-credentials:secret}}"
    range: "P1D"
```Parameters

`authentication.basic.service_principal` (required)  
The Proofpoint TAP service principal for HTTP Basic authentication, stored in AWS Secrets Manager.

`authentication.basic.secret` (required)  
The Proofpoint TAP secret for HTTP Basic authentication, stored in AWS Secrets Manager.

`range` (optional)  
The historical time period for backfilling data. Uses ISO 8601 duration format. Minimum is `PT30S`, maximum is `P1D`. Default is `P1D`.