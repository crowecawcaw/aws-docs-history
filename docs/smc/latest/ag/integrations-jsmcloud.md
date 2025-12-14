# AWS Service Management Connector

for Jira Service Management Cloud

The AWS Service Management Connector (SMC) streamlines cloud operations of AWS resources
with your existing operational IT Service Management (ITSM) tooling. The
AWS Service Management Connector for Atlassian's [Jira
Service Management Cloud](https://www.atlassian.com/software/jira/service-management "https://www.atlassian.com/software/jira/service-management") enables internal customers and Jira
agents to provision, manage, and operate AWS resources natively through
Atlassian's Jira Service Management. Using the Connector for Jira Service
Management Cloud improves the efficiency of Service Management governance
and oversight for AWS resources and services.

The Connector for Jira Service Management Cloud enables role-specific
tasks for Jira internal customers and Jira agents.

Jira Service Management **administrators**
can

- Provide pre-approved, secured, and governed AWS resources to Jira
  agents and internal customers through AWS Service Catalog.
- Configure synchronization and associate Jira projects for AWS Security Hub CSPM
  integration.
- Configure incident resolution behavior and associate Jira projects
  for AWS Systems Manager Incident Manager.
- Configure synchronization and associate Jira projects for Support
  integration.
- Provide access to Jira agents to execute AWS Systems Manager Automation
  Documents.
  Jira Service Management **internal customers and
  Jira agents** can

- Browse, request, and provide pre-secured AWS solutions.
- View, update, and resolve AWS Security Hub CSPM findings as Jira issues.
- View and resolve incidents affecting AWS-hosted applications
  through AWS Systems Manager Incident Manager.
- View, create, add correspondences, and resolve Support cases from Jira
  Service Management (including AMS Accelerate support cases).
- View and execute AWS Systems Manager Automation Documents.
  These features minimize direct AWS console access and simplify AWS
  product requests and operational actions for Jira Service Management Cloud
  internal customers and Jira agents. This ensures efficient service
  management governance and oversight over AWS resources and services.

AWS Service Management Connector is built using [Forge](https://developer.atlassian.com/platform/forge/ "https://developer.atlassian.com/platform/forge/") for
Atlassian's Jira Service Management and is available at no charge in the
[Atlassian Marketplace](https://marketplace.atlassian.com/apps/1221283/aws-service-management-connector-for-jsm-cloud "https://marketplace.atlassian.com/apps/1221283/aws-service-management-connector-for-jsm-cloud"). This feature is generally available in all
AWS Regions where AWS Service Catalog, AWS Security Hub CSPM, AWS Systems Manager Incident Manager Support, and
AWS Systems Manager Automation services are available.

The following AWS services
are integrated with this Connector:

[AWS Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/") provides
a way to manage commonly deployed AWS services and provisioned software.
It can help your organization establish consistent governance and
compliance requirements while limiting users to deploying only approved
AWS services.

[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") provides
a comprehensive view of security alerts and security posture across your
AWS accounts. Security Hub CSPM provides a single location that aggregates,
organizes, and prioritizes alerts (findings).

[AWS Systems Manager Incident Manager](https://aws.amazon.com/incident-manager/ "https://aws.amazon.com/incident-manager/") helps you mitigate and recover from incidents
that affect AWS applications. It improves incident resolutions by
notifying responders of the impact, highlighting relevant troubleshooting
data, and providing collaboration tools.

[AWS Systems Manager
Automation](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") provides a way to automate common and repetitive IT
operations and management tasks. You can use predefined or custom
playbooks to configure AWS resources across multiple accounts and
AWS Regions.

[Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") provides
multiple tools, people, and programs to help you optimize performance,
lower costs, and innovate faster. It addresses best practices,
configuration details, and fixes.

[AWS Health](../../../health.md "../../../health.md") provides
personalized information about events that affect your AWS
infrastructure. It can also guide you through scheduled changes and help
you troubleshoot issues that affect AWS resources and accounts.

[AWS Systems Manager
OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md") provides a central location for operations engineers
and IT professionals to manage work items (OpsItems) related to AWS
resources.

[Atlassian's Jira Service Management](https://www.atlassian.com/software/jira/service-management/features "https://www.atlassian.com/software/jira/service-management/features") is an IT service management
tool that places developers, IT personnel, and business teams on the same
platform so they can deliver services together. Jira Service Management
has request types that provide self-service options and Jira agents that
can deliver IT services like fulfillment approvals and workflows.
