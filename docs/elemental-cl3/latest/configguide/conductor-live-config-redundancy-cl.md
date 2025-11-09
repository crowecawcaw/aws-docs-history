# Creating a

Conductor Live redundancy group

If you are implementing Conductor Live redundancy, then you should have
two Conductor Live nodes — a primary node and a secondary node. You must
create a redundancy group and add the nodes to this group.

**Redundancy groups and a
VLAN**

The redundancy group that you create always runs in HA (high
availability) mode. In this mode, the two Conductor Live nodes must be on
the same VLAN

**The VIP and the Conductor Live redundancy
group**

When you create the redundancy group, as described in the
procedure that follows, you assign a virtual IP address to the
group.

This address serves as the constant _cluster ID_ for the primary and secondary Conductor Live
nodes. When you enable HA (high availability), one of the two Conductor Live
nodes registers as the primary node with this VIP. This node you go
to enable HA, and it is the node that initially registers as the
primary. Later, any time a Conductor Live node failover occurs, the node
that's promoted to primary re-registers with the VIP to indicate
that this node is now the primary node.

###### To create a Conductor Live redundancy group

1. Make sure that the secondary Conductor Live node is in the
   cluster [Adding (recruiting) worker nodes to
   the cluster](conductor-live-config-nodes-add.md "conductor-live-config-nodes-add.md").
2. On the primary Conductor Live web interface, go to the
   **Cluster** page and choose
   **Redundancy**.
3. On the **Redundancy** page, choose
   **New Redundancy Group** and select
   **Elemental Conductor Live**.
4. In the **Add New Redundancy Group**
   dialog, complete the fields and choose
   **Add**. See the table for information
   on each field.

| Field                                   | Description                                                                                                                                                                                                                                                                                                    |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Redundancy Group<br>Name**            | Any name that you choose.                                                                                                                                                                                                                                                                                      |
| **Virtual IP<br>Address**               | A valid IPv4 address. The address must<br>meet these conditions:<br>• It must be an address on your<br>network that will never be allocated to<br>any other host.<br>• It must be on the same subnet as<br>the Conductor Live nodes.                                                                           |
| **Virtual Router Identifier<br>(VRID)** | The VRID must meet these conditions:<br>• It must be an integer 1–254.<br>• The value must not conflict with<br>any other instance of<br>`keepalived` (or any<br>other VRRP service) that's running on<br>the network. You must make sure that<br>there are no conflicts. Elemental Live can't<br>detect them. |

###### To add Conductor Live nodes

Follow these steps on the primary Conductor Live node.

1. On the **Redundancy** page, select the
   Conductor Live redundancy group. Choose **Add HA
   Nodes**.
2. On the dialog, select a Conductor Live node from the
   **Nodes** dropdown list.
3. Choose **Add** .
