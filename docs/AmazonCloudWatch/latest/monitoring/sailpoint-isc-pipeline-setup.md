

# CloudWatch pipelines configuration for SailPoint ISC
<a name="sailpoint-isc-pipeline-setup"></a>

The following pipeline configuration collects identity governance audit events from SailPoint ISC using OAuth 2.0 client credentials authentication. Replace the placeholder values shown between `<<` and `>>` with values for your environment.

```
extension:
  aws:
    secrets:
      sailpoint_isc:
        secret_id: <<arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>>>
        region: <<region>>
        sts_role_arn: <<arn:aws:iam::<account-id>:role/<role-name>>>
pipeline:
  source:
    sailpoint_isc:
      base_url: "https://your-tenant.api.identitynow.com"
      authentication:
        oauth2:
          client_id: "${{aws_secrets:sailpoint_isc:client_id}}"
          client_secret: "${{aws_secrets:sailpoint_isc:client_secret}}"
      range: P90D
  sink:
    - cloudwatch_logs:
        log_group: <<sailpoint-isc-log-group>>
  processor:
    - ocsf:
        schema:
          sailpoint_isc: null
        version: "1.5"
        mapping_version: 1.5.0
```

Configure AWS Secrets Manager access for securely retrieving credentials at runtime. Define a named secret block, such as `sailpoint_isc`, with `secret_id` set to the ARN of your AWS Secrets Manager secret, `region` set to the AWS Region where the secret is stored, and `sts_role_arn` set to the IAM role ARN to assume when accessing the secret. Reference credentials in the pipeline using `${{aws_secrets:<name>:<key>}}`. For more information, see the [AWS Secrets Manager extension](pipeline-extensions.md#aws-secrets-manager-extension).Source parameters

`base_url` (required)  
The SailPoint ISC API base URL. Use the format `https://{tenant}.api.{domain}.com`. The tenant name and domain are specific to your SailPoint deployment. Find the base URL in the SailPoint Admin UI under **Org Details**.

`range` (optional)  
The lookback duration for audit events in ISO 8601 format. Minimum: `PT1H`. Maximum: `P90D`. Default: `P90D`.

`authentication.oauth2.client_id` (required)  
The OAuth 2.0 Client ID from the SailPoint PAT. Store it in AWS Secrets Manager and reference it using `${{aws_secrets:sailpoint_isc:client_id}}`.

`authentication.oauth2.client_secret` (required)  
The OAuth 2.0 Client Secret from the SailPoint PAT. Store it in AWS Secrets Manager and reference it using `${{aws_secrets:sailpoint_isc:client_secret}}`.

**Note**  
Both `client_id` and `client_secret` must be stored in AWS Secrets Manager. Generate the credentials by creating a Personal Access Token in SailPoint ISC under **Preferences**, **Personal Access Tokens**. The PAT must be created by a user with `ORG_ADMIN` privileges, and the `sp:scopes:all` scope must be turned on, to provide access to all audit event types.Sink parameters

`log_group` (required)  
The name of the destination CloudWatch Logs log group, such as `sailpoint-isc-log-group`. For complete configuration options, see the [CloudWatch Logs sink](pipeline-sinks.md#cloudwatch-logs-sink).Processor parameters

`schema.sailpoint_isc` (required)  
Set this parameter to `null`. The presence of the key activates the SailPoint ISC schema mapping and transforms ingested events into OCSF format.

`version` (required)  
The OCSF schema version. Set this parameter to `"1.5"`.

`mapping_version` (required)  
The mapping version. Set this parameter to `1.5.0`. For the full parameter reference, see the [OCSF processor](parser-processors.md#ocsf-processor).