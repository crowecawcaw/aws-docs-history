

# CloudWatch pipelines configuration for JumpCloud
<a name="jumpcloud-pipeline-setup"></a>

The following pipeline configuration collects security and audit events from JumpCloud using API key authentication, and transforms the events from the directory, Single Sign-On (SSO), RADIUS, systems, LDAP, and alerts services into Open Cybersecurity Schema Framework (OCSF) format. Replace the placeholder values shown between `<<` and `>>` with values for your environment.

```
extension:
  aws:
    secrets:
      jumpcloud_credentials:
        secret_id: <<arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>>>
        region: <<region>>
        sts_role_arn: <<arn:aws:iam::<account-id>:role/<role-name>>>
pipeline:
  source:
    jumpcloud:
      hostname: "api.jumpcloud.com"
      authentication:
        api_key: "${{aws_secrets:jumpcloud_credentials:api_key}}"
      range: "P90D"
  sink:
    - cloudwatch_logs:
        log_group: <<jumpcloud-log-group>>
  processor:
    - ocsf:
        schema:
          jumpcloud: null
        version: "1.5"
        mapping_version: 1.5.0
```

The AWS extension configures AWS Secrets Manager access for securely retrieving credentials at runtime. Define a named secret block, such as `jumpcloud_credentials`, with `secret_id` set to the ARN of your AWS Secrets Manager secret, `region` set to the AWS Region where the secret is stored, and `sts_role_arn` set to the IAM role ARN to assume when accessing the secret. Reference credentials in the pipeline using `${{aws_secrets:<name>:<key>}}`. The name in the `aws_secrets` reference must match the secret block name under `extension.aws.secrets`. For the complete configuration reference, see the [AWS Secrets Manager extension](pipeline-extensions.md#aws-secrets-manager-extension).Source parameters

`hostname` (required)  
The JumpCloud API hostname for your organization's data residency region. Use `api.jumpcloud.com` for the US, `api.eu.jumpcloud.com` for the European Union, or `api.in.jumpcloud.com` for India. Do not include `https://`.

`authentication.api_key` (required)  
The JumpCloud API key, prefixed with `jca_`, for authenticating API requests. Store the key in AWS Secrets Manager and reference it using `${{aws_secrets:jumpcloud_credentials:api_key}}`.

`range` (optional)  
The lookback duration for events on the first run, in ISO 8601 duration format. The minimum value is `PT1H`, the maximum value is `P90D`, and the default is `P90D`. JumpCloud retains 90 days of events, so you cannot backfill events that are older than 90 days.

**Note**  
The `api_key` value is retrieved from AWS Secrets Manager. Generate the API key in the JumpCloud Admin Console under your administrator profile settings by choosing **My API Key**.Sink parameters

`log_group` (required)  
The name of the destination CloudWatch Logs log group, such as `jumpcloud-log-group`. For complete configuration options, see the [CloudWatch Logs sink](pipeline-sinks.md#cloudwatch-logs-sink).Processor parameters

`schema.jumpcloud` (required)  
Set this parameter to `null`. The presence of the key activates the JumpCloud schema mapping and transforms ingested events into OCSF format.

`version` (required)  
The OCSF schema version. Set this parameter to `"1.5"`.

`mapping_version` (required)  
The mapping version. Set this parameter to `1.5.0`. For the full parameter reference, see the [OCSF processor](parser-processors.md#ocsf-processor).