

# Deploy with the EVS Deployment Orchestrator

This page applies to Self-deployed environments that run VCF 9.x. For how EVS-deployed environments (VCF 5.2.x) differ, see [Differences between deployment modes](deployment-mode-differences.md).

The EVS Deployment Orchestrator (EDO) is an open-source tool in the [Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs), where Amazon Elastic VMware Service provides tooling and solutions that you can use. EDO deploys a complete VMware Cloud Foundation (VCF) environment on Amazon EVS in Self-deployed mode. You launch one AWS CloudFormation stack, and EDO runs the deployment without further input. EDO is in the `Deploy` folder of the [Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs/tree/main/Deploy) on GitHub.

For the parameters, the blueprint fields, the commands, and the troubleshooting steps, see the [EDO README](https://github.com/aws/solutions-for-amazon-evs/tree/main/Deploy/EVS-Deployment-Orchestrator).

**Note**  
Before you use EDO, complete [Prepare your AWS account](setting-up.md). EDO creates the VPC and the network resources, so you don’t need to complete [Build the network foundation](network-foundation.md) first.

## What EDO builds
<a name="edo-what-it-builds"></a>

The stack starts a small runner instance in your account. The runner does the deployment work and creates the following resources.
+ A VPC with the networking that Amazon EVS needs, including DNS, a NAT gateway, Amazon VPC Route Server, and a security group. You can also deploy into an existing VPC that meets the requirements in the README.
+ An Amazon EVS environment with ESX hosts on bare metal Amazon EC2 instances in your account. You choose the instance type and the host count in a blueprint file.
+ For diskless hosts, an Amazon FSx for NetApp ONTAP file system and the NFS datastore that the management cluster uses as principal storage. If you deploy into your own VPC, you provide the FSx for NetApp ONTAP volume instead.
+ VCF 9.x, installed and configured, with vCenter Server, NSX Manager, SDDC Manager, and VCF Operations.
+ An NSX Edge cluster that connects the NSX overlay network to your VPC.
+ Appliance credentials, stored in AWS Secrets Manager.

The deployment takes about 4 to 7 hours. To remove everything that EDO created, you run one teardown command from the repository. For more information, see [Clean up](#edo-clean-up).

## Supported VCF versions and instance types
<a name="edo-supported-configurations"></a>

You set the VCF version and the instance type in the blueprint. The SDDC Manager Open Virtualization Appliance (OVA) file that you upload must match the VCF version. EDO supports the following combinations.


| Instance type | VCF versions | Principal storage | 
| --- | --- | --- | 
|  `i4i.metal`  | 9.0.2, 9.1.0, 9.1.1 | vSAN on local NVMe storage | 
|  `i7i.metal-24xl`  | 9.0.2, 9.1.0, 9.1.1 | vSAN on local NVMe storage | 
|  `i7i.metal-48xl`  | 9.0.2, 9.1.0, 9.1.1 | vSAN on local NVMe storage | 
|  `r7i.metal-24xl`  | 9.0.2, 9.1.0, 9.1.1 | Amazon FSx for NetApp ONTAP over NFS | 
|  `r7i.metal-48xl`  | 9.0.2, 9.1.0, 9.1.1 | Amazon FSx for NetApp ONTAP over NFS | 

The `i4i` and `i7i` instance types have local NVMe storage, and EDO deploys vSAN on it. The `r7i` instance types are diskless, so EDO uses Amazon FSx for NetApp ONTAP as the principal storage of the management cluster. You choose the storage in the `storage` section of the blueprint. When EDO creates the VPC, it also creates the FSx for NetApp ONTAP file system. When you deploy into your own VPC, you create the file system first and set the ID of its NFS volume in the blueprint. EDO doesn’t support other external storage, such as Amazon FSx for OpenZFS. To use it, follow the manual steps in [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md). For every VCF version and instance type that Amazon EVS supports, see [Supported VCF versions and instance types](versions-provided.md). For the storage options for diskless hosts, see [External storage options for diskless hosts](external-storage-diskless.md).

**Important**  
Billing for the bare metal hosts starts when EDO provisions them, about 50 minutes after the deployment starts. The runner instance is also billed to your account until you tear down the deployment. For prices, see [Amazon EVS pricing](https://aws.amazon.com/evs/pricing).

## Before you begin
<a name="edo-prerequisites"></a>

Before you begin, make sure that the following are true.
+ You prepared your AWS account, including an AWS support plan that meets Amazon EVS requirements. For instructions, see [Prepare your AWS account](setting-up.md).
+ You have a Broadcom download token for the Broadcom online depot from the [Broadcom Support Portal](https://support.broadcom.com), under your VCF entitlement.
+ You downloaded the VCF SDDC Manager OVA for VCF 9.0.2, 9.1.0, or 9.1.1 from the Broadcom Support Portal.
+ You downloaded the Linux zip file of VMware Open Virtualization Format (OVF) Tool from the Broadcom Support Portal.
+ Your computer has the OVA and OVF Tool files and enough disk space for them. If you use the AWS CLI instead of the console, your computer also has AWS CLI version 2 and Python 3.9 or later.
+ You chose an AWS Region and Availability Zone that offer your instance type. For more information about Regions, see [AWS Regions for Amazon EVS](regions-reference.md).
+ For diskless hosts in your own VPC, you created an Amazon FSx for NetApp ONTAP file system in that VPC with an NFS volume whose export policy allows read and write access as root from the management subnet of the hosts. The README lists the export policy rules.
+ Your service quotas cover the deployment. The repository includes a read-only quota check script. For more information about Amazon EVS quotas, see [Service quotas for Amazon EVS](service-quotas-evs.md).

## Deploy with EDO
<a name="edo-procedure"></a>

Follow the [EDO README](https://github.com/aws/solutions-for-amazon-evs/tree/main/Deploy/EVS-Deployment-Orchestrator) for the exact commands in Bash or PowerShell, and for the console steps.

1. Clone the Solutions for Amazon EVS repository and open the `Deploy/EVS-Deployment-Orchestrator` folder.

1. Store your Broadcom download token as a secret in AWS Secrets Manager.

1. Copy the example blueprint and set every field that the blueprint marks as required, including the VCF version, the instance type, and the host names. For diskless hosts, also set the `storage` section.

1. (Optional) Run the quota check script against your blueprint.

1. Upload the blueprint, the SDDC Manager OVA, and the OVF Tool zip file to an Amazon S3 bucket in your account.

1. Create a CloudFormation stack from the EDO template, and pass the S3 locations, the secret name, and the Availability Zone as parameters.

1. Open the logs link on the **Outputs** tab of the stack, and watch the progress in Amazon CloudWatch Logs.

The first stack completes in about 5 minutes. EDO then creates a second stack for the deployment infrastructure. Don’t delete the second stack by hand, because the teardown command removes it.

The deployment is complete when the log shows `ALL STAGES COMPLETE`. If you set an Amazon SNS topic at launch, EDO also publishes a success or failure notification to it.

You have deployed a VCF environment on Amazon EVS. The vCenter, NSX, and SDDC Manager interfaces are reachable only from inside the VPC. To connect to them and to get the appliance credentials, follow the "After deployment" section of the README.

## Clean up
<a name="edo-clean-up"></a>

To stop the charges, remove everything that EDO created by running the teardown command that the [EDO README](https://github.com/aws/solutions-for-amazon-evs/tree/main/Deploy/EVS-Deployment-Orchestrator) describes.

**Important**  
Run the teardown before you delete either CloudFormation stack. EDO creates the hosts through the Amazon EVS API, so if you delete the stacks first, the hosts keep running and you keep paying for them. The teardown script is `destroy.py` in the EDO folder.

## Next steps
<a name="edo-next-steps"></a>
+ Check the hosts, the VCF appliances, and the connectivity. For instructions, see [Step 7: Verify the environment](self-deployed-verify.md).
+ Add more storage. For more information, see [Connect external storage](external-storage-connect.md).
+ Operate the environment. For more information, see [Operate](operate-overview.md).
+ Remove the deployment when you no longer need it. For instructions, see [Clean up](#edo-clean-up).