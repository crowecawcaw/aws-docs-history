# Trying to delete a cluster

If you get an error while trying to delete a cluster, the following sections provide
troubleshooting tips for the common scenarios.

## The `pcluster delete-cluster` command fails to run locally

Check the `~/.parallelcluster/pcluster-cli.log` file in your local file system.

## The cluster stack fails to delete

If the cluster stack fails to delete, check the CloudFormation stack events message.

Check if your issue is mentioned in [GitHub Known Issues](https://github.com/aws/aws-parallelcluster/wiki "https://github.com/aws/aws-parallelcluster/wiki") at
AWS ParallelCluster on GitHub.
