# Performing a standard cluster migration on an AWS Elemental Conductor Live

cluster

This procedure describes how to take the nodes in a AWS Elemental Conductor Live cluster from a version
below x.26.0 and migrate them to version x.26.1 or higher. The nodes in the cluster might be
the following:

- A primary Conductor node and, optionally, a secondary Conductor node.
- AWS Elemental Live nodes.
- AWS Elemental Statmux nodes.

###### Important

We strongly recommend that you test the entire migration procedure in your lab. This
strategy lets you test the migration process itself, and test the entire workflow on the
new software.

In this _standard_ procedure, you take all nodes offline
for a while and tear down the cluster. Therefore there is a period when no channels or
MPTSes are running on any of the worker nodes. If you need to decrease the downtime, you
might want to perform the [split Conductor
migration](migrate-cl-split-cluster.md "migrate-cl-split-cluster.md") instead.

In this procedure, we show how to upgrade the cluster from Conductor Live version 3.25.5 (worker
nodes version 2.25.5) to version 3.26.x (2.26.x). Modify the commands
you enter to match your versions.

###### Important

You must upgrade all the nodes in the cluster to an x.26 version. You can't, for
example, set up the cluster so that Conductor Live is running 3.25.x and the workers (or some of
the workers) are running 2.26.x.

###### Topics

- [Plan maintenance windows for migrating an
  AWS Elemental Conductor Live cluster](migrate-std-plan-maintenance.md "migrate-std-plan-maintenance.md")
- [Step A: Get ready to migrate an AWS Elemental Conductor Live
  cluster](migrate-std-get-ready.md "migrate-std-get-ready.md")
- [Step B: Prepare each AWS Elemental Conductor Live node for
  migration](migrate-std-prepare-node.md "migrate-std-prepare-node.md")
- [Step C: Tear down the cluster](migrate-std-decluster.md "migrate-std-decluster.md")
- [Step D: Create backups](migrate-std-backup.md "migrate-std-backup.md")
- [Step E: Upgrade nodes](migrate-std-upgrade-nodes.md "migrate-std-upgrade-nodes.md")
- [Step F: Rebuild the cluster](migrate-std-rebuild-cluster.md "migrate-std-rebuild-cluster.md")
