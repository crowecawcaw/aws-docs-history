

# Deploy the API
<a name="tutorial-deploy-terraform-deploy-api"></a>

To deploy the API, run the standard Terraform commands in order.

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