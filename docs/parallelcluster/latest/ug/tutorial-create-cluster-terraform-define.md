# Define a Terraform project

In this tutorial, you will define a simple Terraform project to deploy a cluster.

1. Create a directory called `my-clusters`.

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

```
module "pcluster" {
  source  = "aws-tf/parallelcluster/aws"
  version = "1.1.0"

  region                = var.region
  api_stack_name        = var.api_stack_name
  api_version           = var.api_version
  deploy_pcluster_api   = false

  template_vars         = local.config_vars
  cluster_configs       = local.cluster_configs
  config_path           = "config/clusters.yaml"
}
```

5. Create the file `clusters.tf` to define multiple clusters as Terraform local
   variables.

###### Note

You can define multiple clusters within the `cluster_config` element. For
every cluster, you can explicitly define the cluster properties within the local variables
(see `DemoCluster01`) or reference an external file (see
`DemoCluster02`).

To review the cluster properties that you can set within the configuration element,
see [Cluster configuration file](cluster-configuration-file-v3.md "cluster-configuration-file-v3.md").

To review the options that you can set for cluster creation, see [pcluster create-cluster](pcluster.md "pcluster.md").

```
locals {
  cluster_configs = {
    DemoCluster01 : {
      region : local.config_vars.region
      rollbackOnFailure : false
      validationFailureLevel : "WARNING"
      suppressValidators : [
        "type:KeyPairValidator"
      ]
      configuration : {
        Region : local.config_vars.region
        Image : {
          Os : "alinux2"
        }
        HeadNode : {
          InstanceType : "t3.small"
          Networking : {
            SubnetId : local.config_vars.subnet
          }
          Iam : {
            AdditionalIamPolicies : [
              { Policy : "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore" }
            ]
          }
        }
        Scheduling : {
          Scheduler : "slurm"
          SlurmQueues : [{
            Name : "queue1"
            CapacityType : "ONDEMAND"
            Networking : {
              SubnetIds : [local.config_vars.subnet]
            }
            Iam : {
              AdditionalIamPolicies : [
                { Policy : "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore" }
              ]
            }
            ComputeResources : [{
              Name : "compute"
              InstanceType : "t3.small"
              MinCount : "1"
              MaxCount : "4"
            }]
          }]
          SlurmSettings : {
            QueueUpdateStrategy : "TERMINATE"
          }
        }
      }
    }
    DemoCluster02 : {
      configuration : "config/cluster_config.yaml"
    }
  }
}
```

6. Create the file `config/clusters.yaml` to define multiple clusters as YAML configuration.

```
DemoCluster03:
  region: ${region}
  rollbackOnFailure: true
  validationFailureLevel: WARNING
  suppressValidators:
    - type:KeyPairValidator
  configuration: config/cluster_config.yaml
DemoCluster04:
  region: ${region}
  rollbackOnFailure: false
  configuration: config/cluster_config.yaml
```

7. Create the file `config/cluster_config.yaml`, which is a standard ParallelCluster config file where Terraform variables can be injected.

To review the cluster properties that you can set within the configuration element,
see [Cluster configuration file](cluster-configuration-file-v3.md "cluster-configuration-file-v3.md").

```
Region: ${region}
Image:
 Os: alinux2
HeadNode:
 InstanceType: t3.small
 Networking:
   SubnetId: ${subnet}
 Iam:
   AdditionalIamPolicies:
     - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
Scheduling:
 Scheduler: slurm
 SlurmQueues:
   - Name: queue1
     CapacityType: ONDEMAND
     Networking:
       SubnetIds:
         - ${subnet}
     Iam:
       AdditionalIamPolicies:
         - Policy: arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
     ComputeResources:
       - Name: compute
         InstanceType: t3.small
         MinCount: 1
         MaxCount: 5
 SlurmSettings:
   QueueUpdateStrategy: TERMINATE
```

8. Create the file `clusters_vars.tf` to define the variables that can be injected
   into cluster configurations.

This file allows you to define dynamic values that can be used in cluster configurations, such as region and subnet.

This example retrieves values directly from the project variables, but you may need
to use custom logic to determine them.

```
locals {
  config_vars = {
    subnet = var.subnet_id
    region = var.cluster_region
  }
}
```

9. Create the file `variables.tf` to define the variables that can be injected for
   this project.

```
variable "region" {
  description = "The region the ParallelCluster API is deployed in."
  type        = string
  default     = "us-east-1"
}

variable "cluster_region" {
  description = "The region the clusters will be deployed in."
  type        = string
  default     = "us-east-1"
}

variable "profile" {
  type        = string
  description = "The AWS profile used to deploy the clusters."
  default     = null
}

variable "subnet_id" {
  type        = string
  description = "The id of the subnet to be used for the ParallelCluster instances."
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

10. Create the file `terraform.tfvars` to set arbitrary values for the variables.

The file below deploys the clusters in `eu-west-1` within the subnet
`subnet-123456789`, using the existing ParallelCluster API 3.11.1, which is
already deployed in `us-east-1` with stack name
`MyParallelClusterAPI-3111`.

```
region = "us-east-1"
api_stack_name = "MyParallelClusterAPI-3111"
api_version = "3.11.1"

cluster_region = "eu-west-1"
subnet_id = "subnet-123456789"
```

11. Create the file `outputs.tf` to define the outputs returned by this project.

```
output "clusters" {
  value = module.pcluster.clusters
}
```

The project directory is:

```
my-clusters
├── config
│   ├── cluster_config.yaml - Cluster configuration, where terraform variables can be injected..
│   └── clusters.yaml - File listing all the clusters to deploy.
├── clusters.tf - Clusters defined as Terraform local variables.
├── clusters_vars.tf - Variables that can be injected into cluster configurations.
├── main.tf - Terraform entrypoint where the ParallelCluster module is configured.
├── outputs.tf - Defines the cluster as a Terraform output.
├── providers.tf - Configures the providers: ParallelCluster and AWS.
├── terraform.tf - Import the ParallelCluster provider.
├── terraform.tfvars - Defines values for variables, e.g. region, PCAPI stack name.
└── variables.tf - Defines the variables, e.g. region, PCAPI stack name.
```
