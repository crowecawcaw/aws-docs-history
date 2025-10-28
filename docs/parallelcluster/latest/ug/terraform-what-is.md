# AWS ParallelCluster for Terraform

Beginning with AWS ParallelCluster 3.8.0, you can deploy clusters and custom images using
[Terraform](https://www.terraform.io/ "https://www.terraform.io/"). To begin using this feature, see
[Terraform Provider for AWS ParallelCluster](https://registry.terraform.io/providers/aws-tf/aws-parallelcluster/latest "https://registry.terraform.io/providers/aws-tf/aws-parallelcluster/latest") from the Terraform Registry.

###### Note

You must have [ParallelCluster API](api-reference-v3.md "api-reference-v3.md") deployed
in your account to use the provider.

Use the following chart to determine the compatibility between the provider and the
AWS ParallelCluster versions:

| Provider version | AWS ParallelCluster version |
| ---------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0.0            | 3.8.0-3.10.1                |
| 1.1.0            | 3.11.0+                     | See [examples](https://github.com/aws-tf/terraform-provider-aws-parallelcluster/tree/main/examples "https://github.com/aws-tf/terraform-provider-aws-parallelcluster/tree/main/examples") of how to use the provider. For an even smoother experience, use the official [Terraform Module for AWS ParallelCluster](https://registry.terraform.io/modules/aws-tf/parallelcluster/aws/latest "https://registry.terraform.io/modules/aws-tf/parallelcluster/aws/latest") from Terraform Registry. The module allows you to deploy: 1. ParallelCluster API 2. ParallelCluster clusters defined with YAML configuration file and HCL 3. Networking infrastructure required by a ParallelCluster cluster See [examples](https://github.com/aws-tf/terraform-aws-parallelcluster/tree/main/examples "https://github.com/aws-tf/terraform-aws-parallelcluster/tree/main/examples") of how to use the module. |
