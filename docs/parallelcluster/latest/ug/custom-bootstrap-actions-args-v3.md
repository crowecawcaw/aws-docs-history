

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Arguments
<a name="custom-bootstrap-actions-args-v3"></a>

In AWS ParallelCluster 2.x the `$1` arguments was a reserved one, to store the URL of the custom script. If you want to re-use the custom bootstrap scripts created for AWS ParallelCluster 2.x with AWS ParallelCluster 3.x you need to adapt them by considering the shift of the arguments. Please refer to [Moving from AWS ParallelCluster 2.x to 3.x](moving-from-v2-to-v3.md).