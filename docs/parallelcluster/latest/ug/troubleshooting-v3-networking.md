# Network troubleshooting

This section provides a troubleshooting tip for when you come across network issues,
specifically when dealing with a cluster in a single public subnet issue.

## Cluster in a single public subnet issues

Check the `cloud-init-output.log` from one of the compute nodes. If you find something like the following that indicates the node
is stuck in Slurm initialization, it is most likely due to a missing DynamoDB VPC endpoint. Add the DynamoDB endpoint. For more information see [AWS ParallelCluster in a single subnet with no internet
access](aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md "aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md").

```
ruby_block[retrieve compute node info] action run[2022-03-11T17:47:11+00:00] INFO: Processing ruby_block[retrieve compute node info] action run (aws-parallelcluster-slurm::init line 31)
```
