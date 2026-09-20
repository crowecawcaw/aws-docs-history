

# Creating a Conductor Live redundancy group
<a name="conductor-live-config-redundancy-cl"></a>

If you are implementing Conductor Live redundancy, then you should have two Conductor Live nodes — a primary node and a secondary node. You must create a redundancy group and add the nodes to this group. 

**Redundancy groups and a VLAN**

The redundancy group that you create always runs in HA (high availability) mode. In this mode, the two Conductor Live nodes must be on the same VLAN

**The VIP and the Conductor Live redundancy group**

When you create the redundancy group, as described in the procedure that follows, you assign a virtual IP address to the group. 

This address serves as the constant *cluster ID* for the primary and secondary Conductor Live nodes. When you enable HA (high availability), one of the two Conductor Live nodes registers as the primary node with this VIP. This node you go to enable HA, and it is the node that initially registers as the primary. Later, any time a Conductor Live node failover occurs, the node that's promoted to primary re-registers with the VIP to indicate that this node is now the primary node.

**To create a Conductor Live redundancy group**

1. Make sure that the secondary Conductor Live node is in the cluster [Adding (recruiting) worker nodes to the cluster](conductor-live-config-nodes-add.md).

1. On the primary Conductor Live web interface, go to the **Cluster** page and choose **Redundancy**.

1. On the **Redundancy** page, choose **New Redundancy Group** and select **Elemental Conductor Live**.

1. In the **Add New Redundancy Group** dialog, complete the fields and choose **Add**. See the table for information on each field.



<table>
<thead>
  <tr><th>Field</th><th>Description</th><th></th></tr>
</thead>
<tbody>
  <tr><td><b>Redundancy Group Name</b></td><td>Any name that you choose. </td><td></td></tr>
  <tr><td><b>Virtual IP Address</b></td><td>A valid IPv4 address. The address must meet these conditions:<ul><li> It must be an address on your network that will never be allocated to any other host. </li><li> It must be on the same subnet as the Conductor Live nodes. </li></ul></td><td></td></tr>
  <tr><td><b>Virtual Router Identifier (VRID)</b></td><td>The VRID must meet these conditions:<ul><li> It must be an integer 1–254.  </li><li> The value must not conflict with any other instance of <code>keepalived</code> (or any other VRRP service) that's running on the network. You must make sure that there are no conflicts. Elemental Live can't detect them.  </li></ul></td><td></td></tr>
</tbody>
</table>


**To add Conductor Live nodes**

Follow these steps on the primary Conductor Live node.

1. On the **Redundancy** page, select the Conductor Live redundancy group. Choose **Add HA Nodes**.

1. On the dialog, select a Conductor Live node from the **Nodes** dropdown list.

1. Choose **Add** . 