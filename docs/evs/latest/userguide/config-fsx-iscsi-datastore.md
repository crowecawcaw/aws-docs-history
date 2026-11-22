

# Configure FSx for ONTAP as an iSCSI datastore

You can present Amazon FSx for NetApp ONTAP block storage to the ESX hosts in your Amazon Elastic VMware Service environment over iSCSI, and use it as a VMFS datastore. You use the Amazon FSx console, the NetApp ONTAP CLI, and the vSphere Client. To use NVMe/TCP instead, see [Configure FSx for ONTAP as an NVMe/TCP datastore](config-fsx-nvme-datastore.md).

## Before you begin
<a name="fsx-evs-prereqs-iscsi"></a>

Make sure that you meet the following prerequisites.
+ Your Amazon EVS environment is deployed in your VPC. For more information, see [Deploy](deploy-overview.md).
+ You have access to the vSphere Client for your Amazon EVS environment.
+ You or your storage administrator have the permissions to create and manage FSx for ONTAP file systems in your VPC. For more information, see [Identity and access management for Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html).
+ You can run commands in the NetApp ONTAP CLI of the file system.

## In the Amazon FSx console, create an FSx for NetApp ONTAP file system
<a name="create-fsx-file-system-iscsi"></a>

You can use a Single-AZ or Multi-AZ file system. If you choose Multi-AZ, read the route table requirement in [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md) first. For the full file system creation workflow, see [Creating FSx for ONTAP file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-file-systems.html) in the *Amazon FSx for NetApp ONTAP User Guide*.

When you reach the networking and volume configuration pages of the FSx creation wizard, apply the following Amazon EVS settings.

1. Select the Amazon EVS VPC that has connectivity to your Amazon EVS VLAN subnets.

1. Select a security group that permits all required FSx for ONTAP iSCSI traffic to the Amazon EVS host VMkernel management VLAN subnet.

1. Select the Amazon EVS service access subnet for your file system. For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet).

1. Within **Default volume configuration**, set **Storage efficiency** to **Enabled**.

After the file system is created, copy the iSCSI IP address of the storage virtual machine (SVM). You can find it in the [Amazon FSx console](https://console.aws.amazon.com/fsx) on the **Endpoints** tab of the SVM. You use it for dynamic discovery in vSphere.

## In the vSphere Client, configure the iSCSI adapter
<a name="config-iscsi-adapter"></a>

For each ESX host, you must configure the software iSCSI adapter so that the host can access iSCSI storage. We recommend that you use the host management VMkernel adapter (`vmk0`) for iSCSI traffic. For instructions, see [Add or Remove the Software iSCSI Adapter](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/configuring-iscsi-and-iser-adapters-and-storage-with-esxi/configure-the-software-iscsi-adapter-with-esxi/add-or-remove-the-software-iscsi-adapter.html) in the Broadcom documentation.

After you configure the adapter, copy the iSCSI Qualified Name (IQN) of the adapter on each host. You use the IQNs when you create the initiator group.

## In the ONTAP CLI, create an iSCSI LUN
<a name="config-iscsi-lun"></a>

FSx for ONTAP can create logical unit numbers (LUNs) for iSCSI access, which provide shared block storage to your ESX hosts. You use the NetApp ONTAP CLI to create a LUN.

**Note**  
We recommend that you set the LUN size to 90% of the volume size.

The following is a sample command. Replace the values in angle brackets with your own values.

```bash
lun create -vserver <svm-name> \
-path /vol/<volume-name>/<lun-name> \
-size <datastore-capacity> \
-ostype vmware
```

For more information, see [Creating an iSCSI LUN](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/create-iscsi-lun.html) in the *FSx for ONTAP User Guide*.

## In the ONTAP CLI, create an initiator group and map the LUN
<a name="config-initiator-group"></a>

Next, create an initiator group (`igroup`) that contains the ESX hosts, and map the LUN to it. Replace the values in angle brackets with your own values.

1. Create the initiator group. For `-initiator`, use the IQNs that you copied from the iSCSI adapters. The following is a sample command.

   ```bash
   igroup create <svm-name> \
   -igroup <igroup-name> \
   -protocol iscsi \
   -ostype vmware \
   -initiator <iqn-1>,<iqn-2>,<iqn-3>,<iqn-4>
   ```

1. Confirm that the `igroup` exists.

   ```bash
   lun igroup show
   ```

1. Map the LUN to the initiator group. The following is a sample command.

   ```bash
   lun mapping create -vserver <svm-name> \
   -path /vol/<volume-name>/<lun-name> \
   -igroup <igroup-name> \
   -lun-id <lun-id>
   ```

1. Confirm that the LUN is created, online, and mapped.

   ```bash
   lun show -path /vol/<volume-name>/<lun-name> -fields state,mapped,serial-hex
   ```

For more information, see [Provisioning iSCSI for Linux](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-iscsi-luns-linux.html) or [Provisioning iSCSI for Windows](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-iscsi-windows.html) in the *FSx for ONTAP User Guide*.

## In the vSphere Client, configure dynamic discovery of the iSCSI LUN
<a name="config-dynamic-discovery-vsphere"></a>

To let the ESX hosts see the iSCSI LUN, configure dynamic discovery on each host. For the iSCSI server, enter the iSCSI IP address of the SVM that you copied after you created the file system. For instructions, see [Configure Dynamic or Static Discovery for iSCSI and iSER on ESX Host](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/configuring-iscsi-and-iser-adapters-and-storage-with-esxi/configure-dynamic-or-static-discovery-for-iscsi-and-iser-on-esxi-host.html#GUID-4ED3304A-ED4F-4692-825F-83637E04D592-en) in the Broadcom documentation.

## In the vSphere Client, create a VMFS datastore
<a name="create-vmfs"></a>

Virtual Machine File System (VMFS) datastores are repositories for virtual machines. To create the datastore, follow the instructions in [Create a vSphere VMFS Datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-5AC611E0-7CEB-4604-A03C-F600B1BA2D23-en) in the Broadcom documentation. When you are prompted to select a device, choose the iSCSI LUN that you configured.

You have configured FSx for ONTAP as an iSCSI datastore for your Amazon EVS environment. To confirm, open the datastore in the vSphere Client and check that every ESX host in the initiator group is listed on its **Hosts** tab.

For a Multi-AZ file system, configure multipathing on the ESX hosts so that the datastore stays available during a failover. For more information, see [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md).