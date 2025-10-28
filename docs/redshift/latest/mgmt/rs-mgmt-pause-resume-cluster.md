Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Pausing and resuming a cluster

If you have a cluster that only needs to be available at specific times, you can pause
the cluster and later resume it. While the cluster is paused, on-demand billing is
suspended. Only the cluster's storage incurs charges. For more information about
pricing, see the [Amazon Redshift pricing
page](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

When you pause a cluster, Amazon Redshift creates a snapshot, begins terminating queries, and
puts the cluster in a pausing state. If you delete a paused cluster without requesting a
final snapshot, then you can't restore the cluster. You can't cancel or roll back a
pause or resume operation after it's initiated.

You can pause and resume a cluster on the Amazon Redshift console, with the AWS CLI, or with Amazon Redshift
API operations.

You can schedule actions to pause and resume a cluster. When you use the new Amazon Redshift
console to create a recurring schedule to pause and resume, then two scheduled actions
are created for the date range that you choose. The scheduled action names are suffixed
with `-pause` and `-resume`. The total length of the name must fit
within the maximum size of a scheduled action name.

You can't pause the following types of clusters:

- EC2-Classic clusters.
- Clusters that are not active, for example, a cluster that is currently
  modifying.
- Hardware security module (HSM) clusters.
- Clusters that have automated snapshots turned off.
  When deciding to pause a cluster, consider the following:

- Connections or queries to the cluster aren't available.
- You can't see query monitoring information of a paused cluster on the Amazon Redshift
  console.
- You can't modify a paused cluster. Any scheduled actions on the cluster aren't
  done. These include creating snapshots, resizing clusters, and cluster
  maintenance operations.
- Hardware metrics aren't created. Update your CloudWatch alarms if you have alarms
  set on missing metrics.
- You can't copy the latest automated snapshots of a paused cluster to manual
  snapshots.
- While a cluster is pausing, it can't be resumed until the pause operation
  is complete.
- When you pause a cluster, billing is suspended. However, the pause operation
  typically completes within 15 minutes, depending upon the size of the cluster.
- Audit logs are archived and not restored on resume.
- After a cluster is paused, traces and logs might not be available for
  troubleshooting problems that occurred before the pause.
- If you're managing your admin credentials using AWS Secrets Manager and pause your
  cluster, your cluster's secret won't be deleted and you'll continue to be billed
  for the secret. For more information on managing your Redshift admin password
  with AWS Secrets Manager, see [Managing Amazon Redshift admin passwords
  using AWS Secrets Manager](redshift-secrets-manager-integration.md "redshift-secrets-manager-integration.md").
- No-backup tables on the cluster are restored on resume for RA3 instance types.
  They aren't restored on resume for DC2 instance types. For more information about
  no-backup tables, see [Excluding tables from snapshots](working-with-snapshots.md#snapshots-no-backup-tables "working-with-snapshots.md#snapshots-no-backup-tables").
  When you resume a cluster, consider the following:

- The cluster version of the resumed cluster is updated to the maintenance
  version based on the maintenance window of the cluster.
- If you delete the subnet associated with a paused cluster, you might have an
  incompatible network. In this case, restore your cluster from the latest
  snapshot.
- If you delete an Elastic IP address while the cluster is paused, then a new
  Elastic IP address is requested.
- If Amazon Redshift can't resume the cluster with its previous elastic network
  interface, then Amazon Redshift tries to allocate a new one.
- When you resume a cluster, your node IP addresses might change. You might need
  to update your VPC settings to support these new IP addresses for features like
  COPY from Secure Shell (SSH) or COPY from Amazon EMR.
- If you try to resume a cluster that isn't paused, the resume operation
  returns an error. If the resume operation is part of a scheduled action, modify
  or delete the scheduled action to prevent future errors.
- Depending upon the size of the cluster, it can take several minutes to resume
  a cluster before queries can be processed. In addition, query performance can be
  impacted for some period of time while the cluster is being re-hydrated after
  resume completes.
