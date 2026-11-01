

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Creating a custom AMI with Terraform
<a name="tutorial-create-ami-terraform"></a>

When using AWS ParallelCluster, you only pay for the AWS resources that are created when you create or update AWS ParallelCluster images and clusters. For more information, see [AWS services used by AWS ParallelCluster](aws-services-v3.md).

**Prerequisites**
+  Terraform v1.5.7\+ is installed. 
+ [AWS ParallelCluster API](api-reference-v3.md) v3.8.0\+ is deployed in your account. See [Creating a cluster with Terraform](tutorial-create-cluster-terraform.md). 
+ IAM role with the permissions to invoke the ParallelCluster API. See [Required permissions](tutorial-create-ami-terraform-permissions.md).