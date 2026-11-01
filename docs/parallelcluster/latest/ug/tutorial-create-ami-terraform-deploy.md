

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Deploy the AMI
<a name="tutorial-create-ami-terraform-deploy"></a>

To deploy the AMI, run the standard Terraform commands in order.

1. Build the project:

   ```
   terraform init
   ```

1. Define the deployment plan:

   ```
   terraform plan -out tfplan
   ```

1. Deploy the plan:

   ```
   terraform apply tfplan
   ```