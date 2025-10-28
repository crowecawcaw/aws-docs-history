# Deploy the AMI

To deploy the AMI, run the standard Terraform commands in order.

1. Build the project:

```
terraform init
```

2. Define the deployment plan:

```
terraform plan -out tfplan
```

3. Deploy the plan:

```
terraform apply tfplan
```
