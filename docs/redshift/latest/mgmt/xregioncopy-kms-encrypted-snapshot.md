Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring cross-Region snapshot copy

for an AWS KMS–encrypted cluster

When you launch an Amazon Redshift cluster,
you can configure a snapshot copy grant for a root key in your account in the destination AWS Region.
If you don't configure a grant, snapshots in the destination region are encrypted with a default AWS-owned key.
By doing this, you enable Amazon Redshift to perform encryption operations in the destination
AWS Region.

The following procedure describes the process of enabling cross-Region snapshot copy for
an AWS KMS-encrypted cluster. For more information about encryption in Amazon Redshift and snapshot
copy grants, see [Copying AWS KMS–encrypted
snapshots to another AWS Region](working-with-db-encryption.md#configure-snapshot-copy-grant "working-with-db-encryption.md#configure-snapshot-copy-grant").

###### To configure a cross-Region snapshot for an AWS KMS–encrypted cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose the
   cluster that you want to move snapshots for.
3. For **Actions**, choose **Configure cross-region
   snapshot**.

The Configure cross-Region dialog box appears. 4. For **Copy snapshots**, choose **Yes**. 5. In **Destination AWS Region**, choose the AWS Region to which
to copy snapshots. 6. In **Automated snapshot retention period (days)**, choose the
number of days for which you want automated snapshots to be retained in the
destination AWS Region before they are deleted. 7. In **Manual snapshot retention period**, choose the value that
represents the number of days for which you want manual snapshots to be retained in
the destination AWS Region before they are deleted. If you choose **Custom
value**, the retention period must be between 1 to 3653 days. 8. Choose **Save**.
