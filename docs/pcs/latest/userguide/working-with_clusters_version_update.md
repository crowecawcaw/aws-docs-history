

# Updating the scheduler version of a cluster in AWS PCS
<a name="working-with_clusters_version_update"></a>

AWS PCS lets you update the scheduler version on an existing cluster without rebuilding your infrastructure. Version updates move the cluster controller to a newer Slurm major version, giving you access to new features, performance improvements, and security patches. Newer versions also have a longer support lifetime before reaching end of life.

## Overview
<a name="version_update-cluster-overview"></a>

A scheduler version update involves three operations:

1. **Prepare target AMIs** — Build or identify AMIs that include the target Slurm version and the latest AWS PCS agent.

1. **Update the cluster** (`UpdateCluster`) — Moves the controller to the target Slurm major version.

1. **Update compute node groups** (`UpdateComputeNodeGroup`) — Point each compute node group at a new AMI so that new nodes use the target version. For more information, see [Updating an AWS PCS compute node group](working-with_cng_update.md).

There are two paths you can follow. Choose an option based on whether you can tolerate job interruption.

Regardless of which option you choose, before the process starts, all the nodes in the cluster must run the same version "A" and at the end of the process all nodes must run the same version "B". Option 2 works regardless of your cluster configuration.


|  | Option 1: Rolling update | Option 2: Full-fleet maintenance stop | 
| --- | --- | --- | 
| Running jobs | Does not require job termination | All running jobs terminated | 
| Minimum cluster controller version | 24.05 | No restriction | 
| Compute fleet after controller update | Mixed versions temporarily; drain steps required. We recommend minimizing the amount of time during which mixed versions are used in a cluster. | All nodes start fresh on target version | 

**Note**  
Before starting, ensure all compute nodes are on the latest patch of Slurm version A and on the latest AWS PCS agent.

## Limitations
<a name="version_update-cluster-limitations"></a>
+ If your cluster uses [SPANK plugins](spank.md) (plugstack configuration), AWS PCS doesn't support Option 1. A rolling update might cause a plugstack configuration version mismatch and plugin failures.
+ If your cluster uses [Slurm CLI Filter Plugins](slurm-cli-filter-plugins.md), AWS PCS doesn't support Option 1. During a rolling update, compute nodes that run an earlier Slurm version might not be able to parse the updated cluster configuration and might fail to start.

## Version compatibility
<a name="version_update-cluster-compatibility"></a>

The following table shows the supported target versions to update to, depending on the current cluster version. It is always recommended to upgrade to the latest allowed version (shown in bold).

Cluster and all compute nodes must always run the same Slurm version before initiating an update.


| Current cluster version | Compatible target versions | 
| --- | --- | 
| 25.11 | N/A | 
| 25.05 | 25.11 | 
| 24.11 (EOL) | 25.11, 25.05 | 
| 24.05 (EOL) | 25.11, 25.05, 24.11 | 
| 23.11 (EOL) | (via Option 2 only) 25.05, 24.11, 24.05 | 

For more information about supported versions and end-of-life dates, see [Slurm versions in AWS PCS](slurm-versions.md).

You cannot skip beyond three major versions in a single update. If your target version is more than three major versions ahead of your current version, perform the update in multiple consecutive steps. For a multi-step example, see [Example: Updating across multiple versions](working-with_clusters_version_update_procedure.md#version_update-procedure-multi-hop).

## Impact on running jobs
<a name="version_update-cluster-job-impact"></a>

During the update, the Slurm controller is briefly unavailable. This has the following effects:
+ **Running jobs** — For Option 1 (rolling update), jobs that are already running on compute nodes continue to execute. The compute nodes do not require the controller to be available for active job execution. For Option 2 (full-fleet maintenance stop), all running jobs are terminated when the fleet is scaled down.
+ **New job submissions** — You cannot submit new jobs or run scheduler commands while the controller is unavailable.
+ **Scaling** — Automatic scaling is paused during the update. No new instances are launched and no instances are terminated for scale-down until the update completes.
+ **Accounting data** — If accounting is enabled, accounting data is preserved across the update. Job records stored in the accounting database persist after the version change.
+ **Slurm REST API** — If the Slurm REST API is enabled on the cluster, it is automatically updated to the new scheduler version as part of the `UpdateCluster` operation. The REST API endpoint is unavailable during the update and resumes when the cluster returns to `ACTIVE` state. For more information, see [Slurm REST API in AWS PCS](slurm-rest-api.md).

## Combining version updates with configuration changes
<a name="version_update-cluster-combined-changes"></a>

You can combine a version update with other configuration changes in a single `UpdateCluster` request. For example, you can update the scheduler version and enable accounting in the same operation.

**Note**  
Do not add Slurm settings specific to the target version while the fleet still contains nodes on the previous version. Configuration is distributed to all nodes; the old `slurmd` may not recognize new parameters.

**Topics**
+ [Overview](#version_update-cluster-overview)
+ [Limitations](#version_update-cluster-limitations)
+ [Version compatibility](#version_update-cluster-compatibility)
+ [Impact on running jobs](#version_update-cluster-job-impact)
+ [Combining version updates with configuration changes](#version_update-cluster-combined-changes)
+ [Update the scheduler version of an AWS PCS cluster](working-with_clusters_version_update_procedure.md)
+ [Troubleshooting AWS PCS cluster version updates](working-with_clusters_version_update_troubleshooting.md)