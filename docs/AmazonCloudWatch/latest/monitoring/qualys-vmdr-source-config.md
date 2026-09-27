

# Source configuration for Qualys VMDR
<a name="qualys-vmdr-source-config"></a>

## Integrating with Qualys VMDR
<a name="qualys-vmdr-integration"></a>

CloudWatch pipelines use versions 2.0, 4.0, and 5.0 of the Qualys Vulnerability Management (VM) and Policy Compliance (PC) APIs across the supported endpoints. The APIs use HTTP Basic authentication and return XML for Knowledge Base, Assets, and Host Detection data, and CSV for Activity Log data. The connector handles the response parsing internally.

To integrate CloudWatch pipelines with Qualys VMDR, complete the following high-level steps:
+ Identify the API hostname for your Qualys platform.
+ Create a Qualys user with the Manager role, enable API access, and assign the asset groups that the connector can access.
+ Store the Qualys username and password in AWS Secrets Manager.
+ Create a CloudWatch pipeline with Qualys VMDR as the data source.
+ Verify that data is flowing into the destination CloudWatch Logs log group.

## Supported API and platform versions
<a name="qualys-vmdr-supported-versions"></a>

The following table lists the supported API and platform versions.


| Component | Version | Notes | 
| --- | --- | --- | 
| Qualys Vulnerability Management and Policy Compliance (VMPC) API | v2.0, v4.0, v5.0 | Multiple API versions are used across the supported endpoints | 
| Open Cybersecurity Schema Framework (OCSF) schema | v1.5.0 | Event mapping to the OCSF schema | 
| HTTP Basic authentication | Not applicable | Base64-encoded username:password credentials with each request | 

