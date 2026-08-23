# Configure FSx for NetApp ONTAP as a block datastore

FSx for ONTAP block storage can be presented to your ESX hosts over iSCSI or NVMe/TCP. Both protocols use the same FSx for ONTAP file system and result in a VMFS datastore. They differ in how you configure the ESXi storage adapter and provision the block device on ONTAP. NVMe/TCP requires a second-generation file system with 6 or fewer HA pairs. Choose one protocol and follow the corresponding sections.

## Prerequisites

Before you use Amazon EVS with Amazon FSx for NetApp ONTAP, make sure that the following prerequisite tasks have been completed.

- An Amazon EVS environment is deployed in your Virtual Private Cloud (VPC).
  For more information, see [Getting started with Amazon Elastic VMware Service](getting-started.md "getting-started.md").
- You have access to your vSphere client running on Amazon EVS.
- You or your storage admin must have necessary permissions to create and manage FSx for ONTAP file systems in your VPC.
  For more information, see [Identity and access management for Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/security-iam.md "../../../fsx/latest/ONTAPGuide/security-iam.md").

## Create an FSx for NetApp ONTAP file system

Amazon EVS is a single Availability Zone service, but you can use either a Single-AZ or Multi-AZ FSx for ONTAP file system. If you choose a Multi-AZ file system, all VPC route tables used by your Amazon EVS host subnets must be associated with that file system. For the full file-system creation workflow, see [Creating FSx for ONTAP file systems](../../../fsx/latest/ONTAPGuide/creating-file-systems.md "../../../fsx/latest/ONTAPGuide/creating-file-systems.md") in the _Amazon FSx for NetApp ONTAP User Guide_.

When you reach the networking and volume configuration pages of the FSx creation wizard, apply the following Amazon EVS-specific settings:

1. Select the Amazon EVS VPC that has connectivity to your Amazon EVS VLAN subnets.
2. Select a security group that permits all required FSx for ONTAP iSCSI or NVMe/TCP traffic to the Amazon EVS host VMkernel management VLAN subnet.
3. Select the Amazon EVS service access subnet that your file system will be deployed in.
   For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet "concepts.md#concepts-service-access-subnet").
4. Within **Default volume configuration**, set **Storage efficiency** to **Enabled**.

## Configure a software iSCSI adapter in vSphere for ESX host storage

