

# Early-access features and ephemeral clusters in Aurora DSQL

**Important**  
AWS provides early-access features as a Preview, and they're subject to change. For more information about Previews, please see the [Betas and Previews terms](https://aws.amazon.com/service-terms/).

With Aurora DSQL, you can try new functionality in two related ways:
+ **Early-access features** – You can turn on capabilities that aren't yet generally available for a specific cluster when you create it.
+ **Ephemeral clusters** – You can create a cluster with a lifetime of up to 7 days. After the lifetime expires, Aurora DSQL permanently deletes the cluster and all of its data.

Some early-access features require an ephemeral cluster. Data that you write to an ephemeral cluster lasts only for the cluster's lifetime.

**Warning**  
Aurora DSQL permanently deletes an ephemeral cluster and all of its data after its lifetime expires. You set the lifetime when you create the cluster, and you can't undo the deletion. Use ephemeral clusters only for non-production data.

## Early-access features
<a name="ephemeral-clusters-early-access-features"></a>

The following table lists the early-access features that you can select when you create a cluster in the AWS Management Console.


| Feature | Requires an ephemeral cluster | Description | 
| --- | --- | --- | 
| **Latest DSQL major version** | Yes | With this feature, you can choose a preview cluster version when you create the cluster. For more information, see [Trying a newer version on a new cluster](cluster-versions.md#cluster-versions-try-new). | 
| **Major version upgrades** | Yes | With this feature, you can perform in-place major version upgrades on the cluster. For the upgrade process, see [Upgrading cluster versions in Aurora DSQL](version-upgrade.md). | 

## How ephemeral clusters work
<a name="ephemeral-clusters-how-they-work"></a>

When you create an ephemeral cluster, you select its lifetime. Ephemeral clusters follow these rules:
+ **Lifetime** – When you create the cluster, you select a lifetime of up to 7 days. The lifetime starts when you create the cluster. You can't change the lifetime later, and you can't convert between ephemeral and non-ephemeral clusters.
+ **Early-access features** – You must select at least one early-access feature.
+ **Automatic deletion** – After the lifetime expires, Aurora DSQL deletes the cluster and all of its data. You can also delete an ephemeral cluster yourself at any time before its lifetime expires. Deletion protection only prevents you from deleting the cluster yourself. It doesn't affect the cluster's lifetime.
+ **Single-Region only** – Ephemeral clusters are single-Region clusters only.
+ **Data protection features** – Ephemeral clusters don't support data protection features such as backups.
+ **Billing and quotas** – Ephemeral clusters use standard Aurora DSQL pricing. Each ephemeral cluster counts toward your cluster quota until Aurora DSQL deletes it. For more information about billing and quotas, see [How billing works in Aurora DSQL](billing-metering.md) and [Cluster quotas and database limits in Amazon Aurora DSQL](CHAP_quotas.md).

## Creating an ephemeral cluster
<a name="ephemeral-clusters-create"></a>

Create an ephemeral cluster to try early-access features with non-production data. Before you begin, decide which early-access features to use and how long the cluster needs to exist.

**To create an ephemeral cluster**

1. Open the [Aurora DSQL console](https://console.aws.amazon.com/dsql).

1. Choose **Create cluster**.

1. To show all cluster settings, choose **Advanced configuration**.

1. Expand **Ephemeral clusters and early-access Previews**.

1. Under **Early-access features**, select one or more features.

1. For **Cluster lifetime**, select how long the cluster exists.

1. In the remaining sections, configure the cluster settings, and then choose **Create cluster**.

The cluster appears in the cluster list with the status **Creating**. Cluster creation might take a few minutes.

## Checking when the lifetime expires
<a name="ephemeral-clusters-view"></a>

The details page of an ephemeral cluster shows a banner with the date and time when the cluster's lifetime expires. After that time, Aurora DSQL permanently deletes the cluster.

To track when an ephemeral cluster's lifetime expires, use the date and time in this banner. CloudTrail records a `DeleteCluster` event only when you delete a cluster yourself.