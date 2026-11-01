

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Schedulers supported by AWS ParallelCluster
<a name="schedulers-v3"></a>

 AWS ParallelCluster supports Slurm and AWS Batch schedulers, which are set using the [`Scheduler`](Scheduling-v3.md#yaml-Scheduling-Scheduler) setting. The following topics will describe each scheduler and how to use them. Starting with AWS ParallelCluster version 3.16.0, AWS Batch as a scheduler is no longer supported.

**Topics**
+ [Slurm Workload Manager (`slurm`)](slurm-workload-manager-v3.md)
+ [Using AWS Batch (`awsbatch`) scheduler with AWS ParallelCluster](awsbatchcli-v3.md)