For each ESX host, you must configure the software iSCSI adapter so that your ESX
hosts can use it to access iSCSI storage.
For instruction to configure the software iSCSI adapter for ESX hosts in vSphere, see [Add or Remove the Software iSCSI Adapter](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/configuring-iscsi-and-iser-adapters-and-storage-with-esxi/configure-the-software-iscsi-adapter-with-esxi/add-or-remove-the-software-iscsi-adapter.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/configuring-iscsi-and-iser-adapters-and-storage-with-esxi/configure-the-software-iscsi-adapter-with-esxi/add-or-remove-the-software-iscsi-adapter.html") in the VMware vSphere product documentation.

After you configure the software iSCSI adapter, copy the iSCSI Qualified Name (IQN) associated with an iSCSI adapter.
These values will be used later.

## Configure a software NVMe over TCP adapter in vSphere for ESX host storage

For each ESX host, you must configure the software NVMe over TCP adapter so that your ESX hosts can use it to access NVMe/TCP storage.
For instructions to configure the software NVMe over TCP adapter for ESX hosts in vSphere, see [Configuring NVMe over TCP on ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage/about-vmware-nvme-storage/configuring-nvme-over-tcp-on-esxi.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage/about-vmware-nvme-storage/configuring-nvme-over-tcp-on-esxi.html") in the VMware vSphere product documentation.

After you configure the software NVMe over TCP adapter, copy the NVMe Qualified Name (NQN) associated with the ESXi host.
You can retrieve the host NQN by running `esxcli nvme info get` on the ESXi host.
These values will be used later.

## Create an iSCSI LUN

FSx for ONTAP allows you to create Logical Unit Numbers (LUNs) that are specifically intended for iSCSI access, providing shared block storage to your ESX hosts.
You use the NetApp ONTAP CLI to create a LUN.

The following is a sample command.

###### Note

It is recommended to configure the LUN size to 90% of the volume size.

```
lun create -vserver <your_svm_name> \
-path /vol/<your_volume_name>/<lun_name> \
-size <required_datastore_capacity> \
-ostype vmware
```

For more information, see [Creating an iSCSI LUN](../../../fsx/latest/ONTAPGuide/create-iscsi-lun.md "../../../fsx/latest/ONTAPGuide/create-iscsi-lun.md") in the _FSx for ONTAP User Guide_.

## Configure and map an initiator group to the iSCSI LUN

Now that you have created an iSCSI LUN, the next step in the process is to create an initiator group (`igroup`) to connect the volume to the cluster and map the LUN to the initiator group.
You use the NetApp ONTAP CLI to perform these actions.

1. Configure the initiator group.

The following is a sample command.
For `--initiator`, use the iSCSI adapter IQNs that you copied in the previous step.

```
igroup create <svm_name> \
-igroup <initiator_group_name> \
-protocol iscsi \
-ostype vmware \
-initiator <esxi_iqn_1>,<esxi_iqn_2>,<esxi_iqn_3>,<esxi_iqn_4>
```

2. Confirm that the `igroup` exists.

```
lun igroup show
```

3. Map the LUN to the initiator group.
   The following is a sample command.

```
lun mapping create -vserver <svm_name> \
-path /vol/<vol_name>/<lun_name> \
-igroup <initiator_group_name> \
-lun-id <scsi_lun_number_for this_datastore>
```

4. Use the `lun show -path` command to confirm that the LUN is created, online, and mapped.

```
lun show -path /vol/<vol_name>/<lun_name> -fields state,mapped,serial-hex
```

For more information, see [Provisioning iSCSI for Linux](../../../fsx/latest/ONTAPGuide/mount-iscsi-luns-linux.md "../../../fsx/latest/ONTAPGuide/mount-iscsi-luns-linux.md") or [Provisioning iSCSI for Windows](../../../fsx/latest/ONTAPGuide/mount-iscsi-windows.md "../../../fsx/latest/ONTAPGuide/mount-iscsi-windows.md") in the _FSx for ONTAP User Guide_.

## Configure dynamic discovery of the iSCSI LUN in vSphere

To allow the ESX hosts to see the iSCSI LUN, you must configure dynamic discovery for each host in the vSphere client interface.
For the iSCSI server field, enter the (NFS) DNS name that you copied in the previous step.
For more information, see [Configure Dynamic or Static Discovery for iSCSI and iSER on ESX
Host](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/configuring-iscsi-and-iser-adapters-and-storage-with-esxi/configure-dynamic-or-static-discovery-for-iscsi-and-iser-on-esxi-host.html#GUID-4ED3304A-ED4F-4692-825F-83637E04D592-en "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/configuring-iscsi-and-iser-adapters-and-storage-with-esxi/configure-dynamic-or-static-discovery-for-iscsi-and-iser-on-esxi-host.html#GUID-4ED3304A-ED4F-4692-825F-83637E04D592-en") in the VMware vSphere product documentation.

## Create an NVMe namespace

FSx for ONTAP allows you to create NVMe namespaces that are specifically intended for NVMe/TCP access, providing shared block storage to your ESX hosts.
You use the NetApp ONTAP CLI to create a namespace, create a subsystem, map the namespace to the subsystem, and add your ESXi host NQNs.

The following are sample commands.

```
vserver nvme namespace create -vserver <your_svm_name> \
-path /vol/<your_volume_name>/<namespace_name> \
-size <required_datastore_capacity> \
-ostype vmware

vserver nvme subsystem create -vserver <your_svm_name> \
-subsystem <subsystem_name> \
-ostype vmware

vserver nvme subsystem map add -vserver <your_svm_name> \
-subsystem <subsystem_name> \
-path /vol/<your_volume_name>/<namespace_name>

vserver nvme subsystem host add -vserver <your_svm_name> \
-subsystem <subsystem_name> \
-host-nqn <esxi_host_nqn>
```

Repeat the `subsystem host add` command for each ESXi host NQN that requires access to this namespace.

To verify, run:

```
vserver nvme namespace show -vserver <your_svm_name>
```

For more information, see [Provisioning NVMe/TCP](../../../fsx/latest/ONTAPGuide/provision-nvme-linux.md "../../../fsx/latest/ONTAPGuide/provision-nvme-linux.md") in the _FSx for ONTAP User Guide_.

## Configure discovery of the NVMe namespace in vSphere

To allow the ESX hosts to see the NVMe namespace, you must add a controller on the NVMe over TCP adapter for each host in the vSphere client interface.
Use the SVM’s iSCSI LIF IP address as the target address when adding the controller; FSx for ONTAP uses the same SVM endpoints for both iSCSI and NVMe/TCP.
You can find this IP address in the Amazon FSx console on the SVM’s **Endpoints** tab, or by running `network interface show -vserver <your_svm_name> -data-protocol nvme-tcp` in the ONTAP CLI.
For more information, see [Configuring NVMe over TCP on ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage/about-vmware-nvme-storage/configuring-nvme-over-tcp-on-esxi.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage/about-vmware-nvme-storage/configuring-nvme-over-tcp-on-esxi.html") in the VMware vSphere product documentation.

## Create a VMFS datastore in VMware vSphere

Virtual Machine File System (VMFS) datastores serve as repositories for VMware virtual machines.
Follow the instruction in [Create a vSphere VMFS Datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-5AC611E0-7CEB-4604-A03C-F600B1BA2D23-en "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-5AC611E0-7CEB-4604-A03C-F600B1BA2D23-en") to set up the VMFS datastore in VMware vSphere. When prompted to select a device, choose the iSCSI LUN or NVMe namespace that you previously configured.
