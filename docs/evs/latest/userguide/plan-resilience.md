

# Plan for resilience and recovery

An Amazon Elastic VMware Service environment runs in one AWS Availability Zone, so your design must handle host failures inside that zone and plan recovery outside it. You configure most of the VMware availability features yourself, and you’re responsible for the high availability of your virtual machines.

## Design for a single Availability Zone
<a name="plan-resilience-single-az"></a>

An Amazon EVS environment runs in one Availability Zone. All VPC subnets of an Amazon EVS environment must be in the same Availability Zone, and so must its hosts and any external storage. Choose the Availability Zone before you create the environment. For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc).

The following items keep the environment available inside the Availability Zone.


| Item | What it does | 
| --- | --- | 
| Number of hosts | VMware Cloud Foundation (VCF) requires a minimum number of hosts to keep vSAN quorum and to stay available during maintenance and host failures. For more information, see [Size your environment](plan-sizing.md). | 
| NSX Edge cluster | An Active/Standby NSX Edge cluster with its two nodes on different hosts allows a quick failover if one NSX Edge node fails. In EVS-deployed mode, Amazon EVS deploys this cluster. In Self-deployed mode, you deploy it. For more information, see [Step 5: Configure NSX networking](self-deployed-nsx-edge.md). | 
| EC2 placement groups | Amazon EVS supports partition and cluster placement groups for hosts. A partition placement group places groups of hosts on separate hardware, which reduces the chance of correlated hardware failures. A cluster placement group places hosts in the same rack for low latency. For more information, see [Placement strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html) in the *Amazon EC2 User Guide*. | 
| Spare host and Capacity Reservations | A spare host and reserved EC2 capacity let you replace a failed host without waiting for capacity. For more information, see [Reserve capacity for hosts](plan-capacity.md). | 

You choose the placement group when you add a host, so plan it before you add the first host.

## VMware features that you configure
<a name="plan-resilience-vcf"></a>

You’re responsible for configuring the VMware components that run on Amazon EVS for the availability of your virtual machines. The following VCF features are available to you.

 **vSphere HA**   
Restarts virtual machines on other hosts when a host fails. For more information, see [High Availability Design for vCenter Server for VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-design-5-2/vsphere-design-for-vmware-cloud-foundation/vcf-vcenter-server-design.html#GUID-B4380728-190C-428E-83AE-3F7667506948-en) in the Broadcom documentation.

 **vSAN failures to tolerate (FTT)**   
Sets how many host failures a virtual machine can withstand before it becomes inaccessible. For more information, see [Tolerate Additional Failures with Fault Domain in vSAN Cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/tolerate-additional-failures-with-fault-domains-in-vsan-cluster.html) in the Broadcom documentation.

 **vSAN data protection**   
Recovers virtual machines from operational failures or ransomware attacks with native snapshots on the vSAN cluster. For more information, see [Using vSAN Data Protection](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/expanding-and-managing-a-vsan-cluster/using-vsan-data-protection.html) in the Broadcom documentation.

 **vSphere Replication**   
Replicates virtual machines asynchronously for disaster recovery and migration. For more information, see [How vSphere Replication Works](https://techdocs.broadcom.com/us/en/vmware-cis/live-recovery/vsphere-replication/9-0-3/using-vsphere-replication/about-vmware-vsphere-replication/how-vsphere-replication-works.html) in the Broadcom documentation.

The vSAN features apply to hosts with local NVMe. Diskless hosts are available only with VCF 9.x. On diskless hosts, the availability of your datastores depends on the external storage that you choose. For more information, see [External storage options for diskless hosts](external-storage-diskless.md).

Before you design for a VCF feature, check whether Amazon EVS supports it. For example, see the [vSphere Fault Tolerance](vcf-feature-support.md#feat-vsphere-fault-tolerance) row in [VCF feature support on Amazon EVS](vcf-feature-support.md).

## Plan disaster recovery
<a name="plan-resilience-dr"></a>

Because an environment runs in one Availability Zone, plan how you recover if the Availability Zone or the environment is unavailable. You can use vSphere Replication for disaster recovery of your virtual machines.

Multi-AZ external storage doesn’t keep an Amazon EVS environment running through an Availability Zone failure, because the environment itself runs in one Availability Zone. For example, with a Multi-AZ Amazon FSx for NetApp ONTAP file system, you build a new environment in the other Availability Zone. Then you mount the volumes there and register the virtual machines again.

## Plan backup
<a name="plan-resilience-backup"></a>

You can use third-party backup tools that you already know with Amazon EVS, such as Veeam. Check that the backup product supports the VCF version that you deploy.

## Plan for host failures
<a name="plan-resilience-hosts"></a>

You’re responsible for monitoring host health and replacing failed hosts. AWS schedules maintenance and retirement events for EC2 instances, and it notifies you in advance. Replace an affected host before the event, because a reboot of a bare metal instance doesn’t preserve instance store data.

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API.

For more information, see [Host maintenance and retirement events](evs-host-maintenance.md) and [Replace a failed host (Self-deployed)](host-replace.md).