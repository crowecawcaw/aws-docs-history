Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Using VMware vSphere High Availability with Storage Gateway

Storage Gateway provides high availability on VMware through a set of application-level health
checks integrated with VMware vSphere High Availability (VMware HA). This approach helps
protect storage workloads against hardware, hypervisor, or network failures. It also helps
protect against software errors, such as connection timeouts and file share or volume
unavailability.

With this integration, a gateway deployed in a VMware environment on-premises or in a
VMware Cloud on AWS automatically recovers from most service interruptions. It generally
does this in under 60 seconds with no data loss.

###### Note

We recommend doing the following things if you deploy Storage Gateway in a VMware HA
cluster:

- Deploy the VMware ESX .ova downloadable package that contains the Storage
  Gateway VM on only one host in a cluster.
- When deploying the .ova package, select a data store that is not local to one
  host. Instead, use a data store that is accessible to all hosts in the cluster.
  If you select a data store that is local to a host and the host fails, then the
  data source might not be accessible to other hosts in the cluster and failover
  to another host might not succeed.
- With clustering, if you deploy the .ova package to the cluster, select a host
  when you are prompted to do so. Alternately, you can deploy directly to a host
  in a cluster.
  The following topics describe how to deploy Storage Gateway in a VMware HA cluster:

###### Topics

- [Configure Your vSphere VMware HA
  Cluster](#vmware-ha-configure-cluster "#vmware-ha-configure-cluster")
- [Set Up Your Gateway Type](#vmware-ha-download-image "#vmware-ha-download-image")
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

## Set Up Your Gateway Type

Use the following procedure to set up the gateway

###### To download the .ova image for your gateway type

- Download the .ova image for your gateway type from one of the
  following:
  - File Gateway – [Create and activate an
    Amazon FSx File Gateway](create-gateway-file.md "create-gateway-file.md")

## Deploy the Gateway

In your configured cluster, deploy the .ova image to one of the cluster's hosts.
For instructions, see [Deploy an OVF or OVA Template](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-17BEDA21-43F6-41F4-8FB2-E01D275FE9B4.html "https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-17BEDA21-43F6-41F4-8FB2-E01D275FE9B4.html") in the VMware vSphere online
documentation.

###### To deploy the gateway .ova image

1. Deploy the .ova image to one of the hosts in the cluster.
2. Make sure the data stores that you choose for the root disk and the cache are
   available to all hosts in the cluster.

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

After the .ova is deployed in your VMware environment, activate your gateway using the
Storage Gateway console. For instructions, see [Review settings and activate your Amazon FSx File Gateway](create-gateway-file.md#review-and-activate-fsx-file "create-gateway-file.md#review-and-activate-fsx-file").

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
information, see [Getting FSx File Gateway health logs
with CloudWatch log groups](monitoring-file-gateway.md#cw-log-groups "monitoring-file-gateway.md#cw-log-groups").
