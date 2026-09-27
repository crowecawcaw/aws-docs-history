

# CloudWatch pipelines configuration for Google Workspace
<a name="google-workspace-pipeline-setup"></a>

Collects audit logs from Google Workspace using OAuth 2.0 service account authentication with domain-wide delegation.

## YAML configuration
<a name="google-workspace-yaml-configuration"></a>

```
extension:
  aws:
    secrets:
      google_workspace:
        secret_id: <<arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>>>
        region: <<region>>
        sts_role_arn: <<arn:aws:iam::<account-id>:role/<role-name>>>
pipeline:
  source:
    google_workspace:
      user_key: all
      range: P30D
      authentication:
        jwt_key_pair:
          private_key: ${{aws_secrets:google_workspace:private_key}}
          client_email: ${{aws_secrets:google_workspace:client_email}}
          subject: ${{aws_secrets:google_workspace:subject}}
  sink:
    - cloudwatch_logs:
        log_group: <<google-workspace-log-group>>
  processor:
    - ocsf:
        schema:
          google_workspace: null
        version: "1.5"
        mapping_version: 1.5.0
```

## AWS extension parameters
<a name="google-workspace-extension-parameters"></a>

The AWS extension configures AWS Secrets Manager access for securely retrieving credentials at runtime. Define a named secret block, such as `google_workspace`, with `secret_id` set to the ARN of your AWS Secrets Manager secret, `region` set to the AWS Region where the secret is stored, and `sts_role_arn` set to the IAM role ARN to assume when accessing the secret. Credentials are then referenced in the pipeline by using `${{aws_secrets:<name>:<key>}}`. For the complete configuration reference, see the [AWS Secrets Manager extension](pipeline-extensions.md#aws-secrets-manager-extension).

## Source parameters
<a name="google-workspace-source-parameters"></a>Parameters

`user_key` (optional)  
String that provides the profile ID or user email for which the data is filtered. The default value, `all`, fetches all information.

`range` (optional)  
Lookback duration for activity logs in ISO 8601 format. The minimum value is `P1D`, the maximum value is `P180D`, and the default value is `P180D`.

`authentication.jwt_key_pair.private_key` (required)  
The private key from the Google Cloud service account JSON key file. Store the value in AWS Secrets Manager and reference it using `${{aws_secrets:google_workspace:private_key}}`.

`authentication.jwt_key_pair.client_email` (required)  
The service account email address. Store the value in AWS Secrets Manager and reference it using `${{aws_secrets:google_workspace:client_email}}`.

`authentication.jwt_key_pair.subject` (required)  
The administrator email address to impersonate through domain-wide delegation. This value must be a delegated administrator account, not the service account email. Store the value in AWS Secrets Manager and reference it using `${{aws_secrets:google_workspace:subject}}`.

**Note**  
Store all three authentication values, `private_key`, `client_email`, and `subject`, in AWS Secrets Manager. Reference them through the `google_workspace` secret block. The service account credentials, `private_key` and `client_email`, are available in the Google Cloud console under **IAM & Admin** > **Service Accounts**. The `subject`, or delegated administrator email, must be an administrator in your Google Workspace organization with domain-wide delegation authorized for the service account.

**Note**  
For Gmail activity, if `range` is set to more than `P30D`, only the last 30 days of logs are fetched because of API constraints.

## Sink parameters
<a name="google-workspace-sink-parameters"></a>

The sink delivers processed events to a CloudWatch Logs log group. Set `log_group` to the name of your destination log group, for example, `google-workspace-log-group`. For complete configuration options, see the [CloudWatch Logs sink](pipeline-sinks.md#cloudwatch-logs-sink).

## Processor parameters
<a name="google-workspace-processor-parameters"></a>

The processor transforms ingested events into OCSF format using the `google_workspace` schema key. Set `schema.google_workspace` to `null`. The presence of the key activates the Google Workspace schema mapping. Set `version` to `"1.5"` and `mapping_version` to `1.5.0`. For the full parameter reference, see the [OCSF processor](parser-processors.md#ocsf-processor).

## Known platform limitations
<a name="google-workspace-limitations"></a>


| Limitation | Details | Impact | 
| --- | --- | --- | 
| Gmail query window | The Reports API requires a start time and an end time for every Gmail request, and the difference between them cannot be greater than 30 days. | range values exceeding P30D fetch only the most recent 30 days of Gmail data. | 
| Activity data availability delay | The delay before events become available in the Reports API depends on the application, and ranges from near real time to several days. | For the slower applications, recent events might not appear in the destination log group immediately. | 
| Alert Center availability | The Alert Center API is in beta, version v1beta1. | API behavior can change without notice. | 
| Access Transparency edition requirements | Access Transparency logs are available only with the Frontline Plus, Enterprise Plus, Education Standard, Education Plus, and Enterprise Essentials Plus editions. | If your organization uses an edition that is not listed, you do not receive these events. | 
| Domain-wide delegation | Domain-wide delegation requires super-admin privileges to configure. | If you are not a super-admin, you cannot configure the integration. | 
| API rate limits | The Reports API allows 2,400 queries per minute for each user in a Google Cloud project. The Alert Center API allows 1,000 requests per second for each project and 150 requests per second for each user. | High-volume environments might experience throttling. | 

## Troubleshooting
<a name="google-workspace-troubleshooting"></a>


| Error | Likely cause | Resolution or connector behavior | 
| --- | --- | --- | 
| 401 Unauthorized | Invalid or expired service account credentials | Verify that the private\_key stored in AWS Secrets Manager matches the current service account key. If necessary, regenerate the key in the Google Cloud console. | 
| 403 Forbidden – Not Authorized to access this resource/api | Domain-wide delegation is not configured or scopes are not authorized. | Verify that the service account client ID is added in the Google Admin console with the correct OAuth scopes. Make sure that the subject is an administrator account. | 
| 403 Forbidden – Access Not Configured | A required API is not enabled. | Enable the Admin SDK API and Alert Center API in the Google Cloud console. | 
| 429 Too Many Requests | An API rate limit is exceeded. | The connector automatically backs off and retries. If the error persists, verify that other workloads are not consuming the same Google Workspace API quota. | 
| 400 Bad Request – Invalid subject | The subject email is not a valid administrator account. | Verify that the subject value is an administrator email address in your Google Workspace organization. | 
| No data appears in the log group. | The pipeline resource policy was not added within 5 minutes of pipeline creation, before the pipeline became active. | Delete and recreate the pipeline, and then immediately add the CloudWatch Logs resource policy. | 
| Some applications are missing from the data. | Service account scopes are too restrictive. | Verify that all required OAuth scopes are authorized in the Google Admin console domain-wide delegation settings. | 

### Gmail activity shows fewer events than expected
<a name="google-workspace-troubleshooting-gmail"></a>
+ The Reports API limits each Gmail request to a window of 30 days, so only the most recent 30 days of Gmail activity are fetched regardless of the configured `range` value.
+ Gmail activity reports message delivery events, such as messages sent and received.

### Alert Center returns empty results
<a name="google-workspace-troubleshooting-alert-center"></a>
+ The current version of the Alert Center API, v1beta1, is available to all Google Workspace customers. Access depends on a privilege rather than on an edition. Verify that the impersonated `subject` account holds the Alert center administrator privilege.
+ Alerts can take up to 24 hours to appear after the triggering event.
+ Verify that the `https://www.googleapis.com/auth/apps.alerts` scope is authorized.

### Access Transparency logs do not appear
<a name="google-workspace-troubleshooting-access-transparency"></a>
+ This feature requires the Frontline Plus, Enterprise Plus, Education Standard, Education Plus, or Enterprise Essentials Plus edition.
+ Verify that your organization opted in to Access Transparency in the Google Admin console.