

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy an Amazon EKS local cluster on AWS Outposts configured with EC2 instance store
<a name="eks-outposts-instance-store-local-cluster-create"></a>

This topic provides instructions for deploying a local Amazon EKS cluster on an AWS Outpost configured with EC2 instance store.

**Note**  
If your Outpost is configured with Amazon EBS instead of EC2 instance store, the architecture described in this topic isn’t available for your Outpost. Outposts configured with EBS will continue to use the existing local clusters implementation. For more information, see [Deploy an Amazon EKS cluster on AWS Outposts](eks-outposts-local-cluster-create.md).  
If you are interested in creating a local cluster on an EBS-backed Outpost using the updated local clusters architecture, contact your AWS account team.

**Important**  
Local clusters support Outpost racks only. A single local cluster can run across multiple physical Outpost racks that comprise a single logical Outpost. A single local cluster can’t run across multiple logical Outposts.
The Kubernetes control plane runs in an AWS-managed service account on your Outpost. You can’t access the control plane instances, view them in the Amazon EC2 console, or run workloads on them.
The control plane runs on 6 EC2 instances (3 `etcd` \+ 3 API server) in an [external etcd topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/#external-etcd-topology). For capacity requirements, see [Select instance types and placement for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-capacity-considerations.md).
The [Amazon VPC CNI plugin for Kubernetes](managing-vpc-cni.md), [kube-proxy](managing-kube-proxy.md), and [CoreDNS](managing-coredns.md) are automatically installed on local clusters. For the full list of validated add-ons, see [Amazon EKS add-ons for local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-local-cluster-addons.md).
Amazon EKS periodically backs up `etcd`. If `etcd` loses quorum, Amazon EKS recovers your cluster state from the most recent snapshot.

 **Prerequisites** 
+ An existing Outpost rack configured with EC2 instance store, with sufficient virtualized capacity for the control plane instances. See [Select instance types and placement for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-capacity-considerations.md).
+ A VPC and subnets that meet the requirements described in [Create a VPC and subnets for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-vpc-subnet-requirements.md).
+ The `kubectl` command line tool is installed on your computer or AWS CloudShell. The version can be the same as, or up to one minor version earlier or later than, the Kubernetes version of your cluster. To install or upgrade `kubectl`, see [Set up `kubectl` and `eksctl`](install-kubectl.md).
+ The AWS CLI version `2.35.3` or later installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version`. To install or upgrade, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ An IAM principal (user or role) with permissions to create and describe an Amazon EKS cluster. For more information, see [Create a local Kubernetes cluster on an Outpost](security-iam-id-based-policy-examples.md#policy-create-local-cluster) and [List or describe all clusters](security-iam-id-based-policy-examples.md#policy-example2).
+ An IAM role for the cluster with the following AWS managed policies attached: [AmazonEKSClusterPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSClusterPolicy.html) and [AmazonEKSServicePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSServicePolicy.html). The role trust policy must allow the `eks.amazonaws.com` service principal to assume the role.

**Note**  
When you create a local cluster, the [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-principal) that creates the cluster is permanently added to the Kubernetes RBAC authorization table as an administrator with `system:masters` permissions. Make sure you never delete this principal.

## Create a local cluster
<a name="eks-outposts-instance-store-local-cluster-create-cluster"></a>

You can create a local cluster using the AWS Management Console, AWS CLI, Amazon EKS API, or AWS CloudFormation.

When you create a local cluster, note the following:
+ You must pass subnets in the Availability Zone to which the Outpost is homed. The request fails if you pass subnets in multiple Availability Zones.
+ You must set `endpointPrivateAccess` to `true`. You can optionally also enable `endpointPublicAccess`.
+ You must pass values for `outpostConfig`, including `outpostArns`, `controlPlaneInstanceType`, and `etcdInstanceType`. Optionally, you can specify placement configuration. See [Select instance types and placement for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-capacity-considerations.md).

### AWS CLI
<a name="awscli_is_create_cluster_outpost"></a>

```
aws eks create-cluster \
  --name my-cluster \
  --role-arn arn:aws:iam::111122223333:role/myEKSClusterRole \
  --kubernetes-version 1.36 \
  --resources-vpc-config subnetIds=subnet-ExampleID1,endpointPrivateAccess=true,endpointPublicAccess=true \
  --logging '{"clusterLogging":[{"types":["api","audit","authenticator","controllerManager","scheduler"],"enabled":true}]}' \
  --access-config authenticationMode=API_AND_CONFIG_MAP,bootstrapClusterCreatorAdminPermissions=true \
  --outpost-config outpostArns=arn:aws:outposts:region-code:111122223333:outpost/op-uniqueid,controlPlaneInstanceType=m5.large,controlPlanePlacement={spreadLevel=host},etcdInstanceType=m5.large,etcdPlacement={spreadLevel=host}
```

### AWS Management Console
<a name="console_is_create_cluster_outpost"></a>

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose **Create cluster**.

1. For **Kubernetes control plane location**, choose ** AWS Outposts**.

1. Configure the following:
   +  **Name** — A name for your cluster.
   +  **Kubernetes version** — The version to use.
   +  **Cluster service role** — The IAM role with [AmazonEKSClusterPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSClusterPolicy.html) and [AmazonEKSServicePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSServicePolicy.html).
   +  **Outpost ID** — The logical Outpost to deploy to.
   +  **Control plane instance type** — The instance type for the Kubernetes API server, scheduler, and controller manager.
   +  **etcd instance type** — The instance type for `etcd`.
   +  **Spread level** — `host` or `rack` for control plane and `etcd` placement.

1. Configure networking: VPC, subnets, security groups. Enable private endpoint access.

1. Configure observability: control plane logging.

1. Review and create.

### `CreateCluster` API
<a name="api_is_create_cluster_outpost"></a>

```
{
    "name": "my-cluster",
    "roleArn": "arn:aws:iam::111122223333:role/myEKSClusterRole",
    "version": "1.36",
    "resourcesVpcConfig": {
        "subnetIds": ["subnet-ExampleID1"],
        "endpointPublicAccess": true,
        "endpointPrivateAccess": true
    },
    "logging": {
        "clusterLogging": [{
            "types": ["api", "audit", "authenticator", "controllerManager", "scheduler"],
            "enabled": true
        }]
    },
    "accessConfig": {
        "authenticationMode": "API_AND_CONFIG_MAP",
        "bootstrapClusterCreatorAdminPermissions": true
    },
    "outpostConfig": {
        "outpostArns": ["arn:aws:outposts:region-code:111122223333:outpost/op-uniqueid"],
        "controlPlaneInstanceType": "m5.large",
        "controlPlanePlacement": {
            "spreadLevel": "host"
        },
        "etcdInstanceType": "m5.large",
        "etcdPlacement": {
            "spreadLevel": "host"
        }
    }
}
```

The `controlPlaneInstanceType` and `etcdInstanceType` parameters are required when you create a local cluster on Outposts configured with EC2 instance store. The `controlPlanePlacement` and `etcdPlacement` parameters are optional. If you don’t specify them, no placement spread strategy is applied.

**Note**  
 `outpostConfig` is a create-only property. To change the control plane instance type, `etcd` instance type, placement, or Outpost, you must create a new cluster.

## Connect to your cluster
<a name="eks-outposts-instance-store-local-cluster-create-connect"></a>

Configure `kubectl` to communicate with your cluster:

```
aws eks update-kubeconfig --region region-code --name my-cluster
```

**Note**  
If you created your cluster using AWS CLI versions below `2.35.3`, you must update your `kubeconfig` to specify `--cluster-name` (instead of `--cluster-id`) in the `exec` args

The cluster’s Kubernetes API server endpoint is hosted in Amazon Route 53. The endpoint resolves to the private IP addresses of the cross-account elastic network interfaces (ENIs) that Amazon EKS creates in your subnets. These ENIs have fixed private IP addresses that don’t change throughout the cluster lifecycle.

When you create a cluster, Amazon EKS creates 3 elastic network interfaces in the subnets that you specify. These network interfaces enable communication between your cluster and your VPC. Each network interface has the text `Amazon EKS {{cluster-name}} ` in its description.

## Deploy worker nodes
<a name="eks-outposts-instance-store-local-cluster-create-nodes"></a>

Deploy worker nodes to your local cluster using [self-managed node groups](launch-workers.md).

1. Deploy the worker node AWS CloudFormation template or create individual EC2 instances on your Outpost.

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2025-11-24/amazon-eks-outpost-nodegroup.yaml
   ```

1. Grant the node instance role access to your cluster. Create an [access entry](access-entries.md) for the node’s IAM role:

   ```
   aws eks create-access-entry \
     --cluster-name my-cluster \
     --principal-arn arn:aws:iam::111122223333:role/myNodeRole \
     --type EC2_LINUX
   ```

   Alternatively, if you are using the `aws-auth` ConfigMap for authentication, add the node instance role to the ConfigMap. See [Grant IAM users and roles access to Kubernetes APIs](grant-k8s-access.md).

1. Verify that your nodes are in `Ready` state:

   ```
   kubectl get nodes
   ```

## Internal resources
<a name="eks-outposts-instance-store-local-cluster-create-internal-resources"></a>

When you create a local cluster, Amazon EKS automatically installs the self-managed versions of the following add-ons in the `kube-system` namespace: `coredns`, `kube-proxy`, and `aws-node` (VPC CNI). You can optionally install the managed versions of these add-ons through the Amazon EKS add-ons API. For more information, see [Amazon EKS add-ons for local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-local-cluster-addons.md).

Amazon EKS also creates cross-account elastic network interfaces (ENIs) in your subnets for cluster-VPC communication. Do not delete these network interfaces. If a cross-account ENI is deleted or its IP address changes, every node and every administrator using static IP-based access must be updated manually.