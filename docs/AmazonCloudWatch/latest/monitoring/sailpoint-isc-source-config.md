

# Source configuration for SailPoint ISC
<a name="sailpoint-isc-source-config"></a>

## Supported API and schema versions
<a name="sailpoint-isc-supported-versions"></a>
+ **SailPoint ISC Search API v2026** – Primary endpoint for retrieving audit events.
+ **OCSF schema v1.5.0** – Open Cybersecurity Schema Framework mapping.
+ **OAuth 2.0 Client Credentials** – Token-based authentication using Personal Access Token (PAT) credentials.

## Prerequisites
<a name="sailpoint-isc-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active SailPoint Identity Security Cloud tenant with API access enabled.
+ A user account with the `ORG_ADMIN` user level, which is required to access all audit events.
+ Your SailPoint tenant name and API domain.
+ An AWS account with permissions to create and manage CloudWatch pipelines. For more information, see [API caller permissions](pipeline-iam-reference.md#api-caller-permissions).
+ An AWS account with permissions to create and update secrets in AWS Secrets Manager, and a source role that can retrieve the stored credentials. For more information, see [Third-party sources (API Pull)](pipeline-iam-reference.md#third-party-api-pull).
+ An AWS account with permissions to create and manage CloudWatch Logs log groups. For more information, see [CloudWatch Logs API operations and required permissions for actions](permissions-reference-cw.md#cwl-permissions-table).

## Configuring SailPoint ISC
<a name="sailpoint-isc-configure-product"></a>

To configure SailPoint ISC for the integration:

1. Sign in to SailPoint Identity Security Cloud as an `ORG_ADMIN` user.

1. In the SailPoint Admin UI, find **Org Details**. Note your tenant name and the API base URL, which uses the format `https://{tenant}.api.identitynow.com`. Do not derive the base URL from the address that you use to open the user interface, because that address might be a vanity URL.

1. Choose your user name, and then choose **Preferences**.

1. Choose **Personal Access Tokens**, and then choose **New Token**.

1. Enter a description for the token.

1. Turn on the `sp:scopes:all` scope, and then choose **Create Token**.

1. Copy the Client ID and Client Secret for API authentication.

## Authenticating with SailPoint ISC
<a name="sailpoint-isc-authentication"></a>

The connector uses the OAuth 2.0 Client Credentials Grant flow. The pipeline exchanges the stored `client_id` and `client_secret` at the SailPoint token endpoint for a short-lived bearer access token in JSON Web Token (JWT) format. SailPoint reports the remaining lifetime of each token in the `expires_in` field of the token response, and the connector refreshes the token before it expires. No user interaction is required after initial setup.

Open the AWS Secrets Manager console, choose **Store a new secret**, choose **Other type of secret**, and then add the following key-value pairs:
+ `client_id` – Your SailPoint PAT Client ID.
+ `client_secret` – Your SailPoint PAT Client Secret.

For example, name the secret `sailpoint-isc/pipeline-credentials`.

## Configuring the CloudWatch pipeline
<a name="sailpoint-isc-configure-pipeline"></a>

1. Create the destination CloudWatch Logs log group. In the CloudWatch console, choose **Logs**, **Log groups**, **Create log group**, and then enter a descriptive name. For example, use `/aws/cloudwatch/pipelines/sailpoint-isc`.

1. Create a source IAM role with the required permissions. For information about the required policies and permissions, see [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md).

1. Open the CloudWatch console, navigate to **Pipelines**, and choose SailPoint ISC as the data source.

1. Configure OAuth 2.0 client credentials using the `client_id` and `client_secret` stored in AWS Secrets Manager.

1. Provide the SailPoint ISC API base URL and select the destination log group.

1. Verify the destination log group resource policy. For a new log group, the console creates the resource policy automatically. If the log group that you select already has a resource policy, the console warns you that the log group already has a resource policy and that you might need to modify the existing policy to add the permissions that pipelines need to write to the destination log group. In that case, update the existing resource policy within five minutes of pipeline creation to include the required pipeline write permissions. For more information, see [Resource policies](pipeline-iam-reference.md#resource-policies).

1. Wait a few minutes for the initial data pull, check the destination log group for incoming events, and monitor [pipeline metrics](pipelines-metrics.md) for successful ingestion.

**Note**  
When you create the pipeline using the AWS CLI or API, a resource policy is never created automatically, regardless of whether the log group is new or existing. You must create the CloudWatch Logs resource policy manually before the pipeline becomes active.

## Supported Open Cybersecurity Schema Framework event classes
<a name="sailpoint-isc-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0. All SailPoint ISC audit events are retrieved from a single [SailPoint ISC Search API](https://developer.sailpoint.com/docs/api/v2026/search-post) endpoint and mapped to OCSF classes based on their event type category.

**Note**  
Events that do not match an OCSF mapping transformation are automatically passed through and sent directly to the configured sink without additional processing.

### Authentication (3002)
<a name="sailpoint-isc-ocsf-authentication"></a>

`AUTH` – Authentication events for Personal Access Token lifecycle operations, including token usage.

### Account Change (3001)
<a name="sailpoint-isc-ocsf-account-change"></a>
+ `PASSWORD_ACTIVITY` – Password change, reset, and policy enforcement events.
+ `PROVISIONING` – Account provisioning and deprovisioning actions across connected sources.

### Entity Management (3004)
<a name="sailpoint-isc-ocsf-entity-management"></a>
+ `USER_MANAGEMENT` – User lifecycle events including creation, modification, and deletion.
+ `ACCESS_ITEM` – Access item creation, modification, and removal events.
+ `CERTIFICATION` – Access certification campaign events including decisions and sign-offs.
+ `SOURCE_MANAGEMENT` – Source connector configuration and management events.
+ `SYSTEM_CONFIG` – System configuration and platform settings change events.
+ `NON_EMPLOYEE` – Non-employee lifecycle management events.
+ `IDENTITY_MANAGEMENT` – Identity profile and attribute management events.

### User Access Management (3005)
<a name="sailpoint-isc-ocsf-user-access-management"></a>

`ACCESS_REQUEST` – Access request submission, approval, and denial events.

### Ingestion-only event types
<a name="sailpoint-isc-ocsf-ingestion-only"></a>

The following event types do not have an OCSF mapping and are forwarded to the sink without additional processing:
+ `SSO` – Single sign-on events.
+ `IAI_ADMIN_AUDIT` – AI-based identity analytics administrator audit events.

## Known platform limitations
<a name="sailpoint-isc-limitations"></a>
+ **Search result paging limit** – The SailPoint Search API returns a maximum of 10,000 records for each page and limits offset-based paging to a total of 10,000 records for a single query. The connector uses one-hour time partitions so that each query window stays within the 10,000-record paging ceiling. High-volume tenants that generate more than 10,000 events in one hour might exceed the paging ceiling for that window.
+ **API rate limits** – The limit is 100 requests per `client_id`, per API version, per 10 seconds, which is effectively 10 requests per second. When SailPoint returns an HTTP 429 response, the connector retries with progressively increasing delays. The limit applies per `client_id`, not per access token.
+ **Token expiration** – SailPoint issues short-lived access tokens and reports the remaining lifetime of each token in the `expires_in` field of the token response. The connector refreshes the token before it expires, so no manual intervention is required.
+ **Maximum PATs per user** – SailPoint supports a maximum of 10 Personal Access Tokens per user. Plan your token allocation if the same administrator user needs Personal Access Tokens for multiple integrations.
+ **Event time-based filtering** – The connector collects events by the time in the `created` field, not by the time that SailPoint indexed the event. Because the connector queries a closed time window, an event that becomes searchable after the window that contains its `created` time was queried is not collected.

## Troubleshooting
<a name="sailpoint-isc-troubleshooting"></a>

`401 Unauthorized`  
The client credentials are invalid or expired. Verify the `client_id` and `client_secret` stored in AWS Secrets Manager, and generate a new PAT in SailPoint if necessary.

`403 Forbidden`  
The PAT might have insufficient permissions. Make sure that the `sp:scopes:all` scope is turned on for the token, and that the token was generated by a user with the `ORG_ADMIN` user level. Create a new PAT with the correct user and scope if necessary.

`429 Too Many Requests`  
The API rate limit of 10 requests per second for each `client_id` was exceeded. The connector automatically retries with progressively increasing delays. If the error persists, verify that other integrations are not sharing the same `client_id`.

No data appears in the log group  
The pipeline resource policy might not have been added within five minutes. Delete and recreate the pipeline, and then immediately add the CloudWatch Logs resource policy.

`400 Bad Request`  
The API base URL might be malformed or contain an incorrect tenant or domain. Verify that `base_url` uses the format `https://{tenant}.api.{domain}.com`. Check the tenant name in the SailPoint Admin UI under **Org Details**.

**No events are returned despite valid credentials**
+ Verify that the PAT user has `ORG_ADMIN` privileges. Users with lower privilege levels might not have access to all audit event types.
+ Check whether the tenant has events within the configured `range`. A newly provisioned tenant might not have historical data.

**Some event types are missing**
+ Confirm that the `sp:scopes:all` scope is turned on for the PAT. Restricted scopes might limit which event types are accessible.
+ Check whether the event type has an OCSF mapping. Event types that have no mapping, such as `SSO`, are still delivered to the sink, but they are delivered in their original form instead of as OCSF events.

**Vanity URL confusion**

Some SailPoint deployments use vanity URLs, such as `iga.acme.com`, for the user interface. The `base_url` must use the API endpoint format `https://{tenant}.api.{domain}.com`. Find your tenant name in the SailPoint Admin UI under **Org Details**. After you know your API host, you can call the OAuth information endpoint at `https://{tenant}.api.identitynow.com/oauth/info` to confirm the tenant ID and the OAuth endpoints for the tenant.