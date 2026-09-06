

# Run high-performance workloads with Amazon FSx for NetApp ONTAP
<a name="fsx-ontap"></a>

Amazon FSx for NetApp ONTAP is a storage service that allows you to launch and run fully managed ONTAP file systems in the cloud. ONTAP is NetApp’s file system technology that provides a widely adopted set of data access and data management capabilities. FSx for ONTAP provides the features, performance, and APIs of on-premises NetApp file systems with the agility, scalability, and simplicity of a fully managed AWS service. For more information, see the [FSx for ONTAP User Guide](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html).

Amazon EVS supports the use of Amazon FSx for NetApp ONTAP as an NFS/iSCSI datastore and as guest-connected storage for VMware virtual machines running on Amazon EVS.

## Supported FSx for NetApp ONTAP capabilities
<a name="fsx-ontap-supported-capabilities"></a>

The following FSx for NetApp ONTAP functionalities have been validated for use with Amazon EVS:


| Capability | Description | 
| --- | --- | 
| External NFS v3 datastores | Mount FSx for ONTAP volumes as NFS v3 datastores for VMware vSphere on Amazon EVS. | 
| External NFS v4.1 datastores | Mount FSx for ONTAP volumes as NFS v4.1 datastores for VMware vSphere on Amazon EVS, providing enhanced security and performance features over NFS v3. | 
| External NVMe datastores | Use FSx for ONTAP as NVMe-based external datastores for VMware vSphere on Amazon EVS, delivering high-performance block storage for demanding workloads. | 
| iSCSI datastores | Configure FSx for ONTAP as iSCSI-based VMFS datastores for VMware vSphere on Amazon EVS. | 
| Guest-mounted iSCSI disks | Present FSx for ONTAP iSCSI LUNs directly to guest virtual machines running on Amazon EVS as in-guest connected storage. | 
| NetApp SnapCenter Plug-in for VMware vSphere (SCV) | Use NetApp SnapCenter Plug-in for VMware vSphere to provide application-consistent backup and restore operations for VMs and datastores running on Amazon EVS. | 
| Deployment using EVS Expansion VLAN | Deploy FSx for ONTAP external datastores using an Amazon EVS Expansion VLAN for dedicated storage network traffic, providing network isolation and improved performance. | 