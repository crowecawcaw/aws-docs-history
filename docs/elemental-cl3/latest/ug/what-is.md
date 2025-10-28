# About the Conductor Live solution

AWS Elemental Conductor Live lets you create and manage channels on AWS Elemental Live and/or MPTSes on AWS Elemental Statmux.

Each of the three products — AWS Elemental Conductor Live, AWS Elemental Live and AWS Elemental Statmux — runs on its own node.
Conductor Live is a _management node_. Elemental Live and Elemental Statmux node are each
_worker nodes_. And all the nodes are organized in a _cluster._

A cluster contains at least one Conductor Live node and one Elemental Live node. If you want
to produce MPTSes, a cluster contains at least one Conductor Live node, one Elemental Live node,
and one Elemental Statmux node.
