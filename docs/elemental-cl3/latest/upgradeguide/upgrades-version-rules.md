# Rules for software versions

There are rules about working with different software versions on the nodes in a
AWS Elemental Conductor Live cluster.

## Compatible versions

**Worker nodes**

All the worker nodes (Elemental Live and Elemental Statmux) in the cluster should have the same major
version installed. It's only permissible for there to be a mix of versions when you are
in the middle of upgrading the worker nodes.

If you have both Elemental Live and Elemental Statmux nodes in the cluster, consult the release notes to
decide whether to upgrade the minor versions. Often, there are no fixed issues or new
features in a minor version of Elemental Statmux. Therefore, it's acceptable to run, to perform a
minor version upgrade of Elemental Live and to not upgrade Elemental Statmux.

**Conductor Live nodes**

If you have a redundant cluster, both the Conductor Live nodes must have the same version
number, down to the minor version. For example, both must run version
3.25.5.

**Worker nodes compared to Conductor Live nodes**

The Conductor Live nodes can be running different versions from the worker nodes. These rules
apply:

- The Conductor Live nodes must be running the lower version.
- The worker nodes can be a maximum of two major versions of the Conductor Live nodes.
  For example, 2.25 and 3.25.
- The Conductor Live node can control worker nodes that are running a higher version,
  but you won't be able to use features that are new in the higher version. This
  rule exists because the Conductor Live node has no code that can control the new
  feature.

Typically, you introduce worker nodes with a higher software version if you obtain a
new worker node, and the node is installed with a newer software version. You want to
recruit the new worker node, but you are not yet prepare to upgrade the Conductor Live nodes.
AWS Elemental supports this configuration because we recognize that upgrading the Conductor Live nodes
is a major undertaking.

However, we strongly recommend that you align all the software versions, down to the
patch level, as soon as possible.

Note that if you experience a problem with interaction in two nodes running different
software versions, AWS Elemental Support will probably request that you set up all the nodes on
the same patch version.
