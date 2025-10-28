# Service management

The IT service management (ITSM) framework enables enterprises to
align the relationship between people, process, and tooling needed
through the lifecycle of IT services. The service management
framework is also used to create evidentiary support for compliance
and risk audits, Cloud Financial Management (CFM) capabilities, and
business service requests. Enterprises also use ITSM tools to track
business approvals, capture service issue resolutions, inventory
technical assets, identify customer technical inquiries, and capture
data points to make business decisions. These ITSM tools not only
handle the daily operations for business services and applications
(incidents/tickets, and CMDB transparency) but also enable everyday
workflow and approvals of business requests (for example, facilities,
HR, marketing, etc.). Integrating your service management framework
to managing and governing your cloud capabilities will increase your
operational excellence and agility.

The M&G Guide recommends five capabilities as a baseline for your
service management framework within your AWS environments:

- Provisioning and request management
- Event and incident management
- Problem management
- Resource inventory management
- Change management

## Provisioning and request management

Provisioning procedures help plan, implement, and maintain a stable
technical infrastructure to support organizational business
processes. Provisioning focuses on repeatable, standardized,
approved, and curated templates to ensure resilient, cost effective,
scalable resources. It enables enterprises to transition to a
mindset of “infrastructure as code.”

Request management helps in maintaining the curated templates as Service Catalog items. Fulfillment to enterprise end users for any
of the AWS services and infrastructure is ensured by Service Catalog through an automated workflow-driven process. The M&G
Guide recommends integrating your provisioning, request, and
distribution processes with your ITSM tool suite.

## Event and incident management

Event and incident management enables enterprises to control and restore environments and data.
Event management helps in understanding what is currently happening, detect events, assess
potential impact, and determine the appropriate control action. Event management provides the
ability to detect and interpret environment issues, and initiate appropriate response and remediation.
It is a basis for operational monitoring and control and an entry point for many service operation activities.
Automation should be implemented where necessary, based on operations data and metrics. Analyzing event,
incident, and operations metrics will support continual service improvement activities of service assurance.
This analysis is used as inputs for organizational SLAs.

Incident management restores normal service operation and minimizes
adverse business impacts on operations. Combining trend metrics with
the identification of common or adverse patterns in service designs,
can also help inform service availability design and reporting
calculations. The M&G Guide recommends you enable an issue
management mechanism across your AWS accounts. Integrating AWS
events with other ITSM processes, such as incident and change
management, can also increase your ability to scale.

## Problem management

Problem management focuses on identifying and resolving underlying issues (root cause) in the production
environment that can lead to incidents. Problems are the underlying causes of incidents. Initially, problem
management enables you to resolve the root causes of incidents to minimize impact and prevent them from
happening again. Over time, problem management enables you to predict similar incidents using trend analysis
and helps you proactively correlate incidents.

The main focus of problem management is root-case analysis (RCA)
with the goal of identifying why an incident occurred and defining
measures so that similar incidents don’t happen to resources such as
applications, infrastructure, and procedures. At the core, problem
management capabilities include RCA, incident analysis, knowledge
management, collaboration, and reporting. The M&G Guide
recommends that you extend and update existing incident and problem
management capabilities with specific roles and responsibilities,
support escalation paths, and standard operating procedures for your
AWS environments.

## Resource inventory management

Resource inventory management provides the ability to define and
control the components of services and infrastructure, and maintain
accurate configuration records. The configuration management
database (CMDB) ensures assets required to deliver services are
properly controlled, and that accurate and reliable information
about those assets is continuously available. The goal of
configuration management is to define and control service components
and maintain accurate configuration records. CMDB provides a single
source of truth of resources and their relationships. The CMDB
enables resource transparency for:

- Compliance with corporate governance
- Audit support
- Visibility into service assets and their dependencies
- Cost optimization
- Effective change (impact analysis) and release management
- Faster incident and problem resolution

The CMDB ensures that systems configuration management is ubiquitous
and scalable. As AWS adoption progresses and more applications are
deployed and running on AWS, the complexity and interdependence
might become challenging. The M&G Guide recommends using
hierarchical configuration management tools to help manage
configurations across account, environment, stack, application, and
versions.

## Change management

Change management provides the ability to request, prioritize,
authorize, and approve, schedule, and implement changes to assets.
This helps provide a balanced approach to modify IT services while
minimizing the risk to production environments. The evidentiary
controls included with change management functions allow for ease of
audit and compliance reporting. Distributing your infrastructure as
code in your multi-account framework should be part of change
management processes and approval. This basis facilitates the
automation of changes and provides for the documentation, review,
and storage of changes in configuration management tools. The
M&G Guide recommends that you develop an iterative approach for
integrating change management with automation and distribution
functions.
