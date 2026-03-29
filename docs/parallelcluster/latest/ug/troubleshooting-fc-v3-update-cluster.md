# Trying to update a cluster

The following section provides possible troubleshooting solutions to issues that might happen while you're trying to update a cluster.

## `pcluster update-cluster` command fails to run locally

Check the `~/.parallelcluster/pcluster-cli.log` in your local file system for failure details.

## Seeing `clusterStatus` is `UPDATE_FAILED` with `pcluster describe-cluster` command

### Root causing

To identify the root cause of the failure, the starting point is to look at cluster stack events and `/var/log/chef-client.log` in the head node.

A possible cause is that at least one cluster node did not apply the update. You can retrieve the list of nodes that failed to update in `/var/log/chef-client.log` in the head node by looking for `Check cluster readiness` in the log.

Check to see if your issue is mentioned in [GitHub Known Issues](https://github.com/aws/aws-parallelcluster/wiki "https://github.com/aws/aws-parallelcluster/wiki") at AWS ParallelCluster on GitHub.

### Preventing

A cluster update can fail if at least one node in the cluster did not successfully apply the update.
To reduce the risk of cluster update failure, we recommend terminating broken nodes before initiating the update.
An example of nodes that could be broken are compute nodes stuck in `COMPLETING` state for longer than the expected epilog duration.
To detect those nodes, you can run the following command, adapting the `threshold` value to your needs (the value must be greater than the maximum duration expected for your epilogs).

```
`$` `scontrol show nodes --json | jq -r --argjson threshold 60 '
 .nodes[] | select(.state | index("COMPLETING")) |
 select((now - .last_busy.number) > $threshold) |
 .name
'`
```

### Recovering

If the update failed, the rollback is the mechanism expected to recover the state of the cluster.

If the rollback failed, the cluster state is not deterministic.
In this case, it may be that `clustermgtd` was stopped to prevent the amplification of failures.
We recommend starting it by running the following command on the head node. Adapt the Python version to the one shipped with your AWS ParallelCluster version:

```
`$` `/opt/parallelcluster/pyenv/versions/`3.12.11`/envs/cookbook_virtualenv/bin/supervisorctl start clustermgtd`
```

## The cluster update timed out

This could be an issue related to `cfn-hup` not running. If the `cfn-hup` demon is terminated by an external cause,
it's not restarted automatically. If `cfn-hup` isn't running, during a cluster update, the CloudFormation stack starts the update process
as expected, but the update procedure isn't activated on the head node and the stack deployment eventually times out. For more information, see
[Troubleshooting a cluster update timeout when cfn-hup isn't running](troubleshooting-v3-cluster-update-timeout.md "troubleshooting-v3-cluster-update-timeout.md") to troubleshoot and recover
from the issue.
