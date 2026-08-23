# Configure FSx for NetApp ONTAP as an NFS datastore

The following procedure details the minimum steps required to configure FSx for NetApp ONTAP as an NFS datastore for Amazon EVS using the FSx console and the VMware vSphere client interface that runs on Amazon EVS.

## Prerequisites

Before you use Amazon EVS with Amazon FSx for NetApp ONTAP, make sure that the following prerequisite tasks have been completed.

- An Amazon EVS environment is deployed in your Virtual Private Cloud (VPC).
  For more information, see [Getting started with Amazon Elastic VMware Service](getting-started.md "getting-started.md").
- You have access to your vSphere client running on Amazon EVS.
- You or your storage admin must have necessary permissions to create and manage FSx for ONTAP file systems in your VPC.
  For more information, see [Identity and access management for Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/security-iam.md "../../../fsx/latest/ONTAPGuide/security-iam.md").

Your IAM principal has appropriate permissions to create and manage FSx for ONTAP file systems in your VPC.
For more information, see [Create and manage an Amazon EVS environment](security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-create-env "security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-create-env").

## Create an FSx for NetApp ONTAP file system

Amazon EVS is a single Availability Zone service, but you can use either a Single-AZ or Multi-AZ FSx for ONTAP file system. If you choose a Multi-AZ file system, all VPC route tables used by your Amazon EVS host subnets must be associated with that file system. For the full file-system creation workflow, see [Creating FSx for ONTAP file systems](../../../fsx/latest/ONTAPGuide/creating-file-systems.md "../../../fsx/latest/ONTAPGuide/creating-file-systems.md") in the _Amazon FSx for NetApp ONTAP User Guide_.

When you reach the networking and volume configuration pages of the FSx creation wizard, apply the following Amazon EVS-specific settings:

1. Select the Amazon EVS VPC that has connectivity to your Amazon EVS VLAN subnets.
2. Select a security group that permits all required FSx for ONTAP NFS
   traffic to the Amazon EVS host VMkernel management VLAN subnet.
3. Select the Amazon EVS service access subnet that your file system will be deployed in.
   For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet "concepts.md#concepts-service-access-subnet").
4. For **Junction path**, specify a meaningful name such as `/vol1` to identify this volume
   in vSphere.
5. Within **Default volume configuration**, set **Storage efficiency** to **Enabled**.

## Retrieve the NFS DNS name for the storage virtual machine

1. Go to the [Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx").
2. On the left menu, select **File systems**.
3. Choose the newly created file system.
4. Select the **Storage virtual machines** tab.
5. Choose the storage virtual machine.
6. Select the **Endpoints** tab.
7. Copy the network file system (NFS) DNS name for later use in VMware Vsphere.

## Create an NFS datastore in vSphere using the FSx for ONTAP volume

Follow the instructions in [Create an NFS Datastore in vSphere Environment](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-B52657D0-248D-4A99-99CC-D35B350461D5-en "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-B52657D0-248D-4A99-99CC-D35B350461D5-en")to configure Amazon FSx for NetApp ONTAP as external storage for VMware vSphere.
For the Server setting in the vSphere client interface, use the storage virtual machine (SVM) NFS DNS name that you copied in the previous step.
