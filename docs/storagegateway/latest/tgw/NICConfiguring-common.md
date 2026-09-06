

# Configuring network adapters for your gateway
<a name="NICConfiguring-common"></a>

You can configure Storage Gateway so it can be accessed by more than one IP address. You do this by configuring your gateway to use more than one network adapter.

## Configuring Your Gateway for Multiple NICs
<a name="MaintenanceMultiNIC-common"></a>

If you configure your gateway to use multiple network adapters (NICs), it can be accessed by more than one IP address. You might want to do this in the following situations:

 
+ ****Maximizing throughput**** – You might want to maximize throughput to a gateway when network adapters are a bottleneck.
+ ****Application separation**** – You might need to separate how your applications write to a gateway's volumes. For example, you might choose to have a critical storage application exclusively use one particular adapter defined for your gateway.
+ ****Network constraints**** – Your application environment might require that you keep your iSCSI targets and the initiators that connect to them in an isolated network that is different from the network by which the gateway communicates with AWS.

In a typical multiple-adapter use case, one adapter is configured as the route by which the gateway communicates with AWS (that is, as the default gateway). Except for this one adapter, initiators must be in the same subnet as the adapter that contains the iSCSI targets to which they connect. Otherwise, communication with the intended targets might not be possible. If a target is configured on the same adapter that is used for communication with AWS, then iSCSI traffic for that target and AWS traffic will flow through the same adapter.

 When you configure one adapter to connect to the Storage Gateway console and then add a second adapter, Storage Gateway automatically configures the route table to use the second adapter as the preferred route. For instructions on how to configure multiple-adapters, see the following sections. 
+ [Configuring multiple network adapters on a VMware ESXi host](#MaintenanceMultiNIC-vmaware)
+ [Configuring multiple network adapters on Microsoft Hyper-V host](#MaintenanceMultiNIC-hyperv)

### Configuring multiple network adapters on a VMware ESXi host
<a name="MaintenanceMultiNIC-vmaware"></a>

The following procedure assumes that your gateway VM already has one network adapter defined, and describes how to add an adapter on VMware ESXi.

**To configure your gateway to use an additional network adapter in VMware ESXi host**

1. Shut down the gateway.

1. In the VMware vSphere client, select your gateway VM. 

   The VM can remain turned on for this procedure.

1. In the client, open the context (right-click) menu for your gateway VM, and choose **Edit Settings**.

1. On the **Hardware** tab of the **Virtual Machine Properties** dialog box, choose **Add** to add a device.

1. Follow the Add Hardware wizard to add a network adapter.

   1. In the **Device Type** pane, choose **Ethernet Adapter** to add an adapter, and then choose **Next**.

   1. In the **Network Type** pane, ensure that **Connect at power on** is selected for **Type**, and then choose **Next**.

      We recommend that you use the VMXNET3 network adapter with Storage Gateway. For more information on the adapter types that might appear in the adapter list, see Network Adapter Types in the [ESXi and vCenter Server Documentation](http://pubs.vmware.com/vsphere-50/index.jsp?topic=/com.vmware.vsphere.vm_admin.doc_50/GUID-AF9E24A8-2CFA-447B-AC83-35D563119667.html&resultof=%22VMXNET%22%20%22vmxnet%22).

   1. In the **Ready to Complete** pane, review the information, and then choose **Finish**.

1. Choose the **Summary** tab for the VM, and choose **View All** next to the **IP Address** box. The **Virtual Machine IP Addresses** window displays all the IP addresses you can use to access the gateway. Confirm that a second IP address is listed for the gateway.
**Note**  
It might take several moments for the adapter changes to take effect and the VM summary information to refresh.

1. In the Storage Gateway console, turn on the gateway.

1. In the **Navigation** pane of the Storage Gateway console, choose **Gateways** and choose the gateway to which you added the adapter. Confirm that the second IP address is listed in the **Details** tab.

For information about local console tasks common to VMware, Hyper-V, and KVM hosts, see [Performing Tasks on the VM Local Console](manage-on-premises-common.md)

### Configuring multiple network adapters on Microsoft Hyper-V host
<a name="MaintenanceMultiNIC-hyperv"></a>

The following procedure assumes that your gateway VM already has one network adapter defined and that you are adding a second adapter. This procedure shows how to add an adapter for a Microsoft Hyper-V host.

**To configure your gateway to use an additional network adapter in a Microsoft Hyper-V Host**

1. On the Storage Gateway console, turn off the gateway.

1. In the Microsoft Hyper-V Manager, select your gateway VM from the **Virtual Machines** panel.

1. If the gateway VM isn't turned off already, right-click the VM name to open the context menu, and then choose **Turn Off**.

1. Right-click the gateway VM name to open the context menu, and then choose **Settings**.

1. In the **Settings** dialog box, under **Hardware**, choose **Add Hardware**.

1. In the **Add Hardware** panel on the right side of the **Settings** dialog box, choose **Network Adapter**, and then choose **Add** to add a device.

1. Configure the network adapter, and then choose **Apply** to apply settings.

1. In the **Settings** dialog box, under **Hardware**, confirm that the new network adapter was added to the hardware list, and then choose **OK**.

1. Turn on the gateway using the Storage Gateway console.

1. In the **Navigation** panel of the Storage Gateway console, choose **Gateways**, then select the gateway to which you added the adapter. Confirm that a second IP address is listed in the **Details** tab.

For information about local console tasks common to VMware, Hyper-V, and KVM hosts, see [Performing Tasks on the VM Local Console](manage-on-premises-common.md)