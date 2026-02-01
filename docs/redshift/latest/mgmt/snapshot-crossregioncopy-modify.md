Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Modifying the retention period for

cross-Region snapshot copy

After you configure cross-Region snapshot copy, you might want to change the settings.
You can easily change the retention period by selecting a new number of days and saving the
changes.

###### Warning

You can't modify the destination AWS Region after cross-Region snapshot copy
is configured.

If you want to copy snapshots to a different AWS Region, first disable cross-Region
snapshot copy. Then re-enable it with a new destination AWS Region and retention
period. Any copied automated snapshots are deleted after you disable cross-Region
snapshot copy. Thus, you should determine if there are any that you want to keep and
copy them to manual snapshots before disabling cross-Region snapshot copy.

###### To modify a cross-Region snapshot

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose the
   cluster that you want to modify snapshots for.
3. For **Actions**, choose **Configure cross-region
   snapshot** to display the properties of the snapshot.
4. Enter the revised properties of the snapshot definition, then choose
   **Save**.
