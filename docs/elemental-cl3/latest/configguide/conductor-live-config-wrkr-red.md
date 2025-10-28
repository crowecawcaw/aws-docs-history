# Creating worker redundancy

groups

To set up worker nodes for failover resiliency, you create one or
more redundancy groups, then you add worker nodes to each group.

For general information about how failover resiliency works, and
for detailed information about design redundancy groups that meet
your requirements, see [_Conductor Live User
Guide_](../ug.md "../ug.md").

###### To create a redundancy group

1. On the primary Conductor Live web interface, go to the
   **Cluster** page and choose
   **Redundancy**.
2. On the **Redundancy** page, choose
   **New Redundancy Group** and select the
   node type.
3. Enter a name for the redundancy group and choose
   **Add**.
   The group is added to the list on the left side of the Redundancy
   screen. At this point, no nodes are in the group.

###### To add nodes

Follow these steps on the primary Conductor Live node.

1. On the **Redundancy** page, select the
   group that you're adding nodes to. Two tabs appear on the
   right — **Active Nodes** and
   **Backup Nodes**.
2. Select **Active Nodes** tab, then choose
   **Add Active Nodes**.
3. On the dialog, select a node from the
   **Nodes** dropdown list. Only nodes
   that aren't in a redundancy group appear in this list.

If you are setting up an N+M type of group, add several
nodes. 4. Choose **Add** to add the selected nodes
to the group. 5. Repeat these steps to add nodes to the **Backup
Nodes** tab.
The nodes are listed on the **Active Nodes** or
the **Backup Nodes** tab of the redundancy group.

Make sure that you add nodes to both tabs.
