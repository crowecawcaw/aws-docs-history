

# Operate

After you deploy an Amazon Elastic VMware Service environment, you operate it. Amazon EVS is a self-managed service, so you’re responsible for the VMware Cloud Foundation (VCF) software on your hosts, for monitoring host health, and for replacing hosts that fail. For who manages what in each deployment mode, see [Shared responsibility and support](plan-shared-responsibility.md).

The procedures in [Deploy in Self-deployed mode](getting-started-self-deployed.md) deploy VCF 9.x. Pages in [Deploy in EVS-deployed mode](evs-deployed-overview.md) cover VCF 5.2.x. A page with no line and outside those sections covers both.

## Day 2 tasks by area
<a name="operate-overview-tasks"></a>

The following table lists the tasks in this chapter in the order that you usually need them.


| Area | Tasks | 
| --- | --- | 
|  [Monitor your environment](monitor-overview.md)  | Check environment status, get notified about host events, monitor hosts and VCF, and log Amazon EVS API calls with AWS CloudTrail. | 
|  [Manage hosts](host-management.md)  | Prepare for EC2 maintenance events, and add, replace, or delete hosts. | 
|  [Update and upgrade](evs-lifecycle-mgmt.md)  | Update ESX and VCF, use the Amazon EVS custom add-on depot, and upgrade VCF. | 
|  [Manage connectors and credentials](connectors-overview.md)  | Create, update, and delete connectors, rotate vCenter connector credentials, and manage the secrets that Amazon EVS creates. | 
|  [Windows Server entitlements](entitlements.md)  | Create, activate, and delete Windows Server entitlements for your VMs. | 
|  [Migrate workloads with HCX](migrate-evs-hcx.md)  | Prepare for VMware HCX migration, configure HCX internet connectivity, and verify migrations. | 
|  [Use VCF features on Amazon EVS](operate-vcf-features.md)  | Set up VCF features where Amazon EVS adds steps of its own, such as NSX Federation. | 

**Topics**