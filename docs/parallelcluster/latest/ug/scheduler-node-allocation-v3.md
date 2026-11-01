

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Cluster scaling for dynamic nodes
<a name="scheduler-node-allocation-v3"></a>

ParallelCluster supports Slurm's methods to dynamically scale clusters by using Slurm's power saver plugin. For more information, see the [Cloud Scheduling Guide](https://slurm.schedmd.com/elastic_computing.html) and the [Slurm Power Saving Guide](https://slurm.schedmd.com/power_save.html) in the Slurm documentation. The following topics describe the Slurm strategies for each version.

**Topics**
+ [Slurm dynamic node allocation strategies in version 3.8.0](scheduler-node-allocation-v3-3.8.0.md)
+ [Slurm dynamic node allocation strategies in version 3.7.x](scheduler-dynamic-node-allocation-v3-3.7.x.md)
+ [Slurm dynamic node allocation strategies in version 3.6.x and previous](scheduler-dynamic-node-allocation-v3-3.6.x.md)