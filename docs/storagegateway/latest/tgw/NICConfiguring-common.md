# Configuring network adapters for your

gateway

By default, Storage Gateway is configured to use the E1000 network adapter type, but you
can reconfigure your gateway to use the VMXNET3 (10 GbE) network adapter. You can
also configure Storage Gateway so it can be accessed by more than one IP address. You
do this by configuring your gateway to use more than one network adapter.

###### Topics

- [Configuring Your Gateway to Use the VMXNET3
  Network Adapter](#NICChanging-common "#NICChanging-common")
- [Configuring Your Gateway for
  Multiple NICs](#MaintenanceMultiNIC-common "#MaintenanceMultiNIC-common")

## Configuring Your Gateway to Use the VMXNET3

Network Adapter

Storage Gateway supports the E1000 network adapter type in both VMware ESXi and
Microsoft Hyper-V hypervisor hosts. However, the VMXNET3 (10 GbE) network
adapter type is supported in VMware ESXi hypervisor only. If your gateway is
hosted on a VMware ESXi hypervisor, you can reconfigure your gateway to use the
VMXNET3 (10 GbE) adapter type. For more information on these adapters, see
[Choosing a network adapter for your virtual machine](https://knowledge.broadcom.com/external/article/321259/choosing-a-network-adapter-for-your-virt.html "https://knowledge.broadcom.com/external/article/321259/choosing-a-network-adapter-for-your-virt.html") on the Broadcom
(VMware) website.

###### Important

To select VMXNET3, your guest operating system type must be
**Other Linux64**.

Following are the steps you take to configure your gateway to use the VMXNET3
adapter:

1. Remove the default E1000 adapter.
2. Add the VMXNET3 adapter.
3. Restart your gateway.
4. Configure the adapter for the network.

Details on how to perform each step follow.

###### To remove the default E1000 adapter and configure your gateway to use the

VMXNET3 adapter

1. In VMware, open the context (right-click) menu for your gateway and
   choose **Edit Settings**.
2. In the **Virtual Machine Properties** window, choose
   the **Hardware** tab.
3. For **Hardware**, choose **Network
   adapter**. Notice that the current adapter is E1000 in the
   **Adapter Type** section. You will replace this
   adapter with the VMXNET3 adapter.
4. Choose the E1000 network adapter, and then choose
   **Remove**. In this example, the E1000 network
   adapter is **Network adapter 1**.

###### Note

Although you can run the E1000 and VMXNET3 network adapters in
your gateway at the same time, we don't recommend doing so because
it can cause network problems. 5. Choose **Add** to open the Add Hardware
wizard. 6. Choose **Ethernet Adapter**, and then choose
**Next**. 7. In the Network Type wizard, select `VMXNET3` for
**Adapter Type**, and then choose
**Next**. 8. In the Virtual Machine properties wizard, verify in the
**Adapter Type** section that **Current
Adapter** is set to **VMXNET3**, and then
choose **OK**. 9. In the VMware VSphere client, shut down your gateway. 10. In the VMware VSphere client, restart your gateway.

After your gateway restarts, reconfigure the adapter you just added to make
sure that network connectivity to the internet is established.

###### To configure the adapter for the network

1. In the VSphere client, choose the **Console** tab to
   start the local console. Use the default login credentials to log in to
   the gateway's local console for this configuration task. For information
   about how to log in using the default credentials, see [Logging in to the Local Console Using Default
   Credentials](manage-on-premises-common.md#LocalConsole-login-common "manage-on-premises-common.md#LocalConsole-login-common").
2. At the prompt, enter the corresponding numeral to select
   **Network Configuration**.
3. At the prompt, enter the corresponding numeral to select
   **Reset all to DHCP**, and then enter
   `y` (for yes) at the prompt to set all adapters
   to use Dynamic Host Configuration Protocol (DHCP). All available
   adapters are set to use DHCP.

If your gateway is already activated, you must shut it down and
restart it from the Storage Gateway Management Console. After the gateway
restarts, you must test network connectivity to the internet. For
information about how to test network connectivity, see [Testing Your Gateway Connection to the Internet](manage-on-premises-common.md#MaintenanceTestGatewayConnectivity-common "manage-on-premises-common.md#MaintenanceTestGatewayConnectivity-common").

## Configuring Your Gateway for

Multiple NICs

If you configure your gateway to use multiple network adapters (NICs), it can
be accessed by more than one IP address. You might want to do this in the
following situations:

- **Maximizing
  throughput** – You might want to
  maximize throughput to a gateway when network adapters are a
  bottleneck.
- **Application
  separation** – You might need to
  separate how your applications write to a gateway's volumes. For
  example, you might choose to have a critical storage application
  exclusively use one particular adapter defined for your gateway.
- **Network
  constraints** – Your application
  environment might require that you keep your iSCSI targets and the
  initiators that connect to them in an isolated network that is different
  from the network by which the gateway communicates with AWS.

In a typical multiple-adapter use case, one adapter is configured as the route
by which the gateway communicates with AWS (that is, as the default gateway).
Except for this one adapter, initiators must be in the same subnet as the
adapter that contains the iSCSI targets to which they connect. Otherwise,
communication with the intended targets might not be possible. If a target is
configured on the same adapter that is used for communication with AWS, then
iSCSI traffic for that target and AWS traffic will flow through the same
adapter.

When you configure one adapter to connect to the Storage Gateway console and then add
a second adapter, Storage Gateway automatically configures the route table to
use the second adapter as the preferred route. For instructions on how to
configure multiple-adapters, see the following sections.

- [Configuring multiple network
  adapters on a VMware ESXi host](#MaintenanceMultiNIC-vmaware "#MaintenanceMultiNIC-vmaware")
- [Configuring multiple network
  adapters on Microsoft Hyper-V host](#MaintenanceMultiNIC-hyperv "#MaintenanceMultiNIC-hyperv")

### Configuring multiple network

adapters on a VMware ESXi host

The following procedure assumes that your gateway VM already has one
network adapter defined, and describes how to add an adapter on VMware
ESXi.

###### To configure your gateway to use an additional network adapter in

VMware ESXi host

1. Shut down the gateway.
2. In the VMware vSphere client, select your gateway VM.

The VM can remain turned on for this procedure. 3. In the client, open the context (right-click) menu for your
gateway VM, and choose **Edit Settings**. 4. On the **Hardware** tab of the **Virtual
Machine Properties** dialog box, choose
**Add** to add a device. 5. Follow the Add Hardware wizard to add a network adapter.

    1. In the **Device Type** pane, choose
     **Ethernet Adapter** to add an adapter,
     and then choose **Next**.
    2. In the **Network Type** pane, ensure that
     **Connect at power on** is selected for
     **Type**, and then choose
     **Next**.


    We recommend that you use the VMXNET3 network adapter with
     Storage Gateway. For more information on the adapter types that
     might appear in the adapter list, see Network Adapter Types
     in the [ESXi and vCenter Server Documentation](http://pubs.vmware.com/vsphere-50/index.jsp?topic=/com.vmware.vsphere.vm_admin.doc_50/GUID-AF9E24A8-2CFA-447B-AC83-35D563119667.html&resultof=%22VMXNET%22%20%22vmxnet%22 "http://pubs.vmware.com/vsphere-50/index.jsp?topic=/com.vmware.vsphere.vm_admin.doc_50/GUID-AF9E24A8-2CFA-447B-AC83-35D563119667.html&resultof=%22VMXNET%22%20%22vmxnet%22").
    3. In the **Ready to Complete** pane, review
     the information, and then choose
     **Finish**.

6. Choose the **Summary** tab for the VM, and choose
   **View All** next to the **IP
   Address** box. The **Virtual Machine IP
   Addresses** window displays all the IP addresses you
   can use to access the gateway. Confirm that a second IP address is
   listed for the gateway.

###### Note

It might take several moments for the adapter changes to take
effect and the VM summary information to refresh. 7. In the Storage Gateway console, turn on the gateway. 8. In the **Navigation** pane of the Storage Gateway
console, choose **Gateways** and choose the gateway
to which you added the adapter. Confirm that the second IP address
is listed in the **Details** tab.

For information about local console tasks common to VMware, Hyper-V, and
KVM hosts, see [Performing Tasks on the VM Local Console](manage-on-premises-common.md "manage-on-premises-common.md")

### Configuring multiple network

adapters on Microsoft Hyper-V host

The following procedure assumes that your gateway VM already has one
network adapter defined and that you are adding a second adapter. This
procedure shows how to add an adapter for a Microsoft Hyper-V host.

###### To configure your gateway to use an additional network adapter in a

Microsoft Hyper-V Host

1. On the Storage Gateway console, turn off the gateway.
2. In the Microsoft Hyper-V Manager, select your gateway VM from the
   **Virtual Machines** panel.
3. If the gateway VM isn't turned off already, right-click the VM
   name to open the context menu, and then choose **Turn
   Off**.
4. Right-click the gateway VM name to open the context menu, and then
   choose **Settings**.
5. In the **Settings** dialog box, under
   **Hardware**, choose **Add
   Hardware**.
6. In the **Add Hardware** panel on the right side
   of the **Settings** dialog box, choose
   **Network Adapter**, and then choose
   **Add** to add a device.
7. Configure the network adapter, and then choose
   **Apply** to apply settings.
8. In the **Settings** dialog box, under
   **Hardware**, confirm that the new network
   adapter was added to the hardware list, and then choose
   **OK**.
9. Turn on the gateway using the Storage Gateway console.
10. In the **Navigation** panel of the Storage Gateway
    console, choose **Gateways**, then select the
    gateway to which you added the adapter. Confirm that a second IP
    address is listed in the **Details** tab.

For information about local console tasks common to VMware, Hyper-V, and
KVM hosts, see [Performing Tasks on the VM Local Console](manage-on-premises-common.md "manage-on-premises-common.md")
