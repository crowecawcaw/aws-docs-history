

# Trying to update a cluster
<a name="troubleshooting-fc-v3-update-cluster"></a>

The following section provides possible troubleshooting solutions to issues that might happen while you're trying to update a cluster.

## `pcluster update-cluster` command fails to run locally
<a name="update-cluster-failure-cli-v3"></a>

Check the `~/.parallelcluster/pcluster-cli.log` in your local file system for failure details.

## The cluster update timed out
<a name="update-cluster-failure-timeout-v3"></a>

This could be an issue related to `cfn-hup` not running. If the `cfn-hup` demon is terminated by an external cause, it's not restarted automatically. If `cfn-hup` isn't running, during a cluster update, the CloudFormation stack starts the update process as expected, but the update procedure isn't activated on the head node and the stack deployment eventually times out. For more information, see [Troubleshooting a cluster update timeout when `cfn-hup` isn't running](troubleshooting-v3-cluster-update-timeout.md) to troubleshoot and recover from the issue.

## `clusterStatus` is `UPDATE_FAILED`
<a name="update-cluster-failure-v3"></a>

### Root causing
<a name="update-cluster-failure-v3-root-causing"></a>

To identify the root cause of the failure, the starting point is to look at cluster stack events and `/var/log/chef-client.log` in the head node.

A possible cause is that at least one cluster node did not apply the update. You can retrieve the list of nodes that failed to update in `/var/log/chef-client.log` in the head node by looking for `Check cluster readiness` in the log.

Check to see if your issue is mentioned in [GitHub Known Issues](https://github.com/aws/aws-parallelcluster/wiki) at AWS ParallelCluster on GitHub.

### Preventing
<a name="update-cluster-failure-v3-preventing"></a>

A cluster update can fail if at least one node in the cluster did not successfully apply the update. To reduce the risk of cluster update failure, we recommend terminating broken nodes before initiating the update. An example of nodes that could be broken are compute nodes stuck in `COMPLETING` state for longer than the expected epilog duration. To detect those nodes, you can run the following command, adapting the `threshold` value to your needs (the value must be greater than the maximum duration expected for your epilogs). 

```
$ scontrol show nodes --json | jq -r --argjson threshold 60 '
  .nodes[] | select(.state | index("COMPLETING")) |
  select((now - .last_busy.number) > $threshold) |
  .name
'
```

### Recovering
<a name="update-cluster-failure-v3-recovering"></a>

If the update failed, the rollback is the mechanism expected to recover the state of the cluster.

 If the rollback failed, the cluster state is not deterministic. In this case, it may be that `clustermgtd` was stopped to prevent the amplification of failures. We recommend starting it by running the following command on the head node. Adapt the Python version to the one shipped with your AWS ParallelCluster version: 

```
$ /opt/parallelcluster/pyenv/versions/{{3.12.11}}/envs/cookbook_virtualenv/bin/supervisorctl start clustermgtd
```

### `clusterStatus` is `UPDATE_FAILED` and `cloudFormationStackStatus` is `UPDATE_ROLLBACK_FAILED`
<a name="update-cluster-failure-rollback-failed-v3"></a>

 When `pcluster describe-cluster` reports that `clusterStatus` is `UPDATE_FAILED` and `cloudFormationStackStatus` is `UPDATE_ROLLBACK_FAILED`, both the cluster update and the subsequent rollback failed. In this state the cluster stack cannot accept any further update and requires manual intervention to be unblocked. 

To unblock the cluster stack, complete the following steps:

1. Fix the root cause of the failure.

1. Force the continuation of the rollback.

   ```
   $ aws cloudformation continue-update-rollback --region {{REGION}} --stack-name {{CLUSTER_STACK_NAME}}
   ```

1. Wait for the stack to reach the `UPDATE_ROLLBACK_COMPLETE` status.

1. Retry the original update with the `pcluster update-cluster` command.

## The cluster stack appears stuck in `UPDATE_IN_PROGRESS` or `UPDATE_ROLLBACK_IN_PROGRESS`
<a name="update-cluster-stuck-in-progress-v3"></a>

 The cluster stack could be stuck in `UPDATE_IN_PROGRESS` or `UPDATE_ROLLBACK_IN_PROGRESS` for 1 hour at most, if the login nodes Auto Scaling Group is failing to stabilize due to bootstrap failures in the login nodes. 

 To verify whether you are in this situation due to the login nodes Auto Scaling Group, you need to do the following checks: In the main stack, the only resource that is in `UPDATE_IN_PROGRESS` is the login nodes nested stack. In the login nodes nested stack, the only resource that is stuck in `UPDATE_IN_PROGRESS` is the login nodes Auto Scaling Group. 

 If you are in this scenario, you can cancel the update so that you do not need to wait 1 hour for the update to complete. 

```
$ aws cloudformation cancel-update-stack --region {{REGION}} --stack-name {{CLUSTER_STACK_NAME}}
```

 Canceling the update triggers the rollback. You cannot reduce the 1 hour timeout on the rollback, so in the worst case scenario you need to wait for the rollback to reach its final state. 

 If the rollback succeeds, you can immediately retry your original cluster update once you have fixed the root cause of the failure. Otherwise, see [`clusterStatus` is `UPDATE_FAILED` and `cloudFormationStackStatus` is `UPDATE_ROLLBACK_FAILED`](#update-cluster-failure-rollback-failed-v3). 