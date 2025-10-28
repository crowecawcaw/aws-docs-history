# Step I: Add worker nodes

Add the worker nodes back to the cluster and their redundancy groups. Perform these
steps for all worker nodes that are supposed to be in the cluster.

###### Topics

- [Step A: Add worker nodes to the
  cluster](#upg-std-add-w-cluster "#upg-std-add-w-cluster")
- [Step B: Add worker nodes to redundancy
  groups](#upg-std-add-w-red "#upg-std-add-w-red")
- [Step C: Add channel assignments](#upg-std-add-w-channels "#upg-std-add-w-channels")

## Step A: Add worker nodes to the

cluster

Add the worker nodes back to the cluster.

###### To add nodes to the cluster

1.  On the primary Conductor Live node's web interface, go to the
    **Cluster** page and choose
    **Nodes**.
2.  On the **Nodes** page, choose **Add
    Node**.
3.  In the **Add Nodes to Cluster** dialog, do one of the
    following:
    - In **Node IP Address/s**, enter the IP address or
      range of IP addresses for multiple nodes and choose
      **Add**.
    - If your network has a DNS server, search for the node by its
      hostname:
      1. In **Lookup Node IP Address**, enter the
         hostname of the node that you're adding. You set the
         hostname during installation of the node.
      2. Choose the **search** icon.
      3. When Conductor Live displays the IP address that corresponds
         to the hostname, choose the plus sign beside the address to
         add it to the Node IP address list.
      4. Choose **Add**.

4.  Still in the **Add Nodes to Cluster** dialog, add each
    node that will be a part of the cluster.
5.  Verify that the nodes are added to the list on the Nodes screen and the
    correct information is shown:
    - The **Status** is
      **Online**.
    - The **Elemental Product** is the correct type of
      node, either Conductor Live or AWS Elemental Live.

6.  If any nodes contain SDI cards, import the devices so that the Conductor Live node
    knows about them. Do the following:

        1. On a node that as SDI cards, choose the downward triangle and
         select **Import Devices**.


        Conductor Live detects the device and adds its configuration to the
         Conductor Live database.
        2. Import the devices for all nodes that use SDI cards.

    If you don't import the devices, they won't appear in the Conductor Live web
    interface. You won't be able to specify these devices as video sources in a
    channel.

## Step B: Add worker nodes to redundancy

groups

Add the workers to their redundancy groups.

For more information about adding workers to redundancy groups, see _Add
Worker Node Redundancy_ in the [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").

###### To add workers to redundancy groups

1. On the primary Conductor Live node's web interface, go to the
   **Cluster** page.
2. On the **Cluster** page, choose
   **Redundancy**.
3. In the navigation bar, choose the Elemental Live redundancy group.
4. On the **Active Nodes** tab, choose **Add to
   Active**.
5. In the **Nodes** field, select the nodes to add to the
   group.
6. Choose **Add**.
7. On the **Backup Nodes** tab, choose **Add to
   Backup Nodes**.
8. In the **Nodes** field, select the nodes to add to the
   group. Make sure that you add nodes in order, starting with the reserve node
   with the highest priority.
9. Choose **Add**.
10. If you have multiple Elemental Live redundancy groups, repeat this procedure on
    each group, and then go to the next step.

## Step C: Add channel assignments

Assign channels back to the nodes.

###### To assign channels to the workers

1. On the primary Conductor Live node's web interface, go to the
   **Channels** page.
2. Choose **Edit**(pencil icon) on a channel.
3. On the **Edit Channel** page, in
   **Node**, choose the node that this channel will use.
4. Save the channel. Repeat this procedure to edit the remaining channels to
   have the correct node assignment.
5. When all of the channels have node assignments, go to the next
   step.
