

# Release notes for Slurm versions in AWS PCS
<a name="slurm-versions_release-notes"></a>

This topic describes important changes for each Slurm version currently supported in AWS PCS. We recommend you review the changes between the old and new versions when you upgrade your cluster.

## Slurm 25.11
<a name="slurm-versions_release-notes_25.11"></a>

**Changes implemented in AWS PCS**
+ Scheduler audit logs are now delivered separately through the `PCS_SCHEDULER_AUDIT_LOGS` log type, simplifying troubleshooting and auditing with independent control over log delivery. For more information, see [Scheduler audit logs in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring_scheduler-audit-logs.html).
+ Expedited requeue is enabled by default. Jobs that fail due to node issues (such as insufficient capacity errors) can be requeued with the highest scheduling priority using `sbatch --requeue=expedite`. This is controlled by the `SchedulerParameters=enable_expedited_requeue` setting.
+ The `requeue_delay` parameter is available as a custom cluster setting with a default of 5 seconds. Previously, requeue delay was tied to credential expiration (70 seconds). Administrators can now configure this independently via `SchedulerParameters=requeue_delay=<seconds>`.
+ `HealthCheckNodeState` now supports the `START_ONLY` value, which runs the health check program only at node startup (slurmd start).
+ `CommunicationParameters=disable_http` is set by default to disable HTTP endpoints (metrics and health probes) introduced in Slurm 25.11. To re-enable these endpoints, set `CommunicationParameters=enable_http`. For more information, see [Slurm metrics in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-metrics.html).

**Known issues**
+ Slurm 25.11 validates `AllowQOS` and `DenyQOS` partition settings even when `AccountingStorageEnforce=QOS` is not set. If a QOS referenced in `AllowQOS` or `DenyQOS` doesn't exist in the Slurm accounting database, `slurmctld` exits with a fatal error. Ensure that all QOS values listed in partition `AllowQOS` and `DenyQOS` settings exist in the accounting database before upgrading to or restarting Slurm 25.11.
+ The `slurmd` log may show the error message `error: cannot create url_parser context for http_parser/libhttp_parser`. This is a known Slurm issue that occurs even when `CommunicationParameters=disable_http` is set. The error can be safely ignored and doesn't affect cluster operation.

For more information about Slurm 25.11, see the following publications:
+ SchedMD release announcement: [https://www.schedmd.com/slurm-version-25-11-0-is-now-available/](https://www.schedmd.com/slurm-version-25-11-0-is-now-available/)
+ SchedMD release notes: [https://github.com/SchedMD/slurm/blob/slurm-25.11/RELEASE\_NOTES.md](https://github.com/SchedMD/slurm/blob/slurm-25.11/RELEASE_NOTES.md)

## Slurm 25.05
<a name="slurm-versions_release-notes_25.05"></a>

**Changes implemented in AWS PCS**
+ The Slurm requeue\_on\_resume\_failure SchedulerParameter is now Enabled by default.
+ "stderr" was removed as an option for LogTimeFormat, as it was disabled in Slurm 25.05.
+ AWS PCS supports Multi-cluster sackd configuration: login node can access multiple clusters.

For more information about Slurm 25.05, see the following publications:
+ SchedMD release announcement: [https://www.schedmd.com/slurm-version-25-05-0-is-now-available/](https://www.schedmd.com/slurm-version-25-05-0-is-now-available/)
+ SchedMD release notes: [https://github.com/SchedMD/slurm/blob/slurm-25-05-0-1/RELEASE\_NOTES.md](https://github.com/SchedMD/slurm/blob/slurm-25-05-0-1/RELEASE_NOTES.md)

## Slurm 24.11
<a name="slurm-versions_release-notes_24.11"></a>

**Changes implemented in AWS PCS**
+ AWS PCS supports Slurm accounting. For more information, see [Slurm accounting in AWS PCS](slurm-accounting.md).

For more information about Slurm 24.11, see the following publications:
+ [SchedMD release announcement](https://www.schedmd.com/slurm-version-24-11-0-is-now-available/)
+ [SchedMD release notes](https://github.com/SchedMD/slurm/blob/slurm-24-11-0-1/RELEASE_NOTES)

## Slurm 24.05
<a name="slurm-versions_release-notes_24.05"></a>

**Changes implemented in AWS PCS**
+ The new Slurm Step Manager module is now enabled by default in AWS PCS. This module provides significant benefits by offloading step management from the central controller to compute nodes, substantially improving system concurrency in environments with heavy step usage. To support this configuration and better isolate `Prolog` and `Epilog` process execution, new prolog flags (`Contain`, `Alloc`) are enabled. 
+ Hierarchical communication from controller to compute nodes is enabled to optimize Slurm intra-node communication, which improves scalability and performance. Additionally, the routing configuration now uses partition node lists for communications from the controller, instead of the plugin's default routing algorithm, enhancing system resiliency. 
+ A new hash plugin `HashPlugin=hash/sha3` replaces the previous `hash/k12 plugin`. This is now enabled by default in AWS PCS clusters. 
+ Slurm controller logs now include enhanced auditing capabilities for all inbound remote procedure calls (RPC) to `slurmctld`. The logs include the source address, authenticated user, and RPC type before connection processing. 

For more information about Slurm 24.05, see the following publications:
+ [SchedMD release announcement](https://www.schedmd.com/slurm-version-24-05-0-is-now-available/)
+ [SchedMD release notes](https://github.com/SchedMD/slurm/blob/slurm-24-05-0-1/RELEASE_NOTES)

## Slurm 23.11
<a name="slurm-versions_release-notes_23.11"></a>

**Slurm settings you can change in AWS PCS**
+  The `SuspendTime` defaults to `60`. Use the AWS PCS `scaleDownIdleTimeInSeconds` configuration parameter to set it. For more information, see the [`scaleDownIdleTimeInSeconds`](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ClusterSlurmConfiguration.html#PCS-Type-ClusterSlurmConfiguration-scaleDownIdleTimeInSeconds) parameter of the `ClusterSlurmConfiguration` data type in the *AWS PCS API Reference*. 
+  The `MaxJobCount` and `MaxArraySize` is based on the size you choose for the cluster. For more information, see the [`size`](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html#PCS-CreateCluster-request-size) parameter of the `CreateCluster` API action in the *AWS PCS API Reference*.
+  The `SelectTypeParameters` Slurm setting defaults to `CR_CPU`. You can provide it as a value for `slurmCustomSettings` to set it when you create a cluster. For more information, see the [`slurmCustomSettings`](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ClusterSlurmConfigurationRequest.html#PCS-Type-ClusterSlurmConfigurationRequest-slurmCustomSettings) parameter of the `CreateCluster` API action and [SlurmCustomSetting](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SlurmCustomSetting.html) in the *AWS PCS API Reference*.
+ You can set `Prolog` and `Epilog` at the cluster level. You can provide it as a value for `slurmCustomSettings` to set it when you create a cluster. For more information, see [`CreateCluster`](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html) and [SlurmCustomSetting](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SlurmCustomSetting.html) in the *AWS PCS API Reference*.
+ You can set `Weight` and `RealMemory` at the compute node group level. You can provide it as a value for `slurmCustomSettings` to set it when you create a compute node group. For more information, see [`CreateComputeNodeGroup`](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateComputeNodeGroup.html) and [SlurmCustomSetting](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SlurmCustomSetting.html) in the *AWS PCS API Reference*.