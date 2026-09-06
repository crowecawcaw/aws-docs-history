

# Source configuration for Tenable Vulnerability Management
<a name="tenable-source-setup"></a>

## Integrating with Tenable Vulnerability Management
<a name="tenable-integration"></a>

CloudWatch pipelines use the Tenable REST API to retrieve asset inventories, vulnerability findings, compliance data, scan results, audit logs, and plugin metadata from your Tenable environment. The API exposes REST and bulk export endpoints that allow fetching security data for monitoring and analysis.

To integrate CloudWatch Pipelines with Tenable Vulnerability Management, complete the following high-level steps:
+ Generate an Access Key and Secret Key from the Tenable UI.
+ Store the credentials in AWS Secrets Manager.
+ Create a CloudWatch pipeline with Tenable as the data source.
+ Verify that data is flowing into the pipeline.

## Prerequisites
<a name="tenable-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active Tenable account with the Administrator role
+ An AWS account with permissions to create and manage CloudWatch Pipelines
+ An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager
+ An AWS account with permissions to create and manage CloudWatch Logs log groups

## Authenticating with Tenable Vulnerability Management
<a name="tenable-authentication"></a>

Tenable uses API key authentication with an access key and secret key. The pipeline passes these credentials through the `X-ApiKeys` header to authenticate each API request.

## Configure Authentication for Tenable Vulnerability Management
<a name="tenable-configure-auth"></a>

To configure authentication credentials for the pipeline:

1. Log in to the Tenable Vulnerability Management UI.

1. Navigate to Settings > My Account > API Keys.

1. Generate a new API key pair. Note the Access Key and Secret Key values.

1. Make sure your account has the Administrator role.

1. Store the `access_key` and `secret_key` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline
<a name="tenable-pipeline-config"></a>

To configure the pipeline, choose Tenable as the data source. Provide the `access_key` and `secret_key`. After you create and activate the pipeline, vulnerability management data from Tenable will begin flowing into the selected CloudWatch Logs log group.

The following optional parameters are available:
+ **Export settings** – `chunk_size` (default 1000, range 100–10,000), `export_backfill` (default `P30D`, range 30 minutes–90 days), `export_polling_interval` (default `P1D`, range 30 minutes–7 days)
+ **Backfill durations** – Configure historical backfill for audit logs, plugins, and scans independently.
+ **Polling intervals** – Configure independent polling intervals for audit, scan, and plugin streams.
+ **Page sizes** – Configure the number of records retrieved per API request page.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="tenable-ocsf-events"></a>

This integration supports the following OCSF event classes:
+ **Device Inventory Info [5001]** – Assets
+ **Compliance Finding [2003]** – Compliance
+ **Vulnerability Finding [2002]** – Vulnerability
+ **Scan Activity [6007]** – Scans
+ **Authentication [3002]** – Audit Logs (authentication-related actions)
+ **API Activity [6003]** – Audit Logs (API-related actions)
+ **Account Change [3001]** – Audit Logs (account modification actions)

Plugins are passed as raw data and are not mapped to OCSF event classes.