

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Set up a Cloud Connector for Microsoft Azure in Systems Manager
<a name="systems-manager-cloud-connector"></a>

A Systems Manager *Cloud Connector* is a resource that establishes a connection between Systems Manager and virtual machines (VMs) in an external cloud provider such as Microsoft Azure. After you create a Cloud Connector, Systems Manager services such as Automation and State Manager can target and manage Azure VMs as if they were native managed nodes.

This section includes the following topics.
+ [Create a Cloud Connector (AWS Management Console)](cloud-connector-create-console.md)
+ [Prerequisites](cloud-connector-prerequisites.md)
+ [Step 1: Create an AWS Config connector](cloud-connector-create-config-connector.md)
+ [Step 2: Create a Systems Manager Cloud Connector](cloud-connector-create-ssm-connector.md)
+ [Manage Cloud Connectors](cloud-connector-manage.md)
+ [Enable VM onboarding](cloud-connector-enable-vm-onboarding.md)
+ [IAM roles created by the Systems Manager console](cloud-connector-console-iam-roles.md)
+ [Tags applied to managed instances](cloud-connector-managed-instance-tags.md)
+ [How Systems Manager handles cloud resources](cloud-connector-identifiers.md)

Azure VMs onboarded through a Cloud Connector behave as standard hybrid-activated Systems Manager managed instances. You can use the same tools and workflows — such as Run Command, Patch Manager, and State Manager — to manage them alongside your on-premises and EC2 nodes.

Creating a Cloud Connector for Azure involves two main steps:

1. Create an AWS Config connector, which sets up the credential exchange between AWS and Azure and enables AWS Config to record Azure resource state.

1. Create a Systems Manager Cloud Connector, which registers the Azure tenant and subscription targets with Systems Manager.

You can create a Cloud Connector in one of two ways. We recommend that you use the AWS Management Console (the wizard generates a setup script that configures the Azure side for you). You can also use the AWS CLI, where you run the Azure setup commands and the create commands yourself.

**Note**  
Cloud Connectors support Microsoft Azure at launch. Google Cloud Platform support is planned for a future release.
Systems Manager supports up to 10 Cloud Connectors per AWS account. Each Cloud Connector supports up to 75 Azure subscription targets. All Cloud Connectors in a single AWS account must target the same Azure tenant.

For details about the IAM roles that Systems Manager creates on your behalf during the connector setup wizard, including their trust policies and permissions policies, see [IAM roles created by the Systems Manager console](cloud-connector-console-iam-roles.md).