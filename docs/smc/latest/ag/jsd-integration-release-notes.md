# Release notes

Version 2.0.8 includes updates to core features. Version 2.0.5 of the
AWS Service Management Connector for Jira Service Management introduces
an integration with AWS Systems Manager Incident Manager cases and Jira incidents.

**Version 2.0.8 core features**

- Updated package dependencies.
  **Version 2.0.7 core features**

- Updated version of **aws-sdk** library.
- Fix for XML parser issue.
  **AWS Systems Manager Incident Manager**

- Allows Jira Service Management end users to view and resolve a
  Jira issue when AWS Systems Manager Incident Manager creates or updates an
  incident.
- Automatically relate an AWS incident to the associated AWS
  OpsItem when AWS Systems Manager OpsCenter integration is enabled.
- Allows bidirectional or unidirectional synchronization of the
  ‘resolved’ status between a Jira issue and a corresponding AWS
  incident.
  The latest version also includes prior integrations to AWS services,
  such as Support, AWS Security Hub, AWS Service Catalog, AWS Config, AWS Systems Manager automation, and
  AWS Systems Manager OpsCenter.

**Support**

- Configure dual synchronization of Support cases with Jira Service
  Management incidents.
- View, create, resolve and add correspondences to Support tickets
  directly from Jira Incident.
  **AWS Security Hub integration**

- Configure synchronization of AWS Security Hub Findings within Jira
  Service Management.
- Create, view, investigate and resolve AWS Security Hub Findings as Jira
  issues.
- View updates from synced security Findings Jira Issues in
  AWS Security Hub.
  **AWS Service Catalog**

- Render AWS Service Catalog portfolios and products in the Jira Service
  Management Customer Portal and Jira Agent views.
- Associate Jira Service Management approval groups to AWS Service Catalog
  portfolios to require approvals for Jira Service Management user
  product requests.
- Assign the default Jira user that the Jira workflow engine
  uses.
- Configure AWS product request form components available for end
  users to view.
- Create AWS Tags across provisioned products.
- View AWS specific parameters on EC2 resources, such as
  Availability Zones, Image ID, Instance Id, KeyPair, Security Group,
  and VPC.
  **AWS Config**

- Render AWS Config configuration item details on provisioned AWS
  products through Jira Service Management request.
- View the configuration item relationships in a tree
  structure.
- Associate AWS Config items details to Jira issues.
  **AWS Systems Manager Automation**

- Render AWS Systems Manager automation documents in the Jira Service
  Management Customer Portal and Jira Agent views.
- Request and execute AWS Systems Manager automation documents through Jira
  Service Management.
- Create Jira issues (incidents) that provide actionable remediation
  suggestions through a Connector-specific AWS Systems Manager automation
  document.
  **AWS Systems Manager OpsCenter**

- Create and update a Jira Issue when you create and update an
  operational item (OpsItem) in AWS Systems Manager OpsCenter.
- Update OpsItems in AWS Systems Manager OpsCenter when you update the Jira
  issue in Jira Service Management.
- View and execute automation runbooks to resolve OpsItems and view
  execution results from the Jira Issue.
- Support multiple AWS accounts.
- Support FIPS endpoints and usage in the AWS GovCloud East and
  GovCloud West Regions.
- Support the latest releases of Jira Service Management Server and
  data center versions.
