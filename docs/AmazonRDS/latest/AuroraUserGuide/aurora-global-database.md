# Creating an Amazon Aurora global database from an Aurora or Amazon RDS snapshot

You can restore a snapshot of an Aurora DB cluster or from an Amazon RDS DB instance to use as the starting point for your Aurora global database.
You restore the snapshot and create a new Aurora provisioned DB cluster at the same time. You then add another AWS Region to
the restored DB cluster, thus turning it into an Aurora global database. Any Aurora DB cluster that you create using a snapshot in this way becomes the
primary cluster of your Aurora global database.

The snapshot that you use can be from a `provisioned` or from a `serverless` Aurora DB cluster.

During the restore process, choose the same DB engine type as the snapshot. For example,
suppose that you want to restore a snapshot that was made from an Aurora Serverless DB cluster
running Aurora PostgreSQL. In this case, you create an Aurora PostgreSQL DB cluster using that same
Aurora DB engine and version.

The restored DB cluster assumes the role of primary cluster for the Aurora global database when you add
an AWS Region to it. All data contained in this primary cluster is replicated to any secondary clusters
that you add to your Aurora global database.

![Screenshot showing the restore snapshot page for an Aurora global database.](images/aurora-global-databases-restore-snapshot-01.png)
