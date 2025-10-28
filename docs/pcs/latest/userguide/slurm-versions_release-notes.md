# Release notes for Slurm versions in

AWS PCS

This topic describes important changes for each Slurm version currently supported in
AWS PCS. We recommend you review the changes between the old and new versions when you upgrade
your cluster.

###### Changes implemented in AWS PCS

- The Slurm requeue_on_resume_failure SchedulerParameter is now Enabled by default.
- "stderr" was removed as an option for LogTimeFormat, as it was disabled in Slurm 25.05.
- AWS PCS supports Multi-cluster sackd configuration: login node can access multiple clusters.
  For more information about Slurm 25.05, see the following publications:

- SchedMD release announcement: [https://www.schedmd.com/slurm-version-25-05-0-is-now-available/](https://www.schedmd.com/slurm-version-25-05-0-is-now-available/ "https://www.schedmd.com/slurm-version-25-05-0-is-now-available/")
- SchedMD release notes: [https://github.com/SchedMD/slurm/blob/slurm-25-05-0-1/RELEASE_NOTES.md](https://github.com/SchedMD/slurm/blob/slurm-25-05-0-1/RELEASE_NOTES.md "https://github.com/SchedMD/slurm/blob/slurm-25-05-0-1/RELEASE_NOTES.md")

###### Changes implemented in AWS PCS

- AWS PCS supports Slurm accounting. For more information, see
  [Slurm accounting in AWS PCS](slurm-accounting.md "slurm-accounting.md").
  For more information about Slurm 24.11, see the following
  publications:

- [SchedMD release announcement](https://www.schedmd.com/slurm-version-24-11-0-is-now-available/ "https://www.schedmd.com/slurm-version-24-11-0-is-now-available/")
- [SchedMD release notes](https://github.com/SchedMD/slurm/blob/slurm-24-11-0-1/RELEASE_NOTES "https://github.com/SchedMD/slurm/blob/slurm-24-11-0-1/RELEASE_NOTES")

###### Changes implemented in AWS PCS

- The new Slurm Step Manager module is now enabled by default in AWS PCS. This
  module provides significant benefits by offloading step management from the
  central controller to compute nodes, substantially improving system
  concurrency in environments with heavy step usage. To support this
  configuration and better isolate `Prolog` and `Epilog`
  process execution, new prolog flags (`Contain`,
  `Alloc`) are enabled.
- Hierarchical communication from controller to compute nodes is enabled to
  optimize Slurm intra-node communication, which improves scalability and
  performance. Additionally, the routing configuration now uses partition node
  lists for communications from the controller, instead of the plugin's
  default routing algorithm, enhancing system resiliency.
- A new hash plugin `HashPlugin=hash/sha3` replaces the previous
  `hash/k12 plugin`. This is now enabled by default in AWS PCS
  clusters.
- Slurm controller logs now include enhanced auditing capabilities for all
  inbound remote procedure calls (RPC) to `slurmctld`. The logs
  include the source address, authenticated user, and RPC type before
  connection processing.
  For more information about Slurm 24.05, see the following
  publications:

- [SchedMD release announcement](https://www.schedmd.com/slurm-version-24-05-0-is-now-available/ "https://www.schedmd.com/slurm-version-24-05-0-is-now-available/")
- [SchedMD release notes](https://github.com/SchedMD/slurm/blob/slurm-24-05-0-1/RELEASE_NOTES "https://github.com/SchedMD/slurm/blob/slurm-24-05-0-1/RELEASE_NOTES")

###### Slurm settings you can change in AWS PCS

- The `SuspendTime` defaults to `60`. Use the AWS PCS
  `scaleDownIdleTimeInSeconds` configuration parameter to set
  it. For more information, see the [`scaleDownIdleTimeInSeconds`](../APIReference/API_ClusterSlurmConfiguration.md#PCS-Type-ClusterSlurmConfiguration-scaleDownIdleTimeInSeconds "../APIReference/API_ClusterSlurmConfiguration.md#PCS-Type-ClusterSlurmConfiguration-scaleDownIdleTimeInSeconds") parameter of the
  `ClusterSlurmConfiguration` data type in the _AWS PCS
  API Reference_.
- The `MaxJobCount` and `MaxArraySize` is based on
  the size you choose for the cluster. For more information, see the [`size`](../APIReference/API_CreateCluster.md#PCS-CreateCluster-request-size "../APIReference/API_CreateCluster.md#PCS-CreateCluster-request-size") parameter of the
  `CreateCluster` API action in the _AWS PCS API
  Reference_.
- The `SelectTypeParameters` Slurm setting defaults to
  `CR_CPU`. You can provide it as a value for
  `slurmCustomSettings` to set it when you create a cluster.
  For more information, see the [`slurmCustomSettings`](../APIReference/API_ClusterSlurmConfigurationRequest.md#PCS-Type-ClusterSlurmConfigurationRequest-slurmCustomSettings "../APIReference/API_ClusterSlurmConfigurationRequest.md#PCS-Type-ClusterSlurmConfigurationRequest-slurmCustomSettings") parameter of the
  `CreateCluster` API action and [SlurmCustomSetting](../APIReference/API_SlurmCustomSetting.md "../APIReference/API_SlurmCustomSetting.md") in the _AWS PCS API
  Reference_.
- You can set `Prolog` and `Epilog` at the cluster
  level. You can provide it as a value for `slurmCustomSettings` to
  set it when you create a cluster. For more information, see [`CreateCluster`](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") and [SlurmCustomSetting](../APIReference/API_SlurmCustomSetting.md "../APIReference/API_SlurmCustomSetting.md") in the _AWS PCS API
  Reference_.
- You can set `Weight` and `RealMemory` at the compute
  node group level. You can provide it as a value for
  `slurmCustomSettings` to set it when you create a compute
  node group. For more information, see [`CreateComputeNodeGroup`](../APIReference/API_CreateComputeNodeGroup.md "../APIReference/API_CreateComputeNodeGroup.md") and [SlurmCustomSetting](../APIReference/API_SlurmCustomSetting.md "../APIReference/API_SlurmCustomSetting.md") in the _AWS PCS API
  Reference_.
