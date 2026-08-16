# Source configuration for Palo Alto Prisma Cloud

## Integrating with Palo Alto Prisma Cloud

CloudWatch pipelines use the Prisma Cloud CSPM and Compute (CWPP) APIs to retrieve security alerts, vulnerability findings, asset inventories, compliance posture, audit logs, and workload data from your Prisma Cloud tenant. The APIs expose REST endpoints that allow fetching security data for monitoring and analysis.

To integrate CloudWatch Pipelines with Palo Alto Prisma Cloud, complete the following high-level steps:

- Generate an Access Key and Secret Key in the Prisma Cloud Console.
- Identify the CSPM API URL, Compute Console URL, and Compute API version.
- Store the credentials in AWS Secrets Manager.
- Create a CloudWatch pipeline with Palo Alto Prisma Cloud as the data source.
- Verify that data is flowing into the pipeline.

## Prerequisites

Before you begin, make sure you have the following:

- An active Palo Alto Prisma Cloud Enterprise tenant with API access
- A Prisma Cloud user with System Admin or Account Group Read Only role
- An AWS account with permissions to create and manage CloudWatch Pipelines
- An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager
- An AWS account with permissions to create and manage CloudWatch Logs log groups

## Authenticating with Palo Alto Prisma Cloud

Palo Alto Prisma Cloud uses an Access Key and Secret Key for authentication. The pipeline sends these credentials to the CSPM login endpoint, which returns a JWT token for subsequent API access.

## Configure Authentication for Palo Alto Prisma Cloud

To configure authentication credentials for the pipeline:

1. Log in to the Prisma Cloud Console and navigate to Settings > Access Control > Access Keys.
2. Choose **Add** > **Access Key**.
3. Note the Access Key ID and Secret Key.
4. Identify the CSPM API URL based on your tenant region (for example, `https://api.prismacloud.io`).
5. Identify the Compute Console URL by navigating to Compute > Manage > System > Utilities > Path to Console.
6. Identify the Compute API version (available from the bell icon in the Console).
7. Store the Access Key ID as `username` and Secret Key as `password` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline

To configure the pipeline, choose Palo Alto Prisma Cloud as the data source. Provide the `cspm_base_url`, `compute_console_url`, `compute_api_version`, `access_key`, and `secret_key`. After you create and activate the pipeline, security data from Prisma Cloud will begin flowing into the selected CloudWatch Logs log group.

The following optional parameters are available:

- **Page sizes** – Configure the number of records retrieved per API request page.
- **Polling intervals** – Valid range is 10 minutes to 7 days. Uses ISO 8601 duration format.
- **Backfill durations** – Valid range is 1 hour to 90 days. Uses ISO 8601 duration format.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports the following OCSF event classes:

- **Base Event [0]** – Applications
- **Detection Finding [2004]** – Alerts
- **Vulnerability Finding [2002]** – Vulnerabilities
- **Cloud Resources Inventory Info [5023]** – Assets
- **Entity Management [3004]** – Audit Logs
- **Compliance Finding [2003]** – Compliances, Alerts
- **Device Inventory Info [5001]** – Hosts
- **Scan Activity [6007]** – Images, Containers
