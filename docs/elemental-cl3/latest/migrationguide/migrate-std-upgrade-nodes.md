# Step E: Upgrade nodes

## Upgrade the worker nodes

Perform these steps on each worker node in the cluster, after you've removed all
the nodes from the cluster.

Before you start, make sure that you have performed the tasks in [Step B: Prepare each AWS Elemental Conductor Live node for
migration](migrate-std-prepare-node.md "migrate-std-prepare-node.md").

1. Create a backup of the database on the node. See [Backing up data](migrate-topic-lifeboat.md "migrate-topic-lifeboat.md").
2. Set boot mode on the node to UEFI. See [Switching boot mode to UEFI](migrate-topic-uefi.md "migrate-topic-uefi.md").
3. Perform a kickstart to upgrade the operating system to RHEL 9. See [Installing RHEL 9](migrate-topic-install-rhel.md "migrate-topic-install-rhel.md").
4. Install Elemental Live version 2.26.x on the node. See [Installing Elemental Live on a worker node](migrate-topic-install-worker.md "migrate-topic-install-worker.md").
5. Restore the database onto the node. See [Restoring the database](migrate-topic-restore-database.md "migrate-topic-restore-database.md").
6. Install new licenses.

If a specific node handles SMPTE 2110 inputs or outputs, you should have
obtained a new license that includes the SMPTE 2110 add-on package. (The
procedure for obtaining a new license is described in the essential notes in
the [current Release Notes](../../../elemental-live.md "../../../elemental-live.md").) To deploy the license, see the section about configuring
licenses in the [AWS Elemental Live Configuration Guide](../../../elemental-live/latest/configguide.md "../../../elemental-live/latest/configguide.md").

Each worker node now has the new operating system and software installed, and it
restored to its former database, including most of its configuration data.

## Upgrade the Conductor nodes

Perform these steps on both Conductor nodes.

1. Set boot mode on the node to UEFI. See [Switching boot mode to UEFI](migrate-topic-uefi.md "migrate-topic-uefi.md").
2. Perform a kickstart to upgrade the operating system to RHEL 9. See [Backing up data](migrate-topic-lifeboat.md "migrate-topic-lifeboat.md").
3. Install Conductor Live version 3.26.1 on the node. See [Installing Conductor Live on nodes](migrate-topic-install-cl3.md "migrate-topic-install-cl3.md").
4. Restore the database onto each node. See [Restoring the database](migrate-topic-restore-database.md "migrate-topic-restore-database.md").

The primary Conductor node now has all the configuration information about the
cluster. This means that when you add worker nodes back into the cluster,
all the information about redundancy groups, for example, is present on the
primary Conductor node. You don't have to set it up again. 5. If you moved custom files to a safe location as part of your preparation,
you can now copy these files back to their original location.
