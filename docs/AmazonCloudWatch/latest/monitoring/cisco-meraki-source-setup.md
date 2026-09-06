

# Source configuration for Cisco Meraki
<a name="cisco-meraki-source-setup"></a>

## Integrating with Cisco Meraki
<a name="cisco-meraki-integration"></a>

To integrate Cisco Meraki with CloudWatch Logs, you must configure both the source and the pipeline. First, set up your Cisco Meraki source by configuring API access to the Meraki Dashboard API to retrieve data. Then, configure the CloudWatch pipeline to ingest the data from your source into CloudWatch Logs.

## Authenticating with the Meraki Dashboard API
<a name="cisco-meraki-authentication"></a>

To retrieve events from Cisco Meraki, CloudWatch pipelines needs to authenticate with your Meraki organization. Cisco Meraki supports API key access.

**API key**
+ Generate an API key from the Meraki Dashboard. Navigate to your profile and select **API access** to generate a new API key.
+ In AWS Secrets Manager, create a secret and store the API key under the key `api_key`.
+ API keys are permanent and can be scoped down if needed. Make sure the API key has at least read-only access to the specific organization and the APIs.

For more information on Meraki API authorization, see [Meraki API Authorization](https://developer.cisco.com/meraki/api-v1/authorization/).

## Configuring the CloudWatch Pipeline
<a name="cisco-meraki-pipeline-config"></a>

When configuring the pipeline to read data from Cisco Meraki, choose Cisco Meraki as the data source. Fill in the required information including the Organization ID and the secret where your credentials are stored. You can find your organization ID in the Meraki Dashboard under **Organization > Settings**, or by calling `GET /organizations` through the Cisco Meraki API. After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="cisco-meraki-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0 and Cisco Meraki Dashboard API events that map to Network Activity (4001), API Activity (6003), and Detection Finding (2004).

### Network Activity (4001)
<a name="cisco-meraki-network-activity"></a>

Network Activity maps to Meraki Security Events — IDS/IPS alerts (Snort-based), malware detections through Advanced Malware Protection (AMP), and file scan results from MX security appliances.

API endpoint: `GET /organizations/{organizationId}/appliance/security/events`

### API Activity (6003)
<a name="cisco-meraki-api-activity"></a>

API Activity maps to Meraki Configuration Changes — an audit log of all administrative actions capturing who changed what configuration, when, and the before/after values. Covers changes made through the Dashboard UI and API.

API endpoint: `GET /organizations/{organizationId}/configurationChanges`

### Detection Finding (2004)
<a name="cisco-meraki-detection-finding"></a>

Detection Finding maps to Meraki Assurance Alerts — alerts produced by Meraki's monitoring engine that analyze device telemetry and produce discrete alerts with IDs, severity, and a lifecycle status.

API endpoint: `GET /organizations/{organizationId}/assurance/alerts`