# Define a Terraform project

In this tutorial, you will define a Terraform project.

1. Create a directory called `my-pcluster-api`.

All files that you create will be within this directory. 2. Create the file `provider.tf` to configure the AWS provider.

```
provider "aws" {
  region  = var.region
  profile = var.profile
}
```

3. Create the file `main.tf` to define the resources using the ParallelCluster
   module.

```
module `"parallelcluster_pcluster_api"` {
  source = `"aws-tf/parallelcluster/aws//modules/pcluster_api"`
  version = `"1.1.0"`

  region                = var.region
  api_stack_name        = var.api_stack_name
  api_version           = var.api_version

  parameters = {
    EnableIamAdminAccess = `"true"`
  }
}
```

4. Create the file `variables.tf` to define the variables that can be injected for
   this project.

```
variable "region" {
  description = "The region the ParallelCluster API is deployed in."
  type        = string
  default     = "us-east-1"
}

variable "profile" {
  type        = string
  description = "The AWS profile used to deploy the clusters."
  default     = null
}

variable "api_stack_name" {
  type        = string
  description = "The name of the CloudFormation stack used to deploy the ParallelCluster API."
  default     = "ParallelCluster"
}

variable "api_version" {
  type        = string
  description = "The version of the ParallelCluster API."
}
```

5. Create the file `terraform.tfvars` to set arbitrary values for the variables.

The file below deploys a ParallelCluster API 3.11.1 in `us-east-1`
using the stack name `MyParallelClusterAPI-3111`. You'll be able to
reference this ParallelCluster API deployment using its stack name.

###### Note

The `api_version` assignment in the following code can be replaced with any supported AWS ParallelCluster version.

```
region = "us-east-1"
api_stack_name = "MyParallelClusterAPI-3111"
api_version = "3.11.1"
```

6. Create the file `outputs.tf` to define the outputs returned by this project.

```
output "pcluster_api_stack_outputs" {
  value = module.parallelcluster_pcluster_api.stack_outputs
}
```

The project directory is:

```
my-pcluster-api
├── main.tf - Terraform entrypoint to define the resources using the ParallelCluster module.
├── outputs.tf - Defines the outputs returned by Terraform.
├── providers.tf - Configures the AWS provider.
├── terraform.tfvars - Set the arbitrary values for the variables, i.e. region, PCAPI version, PCAPI stack name
└── variables.tf - Defines the variables, e.g. region, PCAPI version, PCAPI stack name.
```
