Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Upgrading the release version of a

cluster

You can upgrade the release maintenance version of a cluster that has a
**Release Status** value of **New release
available**. When you upgrade the maintenance version, you can choose to
upgrade immediately or upgrade in the next maintenance window.

###### Important

If you upgrade immediately, your cluster is offline until the upgrade
completes.

###### To upgrade a cluster to a new release version

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**.
3. Choose the cluster to upgrade.
4. For **Actions**, choose **Upgrade cluster
   version**. The **Upgrade cluster version** page
   appears.
5. Follow the instructions on the page.
6. Choose **Upgrade cluster version**.