## Prerequisites
<a name="qualys-vmdr-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active Qualys VMDR subscription with API access enabled
+ A Qualys user account with the Manager role, or a role with equivalent permissions, and with API access enabled
+ The hostname for your Qualys platform, such as `qualysapi.qg3.apps.qualys.com`
+ A Qualys subscription that includes the VMDR module
+ An AWS account with permissions to create and manage CloudWatch pipelines. For more information, see [API caller permissions](pipeline-iam-reference.md#api-caller-permissions).
+ An AWS account with permissions to create and update secrets in AWS Secrets Manager, and a source role that can retrieve the stored credentials. For more information, see [Third-party sources (API Pull)](pipeline-iam-reference.md#third-party-api-pull).
+ An AWS account with permissions to create and manage CloudWatch Logs log groups. For more information, see [CloudWatch Logs API operations and required permissions for actions](permissions-reference-cw.md#cwl-permissions-table).

## Configure Qualys VMDR
<a name="qualys-vmdr-product-setup"></a>

To configure a Qualys user for the integration:

1. Log in to the Qualys Cloud Platform and identify your Qualys API hostname. You can find your platform assignment under **Help > About** or use the [Qualys Platform Identification](https://www.qualys.com/platform-identification) page.

1. From the module picker, choose **Administration** under Platform and Sensor Management.

1. On the Administration page, choose the **Users** tab, and then choose **Create User**.

1. On the **General Information** tab, complete the required fields: First Name, Last Name, Address 1, Country, State, ZIP Code, and E-mail Address.

1. Choose **User Role** in the left navigation pane. Set the role to **Manager**, and under **Allow access to**, select **API**. Leave Business Unit set to Unassigned unless your organization uses business units to segment access.

1. Choose **Asset Groups**. Add the asset groups that should be visible to this user, and therefore to the connector. Select all asset groups if the connector should retrieve data for every asset in the subscription, or select specific groups to limit the scope.

1. Choose **Permissions**. The extended permissions to manage the VM module, purge host information or history, and manage the PC module are not required for API read access. Leave them cleared unless your process requires this account to manage those modules.

1. Complete the remaining Options and Security tabs. Configure settings such as IP-based login restrictions only if required by your organization, and then create the user. Qualys emails the new user a temporary password.

1. Log in to the Qualys user interface with the temporary password and complete the required password reset. The API credentials do not work with the connector until this first-time password reset is complete.

1. Save the final `username` and `password` for the pipeline configuration.

## Qualys platform hostnames
<a name="qualys-vmdr-platform-hostnames"></a>

Use the hostname that corresponds to your Qualys platform. Do not include `https://`.<a name="qualys-vmdr-platform-hostnames-list"></a>

US Platform 1  
`qualysapi.qualys.com`

US Platform 2  
`qualysapi.qg2.apps.qualys.com`

US Platform 3  
`qualysapi.qg3.apps.qualys.com`

US Platform 4  
`qualysapi.qg4.apps.qualys.com`

EU Platform 1  
`qualysapi.qualys.eu`

EU Platform 2  
`qualysapi.qg2.apps.qualys.eu`

India Platform  
`qualysapi.qg1.apps.qualys.in`

Canada Platform  
`qualysapi.qg1.apps.qualys.ca`

UAE Platform  
`qualysapi.qg1.apps.qualys.ae`

Australia Platform  
`qualysapi.qg1.apps.qualys.com.au`

## Authenticating with Qualys VMDR
<a name="qualys-vmdr-authentication"></a>

Qualys VMDR uses HTTP Basic authentication. The pipeline sends Base64-encoded `username:password` credentials in an Authorization header with each API request. The credentials are retrieved securely from AWS Secrets Manager at runtime and are not stored in the pipeline configuration.

## Configure the CloudWatch pipeline resources
<a name="qualys-vmdr-cloudwatch-setup"></a>

1. In AWS Secrets Manager, choose **Store a new secret**, and then choose **Other type of secret**. Add a `username` key with your Qualys API username and a `password` key with your Qualys API password. Name the secret, for example, `qualys-vmdr/pipeline-credentials`.

1. Create the destination CloudWatch Logs log group, for example, `/aws/cloudwatch/pipelines/qualys-vmdr`.

1. Create the source IAM role with the required permissions. For information about the required policies, see [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md).

1. In the CloudWatch console, navigate to Pipelines and choose **Qualys VMDR** as the data source. Configure the Qualys hostname and authentication credentials, and select the destination log group.

1. Configure the [CloudWatch Logs resource policy](pipeline-iam-reference.md#resource-policies):
   + For a new log group created in the console, the resource policy is created automatically.
   + If the selected log group already has a resource policy, review and update it within 5 minutes of pipeline creation to include the required pipeline write permissions.
   + When you create the pipeline with the AWS CLI or API, a resource policy is not created automatically. Create the policy manually before the pipeline becomes active.

1. Wait a few minutes for the initial data retrieval. Check the destination log group for incoming events and monitor [pipeline metrics](pipelines-metrics.md) for successful ingestion.

## Supported Open Cybersecurity Schema Framework event classes
<a name="qualys-vmdr-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0. Qualys VMDR events are mapped to OCSF classes based on the data type. Vulnerability definitions map to Vulnerability Finding, asset inventory maps to Device Inventory Info, and activity log events map to Authentication, API Activity, Account Change, or Entity Management based on the action type.


| Event type | Application or endpoint ID | OCSF event class | Description | 
| --- | --- | --- | --- | 
| [Vulnerability (Knowledge Base)](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf) | /api/4.0/fo/knowledge\_base/vuln/?action=list | [Vulnerability Finding (2002)](https://schema.ocsf.io/1.5.0/classes/vulnerability_finding) | QID, CVE IDs, severity level 1 through 5, solution text, vendor references, exploitability, patchable flag, and published dates | 
| [Assets](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf) | /api/5.0/fo/asset/host/?action=list | [Device Inventory Info (5001)](https://schema.ocsf.io/1.5.0/classes/device_inventory_info) | Host asset inventory including IP, operating system, DNS, NetBIOS, agent status, and scan timestamps | 
| [Activity Log – login and logout](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf) | /api/2.0/fo/activity\_log/?action=list | [Authentication (3002)](https://schema.ocsf.io/1.5.0/classes/authentication) | User login and logout events with source IP and user role | 
| [Activity Log – all non-authentication actions](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf) | /api/2.0/fo/activity\_log/?action=list | [API Activity (6003)](https://schema.ocsf.io/1.5.0/classes/api_activity) | API requests, appliance downloads, and vulnerability edits, plus operational actions such as scan launch, scan completion, and report generation. Actions that do not match a more specific class map to API Activity with an activity of Other. | 
| [Activity Log – activate, set password, and set authentication](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf) | /api/2.0/fo/activity\_log/?action=list | [Account Change (3001)](https://schema.ocsf.io/1.5.0/classes/account_change) | Account activation, password changes, and credential setup events | 
| [Activity Log – administrative configuration, appliance, and asset group](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf) | /api/2.0/fo/activity\_log/?action=list | [Entity Management (3004)](https://schema.ocsf.io/1.5.0/classes/entity_management) | Administrative configuration changes, scanner appliance create, update, and delete operations, and asset group and domain management | 

### Ingestion-only event types
<a name="qualys-vmdr-ingestion-only-events"></a>

The following event type is ingested but is not currently mapped to an OCSF class:


| Event type | Application or endpoint ID | Description | 
| --- | --- | --- | 
| [Asset Host Detection](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf) | /api/5.0/fo/asset/host/vm/detection/?action=list | Per-host vulnerability detection records. The records contain nested detection arrays that require sub-array record extraction, which is not currently supported for OCSF mapping. | 

Activity log actions that do not match a more specific class, such as scan launch, scan completion, and report generation, are mapped to API Activity (6003) with an activity of Other. They are not ingestion-only.

Events that do not match an OCSF mapping transformation are automatically passed through and sent directly to the configured sink without additional processing.

## Known platform limitations
<a name="qualys-vmdr-limitations"></a>

The following table describes known Qualys VMDR platform limitations.


| Limitation | Details | Impact | 
| --- | --- | --- | 
| Customer-specific API hostname | The API base URL varies by Qualys platform. There is no universal endpoint. | You must identify your platform and configure the correct hostname. | 
| XML and CSV response formats | The APIs return XML for Knowledge Base, Assets, and Host Detection data, and CSV for Activity Log data. There is no JSON response option. | The connector handles the parsing internally. | 
| API rate limits | With the default Standard API Service, Qualys permits 300 API calls per subscription for each API in a rolling 3,600-second window. When the limit is exceeded, Qualys returns HTTP 409 Conflict with error code 1965 and an X-RateLimit-ToWait-Sec header. | The connector backs off and retries based on the rate-limit headers. | 
| Concurrent call limit | With the default Standard API Service, Qualys permits two concurrent API calls per subscription for each API. | High-volume environments might experience throttling during the initial backfill. | 
| No OAuth 2.0 support | The version 2, 4, and 5 API endpoints support only HTTP Basic authentication. | Credentials must be rotated manually. There is no token refresh mechanism. | 
| Asset Host Detection nested arrays | Each host record contains multiple detection entries in a nested array. | These events are ingested without Open Cybersecurity Schema Framework (OCSF) mapping because sub-array extraction is not supported. | 
| Server-driven pagination | Qualys caps the page size at 1,000 records for Assets, 100 records for Host Detection, and 1,000 records for Activity Log. | Large datasets require multiple paginated requests in each polling cycle. | 
| Activity Log shared across modules | The Activity Log captures events from all Qualys modules, not only VMDR. | Some ingested events can relate to Policy Compliance (PC), Web Application Scanning (WAS), or CyberSecurity Asset Management (CSAM). | 

## Troubleshooting
<a name="qualys-vmdr-troubleshooting"></a>


| Error | Likely cause | Resolution or connector behavior | 
| --- | --- | --- | 
| 401 Unauthorized | Invalid or expired credentials | Verify the username and password stored in AWS Secrets Manager, and make sure that the Qualys account has API access enabled. | 
| 403 Forbidden | Insufficient permissions or API access is not enabled | Make sure that the Qualys user has the Manager role, or a role with equivalent permissions, and that the API access option is enabled. | 
| 409 Conflict (CODE 1965) | API rate limit exceeded | The connector reads the X-RateLimit-ToWait-Sec header and retries after the specified wait time. | 
| 409 Conflict (CODE 1960) | Concurrent call limit exceeded | The connector retries with progressive backoff of 5, 10, 30, 60, 120, and 300 seconds. | 
| No data appears in the log group | The pipeline resource policy was not added within 5 minutes | Delete and recreate the pipeline, and then immediately add the CloudWatch Logs resource policy. | 
| XML parse errors | Unexpected response format or API version change | Verify that the hostname is correct and that the Qualys subscription includes access to the VMDR module. | 

During initial backfill, the connector retrieves data for the configured `range` across all four streams. If rate limiting occurs, the connector handles it automatically and no action is required. Enterprise Qualys subscriptions can have higher rate limits; contact Qualys Support to verify your API tier.

The Qualys Activity Log is shared across VMDR, Policy Compliance, Web Application Scanning, and CyberSecurity Asset Management. Events from other modules are ingested and available for search, but might not include VMDR-specific context. This is expected behavior.