

# Use Amazon FSx for NetApp ONTAP with Amazon EVS

Amazon FSx for NetApp ONTAP is a storage service that you use to launch and run fully managed ONTAP file systems in the cloud. Amazon Elastic VMware Service supports FSx for ONTAP as an NFS, iSCSI, or NVMe/TCP datastore for your ESX hosts and as guest-connected storage for virtual machines.

For more information about FSx for ONTAP, see the [FSx for ONTAP User Guide](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html).

## How FSx for ONTAP connects to your environment
<a name="fsx-ontap-architecture"></a>

You create the FSx for ONTAP file system in the same VPC as your Amazon EVS environment. The file system is deployed in the Amazon EVS service access subnet. For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet).

The ESX hosts reach the file system through the endpoints of a storage virtual machine (SVM). NFS datastores use the NFS DNS name of the SVM. iSCSI and NVMe/TCP datastores use the iSCSI logical interface (LIF) IP address of the SVM.

A security group on the file system controls this traffic. It must permit the traffic for your protocol to the Amazon EVS host VMkernel management VLAN subnet. For the ports that FSx for ONTAP uses, see [File system access control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limit-access-security-groups.html) in the *FSx for ONTAP User Guide*.

You can also send storage traffic over an Amazon EVS expansion VLAN to keep it apart from other traffic.

## Single-AZ and Multi-AZ file systems
<a name="fsx-ontap-multi-az"></a>

An Amazon EVS environment runs in one Availability Zone. For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc). You can use either a Single-AZ or a Multi-AZ FSx for ONTAP file system.

If you choose a Multi-AZ file system, you must associate it with every VPC route table that your Amazon EVS host subnets use. FSx for ONTAP adds routes to each associated route table, and a file system supports a limited number of routes. For the route rules and limits, see [Availability and durability](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html) and [Quotas](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limits.html) in the *FSx for ONTAP User Guide*.

During a Multi-AZ failover, NFS datastores reconnect without action from you because the endpoint IP address stays the same. For iSCSI and NVMe/TCP datastores, the failover is transparent only if you configure multipathing on the ESX hosts.

**Important**  
A Multi-AZ file system doesn’t keep your Amazon EVS environment running if its Availability Zone fails, because the environment runs in one Availability Zone. To recover, you create an environment in another Availability Zone, mount the volumes, and register the virtual machines again. For recovery planning, see [Resilience for Amazon EVS](disaster-recovery-resiliency.md).

## Choose a storage protocol
<a name="fsx-ontap-protocol-choice"></a>

All three protocols use the same kind of FSx for ONTAP file system. They differ in the datastore type and in the setup on ONTAP and on the ESX hosts.


| Protocol | Datastore type | Setup on ONTAP | Setup on each ESX host | Requirement | 
| --- | --- | --- | --- | --- | 
| NFS v3 or NFS v4.1 | NFS | A volume with a junction path | None beyond mounting the datastore | None | 
| iSCSI | VMFS | A LUN, an initiator group, and a LUN mapping | A software iSCSI adapter and dynamic discovery | None | 
| NVMe/TCP | VMFS | A namespace and a subsystem with the host NQNs | A software NVMe over TCP adapter and a controller | A second-generation file system with 6 or fewer HA pairs | 

For instructions, see [Configure FSx for ONTAP as an NFS datastore](config-fsx-nfs-datastore.md), [Configure FSx for ONTAP as an iSCSI datastore](config-fsx-iscsi-datastore.md), or [Configure FSx for ONTAP as an NVMe/TCP datastore](config-fsx-nvme-datastore.md).

## Supported FSx for NetApp ONTAP capabilities
<a name="fsx-ontap-supported-capabilities"></a>

The following FSx for NetApp ONTAP capabilities are available for use with Amazon EVS.


| Capability | Description | 
| --- | --- | 
| External NFS v3 datastores | Mount FSx for ONTAP volumes as NFS v3 datastores for VMware vSphere on Amazon EVS. | 
| External NFS v4.1 datastores | Mount FSx for ONTAP volumes as NFS v4.1 datastores for VMware vSphere on Amazon EVS, with added security and performance features over NFS v3. | 
| External NVMe datastores | Use FSx for ONTAP as NVMe-based external datastores for VMware vSphere on Amazon EVS, for block storage for demanding workloads. | 
| iSCSI datastores | Configure FSx for ONTAP as iSCSI-based VMFS datastores for VMware vSphere on Amazon EVS. | 
| Guest-mounted iSCSI disks | Present FSx for ONTAP iSCSI LUNs directly to guest virtual machines running on Amazon EVS as in-guest connected storage. | 
| NetApp SnapCenter Plug-in for VMware vSphere | Provide application-consistent backup and restore operations for VMs and datastores that run on Amazon EVS. | 
| Deployment using Amazon EVS expansion VLAN | Deploy FSx for ONTAP external datastores using an Amazon EVS expansion VLAN for dedicated storage network traffic. | 