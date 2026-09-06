

# Source configuration for Wazuh Platform
<a name="wazuh-platform-source-config"></a>

## Integrating with Wazuh Platform
<a name="wazuh-platform-integration"></a>

Wazuh Platform is an open-source security monitoring platform that delivers threat detection, file integrity monitoring, vulnerability assessment, and compliance across endpoints and cloud workloads. Use CloudWatch pipelines with the Wazuh Platform API (an Elasticsearch-compatible REST API) to retrieve security alerts, vulnerability findings, system inventory, and agent monitoring data from your self-hosted Wazuh Platform instance. The Indexer API provides search endpoints that you can use to access event data stored in daily-rotated indices, so you can collect security logs from your Wazuh Platform environment for centralized monitoring and analysis.

To integrate CloudWatch Pipelines with Wazuh Platform, complete the following high-level steps:
+ Obtain the Wazuh Indexer host URL and credentials.
+ Store the username and password in AWS Secrets Manager.
+ Create a CloudWatch pipeline with Wazuh Platform as the data source.
+ Verify that data is flowing into the pipeline.

## Prerequisites
<a name="wazuh-platform-prerequisites"></a>

Before you begin, make sure you have the following:
+ The Wazuh Indexer installed and running. Follow the official quickstart guide to install: [Quickstart - Wazuh documentation](https://documentation.wazuh.com/current/quickstart.html#installing-wazuh)
+ Wazuh Indexer accessible over HTTPS (port 9200 or 443 with reverse proxy)
+ Network connectivity from the pipeline to the Wazuh Indexer host (if behind a firewall, allow the pipeline's egress IPs)
+ Valid credentials with Basic Auth (username/password) that have read permissions on the target indices
+ User role permissions with at minimum `indices:data/read/search` on the target index patterns (for example, `wazuh-alerts-*`, `wazuh-states-*`)
+ A sortable `timestamp` field present in the documents for incremental ingestion and `search_after` pagination (for inventory indices this may need to be added manually)
+ If using self-signed TLS certificates, the pipeline must trust the CA
+ An AWS account with permissions to create and manage CloudWatch Pipelines
+ An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with Wazuh Platform
<a name="wazuh-platform-authentication"></a>

To read Wazuh Platform data, the pipeline needs to authenticate with your Wazuh Indexer instance. The plugin supports HTTP Basic Authentication (username/password).

Follow these steps to configure authentication:

1. Ensure your Wazuh Indexer is installed and running. The Indexer runs on port 9200 over HTTPS. Verify access by running: `curl -k -u <username>:<password> https://<wazuh-host>:9200/`

1. Identify or create a user with read access to the required indices (`wazuh-alerts-*`, `wazuh-monitoring-*`, `wazuh-states-inventory-*`). The default `admin` user has full access. For production, create a dedicated read-only user through the Security plugin API.

1. In AWS Secrets Manager, create a secret that will hold the Wazuh Indexer credentials. The secret's value must be a JSON object with keys for `username` and `password`. For example, create a secret named `wazuh-credentials` with the following JSON value:

   ```
   {"username": "admin", "password": "your-wazuh-indexer-password"}
   ```

   The corresponding pipeline references are `${{aws_secrets:wazuh-credentials:username}}` and `${{aws_secrets:wazuh-credentials:password}}`.

1. Ensure network connectivity from the pipeline to the Wazuh Indexer host on port 9200/443.

1. If using self-signed TLS certificates (default for Wazuh), configure the pipeline to trust the Wazuh CA certificate, or disable certificate verification in the pipeline configuration.

## Configuring the CloudWatch Pipeline
<a name="wazuh-platform-pipeline-config"></a>

When configuring the pipeline to read logs, choose Wazuh Platform as the data source. Provide the Host URL (your Wazuh Indexer endpoint including port 9200/443) and Authentication credentials. The pipeline will poll for new data at the configured interval. After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="wazuh-platform-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0 and transforms the following events. Events that are not listed but pulled are not mapped to OCSF and will be forwarded to the sink as raw logs.

### Authentication (3002)
<a name="wazuh-platform-ocsf-authentication"></a>

Contains authentication success and failure events including SSH, PAM, and Windows logon events.

### Vulnerability Finding (2002)
<a name="wazuh-platform-ocsf-vulnerability"></a>

Contains [Vulnerability Detection findings](https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/index.html) including CVE findings from vulnerability scanning.

### File System Activity (1001)
<a name="wazuh-platform-ocsf-filesystem"></a>

Contains [File Integrity Monitoring events](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/index.html) including file addition, modification, and deletion.

### Device Inventory Info (5001)
<a name="wazuh-platform-ocsf-device-inventory"></a>

Contains [System Inventory](https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/viewing-system-inventory-data.html#system) and Agent monitoring events.

### Detection Finding (2004)
<a name="wazuh-platform-ocsf-detection"></a>

Contains Rootcheck events generated for [malware detection](https://documentation.wazuh.com/current/user-manual/capabilities/malware-detection/index.html).

### Application Lifecycle (6002)
<a name="wazuh-platform-ocsf-application-lifecycle"></a>

Contains [Container Security events](https://documentation.wazuh.com/current/user-manual/capabilities/container-security/index.html).

### Compliance Finding (2003)
<a name="wazuh-platform-ocsf-compliance"></a>

Contains [SCA compliance events](https://documentation.wazuh.com/current/user-manual/capabilities/sec-config-assessment/index.html).

### Remediation Activity (7001)
<a name="wazuh-platform-ocsf-remediation"></a>

Contains [Active Response events](https://documentation.wazuh.com/current/user-manual/capabilities/active-response/index.html).

### API Activity (6003)
<a name="wazuh-platform-ocsf-api-activity"></a>

Contains [Cloud Security events](https://documentation.wazuh.com/current/cloud-security/monitoring.html) from Amazon, Azure, GCP, GitHub, and Office365.