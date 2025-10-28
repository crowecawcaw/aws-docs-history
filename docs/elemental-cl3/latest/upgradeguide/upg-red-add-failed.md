# Step I: Add failed worker node

Add the failed worker back to the cluster and redundancy groups so that it can encode while the remaining workers are upgraded.

## Step A: Add failed

worker to the cluster

Add the failed worker node back to the cluster.

###### To add nodes to the cluster

1.  On the web interface for the primary Conductor Live node, go to the **Cluster** page
    and choose **Nodes**.
2.  On the **Nodes** page, choose
    **Add Node**.
3.  In the **Add Nodes to Cluster**
    dialog, do one of the following:
    - In **Node IP Address/s**,
      enter the IP address or range of IP addresses
      for multiple nodes and choose
      **Add**.
    - If your network has a DNS server, search for
      the node by its hostname:
      1. In **Lookup Node IP
         Address**, enter the hostname
         of the node that you're adding. You
         set the hostname during installation of
         the node.
      2. Choose the **search**
         icon.
      3. When Conductor Live displays the IP
         address that corresponds to the
         hostname, choose the plus sign beside
         the address to add it to the Node IP
         address list.
      4. Choose
         **Add**.

4.  Still in the **Add Nodes to Cluster**
    dialog, add each node that will be a part of the
    cluster.
5.  Verify that the nodes are added to the list on the
    Nodes screen and the correct information is shown:
    - The **Status** is
      **Online**.
    - The **Elemental Product** is
      the correct type of node, either
      Conductor Live or AWS Elemental Live.

6.  If any nodes contain SDI cards, import the devices so
    that the Conductor Live node knows about them. Do the
    following:

        1. On a node that as SDI cards, choose the
         downward triangle and select **Import
         Devices**.


        Conductor Live detects the device and adds
         its configuration to the Conductor Live database.
        2. Import the devices for all nodes that use SDI
         cards.

    If you don't import the devices, they won't
    appear in the Conductor Live web interface. You won't be
    able to specify these devices as video sources in a
    channel.

## Step B: Add failed worker to a redundancy

groups

Add the failed workers to their redundancy groups.

For more information about adding workers to redundancy groups, see _Add Worker Node Redundancy_ in the [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").

###### To add the failed worker to a redundancy group

1. On the web interface for the primary Conductor Live node, go to the **Cluster** page.
2. On the **Cluster** page, choose **Redundancy**.
3. In the navigation bar, choose the Elemental Live redundancy group that this node belongs to.
4. On the **Backup Nodes** tab, choose **Add to Backup Nodes**.
5. In the **Nodes** field, select the failed worker node to add to the group.
6. Choose **Add**.
