

# External storage options for diskless hosts

This page applies to Self-deployed environments that run VCF 9.x on diskless hosts. For how EVS-deployed environments (VCF 5.2.x) differ, see [Differences between deployment modes](deployment-mode-differences.md).

Diskless Amazon Elastic VMware Service hosts boot from an Amazon EBS volume and have no NVMe instance store volumes to use as vSAN capacity. Every datastore that holds your virtual machines must be on external storage that all hosts in the cluster can reach over the network. This includes the datastore for the VMware Cloud Foundation (VCF) management appliances.

Each diskless host has one EBS boot volume. ESX shows this volume as a local NVMe disk that holds only the ESX system partitions. The host has no VMFS data datastore on local disks, and vSAN isn’t available. For the diskless instance types and the VCF versions that they support, see [Supported VCF versions by instance type](versions-provided.md#current-vcf-versions).

## Requirements for diskless hosts
<a name="external-storage-diskless-instance-types"></a>

Diskless instance types have the following requirements.
+ You can use them only with VCF 9.x. They aren’t available in EVS-deployed mode, where Amazon EVS deploys VCF 5.2.x for you.
+ You must provide and manage the external storage. Amazon EVS doesn’t create, configure, or monitor it.
+ You can’t use vSAN on local disks.
+ The external storage must be in the same VPC and Availability Zone as your hosts.

For the procedure to deploy an environment with diskless hosts, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

## Storage options
<a name="external-storage-diskless-options"></a>

The following storage services are options for diskless hosts.


| Characteristic | Amazon FSx for NetApp ONTAP | Amazon FSx for OpenZFS | Everpure Cloud Dedicated | 
| --- | --- | --- | --- | 
| Service type | Fully managed AWS file system service. | Fully managed AWS file system service. | Software-defined block storage array that you deploy from AWS Marketplace into your AWS account, and that you manage. | 
| Protocols for Amazon EVS | NFS v3, NFS v4.1, iSCSI, and NVMe/TCP. | NFS. The deployment in this guide uses NFS v3. | iSCSI, with VMFS datastores. | 
| Principal storage for the management domain | NFS v3 through the VCF Installer, according to Broadcom and NetApp documentation for ONTAP. Other protocols need the Broadcom Converge workflow, which you run outside Amazon EVS. For more information, see [Principal and supplemental storage](#external-storage-diskless-principal). | NFS v3 through the VCF Installer. For the procedure, see [Configure FSx for OpenZFS as principal storage for diskless hosts](config-fsx-openzfs-datastore.md). | Broadcom Converge workflow. | 
| Supplemental storage | Yes. See [Connect external storage](external-storage-connect.md). | Not covered in this guide. | VMFS datastores on iSCSI that you add after VCF is deployed. | 
| Amazon EVS procedures |  [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md)  |  [Configure FSx for OpenZFS as principal storage for diskless hosts](config-fsx-openzfs-datastore.md)  | Everpure documentation. See [Everpure Cloud Dedicated](#external-storage-diskless-everpure). | 

The deployment procedure in this guide uses FSx for OpenZFS with NFS v3. For FSx for NetApp ONTAP as principal storage and for Everpure Cloud Dedicated, follow the Broadcom, NetApp, and Everpure documentation that applies to your option.

## Principal and supplemental storage
<a name="external-storage-diskless-principal"></a>

For the definitions of principal and supplemental storage, see [Choose storage](plan-storage.md). For the management domain, the VCF Installer places the management appliances on the principal datastore.

The VCF Installer deploys the management domain directly onto an NFS v3 datastore. To use another protocol as principal storage, such as iSCSI, NFS v4.1, or NVMe over TCP, you first build the datastore and a vCenter instance yourself. Then you convert the environment to VCF. For more information, see [article 416270](https://knowledge.broadcom.com/external/article/416270) in the Broadcom knowledge base.

## Requirements for all storage options
<a name="external-storage-diskless-requirements"></a>

Whichever option you choose, plan for the following.

Network placement  
Create the storage in the same VPC and Availability Zone as your Amazon EVS environment. Amazon EVS is a single Availability Zone service. Place the storage endpoints in the Amazon EVS service access subnet or in another subnet of the same VPC. Don’t place storage in an Amazon EVS VLAN subnet, because Amazon EVS manages those subnets. For more information about the service access subnet, see [Concepts and components of Amazon EVS](concepts.md).

Network path  
ESX hosts reach the storage through the VPC. Traffic from the Amazon EVS VLAN subnets uses the VPC local route. If you associate the VLAN subnets with a custom route table, make sure that the route table keeps the local route to the subnet that contains the storage. If you use a network ACL for the VLAN subnets, allow the storage protocol ports in both directions. For more information, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).

Access rules  
Allow the ESX host IP addresses to reach the storage. For NFS, add the host management VLAN subnet CIDR to the export or access list. In the security group of the storage, allow the protocol ports from the host management VLAN subnet CIDR. EC2 security group rules aren’t enforced on the Amazon EVS VLAN subnet network interfaces, but they’re enforced on the storage network interfaces.

DNS and IP addressing  
Use the IP address of the storage endpoint when you configure the datastore in the VCF Installer specification. Whether ESX hosts can resolve the DNS name of the storage depends on your DNS configuration.

MTU  
The host management network in Amazon EVS uses an MTU of 1500, and the NFS datastores in this guide mount through that network. For more information, see [MTU by network function](vlan-subnet-reference.md#vlan-subnet-mtu).

Capacity  
The VCF Installer checks the capacity of the principal datastore before it deploys. Size the datastore for the management domain that you plan to deploy, and leave room for growth. The datastore size that the ESX host reports depends on the storage. For example, a datastore on an Amazon FSx for OpenZFS volume without a quota shows the capacity of the file system. For a sizing example, see [Configure FSx for OpenZFS as principal storage for diskless hosts](config-fsx-openzfs-datastore.md).

Availability  
The management appliances run on the external datastore. If the storage is unavailable, the management plane and your workloads are unavailable. Choose a storage deployment type that matches your availability requirements, and test how your environment behaves during a storage failover. For more information, see [Plan for resilience and recovery](plan-resilience.md).

## Amazon FSx for NetApp ONTAP
<a name="external-storage-diskless-fsx-ontap"></a>

Amazon FSx for NetApp ONTAP provides NFS and block storage that you can use as external datastores with Amazon EVS. The FSx for ONTAP datastore topics in [Connect external storage](external-storage-connect.md) assume that your environment is already deployed and that you use the vSphere Client. For diskless hosts, the principal datastore must exist before VCF is deployed. Use the VMware Host Client and the VCF Installer instead, as described in [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

For NFS v3 principal storage, the VCF Installer needs the following.
+ The datastore is mounted on the first host before you validate the specification.
+ The export allows the ESX host management addresses.
+ The specification declares an NFS network.

For more information, see [Step 4b (diskless): Create the specification and deploy](deploy-diskless-spec.md).

For NetApp guidance on ONTAP as principal NFS storage for the VCF management domain, see [VCF management domain with NFS principal storage](https://docs.netapp.com/us-en/netapp-solutions-virtualization/vmware/vmw-vcf-mgmt-principal-nfs.html) in the NetApp documentation. For NetApp guidance on FSx for ONTAP with Amazon EVS, see [Amazon FSx for NetApp ONTAP with Amazon EVS](https://docs.netapp.com/us-en/netapp-solutions-cloud/vmware/evs-mount-fsxn-intro.html) in the NetApp documentation.

For file system limits and availability options, see [Quotas and limits](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limits.html) and [Availability and durability](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html) in the *Amazon FSx for NetApp ONTAP User Guide*.

## Amazon FSx for OpenZFS
<a name="external-storage-diskless-fsx-openzfs"></a>

Amazon FSx for OpenZFS provides NFS file storage that is built on the OpenZFS file system. The VCF Installer deploys the management domain onto an NFS v3 datastore on an FSx for OpenZFS volume. For the procedure, see [Configure FSx for OpenZFS as principal storage for diskless hosts](config-fsx-openzfs-datastore.md).

For more information, see the [Amazon FSx for OpenZFS User Guide](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/what-is-fsx.html).

## Everpure Cloud Dedicated
<a name="external-storage-diskless-everpure"></a>

Everpure Cloud Dedicated is a block storage array from Everpure (formerly Pure Storage) that runs on Amazon EC2 instances in your AWS account. You subscribe to it and deploy it from AWS Marketplace, and you operate it. According to Everpure, Everpure Cloud Dedicated connects to Amazon EVS over iSCSI and presents VMFS datastores.

**Note**  
Everpure Cloud Dedicated was previously named Pure Cloud Block Store and Pure Storage Cloud Dedicated. Everpure and AWS Marketplace documentation might use any of these names.

The VCF Installer doesn’t accept an iSCSI VMFS datastore as principal storage. Use Everpure Cloud Dedicated in one of the following ways.
+ As supplemental storage that you add after VCF is deployed on a different principal datastore, such as an FSx for OpenZFS or FSx for ONTAP NFS datastore.
+ As principal storage through the Broadcom Converge workflow, which you run outside of Amazon EVS. Everpure doesn’t document this configuration for Amazon EVS. For more information, see [article 416270](https://knowledge.broadcom.com/external/article/416270) in the Broadcom knowledge base.

For the following tasks, use the Everpure documentation.
+ Subscribe to the product and deploy the array into your VPC.
+ Plan the subnets, security groups, IAM role, and quotas that the array needs.
+ Configure the iSCSI network, multipathing, and the Everpure vSphere plug-in.
+ Create volumes and VMFS datastores.

Place the array in the same Availability Zone as your hosts, and use separate VPC subnets for the array interfaces. Don’t use an Amazon EVS VLAN subnet for the array.

For more information, see the following resources.
+  [Everpure Cloud Dedicated: Support for Amazon Elastic VMware Service](https://www.everpuredata.com/content/dam/pdf/en/solution-briefs/sb-pure-storage-cloud-dedicated-support-for-amazon-evs.pdf) solution brief
+  [Everpure Cloud Dedicated (subscription)](https://aws.amazon.com/marketplace/pp/prodview-j2mtejfozqlto) in AWS Marketplace 
+  [Everpure Community posts about Amazon EVS](https://purecommunity.purestorage.com/tag/evs) 

## Broadcom references for external principal storage
<a name="external-storage-diskless-broadcom"></a>

The following Broadcom articles describe the requirements that the VCF Installer enforces for NFS principal storage.
+  [Article 414088](https://knowledge.broadcom.com/external/article/414088) in the Broadcom knowledge base describes the requirement that the NFS datastore is mounted on the first ESX host before validation.
+  [Article 446573](https://knowledge.broadcom.com/external/article/446573) in the Broadcom knowledge base describes the causes of NFS pre-check failures, including port group names, MTU, and export lists.
+  [Article 416270](https://knowledge.broadcom.com/external/article/416270) in the Broadcom knowledge base describes which storage types can be principal storage and how to use the Converge workflow.