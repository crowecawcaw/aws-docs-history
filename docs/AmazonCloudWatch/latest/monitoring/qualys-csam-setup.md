

# Qualys CSAM integration configuration
<a name="qualys-csam-setup"></a>

Qualys CyberSecurity Asset Management (CSAM) provides visibility into your IT asset inventory, software components, and domain intelligence. It discovers and catalogs assets across on-premises, cloud, and container environments, and it tracks the software installed on them, including lifecycle and authorization status. It also identifies vulnerabilities in your internet-facing assets through External Attack Surface Management (EASM), and it detects unresolved and typosquatted domains.

CloudWatch pipelines use the Qualys CSAM REST API to retrieve asset inventory, software components, vulnerability findings, and domain intelligence data from your Qualys tenant. The API provides paginated REST endpoints with JSON Web Token (JWT) bearer token authentication for retrieving security asset data for monitoring and analysis.

**Topics**
+ [Source configuration for Qualys CSAM](qualys-csam-source-config.md)
+ [CloudWatch pipelines configuration for Qualys CSAM](qualys-csam-pipeline-setup.md)
+ [Known Qualys CSAM platform limitations](qualys-csam-limitations.md)
+ [Troubleshooting the Qualys CSAM integration](qualys-csam-troubleshooting.md)