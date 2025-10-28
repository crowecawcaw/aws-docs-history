# Set the MTU of an AWS Direct Connect private virtual interface

If your virtual interface has both an IPv4 and IPv6 BGP peering session, you can delete
one of the BGP peering sessions (but not both). For more information about MTUs and private
virtual interfaces, see [MTUs for private virtual
interfaces or transit virtual interfaces](WorkingWithVirtualInterfaces.md#set-jumbo-frames-vif.title "WorkingWithVirtualInterfaces.md#set-jumbo-frames-vif.title").

You can set the MTU of a private virtual interface using either the AWS Direct Connect console or using the command line or API.

###### To set the MTU of a private virtual interface

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Virtual Interfaces**.
3. Select the virtual interface and then choose
   **Edit**.
4. Under **Jumbo MTU (MTU size 8500)**, select
   **Enabled**.
5. Under **Acknowledge**, select **I understand the
   selected connection(s) will go down for a brief period**. The state
   of the virtual interface is `pending` until the update is
   complete.

###### To set the MTU of a private virtual interface using the command line or

API

- [update-virtual-interface-attributes](../../../cli/latest/reference/directconnect/update-virtual-interface-attributes.md "../../../cli/latest/reference/directconnect/update-virtual-interface-attributes.md") (AWS CLI)
- [UpdateVirtualInterfaceAttributes](../APIReference/API_UpdateVirtualInterfaceAttributes.md "../APIReference/API_UpdateVirtualInterfaceAttributes.md") (AWS Direct Connect API)
