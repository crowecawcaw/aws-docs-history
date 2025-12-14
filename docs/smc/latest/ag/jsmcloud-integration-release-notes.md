# Release notes

The AWS Service Management Connector is for Atlassian's Jira Service Management Cloud, an
application based on [Forge](https://developer.atlassian.com/platform/forge/ "https://developer.atlassian.com/platform/forge/"). The
connector is available from [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1221283/aws-service-management-connector-for-jsm-cloud "https://marketplace.atlassian.com/apps/1221283/aws-service-management-connector-for-jsm-cloud"). The latest version integrates with
AWS Systems Manager OpsCenter and AWS Health.

## Version 6.6.0

**Core features**

- Improved reliability of resource installation process.

**AWS Systems Manager OpsCenter
integration**

- Create and update Jira issues when you create and update
  operational items (AWS OpsItems) in AWS Systems Manager OpsCenter.
- Update OpsItems in AWS Systems Manager OpsCenter when you update the Jira
  issue in Jira Service Management Cloud.
- View and run AWS Systems Manager automation runbooks to resolve OpsItems
  and view results of the Jira issues.
- Synchronize action-item type OpsItems from
  AWS Systems Manager Incident Manager.
- Creates a relationship between synced incidents from Incident Manager
  and the associated OpsItem.

**AWS Health integration**

- Creates Jira issues from AWS Health events.
- Supports affected resource tracking for planned lifecycle
  events.
- Supports pagination by syncing health events with visual
  information about the progress.
- Supports AWS Organizations to view and consolidate multiple AWS
  accounts through Amazon EventBridge.

## Version 6.0.0

**Core features**

- Resolves an issue during installation that creates workflows,
  issue types, and other resources.
- Upgrades packages to address vulnerabilities.

**AWS Systems Manager Incident Manager integration**

- Resolves an intermittent issue with the Incident Manager integration
  that delays ticket creation.

**AWS Security Hub CSPM integration
enhancement**

- Resolves an issue with duplicate fields that causes an _Error in Data_ issue when viewing the
  Security Hub CSPM details panel.
- Enhances logging for Security Hub CSPM integration.

## Version 5.7.0

**Core features**

- To avoid timeouts, the connector installation now uses the Forge
  Async events API.

## Version 5.6.0

**Core features**

- Resolved site-specific issues with AWS Security Hub CSPM sync
- Improved throttling exception handing for AWS Systems Manager Automation
  sync
- Package dependency update

## Version 5.0.0

**Support integration**

- Configure dual synchronization of Support cases as Jira issues
- View, create, resolve, and add correspondences to Support tickets
  directly from Jira issues

**AWS Systems Manager Automation
integration**

- Render AWS Systems Manager automation documents in the Jira Service
  Management Agent views
- Request and execute AWS Systems Manager automation documents through Jira
  Service Management

## Version 4.4.0

**AWS Security Hub CSPM integration**

- Corrected the invalid request type message to appear on the
  "update product issue" action only, and excluded from display on the
  main portal view

## Version 4.2.0

**AWS Security Hub CSPM integration**

- Enhanced logging for AWS Security Hub CSPM integration

**Core features**

- Improved the connector configurations filter to allow only
  selection of Jira Service Desk project types

## Version 4.0.0

**AWS Service Catalog integration**

- Render AWS Service Catalog portfolios and products in Jira Service
  Management using the Customer Portal view

**Core features**

- Implement appropriate endpoint to support AWS Service Catalog integration
  for China Regions into the Connector for Jira Service Management

## Version 3.9.0

**AWS Security Hub CSPM integration
enhancement**

- Additional error trapping and enhanced logging for configuration
  errors

## Version 3.8.0

**AWS Service Catalog integration**

- Render AWS Service Catalog portfolios and products in Jira Service
  Management using the Jira Agent view
- Associate Jira Service Management approval groups to AWS Service Catalog
  portfolios to require approvals for Jira Service Management user
  product requests
- Configure AWS product request form components available for
  internal customers and Jira agents to view
- Create AWS Tags across provisioned products
- View AWS-specific parameters on Amazon EC2 resources, such as
  Availability Zones, Image ID, Instance ID, KeyPair, Security Group,
  and VPC

**AWS Security Hub CSPM integration**

- Configure synchronization behavior of AWS Security Hub CSPM Findings within
  Jira Service Management Cloud
- Create, view, update, investigate and resolve AWS Security Hub CSPM Findings
  as Jira issues

**AWS Systems Manager Incident Manager integration**

- Sync Incident Manager incidents as Jira Issues
- Provide configuration to allow bidirectional or unidirectional
  synchronization of the `resolved` status between a Jira
  Issue and the corresponding AWS incident
