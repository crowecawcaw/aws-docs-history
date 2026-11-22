

# Configure FSx for ONTAP as an NFS datastore

You can mount an Amazon FSx for NetApp ONTAP volume as an NFS datastore on the ESX hosts in your Amazon Elastic VMware Service environment. In this procedure, you use the Amazon FSx console and the vSphere Client to create the datastore.

## Before you begin
<a name="fsx-evs-prereqs-nfs"></a>

Make sure that you meet the following prerequisites.
+ Your Amazon EVS environment is deployed in your VPC. For more information, see [Deploy](deploy-overview.md).
+ You have access to the vSphere Client for your Amazon EVS environment.
+ You or your storage administrator have the permissions to create and manage FSx for ONTAP file systems in your VPC. For more information, see [Identity and access management for Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html).

## In the Amazon FSx console, create an FSx for NetApp ONTAP file system
<a name="create-fsx-file-system-nfs"></a>

You can use a Single-AZ or Multi-AZ file system. If you choose Multi-AZ, read the route table requirement in [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md) first. For the full file system creation workflow, see [Creating FSx for ONTAP file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-file-systems.html) in the *Amazon FSx for NetApp ONTAP User Guide*.

When you reach the networking and volume configuration pages of the FSx creation wizard, apply the following Amazon EVS settings.

1. Select the Amazon EVS VPC that has connectivity to your Amazon EVS VLAN subnets.

1. Select a security group that permits all required FSx for ONTAP NFS traffic to the Amazon EVS host VMkernel management VLAN subnet.

1. Select the Amazon EVS service access subnet for your file system. For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet).

1. For **Junction path**, enter a name that identifies this volume in vSphere, such as `/vol1`.

1. Within **Default volume configuration**, set **Storage efficiency** to **Enabled**.

## In the Amazon FSx console, get the NFS DNS name
<a name="create-fsx-volume-nfs"></a>

To get the NFS DNS name of the storage virtual machine (SVM), do the following.

1. Open the [Amazon FSx console](https://console.aws.amazon.com/fsx).

1. In the navigation pane, choose **File systems**.

1. Choose the file system that you created.

1. Choose the **Storage virtual machines** tab.

1. Choose the storage virtual machine.

1. Choose the **Endpoints** tab.

1. Copy the NFS DNS name. You use it in the vSphere Client.

## In the vSphere Client, create the NFS datastore
<a name="attach-fsx-volume-vsphere-nfs"></a>

To create the datastore from the FSx for ONTAP volume, do the following.

1. Follow the instructions in [Create an NFS Datastore in vSphere Environment](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-B52657D0-248D-4A99-99CC-D35B350461D5-en) in the Broadcom documentation.

1. For the **Server** setting, enter the NFS DNS name of the SVM that you copied.

1. For the folder, enter the junction path of the volume.

1. Select the ESX hosts that must have access to the datastore.

## In the vSphere Client, verify the datastore
<a name="verify-fsx-volume-vsphere-nfs"></a>

To verify the datastore, do the following.

1. In the vSphere Client, open the **Datastores** view.

1. Choose the new datastore.

1. Confirm that the datastore is accessible and that its capacity matches the size of the FSx for ONTAP volume.

1. On the **Hosts** tab of the datastore, confirm that every ESX host that you selected is listed.

You have configured FSx for ONTAP as an NFS datastore for your Amazon EVS environment.

If the hosts can’t mount the datastore, check the security group rules and the routes between the service access subnet and the VMkernel management VLAN subnet. For help, see [Troubleshoot networking](troubleshoot-networking.md).