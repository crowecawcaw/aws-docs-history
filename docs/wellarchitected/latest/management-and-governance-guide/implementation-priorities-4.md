# Implementation priorities

Implementation priorities for service management include
incorporating or establishing policies and procedures to account
for cloud services. It is a best practice to involve your
operations teams early in a preparation phase before migrating
production workloads using iterative production readiness criteria
and checklists. Use of ITSM tools and integration with AWS
services can be accomplished in an iterative manner. For example,
initially tooling and integration can be implemented manually and
progressing to full automation in later phases. The M&G Guide
recommends that you implement service
management framework processes in a phased approach that
establishes a cloud operational baseline and connects with your
system of record declared ITSM tools.

## Integrate provisioning processes with the ITSM tool suite

Infrastructure as code templates are the cornerstone of
distribution, but also enable full service management. Integrating
your provisioning and distribution processes with your ITSM tool
suite is an essential step. Prioritize common requests for
self-service in your ITSM tool. When creating a service template
naming convention across your accounts and workloads, establish a
lifecycle management process using approvals and standard workflow
processes. Build templates with operational metadata (tags) and
parameters to be populated in alignment with the configuration
management system. Sensitive data should not be used for tag keys
or values. Ensure that template access is enforced across both
distribution and ITSM tooling permissions.

## Enable event, incident, and problem management across your

environment

Enable an issue management mechanism such as ticketing across your
AWS accounts. Integrate event management with other ITSM
processes, such as incident and change management. Identify
service owners, dependencies, and third-party integrations
required to scale effectively with updated event store and
sourcing patterns. Extend existing roles, procedures, and
governance activities to accommodate cloud scale. This extension
includes: incident and problem management roles and
responsibilities, support escalation paths, and standard operating
procedures. Establish remediation runbooks for common issue
patterns to improve mean time to repair. Use game-day scenarios to
validate support procedures. Analyze service trends to help
provide recommendations and improve designs of your applications,
resources, and environments on AWS.

## Identify accounts, environments, and resources that require asset

tracking

Identify the accounts, environments, and resources that require
asset tracking for compliance. Update registration in the CMDB as
part of the account and asset provisioning and decommissioning
processes. Track standards (regulatory, enterprise, security,
financial, etc.) and compliance of required resources within AWS
by creating integrations to your ITSM tooling that will enable a
federated view of your AWS services and resources.

## Align change request procedures and policies for rapid cloud

deployment

Align or create change request types in your policies and
procedures that allow rapid deployment of resources. Determine
which service templates (infrastructure as code) can be deemed as
pre-approved changes. Determine how continuous integration and
continuous delivery (CI/CD) pipelines will be accounted for in
your change procedures. Align service and resource change
requests through your ITSM tools.

## Connect your ITSM system of record tooling to AWS

Implementing
[AWS Service Management Connectors](../../../servicecatalog/latest/adminguide/integrations-servicenow.md "../../../servicecatalog/latest/adminguide/integrations-servicenow.md") is composed of three key
steps: configuring AWS native services, configuring ITSM tooling,
and validating your configuration and connectivity.

1. Configuring AWS management and governance services

AWS Service Management Connectors enable integration features for Service Catalog, AWS Config,
AWS Systems Manager Automation, AWS Systems Manager OpsCenter, and AWS Security Hub. AWS Service Management
Connectors requires baseline configurations and permissions to these services. For more
information on these specific requirements, refer to the following documentation:

    * [AWS Service
     Management Connector for ServiceNow](../../../servicecatalog/latest/adminguide/integrations-servicenow.md "../../../servicecatalog/latest/adminguide/integrations-servicenow.md")
    * [AWS
     Service Management Connect for Jira Service Management](../../../servicecatalog/latest/adminguide/integrations-jiraservicedesk.md "../../../servicecatalog/latest/adminguide/integrations-jiraservicedesk.md")

2. Configuring ITSM Tool

AWS Service Management Connectors enable integration for ServiceNow and Atlassian
Jira Service Management. The connector requires you to download the Connector plugin
(scoped app) from the respective ITSM tool platform. For more information on these
specific requirements, refer to the:

    * [[ServiceNow Store App] AWS Service Management Connector for ServiceNow](https://store.servicenow.com/sn_appstore_store.do#!/store/application/f0b117a3db32320093a7d7a0cf961912/ "https://store.servicenow.com/sn_appstore_store.do#!/store/application/f0b117a3db32320093a7d7a0cf961912/")
    * [[Atlassian Marketplace App]
     AWS Service Management Connect for Jira Service Management](https://marketplace.atlassian.com/1221283 "https://marketplace.atlassian.com/1221283")

3. Validating configurations

Once the AWS and ITSM Tooling configurations are complete, the final step is to
validate that AWS and the respective ITSM tool connected successful and the intended
service management actions are enabled. For more information on these validation
actions, refer to the [public documentation](../../../servicecatalog/latest/adminguide/integrations.md "../../../servicecatalog/latest/adminguide/integrations.md")
for the desired ITSM tool.
