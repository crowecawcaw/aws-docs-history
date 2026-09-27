

# CloudWatch pipelines configuration for Qualys CSAM
<a name="qualys-csam-pipeline-setup"></a>

With this pipeline, you can collect asset inventory, software component, External Attack Surface Management (EASM) vulnerability finding, and domain intelligence data from Qualys CSAM. The pipeline uses the Global AssetView (GAV) and CSAM REST APIs with OAuth 2.0 authentication and a JWT exchange.

The following example shows the complete pipeline configuration:

```
extension:
  aws:
    secrets:
      qualys_csam:
        secret_id: "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>"
        region: "<region>"
        sts_role_arn: "arn:aws:iam::<account-id>:role/<role-name>"
pipeline:
  source:
    qualys_csam:
      hostname: "gateway.qg3.apps.qualys.com"
      range: "P1D"
      authentication:
        oauth2:
          username: "${{aws_secrets:qualys_csam:username}}"
          password: "${{aws_secrets:qualys_csam:password}}"
  sink:
    - cloudwatch_logs:
        log_group: "<qualys-csam-log-group>"
  processor:
    - ocsf:
        schema:
          qualys_csam: null
        version: "1.5"
        mapping_version: 1.5.0
```

## AWS extension parameters
<a name="qualys-csam-extension-parameters"></a>

The AWS extension configures AWS Secrets Manager access for securely retrieving credentials at runtime. Define a named secret block, such as `qualys_csam`. Set `secret_id` to the ARN of your secret, `region` to the AWS Region where the secret is stored, and `sts_role_arn` to the IAM role ARN to assume when accessing the secret. Reference credentials in the pipeline with `${{aws_secrets:<name>:<key>}}`. For more information, see the [AWS Secrets Manager extension](pipeline-extensions.md#aws-secrets-manager-extension).

## Source parameters
<a name="qualys-csam-source-parameters"></a>Parameters

`hostname` (string, required)  
The customer-specific Qualys API Gateway hostname for your platform subscription, such as `gateway.qg3.apps.qualys.com`. Do not include `https://`.

`authentication.oauth2.username` (string, required)  
The Qualys platform username for JWT token exchange. Store the value in AWS Secrets Manager and reference it by using `${{aws_secrets:qualys_csam:username}}`.

`authentication.oauth2.password` (string, required)  
The Qualys platform password for JWT token exchange. Store the value in AWS Secrets Manager and reference it by using `${{aws_secrets:qualys_csam:password}}`.

`range` (string, optional)  
The lookback duration for the initial data backfill, in ISO 8601 duration format. The minimum is one hour (`PT1H`), the maximum is one day (`P1D`), and the default is `P1D`.

**Note**  
The connector retrieves credential values from AWS Secrets Manager. You can find the Qualys user name in the Qualys Cloud Platform on the **Administration** page, on the **Users** tab. You can use the same credentials as Qualys VMDR or Policy Compliance (PC) if the account has access to the CSAM module.

## Sink parameters
<a name="qualys-csam-sink-parameters"></a>

The sink delivers processed events to a CloudWatch Logs log group. Set `log_group` to the name of your destination log group, such as `qualys-csam-log-group`. For complete configuration options, see the [CloudWatch Logs sink](pipeline-sinks.md#cloudwatch-logs-sink).

## Processor parameters
<a name="qualys-csam-processor-parameters"></a>

The processor transforms ingested events into OCSF format using the `qualys_csam` schema key. Set `schema.qualys_csam` to `null`; the presence of the key activates the Qualys CSAM schema mapping. Set `version` to `"1.5"` and `mapping_version` to `1.5.0`. For the full parameter reference, see the [OCSF processor](parser-processors.md#ocsf-processor).