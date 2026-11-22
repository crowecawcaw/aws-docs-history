

# Connect external storage

You can add external storage to the ESX hosts in a running Amazon Elastic VMware Service environment. You add each datastore in vSphere after the environment is running, next to the storage that the hosts already use. You can use the procedures on this page with VCF 5.x and VCF 9.x environments, in either deployment mode.

Using Amazon FSx for NetApp ONTAP as the principal storage of diskless hosts is available only with VCF 9.x in Self-deployed mode.

Choose the procedure by storage service and protocol.


| Storage service | Protocol | Datastore type in vSphere | Procedure | 
| --- | --- | --- | --- | 
| Amazon FSx for NetApp ONTAP | NFS v3 or NFS v4.1 | NFS datastore |  [Configure FSx for ONTAP as an NFS datastore](config-fsx-nfs-datastore.md)  | 
| Amazon FSx for NetApp ONTAP | iSCSI | VMFS datastore |  [Configure FSx for ONTAP as an iSCSI datastore](config-fsx-iscsi-datastore.md)  | 
| Amazon FSx for NetApp ONTAP | NVMe/TCP | VMFS datastore |  [Configure FSx for ONTAP as an NVMe/TCP datastore](config-fsx-nvme-datastore.md)  | 

To decide which protocol to use and how FSx for ONTAP connects to your environment, read [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md) first.

Diskless hosts are available only with VMware Cloud Foundation (VCF) 9.x. For diskless hosts, external storage is the principal storage. You create it during deployment, as described in [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md) and [Configure FSx for OpenZFS as principal storage for diskless hosts](config-fsx-openzfs-datastore.md).

**Topics**
+ [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md)
+ [Configure FSx for ONTAP as an NFS datastore](config-fsx-nfs-datastore.md)
+ [Configure FSx for ONTAP as an iSCSI datastore](config-fsx-iscsi-datastore.md)
+ [Configure FSx for ONTAP as an NVMe/TCP datastore](config-fsx-nvme-datastore.md)