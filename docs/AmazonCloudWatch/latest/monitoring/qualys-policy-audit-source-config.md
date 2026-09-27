

# Source configuration for Qualys Policy Audit
<a name="qualys-policy-audit-source-config"></a>

## Prerequisites
<a name="qualys-policy-audit-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active Qualys subscription with the Policy Compliance (Policy Audit) module enabled
+ A Qualys user account with API access permissions to PCRS endpoints
+ A Qualys API user account that is not SSO-only. API authentication uses a username and password, so the account must be able to authenticate directly.
+ Your platform-specific Qualys API Gateway hostname, such as `gateway.qg3.apps.qualys.com`
+ The final Qualys username and password from the Qualys console procedure, after the first-time password reset is complete
+ An AWS account with permissions to create and manage CloudWatch pipelines. For more information, see [API caller permissions](pipeline-iam-reference.md#api-caller-permissions).
+ An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager, and a source role that can retrieve the stored credentials. For more information, see [Third-party sources (API Pull)](pipeline-iam-reference.md#third-party-api-pull).
+ An AWS account with permissions to create and manage CloudWatch Logs log groups. For more information, see [CloudWatch Logs API operations and required permissions for actions](permissions-reference-cw.md#cwl-permissions-table).

## Integrating with Qualys Policy Audit
<a name="qualys-policy-audit-integration"></a>

To integrate Qualys Policy Audit with CloudWatch pipelines, complete the following high-level steps:
+ Identify your platform-specific Qualys API Gateway hostname.
+ Create a Qualys Reader user with API access and the required asset groups.
+ Store the Qualys username and password in AWS Secrets Manager.
+ Create a destination CloudWatch Logs log group and the source IAM role.
+ Create a CloudWatch pipeline with Qualys Policy Audit as the data source.
+ Verify that compliance posture findings are flowing into the configured log group.

## Configure Qualys Policy Audit
<a name="qualys-policy-audit-product-setup"></a>

1. **Identify your Qualys API Gateway hostname**

   Log in to the Qualys Cloud Platform. Use the [Qualys Platform Identification](https://www.qualys.com/platform-identification) page to determine your platform-specific API Gateway hostname, such as `gateway.qg3.apps.qualys.com`.

1. **Open the Administration module**

   From the module picker, select **Administration** under Platform And Sensor Management.

1. **Start the New User wizard**

   On the Administration page, choose the **Users** tab. Choose **Create User**, and then choose **Create Reader User**.

1. **Enter General Information**

   On the General Information tab, complete the required fields marked with an asterisk: First Name, Last Name, Address 1, Country, State, ZIP Code, and E-mail Address.

1. **Set the User Role and enable API access**

   Choose **User Role** in the left navigation. Set **User Role** to **Reader**. Under **Allow access to**, select **API**. You must select **API**, because this setting is what allows the account to authenticate to the Qualys API for the connector. Leave **Business Unit** set to **Unassigned** unless your organization uses Business Units to segment access.

1. **Assign Asset Groups**

   Choose **Asset Groups** in the left navigation. Use **Add asset groups** to select the asset groups that should be visible to this user and to the connector. Select **All** to retrieve data for every asset in the subscription, or select specific groups to limit the scope.

1. **Review Permissions**

   Choose **Permissions** in the left navigation. The Extended Permissions options for Manage VM module, Purge host information/history, and Manage PC module grant administrative rights and are not required for API read access. Leave them unselected unless your process requires the account to manage those modules.

1. **Complete the remaining tabs and create the user**

   Continue through the remaining Options and Security tabs, changing settings only if your organization has specific requirements such as IP-based login restrictions. Create the user. Qualys emails the new user a temporary password.

   Log in once through the Qualys user interface with the temporary password and complete the required password reset. The API user credentials do not work for the connector until this first-time password reset is complete. Save the final username and password for the pipeline configuration.

## Authenticating with Qualys Policy Audit
<a name="qualys-policy-audit-authentication"></a>

Qualys Policy Audit uses OAuth 2.0 with a username and password exchange for a JWT. The connector performs the following authentication flow:

1. Retrieves the credentials securely from AWS Secrets Manager at runtime.

1. Sends a form-urlencoded `POST` request to the Qualys `/auth` endpoint with `username`, `password`, and `token=true`.

1. Receives the JWT as a raw plain-text string. The token remains valid for approximately four hours.

1. Uses `Authorization: Bearer <token>` for all subsequent API requests and automatically renews the token before it expires.

## Configure the CloudWatch pipeline resources
<a name="qualys-policy-audit-cloudwatch-setup"></a>

1. **Store credentials in AWS Secrets Manager**

   In AWS Secrets Manager, choose **Store a new secret**, and then choose **Other type of secret**. Add the following key-value pairs:
   + `username` – Your Qualys platform username
   + `password` – Your Qualys platform password

   Name the secret, for example `qualys-policyaudit/pipeline-credentials`.

1. **Create the destination CloudWatch Logs log group**

   In the CloudWatch console, choose **Logs**, **Log groups**, and **Create log group**. Choose a descriptive name, such as `/aws/cloudwatch/pipelines/qualys-policyaudit`.

1. **Create the source IAM role**

   Create an IAM role with the required permissions. For information about the required policies and permissions, see [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md).

1. **Create the CloudWatch pipeline**

   In the CloudWatch console, navigate to Pipelines and choose **Qualys Policy Audit** as the data source. Configure authentication with the Qualys API Gateway hostname, username, and password. Select the destination log group. For the complete pipeline YAML configuration and parameter reference, see [CloudWatch pipelines configuration for Qualys Policy Audit](qualys-policy-audit-pipeline-setup.md).

1. **Configure the CloudWatch Logs resource policy**

   The behavior depends on whether the destination log group is new or already exists. For a new log group created through the console, the resource policy is created automatically and no action is required. If the selected log group already has a resource policy, the console displays a Resource Policy Detected warning. In that case, verify that the existing policy includes permissions for pipelines to write to the destination log group, and add or update the [CloudWatch Logs resource policy](pipeline-iam-reference.md#resource-policies) within five minutes of pipeline creation.
**Note**  
When you create the pipeline by using the AWS CLI or API, a resource policy is never created automatically, regardless of whether the log group is new or existing. You must create the resource policy manually before the pipeline becomes active.

1. **Verify data flow**

   Allow time for the initial data retrieval to complete. Check the destination log group for incoming events, and monitor [pipeline metrics](pipelines-metrics.md) for successful ingestion.

## Supported Open Cybersecurity Schema Framework event classes
<a name="qualys-policy-audit-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0. Qualys Policy Audit compliance posture findings are mapped to the Compliance Finding OCSF class, capturing per-host, per-control evaluation results including pass, fail, and error status; control statements; rationale; remediation guidance; severity; and scan timestamps.

### Compliance Finding (2003)
<a name="qualys-policy-audit-ocsf-compliance-finding"></a>

The [Compliance Posture](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf) event from the `/pcrs/5.0/posture/postureInfo` endpoint maps to [Compliance Finding (2003)](https://schema.ocsf.io/1.5.0/classes/compliance_finding). Each event contains a per-host, per-control compliance evaluation including pass, fail, or error status; control statements; rationale; remediation; severity or criticality; and scan timestamps.

**Note**  
Events that do not match an OCSF mapping transformation are automatically passed through and sent directly to the configured sink without additional processing.

## Known platform limitations
<a name="qualys-policy-audit-limitations"></a>

The following table describes known Qualys Policy Audit platform limitations.


| Limitation | Details | Impact | 
| --- | --- | --- | 
| Backfill window | The first-run backfill is bounded by range, with a minimum of P1D, maximum of P5D, and default of P5D. | Historical posture data older than the backfill window is not retrieved on the first run. | 
| Posture availability delay | Posture data becomes available only after a compliance scan completes and is evaluated by the Qualys platform. Qualys does not document an exact delay. | Findings are delivered only after the Qualys platform finishes evaluating a scan, so delivery lags scan completion. | 
| No sort-order support | The PCRS API does not document an ascending or descending sort parameter. | Records are not guaranteed to arrive in a specific order within a window. | 
| Shared API rate limit | With the default Standard API Service, Qualys permits 300 API calls per subscription for each API in a rolling 3,600-second window. When the limit is exceeded, Qualys returns HTTP 409 Conflict with error code 1965 and an X-RateLimit-ToWait-Sec header. Qualys Support can customize the limit for your subscription. | The pipeline shares one quota with every other user and integration in the subscription, so heavy API use elsewhere slows pipeline ingestion, especially during the initial backfill. The connector waits for the interval in the header and retries, so throughput is reduced but data is not lost. | 
| Concurrent call limit | With the default Standard API Service, Qualys permits two concurrent API calls for each API. Qualys checks the concurrency limit before the rate limit and returns HTTP 409 Conflict with error code 1960 when the limit is exceeded. Concurrency errors take precedence over rate-limit errors and don't include rate-limit headers. | High-volume environments might experience throttling during the initial backfill. The connector retries with backoff, so throughput is reduced but data is not lost. | 
| Customer-specific hostname | There is no universal endpoint. The API Gateway hostname is assigned per Qualys subscription and region. | You must supply the exact gateway fully qualified domain name for your platform. | 
| Token time to live | JWT tokens expire approximately four hours after issue. | The connector automatically renews the token before it expires. | 

## Troubleshooting
<a name="qualys-policy-audit-troubleshooting"></a>

The following table lists common errors and their resolutions.


| Error | Likely cause | Resolution or connector behavior | 
| --- | --- | --- | 
| 401 Unauthorized | Invalid or expired credentials, or credentials rotated in AWS Secrets Manager | The connector renews the token and retries up to six times. Verify that the username and password in AWS Secrets Manager are current, API access is enabled, and the account is not SSO-only. | 
| 403 Forbidden | Insufficient permissions for the API user | This error is not retryable, and the connector stops immediately. Verify that the Reader user has API access and the required asset groups assigned. | 
| 5xx Server Error | Transient Qualys platform error | The connector retries with exponential backoff at 1, 2, 5, 10, 20, and 40 seconds. | 
| No data in the log group | The pipeline resource policy was not added within five minutes of creation. | Delete and recreate the pipeline, and then immediately add the CloudWatch Logs resource policy. | 
| Wrong hostname or connection failure | A VMDR hostname was used instead of the PCRS gateway hostname, or the hostname includes a scheme. | Use the gateway.<platform>.apps.qualys.com form without https://. | 

### Identify the Qualys API Gateway hostname
<a name="qualys-policy-audit-troubleshooting-hostname"></a>
+ The Policy Audit connector uses the Qualys API Gateway hostname, such as `gateway.qg3.apps.qualys.com`. This differs from the VMDR API hostname, such as `qualysapi.qg3.apps.qualys.com`.
+ Identify your platform from the platform identifier embedded in your Qualys username. For example, the character `3` indicates US Platform 3, a hyphen indicates EU Platform 1, and the character `C` indicates the US federal platform.
+ Use the [Qualys Platform Identification](https://www.qualys.com/platform-identification) page to map your platform identifier to the gateway hostname.
+ Provide only the domain. Do not include `https://`.

### Policy Audit and VMDR use different hostnames
<a name="qualys-policy-audit-troubleshooting-vmdr-hostname"></a>
+ Qualys VMDR uses `qualysapi.<platform>.apps.qualys.com` on most platforms, such as `qualysapi.qg3.apps.qualys.com`. US Platform 1 and EU Platform 1 are exceptions and use the shorter legacy forms `qualysapi.qualys.com` and `qualysapi.qualys.eu`, with no platform segment and no `apps` segment.
+ Qualys Policy Audit uses `gateway.<platform>.apps.qualys.com`, such as `gateway.qg3.apps.qualys.com`.
+ Both hostnames are on the same Qualys platform but use different API surfaces. Use the gateway hostname for this connector.

### No compliance findings are returned
<a name="qualys-policy-audit-troubleshooting-no-findings"></a>
+ Confirm that the Policy Compliance module is active in your Qualys subscription.
+ Verify that compliance policies are assigned to hosts or asset groups and that scans have completed.
+ Check the `range` parameter. The default is `P5D`. If no scans occurred in that window, no data is returned.

## References
<a name="qualys-policy-audit-references"></a>
+ [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md)
+ [Monitoring pipelines](pipelines-metrics.md)
+ [Troubleshooting](troubleshooting.md)
+ [Qualys API (VM, PA) User Guide](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf)
+ [Qualys Policy Compliance Guide](https://cdn2.qualys.com/docs/qualys-policy-compliance-guide.pdf)
+ [Qualys API Limits](https://cdn2.qualys.com/docs/qualys-api-limits.pdf)
+ [Qualys Platform Identification](https://www.qualys.com/platform-identification)
+ [OCSF schema v1.5.0](https://schema.ocsf.io/1.5.0/)