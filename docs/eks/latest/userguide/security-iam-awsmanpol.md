**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# AWS managed policies for Amazon Elastic Kubernetes Service

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they’re available for all AWS customers to use. We recommend that you reduce permissions further by defining [customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

## AWS managed policy: AmazonEKS_CNI_Policy

You can attach the `AmazonEKS_CNI_Policy` to your IAM entities. Before you create an Amazon EC2 node group, this policy must be attached to either the [node IAM role](create-node-role.md "create-node-role.md"), or to an IAM role that’s used specifically by the Amazon VPC CNI plugin for Kubernetes. This is so that it can perform actions on your behalf. We recommend that you attach the policy to a role that’s used only by the plugin. For more information, see [Assign IPs to Pods with the Amazon VPC CNI](managing-vpc-cni.md "managing-vpc-cni.md") and [Configure Amazon VPC CNI plugin to use IRSA](cni-iam-role.md "cni-iam-role.md").

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- **`ec2:*NetworkInterface` and `ec2:*PrivateIpAddresses`** – Allows the Amazon VPC CNI plugin to perform actions such as provisioning Elastic Network Interfaces and IP addresses for Pods to provide networking for applications that run in Amazon EKS.
- **`ec2` read actions** – Allows the Amazon VPC CNI plugin to perform actions such as describe instances and subnets to see the amount of free IP addresses in your Amazon VPC subnets. The VPC CNI can use the free IP addresses in each subnet to pick the subnets with the most free IP addresses to use when creating an elastic network interface.

To view the latest version of the JSON policy document, see [AmazonEKS_CNI_Policy](../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md#AmazonEKS_CNI_Policy-json "../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md#AmazonEKS_CNI_Policy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSClusterPolicy

You can attach `AmazonEKSClusterPolicy` to your IAM entities. Before creating a cluster, you must have a [cluster IAM role](cluster-iam-role.md "cluster-iam-role.md") with this policy attached. Kubernetes clusters that are managed by Amazon EKS make calls to other AWS services on your behalf. They do this to manage the resources that you use with the service.

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- **`autoscaling`** – Read and update the configuration of an Auto Scaling group. These permissions aren’t used by Amazon EKS but remain in the policy for backwards compatibility.
- **`ec2`** – Work with volumes and network resources that are associated to Amazon EC2 nodes. This is required so that the Kubernetes control plane can join instances to a cluster and dynamically provision and manage Amazon EBS volumes that are requested by Kubernetes persistent volumes.
- **`ec2`** - Delete elastic network interfaces that are created by the VPC CNI. This is required so that EKS can clean up elastic network interfaces that are left behind if the VPC CNI quits unexpectedly.
- **`elasticloadbalancing`** – Work with Elastic Load Balancers and add nodes to them as targets. This is required so that the Kubernetes control plane can dynamically provision Elastic Load Balancers requested by Kubernetes services.
- **`iam`** – Create a service-linked role. This is required so that the Kubernetes control plane can dynamically provision Elastic Load Balancers that are requested by Kubernetes services.
- **`kms`** – Read a key from AWS KMS. This is required for the Kubernetes control plane to support [secrets encryption](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/ "https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/") of Kubernetes secrets stored in `etcd`.

To view the latest version of the JSON policy document, see [AmazonEKSClusterPolicy](../../../aws-managed-policy/latest/reference/AmazonEKSClusterPolicy.md#AmazonEKSClusterPolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSClusterPolicy.md#AmazonEKSClusterPolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSDashboardConsoleReadOnly

You can attach `AmazonEKSDashboardConsoleReadOnly` to your IAM entities.

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- **`eks`** - Read-only access to EKS dashboard data, resources, and cluster versions information. This allows viewing EKS-related metrics and cluster configuration details.
- **`organizations`** - Read-only access to AWS Organizations information, including:
  - Viewing organization details and service access
  - Listing organizational roots, accounts, and organizational units
  - Viewing organization structure

To view the latest version of the JSON policy document, see [AmazonEKSDashboardConsoleReadOnly](../../../aws-managed-policy/latest/reference/AmazonEKSDashboardConsoleReadOnly.md#AmazonEKSDashboardConsoleReadOnly-json "../../../aws-managed-policy/latest/reference/AmazonEKSDashboardConsoleReadOnly.md#AmazonEKSDashboardConsoleReadOnly-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSFargatePodExecutionRolePolicy

You can attach `AmazonEKSFargatePodExecutionRolePolicy` to your IAM entities. Before you can create a Fargate profile, you must create a Fargate Pod execution role and attach this policy to it. For more information, see [Step 2: Create a Fargate Pod execution role](fargate-getting-started.md#fargate-sg-pod-execution-role "fargate-getting-started.md#fargate-sg-pod-execution-role") and [Define which Pods use AWS Fargate when launched](fargate-profile.md "fargate-profile.md").

This policy grants the role the permissions that provide access to other AWS service resources that are required to run Amazon EKS Pods on Fargate.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- **`ecr`** – Allows Pods that are running on Fargate to pull container images that are stored in Amazon ECR.

To view the latest version of the JSON policy document, see [AmazonEKSFargatePodExecutionRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSFargatePodExecutionRolePolicy.md#AmazonEKSFargatePodExecutionRolePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSFargatePodExecutionRolePolicy.md#AmazonEKSFargatePodExecutionRolePolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSConnectorServiceRolePolicy

You can’t attach `AmazonEKSConnectorServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon EKS to perform actions on your behalf. For more information, see [Using roles to connect a Kubernetes cluster to Amazon EKS](using-service-linked-roles-eks-connector.md "using-service-linked-roles-eks-connector.md").

The role allows Amazon EKS to connect Kubernetes clusters. The attached policies allow the role to manage necessary resources to connect to your registered Kubernetes cluster.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks.

- **`SSM Management`** – Create, describe, and delete SSM activations, and deregister managed instances. This allows basic Systems Manager operations.
- **`Session Management`** – Start SSM sessions specifically for EKS clusters and execute non-interactive commands using the AmazonEKS document.
- **`IAM Role Passing`** – Pass IAM roles specifically to the SSM service, controlled by a condition that restricts the passed roles to `ssm.amazonaws.com`.
- **`EventBridge Rules`** – Create EventBridge rules and targets, but only when managed by `eks-connector.amazonaws.com`. Rules are specifically limited to AWS SSM as the event source.

To view the latest version of the JSON policy document, see [AmazonEKSConnectorServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSConnectorServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonEKSConnectorServiceRolePolicy.md") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSForFargateServiceRolePolicy

You can’t attach `AmazonEKSForFargateServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon EKS to perform actions on your behalf. For more information, see `AWSServiceRoleforAmazonEKSForFargate`.

This policy grants necessary permissions to Amazon EKS to run Fargate tasks. The policy is only used if you have Fargate nodes.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks.

- **`ec2`** – Create and delete Elastic Network Interfaces and describe Elastic Network Interfaces and resources. This is required so that the Amazon EKS Fargate service can configure the VPC networking that’s required for Fargate Pods.

To view the latest version of the JSON policy document, see [AmazonEKSForFargateServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSForFargateServiceRolePolicy.md#AmazonEKSForFargateServiceRolePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSForFargateServiceRolePolicy.md#AmazonEKSForFargateServiceRolePolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSComputePolicy

You can attach `AmazonEKSComputePolicy` to your IAM entities. You may attach this policy to your [cluster IAM role](cluster-iam-role.md "cluster-iam-role.md") to expand the resources EKS can manage in your account.

This policy grants the permissions required for Amazon EKS to create and manage EC2 instances for the EKS cluster, and the necessary IAM permissions to configure EC2. Also, this policy grants the permissions for Amazon EKS to create the EC2 Spot service-linked role on your behalf.

### Permissions details

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- **`ec2` Permissions**:
  - `ec2:CreateFleet` and `ec2:RunInstances` - Allows creating EC2 instances and using specific EC2 resources (images, security groups, subnets) for EKS cluster nodes.
  - `ec2:CreateLaunchTemplate` - Allows creating EC2 launch templates for EKS cluster nodes.
  - The policy also includes conditions to restrict the use of these EC2 permissions to resources tagged with the EKS cluster name and other relevant tags.
  - `ec2:CreateTags` - Allows adding tags to EC2 resources created by the `CreateFleet`, `RunInstances`, and `CreateLaunchTemplate` actions.

- **`iam` Permissions**:
  - `iam:AddRoleToInstanceProfile` - Allows adding an IAM role to the EKS compute instance profile.
  - `iam:PassRole` - Allows passing the necessary IAM roles to the EC2 service.

To view the latest version of the JSON policy document, see [AmazonEKSComputePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSComputePolicy.md#AmazonEKSComputePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSComputePolicy.md#AmazonEKSComputePolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSNetworkingPolicy

You can attach `AmazonEKSNetworkingPolicy` to your IAM entities. You may attach this policy to your [cluster IAM role](cluster-iam-role.md "cluster-iam-role.md") to expand the resources EKS can manage in your account.

This policy is designed to grant the necessary permissions for Amazon EKS to create and manage network interfaces for the EKS cluster, allowing the control plane and worker nodes to communicate and function properly.

### Permissions details

This policy grants the following permissions to allow Amazon EKS to manage network interfaces for the cluster:

- **`ec2` Network Interface Permissions**:
  - `ec2:CreateNetworkInterface` - Allows creating EC2 network interfaces.
  - The policy includes conditions to restrict the use of this permission to network interfaces tagged with the EKS cluster name and the Kubernetes CNI node name.
  - `ec2:CreateTags` - Allows adding tags to the network interfaces created by the `CreateNetworkInterface` action.

- **`ec2` Network Interface Management Permissions**:
  - `ec2:AttachNetworkInterface`, `ec2:DetachNetworkInterface` - Allows attaching and detaching network interfaces to EC2 instances.
  - `ec2:UnassignPrivateIpAddresses`, `ec2:UnassignIpv6Addresses`, `ec2:AssignPrivateIpAddresses`, `ec2:AssignIpv6Addresses` - Allows managing the IP address assignments of the network interfaces.
  - These permissions are restricted to network interfaces tagged with the EKS cluster name.

To view the latest version of the JSON policy document, see [AmazonEKSNetworkingPolicy](../../../aws-managed-policy/latest/reference/AmazonEKSNetworkingPolicy.md#AmazonEKSNetworkingPolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSNetworkingPolicy.md#AmazonEKSNetworkingPolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSBlockStoragePolicy

You can attach `AmazonEKSBlockStoragePolicy` to your IAM entities. You may attach this policy to your [cluster IAM role](cluster-iam-role.md "cluster-iam-role.md") to expand the resources EKS can manage in your account.

This policy grants the necessary permissions for Amazon EKS to create, manage, and maintain EC2 volumes and snapshots for the EKS cluster, enabling the control plane and worker nodes to provision and use persistent storage as required by Kubernetes workloads.

### Permissions details

This IAM policy grants the following permissions to allow Amazon EKS to manage EC2 volumes and snapshots:

- **`ec2` Volume Management Permissions**:
  - `ec2:AttachVolume`, `ec2:DetachVolume`, `ec2:ModifyVolume`, `ec2:EnableFastSnapshotRestores` - Allows attaching, detaching, modifying, and enabling fast snapshot restores for EC2 volumes.
  - These permissions are restricted to volumes tagged with the EKS cluster name.
  - `ec2:CreateTags` - Allows adding tags to the EC2 volumes and snapshots created by the `CreateVolume` and `CreateSnapshot` actions.

- **`ec2` Volume Creation Permissions**:
  - `ec2:CreateVolume` - Allows creating new EC2 volumes.
  - The policy includes conditions to restrict the use of this permission to volumes tagged with the EKS cluster name and other relevant tags.
  - `ec2:CreateSnapshot` - Allows creating new EC2 volume snapshots.
  - The policy includes conditions to restrict the use of this permission to snapshots tagged with the EKS cluster name and other relevant tags.

To view the latest version of the JSON policy document, see [AmazonEKSBlockStoragePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSBlockStoragePolicy.md#AmazonEKSBlockStoragePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSBlockStoragePolicy.md#AmazonEKSBlockStoragePolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSLoadBalancingPolicy

You can attach `AmazonEKSLoadBalancingPolicy` to your IAM entities. You may attach this policy to your [cluster IAM role](cluster-iam-role.md "cluster-iam-role.md") to expand the resources EKS can manage in your account.

This IAM policy grants the necessary permissions for Amazon EKS to work with various AWS services to manage Elastic Load Balancers (ELBs) and related resources.

### Permissions details

The key permissions granted by this policy are:

- **`elasticloadbalancing`**: Allows creating, modifying, and managing Elastic Load Balancers and Target Groups. This includes permissions to create, update, and delete load balancers, target groups, listeners, and rules.
- **`ec2`**: Allows creating and managing security groups, which are required for the Kubernetes control plane to join instances to a cluster and manage Amazon EBS volumes. Also allows describing and listing EC2 resources such as instances, VPCs, Subnets, Security Groups, and other networking resources.
- **`iam`**: Allows creating a service-linked role for Elastic Load Balancing, which is required for the Kubernetes control plane to dynamically provision ELBs.
- **`kms`**: Allows reading a key from AWS KMS, which is required for the Kubernetes control plane to support encryption of Kubernetes secrets stored in etcd.
- **`wafv2`** and **`shield`**: Allows associating and disassociating Web ACLs and creating/deleting AWS Shield protections for the Elastic Load Balancers.
- **`cognito-idp`**, **`acm`**, and **`elasticloadbalancing`**: Grants permissions to describe user pool clients, list and describe certificates, and describe target groups, which are required for the Kubernetes control plane to manage the Elastic Load Balancers.

The policy also includes several condition checks to ensure that the permissions are scoped to the specific EKS cluster being managed, using the `eks:eks-cluster-name` tag.

To view the latest version of the JSON policy document, see [AmazonEKSLoadBalancingPolicy](../../../aws-managed-policy/latest/reference/AmazonEKSLoadBalancingPolicy.md#AmazonEKSLoadBalancingPolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSLoadBalancingPolicy.md#AmazonEKSLoadBalancingPolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSMCPReadOnlyAccess

You can attach `AmazonEKSMCPReadOnlyAccess` to your IAM entities. This policy provides read-only access to Amazon EKS resources and related AWS services, enabling the Amazon EKS Model Context Protocol (MCP) Server to perform observability and troubleshooting operations without making any modifications to your infrastructure.

**Permissions details**

This policy includes the following permissions that allow principals to complete the following tasks:

- **`eks`** Allows principals to describe and list EKS clusters, node groups, add-ons, access entries, insights, and access the Kubernetes API for read-only operations.
- **`iam`** Allows principals to retrieve information about IAM roles, policies, and their attachments to understand the permissions associated with EKS resources.
- **`ec2`** Allows principals to describe VPCs, subnets, and route tables to understand the network configuration of EKS clusters.
- **`sts`** Allows principals to retrieve caller identity information for authentication and authorization purposes.
- **`logs`** Allows principals to start queries and retrieve query results from CloudWatch Logs for troubleshooting and monitoring.
- **`cloudwatch`** Allows principals to retrieve metric data for monitoring cluster and workload performance.
- **`eks-mcp`** Allows principals to invoke MCP operations and call read-only tools within the Amazon EKS MCP Server.

To view the latest version of the JSON policy document, see [AmazonEKSMCPReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonEKSMCPReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonEKSMCPReadOnlyAccess.md") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSServicePolicy

You can attach `AmazonEKSServicePolicy` to your IAM entities. Clusters that were created before April 16, 2020, required you to create an IAM role and attach this policy to it. Clusters that were created on or after April 16, 2020, don’t require you to create a role and don’t require you to assign this policy. When you create a cluster using an IAM principal that has the `iam:CreateServiceLinkedRole` permission, the [AWSServiceRoleforAmazonEKS](using-service-linked-roles-eks.md#service-linked-role-permissions-eks "using-service-linked-roles-eks.md#service-linked-role-permissions-eks") service-linked role is automatically created for you. The service-linked role has the [managed policy: AmazonEKSServiceRolePolicy](#security-iam-awsmanpol-amazoneksservicerolepolicy "#security-iam-awsmanpol-amazoneksservicerolepolicy") attached to it.

This policy allows Amazon EKS to create and manage the necessary resources to operate Amazon EKS clusters.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks.

- **`eks`** – Update the Kubernetes version of your cluster after you initiate an update. This permission isn’t used by Amazon EKS but remains in the policy for backwards compatibility.
- **`ec2`** – Work with Elastic Network Interfaces and other network resources and tags. This is required by Amazon EKS to configure networking that facilitates communication between nodes and the Kubernetes control plane. Read information about security groups. Update tags on security groups.
- **`route53`** – Associate a VPC with a hosted zone. This is required by Amazon EKS to enable private endpoint networking for your Kubernetes cluster API server.
- **`logs`** – Log events. This is required so that Amazon EKS can ship Kubernetes control plane logs to CloudWatch.
- **`iam`** – Create a service-linked role. This is required so that Amazon EKS can create the [Service-linked role permissions for Amazon EKS](using-service-linked-roles-eks.md#service-linked-role-permissions-eks "using-service-linked-roles-eks.md#service-linked-role-permissions-eks") service-linked role on your behalf.

To view the latest version of the JSON policy document, see [AmazonEKSServicePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSServicePolicy.md#AmazonEKSServicePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSServicePolicy.md#AmazonEKSServicePolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSServiceRolePolicy

You can’t attach `AmazonEKSServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon EKS to perform actions on your behalf. For more information, see [Service-linked role permissions for Amazon EKS](using-service-linked-roles-eks.md#service-linked-role-permissions-eks "using-service-linked-roles-eks.md#service-linked-role-permissions-eks"). When you create a cluster using an IAM principal that has the `iam:CreateServiceLinkedRole` permission, the [AWSServiceRoleforAmazonEKS](using-service-linked-roles-eks.md#service-linked-role-permissions-eks "using-service-linked-roles-eks.md#service-linked-role-permissions-eks") service-linked role is automatically created for you and this policy is attached to it.

This policy allows the service-linked role to call AWS services on your behalf.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks.

- **`ec2`** – Create and describe Elastic Network Interfaces and Amazon EC2 instances, the cluster security group, and VPC that are required to create a cluster. For more information, see [View Amazon EKS security group requirements for clusters](sec-group-reqs.md "sec-group-reqs.md"). Read information about security groups. Update tags on security groups. Read information about On-Demand Capacity Reservations. Read VPC configuration including route tables and network ACLs to detect configuration issues as part of cluster insights.
- **`ec2` Auto Mode** – Terminate EC2 instances created by EKS Auto Mode. For more information, see [Automate cluster infrastructure with EKS Auto Mode](automode.md "automode.md").
- **`iam`** – List all of the managed policies that attached to an IAM role. This is required so that Amazon EKS can list and validate all managed policies and permissions required to create a cluster.
- **Associate a VPC with a hosted zone** – This is required by Amazon EKS to enable private endpoint networking for your Kubernetes cluster API server.
- **Log event** – This is required so that Amazon EKS can ship Kubernetes control plane logs to CloudWatch.
- **Put metric** – This is required so that Amazon EKS can ship Kubernetes control plane logs to CloudWatch.
- **`eks`** - Manage cluster access entries and policies, allowing fine-grained control over who can access EKS resources and what actions they can perform. This includes associating standard access policies for compute, networking, load balancing, and storage operations.
- **`elasticloadbalancing`** - Create, manage, and delete load balancers and their components (listeners, target groups, certificates) that are associated with EKS clusters. View load balancer attributes and health status.
- **`events`** - Create and manage EventBridge rules for monitoring EC2 and AWS Health events related to EKS clusters, enabling automated responses to infrastructure changes and health alerts.
- **`iam`** - Manage EC2 instance profiles with the "eks" prefix, including creation, deletion, and role association, which is necessary for EKS node management.
- **`pricing`**
  **`shield`** - Access AWS pricing information and Shield protection status, enabling cost management and advanced security features for EKS resources.
- **Resource cleanup** - Safely delete EKS-tagged resources including volumes, snapshots, launch templates, and network interfaces during cluster cleanup operations.

To view the latest version of the JSON policy document, see [AmazonEKSServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSServiceRolePolicy.md#AmazonEKSServiceRolePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSServiceRolePolicy.md#AmazonEKSServiceRolePolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSVPCResourceController

You can attach the `AmazonEKSVPCResourceController` policy to your IAM identities. If you’re using [security groups for Pods](security-groups-for-pods.md "security-groups-for-pods.md"), you must attach this policy to your [Amazon EKS cluster IAM role](cluster-iam-role.md "cluster-iam-role.md") to perform actions on your behalf.

This policy grants the cluster role permissions to manage Elastic Network Interfaces and IP addresses for nodes.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- **`ec2`** – Manage Elastic Network Interfaces and IP addresses to support Pod security groups and Windows nodes.

To view the latest version of the JSON policy document, see [AmazonEKSVPCResourceController](../../../aws-managed-policy/latest/reference/AmazonEKSVPCResourceController.md#AmazonEKSVPCResourceController-json "../../../aws-managed-policy/latest/reference/AmazonEKSVPCResourceController.md#AmazonEKSVPCResourceController-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSWorkerNodePolicy

You can attach the `AmazonEKSWorkerNodePolicy` to your IAM entities. You must attach this policy to a [node IAM role](create-node-role.md "create-node-role.md") that you specify when you create Amazon EC2 nodes that allow Amazon EKS to perform actions on your behalf. If you create a node group using `eksctl`, it creates the node IAM role and attaches this policy to the role automatically.

This policy grants Amazon EKS Amazon EC2 nodes permissions to connect to Amazon EKS clusters.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- **`ec2`** – Read instance volume and network information. This is required so that Kubernetes nodes can describe information about Amazon EC2 resources that are required for the node to join the Amazon EKS cluster.
- **`eks`** – Optionally describe the cluster as part of node bootstrapping.
- **`eks-auth:AssumeRoleForPodIdentity`** – Allow retrieving credentials for EKS workloads on the node. This is required for EKS Pod Identity to function properly.

To view the latest version of the JSON policy document, see [AmazonEKSWorkerNodePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.md#AmazonEKSWorkerNodePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.md#AmazonEKSWorkerNodePolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSWorkerNodeMinimalPolicy

You can attach the AmazonEKSWorkerNodeMinimalPolicy to your IAM entities. You may attach this policy to a node IAM role that you specify when you create Amazon EC2 nodes that allow Amazon EKS to perform actions on your behalf.

This policy grants Amazon EKS Amazon EC2 nodes permissions to connect to Amazon EKS clusters. This policy has fewer permissions compared to AmazonEKSWorkerNodePolicy.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- `eks-auth:AssumeRoleForPodIdentity` - Allow retrieving credentials for EKS workloads on the node. This is required for EKS Pod Identity to function properly.

To view the latest version of the JSON policy document, see [AmazonEKSWorkerNodePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSWorkerNodeMinimalPolicy.md#AmazonEKSWorkerNodeMinimalPolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSWorkerNodeMinimalPolicy.md#AmazonEKSWorkerNodeMinimalPolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AWSServiceRoleForAmazonEKSNodegroup

You can’t attach `AWSServiceRoleForAmazonEKSNodegroup` to your IAM entities. This policy is attached to a service-linked role that allows Amazon EKS to perform actions on your behalf. For more information, see [Service-linked role permissions for Amazon EKS](using-service-linked-roles-eks-nodegroups.md#service-linked-role-permissions-eks-nodegroups "using-service-linked-roles-eks-nodegroups.md#service-linked-role-permissions-eks-nodegroups").

This policy grants the `AWSServiceRoleForAmazonEKSNodegroup` role permissions that allow it to create and manage Amazon EC2 node groups in your account.

**Permissions details**

This policy includes the following permissions that allow Amazon EKS to complete the following tasks:

- **`ec2`** – Work with security groups, tags, capacity reservations, and launch templates. This is required for Amazon EKS managed node groups to enable remote access configuration and to describe capacity reservations that can be used in managed node groups. Additionally, Amazon EKS managed node groups create a launch template on your behalf. This is to configure the Amazon EC2 Auto Scaling group that backs each managed node group.
- **`iam`** – Create a service-linked role and pass a role. This is required by Amazon EKS managed node groups to manage instance profiles for the role being passed when creating a managed node group. This instance profile is used by Amazon EC2 instances launched as part of a managed node group. Amazon EKS needs to create service-linked roles for other services such as Amazon EC2 Auto Scaling groups. These permissions are used in the creation of a managed node group.
- **`autoscaling`** – Work with security Auto Scaling groups. This is required by Amazon EKS managed node groups to manage the Amazon EC2 Auto Scaling group that backs each managed node group. It’s also used to support functionality such as evicting Pods when nodes are terminated or recycled during node group updates.

To view the latest version of the JSON policy document, see [AWSServiceRoleForAmazonEKSNodegroup](../../../aws-managed-policy/latest/reference/AWSServiceRoleForAmazonEKSNodegroup.md#AWSServiceRoleForAmazonEKSNodegroup-json "../../../aws-managed-policy/latest/reference/AWSServiceRoleForAmazonEKSNodegroup.md#AWSServiceRoleForAmazonEKSNodegroup-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSDashboardServiceRolePolicy

You can’t attach `AmazonEKSDashboardServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon EKS to perform actions on your behalf. For more information, see [Service-linked role permissions for Amazon EKS](using-service-linked-roles-eks-dashboard.md#service-linked-role-permissions-eks-dashboard "using-service-linked-roles-eks-dashboard.md#service-linked-role-permissions-eks-dashboard").

This policy grants the `AWSServiceRoleForAmazonEKSDashboard` role permissions that allow it to create and manage Amazon EC2 node groups in your account.

**Permissions details**

This policy includes the following permissions that allow access to complete these tasks:

- **`organizations`** – View information about your AWS Organizations structure and accounts. This includes permissions to list accounts in your organization, view organizational units and roots, list delegated administrators, view services that have access to your organization, and retrieve detailed information about your organization and accounts.

To view the latest version of the JSON policy document, see [AmazonEKSDashboardServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSDashboardServiceRolePolicy.md#AmazonEKSDashboardServiceRolePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSDashboardServiceRolePolicy.md#AmazonEKSDashboardServiceRolePolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEBSCSIDriverPolicy

The `AmazonEBSCSIDriverPolicy` policy allows the Amazon EBS Container Storage Interface (CSI) driver to create, modify, copy, attach, detach, and delete volumes on your behalf. This includes modifying tags on existing volumes and enabling Fast Snapshot Restore (FSR) on EBS volumes. It also grants the EBS CSI driver permissions to create, lock, restore, and delete snapshots, and to list your instances, volumes, and snapshots.

To view the latest version of the JSON policy document, see [AmazonEBSCSIDriverServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.md#AmazonEBSCSIDriverPolicy-json "../../../aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.md#AmazonEBSCSIDriverPolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEFSCSIDriverPolicy

The `AmazonEFSCSIDriverPolicy` policy allows the Amazon EFS Container Storage Interface (CSI) to create and delete access points on your behalf. It also grants the Amazon EFS CSI driver permissions to list your access points file systems, mount targets, and Amazon EC2 availability zones.

To view the latest version of the JSON policy document, see [AmazonEFSCSIDriverServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEFSCSIDriverPolicy.md#AmazonEFSCSIDriverPolicy-json "../../../aws-managed-policy/latest/reference/AmazonEFSCSIDriverPolicy.md#AmazonEFSCSIDriverPolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSLocalOutpostClusterPolicy

You can attach this policy to IAM entities. Before creating a local cluster, you must attach this policy to your [cluster role](cluster-iam-role.md "cluster-iam-role.md"). Kubernetes clusters that are managed by Amazon EKS make calls to other AWS services on your behalf. They do this to manage the resources that you use with the service.

The `AmazonEKSLocalOutpostClusterPolicy` includes the following permissions:

- **`ec2` read actions** – Allows control plane instances to describe Availability Zone, route table, instance, and network interface properties. Required permissions for Amazon EC2 instances to successfully join the cluster as control plane instances.
- **`ssm`** – Allows Amazon EC2 Systems Manager connection to the control plane instance, which is used by Amazon EKS to communicate and manage the local cluster in your account.
- **`logs`** – Allows instances to push logs to Amazon CloudWatch.
- **`secretsmanager`** – Allows instances to get and delete bootstrap data for the control plane instances securely from AWS Secrets Manager.
- **`ecr`** – Allows Pods and containers that are running on the control plane instances to pull container images that are stored in Amazon Elastic Container Registry.

To view the latest version of the JSON policy document, see [AmazonEKSLocalOutpostClusterPolicy](../../../aws-managed-policy/latest/reference/AmazonEKSLocalOutpostClusterPolicy.md#AmazonEKSLocalOutpostClusterPolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSLocalOutpostClusterPolicy.md#AmazonEKSLocalOutpostClusterPolicy-json") in the AWS Managed Policy Reference Guide.

## AWS managed policy: AmazonEKSLocalOutpostServiceRolePolicy

You can’t attach this policy to your IAM entities. When you create a cluster using an IAM principal that has the `iam:CreateServiceLinkedRole` permission, Amazon EKS automatically creates the [AWSServiceRoleforAmazonEKSLocalOutpost](using-service-linked-roles-eks-outpost.md "using-service-linked-roles-eks-outpost.md") service-linked role for you and attaches this policy to it. This policy allows the service-linked role to call AWS services on your behalf for local clusters.

The `AmazonEKSLocalOutpostServiceRolePolicy` includes the following permissions:

- **`ec2`** – Allows Amazon EKS to work with security, network, and other resources to successfully launch and manage control plane instances in your account.
- **`ssm`, `ssmmessages`** – Allows Amazon EC2 Systems Manager connection to the control plane instances, which is used by Amazon EKS to communicate and manage the local cluster in your account.
- **`iam`** – Allows Amazon EKS to manage the instance profile associated with the control plane instances.
- **`secretsmanager`** - Allows Amazon EKS to put bootstrap data for the control plane instances into AWS Secrets Manager so it can be securely referenced during instance bootstrapping.
- **`outposts`** – Allows Amazon EKS to get Outpost information from your account to successfully launch a local cluster in an Outpost.

To view the latest version of the JSON policy document, see [AmazonEKSLocalOutpostServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSLocalOutpostServiceRolePolicy.md#AmazonEKSLocalOutpostServiceRolePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSLocalOutpostServiceRolePolicy.md#AmazonEKSLocalOutpostServiceRolePolicy-json") in the AWS Managed Policy Reference Guide.

## Amazon EKS updates to AWS managed policies

View details about updates to AWS managed policies for Amazon EKS since this service began tracking these changes.

To receive notifications of all source file changes to this specific documentation page, you can subscribe to the following URL with an RSS reader:

```
https://github.com/awsdocs/amazon-eks-user-guide/commits/mainline/latest/ug/security/iam-reference/security-iam-awsmanpol.adoc.atom
```

| Change                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Date              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Added permissions to [AmazonEBSCSIDriverPolicy](#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy "#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy").                                            | Added `ec2:LockSnapshot` permission to allow the EBS CSI Driver to lock EBS Snapshots directly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | January 15, 2026  |
| Introduced [AWS managed policy: AmazonEKSMCPReadOnlyAccess](#security-iam-awsmanpol-amazoneksmcpreadonlyaccess "#security-iam-awsmanpol-amazoneksmcpreadonlyaccess").                                                  | Amazon EKS introduced new managed policy `AmazonEKSMCPReadOnlyAccess` to enable read-only tools in the Amazon EKS MCP Server for observability and troubleshooting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | November 21, 2025 |
| Added permissions to [AmazonEBSCSIDriverPolicy](#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy "#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy").                                            | Added `ec2:CopyVolumes` permission to allow the EBS CSI Driver to copy EBS volumes directly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | November 17, 2025 |
| Added permission to [AWS managed policy: AmazonEKSServiceRolePolicy](#security-iam-awsmanpol-amazoneksservicerolepolicy "#security-iam-awsmanpol-amazoneksservicerolepolicy").                                         | Added `ec2:DescribeRouteTables` and `ec2:DescribeNetworkAcls` permissions to `AmazonEKSServiceRolePolicy`. This allows Amazon EKS to detect configuration issues with VPC route tables and network ACLs for hybrid nodes as part of cluster insights.                                                                                                                                                                                                                                                                                                                                                                                 | Oct 22, 2025      |
| Added permission to [AWSServiceRoleForAmazonEKSConnector](using-service-linked-roles-eks-connector.md "using-service-linked-roles-eks-connector.md")                                                                   | Added `ssmmessages:OpenDataChannel` permission to `AmazonEKSConnectorServiceRolePolicy`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | October 15, 2025  |
| Added permission to [AWS managed policy: AmazonEKSServiceRolePolicy](#security-iam-awsmanpol-amazoneksservicerolepolicy "#security-iam-awsmanpol-amazoneksservicerolepolicy")                                          | This role can attach new access policy `AmazonEKSEventPolicy`. Restricted permissions for `ec2:DeleteLaunchTemplate` and `ec2:TerminateInstances`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | August 26, 2025   |
| Added permission to [AWS managed policy: AmazonEKSLocalOutpostServiceRolePolicy](#security-iam-awsmanpol-amazonekslocaloutpostservicerolepolicy "#security-iam-awsmanpol-amazonekslocaloutpostservicerolepolicy")      | Added `ssmmessages:OpenDataChannel` permission to `AmazonEKSLocalOutpostServiceRolePolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | June 26, 2025     |
| Added permission to [AWS managed policy: AmazonEKSComputePolicy](#security-iam-awsmanpol-AmazonEKSComputePolicy "#security-iam-awsmanpol-AmazonEKSComputePolicy").                                                     | Updated resource permissions for the `ec2:RunInstances` and `ec2:CreateFleet` actions to include capacity reservations `arn:aws:ec2:*:*:capacity-reservation/*`. This allows Amazon EKS Auto Mode to launch instances by using the EC2 On-Demand Capacity Reservations in your account. Added `iam:CreateServiceLinkedRole` to allow Amazon EKS Auto Mode to create the EC2 Spot service-linked role `AWSServiceRoleForEC2Spot` on your behalf.                                                                                                                                                                                       | June 20, 2025     |
| Added permission to [AmazonEKSServiceRolePolicy](#security-iam-awsmanpol-amazoneksservicerolepolicy "#security-iam-awsmanpol-amazoneksservicerolepolicy").                                                             | Added `ec2:DescribeCapacityReservations` permission to allow Amazon EKS Auto Mode to launch instances by using the EC2 On-Demand Capacity Reservations in your account.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | June 20, 2025     |
| Introduced [AWS managed policy: AmazonEKSDashboardConsoleReadOnly](#security-iam-awsmanpol-amazoneksdashboardconsolereadonly "#security-iam-awsmanpol-amazoneksdashboardconsolereadonly").                             | Introduced new `AmazonEKSDashboardConsoleReadOnly` policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | June 19, 2025     |
| Introduced [AWS managed policy: AmazonEKSDashboardServiceRolePolicy](#security-iam-awsmanpol-AmazonEKSDashboardServiceRolePolicy "#security-iam-awsmanpol-AmazonEKSDashboardServiceRolePolicy").                       | Introduced new `AmazonEKSDashboardServiceRolePolicy` policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | May 21, 2025      |
| Added permissions to [AmazonEKSClusterPolicy](#security-iam-awsmanpol-amazoneksclusterpolicy "#security-iam-awsmanpol-amazoneksclusterpolicy").                                                                        | Added `ec2:DeleteNetworkInterfaces` permission to allow Amazon EKS to delete elastic network interfaces that are left behind if the VPC CNI quits unexpectedly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | April 16, 2025    |
| Added permission to [AmazonEKSServiceRolePolicy](#security-iam-awsmanpol-amazoneksservicerolepolicy "#security-iam-awsmanpol-amazoneksservicerolepolicy").                                                             | Added `ec2:RevokeSecurityGroupEgress` and `ec2:AuthorizeSecurityGroupEgress` permissions to allow EKS AI/ML customers to add Security Group Egress rules to the default EKS Cluster SG that are compatible with EFA, as part of the EKS 1.33 version release.                                                                                                                                                                                                                                                                                                                                                                         | April 14, 2025    |
| Added permissions to [AmazonEKSServiceRolePolicy](#security-iam-awsmanpol-amazoneksservicerolepolicy "#security-iam-awsmanpol-amazoneksservicerolepolicy").                                                            | Added permission to terminate EC2 instances created by EKS Auto Mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | February 28, 2025 |
| Added permissions to [AmazonEBSCSIDriverPolicy](#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy "#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy").                                            | Added a new statement authorizing the EBS CSI Driver to restore all snapshots. This was previously allowed by the existing policy but a new explicit statement is required due to a change in the handling of IAM for `CreateVolume`.<br>Added the ability for the EBS CSI Driver to modify tags on existing volumes. The EBS CSI Driver can modify tags of existing volumes via a parameters in Kubernetes VolumeAttributesClasses.<br>Added the ability for the EBS CSI Driver to enable Fast Snapshot Restore (FSR) on EBS volumes. The EBS CSI Driver can enable FSR on new volumes via parameters in Kubernetes storage classes. | January 13, 2025  |
| Added permissions to [AWS managed policy: AmazonEKSLoadBalancingPolicy](#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy "#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy").                                  | Updated `AmazonEKSLoadBalancingPolicy` to allow listing and describing networking and IP address resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | December 26, 2024 |
| Added permissions to [AWS managed policy: AWSServiceRoleForAmazonEKSNodegroup](#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup "#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup").             | Updated `AWSServiceRoleForAmazonEKSNodegroup` for compatibility with China regions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | November 22, 2024 |
| Added permissions to [AWS managed policy: AmazonEKSLocalOutpostClusterPolicy](#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy "#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy")                 | Added `ec2:DescribeAvailabilityZones` permission to `AmazonEKSLocalOutpostClusterPolicy` so the AWS Cloud Controller Manager on the cluster control plane can identify the Availability Zone that each node is in.                                                                                                                                                                                                                                                                                                                                                                                                                    | November 21, 2024 |
| Added permissions to [AWS managed policy: AWSServiceRoleForAmazonEKSNodegroup](#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup "#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup").             | Updated `AWSServiceRoleForAmazonEKSNodegroup` policy to allow `ec2:RebootInstances` for instances created by Amazon EKS managed node groups. Restricted the `ec2:CreateTags` permissions for Amazon EC2 resources.                                                                                                                                                                                                                                                                                                                                                                                                                    | November 20, 2024 |
| Added permissions to [AWS managed policy: AmazonEKSServiceRolePolicy](#security-iam-awsmanpol-amazoneksservicerolepolicy "#security-iam-awsmanpol-amazoneksservicerolepolicy").                                        | EKS updated AWS managed policy `AmazonEKSServiceRolePolicy`. Added permissions for EKS access policies, load balancer management, and automated cluster resource cleanup.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | November 16, 2024 |
| Introduced [AWS managed policy: AmazonEKSComputePolicy](#security-iam-awsmanpol-AmazonEKSComputePolicy "#security-iam-awsmanpol-AmazonEKSComputePolicy").                                                              | EKS updated AWS managed policy `AmazonEKSComputePolicy`. Updated resource permissions for the `iam:AddRoleToInstanceProfile` action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | November 7, 2024  |
| Introduced [AWS managed policy: AmazonEKSComputePolicy](#security-iam-awsmanpol-AmazonEKSComputePolicy "#security-iam-awsmanpol-AmazonEKSComputePolicy").                                                              | AWS introduced the `AmazonEKSComputePolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | November 1, 2024  |
| Added permissions to `AmazonEKSClusterPolicy`                                                                                                                                                                          | Added `ec2:DescribeInstanceTopology` permission to allow Amazon EKS to attach topology information to the node as labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | November 1, 2024  |
| Introduced [AWS managed policy: AmazonEKSBlockStoragePolicy](#security-iam-awsmanpol-AmazonEKSBlockStoragePolicy "#security-iam-awsmanpol-AmazonEKSBlockStoragePolicy").                                               | AWS introduced the `AmazonEKSBlockStoragePolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | October 30, 2024  |
| Introduced [AWS managed policy: AmazonEKSLoadBalancingPolicy](#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy "#security-iam-awsmanpol-AmazonEKSLoadBalancingPolicy").                                            | AWS introduced the `AmazonEKSLoadBalancingPolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | October 30, 2024  |
| Added permissions to [AmazonEKSServiceRolePolicy](#security-iam-awsmanpol-amazoneksservicerolepolicy "#security-iam-awsmanpol-amazoneksservicerolepolicy").                                                            | Added `cloudwatch:PutMetricData` permissions to allow Amazon EKS to publish metrics to Amazon CloudWatch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | October 29, 2024  |
| Introduced [AWS managed policy: AmazonEKSNetworkingPolicy](#security-iam-awsmanpol-AmazonEKSNetworkingPolicy "#security-iam-awsmanpol-AmazonEKSNetworkingPolicy").                                                     | AWS introduced the `AmazonEKSNetworkingPolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | October 28, 2024  |
| Added permissions to `AmazonEKSServicePolicy` and `AmazonEKSServiceRolePolicy`                                                                                                                                         | Added `ec2:GetSecurityGroupsForVpc` and associated tag permissions to allow EKS to read security group information and update related tags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | October 10, 2024  |
| Introduced [AmazonEKSWorkerNodeMinimalPolicy](#security-iam-awsmanpol-AmazonEKSWorkerNodeMinimalPolicy "#security-iam-awsmanpol-AmazonEKSWorkerNodeMinimalPolicy").                                                    | AWS introduced the `AmazonEKSWorkerNodeMinimalPolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | October 3, 2024   |
| Added permissions to [AWSServiceRoleForAmazonEKSNodegroup](#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup "#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup").                                 | Added `autoscaling:ResumeProcesses` and `autoscaling:SuspendProcesses` permissions to allow Amazon EKS to suspend and resume `AZRebalance` in Amazon EKS-managed Auto Scaling groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | August 21, 2024   |
| Added permissions to [AWSServiceRoleForAmazonEKSNodegroup](#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup "#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup").                                 | Added `ec2:DescribeCapacityReservations` permission to allow Amazon EKS to describe capacity reservation in user’s account. Added `autoscaling:PutScheduledUpdateGroupAction` permission to enable setting scheduled scaling on `CAPACITY_BLOCK` node groups.                                                                                                                                                                                                                                                                                                                                                                         | June 27, 2024     |
| [AmazonEKS_CNI_Policy](#security-iam-awsmanpol-amazoneks-cni-policy "#security-iam-awsmanpol-amazoneks-cni-policy") – Update to an existing policy                                                                     | Amazon EKS added new `ec2:DescribeSubnets` permissions to allow the Amazon VPC CNI plugin for Kubernetes to see the amount of free IP addresses in your Amazon VPC subnets. The VPC CNI can use the free IP addresses in each subnet to pick the subnets with the most free IP addresses to use when creating an elastic network interface.                                                                                                                                                                                                                                                                                           | March 4, 2024     |
| [AmazonEKSWorkerNodePolicy](#security-iam-awsmanpol-amazoneksworkernodepolicy "#security-iam-awsmanpol-amazoneksworkernodepolicy") – Update to an existing policy                                                      | Amazon EKS added new permissions to allow EKS Pod Identities. The Amazon EKS Pod Identity Agent uses the node role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | November 26, 2023 |
| Introduced [AmazonEFSCSIDriverPolicy](#security-iam-awsmanpol-amazonefscsidriverservicerolepolicy "#security-iam-awsmanpol-amazonefscsidriverservicerolepolicy").                                                      | AWS introduced the `AmazonEFSCSIDriverPolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | July 26, 2023     |
| Added permissions to [AmazonEKSClusterPolicy](#security-iam-awsmanpol-amazoneksclusterpolicy "#security-iam-awsmanpol-amazoneksclusterpolicy").                                                                        | Added `ec2:DescribeAvailabilityZones` permission to allow Amazon EKS to get the AZ details during subnet auto-discovery while creating load balancers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | February 7, 2023  |
| Updated policy conditions in [AmazonEBSCSIDriverPolicy](#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy "#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy").                                    | Removed invalid policy conditions with wildcard characters in the `StringLike` key field. Also added a new condition `ec2:ResourceTag/kubernetes.io/created-for/pvc/name: "*"` to `ec2:DeleteVolume`, which allows the EBS CSI driver to delete volumes created by the in-tree plugin.                                                                                                                                                                                                                                                                                                                                                | November 17, 2022 |
| Added permissions to [AmazonEKSLocalOutpostServiceRolePolicy](#security-iam-awsmanpol-amazonekslocaloutpostservicerolepolicy "#security-iam-awsmanpol-amazonekslocaloutpostservicerolepolicy").                        | Added `ec2:DescribeVPCAttribute`, `ec2:GetConsoleOutput` and `ec2:DescribeSecret` to allow better prerequisite validation and managed lifecycle control. Also added `ec2:DescribePlacementGroups` and `"arn:aws:ec2:*:*:placement-group/*"` to `ec2:RunInstances` to support placement control of the control plane Amazon EC2 instances on Outposts.                                                                                                                                                                                                                                                                                 | October 24, 2022  |
| Update Amazon Elastic Container Registry permissions in [AmazonEKSLocalOutpostClusterPolicy](#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy "#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy"). | Moved action `ecr:GetDownloadUrlForLayer` from all resource sections to a scoped section. Added resource `arn:aws:ecr:*:*:repository/eks/`. Removed resource `arn:aws:ecr:`. This resource is covered by the added `arn:aws:ecr:*:*:repository/eks/*` resource.                                                                                                                                                                                                                                                                                                                                                                       | October 20, 2022  |
| Added permissions to [AmazonEKSLocalOutpostClusterPolicy](#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy "#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy").                                    | Added the `arn:aws:ecr:*:*:repository/kubelet-config-updater` Amazon Elastic Container Registry repository so the cluster control plane instances can update some `kubelet` arguments.                                                                                                                                                                                                                                                                                                                                                                                                                                                | August 31, 2022   |
| Introduced [AmazonEKSLocalOutpostClusterPolicy](#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy "#security-iam-awsmanpol-amazonekslocaloutpostclusterpolicy").                                              | AWS introduced the `AmazonEKSLocalOutpostClusterPolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | August 24, 2022   |
| Introduced [AmazonEKSLocalOutpostServiceRolePolicy](#security-iam-awsmanpol-amazonekslocaloutpostservicerolepolicy "#security-iam-awsmanpol-amazonekslocaloutpostservicerolepolicy").                                  | AWS introduced the `AmazonEKSLocalOutpostServiceRolePolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | August 23, 2022   |
| Introduced [AmazonEBSCSIDriverPolicy](#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy "#security-iam-awsmanpol-amazonebscsidriverservicerolepolicy").                                                      | AWS introduced the `AmazonEBSCSIDriverPolicy`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | April 4, 2022     |
| Added permissions to [AmazonEKSWorkerNodePolicy](#security-iam-awsmanpol-amazoneksworkernodepolicy "#security-iam-awsmanpol-amazoneksworkernodepolicy").                                                               | Added `ec2:DescribeInstanceTypes` to enable Amazon EKS-optimized AMIs that can auto discover instance level properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | March 21, 2022    |
| Added permissions to [AWSServiceRoleForAmazonEKSNodegroup](#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup "#security-iam-awsmanpol-awsserviceroleforamazoneksnodegroup").                                 | Added `autoscaling:EnableMetricsCollection` permission to allow Amazon EKS to enable metrics collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | December 13, 2021 |
| Added permissions to [AmazonEKSClusterPolicy](#security-iam-awsmanpol-amazoneksclusterpolicy "#security-iam-awsmanpol-amazoneksclusterpolicy").                                                                        | Added `ec2:DescribeAccountAttributes`, `ec2:DescribeAddresses`, and `ec2:DescribeInternetGateways` permissions to allow Amazon EKS to create a service-linked role for a Network Load Balancer.                                                                                                                                                                                                                                                                                                                                                                                                                                       | June 17, 2021     |
| Amazon EKS started tracking changes.                                                                                                                                                                                   | Amazon EKS started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | June 17, 2021     |
