# Configure FSx for NetApp ONTAP FSx as an iSCSI datastore

The following procedure details the minimum steps required to configure FSx for NetApp ONTAP as an iSCSI datastore for Amazon EVS using the FSx console and VMware vSphere client interface that runs on Amazon EVS.

## Prerequisites

Before you use Amazon EVS with Amazon FSx for NetApp ONTAP, make sure that the following prerequisite tasks have been completed.

- An Amazon EVS environment is deployed in your Virtual Private Cloud (VPC).
  For more information, see [Getting started with Amazon Elastic VMware Service](getting-started.md "getting-started.md").
- You have access to your vSphere client running on Amazon EVS.
- You or your storage admin must have necessary permissions to create and manage FSx for ONTAP file systems in your VPC.
  For more information, see [Identity and access management for Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/security-iam.html..md "../../../fsx/latest/ONTAPGuide/security-iam.html..md").

## Create an FSx for NetApp ONTAP file system

1. Go to the [Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx").
2. Choose **Create file system**.
3. Select **Amazon FSx for NetApp ONTAP**.
4. Choose **Next**.
5. Select **Standard create**.
6. For **Deployment type**, select a Single-AZ deployment option.

###### Note

Amazon EVS only supports Single-AZ deployments at this time. 7. For **SSD storage capacity**, specify 1024 GiB. 8. For **Throughput capacity**, choose **Specify throughput capacity**. Choose at least 512 MB/s for Single-AZ 1 or
at least 768 MB/s for Single-AZ 2. 9. Select the Amazon EVS VPC that has connectivity to your Amazon EVS VLAN subnets. 10. Select a security group that permits all required FSx for ONTAP iSCSI
traffic to the Amazon EVS host VMkernel management VLAN subnet. 11. Select the Amazon EVS service access subnet that your file system will be deployed in.
For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet "concepts.md#concepts-service-access-subnet"). 12. Within **Default volume configuration**, set **Storage efficiency** to **Enabled**. 13. Leave the remaining setting at their default values and choose **Next**. 14. Review the file system attributes and choose **Create file system**.

## Configure a software iSCSI adapter in vSphere for ESX host storage

For each ESX host, you must configure the software iSCSI adapter so that your ESX
hosts can use it to access iSCSI storage.
For instruction to configure the software iSCSI adapter for ESX hosts in vSphere, see [Add or Remove the Software iSCSI Adapter](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/configuring-iscsi-and-iser-adapters-and-storage-with-esxi/configure-the-software-iscsi-adapter-with-esxi/add-or-remove-the-software-iscsi-adapter.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/configuring-iscsi-and-iser-adapters-and-storage-with-esxi/configure-the-software-iscsi-adapter-with-esxi/add-or-remove-the-software-iscsi-adapter.html") in the VMware vSphere product documentation.

After you configure the software iSCSI adapter, copy the iSCSI Qualified Name (IQN) associated with an iSCSI adapter.
These values will be used later.

## Create an iSCSI LUN

FSx for ONTAP allows you to create Logical Unit Numbers (LUNs) that are specifically intended for iSCSI access, providing shared block storage to your ESX hosts.
You use the NetApp ONTAP CLI to create a LUN.

Below is a sample command.

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

Below is a sample command.
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
   Below is a sample command.

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

## Create a VMFS Datastore in VMware vSphere using the iSCSI LUN

Virtual Machine File System (VMFS) datastores serve as repositories for VMware virtual machines.
Follow the instruction in [Create a vSphere VMFS Datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-5AC611E0-7CEB-4604-A03C-F600B1BA2D23-en "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-5AC611E0-7CEB-4604-A03C-F600B1BA2D23-en") to set up the VMFS datastore in VMware vSphere using the iSCSI LUN that you previously configured.
