Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring cross-Region snapshot copy

for a nonencrypted cluster

You can configure Amazon Redshift to copy snapshots for a cluster to another AWS Region. To
configure cross-Region snapshot copy, you need to enable this copy feature for each cluster
and configure where to copy snapshots and how long to keep copied automated or manual
snapshots in the destination AWS Region. When cross-Region copy is enabled for a cluster,
all new manual and automated snapshots are copied to the specified AWS Region. Copied
snapshot names are prefixed with `copy:`.

###### To configure a cross-Region snapshot

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
