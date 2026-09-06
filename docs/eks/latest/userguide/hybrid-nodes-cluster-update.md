

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable hybrid nodes on an existing Amazon EKS cluster or modify configuration
<a name="hybrid-nodes-cluster-update"></a>

This topic provides an overview of the available options and describes what to consider when you add, change, or remove the hybrid nodes configuration for an Amazon EKS cluster.

To enable an Amazon EKS cluster to use hybrid nodes, add the IP address CIDR ranges of your on-premises node and optionally pod network in the `RemoteNetworkConfig` configuration. EKS uses this list of CIDRs to enable connectivity between the cluster and your on-premises networks. For a full list of options when updating your cluster configuration, see the [UpdateClusterConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterConfig.html) in the *Amazon EKS API Reference*.

You can do any of the following actions to the EKS Hybrid Nodes networking configuration in a cluster:
+  [Add remote network configuration to enable EKS Hybrid Nodes in an existing cluster.](#hybrid-nodes-cluster-enable-existing) 
+  [Add, change, or remove the remote node networks or the remote pod networks in an existing cluster.](#hybrid-nodes-cluster-update-config) 
+  [Remove all remote node network CIDR ranges to disable EKS Hybrid Nodes in an existing cluster.](#hybrid-nodes-cluster-disable) 

## Prerequisites
<a name="hybrid-nodes-cluster-enable-prep"></a>
+ Before enabling your Amazon EKS cluster for hybrid nodes, ensure your environment meets the requirements outlined at [Prerequisite setup for hybrid nodes](hybrid-nodes-prereqs.md), and detailed at [Prepare networking for hybrid nodes](hybrid-nodes-networking.md), [Prepare operating system for hybrid nodes](hybrid-nodes-os.md), and [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md).
+ Your cluster must use IPv4 address family.
+ Your cluster must use either `API` or `API_AND_CONFIG_MAP` for the cluster authentication mode. The process for modifying the cluster authentication mode is described at [Change authentication mode to use access entries](setting-up-access-entries.md).
+ We recommend that you use either public or private endpoint access for the Amazon EKS Kubernetes API server endpoint, but not both. If you choose “Public and Private”, the Amazon EKS Kubernetes API server endpoint will always resolve to the public IPs for hybrid nodes running outside of your VPC, which can prevent your hybrid nodes from joining the cluster. The process for modifying network access to your cluster is described at [Cluster API server endpoint](cluster-endpoint.md).
+ The latest version of the AWS Command Line Interface (AWS CLI) installed and configured on your device. To check your current version, use `aws --version`. Package managers such as yum, apt-get, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Configuring settings for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) in the AWS Command Line Interface User Guide.
+ An [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles#iam-term-principal) with permission to call [UpdateClusterConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterConfig.html) on your Amazon EKS cluster.
+ Update add-ons to versions that are compatible with hybrid nodes. For the add-ons versions that are compatible with hybrid nodes, see [Configure add-ons for hybrid nodes](hybrid-nodes-add-ons.md).
+ If you are running add-ons that are not compatible with hybrid nodes, ensure that the add-on [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) or [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) has the following affinity rule to prevent deployment to hybrid nodes. Add the following affinity rule if it is not already present.

  ```
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: NotIn
            values:
            - hybrid
  ```

## Considerations
<a name="hybrid-nodes-cluster-enable-consider"></a>

The `remoteNetworkConfig` JSON object has the following behavior during an update:
+ Any existing part of the configuration that you don’t specify is unchanged. If you don’t specify either of the `remoteNodeNetworks` or `remotePodNetworks`, that part will remain the same.
+ If you are modifying either the `remoteNodeNetworks` or `remotePodNetworks` lists of CIDRs, you must specify the complete list of CIDRs that you want in your final configuration. When you specify a change to either the `remoteNodeNetworks` or `remotePodNetworks` CIDR list, EKS replaces the original list during the update.
+ Your on-premises node and pod CIDR blocks must meet the following requirements:

  1. Be within one of the IPv4 RFC-1918 ranges: 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16 , or within the CGNAT range defined by RFC 6598: `100.64.0.0/10` 

  1. Not overlap with each other, all CIDRs of the VPC for your Amazon EKS cluster, or your Kubernetes service IPv4 CIDR.

## Enable hybrid nodes on an existing cluster
<a name="hybrid-nodes-cluster-enable-existing"></a>

You can enable EKS Hybrid Nodes in an existing cluster by using:
+  [AWS CloudFormation](#hybrid-nodes-cluster-enable-cfn) 
+  [AWS CLI](#hybrid-nodes-cluster-enable-cli) 
+  [AWS Management Console](#hybrid-nodes-cluster-enable-console) 

### Enable EKS Hybrid Nodes in an existing cluster - AWS CloudFormation
<a name="hybrid-nodes-cluster-enable-cfn"></a>

1. To enable EKS Hybrid Nodes in your cluster, add the `RemoteNodeNetwork` and (optional) `RemotePodNetwork` to your CloudFormation template and update the stack. Note that `RemoteNodeNetwork` is a list with a maximum of one `Cidrs` item and the `Cidrs` is a list of multiple IP CIDR ranges.

   ```
   RemoteNetworkConfig:
     RemoteNodeNetworks:
       - Cidrs: [RemoteNodeCIDR]
     RemotePodNetworks:
       - Cidrs: [RemotePodCIDR]
   ```

1. Continue to [Prepare cluster access for hybrid nodes](hybrid-nodes-cluster-prep.md).

### Enable EKS Hybrid Nodes in an existing cluster - AWS CLI
<a name="hybrid-nodes-cluster-enable-cli"></a>

1. Run the following command to enable `RemoteNetworkConfig` for EKS Hybrid Nodes for your EKS cluster. Before running the command, replace the following with your settings. For a full list of settings, see the [UpdateClusterConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterConfig.html) in the *Amazon EKS API Reference*.

   1.  `CLUSTER_NAME`: name of the EKS cluster to update.

   1.  `AWS_REGION`: AWS Region where the EKS cluster is running.

   1.  `REMOTE_NODE_CIDRS`: the on-premises node CIDR for your hybrid nodes.

   1.  `REMOTE_POD_CIDRS` (optional): the on-premises pod CIDR for workloads running on hybrid nodes.

      ```
      aws eks update-cluster-config \
          --name CLUSTER_NAME \
          --region AWS_REGION \
          --remote-network-config '{"remoteNodeNetworks":[{"cidrs":["REMOTE_NODE_CIDRS"]}],"remotePodNetworks":[{"cidrs":["REMOTE_POD_CIDRS"]}]}'
      ```

1. It takes several minutes to update the cluster. You can query the status of your cluster with the following command. Replace `CLUSTER_NAME` with the name of the cluster you are modifying and `AWS_REGION` with the AWS Region where the cluster is running. Don’t proceed to the next step until the output returned is `ACTIVE`.

   ```
   aws eks describe-cluster \
       --name CLUSTER_NAME \
       --region AWS_REGION \
       --query "cluster.status"
   ```

1. Continue to [Prepare cluster access for hybrid nodes](hybrid-nodes-cluster-prep.md).

### Enable EKS Hybrid Nodes in an existing cluster - AWS Management Console
<a name="hybrid-nodes-cluster-enable-console"></a>

1. Open the Amazon EKS console at [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose the name of the cluster to display your cluster information.

1. Choose the **Networking** tab and choose **Manage**.

1. In the dropdown, choose **Remote networks**.

1.  **Choose Configure remote networks to enable hybrid nodes** and specify your on-premises node and pod CIDRs for hybrid nodes.

1. Choose **Save changes** to finish. Wait for the cluster status to return to **Active**.

1. Continue to [Prepare cluster access for hybrid nodes](hybrid-nodes-cluster-prep.md).

## Update hybrid nodes configuration in an existing cluster
<a name="hybrid-nodes-cluster-update-config"></a>

You can modify `remoteNetworkConfig` in an existing hybrid cluster by using any of the following:
+  [AWS CloudFormation](#hybrid-nodes-cluster-update-cfn) 
+  [AWS CLI](#hybrid-nodes-cluster-update-cli) 
+  [AWS Management Console](#hybrid-nodes-cluster-update-console) 

### Update hybrid configuration in an existing cluster - AWS CloudFormation
<a name="hybrid-nodes-cluster-update-cfn"></a>

1. Update your CloudFormation template with the new network CIDR values.

   ```
   RemoteNetworkConfig:
     RemoteNodeNetworks:
       - Cidrs: [NEW_REMOTE_NODE_CIDRS]
     RemotePodNetworks:
       - Cidrs: [NEW_REMOTE_POD_CIDRS]
   ```
**Note**  
When updating `RemoteNodeNetworks` or `RemotePodNetworks` CIDR lists, include all CIDRs (new and existing). EKS replaces the entire list during updates. Omitting these fields from the update request retains their existing configurations.

1. Update your CloudFormation stack with the modified template and wait for the stack update to complete.

### Update hybrid configuration in an existing cluster - AWS CLI
<a name="hybrid-nodes-cluster-update-cli"></a>

1. To modify the remote network CIDRs, run the following command. Replace the values with your settings:

   ```
   aws eks update-cluster-config
   --name CLUSTER_NAME
   --region AWS_REGION
   --remote-network-config '{"remoteNodeNetworks":[{"cidrs":["NEW_REMOTE_NODE_CIDRS"]}],"remotePodNetworks":[{"cidrs":["NEW_REMOTE_POD_CIDRS"]}]}'
   ```
**Note**  
When updating `remoteNodeNetworks` or `remotePodNetworks` CIDR lists, include all CIDRs (new and existing). EKS replaces the entire list during updates. Omitting these fields from the update request retains their existing configurations.

1. Wait for the cluster status to return to ACTIVE before proceeding.

### Update hybrid configuration in an existing cluster - AWS Management Console
<a name="hybrid-nodes-cluster-update-console"></a>

1. Open the Amazon EKS console at [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose the name of the cluster to display your cluster information.

1. Choose the **Networking** tab and choose **Manage**.

1. In the dropdown, choose **Remote networks**.

1. Update the CIDRs under `Remote node networks` and `Remote pod networks - Optional` as needed.

1. Choose **Save changes** and wait for the cluster status to return to **Active**.

## Disable Hybrid nodes in an existing cluster
<a name="hybrid-nodes-cluster-disable"></a>

You can disable EKS Hybrid Nodes in an existing cluster by using:
+  [AWS CloudFormation](#hybrid-nodes-cluster-disable-cfn) 
+  [AWS CLI](#hybrid-nodes-cluster-disable-cli) 
+  [AWS Management Console](#hybrid-nodes-cluster-disable-console) 

### Disable EKS Hybrid Nodes in an existing cluster - AWS CloudFormation
<a name="hybrid-nodes-cluster-disable-cfn"></a>

1. To disable EKS Hybrid Nodes in your cluster, set `RemoteNodeNetworks` and `RemotePodNetworks` to empty arrays in your CloudFormation template and update the stack.

   ```
   RemoteNetworkConfig:
     RemoteNodeNetworks: []
     RemotePodNetworks: []
   ```

### Disable EKS Hybrid Nodes in an existing cluster - AWS CLI
<a name="hybrid-nodes-cluster-disable-cli"></a>

1. Run the following command to remove `RemoteNetworkConfig` from your EKS cluster. Before running the command, replace the following with your settings. For a full list of settings, see the [UpdateClusterConfig](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterConfig.html) in the *Amazon EKS API Reference*.

   1.  `CLUSTER_NAME`: name of the EKS cluster to update.

   1.  `AWS_REGION`: AWS Region where the EKS cluster is running.

      ```
      aws eks update-cluster-config \
          --name CLUSTER_NAME \
          --region AWS_REGION \
          --remote-network-config '{"remoteNodeNetworks":[],"remotePodNetworks":[]}'
      ```

1. It takes several minutes to update the cluster. You can query the status of your cluster with the following command. Replace `CLUSTER_NAME` with the name of the cluster you are modifying and `AWS_REGION` with the AWS Region where the cluster is running. Don’t proceed to the next step until the output returned is `ACTIVE`.

   ```
   aws eks describe-cluster \
       --name CLUSTER_NAME \
       --region AWS_REGION \
       --query "cluster.status"
   ```

### Disable EKS Hybrid Nodes in an existing cluster - AWS Management Console
<a name="hybrid-nodes-cluster-disable-console"></a>

1. Open the Amazon EKS console at [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose the name of the cluster to display your cluster information.

1. Choose the **Networking** tab and choose **Manage**.

1. In the dropdown, choose **Remote networks**.

1. Choose **Configure remote networks to enable hybrid nodes** and remove all the CIDRs under `Remote node networks` and `Remote pod networks - Optional`.

1. Choose **Save changes** to finish. Wait for the cluster status to return to **Active**.