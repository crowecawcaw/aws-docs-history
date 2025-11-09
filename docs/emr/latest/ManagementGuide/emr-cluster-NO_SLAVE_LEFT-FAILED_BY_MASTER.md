# Amazon EMR cluster terminates with NO_SLAVE_LEFT and core nodes FAILED_BY_MASTER

Usually, this happens because termination protection is disabled, and all core nodes exceed disk storage capacity as specified by a maximum utilization threshold in the `yarn-site` configuration classification, which corresponds to the `yarn-site.xml` file. This value is 90% by default. When disk utilization for a core node exceeds the utilization threshold, the YARN NodeManager health service reports the node as `UNHEALTHY`. While it's in this state, Amazon EMR deny lists the node and does not allocate YARN containers to it. If the node remains unhealthy for 45 minutes, Amazon EMR marks the associated Amazon EC2 instance for termination as `FAILED_BY_MASTER`. When all Amazon EC2 instances associated with core nodes are marked for termination, the cluster terminates with the status `NO_SLAVE_LEFT` because there are no resources to execute jobs.

Exceeding disk utilization on one core node might lead to a chain reaction. If a single node exceeds the disk utilization threshold because of HDFS, other nodes are likely to be near the threshold as well. The first node exceeds the disk utilization threshold, so Amazon EMR deny lists it. This increases the burden of disk utilization for remaining nodes because they begin to replicate HDFS data among themselves that they lost on the deny-listed node. Each node subsequently goes `UNHEALTHY` in the same way, and the cluster eventually terminates.

## Best practices and recommendations

### Configure cluster hardware with adequate storage

When you create a cluster, make sure that there are enough core nodes and that each has an adequate instance store and EBS storage volumes for HDFS. For more information, see [Calculating the required HDFS
capacity of a cluster](emr-plan-instances-guidelines.md#emr-plan-instances-hdfs "emr-plan-instances-guidelines.md#emr-plan-instances-hdfs"). You can also add core instances to existing instance groups manually or by using auto-scaling. The new instances have the same storage configuration as other instances in the instance group. For more information, see [Use Amazon EMR cluster scaling to adjust
for changing workloads](emr-scale-on-demand.md "emr-scale-on-demand.md").

### Enable termination protection

Enable termination protection. This way, if a core node is deny listed, you can connect to the associated Amazon EC2 instance using SSH to troubleshoot and recover data. If you enable termination protection, be aware that Amazon EMR does not replace the Amazon EC2 instance with a new instance. For more information, see [Using termination protection to protect your Amazon EMR clusters from
accidental shut down](UsingEMR_TerminationProtection.md "UsingEMR_TerminationProtection.md").

### Create an alarm for the MRUnhealthyNodes CloudWatch metric

This metric reports the number of nodes reporting an `UNHEALTHY` status. It's equivalent to the YARN metric `mapred.resourcemanager.NoOfUnhealthyNodes`. You can set up a notification for this alarm to warn you of unhealthy nodes before the 45-minute timeout is reached. For more information, see [Monitoring Amazon EMR metrics with CloudWatch](UsingEMR_ViewingMetrics.md "UsingEMR_ViewingMetrics.md").

### Tweak settings using yarn-site

The settings below can be adjusted according to your application requirements. For example, you may want to increase the disk utilization threshold where a node reports `UNHEALTHY` by increasing the value of `yarn.nodemanager.disk-health-checker.max-disk-utilization-per-disk-percentage`.

You can set these values when you create a cluster using the `yarn-site` configuration classification. For more information see [Configuring applications](../ReleaseGuide/emr-configure-apps.md "../ReleaseGuide/emr-configure-apps.md") in the _Amazon EMR Release Guide_. You can also connect to the Amazon EC2 instances associated with core nodes using SSH, and then add the values in `/etc/hadoop/conf.empty/yarn-site.xml` using a text editor. After making the change, you must restart hadoop-yarn-nodemanager as shown below.

###### Important

When you restart the NodeManager service, active YARN containers are killed unless `yarn.nodemanager.recovery.enabled` is set to `true` using the `yarn-site` configuration classification when you create the cluster. You must also specify the directory in which to store container state using the `yarn.nodemanager.recovery.dir` property.

```
sudo /sbin/stop hadoop-yarn-nodemanager
sudo /sbin/start hadoop-yarn-nodemanager
```

For more information about current `yarn-site` properties and default values, see [YARN default settings](http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-common/yarn-default.xml "http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-common/yarn-default.xml") in Apache Hadoop documentation.

| Property                                                                        | Default value | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| yarn.nodemanager.disk-health-checker.interval-ms                                | 120000        | The frequency (in seconds) that the disk health checker runs.                                                                                                                                                                                                                                                                                                                        |
| yarn.nodemanager.disk-health-checker.min-healthy-disks                          | 0.25          | The minimum fraction of the number of disks that must be<br>healthy for NodeManager to launch new containers. This<br>corresponds to both yarn.nodemanager.local-dirs (by default,<br>`/mnt/yarn` in Amazon EMR) and<br>yarn.nodemanager.log-dirs (by default<br>`/var/log/hadoop-yarn/containers`, which is<br>symlinked to `mnt/var/log/hadoop-yarn/containers`<br>in Amazon EMR). |
| `yarn.nodemanager.disk-health-checker.max-disk-utilization-per-disk-percentage` | 90.0          | The maximum percentage of disk space utilization allowed after which a disk is marked as bad. Values can range from 0.0 to 100.0. If the value is greater than or equal to 100, the NodeManager checks for a full disk. This applies to `yarn-nodemanager.local-dirs` and `yarn.nodemanager.log-dirs`.                                                                               |
| `yarn.nodemanager.disk-health-checker.min-free-space-per-disk-mb`               | 0             | The minimum space that must be available on a disk for it to be used. This applies to `yarn-nodemanager.local-dirs` and `yarn.nodemanager.log-dirs`.                                                                                                                                                                                                                                 |
