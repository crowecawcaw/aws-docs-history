

# Troubleshooting AWS PCS cluster version updates
<a name="working-with_clusters_version_update_troubleshooting"></a>

This topic helps you identify and resolve common problems that can occur when updating the scheduler version on a cluster.
+ [Compute nodes fail to connect after update](#update-troubleshooting-nodes-fail)
+ [Update request rejected with ValidationException](#update-troubleshooting-validation-error)
+ [Cluster remains in UPDATING state](#update-troubleshooting-stuck-updating)
+ [Cluster enters UPDATE\_FAILED state after update](#update-troubleshooting-update-failed)
+ [Compute nodes fail to start due to configuration parsing errors](#update-troubleshooting-config-parse)
+ [Cluster unavailable after update due to invalid QoS configuration](#update-troubleshooting-qos-bootloop)

## Compute nodes fail to connect after update
<a name="update-troubleshooting-nodes-fail"></a>

### Common cause
<a name="update-troubleshooting-nodes-fail-cause"></a>

After updating the cluster, newly launched compute nodes fail to register with the controller. The nodes start but never appear in `sinfo` output, and the compute node group may cycle through instances repeatedly. This occurs when the compute node group's AMI contains a scheduler version that falls outside the compatibility window of the new controller version.

For example, if you update a cluster from 24.11 to 25.11 but the compute node group still uses an AMI with Slurm 23.11, new instances cannot connect because 23.11 is outside the compatibility window of 25.11.

### How to diagnose
<a name="update-troubleshooting-nodes-fail-diagnosis"></a>

You can confirm this issue by checking logs in two places:

**Scheduler logs**

If you have scheduler logging enabled, check the scheduler logs in CloudWatch Logs for errors similar to the following:

```
error: unpack_header: protocol_version 10240 not supported
error: slurm_unpack_received_msg: [{{ip-10-0-1-23}}] Incompatible versions of client and server code
```

These errors indicate that a compute node with an incompatible scheduler version is trying to connect to the controller. For information about setting up scheduler logging, see [Scheduler logs in AWS PCS](monitoring_scheduler-logs.md).

**Compute node instance logs**

Retrieve the instance console output or connect via Systems Manager and check the bootstrap log for errors similar to the following:

```
error: _fetch_child: failed to fetch remote configs: Incompatible versions of client and server
error: _establish_configuration: failed to load configs
error: slurmd initialization failed
```

For more information about retrieving instance logs, see [Retrieve instance logs](troubleshooting-compute-node-bootstrap.md#troubleshooting-compute-node-bootstrap-retrieve-logs).

### Resolution
<a name="update-troubleshooting-nodes-fail-resolution"></a>

Update the compute node group to use an AMI that contains a scheduler version within the compatibility window of your new cluster version:

```
aws pcs update-compute-node-group \
--cluster-identifier {{my-cluster}} \
--compute-node-group-identifier {{my-cng}} \
--ami-id {{ami-0123456789abcdef0}}
```

To determine which scheduler versions are compatible with your cluster, see [Version compatibility](working-with_clusters_version_update.md#version_update-cluster-compatibility).

For information about building custom AMIs with the correct scheduler version, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md).

## Update request rejected with ValidationException
<a name="update-troubleshooting-validation-error"></a>

### Common cause
<a name="update-troubleshooting-validation-error-cause"></a>

The `UpdateCluster` request returns immediately with a `ValidationException` error indicating the update is not supported. This occurs when:
+ The target version is outside the [compatibility window](https://slurm.schedmd.com/upgrades.html#compatibility_window) of the current version.
+ The target version is designated as End of Life (EOL) and is no longer a valid update target.
+ The target version is older than or equal to the current version (downgrades are not supported).

### Resolution
<a name="update-troubleshooting-validation-error-resolution"></a>

If the target version is outside the compatibility window, perform the update in multiple steps. Each step must target a supported version within the compatibility window. For example, to go from 23.11 to 25.11, first update to 25.05, wait for the cluster to return to `ACTIVE`, then update to 25.11.

If the target version is EOL, choose a newer supported version instead. For information about supported versions, see [Slurm versions in AWS PCS](slurm-versions.md).

## Cluster remains in UPDATING state
<a name="update-troubleshooting-stuck-updating"></a>

### Common cause
<a name="update-troubleshooting-stuck-updating-cause"></a>

The cluster stays in `UPDATING` state for longer than expected (more than 20 minutes). This can occur due to transient internal issues during the update process.

### Resolution
<a name="update-troubleshooting-stuck-updating-resolution"></a>

AWS PCS automatically recovers clusters that are stuck in `UPDATING` state. If the cluster does not return to `ACTIVE` or `UPDATE_FAILED` within 30 minutes, contact AWS Support for assistance.

## Cluster enters UPDATE\_FAILED state after update
<a name="update-troubleshooting-update-failed"></a>

### Common cause
<a name="update-troubleshooting-update-failed-cause"></a>

The cluster transitions to `UPDATE_FAILED` state during the update. This can occur when transient service errors prevent the update from completing successfully.

### Resolution
<a name="update-troubleshooting-update-failed-resolution"></a>

Retry the update by submitting the same `UpdateCluster` request again. Clusters in `UPDATE_FAILED` state accept new update requests. If the update continues to fail, contact AWS Support.

## Compute nodes fail to start due to configuration parsing errors
<a name="update-troubleshooting-config-parse"></a>

### Common cause
<a name="update-troubleshooting-config-parse-cause"></a>

After updating the cluster, compute nodes fail to start and never appear in `sinfo` output. The compute node instance logs show errors similar to the following:

```
error: _parse_next_key: Parsing error at unrecognized key: {{HashPlugin}}
error: Invalid DebugFlag: {{AuditRPCs}}
fatal: Unable to process configuration file
```

This occurs when compute nodes running scheduler version 23.11 receive configuration from a newer cluster version. Scheduler versions after 23.11 introduced new configuration directives that 23.11 cannot parse. Unlike other versions within the [compatibility window](https://slurm.schedmd.com/upgrades.html#compatibility_window), 23.11 compute nodes cannot connect to a newer cluster because they fatally error on unrecognized configuration keys.

This issue can also occur if your custom AMI uses a AWS PCS agent version older than v1.4.0. Older agent versions do not support automatic version fallback for the compute node daemon.

### Resolution
<a name="update-troubleshooting-config-parse-resolution"></a>

Rebuild your custom AMI with the following requirements:
+ Scheduler version 24.05 or later
+ AWS PCS agent version 1.4.0 or later

Then update the compute node group to use the new AMI:

```
aws pcs update-compute-node-group \
--cluster-identifier {{my-cluster}} \
--compute-node-group-identifier {{my-cng}} \
--ami-id {{ami-0123456789abcdef0}}
```

For information about building custom AMIs, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md). For information about AWS PCS agent versions, see [AWS PCS agent versions](pcs-agent-versions.md).

## Cluster unavailable after update due to invalid QoS configuration
<a name="update-troubleshooting-qos-bootloop"></a>

### Common cause
<a name="update-troubleshooting-qos-bootloop-cause"></a>

After updating to version 25.11, the cluster enters `UPDATE_FAILED` state or the scheduler becomes unavailable. You cannot submit jobs or run scheduler commands. The scheduler logs show errors similar to the following:

```
error: Invalid Allow/DenyQOS value: {{low}}
fatal: Partition {{my-queue}} has an invalid DenyQOS ({{low}}), please check your configuration
```

This occurs when a queue (partition) references a QoS name through `AllowQOS`, `DenyQOS`, or `QOS` settings that does not exist in the Slurm accounting database. Slurm 25.11 introduced stricter validation of QoS references at scheduler startup. Earlier versions allowed references to non-existent QoS names without error.

### Resolution
<a name="update-troubleshooting-qos-bootloop-resolution"></a>

Before updating to version 25.11, verify that all QoS names referenced in your queue configurations exist in the accounting database. Connect to a login node and run the following command to check if a QoS exists:

```
sacctmgr show qos where name={{low}} format=name
```

If the QoS does not exist, create it before attempting the update:

```
sacctmgr add qos {{low}}
```

Alternatively, remove the QoS reference from your queue configuration by updating the queue's Slurm custom settings to remove the `AllowQOS`, `DenyQOS`, or `QOS` parameter before updating the cluster.