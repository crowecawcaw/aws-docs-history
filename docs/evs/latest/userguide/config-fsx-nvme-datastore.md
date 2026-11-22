

# Configure FSx for ONTAP as an NVMe/TCP datastore

You can present Amazon FSx for NetApp ONTAP block storage to the ESX hosts in your Amazon Elastic VMware Service environment over NVMe/TCP, and use it as a VMFS datastore. You use the Amazon FSx console, the NetApp ONTAP CLI, and the vSphere Client. To use iSCSI instead, see [Configure FSx for ONTAP as an iSCSI datastore](config-fsx-iscsi-datastore.md).

**Important**  
NVMe/TCP requires a second-generation FSx for ONTAP file system with six or fewer HA pairs. Choose a second-generation file system when you create it.

## Before you begin
<a name="fsx-evs-prereqs-nvme"></a>

Make sure that you meet the following prerequisites.
+ Your Amazon EVS environment is deployed in your VPC. For more information, see [Deploy](deploy-overview.md).
+ You have access to the vSphere Client for your Amazon EVS environment.
+ You or your storage administrator have the permissions to create and manage FSx for ONTAP file systems in your VPC. For more information, see [Identity and access management for Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html).
+ You can run commands in the NetApp ONTAP CLI of the file system and the ESX shell of each host.

## In the Amazon FSx console, create an FSx for NetApp ONTAP file system
<a name="create-fsx-file-system-nvme"></a>

You can use a Single-AZ or Multi-AZ file system. If you choose Multi-AZ, read the route table requirement in [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md) first. For the full file system creation workflow, see [Creating FSx for ONTAP file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-file-systems.html) in the *Amazon FSx for NetApp ONTAP User Guide*.

When you reach the networking and volume configuration pages of the FSx creation wizard, apply the following Amazon EVS settings.

1. Select the Amazon EVS VPC that has connectivity to your Amazon EVS VLAN subnets.

1. Select a security group that permits all required FSx for ONTAP NVMe/TCP traffic to the Amazon EVS host VMkernel management VLAN subnet.

1. Select the Amazon EVS service access subnet for your file system. For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet).

1. Within **Default volume configuration**, set **Storage efficiency** to **Enabled**.

## In the vSphere Client, configure the NVMe/TCP adapter
<a name="config-nvme-tcp-adapter"></a>

For each ESX host, you must configure the software NVMe over TCP adapter so that the host can access NVMe/TCP storage. We recommend that you use the host management VMkernel adapter (`vmk0`) for NVMe/TCP traffic. For instructions, see [Configuring NVMe over TCP on ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage/about-vmware-nvme-storage/configuring-nvme-over-tcp-on-esxi.html) in the Broadcom documentation.

After you configure the adapter, copy the NVMe Qualified Name (NQN) of each ESX host. To get the host NQN, run the following command on the host.

```bash
esxcli nvme info get
```

You use the NQNs when you add hosts to the subsystem.

## In the ONTAP CLI, create an NVMe namespace and subsystem
<a name="config-nvme-namespace"></a>

FSx for ONTAP can create NVMe namespaces for NVMe/TCP access, which provide shared block storage to your ESX hosts. You use the NetApp ONTAP CLI to create a namespace and a subsystem, map the namespace to the subsystem, and add the host NQNs. Replace the values in angle brackets with your own values.

1. Create the namespace. The following is a sample command.

   ```bash
   vserver nvme namespace create -vserver <svm-name> \
   -path /vol/<volume-name>/<namespace-name> \
   -size <datastore-capacity> \
   -ostype vmware
   ```

1. Create the subsystem.

   ```bash
   vserver nvme subsystem create -vserver <svm-name> \
   -subsystem <subsystem-name> \
   -ostype vmware
   ```

1. Map the namespace to the subsystem.

   ```bash
   vserver nvme subsystem map add -vserver <svm-name> \
   -subsystem <subsystem-name> \
   -path /vol/<volume-name>/<namespace-name>
   ```

1. Add the NQN of an ESX host to the subsystem. Repeat this command for each host that needs access to the namespace.

   ```bash
   vserver nvme subsystem host add -vserver <svm-name> \
   -subsystem <subsystem-name> \
   -host-nqn <host-nqn>
   ```

1. Confirm that the namespace exists.

   ```bash
   vserver nvme namespace show -vserver <svm-name>
   ```

For more information, see [Provisioning NVMe/TCP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/provision-nvme-linux.html) in the *FSx for ONTAP User Guide*.

## In the vSphere Client, add a controller for the NVMe namespace
<a name="config-nvme-discovery-vsphere"></a>

To let the ESX hosts see the NVMe namespace, add a controller on the NVMe over TCP adapter of each host.

1. Get the iSCSI IP address of the storage virtual machine (SVM). FSx for ONTAP uses the same SVM endpoints for iSCSI and NVMe/TCP. You can find the address in the [Amazon FSx console](https://console.aws.amazon.com/fsx) on the **Endpoints** tab of the SVM, or by running the following command in the ONTAP CLI. Replace the values in angle brackets with your own values.

   ```bash
   network interface show -vserver <svm-name> -data-protocol nvme-tcp
   ```

1. In the vSphere Client, add a controller on the NVMe over TCP adapter of each host, and use that IP address as the target address. For instructions, see [Configuring NVMe over TCP on ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage/about-vmware-nvme-storage/configuring-nvme-over-tcp-on-esxi.html) in the Broadcom documentation.

## In the vSphere Client, create a VMFS datastore
<a name="create-vmfs-nvme"></a>

Virtual Machine File System (VMFS) datastores are repositories for virtual machines. To create the datastore, follow the instructions in [Create a vSphere VMFS Datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage-8-0/working-with-datastores-in-vsphere-storage-environment/creating-vsphere-datastores.html#GUID-5AC611E0-7CEB-4604-A03C-F600B1BA2D23-en) in the Broadcom documentation. When you are prompted to select a device, choose the NVMe namespace that you configured.

You have configured FSx for ONTAP as an NVMe/TCP datastore for your Amazon EVS environment. To confirm, open the datastore in the vSphere Client and check that every ESX host that you added to the subsystem is listed on its **Hosts** tab.

For a Multi-AZ file system, configure multipathing on the ESX hosts so that the datastore stays available during a failover. For more information, see [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md).