

# Deploy

You can deploy an Amazon Elastic VMware Service environment in three ways.

The procedures in [Deploy in Self-deployed mode](getting-started-self-deployed.md) deploy VCF 9.x. Pages in [Deploy in EVS-deployed mode](evs-deployed-overview.md) cover VCF 5.2.x. A page with no line and outside those sections covers both.

## Choose how to deploy
<a name="deploy-choose-path"></a>

Each path creates an Amazon EVS environment with hosts in your own Amazon VPC. The paths differ in the VMware Cloud Foundation (VCF) version and in who installs VCF.


| Path | VCF version | Who installs VCF | Use it when | Start here | 
| --- | --- | --- | --- | --- | 
| EVS Deployment Orchestrator (EDO), a tool in the [Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs)  | 9.x | EDO installs VCF. You launch one AWS CloudFormation stack, and it builds the network, adds the hosts, and installs VCF in Self-deployed mode. | You want a complete VCF environment without running each step yourself, and EDO supports your VCF version and instance type. |  [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md)  | 
| Manual, Self-deployed mode | 9.x | You install VCF. You use the VCF Installer on hosts that Amazon EVS provisions. | You want to control each step, or you plan to use settings that EDO doesn’t support, such as Amazon FSx for OpenZFS as the principal storage. |  [Deploy in Self-deployed mode](getting-started-self-deployed.md)  | 
| EVS-deployed mode | 5.2.x | Amazon EVS installs VCF when you create the environment. | You deploy VCF 5.2.x. |  [Deploy in EVS-deployed mode](evs-deployed-overview.md)  | 

For how the two modes differ after deployment, see [Differences between deployment modes](deployment-mode-differences.md). For the VCF versions and instance types that each mode supports, see [Supported VCF versions and instance types](versions-provided.md).

## Before you begin
<a name="deploy-prerequisites"></a>

Every path needs the following.
+ An AWS account that is ready for Amazon EVS, with a support plan, the AWS CLI, and an IAM role for administrators. For instructions, see [Prepare your AWS account](setting-up.md).
+ A plan for your IP address space, DNS records, host count, and VCF subscriptions. For a list of the decisions to make first, see [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md).

We recommend that you complete the checklist before you create any resources, so that you have every value that the deployment steps ask for.

If you plan to use VMware HCX over the internet, also set up the IPAM pool and the public CIDR block before you create the environment. For the task list, see [Build the network foundation](network-foundation.md).

## Order of the sections
<a name="deploy-section-order"></a>

For the manual paths, follow the sections in this order.

1.  [Prepare your AWS account](setting-up.md).

1.  [Build the network foundation](network-foundation.md). Both modes use the same VPC, DHCP option set, Amazon VPC Route Server, network ACL, and route table setup.

1. Deploy the environment in one mode. Follow [Deploy in Self-deployed mode](getting-started-self-deployed.md) to install VCF yourself (the procedures deploy VCF 9.x), or [Deploy in EVS-deployed mode](evs-deployed-overview.md) to have Amazon EVS install VCF 5.2.x.

1. (Optional) [Connect external storage](external-storage-connect.md) after the environment is running.

If you use EDO, you still prepare your AWS account first. EDO then creates the network resources and runs the Self-deployed steps for you. You can also deploy EDO into an existing VPC. For more information, see [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md).

To create Amazon EVS resources from templates instead of the console or AWS CLI, see [Automate your deployment](deploy-automate.md).

## Deployment tools
<a name="deploy-tools"></a>

The following table lists the released open-source tools that help you deploy Amazon EVS environments.


| Tool | VCF version | What it does | Link | 
| --- | --- | --- | --- | 
| EVS Deployment Orchestrator (EDO) | 9.0.2 and 9.1.0 | Deploys a complete VCF environment on Amazon EVS from one AWS CloudFormation stack. |  [Deploy folder of the Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs/tree/main/Deploy)  | 

**Topics**