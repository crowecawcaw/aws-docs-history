# AWS Systems Manager (SSM) Documents used by

CloudWatch Application Insights

Application Insights uses the SSM Documents listed in this section to define the actions that
AWS Systems Manager performs on your managed instances. These documents use the `Run Command`
capability of Systems Manager to automate the tasks necessary for carrying out Application Insights monitoring
capabilities. The run schedules for these documents are maintained by Application Insights and can't
be altered.

For more information about SSM Documents, see [AWS Systems Manager Documents](../../../systems-manager/latest/userguide/documents.md "../../../systems-manager/latest/userguide/documents.md") in the
_AWS Systems Manager User Guide_.

## Documents managed by

CloudWatch Application Insights

The following table lists the SSM documents that are managed by Application Insights.

| Document name                                                  | Description                                                                                                                   | Run schedule                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AWSEC2-DetectWorkload`                                        | Auto detects applications running in your application environment that can be set up to be monitored by Application Insights. | This document runs hourly in your application environment<br>to get up-to-date application details.                                                                                                                                                                                                    |
| `AWSEC2-CheckPerformanceCounterSets`                           | Checks whether Performance Counter namespaces are enabled on your Amazon EC2 Windows instances.                               | This document runs hourly in your application environment<br>and only monitors Performance Counter metrics if the<br>corresponding namespaces are enabled.                                                                                                                                             |
| `AWSEC2-ApplicationInsightsCloudwatchAgentInstallAndConfigure` | Installs and configures CloudWatch Agent based on the monitoring configuration of your application components.                | This document runs every 30 minutes to ensure that the<br>CloudWatch Agent configuration is always accurate and up-to-date.<br>The document also runs immediately after a change is made to<br>your application monitoring setup such as adding or removing<br>metrics or updating log configurations. |

## Documents managed by AWS Systems Manager

The following documents are used by CloudWatch Application Insights and managed by Systems Manager.

###### `AWS-ConfigureAWSPackage`

Application Insights uses this document to install and uninstall Prometheus exporter
distributor packages, to collect workload specific metrics, and to enable
comprehensive monitoring of workloads on customer Amazon EC2 instances. CloudWatch Application Insights
installs the Prometheus exporter distributor packages only if the correlated
target workload is running on your instance.

The following table lists the Prometheus exporter distributor packages and the correlated target workloads.

| Prometheus exporter distributor package name                      | Target workload                          |
| ----------------------------------------------------------------- | ---------------------------------------- |
| `AWSObservabilityExporter-HAClusterExporterInstallAndConfigure`   | SAP HANA HA                              |
| `AWSObservabilityExporter-JMXExporterInstallAndConfigure`         | Java/JMX                                 |
| `AWSObservabilityExporter-SAP-HANADBExporterInstallAndConfigure`  | SAP HANA                                 |
| `AWSObservabilityExporter-SAP-SAPHostExporterInstallAndConfigure` | NetWeaver                                |
| `AWSObservabilityExporter-SQLExporterInstallAndConfigure`         | SQL Server (Windows) and SAP ASE (Linux) |

###### `AmazonCloudWatch-ManageAgent`

Application Insights uses this document to manage the status and configuration of
CloudWatch Agent on your instances and to collect internal system level metrics
and logs from Amazon EC2 instances across operating systems.
