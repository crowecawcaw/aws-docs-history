

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy Amazon EKS on-premises with AWS Outposts
<a name="eks-outposts"></a>

You can use Amazon EKS to run on-premises Kubernetes applications on AWS Outposts. You can deploy Amazon EKS on Outposts in the following ways:
+  **Extended clusters** – Run the Kubernetes control plane in an AWS Region and nodes on your Outpost.
+  **Local clusters** – Run the Kubernetes control plane and nodes on your Outpost.

For both deployment options, the Kubernetes control plane is fully managed by AWS. You can use the same Amazon EKS APIs, tools, and console that you use in the cloud to create and run Amazon EKS on Outposts.

The following diagram shows these deployment options.

![Outpost deployment options](http://docs.aws.amazon.com/eks/latest/userguide/images/outposts-deployment-options.png)


## When to use each deployment option
<a name="outposts-overview-when-deployment-options"></a>

Both local and extended clusters are general-purpose deployment options and can be used for a range of applications.

With extended clusters, you can conserve capacity on your Outpost because the Kubernetes control plane runs in the parent AWS Region. This option is suitable if you have reliable network connectivity from your Outpost to the AWS Region. It is recommended that you design your applications for static stability through network disconnects from the AWS Region. The way that Kubernetes handles network disconnects between the Kubernetes control plane and nodes might lead to application downtime. For more information on the behavior of Kubernetes, see [Scheduling, Preemption, and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/) in the Kubernetes documentation.

With local clusters, you can run the entire Amazon EKS cluster locally on Outposts. This option can mitigate the risk of application downtime that might result from temporary network disconnects to the cloud. These network disconnects can be caused by fiber cuts or weather events. Because the entire Amazon EKS cluster runs locally on Outposts, applications remain available. You can perform cluster operations during network disconnects to the cloud. Choose local clusters if you require continued Kubernetes operations through network disconnects, or if required by data residency mandates.

## Two local cluster implementations
<a name="outposts-overview-two-local-cluster-implementations"></a>

Amazon EKS supports two local cluster implementations on Outposts racks. An Outpost is configured to use either Amazon EBS or Amazon EC2 instance store as the [root volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html) type for the EC2 instances that run on it. The implementation Amazon EKS uses for your local cluster’s control plane depends on this configuration:
+  ** AWS Outposts configured with Amazon EBS.** The Kubernetes control plane runs in your AWS account on your Outpost, with stacked `etcd` on three Amazon EC2 instances backed by Amazon EBS. For more information, see [Create local Amazon EKS clusters on AWS Outposts for high availability](eks-outposts-local-cluster-overview.md).
+  ** AWS Outposts configured with EC2 instance store.** Amazon EKS deploys an updated local clusters architecture. The Kubernetes control plane runs on 6 Amazon EC2 instances in an AWS-managed service account on your Outpost, with 3 instances dedicated to `etcd` and 3 instances for the other control plane components. The implementation has greater parity with Amazon EKS in the cloud, follows the Amazon EKS Kubernetes version lifecycle, and supports additional features like Amazon EKS add-ons and Bottlerocket-based worker nodes (in addition to AL2023). It is available in all standard AWS Regions where AWS Outposts is available. For more information, see [Overview of local Amazon EKS clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-local-cluster-overview.md).

The features available on each implementation are summarized in the following table.

## Comparing the deployment options
<a name="outposts-overview-comparing-deployment-options"></a>

The following table compares the differences between extended clusters and the two local cluster implementations.


| Feature | Extended cluster | Local cluster on Outposts with EBS | Local cluster on Outposts with EC2 instance store | 
| --- | --- | --- | --- | 
| Kubernetes control plane location |  AWS Region | Outpost | Outpost | 
| Kubernetes control plane account |  AWS account | Your AWS account |  AWS-managed account | 
| Kubernetes control plane topology | Cloud-managed | 3 Amazon EC2 instances, [stacked etcd](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/#stacked-etcd-topology)  | 6 Amazon EC2 instances (3 `etcd` \+ 3 API server) | 
| Control plane storage | Cloud-managed | Amazon EBS | Amazon EC2 instance store | 
| Regional availability | See [Service endpoints](https://docs.aws.amazon.com/general/latest/gr/eks.html#eks_region)  | US East (Ohio), US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Middle East (Bahrain), and South America (São Paulo) | All commercial AWS Regions where AWS Outposts is available | 
| Kubernetes minor versions |  [Supported Amazon EKS versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)  | See [Learn Kubernetes and Amazon EKS platform versions for AWS Outposts](eks-outposts-platform-versions.md)  |  [Supported Amazon EKS versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)  | 
| Platform versions | See [Amazon EKS platform versions](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html)  | See [Learn Kubernetes and Amazon EKS platform versions for AWS Outposts](eks-outposts-platform-versions.md)  | See [Amazon EKS platform versions](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html)  | 
| Outpost form factors | Outpost racks | Outpost racks | Outpost racks | 
| User interfaces |  AWS Management Console, AWS CLI, Amazon EKS API, `eksctl`, AWS CloudFormation, and Terraform |  AWS Management Console, AWS CLI, Amazon EKS API, `eksctl`, AWS CloudFormation, and Terraform |  AWS Management Console, AWS CLI, Amazon EKS API, AWS CloudFormation | 
| Managed policies |  [AmazonEKSClusterPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksclusterpolicy) and [AWS managed policy: AmazonEKSServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksservicerolepolicy)  |  [AmazonEKSLocalOutpostClusterPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy) and [AWS managed policy: AmazonEKSLocalOutpostServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazonekslocaloutpostservicerolepolicy)  |  [AmazonEKSClusterPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksclusterpolicy) and [AWS managed policy: AmazonEKSServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksservicerolepolicy)  | 
| Cluster VPC and subnets | See [View Amazon EKS networking requirements for VPC and subnets](network-reqs.md)  | See [Create a VPC and subnets for Amazon EKS clusters on AWS Outposts](eks-outposts-vpc-subnet-requirements.md)  | See [Create a VPC and subnets for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-vpc-subnet-requirements.md)  | 
| Cluster endpoint access | Public or private or both | Private only | Private or Public and Private | 
| Kubernetes API server authentication |  AWS Identity and Access Management (IAM), OIDC, and access entries | IAM and `x.509` certificates | IAM, OIDC, access entries, `aws-auth` ConfigMap, and `x.509` certificates (for network disconnects) | 
| Node types | Self-managed only | Self-managed only | Self-managed only | 
| Node compute types | Amazon EC2 on-demand | Amazon EC2 on-demand | Amazon EC2 on-demand | 
| Node storage types | Amazon EBS `gp2` and local NVMe SSD | Amazon EBS `gp2` and local NVMe SSD | Local NVMe SSD | 
| Amazon EKS optimized AMIs | Amazon Linux, Windows, and Bottlerocket | Amazon Linux | Amazon Linux and Bottlerocket | 
| IP versions |  `IPv4` only |  `IPv4` only |  `IPv4` only | 
| Add-ons | Amazon EKS add-ons or self-managed add-ons | Self-managed add-ons | Amazon EKS add-ons ([validated list](eks-outposts-instance-store-local-cluster-addons.md)) or self-managed add-ons | 
| Default Container Network Interface | Amazon VPC CNI plugin for Kubernetes | Amazon VPC CNI plugin for Kubernetes | Amazon VPC CNI plugin for Kubernetes | 
| Kubernetes control plane logs | Amazon CloudWatch Logs | Amazon CloudWatch Logs | Amazon CloudWatch Logs | 
|  `etcd` backup | Cloud-managed | Customer-managed (`etcdctl` or Amazon EBS volume backups) | Managed by Amazon EKS | 
| Load balancing | Use the [AWS Load Balancer Controller](aws-load-balancer-controller.md) to provision Application Load Balancers only (no Network Load Balancers) | Use the [AWS Load Balancer Controller](aws-load-balancer-controller.md) to provision Application Load Balancers only (no Network Load Balancers) | Use the [AWS Load Balancer Controller](aws-load-balancer-controller.md) to provision Application Load Balancers only (no Network Load Balancers) | 
| Secrets envelope encryption | Supported, see [Encrypt Kubernetes secrets with KMS on existing clusters](enable-kms.md)  | Not supported | Not supported | 
| IAM Roles for Service Accounts (IRSA) | Supported, see [IAM roles for service accounts](iam-roles-for-service-accounts.md)  | Not supported | Supported (requires connectivity to the AWS Region; not available during network disconnects) | 
| EKS Pod Identity | Supported, see [Learn how EKS Pod Identity grants pods access to AWS services](pod-identities.md)  | Not supported | Supported (requires connectivity to the AWS Region; not available during network disconnects) | 
| Troubleshooting | See [Troubleshoot problems with Amazon EKS clusters and nodes](troubleshooting.md)  | See [Troubleshoot local Amazon EKS clusters on AWS Outposts](eks-outposts-troubleshooting.md)  | See [Troubleshoot local Amazon EKS clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-troubleshooting.md)  | 

**Important**  
Creating a local cluster on a RAM-shared Outpost places the cluster’s control plane under the Outpost owner’s physical access
On EC2 instance store Outposts, IRSA and EKS Pod Identity depend on AWS STS in the AWS Region. During network disconnects, workloads that use IRSA or Pod Identity cannot obtain new credentials. For more information, see [Prepare local Amazon EKS clusters on AWS Outposts configured with EC2 instance store for network disconnects](eks-outposts-instance-store-network-disconnects.md).

**Topics**