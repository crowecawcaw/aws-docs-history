# Worker node redundancy

This section describes redundancy options for worker nodes in an AWS Elemental Conductor Live cluster.
Worker nodes are Elemental Live nodes and Elemental Statmux nodes. The same redundancy options are available
to both types of worker nodes.

You can set up worker nodes in a group in order to provide node
redundancy. When a problem occurs on an active node, a backup node
takes over.

- For Elemental Live nodes, we recommend that when you have statmux
  workflows, you set up Live nodes for redundancy, even if
  your cluster requires only one Elemental Live node.
- For Elemental Statmux nodes, we recommend that you always set up the
  nodes for redundancy.
  You set up node redundancy by setting up redundancy groups. There
  are three types of groups:

- N-to-M
- 1-to-1
- 1-to-1 Plus
  You can set up multiple redundancy groups in the cluster, of the
  same or different types. For example, some nodes in two N-to-M
  redundancy groups, and more important nodes in a 1-to-1 Plus redundancy
  group. The redundancy groups always operate separately from each
  other.

**Node Failure Detection**

Conductor Live maintains contact with the worker nodes in the cluster. If
Conductor Live can no longer communicate with the node, its assumes that the
worker node has failed.

Nodes that are not part of a redundancy group will not fail over,
but Conductor Live will still detect a failure.

Node failure detection is always enabled in Conductor Live. You don't need
to configure it.

###### Topics

- [N-to-M redundancy](redundancy-n-m.md "redundancy-n-m.md")
- [1-to-1 redundancy](redundancy-11.md "redundancy-11.md")
- [1-to-1 Plus
  redundancy](redundancy-11-plus.md "redundancy-11-plus.md")
