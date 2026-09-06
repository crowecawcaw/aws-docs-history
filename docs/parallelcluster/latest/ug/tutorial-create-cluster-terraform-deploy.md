

# Deploy the cluster
<a name="tutorial-create-cluster-terraform-deploy"></a>

To deploy the cluster, run the standard Terraform commands in order.

**Note**  
This example assumes that you've already deployed the ParallelCluster API in your account.

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

## Deploy the ParallelCluster API with clusters
<a name="tutorial-create-cluster-terraform-deploy-api"></a>

If you haven't deployed the ParallelCluster API and you want to deploy it with the clusters, change the following files:
+ `main.tf`

  ```
  module "pcluster" {
    source  = "aws-tf/aws/parallelcluster"
    version = "1.0.0"
  
    region                = var.region
    api_stack_name        = var.api_stack_name
    api_version           = var.api_version
    deploy_pcluster_api   = true
    parameters = {
      EnableIamAdminAccess = "true"
    }
    
    template_vars         = local.config_vars
    cluster_configs       = local.cluster_configs
    config_path           = "config/clusters.yaml"
  }
  ```
+ `providers.tf`

  ```
  provider "aws-parallelcluster" {
    region   = var.region
    profile  = var.profile
    endpoint = module.pcluster.pcluster_api_stack_outputs.ParallelClusterApiInvokeUrl
    role_arn = module.pcluster.pcluster_api_stack_outputs.ParallelClusterApiUserRole
  }
  ```