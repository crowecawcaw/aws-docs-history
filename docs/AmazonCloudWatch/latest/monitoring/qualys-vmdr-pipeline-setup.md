

# CloudWatch pipelines configuration for Qualys VMDR
<a name="qualys-vmdr-pipeline-setup"></a>

Collects vulnerability management data, asset inventory, host detection findings, and platform activity logs from Qualys VMDR using HTTP Basic authentication.

The following example shows the complete pipeline configuration:

```
extension:
  aws:
    secrets:
      qualys-vmdr-credentials:
        secret_id: "<secret-arn>"
        region: "<secret-region>"
        sts_role_arn: "<secret-access-role-arn>"
pipeline:
  source:
    qualys_vmdr:
      hostname: "qualysapi.qg3.apps.qualys.com"
      range: "P1D"
      authentication:
        basic:
          username: "${{aws_secrets:qualys-vmdr-credentials:username}}"
          password: "${{aws_secrets:qualys-vmdr-credentials:password}}"
  sink:
    - cloudwatch_logs:
        log_group: "<qualys-vmdr-log-group>"
  processor:
    - ocsf:
        schema:
          qualys_vmdr: null
        version: "1.5"
        mapping_version: 1.5.0
```

The name in each `aws_secrets` reference must match the secret block name under `extension.aws.secrets`.

The following four fields are the only source fields that you configure for `qualys_vmdr`. A configuration that sets any other source field fails validation.Source parameters

`hostname` (required)  
The customer-specific Qualys API hostname for your platform subscription, for example, `qualysapi.qg3.apps.qualys.com`. Do not include `https://`.

`authentication.basic.username` (required)  
The Qualys API username. Store the value in AWS Secrets Manager and reference it using `${{aws_secrets:qualys-vmdr-credentials:username}}`.

`authentication.basic.password` (required)  
The Qualys API password. Store the value in AWS Secrets Manager and reference it using `${{aws_secrets:qualys-vmdr-credentials:password}}`.

`range` (optional)  
The lookback duration for initial data collection, in ISO 8601 duration format. The minimum is one hour (`PT1H`) and the maximum is one day (`P1D`). The value applies to all four streams. If you omit it, each stream backfills `P1D`.

**Note**  
The credential values are retrieved from AWS Secrets Manager. You can manage the Qualys API user in the Qualys Cloud Platform under Administration > User Management.

## AWS extension parameters
<a name="qualys-vmdr-extension-parameters"></a>

The AWS extension configures AWS Secrets Manager access so that the pipeline can retrieve credentials at runtime. Define a named secret block, such as `qualys-vmdr-credentials`. Set `secret_id` to the ARN of your secret, `region` to the AWS Region where the secret is stored, and `sts_role_arn` to the IAM role ARN to assume when accessing the secret. Reference the credentials in the pipeline with `${{aws_secrets:<name>:<key>}}`. For more information, see the [AWS Secrets Manager extension](pipeline-extensions.md#aws-secrets-manager-extension).

## Sink parameters
<a name="qualys-vmdr-sink-parameters"></a>

The sink delivers processed events to a CloudWatch Logs log group. Set `log_group` to the name of your destination log group, such as `/aws/cloudwatch/pipelines/qualys-vmdr`. For complete configuration options, see the [CloudWatch Logs sink](pipeline-sinks.md#cloudwatch-logs-sink).

## Processor parameters
<a name="qualys-vmdr-processor-parameters"></a>

The processor transforms ingested events into Open Cybersecurity Schema Framework (OCSF) format by using the `qualys_vmdr` schema key. Set `schema.qualys_vmdr` to `null`; the presence of the key activates the Qualys VMDR schema mapping. Set `version` to `"1.5"` and `mapping_version` to `1.5.0`. Events that do not match an OCSF mapping pass through to the sink unchanged. For the full parameter reference, see the [OCSF processor](parser-processors.md#ocsf-processor).