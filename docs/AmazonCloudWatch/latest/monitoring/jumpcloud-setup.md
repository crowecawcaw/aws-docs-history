

# JumpCloud integration configuration
<a name="jumpcloud-setup"></a>

JumpCloud is a cloud-based open directory platform that unifies identity, access, and device management across IT resources. It provides centralized directory services, Single Sign-On (SSO), Multi-Factor Authentication (MFA), RADIUS, LDAP, and device management for organizations managing hybrid environments. CloudWatch pipelines use version 1 of the JumpCloud Directory Insights API to retrieve security and audit events from your JumpCloud tenant. The pipeline requests events from every Directory Insights service, so all of the events that your organization records are delivered to the sink. Events from the directory, SSO, RADIUS, systems, LDAP, and alerts services are transformed into Open Cybersecurity Schema Framework (OCSF) format. Events from any other Directory Insights service are forwarded to the sink without transformation. The API provides a single POST endpoint with cursor-based pagination and API key authentication for comprehensive identity and access event data.

**Topics**
+ [Source configuration for JumpCloud](jumpcloud-source-config.md)
+ [CloudWatch pipelines configuration for JumpCloud](jumpcloud-pipeline-setup.md)