

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable or Disable Built-in NodePools
<a name="set-builtin-node-pools"></a>

EKS Auto Mode has two built-in NodePools. You can enable or disable these NodePools using the AWS console, CLI, or API.

## Built-in NodePool Reference
<a name="_built_in_nodepool_reference"></a>
+  `system` 
  + This NodePool has a `CriticalAddonsOnly` taint. Many EKS add-ons, such as CoreDNS, tolerate this taint. Use this system node pool to separate cluster-critical applications.
  + Supports both `amd64` and `arm64` architectures.
+  `general-purpose` 
  + This NodePool provides support for launching nodes for general purpose workloads in your cluster.
  + Uses only `amd64` architecture.

Both built-in NodePools:
+ Use the default EKS NodeClass
+ Use only on-demand EC2 capacity
+ Use the C, M, and R EC2 instance families
+ Require generation 5 or newer EC2 instances

**Note**  
Enabling at least one built-in NodePool is required for EKS to provision the "default" NodeClass. If you disable all built-in NodePools, you’ll need to create a custom NodeClass and configure a NodePool to use it. For more information about NodeClasses, see [Create a Node Class for Amazon EKS](create-node-class.md).

**Important**  
When you remove a built-in NodePool name from `computeConfig.nodePools`, the corresponding NodePool Kubernetes resource is deleted from the cluster. Any nodes managed by that NodePool are drained and terminated. When you add a built-in NodePool name back to `computeConfig.nodePools`, the corresponding NodePool resource is recreated on the cluster. This behavior is important when planning capacity changes, because Karpenter discovers NodePool resources through the Kubernetes API and stops scheduling nodes for deleted NodePools.

## Procedure
<a name="_procedure"></a>

### Prerequisites
<a name="_prerequisites"></a>
+ The latest version of the AWS Command Line Interface (AWS CLI) installed and configured on your device. To check your current version, use `aws --version`. To install the latest version, see [Installing](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Quick configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-configure-quickstart-config) with aws configure in the AWS Command Line Interface User Guide.
  + Login to the CLI with sufficient IAM permissions to create AWS resources including IAM Policies, IAM Roles, and EKS Clusters.

### Enable with AWS CLI
<a name="enable_with_shared_aws_cli"></a>

Use the following command to enable both built-in NodePools:

```
aws eks update-cluster-config \
  --name <cluster-name> \
  --compute-config '{
    "nodeRoleArn": "<node-role-arn>",
    "nodePools": ["general-purpose", "system"],
    "enabled": true
  }' \
  --kubernetes-network-config '{
  "elasticLoadBalancing":{"enabled": true}
  }' \
  --storage-config '{
  "blockStorage":{"enabled": true}
  }'
```

You can modify the command to selectively enable the NodePools.

### Disable with AWS CLI
<a name="disable_with_shared_aws_cli"></a>

Use the following command to disable both built-in NodePools:

```
aws eks update-cluster-config \
  --name <cluster-name> \
  --compute-config '{
  "enabled": true,
  "nodePools": []
  }' \
  --kubernetes-network-config '{
  "elasticLoadBalancing":{"enabled": true}}' \
  --storage-config '{
  "blockStorage":{"enabled": true}
  }'
```