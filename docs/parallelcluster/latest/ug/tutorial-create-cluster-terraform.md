# Creating a cluster with Terraform

When using AWS ParallelCluster, you only pay for the AWS resources that are created when you create or update AWS ParallelCluster images and clusters. For more information, see [AWS services used by AWS ParallelCluster](aws-services-v3.md "aws-services-v3.md").

**Prerequisites**

- Terraform v1.5.7+ is installed.
- [AWS ParallelCluster API](api-reference-v3.md "api-reference-v3.md") v3.8.0+ is deployed in your account. See [Deploy ParallelCluster API with Terraform](tutorial-deploy-terraform.md "tutorial-deploy-terraform.md").
- IAM role with the permissions to invoke the ParallelCluster API. See [Required
  permissions]
