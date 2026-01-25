# Amazon EVS environment lifecycle management

This page describes your lifecycle management responsibilities within an Amazon EVS environment.

A key benefit of Amazon EVS is that you have complete control over your VMware architecture in the cloud.
You can optimize the VMware Cloud Foundation (VCF) software stack to meet the unique demands of your applications.
Because Amazon EVS is a self-managed service, you are responsible for the lifecycle management and maintenance of the VMware software used in the Amazon EVS environment, such as ESX, vSphere, vSAN, NSX, and SDDC Manager.
You are also responsible for maintaining any third-party integrations, such as data protection solutions that you integrate into your Amazon EVS hosts.

You are responsible for the configuration of the underlying AWS networking components that Amazon EVS uses, including VPC route tables, security group and network access control list (ACL) rules, VPC Route Server configuration, internet gateways, NAT gateways, and transit gateways (for on-premises connectivity).

AWS is responsible for deploying the Amazon EVS environment with networking configurations that you provide.
Environment deployment includes the following:

- Bootstrapping the network configuration of your Amazon EVS environment.
- Enabling north-south routing with the VPC Route Server instance you provide.
- Deploying the required EVS VLAN subnets, elastic network interfaces, and four initial ESX hosts.
- Configuring an NSX overlay network with a Tier-0 gateway and a Tier-1 gateway.
- Deploying an NSX Edge cluster with two NSX Edge nodes in Active/Standby mode.
- Creating and configuring the initial vSAN cluster and mounting the datastore.
  You are responsible for VMware NSX configuration, including network segments, distributed firewall rules, and load balancers.
  You are also responsible for the configuration of any integrated solutions that you implement with Amazon EVS after the EVS environment deploys, including VMware HCX configuration and additional NSX Tier-1 gateways.

For more information about AWS and customer responsibilities, see the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

###### Note

A Tier-0 gateway and a Tier-1 gateway is created and configured as part of Amazon EVS environment deployment.
Amazon EVS only supports a single Tier-0 gateway at this time.
Any modification to these logical routers or the NSX edge node VMs could affect connectivity and should be avoided.

## VMware software updates

###### Warning

If you have updated your ESX version after the Amazon EVS environment deployment, SDDC manager may fail
during VCF host validation in the commission hosts step.
For steps to troubleshoot this issue, see [SDDC Manager fails VCF host validation during host commissioning](troubleshooting.md#troubleshoot-sddc-failure-host-commission "troubleshooting.md#troubleshoot-sddc-failure-host-commission").

For information about VCF versions provided by Amazon EVS, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md "versions-provided.md").
Per the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), you are responsible for applying any patches, updates, or upgrades to VCF software, including ESX, vCenter Server, vSAN, NSX, SDDC Manager, and other integrated solutions, in your EVS environment.
Post-deployment, we recommend that you review the VCF software version deployed by Amazon EVS and update as needed.
You can obtain VCF updates through the [Broadcom support portal](https://support.broadcom.com/web/ecx "https://support.broadcom.com/web/ecx").
We also recommend that you establish and adhere to a regular maintenance schedule for updates and patches.

###### Note

Amazon EVS does not support VMware Cloud Foundation 9 at this time.

###### Note

Amazon EVS does not provide all versions of VCF and ESX released by Broadcom. For software interoperability information, refer to the [Broadcom Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability?col=1 "https://interopmatrix.broadcom.com/Interoperability?col=1"). For full hardware compatibility with AWS EC2 instances, refer to the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/ "https://compatibilityguide.broadcom.com/").

Certain patches, updates, or upgrade may have impact on workloads running in your environment.
Before patching, updating, or upgrading your VCF software, we recommend that you review the [VCF Lifecycle Management Guide](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vmware-cloud-foundation-lifecycle-management.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vmware-cloud-foundation-lifecycle-management.html") to understand how these changes will impact your environment.
We also recommend that you test changes in a staging environment before deploying to production.
You can review the [VCF 5.2.x release notes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes.html") to understand the latest VCF 5.2.x updates.

## ESX host lifecyle and maintenance

You are responsible for ESX host lifecycle management and maintenance within the Amazon EVS environment, including monitoring host health and remediating host issues.
For more information, see [Performing maintenance on your environment](evs-env-maintenance.md "evs-env-maintenance.md").

AWS performs scheduled maintenance on the underlying i4i.metal EC2 instances to ensure reliability, availability, and performance of the infrastructure.
For more information, see [About AWS scheduled maintenance for EC2 instances](evs-host-maintenance.md#evs-host-maintenance-about "evs-host-maintenance.md#evs-host-maintenance-about").
