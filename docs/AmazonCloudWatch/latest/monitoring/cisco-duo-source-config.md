# Source configuration for Cisco Duo

## Integrating with Cisco Duo

CloudWatch Pipeline uses the Cisco Duo Admin API to retrieve audit logs, authentication activity, administrator actions, and policy-related events from your Cisco Duo environment. The Admin API exposes REST endpoints that allow fetching time-filtered event data for security monitoring and analysis.

To integrate CloudWatch Pipelines with Cisco Duo, complete the following high-level steps:

- Create an Admin API integration in the Duo Admin Panel.
- Note the Integration Key, Secret Key, and API Hostname.
- Store the credentials in AWS Secrets Manager.
- Create a CloudWatch pipeline with Cisco Duo as the data source.
- Verify that data is flowing into the pipeline.

## Prerequisites

Before you begin, make sure you have the following:

- An active Cisco Duo account with Admin API access
- A Cisco Duo auth credential with Admin API access
- An AWS account with permissions to create and manage CloudWatch Pipelines
- An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with Cisco Duo

Cisco Duo uses HMAC Authentication with an integration key and secret key, combined with request signing. The pipeline uses these credentials to authenticate each API request to the Duo Admin API.

## Configure Authentication for Cisco Duo

To configure authentication credentials for the pipeline:

1. Log in to the Duo Admin Panel and navigate to Applications > Protect an Application.
2. Search for "Admin API" and create a new integration.
3. Note the Integration Key, Secret Key, and API Hostname provided by Duo.
4. Grant the "Grant read log" permission to the integration.
5. Store the `integration_key` and `secret_key` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline

To configure the pipeline, choose Cisco Duo as the data source. Provide the `api_host`, `integration_key`, and `secret_key`. After you create and activate the pipeline, log data from Cisco Duo will begin flowing into the selected CloudWatch Logs log group.

The following optional parameters are available:

- **Page sizes** – Default is 100 for all streams. Valid ranges vary by stream.
- **Polling intervals** – Default is `P1D` (one day). Valid range is `PT30M` to `P15D`.
- **Backfill durations** – Default is `P180D` (180 days). Valid range is `PT1H` to `P180D`.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports the following OCSF event classes:

- **Base Event [0]** – Telephony Logs
- **Authentication [3002]** – Authentication Logs
- **Entity Management [3004]** – Activity Logs
- **Device Inventory Info [5001]** – Registered Devices, Phones
- **User Inventory Info [5003]** – Users
