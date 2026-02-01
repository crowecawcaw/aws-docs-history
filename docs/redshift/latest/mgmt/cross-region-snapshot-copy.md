Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Copying a snapshot to another AWS

Region

You can configure Amazon Redshift to automatically copy snapshots (automated or manual) for a
cluster to another AWS Region. When a snapshot is created in the cluster's primary
AWS Region, it's copied to a secondary AWS Region. The two AWS Regions are known
respectively as the _source AWS Region_ and _destination
AWS Region_. If you store a copy of your snapshots in another AWS Region,
you can restore your cluster from recent data if anything affects the primary AWS Region.
You can configure your cluster to copy snapshots to only one destination AWS Region at a
time. For a list of Amazon Redshift Regions, see [Regions and
endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_.

When you enable Amazon Redshift to automatically copy snapshots to another AWS Region, you
specify the destination AWS Region to copy the snapshots to. For automated snapshots, you
can also specify the retention period to keep them in the destination AWS Region. After
an automated snapshot is copied to the destination AWS Region and it reaches the
retention time period there, it's deleted from the destination AWS Region. Doing
this keeps your snapshot usage low. To keep the automated snapshots for a shorter or longer
time in the destination AWS Region, change this retention period.

The retention period that you set for automated snapshots that are copied to the
destination AWS Region is separate from the retention period for automated snapshots in
the source AWS Region. The default retention period for copied snapshots is seven days.
That seven-day period applies only to automated snapshots. In both the source and
destination AWS Regions, manual snapshots are deleted at the end of the snapshot
retention period or when you manually delete them.

You can disable automatic snapshot copy for a cluster at any time. When you disable this
feature, snapshots are no longer copied from the source AWS Region to the destination
AWS Region. Any automated snapshots copied to the destination AWS Region are deleted as
they reach the retention period limit, unless you create manual snapshot copies of them.
These manual snapshots, and any manual snapshots that were copied from the destination
AWS Region, are kept in the destination AWS Region until you manually delete
them.

To change the destination AWS Region that you copy snapshots to, first disable the
automatic copy feature. Then re-enable it, specifying the new destination AWS
Region.

After
a snapshot is copied to the destination AWS Region, it becomes active and available for
restoration purposes.

To copy snapshots for AWS KMS–encrypted clusters to another AWS Region, create a
grant for Amazon Redshift to use a customer managed key in the destination AWS Region. Then choose that
grant when you enable copying of snapshots in the source AWS Region. For more information
about configuring snapshot copy grants, see [Copying AWS KMS–encrypted
snapshots to another AWS Region](working-with-db-encryption.md#configure-snapshot-copy-grant "working-with-db-encryption.md#configure-snapshot-copy-grant").
