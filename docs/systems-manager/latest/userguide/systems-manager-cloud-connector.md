# Set up a Cloud Connector for Microsoft Azure in Systems Manager

A Systems Manager _Cloud Connector_ is a resource that
establishes a connection between Systems Manager and virtual machines (VMs) in an external cloud
provider such as Microsoft Azure. After you create a Cloud Connector, Systems Manager services such
as Automation and State Manager can target and manage Azure VMs as if they were native managed
nodes.

This section includes the following topics.

- [Azure prerequisites](cloud-connector-prereqs-azure.md "cloud-connector-prereqs-azure.md")
- [Manage Cloud Connectors](cloud-connector-manage.md "cloud-connector-manage.md")
- [Enable VM onboarding (AWS Management Console)](cloud-connector-onboarding-console.md "cloud-connector-onboarding-console.md")
- [How Systems Manager handles cloud resources](cloud-connector-identifiers.md "cloud-connector-identifiers.md")
- [Step 1: Create an AWS Config connector](cloud-connector-create-config-connector.md "cloud-connector-create-config-connector.md")
- [Enable VM onboarding (AWS CLI)](cloud-connector-onboarding-cli.md "cloud-connector-onboarding-cli.md")
- [AWS prerequisites](cloud-connector-prereqs-aws.md "cloud-connector-prereqs-aws.md")
- [Prerequisites](cloud-connector-prerequisites.md "cloud-connector-prerequisites.md")
- [Enable VM onboarding](cloud-connector-enable-vm-onboarding.md "cloud-connector-enable-vm-onboarding.md")
- Set up a Cloud Connector for Microsoft Azure in Systems Manager
  Azure VMs onboarded through a Cloud Connector behave as standard hybrid-activated Systems Manager
  managed instances. You can use the same tools and workflows — such as Run Command, Patch
  Manager, and State Manager — to manage them alongside your on-premises and EC2
  nodes.

Creating a Cloud Connector for Azure involves two main steps:

1. Create an AWS Config connector, which sets up the credential exchange
   between AWS and Azure and enables AWS Config to record Azure resource
   state.
2. Create a Systems Manager Cloud Connector, which registers the Azure tenant and
   subscription targets with Systems Manager.

###### Note

- Cloud Connectors support Microsoft Azure at launch. Google Cloud Platform
  support is planned for a future release.
- Systems Manager supports up to 10 Cloud Connectors per AWS account. Each Cloud
  Connector supports up to 75 Azure subscription targets. All Cloud Connectors
  in a single AWS account must target the same Azure tenant.
  For details about the IAM roles that Systems Manager creates on your behalf during the
  connector setup wizard, including their trust policies and permissions policies, see
  [IAM roles created by the Systems Manager console](cloud-connector-console-iam-roles.md "cloud-connector-console-iam-roles.md").
