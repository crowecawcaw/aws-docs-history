# Managing an Amazon Aurora global database

You perform most management
operations on the individual clusters that make up an Aurora global database. When you choose
**Group related resources** on the **Databases** page in
the console, you see the primary cluster and secondary clusters grouped under the associated
global database. To find the AWS Regions where a global database's DB clusters are running,
its Aurora DB engine and version, and its identifier, use its
**Configuration** tab.

The cross-Region database failover processes are available to Aurora global databases only, not
for a single Aurora DB cluster. To learn more, see
[Using switchover or failover in Amazon Aurora Global Database](aurora-global-database-disaster-recovery.md "aurora-global-database-disaster-recovery.md").

To recover an Aurora global database from an unplanned outage in its primary
Region, see [Recovering an Amazon Aurora global database from an unplanned outage](aurora-global-database-disaster-recovery.md#aurora-global-database-failover "aurora-global-database-disaster-recovery.md#aurora-global-database-failover").

###### Topics

- [Modifying an Amazon Aurora global database](aurora-global-database-modifying.md "aurora-global-database-modifying.md")
- [Modifying parameters for an Aurora global database](aurora-global-database-modifying.md "aurora-global-database-modifying.md")
- [Removing a cluster from an Amazon Aurora global database](aurora-global-database-detaching.md "aurora-global-database-detaching.md")
- [Deleting an Amazon Aurora global database](aurora-global-database-deleting.md "aurora-global-database-deleting.md")
- [Tagging Amazon Aurora Global Database resources](aurora-global-database-tagging.md "aurora-global-database-tagging.md")
