# Step D: Upgrade node X

Now that node X is not controlling the cluster, you can upgrade it.

1. Set boot mode on the node to UEFI. See [Backing up data](migrate-topic-lifeboat.md "migrate-topic-lifeboat.md").
2. Perform a kickstart to upgrade the operating system to RHEL 9. See [Installing RHEL 9](migrate-topic-install-rhel.md "migrate-topic-install-rhel.md").
3. Install Conductor Live version 3.26.1 on the node. See [Installing Conductor Live on nodes](migrate-topic-install-cl3.md "migrate-topic-install-cl3.md").
4. In [Step C: Split the cluster](migrate-split-c-split.md "migrate-split-c-split.md"), you created a backup of the
   database on node X. You can now restore the backup onto the node. See [Restoring the database](migrate-topic-restore-database.md "migrate-topic-restore-database.md").

As a result of restoring the database, this Conductor node is now configured as it
was before you removed it from the cluster. Specifically, it has the data
relating to the channels, MPTSes, node assignments for channels and MPTSes, user
setup, redundancy groups, and cluster members.

This means that when you add worker nodes back into the cluster (in the next
section), there is less worker node configuration required compared to when you
set up the cluster for the very first time. 5. If you moved custom files to a safe location as part of your preparation, you
can now copy these files back to their original location.
