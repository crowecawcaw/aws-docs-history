**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Learn about identity and access in EKS Auto Mode

This topic describes the Identity and Access Management (IAM) roles and permissions required to use EKS Auto Mode. EKS Auto Mode uses two primary IAM roles: a Cluster IAM Role and a Node IAM Role. These roles work in conjunction with EKS Pod Identity and EKS access entries to provide comprehensive access management for your EKS clusters.

When you configure EKS Auto Mode, you will need to set up these IAM roles with specific permissions that allow AWS services to interact with your cluster resources. This includes permissions for managing compute resources, storage volumes, load balancers, and networking components. Understanding these role configurations is essential for proper cluster operation and security.

In EKS Auto Mode, AWS IAM roles are automatically mapped to Kubernetes permissions through EKS access entries, removing the need for manual configuration of `aws-auth` ConfigMaps or custom bindings. When you create a new auto mode cluster, EKS automatically creates the corresponding Kubernetes permissions using Access entries, ensuring that AWS services and cluster components have the appropriate access levels within both the AWS and Kubernetes authorization systems. This automated integration reduces configuration complexity and helps prevent permission-related issues that commonly occur when managing EKS clusters.

## Cluster IAM role

The Cluster IAM role is an AWS Identity and Access Management (IAM) role used by Amazon EKS to manage permissions for Kubernetes clusters. This role grants Amazon EKS the necessary permissions to interact with other AWS services on behalf of your cluster, and is automatically configured with Kubernetes permissions using EKS access entries.

- You must attach AWS IAM policies to this role.
- EKS Auto Mode attaches Kubernetes permissions to this role automatically using EKS access entries.
- With EKS Auto Mode, AWS suggests creating a single Cluster IAM Role per AWS account.
- AWS suggests naming this role `AmazonEKSAutoClusterRole`.
- This role requires permissions for multiple AWS services to manage resources including EBS volumes, Elastic Load Balancers, and EC2 instances.
- The suggested configuration for this role includes multiple AWS managed IAM policies, related to the different capabilities of EKS Auto Mode.
  - `AmazonEKSComputePolicy`
  - `AmazonEKSBlockStoragePolicy`
  - `AmazonEKSLoadBalancingPolicy`
  - `AmazonEKSNetworkingPolicy`
  - `AmazonEKSClusterPolicy`

For more information about the Cluster IAM Role and AWS managed IAM policies, see:

- [AWS managed policies for Amazon Elastic Kubernetes Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Amazon EKS cluster IAM role](cluster-iam-role.md "cluster-iam-role.md")

For more information about Kubernetes access, see:

- [Review access policy permissions](access-policy-permissions.md "access-policy-permissions.md")

## Node IAM role

The Node IAM role is an AWS Identity and Access Management (IAM) role used by Amazon EKS to manage permissions for worker nodes in Kubernetes clusters. This role grants EC2 instances running as Kubernetes nodes the necessary permissions to interact with AWS services and resources, and is automatically configured with Kubernetes RBAC permissions using EKS access entries.

- You must attach AWS IAM policies to this role.
- EKS Auto Mode attaches Kubernetes RBAC permissions to this role automatically using EKS access entries.
- AWS suggests naming this role `AmazonEKSAutoNodeRole`.
- With EKS Auto Mode, AWS suggests creating a single Node IAM Role per AWS account.
- This role has limited permissions. The key permissions include assuming a Pod Identity Role, and pulling images from ECR.
- AWS suggests the following AWS managed IAM policies:
  - `AmazonEKSWorkerNodeMinimalPolicy`
  - `AmazonEC2ContainerRegistryPullOnly`

For more information about the Cluster IAM Role and AWS managed IAM policies, see:

- [AWS managed policies for Amazon Elastic Kubernetes Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Amazon EKS node IAM role](create-node-role.md "create-node-role.md")

For more information about Kubernetes access, see:

- [Review access policy permissions](access-policy-permissions.md "access-policy-permissions.md")

## Service-linked role

Amazon EKS uses a service-linked role (SLR) for certain operations. A service-linked role is a unique type of IAM role that is linked directly to Amazon EKS. Service-linked roles are predefined by Amazon EKS and include all the permissions that the service requires to call other AWS services on your behalf.

AWS automatically creates and configures the SLR. You can delete an SLR only after first deleting their related resources. This protects your Amazon EKS resources because you can’t inadvertently remove permission to access the resources.

The SLR policy grants Amazon EKS permissions to observe and delete core infrastructure components: EC2 resources (instances, network interfaces, security groups), ELB resources (load balancers, target groups), CloudWatch capabilities (logging and metrics), and IAM roles with "eks" prefix. It also enables private endpoint networking through VPC/hosted zone association and includes permissions for EventBridge monitoring and cleanup of EKS-tagged resources.

For more information, see:

- [AWS managed policy: AmazonEKSServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksservicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-amazoneksservicerolepolicy")
- [Service-linked role permissions for Amazon EKS](using-service-linked-roles-eks.md#service-linked-role-permissions-eks "using-service-linked-roles-eks.md#service-linked-role-permissions-eks")

## Custom AWS tags for EKS Auto resources

By default, the managed policies related to EKS Auto Mode do not permit applying user defined tags to Auto Mode provisioned AWS resources. If you want to apply user defined tags to AWS resources, you must attach additional permissions to the Cluster IAM Role with sufficient permissions to create and modify tags on AWS resources. Below is an example of a policy that will allow unrestricted tagging access:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "Compute",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateFleet",
                "ec2:RunInstances",
                "ec2:CreateLaunchTemplate"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/eks:eks-cluster-name": "${aws:PrincipalTag/eks:eks-cluster-name}"
                },
                "StringLike": {
                    "aws:RequestTag/eks:kubernetes-node-class-name": "*",
                    "aws:RequestTag/eks:kubernetes-node-pool-name": "*"
                }
            }
        },
        {
            "Sid": "Storage",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateVolume",
                "ec2:CreateSnapshot"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:volume/*",
                "arn:aws:ec2:*:*:snapshot/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/eks:eks-cluster-name": "${aws:PrincipalTag/eks:eks-cluster-name}"
                }
            }
        },
        {
            "Sid": "Networking",
            "Effect": "Allow",
            "Action": "ec2:CreateNetworkInterface",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/eks:eks-cluster-name": "${aws:PrincipalTag/eks:eks-cluster-name}"
                },
                "StringLike": {
                    "aws:RequestTag/eks:kubernetes-cni-node-name": "*"
                }
            }
        },
        {
            "Sid": "LoadBalancer",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:CreateLoadBalancer",
                "elasticloadbalancing:CreateTargetGroup",
                "elasticloadbalancing:CreateListener",
                "elasticloadbalancing:CreateRule",
                "ec2:CreateSecurityGroup"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/eks:eks-cluster-name": "${aws:PrincipalTag/eks:eks-cluster-name}"
                }
            }
        },
        {
            "Sid": "ShieldProtection",
            "Effect": "Allow",
            "Action": [
                "shield:CreateProtection"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/eks:eks-cluster-name": "${aws:PrincipalTag/eks:eks-cluster-name}"
                }
            }
        },
        {
            "Sid": "ShieldTagResource",
            "Effect": "Allow",
            "Action": [
                "shield:TagResource"
            ],
            "Resource": "arn:aws:shield::*:protection/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/eks:eks-cluster-name": "${aws:PrincipalTag/eks:eks-cluster-name}"
                }
            }
        }
    ]
}
```

## Access Policy Reference

For more information about the Kubernetes permissions used by EKS Auto Mode, see [Review access policy permissions](access-policy-permissions.md "access-policy-permissions.md").
