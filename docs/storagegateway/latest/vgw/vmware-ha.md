# Using VMware vSphere High Availability with Storage Gateway

Storage Gateway provides high availability on VMware through a set of application-level health
checks integrated with VMware vSphere High Availability (VMware HA). This approach helps
protect storage workloads against hardware, hypervisor, or network failures. It also helps
protect against software errors, such as connection timeouts and file share or volume
unavailability.

vSphere HA works by pooling virtual machines and the hosts they reside on into a cluster
for redundancy. Hosts in the cluster are monitored and in the event of a failure, the
virtual machines on a failed host are restarted on alternate hosts. Generally, this recovery
happens quickly and without data loss. For more information about vSphere HA, see [How vSphere HA Works](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.avail.doc/GUID-33A65FF7-DA22-4DC5-8B18-5A7F97CCA536.html "https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.avail.doc/GUID-33A65FF7-DA22-4DC5-8B18-5A7F97CCA536.html") in the VMware documentation.

###### Note

The time required to restart a failed virtual machine and re-establish the iSCSI
connection on a new host depends on many factors, such as the host operating system and
resource load, disk speed, network connection, and SAN/storage infrastructure. To
minimize failover downtime, implement the recommendations outlined in [Optimizing
Gateway Performance](Performance.md#Optimizing-common "Performance.md#Optimizing-common").

To use Storage Gateway with VMware HA, we recommend doing the following things:

- Deploy the VMware ESX `.ova` downloadable package that contains the
  Storage Gateway VM on only one host in a cluster.
- When deploying the `.ova` package, select a data store that is not
  local to one host. Instead, use a data store that is accessible to all hosts in
  the cluster. If you select a data store that is local to a host and the host
  fails, then the data source might not be accessible to other hosts in the
  cluster and failover to another host might not succeed.
- To prevent your initiator from disconnecting from storage volume targets
  during failover, follow the recommended iSCSI settings for your operating
  system. In a failover event, it can take from a few seconds to several minutes
  for a gateway VM to start in a new host in the failover cluster. The recommended
  iSCSI timeouts for both Windows and Linux clients are greater than the typical
  time it takes for failover to occur. For more information on customizing Windows
  clients' timeout settings, see [Customizing Your Windows iSCSI
  Settings](recommendediSCSISettings.md#CustomizeWindowsiSCSISettings "recommendediSCSISettings.md#CustomizeWindowsiSCSISettings"). For more information on
  customizing Linux clients' timeout settings, see [Customizing Your Linux iSCSI
  Settings](recommendediSCSISettings.md#CustomizeLinuxiSCSISettings "recommendediSCSISettings.md#CustomizeLinuxiSCSISettings").
- With clustering, if you deploy the `.ova` package to the cluster,
  select a host when you are prompted to do so. Alternately, you can deploy
  directly to a host in a cluster.
  The following topics describe how to deploy Storage Gateway in a VMware HA cluster:

###### Topics

- [Configure Your vSphere VMware HA
  Cluster](#vmware-ha-configure-cluster "#vmware-ha-configure-cluster")
- [Download the .ova Image from the Storage Gateway
  console](#vmware-ha-download-image "#vmware-ha-download-image")
- [Deploy the Gateway](#vmware-ha-deploy-gateway "#vmware-ha-deploy-gateway")
- [(Optional) Add Override Options for Other VMs on
  Your Cluster](#vmware-ha-overrides "#vmware-ha-overrides")
- [Activate Your Gateway](#vmware-ha-activate-gateway "#vmware-ha-activate-gateway")
- [Test Your VMware High Availability
  Configuration](#vmware-ha-test-failover "#vmware-ha-test-failover")

## Configure Your vSphere VMware HA

Cluster

First, if you haven’t already created a VMware cluster, create one. For information
about how to create a VMware cluster, see [Create a vSphere HA Cluster](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.avail.doc/GUID-4BC60283-B638-472F-B1D2-1E4E57EAD213.html "https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.avail.doc/GUID-4BC60283-B638-472F-B1D2-1E4E57EAD213.html") in the VMware documentation.

Next, configure your VMware cluster to work with Storage Gateway.

###### To configure your VMware cluster

1.  On the **Edit Cluster Settings** page in VMware vSphere, make
    sure that VM monitoring is configured for VM and application monitoring. To do
    so, set the following values for each option:
    - **Host Failure Response**: **Restart
      VMs**
    - **Response for Host Isolation**: **Shut down
      and restart VMs**
    - **Datastore with PDL**:
      **Disabled**
    - **Datastore with APD**:
      **Disabled**
    - **VM Monitoring**: **VM and Application
      Monitoring**

2.  Fine-tune the sensitivity of the cluster by adjusting the following values:

        * **Failure interval** – After this interval,
         the VM is restarted if a VM heartbeat isn't received.
        * **Minimum uptime** – The cluster waits this
         long after a VM starts to begin monitoring for VM tools'
         heartbeats.
        * **Maximum per-VM resets** – The cluster
         restarts the VM a maximum of this many times within the maximum resets
         time window.
        * **Maximum resets time window** – The window of
         time in which to count the maximum resets per-VM resets.

    If you aren't sure what values to set, use these example settings:

        * **Failure interval**: `30`
         seconds
        * **Minimum uptime**: `120`
         seconds
        * **Maximum per-VM resets**:
         `3`
        * **Maximum resets time window**:
         `1` hour

If you have other VMs running on the cluster, you might want to set these values
specifically for your VM. You can't do this until you deploy the VM from the .ova. For
more information on setting these values, see [(Optional) Add Override Options for Other VMs on
Your Cluster](#vmware-ha-overrides "#vmware-ha-overrides").

## Download the .ova Image from the Storage Gateway

console

###### To download the .ova image for your gateway

- On the **Set up gateway** page in the Storage Gateway console, select
  your gateway type and host platform, then use the link provided in the console
  to download the .ova as outlined in [Set up a
  Volume Gateway](create-volume-gateway.md "create-volume-gateway.md").

## Deploy the Gateway

In your configured cluster, deploy the .ova image to one of the cluster's
hosts.

###### To deploy the gateway .ova image

1. Deploy the .ova image to one of the hosts in the cluster.
2. Make sure the data stores that you choose for the root disk and the cache are
   available to all hosts in the cluster. When deploying the Storage Gateway .ova
   file in a VMware or on-prem environment, the disks are described as
   paravirtualized SCSI disks. _Paravirtualization_ is a mode
   where the gateway VM works with the host operating system so the console can
   identify the virtual disks that you add to your VM.

To configure your VM to use paravirtualized controllers

    1. In the VMware vSphere client, open the context (right-click) menu for
     your gateway VM, and then choose **Edit
     Settings**.
    2. In the **Virtual Machine Properties** dialog box,
     choose the **Hardware** tab, select the **SCSI
     controller 0**, and then choose **Change
     Type**.
    3. In the **Change SCSI Controller Type** dialog box,
     select the **VMware Paravirtual SCSI** controller type,
     and then choose **OK**.

## (Optional) Add Override Options for Other VMs on

Your Cluster

If you have other VMs running on your cluster, you might want to set the cluster
values specifically for each VM. For instructions, see [Customize an Individual Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.avail.doc/GUID-CFD74742-26EA-4BED-A4FC-4E8F50A46C83.html "https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.avail.doc/GUID-CFD74742-26EA-4BED-A4FC-4E8F50A46C83.html") in the VMware vSphere online
documentation.

###### To add override options for other VMs on your cluster

1. On the **Summary** page in VMware vSphere, choose your
   cluster to open the cluster page, and then choose
   **Configure**.
2. Choose the **Configuration** tab, and then choose
   **VM Overrides**.
3. Add a new VM override option to change each value.

Set the following values for each option under **vSphere HA - VM
Monitoring**:

    * **VM Monitoring**: **Override
     Enabled** - **VM and Application
     Monitoring**
    * **VM monitoring sensitivity**: **Override
     Enabled** - **VM and Application
     Monitoring**
    * **VM Monitoring**: **Custom**
    * **Failure interval**: `30`
    **seconds**
    * **Minimum uptime**: `120`
    **seconds**
    * **Maximum per-VM resets**:
     `5`
    * **Maximum resets time window**:
     **Within**
    `1`
    **hrs**

## Activate Your Gateway

After the .ova for your gateway is deployed, activate your gateway. The instructions
about how are different for each gateway type.

###### To activate your gateway

- Follow the procedures outlined in the following topics:
  1.  [Connect your Volume Gateway to AWS](create-volume-gateway.md#connect-to-amazon-volume "create-volume-gateway.md#connect-to-amazon-volume")
  2.  [Review settings and activate your Volume Gateway](create-volume-gateway.md#review-and-activate-volume "create-volume-gateway.md#review-and-activate-volume")
  3.  [Configure your Volume Gateway](create-volume-gateway.md#configure-gateway-volume "create-volume-gateway.md#configure-gateway-volume")

## Test Your VMware High Availability

Configuration

After you activate your gateway, test your configuration.

###### To test your VMware HA configuration

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. On the navigation pane, choose **Gateways**, and then choose
   the gateway that you want to test for VMware HA.
3. For **Actions**, choose **Verify VMware
   HA**.
4. In the **Verify VMware High Availability Configuration** box
   that appears, choose **OK**.

###### Note

Testing your VMware HA configuration reboots your gateway VM and
interrupts connectivity to your gateway. The test might take a few minutes
to complete.

If the test is successful, the status of **Verified** appears
in the details tab of the gateway in the console. 5. Choose **Exit**.

You can find information about VMware HA events in the Amazon CloudWatch log groups. For more
information, see [Getting Volume Gateway Health Logs with CloudWatch Log Groups](monitoring-volume-gateway.md#cw-log-groups-volume "monitoring-volume-gateway.md#cw-log-groups-volume").
