

# AWS.Deployment.VNFDeployment
<a name="node-vnf-deployment"></a>

NF deployments are modeled by providing the infrastructure and the application associated to it. The [cluster](#node_vnf_deployment_cluster) attribute specifies the EKS cluster to host your NFs. The [vnfs](#node_vnf_deployment_vnfs) attribute specifies the network functions for your deployment. You can also provide optional lifecycle hooks operations of type [pre\_create](#node_vnf_deployment_pre_create) and [post\_create](#node_vnf_deployment_post_create) to run instructions specific to your deployment, such as calling an Inventory Management system API.

## Syntax
<a name="node-vnf-deployment-syntax"></a>

```
tosca.nodes.AWS.Deployment.VNFDeployment:
  requirements:
    deployment: String
    cluster: String
    vnfs: List
  interfaces:
    Hook:
      pre\_create: String
      post\_create: String
```

## Requirements
<a name="node-vnf-deployment-requirements"></a>

 `deployment`    
An [AWS.Deployment.VNFDeployment](node-vnf.md) node.  
Required: No  
Type: String

 `cluster`    
An [AWS.Compute.EKS](node-eks.md) node.  
Required: Yes  
Type: String

 `vnfs`    
An [AWS.VNF](node-vnf.md) node.  
Required: Yes  
Type: String

## Interfaces
<a name="node-vnf-deployment-interfaces"></a>

### Hooks
<a name="node-vnf-deployment-hooks"></a>

Defines the stage when lifecycle hooks are run.

 `pre_create`    
An [AWS.HookExecution](node-hook-execution.md) node. This hook is run before the `VNFDeployment` node deploys.  
Required: No  
Type: String

 `post_create`    
An [AWS.HookExecution](node-hook-execution.md) node. This hook is run after the `VNFDeployment` node deploys.  
Required: No  
Type: String

## Example
<a name="node-vnf-deployment-example"></a>

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