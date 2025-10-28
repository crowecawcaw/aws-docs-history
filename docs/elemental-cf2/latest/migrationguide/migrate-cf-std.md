# Performing a standard cluster

migration on an
AWS Elemental Conductor File cluster

This procedure describes how to take the nodes in a AWS Elemental Conductor File cluster from a version below
2.18 and migrate them to version 2.18 or higher. The nodes in the cluster might be the
following:

- A primary Conductor node and, optionally, a secondary Conductor node.
- AWS Elemental Server nodes.

###### Important

We strongly recommend that you test the entire migration procedure in your lab. This
strategy lets you test the migration process itself, and test the entire workflow on the
new software.

In this procedure, we show how to upgrade the cluster from Conductor File version 2.17.5 (worker
nodes version 2.17.5) to version 2.17.5). Modify the commands you enter to match your
versions.

###### Important

You must upgrade all the nodes in the cluster to a 2.18 version. You can't, for
example, set up the cluster so that Conductor File is running 2.17 and the workers (or some of
the workers) are running 2.18.

###### Topics

- [Plan maintenance
  windows for
  migrating an AWS Elemental Conductor File cluster](migrate-std-plan-maintenance.md "migrate-std-plan-maintenance.md")
- [Step A: Get ready to migrate an AWS Elemental Conductor File
  cluster](migrate-std-get-ready.md "migrate-std-get-ready.md")
- [Step B: Prepare each
  AWS Elemental Conductor File
  node
  for migration](migrate-std-prepare-node.md "migrate-std-prepare-node.md")
- [Step C: Tear down
  an
  AWS Elemental Conductor File cluster](migrate-std-decluster.md "migrate-std-decluster.md")
- [Step D: Create backups](migrate-std-backup.md "migrate-std-backup.md")
- [Step E: Upgrade nodes](migrate-server-218-install-software-cf.md "migrate-server-218-install-software-cf.md")
- [Step F: Rebuild the cluster](migrate-std-rebuild-cluster.md "migrate-std-rebuild-cluster.md")
