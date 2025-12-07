# Source configuration for ServiceNow CMDB Audit Log

## Integrating with ServiceNow CMDB

ServiceNow is an enterprise platform that provides IT service management (ITSM) and configuration management database (CMDB) capabilities for tracking and managing IT assets, configurations, and changes across organizations. CloudWatch Pipeline uses the ServiceNow Table API to retrieve information about sys_audit, syslog, sysevent, and syslog_transactions from your ServiceNow instance.

## Authenticating with ServiceNow CMDB

To read the logs, the pipeline needs to authenticate with your ServiceNow instance. The ServiceNow Table API supports OAuth 2.0.

- Ensure the REST API is enabled on your ServiceNow instance.
- Enable OAuth 2.0 Client Credentials grant type in your ServiceNow instance
- Create an OAuth Application Registry for external client authentication
- In the AWS Secrets Manager, create a secret and store the Application (client) ID under the key `client_id` and the client secret under the key `client_secret`.
- Configure OAuth Application User and assign required roles

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read audit logs from ServiceNow choose ServiceNow CMDB as the data source. Fill in the required information like `instance_url` and the secret where `client_id` and `client_secret` are stored. Once you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and events that map to Entity Management (3004), API Activity (6003), and Datastore Activity (6005). These events are from specific tables and filtered for CMDB reference.

**Entity Management** contains events from following tables:

- sys_audit

**API Activity** contains events from following tables:

- sysevent
- syslog

**Datastore Activity** contains events from following tables:

- syslog_transactions
