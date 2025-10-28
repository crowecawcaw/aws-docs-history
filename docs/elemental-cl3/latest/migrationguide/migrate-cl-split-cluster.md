# Performing a split cluster migration

This procedure describes how to take the nodes in a AWS Elemental Conductor Live cluster from a version
below x.26.0 and migrate them to version x.26.1 or higher. The nodes in the cluster might be
the following:

- Both a primary Conductor node and a secondary Conductor node.
- AWS Elemental Live nodes.
- AWS Elemental Statmux nodes.

###### Important

We strongly recommend that you test the entire migration procedure in your lab. This
strategy lets you test the migration process itself, and test the entire workflow on the
new software.

In this procedure, we show how to upgrade the cluster from Conductor Live version 3.25.5 (worker
nodes version 2.25.5) to version 3.26.x (2.26.x). Modify the commands
you enter to match your versions.

###### Important

You must upgrade all the nodes in the cluster to an x.26 version. You can't, for
example, set up the cluster so that Conductor Live is running 3.25.x and the workers (or some of
the workers) are running 2.26.x.

**How a split cluster migration works**

In this procedure, which you typically perform over several maintenance windows, you
remove the primary Conductor node from the cluster. The secondary Conductor node takes control of this
cluster (the original cluster). You upgrade the primary Conductor to the new operating system and
Conductor Live software. This node is then ready to control a new cluster (the new cluster).

You then remove the worker nodes from the original cluster, upgrade them, add them to the
new cluster, and restart their channels. Eventually, the secondary Conductor has no worker nodes.
At that point, you upgrade that node and add it to the new cluster, then enable HA. You now
have the cluster running again, with all the nodes running the new version of the AWS Elemental
software on the new operating system.

If this procedure seems unnecessarily complicated and you don't mind losing all processing
for a few hours, then you might want to perform the [standard
migration](migrate-cl-std.md "migrate-cl-std.md") instead.

###### Topics

- [Plan maintenance windows](migrate-split-c-plan-maintenance.md "migrate-split-c-plan-maintenance.md")
- [Step A: Get ready](migrate-split-c-get-ready.md "migrate-split-c-get-ready.md")
- [Step B: Prepare each node](migrate-split-c-prepare-node.md "migrate-split-c-prepare-node.md")
- [Step C: Split the cluster](migrate-split-c-split.md "migrate-split-c-split.md")
- [Step D: Upgrade node X](migrate-split-c-upgrade-primary.md "migrate-split-c-upgrade-primary.md")
- [Step E: Upgrade the worker
  nodes](migrate-split-c-upgrade-w-nodes.md "migrate-split-c-upgrade-w-nodes.md")
- [Step F: Upgrade node Y](migrate-split-c-upgrade-secondary.md "migrate-split-c-upgrade-secondary.md")
- [Step G: Add node Y to cluster](migrate-split-c-add-secondary.md "migrate-split-c-add-secondary.md")
