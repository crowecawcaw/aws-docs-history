**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable or Disable Built-in NodePools

EKS Auto Mode has two built-in NodePools. You can enable or disable these NodePools using the AWS console, CLI, or API.

## Built-in NodePool Reference

- `system`
  - This NodePool has a `CriticalAddonsOnly` taint. Many EKS add-ons, such as CoreDNS, tolerate this taint. Use this system node pool to separate cluster-critical applications.
  - Supports both `amd64` and `arm64` architectures.

- `general-purpose`
  - This NodePool provides support for launching nodes for general purpose workloads in your cluster.
  - Uses only `amd64` architecture.

Both built-in NodePools:

- Use the default EKS NodeClass
- Use only on-demand EC2 capacity
- Use the C, M, and R EC2 instance families
- Require generation 5 or newer EC2 instances

###### Note

Enabling at least one built-in NodePool is required for EKS to provision the "default" NodeClass. If you disable all built-in NodePools, you’ll need to create a custom NodeClass and configure a NodePool to use it. For more information about NodeClasses, see [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md").

## Procedure

### Prerequisites

- The latest version of the AWS Command Line Interface (AWS CLI) installed and configured on your device. To check your current version, use `aws --version`. To install the latest version, see [Installing](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Quick configuration](../../../cli/latest/userguide/cli-chap-configure.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-chap-configure.md#cli-configure-quickstart-config") with aws configure in the AWS Command Line Interface User Guide.
  - Login to the CLI with sufficent IAM permissions to create AWS resources including IAM Policies, IAM Roles, and EKS Clusters.

### Enable with AWS CLI

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
