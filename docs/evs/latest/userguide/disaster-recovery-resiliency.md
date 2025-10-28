# Resilience in Amazon EVS

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected through low-latency, high-throughput, and highly redundant networking.
With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption.
Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

Amazon EVS environments are available in a single AWS Availability Zone.
To ensure high availability of Amazon EVS Single-AZ infrastructure, Amazon EVS offers the following features:

###### Note

Amazon EVS only supports Single-AZ deployments at this time.

- Amazon EVS supports the use of AWS Elastic Disaster Recovery to automate the backup and recovery of your data.
- Amazon EVS deploys an Active/Standby NSX Edge cluster with two NSX Edge nodes per VCF requirements.
  The NSX Edge nodes run on different hosts to ensure high availability and allow for quick failover in the rare event that an NSX Edge node fails.
- Amazon EVS deploys a minimal environment of four ESXi hosts, which VCF requires.
  Additional hosts can be added post-deployment.
  This is a VMware design requirement to ensure proper vSAN quorum and maintain availability during maintenance operations and host failures.
  For more information, see [vSphere Cluster Design for VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-design-5-2/vsphere-design-for-vmware-cloud-foundation/vcf-vsphere-cluster-design.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-design-5-2/vsphere-design-for-vmware-cloud-foundation/vcf-vsphere-cluster-design.html") in the VMware Cloud Foundation documentation.
- Amazon EVS supports the use of an EC2 partition placement group or cluster placement group for EC2 hosts.
  The partition placement group spreads your EC2 instances across logical partitions such that groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions.
  This strategy helps reduce the likelihood of correlated hardware failures for large distributed workloads.
  Cluster placement groups are used to place your EC2 instances within the same physical rack to ensure low latecy.
  For more information, see [Partition placement groups](../../../AWSEC2/latest/UserGuide/placement-strategies.md "../../../AWSEC2/latest/UserGuide/placement-strategies.md") in the _Amazon EC2 User Guide_.
  For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure "https://aws.amazon.com/about-aws/global-infrastructure").

## VMware component resilience

Amazon EVS customers are responsible for configuring the VMware components running on Amazon EVS to ensure high availability of your virtual machines (VMs) and workload resiliency.

Amazon EVS supports the following VMware Cloud Foundation (VCF) resiliency features:

- vSphere replication - Provides host-based, asynchronous replication of your VMs for disaster recovery and workload migration purposes.
  For more information, see [How vSphere Replication Works](https://techdocs.broadcom.com/us/en/vmware-cis/live-recovery/vsphere-replication/9-0-3/using-vsphere-replication/about-vmware-vsphere-replication/how-vsphere-replication-works.html "https://techdocs.broadcom.com/us/en/vmware-cis/live-recovery/vsphere-replication/9-0-3/using-vsphere-replication/about-vmware-vsphere-replication/how-vsphere-replication-works.html") in the VMware vSphere Replication documentation.
- vSAN data protection - Enables you to quickly recover VMs from operational failure for ransomware attacks, using native snapshots stored locally on the vSAN cluster.
  For more information, see [Using vSAN Data Protection](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/expanding-and-managing-a-vsan-cluster/using-vsan-data-protection.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/expanding-and-managing-a-vsan-cluster/using-vsan-data-protection.html") in the vSAN documentation.
- vSphere HA - Provides automatic failover for VMs in the event of a host failure.
  For more information, see [High Availability Design for vCenter Server for VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-design-5-2/vsphere-design-for-vmware-cloud-foundation/vcf-vcenter-server-design.html#GUID-B4380728-190C-428E-83AE-3F7667506948-en "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-design-5-2/vsphere-design-for-vmware-cloud-foundation/vcf-vcenter-server-design.html#GUID-B4380728-190C-428E-83AE-3F7667506948-en") in the VCF documentation.
- vSphere Fault Tolerance (FT) - Provides continuous availability for mission-critical VMs by creating and maintaining another VM that is identical and continuously available to replace it in the event of a failover situation.
  For more information, see [How Fault Tolerance Works](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-availability/providing-fault-tolerance-for-virtual-machines/how-fault-tolerance-works.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-availability/providing-fault-tolerance-for-virtual-machines/how-fault-tolerance-works.html") in the vSphere documentation.
- vSAN Failure to Tolerate (FTT) - A vSAN setting that determines how many host failures a VM can withstand before becoming inaccessible.
  This defines the level of redundancy and fault tolerance for your virtual machines within the vSAN cluster.
  For more information, see [Tolerate Additional Failures with Fault Domain in vSAN
  Cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/tolerate-additional-failures-with-fault-domains-in-vsan-cluster.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/expanding-and-managing-a-vsan-cluster/managing-fault-domains-in-vsan-clusters/tolerate-additional-failures-with-fault-domains-in-vsan-cluster.html") in the vSAN documentation.
