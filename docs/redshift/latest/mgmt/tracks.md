Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Tracks for Amazon Redshift provisioned

clusters and serverless workgroups

When Amazon Redshift releases a new version,
it updates the version of your Amazon Redshift data warehouse (serverless workgroup or provisioned cluster). You can control whether
your data warehouse is updated to the most
recent release or to the previous certified release.

The serverless workgroup or provisioned cluster's track determines which released version is applied during a version update.
Amazon Redshift updates provisioned clusters during the specified maintenance window, and usually updates serverless workgroups during idle periods.
For details of when Redshift Serverless updates workgroups, see [Updating serverless workgroups](#tracks-serverless-updating "#tracks-serverless-updating").

When Amazon Redshift releases
a new version, that version is
assigned to the _current_ track, and the previous
version is assigned to the _trailing_ track. To set
the track for your data warehouse, specify one of the following values:

- **Current** – With the **Current** track,
  you get the most up-to-date certified release version with the latest features, security updates, and
  performance enhancements.
- **Trailing** – With the **Trailing** track,
  you will be on the previous certified release.
  For example, suppose that your serverless workgroup is currently running version 1.0.2762 and
  Amazon Redshift releases Redshift Serverless version 1.0.3072. If your track value is
  **Current**, your workgroup is updated to version 1.0.3072 (the
  latest release). If you set the
  track value to **Trailing**, your workgroup is
  updated when the next trailing track version is released.

With the trailing track feature, you have the option to run a subset of Amazon Redshift data warehouses in the trailing track.
This allows for 1-6 weeks of testing and integration validation on data warehouses set to the Current track before applying the release
to data warehouses on the Trailing track. By default, Amazon Redshift creates all clusters and workgroups on the Current track to take advantage
of the most up-to-date, certified release. However, using the Amazon Redshift trailing track in your production
environment, and the current track in your testing and development environment, gives you additional diligence and time to evaluate the latest release.

The Trailing track ensures maximum stability,
making it ideal for mission-critical workloads in production environments.

###### Note

The trailing track version may be the same as the current track version for short periods of time. This happens
when the current track hasn't advanced to the next version. Normally, the current track version is ahead of the trailing track version.

## Switching between tracks

Changing tracks for an Amazon Redshift resource is generally a one-time decision. You should
exercise caution in changing tracks. For information
about which features are in which data warehouse versions, see [Cluster versions for Amazon Redshift](cluster-versions.md "cluster-versions.md").

If you change the track from
**Trailing** to **Current**, we will update
the data warehouse to the **Current** track release version. If you change the data warehouse's track
to **Trailing**, we will update your data warehouse as follows:

- For serverless workgroups, we update your data warehouse's version during an idle period. For more details about how
  Redshift Serverless updates your workgroup's version, see [Updating serverless workgroups](#tracks-serverless-updating "#tracks-serverless-updating").
- For provisioned clusters, we won't update your data warehouse until there is a
  new release after the **Current** track release version.

## Tracks and restore

For serverless workgroups, a snapshot inherits the target Amazon Redshift data warehouse's track. For example, if you create
a snapshot for a workgroup set to Trailing track, and apply that snapshot to a workgroup set to Current track, the workgroup
will have a track setting of Current.

For provisioned clusters, a snapshot inherits the source Amazon Redshift data warehouse's track. If you change the
source data warehouse's track after you take a snapshot, the snapshot and
the source data warehouse are on different tracks. When you restore from the snapshot, the
new data warehouse will be on the track that was inherited from the snapshot source.
You can change the track after the restore operation completes.

Resizing a data warehouse doesn't affect its track.

## Updating serverless workgroups

When a new version beomes available for a workgroup's chosen track, Amazon Redshift Serverless
typically applies the update during an idle period as long as there is no pending track
update request. If the workgroup doesn't experience an idle period within 14 days, Redshift Serverless
forces the version update.

Redshift Serverless only updates your workgroup to the next higher version. Redshift Serverless doesn't skip
intermediate versions or downgrade workgroups, even if the version for the selected
workgroup's track is less than the workgroup's current version. Your workgroup will not
receive any major version upgrades until and unless the `Trailing` track
catches up.

For example, suppose the `Current` track is version 186, and the
`Trailing` track version is 185. If you have a workgroup that has a
`Track` value of `Current`, whose version is 186, if you
change the `Track` value to `Trailing`, Redshift Serverless won't downgrade the
workgroup's version to 185. In this scenario, Redshift Serverless keeps the workgroup on version 186
until the `Trailing` track version is equal to or higher than 186.

If a track change is pending, Redshift Serverless doesn't update the workgroup to the next major
version in the exisiting track until it applies the track change. After the track change
is complete, Redshift Serverless evaluates the conditions for updating the workgroup to the
appropriate version under the new track.

For example, if your workgroup is set to the `Current` track, and the
current track is 186, and you change your workgroup to the `Trailing` track,
Redshift Serverless won't update the workgroup until after it applies the track change, and after the
`Trailing` version is updated to a version equal to or higher than 186.

###### Note

Any existing operation on a workgroup, such as restoring from a snapshot, changing the KMS key, or resizing, only happens on the
existing track. Redshift Serverless does not use the pending track for serverless operations.

If you have a pending track switch request, you can cancel the request by setting the `track` parameter
back to its original value using
[UpdateWorkgroup](../../../redshift-serverless/latest/APIReference/API_UpdateWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_UpdateWorkgroup.md").

## Managing versions

A track is a series of releases. You can decide if your Amazon Redshift data warehouse is on
the **Current** track or the **Trailing** track. If you put your data warehouse on the **Current** track, it will always be upgraded to the most recent
release version. If you put your resource on the
**Trailing** track, it will always run the
release version that was released immediately before the most recently released
version.

For provisioned clusters, the **Release status** column in the Amazon Redshift console list of
Amazon Redshift data warehouses indicates whether one of your resources is available for upgrade.

## Determining the workgroup or cluster

version

You can determine the Amazon Redshift serverless workgroup version or provisioned cluster version engine with the Amazon Redshift
console.

Sign in to the AWS Management Console and open the Amazon Redshift console at
[https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").

Serverless workgroups For serverless workgroups, on the navigation menu,
choose **Workgroups**, then choose
the workgroup name from the list to open its details. The details of the
workgroup are displayed.

Provisioned clusters For provisioned clusters, on the navigation menu,
choose **Clusters**, then choose
the cluster name from the list to open its details.

The details of the
cluster are displayed, which can include **Cluster performance**, **Query monitoring**,
**Databases**, **Datashares**,
**Schedules**, **Maintenance**, and **Properties** tabs.
Choose the **Maintenance** tab for more details.

In the **Maintenance** section, find **Current
cluster version**.

###### Note

For provisioned clusters, the console displays the version information in one field, but it's two
parameters in the Amazon Redshift API. These parameters are `ClusterVersion` and
`ClusterRevisionNumber`. For more information, see [Cluster](../APIReference/API_Cluster.md "../APIReference/API_Cluster.md") in the
_Amazon Redshift API Reference_.
