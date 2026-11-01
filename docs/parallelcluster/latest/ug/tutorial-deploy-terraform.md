

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Deploy ParallelCluster API with Terraform
<a name="tutorial-deploy-terraform"></a>

In this tutorial, you will define a simple Terraform project to deploy a ParallelCluster API. 

**Prerequisites**
+ Terraform v1.5.7\+ is installed.
+ IAM role with the permissions to deploy the ParallelCluster API. See [Required permissions](tutorial-deploy-terraform-permissions.md).