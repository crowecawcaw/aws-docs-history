# Copying a DB cluster snapshot with the AWS Management Console

Use the procedures in this topic to copy a DB cluster snapshot. If your source database engine is Aurora,
then your snapshot is a DB cluster snapshot.

For each AWS account, you can copy up to five DB cluster snapshots at a time from one AWS Region
to another. Copying both encrypted and unencrypted DB cluster snapshots is supported. If
you copy a DB cluster snapshot to another AWS Region, you create a manual DB cluster
snapshot that is retained in that AWS Region. Copying a DB cluster snapshot out of the
source AWS Region incurs Amazon RDS data transfer charges.

For more information about data transfer pricing, see
[Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

After the DB cluster snapshot copy has been created in the new AWS Region, the DB cluster
snapshot copy behaves the same as all other DB cluster snapshots in that AWS Region.

This procedure works for copying encrypted or unencrypted DB cluster snapshots, in the same
AWS Region or across Regions.

To cancel a copy operation once it is in progress, delete the target DB cluster snapshot
while that DB cluster snapshot is in **copying** status.

Before copying a DB cluster snapshot, review the [Limitations](aurora-copy-snapshot.md#aurora-copy-snapshot.Limitations "aurora-copy-snapshot.md#aurora-copy-snapshot.Limitations") and [Considerations for snapshot copying](aurora-copy-snapshot.md#aurora-copy-snapshot.Considerations "aurora-copy-snapshot.md#aurora-copy-snapshot.Considerations").

###### To copy a DB cluster snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Select the DB cluster snapshot you want to copy.
4. Choose **Actions**, and then choose **Copy snapshot**.

![DB cluster snapshot copy interface with source and destination configuration options.](images/action-copy-db-cluster-snapshot.png) 5. (Optional) To copy the DB cluster snapshot to a different AWS Region, choose that AWS Region for
**Destination Region**. 6. Enter the name of the DB cluster snapshot copy in **New DB Snapshot Identifier**. 7. To copy tags and values from the snapshot to the copy of the snapshot, choose **Copy Tags**. 8. Choose **Copy Snapshot**.
