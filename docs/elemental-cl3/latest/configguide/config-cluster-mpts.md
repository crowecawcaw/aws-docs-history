# Dedicating interfaces to MPTS

This section applies only of your cluster includes AWS Elemental Statmux nodes.

You must perform an extra configuration step on every Elemental Statmux node and on any Elemental Live node
that will be produce SPTS outputs for an Elemental Statmux MPTS:

- On each Elemental Statmux node, you must identify two interfaces that will handle MPTS
  communications between this node and any Elemental Live node.
- On each affected Elemental Live node, you must identify two interfaces that will handle MPTS
  communications between this node and any Elemental Statmux node.

###### To identify dedicated interfaces

1. On each Elemental Statmux node, identify two interfaces from the Ethernet interfaces [that you have created](config-conductor-live-ethernet-create.md "config-conductor-live-ethernet-create.md").

On each Elemental Live node, identify two interfaces from the Ethernet interfaces [that you have created](config-conductor-live-ethernet-create.md "config-conductor-live-ethernet-create.md").

We recommend that you dedicate two interfaces on every node, to provided network
redundancy. These interfaces can be separate or they can be already bonded
together. 2. On the primary Conductor Live web interface, choose the **Cluster** page,
then choose **Nodes**. 3. On the **Nodes** page, select the hostname of an Elemental Statmux or Elemental Live
node. Don't selected the node by its IP address. The node details page appears for this
node. 4. Choose the **Network** tab. On the menu across the top, choose the
**MPTS Configuration** tab. (Note that this tab is the only read-write
tab on this page. The other **Network** tabs are read-only.) 5. Complete the **MPTS Configuration** page as follows:

    * In the **Interface 1** and **Interface 2**
     fields, select the IP addresses that you identified.


    If you identified only one interface, select the same value in both fields.


    If you identified a bonded interface, select the same value in both fields.
    * In the **Cluster Multicast Address** field, enter a multicast
     address. A multicast address ensures that communications will resume if either the
     Elemental Statmux or the Elemental Live node fails over.

6. Repeat steps 3 to 5 on every Elemental Statmux node and on every affected Elemental Live node.
