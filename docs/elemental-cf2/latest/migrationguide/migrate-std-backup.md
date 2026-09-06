

# Step D: Create backups
<a name="migrate-std-backup"></a>

Create a backup of the data on every node — the primary Conductor node, the secondary Conductor node, and all the workers.

**Important**  
After you make a backup of the first node in the cluster , don't make any changes to any worker node or Conductor node or to cluster until you've finished this migration process. Don't change the setup of the Conductor node.

To create database backups, see [Backing up data](migrate-topic-lifeboat.md). 