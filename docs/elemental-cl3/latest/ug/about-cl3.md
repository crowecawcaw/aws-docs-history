# Working with Conductor Live

AWS Elemental Conductor Live lets you create and manage channels on AWS Elemental Live and/or MPTSes on AWS Elemental Statmux. Each
of the three products—Conductor Live, Elemental Live and Elemental Statmux—runs on its own node. Conductor Live is a _management node_. Elemental Live and Elemental Statmux node are each _worker nodes_.

All the nodes are organized in a _cluster._

Broadly speaking, there are two ways to work with the Conductor Live suite of
products:

- Create and run events (which are called channels in Conductor Live). You use
  Conductor Live to create the channel on an Elemental Live node that is in the cluster. You use
  Conductor Live to start and control the channel.

For this scenario, the cluster includes Conductor Live and Elemental Live nodes.

- Create and run MPTSes. You use Conductor Live to create an MPTS on an Elemental Statmux node
  that is in the cluster. You use the Conductor Live to add Elemental Live channels to the MPTS.
  You use Conductor Live to start and control the MPTS.
  A cluster contains at least one Conductor Live node and one Elemental Live node. If you want
  to produce MPTSes, a cluster contains at least one Conductor Live node, one Elemental Live node,
  and one Elemental Statmux node.

###### Topics

- [General information](cl3-general.md "cl3-general.md")
- [Software
  versions](cl3-software-versions.md "cl3-software-versions.md")
- [Licenses](cl3-software-licenses.md "cl3-software-licenses.md")
- [Centralized management](centralized-management.md "centralized-management.md")
- [Redundancy and failover](redundancy-and-failover.md "redundancy-and-failover.md")
