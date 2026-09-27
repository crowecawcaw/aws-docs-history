

# Qualys VMDR integration configuration
<a name="qualys-vmdr-setup"></a>

Qualys Vulnerability Management, Detection and Response (VMDR) is a cloud-native vulnerability management platform. It provides continuous discovery, assessment, prioritization, and remediation of vulnerabilities across on-premises, cloud, container, and hybrid environments. It combines asset discovery and vulnerability scanning with prioritization based on TruRisk, the proprietary Qualys risk-scoring model, and integrated patch management.

CloudWatch pipelines poll the Qualys REST APIs to ingest vulnerability knowledge base data, asset inventory, host detection findings, and platform activity logs.

**Topics**
+ [Source configuration for Qualys VMDR](qualys-vmdr-source-config.md)
+ [CloudWatch pipelines configuration for Qualys VMDR](qualys-vmdr-pipeline-setup.md)