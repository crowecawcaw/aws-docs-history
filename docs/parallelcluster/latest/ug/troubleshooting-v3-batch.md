# Troubleshooting issues in clusters with AWS Batch integration

This section provides possible troubleshooting tips for clusters with AWS Batch scheduler
integration, specifically with head node issues, compute issues, job failures, and timeout
errors.

###### Topics

- [Head node issues](#troubleshooting-v3-batch-head-node "#troubleshooting-v3-batch-head-node")
- [Compute issues](#troubleshooting-v3-batch-compute-nodes "#troubleshooting-v3-batch-compute-nodes")
- [Job failures](#troubleshooting-v3-batch-job-fail "#troubleshooting-v3-batch-job-fail")
- [Connect timeout on endpoint URL error](#troubleshooting-v3-batch-connect-timeout "#troubleshooting-v3-batch-connect-timeout")

## Head node issues

You can troubleshoot head node setup issues in the same way as a Slurm cluster (except for Slurm specific logs). For more information
about these issues, see [Head node](troubleshooting-v3-scaling-issues.md#troubleshooting-v3-node-init.head-node "troubleshooting-v3-scaling-issues.md#troubleshooting-v3-node-init.head-node").

## Compute issues

AWS Batch manages the scaling and compute aspects of your services. If you encounter compute related issues, see
the AWS Batch [troubleshooting](../../../batch/latest/userguide/troubleshooting.md "../../../batch/latest/userguide/troubleshooting.md")
documentation for help.

## Job failures

If a job fails, you can run the [awsbout](awsbatchcli.md "awsbatchcli.md")
command to retrieve the job output. You can also run the [awsbstat](awsbatchcli.md "awsbatchcli.md") command to obtain a link to the job logs stored by Amazon CloudWatch.

## Connect timeout on endpoint URL error

If multi-node parallel jobs fail with error: `Connect timeout on endpoint URL`:

- In the `awsbout` output log, check that the job is multi-node parallel from the output: `Detected 3/3 compute nodes. Waiting for all compute nodes to start.`
- Verify whether the compute nodes subnet is public.

Multi-node parallel jobs don't support the use of public subnets when using AWS Batch in AWS ParallelCluster. Use a private subnet for your
compute nodes and jobs. For more information, see [Compute environment considerations](../../../batch/latest/userguide/multi-node-parallel-jobs.md#mnp-ce "../../../batch/latest/userguide/multi-node-parallel-jobs.md#mnp-ce") in the _AWS Batch User Guide_. To configure a private subnet for your compute nodes,
see [AWS ParallelCluster with AWS Batch
scheduler](network-configuration-v3-batch.md "network-configuration-v3-batch.md").
