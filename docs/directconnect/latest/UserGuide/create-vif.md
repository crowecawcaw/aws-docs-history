# AWS Direct Connect virtual interfaces

You can create a transit virtual interface to connect to a transit gateway, a public
virtual interface to connect to public resources (non-VPC services), or a private
virtual interface to connect to a VPC.

To create a virtual interface for accounts within your AWS Organizations, or AWS Organizations that are
different from yours, create a hosted virtual interface.

See the following to create a virtual interface:

- [Create a public virtual interface](create-public-vif.md "create-public-vif.md")
- [Create a private virtual interface](create-private-vif.md "create-private-vif.md")
- [Create a transit virtual interface to the Direct Connect
  gateway](create-transit-vif-dx.md "create-transit-vif-dx.md")

###### Prerequisites

Before you begin, ensure that you have read the information in [Prerequisites for virtual interfaces](WorkingWithVirtualInterfaces.md#vif-prerequisites "WorkingWithVirtualInterfaces.md#vif-prerequisites").

## Prerequisites for transit virtual interfaces to a Direct Connect gateway

To connect your AWS Direct Connect connection to the transit gateway, you must create a
transit interface for your connection. Specify the Direct Connect gateway to which
to connect.

The maximum transmission unit (MTU) of a network connection is the size, in bytes,
of the largest permissible packet that can be passed over the connection. The MTU of
a private virtual interface can be either 1500 or 9001 (jumbo frames). The MTU of a
transit virtual interface can be either 1500 or 8500 (jumbo frames). You can specify
the MTU when you create the interface or update it after you create it. Setting the
MTU of a virtual interface to 8500 (jumbo frames) or 9001 (jumbo frames) can cause
an update to the underlying physical connection if it wasn't updated to support
jumbo frames. Updating the connection disrupts network connectivity for all virtual
interfaces associated with the connection for up to 30 seconds. To check whether a
connection or virtual interface supports jumbo frames, select it in the AWS Direct Connect
console and find **Jumbo Frame Capable** on the
**Summary** tab.

###### Important

If you associate your transit gateway with one or more Direct Connect gateways, the Autonomous System Number (ASN) used by the transit gateway and the Direct Connect gateway must be different. For example, if you use the default ASN 64512 for both the transit gateway and the Direct Connect gateway, the association request fails.
