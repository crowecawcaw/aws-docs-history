

# Set up a Cloud Connector for Google Cloud Platform in Systems Manager

A Systems Manager *Cloud Connector* is a resource that establishes a connection between Systems Manager and virtual machines (VMs) in an external cloud provider such as Google Cloud Platform (GCP). After you create a Cloud Connector and [enable VM onboarding](cloud-connector-gcp-enable-vm-onboarding.md), Systems Manager tools such as Automation and State Manager can target and manage your GCP Compute Engine VMs as Systems Manager managed nodes.

This section includes the following topics.
+ [Create a Cloud Connector (AWS Management Console)](cloud-connector-gcp-create-console.md)
+ [Prerequisites](cloud-connector-gcp-prerequisites.md)
+ [Step 1: Create an AWS Config connector (optional)](cloud-connector-gcp-create-config-connector.md)
+ [Step 2: Create a Systems Manager Cloud Connector](cloud-connector-gcp-create-ssm-connector.md)
+ [Manage Cloud Connectors](cloud-connector-gcp-manage.md)
+ [Enable VM onboarding](cloud-connector-gcp-enable-vm-onboarding.md)
+ [IAM roles created by the Systems Manager console](cloud-connector-gcp-console-iam-roles.md)
+ [Tags applied to managed instances](cloud-connector-gcp-managed-instance-tags.md)
+ [How Systems Manager handles cloud resources](cloud-connector-gcp-identifiers.md)

GCP VMs onboarded through a Cloud Connector behave as standard hybrid-activated Systems Manager managed instances. You can use the same tools and workflows – such as Run Command, Patch Manager, and State Manager – to manage them alongside your on-premises and EC2 nodes.

When you create a Cloud Connector for GCP, you choose whether AWS Config records the connector's GCP resources. Recording is on by default, and you can't change the choice after you create the connector. Creating a Cloud Connector involves the following steps:

1. (Optional) Create an AWS Config connector, which uses workload identity federation to let AWS Config record GCP resource state. You need it only if you record with AWS Config.

1. Create a Systems Manager Cloud Connector, which registers the GCP host project and the target projects, or the entire GCP organization, with Systems Manager.

You can create a Cloud Connector in one of two ways. We recommend that you use the AWS Management Console, which generates a setup script that you run in Google Cloud Shell to configure the GCP side. You can also use the AWS CLI. Complete the [prerequisites](cloud-connector-gcp-prerequisites.md), and then follow [Step 1](cloud-connector-gcp-create-config-connector.md) and [Step 2](cloud-connector-gcp-create-ssm-connector.md).

**Note**  
Systems Manager supports up to 10 Cloud Connectors per AWS account. Each Cloud Connector supports up to 75 GCP project targets, whether you list the projects or target an entire GCP organization. Across all of its Cloud Connectors, an AWS account supports up to 100 GCP project targets. For example, if one Cloud Connector targets 75 projects, the other Cloud Connectors in the account can target up to 25 more projects in total.
If you target an entire GCP organization, you must provide the organization ID. If you target specific projects and record with AWS Config, provide the organization ID when your host project belongs to a GCP organization, because the AWS Config connector requires it.
GCP VMs that you onboard through a Cloud Connector are hybrid managed nodes. Session Manager, Run Command, and Patch Manager use pay-as-you-go pricing on hybrid managed nodes. For more information, see [Managing nodes in hybrid and multicloud environments with Systems Manager](systems-manager-hybrid-multicloud.md) and [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/).
If you record with AWS Config, you're charged service usage fees when AWS Config starts recording the connector's GCP resources. For pricing information, see [AWS Config pricing](https://aws.amazon.com/config/pricing/).

For more information about the IAM roles that Systems Manager creates on your behalf during the connector setup wizard, including their trust policies and permissions policies, see [IAM roles created by the Systems Manager console](cloud-connector-gcp-console-iam-roles.md).