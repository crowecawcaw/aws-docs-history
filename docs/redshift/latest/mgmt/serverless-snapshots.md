Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a snapshot

###### Note

No-backup tables aren't supported for RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot. To avoid snapshot costs for no-backup tables,
truncate them before taking a snapshot.

To create a snapshot, perform the steps in the following procedure.

###### To create a snapshot

1. On the Amazon Redshift Serverless console, choose **Data backup**.
2. Choose **Create snapshot**.
3. Choose a namespace to create a snapshot of.
4. Enter a snapshot identifier.
5. (Optional) Choose a retention period. If you choose **Custom
   value**, choose the number of days. The amount you choose must be
   between 1-3653 days, inclusive. The default is retain indefinitely.
6. Choose **Create**.

###### To create a snapshot from namespace configuration

1. On the Amazon Redshift Serverless console, choose **Namespace
   configuration**.
2. Choose the namespace to create a snapshot of. You can only create snapshots of
   namespaces that are associated with a workgroup and whose statuses are
   Available.
3. Choose the **Data backup** tab.
4. Choose **Create snapshot**.
5. Enter a snapshot identifier.
6. (Optional) Choose a retention period. If you choose **Custom
   value**, choose the number of days. The amount you choose must be
   between 1-3653 days, inclusive.
7. Choose **Create**.
