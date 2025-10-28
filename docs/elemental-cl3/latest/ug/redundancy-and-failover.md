# Redundancy and failover

Running Elemental Live events and Elemental Statmux MPTSes in Conductor Live lets you implement several
resiliency features. These features help reduce outages in your
workflows.

To clarify the terms:

- _Resiliency_ refers to the ability to
  continue when errors occur.
- _Redundancy_ refers to duplication of
  hardware or software components to protect against single points of
  failure. Therefore, redundancy is one way to achieve resiliency.
  Conductor Live offers resiliency solutions in all areas of the workflow:

- Node redundancy for Conductor Live nodes, Elemental Live nodes, and Elemental Statmux nodes. This
  redundancy protects against failure of an entire node.

Node redundancy is the foundation for some resiliency options within
the worker nodes. For example, within Elemental Live, there are some resiliency
options that only work with specific types of redundancy. Keep this fact in
mind when planning node redundancy.

When you first deploy your Conductor Live cluster, you should plan redundancy
for the nodes in the cluster.

After your initial deployment, you should review your node redundancy
design when you add more nodes or when your workflows change
dramatically.

For more information about planning node redundancy, see [Setup: Planning resiliency in a cluster](cl3-resiliency.md "cl3-resiliency.md").

- Resiliency features in different types of workflows:

      + Encoding workflows: workflows that involve only Elemental Live.
      + MPTS workflows: workflows that involve Elemental Live and Elemental Statmux.

  As part of the design procedure for a workflow, decide which
  resiliency features you want to implement. An encoding workflow and in an
  MPTS workflow have slightly different resiliency options.

For more information about resiliency features, see [Resiliency features
in Elemental Statmux](worker-nodes-other-resiliency.md "worker-nodes-other-resiliency.md").
