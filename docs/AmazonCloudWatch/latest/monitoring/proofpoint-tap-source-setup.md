

# Source configuration for Proofpoint TAP
<a name="proofpoint-tap-source-setup"></a>

## Integrating with Proofpoint TAP
<a name="proofpoint-tap-integration"></a>

CloudWatch Pipelines use the Proofpoint TAP SIEM API, Campaign API, and Forensics API to retrieve security event data. The SIEM API returns message and click events within configurable time windows, while the Campaign and Forensics APIs provide detailed threat campaign information and sandbox analysis results. All API endpoints are available at `https://tap-api-v2.proofpoint.com`.

To integrate CloudWatch Pipelines with Proofpoint TAP, complete the following steps:

1. Configure Proofpoint TAP authentication credentials:
   + Log in to the Proofpoint TAP Threat Insight Dashboard.
   + Navigate to Settings > Connected Applications > Service Credentials.
   + Generate a new service credential.
   + Note the Service Principal and Secret values.

1. Store the `servicePrincipal` and `secret` in AWS Secrets Manager.

1. Create a CloudWatch Logs log group for the pipeline output.

1. Create an IAM role with AWS Secrets Manager access and a trust relationship for the pipeline.

1. Configure and create the CloudWatch pipeline.

## Prerequisites
<a name="proofpoint-tap-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active Proofpoint TAP account with Threat Insight Dashboard access
+ A TAP service credential with SIEM, Campaign, and Forensics API access
+ An AWS account with permissions to create and manage CloudWatch Pipelines
+ An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with Proofpoint TAP
<a name="proofpoint-tap-authentication"></a>

Proofpoint TAP uses HTTP Basic authentication with a service principal and secret. The pipeline sends these credentials with each API request to authenticate access to the SIEM, Campaign, and Forensics endpoints.

## Configure Authentication for Proofpoint TAP
<a name="proofpoint-tap-configure-auth"></a>

To configure authentication credentials for the pipeline:

1. Log in to the Proofpoint TAP Threat Insight Dashboard.

1. Navigate to Settings > Connected Applications > Service Credentials.

1. Generate a new service credential.

1. Note the Service Principal and Secret values.

1. Store the `servicePrincipal` and `secret` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline
<a name="proofpoint-tap-pipeline-config"></a>

To configure the pipeline, choose Proofpoint TAP as the data source. Provide the required `service_principal` and `secret` credentials. After you create and activate the pipeline, security event data from Proofpoint TAP will begin flowing into the selected CloudWatch Logs log group.

The following optional parameters are available:
+ **Polling intervals** – `siem_polling_interval` (default `PT10M`), `clicks_permitted_polling_interval` (default `PT5M`), `campaign_polling_interval` (default `P1D`)
+ **Backfill durations** – `siem_backfill` (default `P1D`), `campaign_backfill` (default `P1D`). Valid range: `PT30S` to `P1D`.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="proofpoint-tap-ocsf-events"></a>

This integration supports the following OCSF event classes:
+ **Email Activity [4009]** – Message Delivered, Click Permitted
+ **Detection Finding [2004]** – Message Blocked, Click Blocked
+ **OSINT Inventory Info [5021]** – Campaign, Forensic Evidence