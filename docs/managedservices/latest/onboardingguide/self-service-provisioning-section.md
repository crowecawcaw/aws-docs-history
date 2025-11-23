# Self-Service Provisioning mode in AMS

AWS Managed Services (AMS) Self-Service Provisioning (SSP) mode provides full access to native AWS service and API capabilities in AMS managed accounts.
You access services through standardized, scoped down, AWS Identity and Access Management roles. AMS provides service requests
and incident management. Alerting, monitoring, logging, patch, back up, and change management are your
responsibility. In many cases, Self-Service Provisioning services (SSPS) are self-managed,
or serverless, and don’t require management of certain operational tasks like patching. You benefit
from using these services within the environment boundary defined by AMS guardrails and any IAM changes
(including service linked roles, service roles, cross-account roles, or policy updates) need to be approved
by AMS Operations to maintain the baseline security of the platform. You can leverage CloudFormation
templates to automate deployment of these services, but this isn't supported for all SSP services.

###### Important

Use SSP mode in your AWS Managed Services (AMS) accounts to access and employ AWS services, with restrictions as noted.

There are some AWS services that you can use without AMS management, in your AMS account. The Self-Service Provisioning mode services,
or SSPS for short, how to add them into your AMS account and FAQs for each, are described in the section.

Self-service provisioning services are offered as is, and you're responsible for managing
them. AMS provides no alerts, monitoring, logging, or patching for the resources
associated with those services. AMS provides IAM roles that enable you to use the service
in your AMS account safely. AMS SLAs do not apply.

For resources that you provision through self-service, AMS provides incident management, detective controls and guardrails, reporting, designated
resources (Cloud Service Delivery Manager and Cloud Architect), security and access, and technical support through service requests. Additionally, where
applicable, you assume responsibility for continuity management, patch management, infrastructure monitoring, and change management for resources
provisioned or configured outside of the AMS change management system.
