# AWS.Deployment.VNFDeployment

NF deployments are modeled by providing the infrastructure and the application
associated to it. The [cluster](#node_vnf_deployment_cluster "#node_vnf_deployment_cluster") attribute
specifies the EKS cluster to host your NFs. The [vnfs](#node_vnf_deployment_vnfs "#node_vnf_deployment_vnfs") attribute specifies the network functions for your deployment. You can also
provide optional lifecycle hooks operations of type [pre_create](#node_vnf_deployment_pre_create "#node_vnf_deployment_pre_create") and [post_create](#node_vnf_deployment_post_create "#node_vnf_deployment_post_create") to run instructions
specific to your deployment, such as calling an Inventory Management system API.

## Syntax

```
tosca.nodes.AWS.Deployment.VNFDeployment:
  requirements:
    deployment: String
    cluster: String
    vnfs: List
  interfaces:
    Hook:
      pre_create: String
      post_create: String
```

## Requirements

`deployment`

An [AWS.Deployment.VNFDeployment](node-vnf.md "node-vnf.md")
node.

Required: No

Type: String

`cluster`

An [AWS.Compute.EKS](node-eks.md "node-eks.md") node.

Required: Yes

Type: String

`vnfs`

An [AWS.VNF](node-vnf.md "node-vnf.md") node.

Required: Yes

Type: String

## Interfaces

### Hooks

Defines the stage when lifecycle hooks are run.

`pre_create`

An [AWS.HookExecution](node-hook-execution.md "node-hook-execution.md") node.
This hook is run before the `VNFDeployment` node deploys.

Required: No

Type: String

`post_create`

An [AWS.HookExecution](node-hook-execution.md "node-hook-execution.md") node.
This hook is run after the `VNFDeployment` node deploys.

Required: No

Type: String

## Example

```
SampleHelmDeploy:
  type: tosca.nodes.AWS.Deployment.VNFDeployment
  requirements:
    deployment: SampleHelmDeploy2
    cluster: SampleEKS
    vnfs:
      - vnf.SampleVNF
  interfaces:
    Hook:
      pre_create: SampleHook
```
