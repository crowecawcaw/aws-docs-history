

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Seeing nodes are in `DOWN` state with `Reason (Code:InsufficientInstanceCapacity)...`
<a name="compute-node-initialization-down-nodes-v3"></a>

You are experiencing an insufficient capacity issue. Follow [https://aws.amazon.com/premiumsupport/knowledge-center/ec2-insufficient-capacity-errors/](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-insufficient-capacity-errors/) to troubleshoot the issue. For more information about AWS ParallelCluster's fast insufficient capacity fail-over mode, see [Slurm cluster fast insufficient capacity fail-over](slurm-short-capacity-fail-mode-v3.md).