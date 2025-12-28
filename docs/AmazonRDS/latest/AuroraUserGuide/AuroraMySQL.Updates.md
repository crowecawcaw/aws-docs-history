# Enabling automatic upgrades between minor Aurora MySQL versions

For an Amazon Aurora MySQL DB cluster, you can specify that Aurora upgrades the DB cluster
automatically to new minor versions. You do so by setting the
`AutoMinorVersionUpgrade` property (**Auto minor version upgrade**
in the AWS Management Console) of the DB cluster.

Automatic upgrades occur during the maintenance window. If the individual DB instances in the DB cluster have different
maintenance windows from the cluster maintenance window, then the cluster maintenance window takes precedence.

Automatic minor version upgrade doesn't apply to the following kinds of Aurora MySQL clusters:

- Clusters that are part of an Aurora global database
- Clusters that have cross-Region replicas
  The outage duration varies depending on workload, cluster size, the amount of binary log data, and if Aurora can use the
  zero-downtime patching (ZDP) feature. Aurora restarts the database cluster, so you might experience a short period of unavailability
  before resuming use of your cluster. In particular, the amount of binary log data affects recovery time. The DB instance processes
  the binary log data during recovery. Thus, a high volume of binary log data increases recovery time.

###### Note

Aurora only performs automatic upgrades if all DB instances in your DB cluster have the `AutoMinorVersionUpgrade` setting enabled.
For information on how to set it, and how it works when applied at the cluster and instance levels, see
[Automatic minor version upgrades for Aurora
DB clusters](USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU "USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU").

Then if an upgrade path exists for the DB cluster's instances to a minor DB engine version
that has `AutoUpgrade` set to true, the upgrade will take place. The
`AutoUpgrade` setting is dynamic, and is set by RDS.

Auto minor version upgrades are performed to the default minor version.

You can use a CLI command such as the following to check the status of the `AutoMinorVersionUpgrade` setting for all of
the DB instances in your Aurora MySQL clusters.

```
aws rds describe-db-instances \
  --query '*[].{DBClusterIdentifier:DBClusterIdentifier,DBInstanceIdentifier:DBInstanceIdentifier,AutoMinorVersionUpgrade:AutoMinorVersionUpgrade}'

```

That command produces output similar to the following:

```
[
  {
      "DBInstanceIdentifier": "db-t2-medium-instance",
      "DBClusterIdentifier": "cluster-57-2020-06-03-6411",
      "AutoMinorVersionUpgrade": true
  },
  {
      "DBInstanceIdentifier": "db-t2-small-original-size",
      "DBClusterIdentifier": "cluster-57-2020-06-03-6411",
      "AutoMinorVersionUpgrade": false
  },
  {
      "DBInstanceIdentifier": "instance-2020-05-01-2332",
      "DBClusterIdentifier": "cluster-57-2020-05-01-4615",
      "AutoMinorVersionUpgrade": true
  },
... output omitted ...

```

In this example, **Enable auto minor version upgrade** is turned off for the DB cluster
`cluster-57-2020-06-03-6411`, because it's turned off for one of the DB instances in the cluster.
