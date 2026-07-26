# Source configuration for Wazuh Platform

## Integrating with Wazuh Platform

CloudWatch Pipeline uses the Wazuh Indexer API to retrieve security alerts, agent monitoring data, and inventory information. The Indexer API (OpenSearch-based, port 9200) exposes REST endpoints for querying time-filtered security event data.

To integrate CloudWatch Pipelines with Wazuh Platform, complete the following high-level steps:

- Obtain the Wazuh Indexer host URL and credentials.
- Store the username and password in AWS Secrets Manager.
- Create a CloudWatch pipeline with Wazuh Platform as the data source.
- Verify that data is flowing into the pipeline.

## Prerequisites

Before you begin, ensure you have the following:

- An active Wazuh deployment with Indexer API access (port 9200)
- Wazuh Indexer credentials with read access to security indices
- An AWS account with permissions to create and manage CloudWatch Pipelines
- An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with Wazuh Platform

Wazuh Platform uses Basic Authentication with a username and password. The pipeline uses these credentials to authenticate each API request to the Wazuh Indexer.

## Configure Authentication for Wazuh Platform

To configure authentication credentials for the pipeline:

1. Obtain the Wazuh Indexer admin username and password from your Wazuh deployment.
2. Store the `username` and `password` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline

To configure the pipeline, choose Wazuh Platform as the data source. Provide the `host`, `username`, and `password`. Once you create and activate the pipeline, log data from Wazuh will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports the following OCSF event classes:

- **API Activity [6003]** – Wazuh API activity events
- **Application Lifecycle [6002]** – Application lifecycle events
- **Authentication [3002]** – Authentication events
- **Compliance Finding [2003]** – Compliance findings
- **Detection Finding [2004]** – Threat detection findings
- **Device Inventory Info [5001]** – Agent inventory information
- **File System Activity [1001]** – File integrity monitoring events
- **Remediation Activity [1007]** – Remediation actions
- **Vulnerability Finding [2002]** – Vulnerability assessment findings
