Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Renaming a cluster

You can rename a cluster if you want the cluster to use a different name. Because the
endpoint to your cluster includes the cluster name (also referred to as the
_cluster identifier_), the endpoint changes to use the new name
after the rename finishes. For example, if you have a cluster named
`examplecluster` and rename it to `newcluster`, the endpoint
changes to use the `newcluster` identifier. Any applications that connect to
the cluster must be updated with the new endpoint.

You may rename a cluster if you want to change the cluster your applications connect
to without having to change the endpoint in those applications. In this case, you must
first rename the original cluster and then change the second cluster to reuse the name
of the original cluster before the rename. Doing this is necessary because the cluster
identifier must be unique within your account and region, so the original cluster and
second cluster cannot have the same name. You might do this if you restore a cluster
from a snapshot and don't want to change the connection properties of any dependent
applications.

###### Note

If you delete the original cluster, you are responsible for deleting any unwanted
cluster snapshots.

When you rename a cluster, the cluster status changes to `renaming` until
the process finishes. The old DNS name that was used by the cluster is immediately
deleted, although it could remain cached for a few minutes. The new DNS name for the
renamed cluster becomes effective within about 10 minutes. The renamed cluster is not
available until the new name becomes effective. The cluster will be rebooted and any
existing connections to the cluster will be dropped. After this completes, the endpoint
will change to use the new name. For this reason, you should stop queries from running
before you start the rename and restart them after the rename finishes.

Cluster snapshots are retained, and all snapshots associated with a cluster remain
associated with that cluster after it is renamed. For example, suppose that you have a
cluster that serves your production database and the cluster has several snapshots. If
you rename the cluster and then replace it in the production environment with a
snapshot, the cluster that you renamed still has those existing snapshots associated
with it.

Amazon CloudWatch alarms and Amazon Simple Notification Service (Amazon SNS) event notifications are associated with the
name of the cluster. If you rename the cluster, you must update these accordingly. You
can update the CloudWatch alarms in the CloudWatch console, and you can update the Amazon SNS event
notifications in the Amazon Redshift console on the **Events** pane. The load
and query data for the cluster continues to display data from before the rename and
after the rename. However, performance data is reset after the rename process finishes.

For more information, see [Modifying a cluster](modify-cluster.md "modify-cluster.md").
