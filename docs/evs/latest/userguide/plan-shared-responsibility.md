

# Shared responsibility and support

Amazon Elastic VMware Service is a self-managed service. AWS manages the infrastructure that Amazon EVS provisions, and you manage the VMware Cloud Foundation (VCF) software that runs on it.

## Who manages what
<a name="plan-shared-responsibility-table"></a>

The following table shows who manages each area in each deployment mode. In the mode columns, AWS or You shows the owner.


| Area | VCF 9.x (Self-deployed) | VCF 5.2.x (EVS-deployed) | Notes | 
| --- | --- | --- | --- | 
| Amazon EVS control plane and the AWS resources that Amazon EVS provisions |  AWS  |  AWS  | Includes the VLAN subnets that Amazon EVS creates, the bare metal hosts and their firmware upgrades. You maintain the VPC networking resources that you create, such as route tables, network ACLs, route servers, and gateways. | 
| Initial VCF installation | You |  AWS  | In Self-deployed mode, you install VCF on the hosts that Amazon EVS creates. In EVS-deployed mode, Amazon EVS installs VCF when it creates the environment. | 
| VCF upgrades and patches (vCenter, NSX, SDDC Manager or VCF Operations, ESX) | You | You | For more information, see [Update and upgrade](evs-lifecycle-mgmt.md). | 
| VCF authentication, role-based access control, and password rotation for the management appliances | You | You | Harden the VCF management network according to Broadcom guidance and the security requirements of your organization. | 
| Host health monitoring and host replacement | You | You | For more information, see [Host maintenance and retirement events](evs-host-maintenance.md) and [Plan for resilience and recovery](plan-resilience.md). | 
| VCF subscriptions | You | You | For more information, see [VCF licensing](vcf-license-mgmt.md). | 
| Secrets for connectors in AWS Secrets Manager | You rotate them | You rotate them | Amazon EVS encrypts the credentials that you store in Secrets Manager with AWS KMS and restricts service access to them with resource tags. For more information, see [Manage secrets](evs-env-secret-rotation.md). | 
| Connector health and aggregate environment health |  AWS  |  AWS  | Amazon EVS monitors the connectors that you create and reports the health of the environment. For more information, see [Monitor environment status](evs-env-status-check.md). | 
| Security monitoring of the VCF deployment | You | You | For more information, see [Security in Amazon Elastic VMware Service](security.md). | 
| VM-level high availability, replication, and backup | You | You | For more information, see [Plan for resilience and recovery](plan-resilience.md). | 

Security follows the AWS shared responsibility model, which divides security of the cloud from security in the cloud. For more information, see [Security in Amazon Elastic VMware Service](security.md).

You can also work with AWS Partners to manage your environment.

## Get help from AWS Support and Broadcom
<a name="plan-shared-responsibility-support"></a>

Amazon EVS requires an AWS Business Support, AWS Enterprise On-Ramp, or AWS Enterprise Support plan. AWS Business Support is the minimum tier that meets the requirement. If you run business-critical workloads, we recommend AWS Enterprise On-Ramp or AWS Enterprise Support. The support plan gives you continuous access to technical support and architectural guidance. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans).

**Important**  
Environment creation fails if your account isn’t enrolled in an AWS Business Support, AWS Enterprise On-Ramp, or AWS Enterprise Support plan.

 AWS provides support for Amazon EVS and its associated infrastructure services, including VCF. For VCF configuration guidance, or for issues with other VMware products such as VCF Operations, HCX or NSX, you can also contact Broadcom with your Broadcom support entitlement. For more information, see the [Broadcom Support Portal](https://support.broadcom.com/).

For troubleshooting steps and how to open a case, see [Get help from AWS Support and Broadcom](get-help.md).