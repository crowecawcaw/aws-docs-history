

# CloudWatch pipelines configuration for Qualys Policy Audit
<a name="qualys-policy-audit-pipeline-setup"></a>

Collects compliance posture findings from Qualys Policy Audit by using the PCRS streaming API with OAuth 2.0 authentication and a JWT exchange.

Configure the Qualys Policy Audit pipeline with the following YAML:

```
extension:
  aws:
    secrets:
      qualys-policyaudit-credentials:
        secret_id: "<<secret-arn>>"
        region: "<<secret-region>>"
        sts_role_arn: "<<secret-access-role-arn>>"

pipeline:
  source:
    qualys_policyaudit:
      hostname: "gateway.qg3.apps.qualys.com"
      authentication:
        oauth2:
          username: "${{aws_secrets:qualys-policyaudit-credentials:username}}"
          password: "${{aws_secrets:qualys-policyaudit-credentials:password}}"
      range: "P5D"               # optional (default); from P1D to P5D

  processor:
    - ocsf:
        schema:
          qualys_policyaudit: null
        version: "1.5"
        mapping_version: 1.5.0

  sink:
    - cloudwatch_logs:
        log_group: "/aws/cloudwatch/pipelines/qualys-policyaudit"
```Source parameters

`hostname` (required)  
The Qualys API Gateway hostname, such as `gateway.qg3.apps.qualys.com`. Do not include a scheme. The connector adds `https://` automatically. The hostname varies by platform, such as qg1, qg2, or qg3.

`authentication.oauth2.username` (required)  
The Qualys platform username for the JWT token exchange. Store it in AWS Secrets Manager and reference it with `${{aws_secrets:qualys-policyaudit-credentials:username}}`.

`authentication.oauth2.password` (required)  
The Qualys platform password for the JWT token exchange. Store it in AWS Secrets Manager and reference it with `${{aws_secrets:qualys-policyaudit-credentials:password}}`.

`range` (optional)  
How far back to retrieve posture data on the first run. Use an ISO 8601 duration from `P1D` through `P5D`. Default: `P5D`.

## AWS Secrets Manager extension parameters
<a name="qualys-policy-audit-secrets-parameters"></a>

Define a named secret block, such as `qualys-policyaudit-credentials`, under `extension.aws.secrets`. Set `secret_id` to the ARN of the AWS Secrets Manager secret, `region` to the AWS Region where the secret is stored, and `sts_role_arn` to the role that accesses the secret. Reference credentials with `${{aws_secrets:<name>:<key>}}`.

## Processor parameters
<a name="qualys-policy-audit-processor-parameters"></a>

The `ocsf` processor transforms ingested events into OCSF format. Under `schema`, specify the single source key `qualys_policyaudit` with a null value. Set `version` to `1.5` and `mapping_version` to `1.5.0`.

## Sink parameters
<a name="qualys-policy-audit-sink-parameters"></a>

The `cloudwatch_logs` sink delivers processed events to a CloudWatch Logs log group. Set `log_group` to the name of your destination log group, such as `/aws/cloudwatch/pipelines/qualys-policyaudit`. The sink writes to the AWS Region in which you create the pipeline, and you do not specify an AWS Region in the sink configuration.

**Note**  
The credential values are retrieved from AWS Secrets Manager. You can find your Qualys credentials in the Qualys Cloud Platform under Administration > User Management. The same credentials used for Qualys VMDR can be used for this connector if the account has access to the Policy Compliance module and can authenticate with a username and password.