# Adding worker nodes

###### Topics

- [Step A: Add worker nodes to the
  cluster](#migrate-topic-add-w-cluster "#migrate-topic-add-w-cluster")
- [Step B: Add worker nodes to redundancy
  groups](#migrate-topic-add-w-red "#migrate-topic-add-w-red")
- [Step C: Add node assignments](#migrate-topic-add-w-channels "#migrate-topic-add-w-channels")

## Step A: Add worker nodes to the

cluster

1.  On the web interface for the primary Conductor node, choose the
    **Cluster** page, then choose
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
      3. When Conductor Live displays the IP address that corresponds to
         the hostname, choose the plus sign beside the address to add
         it to the Node IP address list.
      4. Choose **Add**.

4.  Still in the **Add Nodes to Cluster** dialog, add each
    node that will be a part of the cluster.
5.  Verify that the nodes have been added to the list on the
    **Nodes** page and the correct information is
    shown:
    - The **Status** is
      **Online**.
    - The **Elemental Product** is the correct type of
      node, either Conductor Live or a worker.

6.  If any worker nodes contain SDI cards, import the devices so that the Conductor
    node knows about them. Do the following:

        1. Still on the primary Conductor, go to **Nodes** page
         and find the first worker node that has an SDI card, Beside that
         node, choose the downward triangle and select **Import
         Devices**.


        Conductor Live detects the device and adds the device's configuration to
         the Conductor Live database.
        2. Repeat for every worker node that has an SDI card.

    If you don't import the devices, they won't appear in the Conductor Live web
    interface. You won't be able to specify these devices as video sources in a
    channel.

## Step B: Add worker nodes to redundancy

groups

1. On the web interface for the primary Conductor node, choose the
   **Cluster** page, then choose
   **Redundancy**. In the navigation bar, choose the Elemental Live
   redundancy group.
2. On the **Active Nodes** tab, choose **Add to
   Active**. In the **Nodes** field, select the
   nodes to add to the group.
3. Choose **Add**.
4. On the **Backup Nodes** tab, choose **Add to
   Backup Nodes**. In the **Nodes** field, select
   the nodes to add to the group. Make sure that you add nodes in order,
   starting with the reserve node with the highest priority.
5. Choose **Add**.
6. If you have multiple Elemental Live redundancy groups, repeat this procedure on
   each group.

## Step C: Add node assignments

To assign channels back to a node, use the [list of channel assignments](migrate-std-prepare-node.md#migrate-std-capture-assignments "migrate-std-prepare-node.md#migrate-std-capture-assignments")
that you created for the node.

1. On the web interface for the primary Conductor node, display the
   **Channels** page, then choose
   **Tasks**, then choose **Change
   channel node assignments**.
2. Select the channels that should all be assigned to one node, according to
   your list. Choose **Next**.
3. On the **Select a new node** page, in **New
   Node**, choose the node for these channel.
4. Choose **Next**, then choose **Process Now**.
