# Troubleshooting cluster deployment using Terraform

This section is relevant to clusters that were deployed using Terraform.

## ParallelCluster API not found

The planning could fail because the ParallelCluster API cannot be found. In this case, the returned error would be something like:

```
`Planning failed. Terraform encountered an error while generating this plan.

╷
│ Error: Unable to retrieve ParallelCluster API cloudformation stack.
│
│ with provider["registry.terraform.io/aws-tf/aws-parallelcluster"],
│ on providers.tf line 6, in provider "aws-parallelcluster":
│ 6: provider "aws-parallelcluster" {
│
│ operation error CloudFormation: DescribeStacks, https response error StatusCode: 400, RequestID: `REQUEST_ID`, api error ValidationError: Stack with id `PCAPI_STACK_NAME` does not exist`
```

To solve this error, deploy the ParallelCluster API in the account where the clusters
are going to be created. See [Creating a cluster with Terraform](tutorial-create-cluster-terraform.md "tutorial-create-cluster-terraform.md").

## User not authorized to call ParallelCluster API

The planning could fail because the IAM role/user you assumed to deploy your Terraform
project doesn't have permissions to interact with the ParallelCluster API. In this case, the
returned error would be something like:

```
`Planning failed. Terraform encountered an error while generating this plan.

│ Error: 403 Forbidden
│
│ with module.parallelcluster_clusters.module.clusters[0].pcluster_cluster.managed_configs["DemoCluster01"],
│ on .terraform/modules/parallelcluster_clusters/modules/clusters/main.tf line 35, in resource "pcluster_cluster" "managed_configs":
│ 35: resource "pcluster_cluster" "managed_configs" {
│
│ {{"Message":"User: `USER_ARN` is not authorized to perform: execute-api:Invoke on resource: `PC_API_REST_RESOURCE` with an explicit deny"}
│ }`
```

To solve this error, configure the ParallelCluster Provider so that it uses the
ParallelCluster API role to interact with the API.

```
provider "aws-parallelcluster" {
  region         = var.region
  profile        = var.profile
  api_stack_name = var.api_stack_name
  **use_user_role** **= true**
}
```
