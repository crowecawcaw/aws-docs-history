# Trying to update a cluster

The following section provides possible troubleshooting solutions to issues that might happen while you're trying to update a cluster.

## `pcluster update-cluster` command fails to run locally

Check the `~/.parallelcluster/pcluster-cli.log` in your local file system for failure details.

## Seeing `clusterStatus` is `UPDATE_FAILED` with `pcluster describe-cluster` command

If the cluster stack update rolled back, check the `/var/log/chef-client.log` file for error details.

Check to see if your issue is mentioned in [GitHub Known Issues](https://github.com/aws/aws-parallelcluster/wiki "https://github.com/aws/aws-parallelcluster/wiki") at AWS ParallelCluster on GitHub.

If the rollback failed according to logs `/var/log/chef-client.log`, it may be that `clustermgtd` was stopped to prevent the amplification of failures.
In this case, you need to manually restart it by executing the following command on the Head Node:

```
`$` `/opt/parallelcluster/pyenv/versions/`3.12.11`/envs/cookbook_virtualenv/bin/supervisorctl start clustermgtd`
```

## The cluster update timed out

This could be an issue related to `cfn-hup` not running. If the `cfn-hup` demon is terminated by an external cause,
it's not restarted automatically. If `cfn-hup` isn't running, during a cluster update, the CloudFormation stack starts the update process
as expected, but the update procedure isn't activated on the head node and the stack deployment eventually times out. For more information, see
[Troubleshooting a cluster update timeout when cfn-hup isn't
running](troubleshooting-v3-cluster-update-timeout.md "troubleshooting-v3-cluster-update-timeout.md") to troubleshoot and recover
from the issue.
