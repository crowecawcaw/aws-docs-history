# Define a Terraform project

In this tutorial, you will define a simple Terraform project to deploy a ParallelCluster custom AMI.

1. Create a directory called `my-amis`.

All files that you create will be within this directory. 2. Create the file `terraform.tf` to import the ParallelCluster provider.

```
terraform {
  required_version = ">= 1.5.7"
  required_providers {
    aws-parallelcluster = {
      source  = "aws-tf/aws-parallelcluster"
      version = "~> 1.0"
    }
  }
}
```

3. Create the file `providers.tf` to configure the ParallelCluster and AWS
   providers.

```
provider "aws" {
  region  = var.region
  profile = var.profile
}

provider "aws-parallelcluster" {
  region         = var.region
  profile        = var.profile
  api_stack_name = var.api_stack_name
  use_user_role  = true
}
```

4. Create the file `main.tf` to define the resources using the ParallelCluster
   module.

To review the image properties that you can set within the `image_configuration` element, see [Build image configuration files](image-builder-configuration-file-v3.md "image-builder-configuration-file-v3.md").

To review the options that you can set for image creation, for example
`image_id` and `rollback_on_failure`, see [pcluster build-image](pcluster.md "pcluster.md").

```
data "aws-parallelcluster_list_official_images" "parent_image" {
  region = var.region
  os = var.os
  architecture = var.architecture
}

resource "aws-parallelcluster_image" "demo01" {
  image_id            = "demo01"
  image_configuration = yamlencode({
    "Build":{
      "InstanceType": "c5.2xlarge",
      "ParentImage": data.aws-parallelcluster_list_official_images.parent_image.official_images[0].amiId,
      "UpdateOsPackages": {"Enabled": false}
    }
  })
  rollback_on_failure = false
}
```

5. Create the file `variables.tf` to define the variables that can be injected for
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

variable "os" {
  type        = string
  description = "The OS of the ParallelCluster image."
}

variable "architecture" {
  type        = string
  description = "The architecture of the ParallelCluster image."
}
```

6. Create the file `terraform.tfvars` to set your arbitrary values for the variables.

With the file below deploy the custom AMI in `us-east-1` based on Amazon
Linux 2 for x86_64 architecture, using the existing ParallelCluster API 3.11.1 which is
already deployed in `us-east-1` with stack name
`MyParallelClusterAPI-3111`.

```
region = "us-east-1"
api_stack_name = "MyParallelClusterAPI-3111"
api_version = "3.11.1"

os = "alinux2"
architecture = "x86_64"
```

7. Create the file `outputs.tf` to define the outputs returned by this project.

```
output "parent_image" {
  value = data.aws-parallelcluster_list_official_images.parent_image.official_images[0]
}

output "custom_image" {
  value = aws-parallelcluster_image.demo01
}
```

The project directory is:

```
my-amis
├── main.tf - Terraform entrypoint where the ParallelCluster module is configured.
├── outputs.tf - Defines the cluster as a Terraform output.
├── providers.tf - Configures the providers: ParallelCluster and AWS.
├── terraform.tf - Import the ParallelCluster provider.
├── terraform.tfvars - Defines values for variables, e.g. region, PCAPI stack name.
└── variables.tf - Defines the variables, e.g. region, PCAPI stack name.
```
