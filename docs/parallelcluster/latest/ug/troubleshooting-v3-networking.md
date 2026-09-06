

# Network troubleshooting
<a name="troubleshooting-v3-networking"></a>

This section provides a troubleshooting tip for when you come across network issues, specifically when dealing with a cluster in a single public subnet issue.

## Cluster in a single public subnet issues
<a name="troubleshooting-v3-networking-private-subnet"></a>

In AWS ParallelCluster 3.16.0 and later, check `/var/log/chef-client.log` on a failed compute node. If you find an error similar to the following, the node was unable to reach DynamoDB during bootstrap:

```
INFO: Retrying execution of ruby_block[retrieve compute node info], 0 attempt left

    ================================================================================
    Error executing action `run` on resource 'ruby_block[retrieve compute node info]'
    ================================================================================

    RuntimeError
    ------------
    Failed to query DynamoDB for compute node info: the aws cli call did not return in time and was terminated. This usually means the compute node cannot reach DynamoDB. If the compute subnet has no internet egress (NAT/IGW), ensure a DynamoDB VPC gateway endpoint is configured and attached to the subnet's route table.
```

In AWS ParallelCluster versions prior to 3.16.0, compute nodes may silently hang during bootstrap instead of failing fast. Check `cloud-init-output.log` on a compute node for a log entry like the one below, which indicates the node is stuck retrieving information from DynamoDB:

```
ruby_block[retrieve compute node info] action run[2022-03-11T17:47:11+00:00] INFO: Processing ruby_block[retrieve compute node info] action run (aws-parallelcluster-slurm::init line 31)
```

The most common cause is a missing DynamoDB VPC endpoint, since AWS ParallelCluster reads compute node information from DynamoDB during bootstrap. For the full list of required endpoints, see [AWS ParallelCluster in a single subnet with no internet access](aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md).

To resolve, add the missing VPC endpoint (typically DynamoDB) to the compute subnet's route table. If the cluster has entered protected mode, see [Slurm cluster protected mode](slurm-protected-mode-v3.md) for how to recover.