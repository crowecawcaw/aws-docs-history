Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Configuring network adapters for your gateway

Storage Gateway uses a single VMXNET3 (10 GbE) network adapter by default, but you can configure
your gateway to use more than one network adapter so that it can be accessed by multiple IP
addresses. You might want to do this in the following situations:

- **Maximizing
  throughput**– You might want to maximize throughput to a
  gateway when network adapters are a bottleneck.
- **Application
  separation** – You might need to separate how your
  applications write to a gateway's volumes. For example, you might choose to have a
  critical storage application exclusively use one particular adapter defined for your
  gateway.
- **Network
  constraints** – Your application environment might
  require that you keep your file shares and the initiators that connect to them in an
  isolated network. This network is different from the network by which the gateway
  communicates with AWS.
  In a typical multiple-adapter use case, one adapter is configured as the route by which
  the gateway communicates with AWS (that is, as the default gateway). Except for this one
  adapter, initiators must be in the same subnet as the adapter that contains the file shares
  to which they connect. Otherwise, communication with the intended targets might not be
  possible. If a target is configured on the same adapter that is used for communication with
  AWS, then file share traffic for that target and AWS traffic flows through the same
  adapter.

In some cases, you might configure one adapter to connect to the Storage Gateway console and
then add a second adapter. In such a case, Storage Gateway automatically configures the route
table to use the second adapter as the preferred route. For instructions on how to configure
multiple adapters, see the following topics:

###### Topics

- [Configuring Your Gateway for Multiple NICs
  on a VMware ESXi Host](#MaintenanceMultiNIC-vmaware "#MaintenanceMultiNIC-vmaware")
- [Configuring Your Gateway for Multiple NICs
  in Microsoft Hyper-V Host](#MaintenanceMultiNIC-hyperv "#MaintenanceMultiNIC-hyperv")

## Configuring Your Gateway for Multiple NICs

on a VMware ESXi Host

The following procedure assumes that your gateway VM already has one network adapter
defined, and describes how to add an adapter on VMware ESXi.

###### To configure your gateway to use an additional network adapter in VMware ESXi

host

1. Shut down the gateway.
2. In the VMware vSphere client, select your gateway VM.

The VM can remain turned on for this procedure. 3. In the client, open the context (right-click) menu for your gateway VM, and
choose **Edit Settings**. 4. On the **Hardware** tab of the **Virtual Machine
Properties** dialog box, choose **Add** to add a
device. 5. Follow the Add Hardware wizard to add a network adapter.

    1. In the **Device Type** pane, choose
     **Ethernet Adapter** to add an adapter, and then
     choose **Next**.
    2. In the **Network Type** pane, ensure that
     **Connect at power on** is selected for
     **Type**, and then choose
     **Next**.


    We recommend that you use the VMXNET3 network adapter with
     Storage Gateway. For more information on the adapter types that might
     appear in the adapter list, see Network Adapter Types in the [ESXi and vCenter Server Documentation](http://pubs.vmware.com/vsphere-50/index.jsp?topic=/com.vmware.vsphere.vm_admin.doc_50/GUID-AF9E24A8-2CFA-447B-AC83-35D563119667.html&resultof=%22VMXNET%22%20%22vmxnet%22 "http://pubs.vmware.com/vsphere-50/index.jsp?topic=/com.vmware.vsphere.vm_admin.doc_50/GUID-AF9E24A8-2CFA-447B-AC83-35D563119667.html&resultof=%22VMXNET%22%20%22vmxnet%22").
    3. In the **Ready to Complete** pane, review the
     information, and then choose **Finish**.

6. Choose the **Summary** tab for the VM, and choose
   **View All** next to the **IP Address**
   box. The **Virtual Machine IP Addresses** window displays all
   the IP addresses you can use to access the gateway. Confirm that a second IP
   address is listed for the gateway.

###### Note

It might take several moments for the adapter changes to take effect and
the VM summary information to refresh. 7. In the Storage Gateway console, turn on the gateway. 8. In the **Navigation** pane of the Storage Gateway console,
choose **Gateways** and choose the gateway to which you added
the adapter. Confirm that the second IP address is listed in the
**Details** tab.

For information about local console tasks common to VMware, Hyper-V, and KVM hosts,
see [Performing tasks on the virtual machine local
console](manage-on-premises-fgw.md "manage-on-premises-fgw.md")

## Configuring Your Gateway for Multiple NICs

in Microsoft Hyper-V Host

The following procedure assumes that your gateway VM already has one network adapter
defined and that you are adding a second adapter. This procedure shows how to add an
adapter for a Microsoft Hyper-V host.

###### To configure your gateway to use an additional network adapter in a Microsoft

Hyper-V Host

1. On the Storage Gateway console, turn off the gateway.
2. In the Microsoft Hyper-V Manager, select your gateway VM from the
   **Virtual Machines** panel.
3. If the gateway VM isn't turned off already, right-click the VM name to open
   the context menu, and then choose **Turn Off**.
4. Right-click the gateway VM name to open the context menu, and then choose
   **Settings**.
5. In the **Settings** dialog box, under
   **Hardware**, choose **Add
   Hardware**.
6. In the **Add Hardware** panel on the right side of the
   **Settings** dialog box, choose **Network
   Adapter**, and then choose **Add** to add a
   device.
7. Configure the network adapter, and then choose **Apply** to
   apply settings.
8. In the **Settings** dialog box, under
   **Hardware**, confirm that the new network adapter was
   added to the hardware list, and then choose **OK**.
9. Turn on the gateway using the Storage Gateway console.
10. In the **Navigation** panel of the Storage Gateway console,
    choose **Gateways**, then select the gateway to which you added
    the adapter. Confirm that a second IP address is listed in the
    **Details** tab.

For information about local console tasks common to VMware, Hyper-V, and KVM hosts,
see [Performing tasks on the virtual machine local
console](manage-on-premises-fgw.md "manage-on-premises-fgw.md")
