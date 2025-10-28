Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Copying backups to another AWS Region

You can configure Amazon Redshift Serverless to automatically copy snapshots and recovery points to
another AWS Region. When you create a snapshot in the _source_
AWS Region, it's copied to a _destination_ Region. You can
configure your namespace so that it only copies snapshots and recovery points to one
destination AWS Region at a time. For a list of AWS Regions where Amazon Redshift Serverless is
available, see the endpoints listed for [Redshift Serverless API](../../../general/latest/gr/redshift-service.md "../../../general/latest/gr/redshift-service.md") in
the _Amazon Web Services General Reference_.

When you configure copying backups, you can also specify a retention period of how
long Amazon Redshift Serverless should keep the copied snapshot. You can't change the retention periods
of recovery points, which must be 1 day. The retention periods of snapshots in the
destination Region is separate from the retention period of the snapshot in the source
Region. By default, the retention period is to keep the snapshot indefinitely. If you
choose **Custom value** choose the number of days. This amount you
choose must be between 1-3653 days, inclusive.

To change the destination Region to copy snapshots to, first disable copying backups,
and then specify the new destination Region when you re-enable copying.

Once a snapshot or recovery point is copied to a destination Region, you can use it to
restore data to the Region.

By default, your data is encrypted with a key that AWS manages for you. To use a
different key, choose the key that you want to use when configuring backup copying in
the source AWS Region, and Amazon Redshift Serverless automatically creates a grant, which enables
snapshot encryption in the destination AWS Region.

To copy backups to another Region, make sure that you have the following IAM
permissions:

```
redshift-serverless:CreateSnapshotCopyConfiguration
redshift-serverless:UpdateSnapshotCopyConfiguration
redshift-serverless:ListSnapshotCopyConfigurations
redshift-serverless:DeleteSnapshotCopyConfiguration
```

If you're using your own KMS key to encrypt your backups, you also need the following
permissions:

```
kms:CreateGrant
kms:DescribeKey
```

To configure copying your snapshots or recovery points to another
AWS Region

1. On the Amazon Redshift Serverless console, choose the namespace for which you want to configure
   copying snapshots or recovery points.
2. Choose the **Actions**, **Configure cross-Region
   backup**.
3. Choose the destination AWS Region to copy the snapshot to.
4. (Optional) Choose how long to retain the snapshot. If you choose **Custom value** choose the number of days The amount you choose must
   be between 1-3653 days, inclusive. The default is to retain indefinitely.
5. (Optional) Choose a different AWS KMS key to use to encrypt for encryption in
   the destination Region.
6. Choose **Save configuration**.
