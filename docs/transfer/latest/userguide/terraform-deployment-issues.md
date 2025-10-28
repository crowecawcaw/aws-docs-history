# Troubleshoot Terraform deployment

issues

This section describes possible solutions for issues related to deploying Transfer Family resources
using Terraform. For general information about Terraform modules for Transfer Family, see [Transfer Family Terraform modules](terraform.md "terraform.md").

###### Topics

- [Troubleshoot Terraform resource creation
  failures](#terraform-resource-creation "#terraform-resource-creation")
- [Troubleshoot Terraform state management
  issues](#terraform-state-issues "#terraform-state-issues")

## Troubleshoot Terraform resource creation

failures

Description

When attempting to create Transfer Family resources using Terraform, you encounter errors such
as:

```
Error: error creating Transfer Server: InvalidRequestException: The request is not valid.
Error: error creating Transfer User: InvalidRequestException: Unable to create the user because the server endpoint type is incompatible with the home directory type.
```

Cause

These errors typically occur due to incompatible configuration parameters or missing
dependencies in your Terraform configuration. Common causes include:

- Incompatible endpoint type and storage configurations
- Missing required IAM roles or policies
- Incorrect security policy specifications
- VPC endpoint configuration issues

Solution

To resolve Terraform deployment issues:

- Ensure your Terraform configuration uses compatible parameter
  combinations:
  - For public endpoints, ensure you're using Amazon S3 for storage.
  - For VPC endpoints, verify proper VPC and security group
    configuration.

- Use explicit dependencies with the `depends_on` attribute to ensure
  resources are created in the correct order.
- Verify that all IAM roles have the necessary trust relationships and
  permissions.
- Use the latest version of the AWS provider for Terraform to ensure
  compatibility with all Transfer Family features.
- For complex deployments and simple use cases, consider using the official Transfer Family
  Terraform modules available on GitHub at [https://github.com/aws-ia/terraform-aws-transfer-family](https://github.com/aws-ia/terraform-aws-transfer-family "https://github.com/aws-ia/terraform-aws-transfer-family"). These
  modules provide extensive examples covering simple and complex customer use
  cases, follow AWS best practices, and can simplify deployment for customers
  who need help with infrastructure as code (IaC) configuration.

## Troubleshoot Terraform state management

issues

Description

After making changes to your Transfer Family resources outside of Terraform (via console or
AWS CLI), you encounter state drift or errors when running `terraform plan` or
`terraform apply`.

Cause

Terraform maintains a state file that tracks the resources it manages. When changes
are made outside of Terraform, the state file becomes out of sync with the actual
resources, causing errors or unexpected behavior during subsequent Terraform
operations.

Solution

To resolve Terraform state management issues with Transfer Family resources:

1. Use `terraform import` to bring existing resources under Terraform
   management:

```
terraform import `<transfer_family_server.example>` s-`<server-id>`
terraform import `<transfer_family_server.example>` s-`<server-id>`/username
```

2. Use `terraform refresh` to update the state file with the current
   real-world infrastructure
3. For resources that can't be imported or have complex state issues, consider
   using `terraform state rm` to remove them from the state file, then
   recreate them with Terraform
4. Implement a policy to manage Transfer Family resources exclusively through Terraform to
   prevent future state drift
5. Use remote state storage with locking to prevent concurrent modifications when
   working in teams
