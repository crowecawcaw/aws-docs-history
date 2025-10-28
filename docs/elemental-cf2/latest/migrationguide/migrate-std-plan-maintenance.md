# Plan maintenance

windows for
migrating an AWS Elemental Conductor File cluster

You should plan to perform the cluster migration in several phases:

**First phase**

You can perform the tasks in [Step A: Get ready to migrate an AWS Elemental Conductor File
cluster](migrate-std-get-ready.md "migrate-std-get-ready.md") outside of a
maintenance window.

**Second phase**

Perform the following tasks in one or more maintenance windows. The number of windows
depends on the number of nodes you can complete in one maintenance window.

- [Step B: Prepare each
  AWS Elemental Conductor File
  node
  for migration](migrate-std-prepare-node.md "migrate-std-prepare-node.md")
  **Third phase**

Perform all the following tasks on every node, all in one maintenance window.

- [Step C: Tear down
  an
  AWS Elemental Conductor File cluster](migrate-std-decluster.md "migrate-std-decluster.md")
- [Step D: Create backups](migrate-std-backup.md "migrate-std-backup.md")
- [Step F: Rebuild the cluster](migrate-std-rebuild-cluster.md "migrate-std-rebuild-cluster.md")
  These steps upgrade all the nodes at one time. You must perform the upgrade in this
  way because you can't have a cluster where some nodes are on the previous version of the
  AWS Elemental software and some are on the new version.
