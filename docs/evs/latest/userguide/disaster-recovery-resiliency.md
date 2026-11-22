

# Resilience for Amazon EVS

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected through low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure).

To choose a recovery approach for your workloads, see [Plan for resilience and recovery](plan-resilience.md).

## Amazon EVS infrastructure resilience
<a name="disaster-recovery-resiliency-infra"></a>

An Amazon Elastic VMware Service environment runs in a single AWS Availability Zone. Amazon EVS supports Single-AZ deployments only. To help keep your Single-AZ infrastructure available, Amazon EVS offers the following features:
+ Amazon EVS supports partition placement groups and cluster placement groups for Amazon EVS hosts. For more information, see [Placement strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html) in the * Amazon EC2 User Guide*.
+ In EVS-deployed environments that run VMware Cloud Foundation (VCF) 5.2.x, Amazon EVS deploys an Active/Standby NSX Edge cluster with two NSX Edge nodes, as VCF requires. The NSX Edge nodes run on different hosts, which allows quick failover in the rare event that an NSX Edge node fails. In Self-deployed environments that run VCF 9.x, you deploy and configure the NSX Edge cluster yourself. For design guidance, see [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md).

A partition placement group spreads your Amazon EC2 instances across logical partitions. Instances in one partition don’t share underlying hardware with instances in other partitions. This strategy helps reduce the likelihood of correlated hardware failures for large distributed workloads. A cluster placement group places your Amazon EC2 instances within the same physical rack for low latency.

## Host count and availability
<a name="disaster-recovery-resiliency-hosts"></a>

In EVS-deployed environments (VCF 5.2.x), Amazon EVS deploys a minimal environment of four ESX hosts, which VCF requires. You can add hosts after deployment. This VMware design requirement ensures proper vSAN quorum and maintains availability during maintenance operations and host failures. For more information, see [vSphere Cluster Design for VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-design-5-2/vsphere-design-for-vmware-cloud-foundation/vcf-vsphere-cluster-design.html) in the Broadcom documentation.

In Self-deployed environments that run VCF 9.x, you add enough hosts for your VCF topology. For the minimum host counts of each topology, see the Broadcom documentation for your VCF version. For host limits and sizing guidance in both modes, see [Size your environment](plan-sizing.md).

## VMware component resilience
<a name="disaster-recovery-resiliency-app"></a>

You are responsible for configuring the VMware components that run on Amazon EVS for the high availability of your virtual machines (VMs) and for workload resiliency. You can configure the following VCF resiliency features:
+ vSphere Replication provides host-based, asynchronous replication of your VMs for disaster recovery and workload migration. For more information, see [How vSphere Replication Works](https://techdocs.broadcom.com/us/en/vmware-cis/live-recovery/vsphere-replication/9-0-3/using-vsphere-replication/about-vmware-vsphere-replication/how-vsphere-replication-works.html) in the Broadcom documentation.
+ vSphere HA provides automatic failover for VMs when a host fails. For more information, see [High Availability Design for vCenter Server for VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-design-5-2/vsphere-design-for-vmware-cloud-foundation/vcf-vcenter-server-design.html#GUID-B4380728-190C-428E-83AE-3F7667506948-en) in the Broadcom documentation.
+ With vSAN data protection, you can quickly recover VMs from operational failures or ransomware attacks by using native snapshots stored locally on the vSAN cluster. For more information, see [Using vSAN Data Protection](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/expanding-and-managing-a-vsan-cluster/using-vsan-data-protection.html) in the Broadcom documentation.
+ vSAN Failures to Tolerate (FTT) is a vSAN setting that determines how many host failures a VM can withstand before it becomes inaccessible. This setting defines the level of redundancy for your VMs within the vSAN cluster. For more information, see [Tolerate Additional Failures with Fault Domain in vSAN Cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/tolerate-additional-failures-with-fault-domains-in-vsan-cluster.html) in the Broadcom documentation.

The vSAN features apply only to clusters that use vSAN storage. Diskless hosts, which need VCF 9.x, have no instance store volumes and use external principal storage. The resilience of their VM data depends on the storage service. For more information, see [External storage options for diskless hosts](external-storage-diskless.md).

**Note**  
Amazon EVS doesn’t support vSphere Fault Tolerance (FT). Workload VMs on Amazon EVS run on NSX overlay networks, and Broadcom doesn’t support FT on VMs that use NSX port groups or on NSX Manager and NSX Edge nodes. For more information, see [article 317806](https://knowledge.broadcom.com/external/article?articleNumber=317806) in the Broadcom Knowledge Base.

For the support status of VCF features on Amazon EVS, including the [vSphere Fault Tolerance](vcf-feature-support.md#feat-vsphere-fault-tolerance) row, see [VCF feature support on Amazon EVS](vcf-feature-support.md).