

# Source configuration for JumpCloud
<a name="jumpcloud-source-config"></a>

## Supported API and platform versions
<a name="jumpcloud-supported-versions"></a>


| Component | Version | Notes | 
| --- | --- | --- | 
| Directory Insights API | v1 | Security and audit event retrieval across all services | 
| Open Cybersecurity Schema Framework (OCSF) schema | v1.5.0 | Open Cybersecurity Schema Framework mapping | 
| API key authentication | v1 | API key sent in the x-api-key header | 

## Prerequisites
<a name="jumpcloud-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active JumpCloud organization with Directory Insights enabled. Directory Insights is included in some JumpCloud package plans. JumpCloud stores 90 days of event logs and removes logs that are older than 90 days.
+ A [JumpCloud administrator account](https://console.jumpcloud.com/login) with permissions to generate API keys.
+ The JumpCloud API hostname for your organization's data residency region.
+ An AWS account with permissions to create and manage CloudWatch pipelines. For more information, see [API caller permissions](pipeline-iam-reference.md#api-caller-permissions).
+ An AWS account with permissions to create and update secrets in AWS Secrets Manager, and a source role that can retrieve the stored credentials. For more information, see [Third-party sources (API Pull)](pipeline-iam-reference.md#third-party-api-pull).
+ An AWS account with permissions to create and manage CloudWatch Logs log groups. For more information, see [CloudWatch Logs API operations and required permissions for actions](permissions-reference-cw.md#cwl-permissions-table).

## Integrating with JumpCloud
<a name="jumpcloud-integration"></a>

To integrate CloudWatch pipelines with JumpCloud, complete the following high-level steps:
+ Generate an API key in the JumpCloud Admin Console.
+ Identify the API hostname for your organization's data residency region.
+ Store the API key in AWS Secrets Manager.
+ Create a destination CloudWatch Logs log group and the required source IAM role.
+ Create a CloudWatch pipeline with JumpCloud as the data source.
+ Verify that data is flowing into the configured CloudWatch Logs log group.

## Authenticating with JumpCloud
<a name="jumpcloud-authentication"></a>

JumpCloud uses API key authentication. The pipeline sends the API key as an `x-api-key` header with every request to the JumpCloud Directory Insights API. API keys are prefixed with `jca_` and are tied to an individual administrator account.

## Configure authentication for JumpCloud
<a name="jumpcloud-configure-auth"></a>

To configure authentication credentials for the pipeline:

1. Log in to the [JumpCloud Admin Console](https://console.jumpcloud.com/login) with your administrator credentials.

1. Navigate to your administrator profile settings and select **My API Key**.

1. Generate a new API key. The key is prefixed with `jca_`.

1. Copy and securely store the API key immediately. You cannot view it again.

1. Identify the API hostname for your organization's data residency region:
   + US (default): `api.jumpcloud.com`
   + EU (European Union): `api.eu.jumpcloud.com`
   + IN (India): `api.in.jumpcloud.com`
**Note**  
The hostname must not include `https://`. Provide only the domain, such as `api.jumpcloud.com`.

1. In AWS Secrets Manager, choose **Store a new secret**, and then choose **Other type of secret**. Add the key-value pair `api_key` with the JumpCloud API key as the value. For example, name the secret `jumpcloud/pipeline-credentials`.

## Configuring the CloudWatch pipeline
<a name="jumpcloud-pipeline-config"></a>

1. Create the destination CloudWatch Logs log group. For example, use `/aws/cloudwatch/pipelines/jumpcloud`.

1. Create a source IAM role with the required permissions. For information about the required policies and permissions, see [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md).

1. Open the CloudWatch console, navigate to **Pipelines**, and choose JumpCloud as the data source.

1. Provide the API `hostname` for your organization's data residency region and the `api_key` stored in AWS Secrets Manager.

1. Select the destination log group.

1. Verify the destination log group resource policy. For a new log group, the console creates the resource policy automatically. If the log group already has a resource policy, the console warns you, and you must update that policy within five minutes of pipeline creation to include the required pipeline write permissions. For more information, see [Resource policies](pipeline-iam-reference.md#resource-policies).

1. Wait a few minutes for the initial data pull, check the destination log group for incoming events, and monitor [pipeline metrics](pipelines-metrics.md) for successful ingestion.

After you create and activate the pipeline, security and audit events from JumpCloud begin flowing into the selected CloudWatch Logs log group.

**Note**  
When you create the pipeline using the AWS CLI or API, a resource policy is never created automatically, regardless of whether the log group is new or existing. You must create the CloudWatch Logs resource policy manually before the pipeline becomes active.

## Supported Open Cybersecurity Schema Framework event classes
<a name="jumpcloud-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0. Each JumpCloud service maps to one or more of the following OCSF event classes.

**Note**  
Events that do not match an OCSF mapping transformation are automatically passed through and sent directly to the configured sink without additional processing.

### Authentication (3002)
<a name="jumpcloud-ocsf-authentication"></a>
+ [**Directory authentication events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/Directory-Attributes) (`directory`) – Admin portal login attempts, admin API key authentication, and user portal login attempts.
+ [**SSO authentication events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/SSO-Attributes) (`sso`) – User authentications to SSO applications. The authentication protocol of the target application is reported as SAML or OpenID.
+ [**Systems authentication events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/Systems-Attributes) (`systems`) – Device-level login attempts, including SSH and console login attempts, on JumpCloud-managed systems, and remote session start, join, and end events.
+ [**RADIUS authentication events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/RADIUS-Attributes) (`radius`) – RADIUS-based network authentication attempts with PAP, CHAP, and EAP support.
+ [**LDAP Bind authentication events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/LDAP-Attributes) (`ldap`) – LDAP Bind operations representing directory authentication attempts.

### Account Change (3001)
<a name="jumpcloud-ocsf-account-change"></a>

[**Directory account lifecycle events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/Directory-Attributes) (`directory`) – User and administrator account lifecycle operations including creation, modification, deletion, activation, suspension, lockout, unlock, password change or reset, and MFA factor enable or disable operations.

### Entity Management (3004)
<a name="jumpcloud-ocsf-entity-management"></a>
+ [**Directory entity management events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/Directory-Attributes) (`directory`) – Create, read, update, and delete operations on directory objects including groups, policies, applications, SSO integrations, resource associations, SCIM provisioning, and platform configurations.
+ [**Systems entity management events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/Systems-Attributes) (`systems`) – System and device lifecycle management including creation, update, deletion, operating system upgrades, rollbacks, and Google EMM operations.
+ [**Alerts rule configuration events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/Alert-Attributes) (`alerts`) – Alert rule lifecycle management including rule creation, modification, and deletion.

### Detection Finding (2004)
<a name="jumpcloud-ocsf-detection-finding"></a>

[**Alert detection finding events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/Alert-Attributes) (`alerts`) – Alert creation, update, and status change events generated by JumpCloud security rules for device compliance and policy violations.

### Datastore Activity (6005)
<a name="jumpcloud-ocsf-datastore-activity"></a>

[**LDAP Search events**](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html#section/Schemas/LDAP-Attributes) (`ldap`) – LDAP directory query operations including search filter, base DN, and result tracking.

## Known platform limitations
<a name="jumpcloud-limitations"></a>


| Limitation | Details | Impact | 
| --- | --- | --- | 
| Directory Insights entitlement | Directory Insights is included in only some JumpCloud package plans. JumpCloud stores 90 days of event logs and removes logs that are older than 90 days. | If your plan does not include Directory Insights, no events are available until your JumpCloud account manager enables it. You cannot backfill events that are older than 90 days. | 
| API key scope | API keys are tied to an individual administrator account. | If that administrator account is deactivated, the API key becomes invalid. | 
| Data residency | The API hostname must match the data residency region that is configured for your organization. | If you use a hostname for another region, authentication fails. | 
| Event delivery delay | Events can take a few minutes to appear in the Directory Insights API. | Near-real-time monitoring might not capture the most recent events. | 
| API rate limits | JumpCloud does not publish explicit rate limit numbers for the Directory Insights API. | The connector handles HTTP 429 responses automatically by backing off and retrying. | 

## Troubleshooting
<a name="jumpcloud-troubleshooting"></a>


| Error | Likely cause | Resolution or connector behavior | 
| --- | --- | --- | 
| 401 Unauthorized | The API key is invalid or expired. | Verify that the api\_key stored in AWS Secrets Manager is correct and that the associated administrator account is active. Regenerate the key if necessary. | 
| 403 Forbidden | Insufficient permissions, or the hostname does not match your region. | Make sure that the API key belongs to an administrator who has Directory Insights access. Verify that hostname matches your organization's data residency region. | 
| 429 Too Many Requests | The API rate limit was exceeded. | The connector automatically backs off and retries. | 
| No data appears in the log group. | The pipeline resource policy was not added within five minutes of pipeline creation, before the pipeline became active. | Delete and recreate the pipeline, and then immediately add the CloudWatch Logs resource policy. | 
| Empty responses | Directory Insights is not enabled for your organization, or no events exist in the requested time range. | Verify that Directory Insights is enabled for your JumpCloud plan, and check that events exist within the configured range period. | 

### No events from a specific service
<a name="jumpcloud-troubleshooting-missing-service"></a>
+ Verify that the service, such as SSO, RADIUS, or LDAP, is actively used in your JumpCloud organization. Services without activity do not generate events.
+ Check that the service is enabled and configured in the JumpCloud Admin Console.

### The API key becomes invalid unexpectedly
<a name="jumpcloud-troubleshooting-api-key"></a>
+ API keys are tied to an individual administrator account. If that account is deactivated or deleted, or if its permissions change, the key becomes invalid.
+ Regenerate the API key from an active administrator account, and then update the secret in AWS Secrets Manager.

### Events are missing after a data residency change
<a name="jumpcloud-troubleshooting-region-change"></a>
+ If your organization changed data residency regions, update the `hostname` parameter to the API hostname for the new region.