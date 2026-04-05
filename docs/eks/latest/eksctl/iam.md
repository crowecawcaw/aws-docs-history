# IAM

This chapter includes information about working with AWS IAM.

## Topics:

- [Manage IAM users and roles](iam-identity-mappings.md "iam-identity-mappings.md")
  - Manage IAM user and role mappings to control access to an EKS cluster
  - Configure IAM identity mappings through the cluster config file or CLI commands

- [IAM Roles for Service Accounts](iamserviceaccounts.md "iamserviceaccounts.md")
  - Manage fine-grained permissions for applications running on Amazon EKS that use other AWS services
  - Create and configure IAM Roles and Kubernetes Service Account pairs using eksctl
  - Enable IAM OpenID Connect Provider for an EKS cluster to enable IAM Roles for Service Accounts

- [IAM permissions boundary](iam-permissions-boundary.md "iam-permissions-boundary.md")
  - Control the maximum permissions granted to IAM entities (users or roles) by setting a permissions boundary

- [EKS Pod Identity Associations](pod-identity-associations.md "pod-identity-associations.md")
  - Configure IAM permissions for EKS add-ons using recommended pod identity associations
  - Enable Kubernetes applications to receive required IAM permissions to connect with AWS services outside the cluster
  - Simplify the process of automating IAM roles and service accounts across multiple EKS clusters

- [IAM policies](iam-policies.md "iam-policies.md")
  - Manage IAM policies for EKS node groups, including support for various add-on policies like image builder, auto scaler, external DNS, cert manager, and more.
  - Attach custom instance roles or inline policies to node groups for additional permissions.
  - Attach specific AWS managed policies by ARN to node groups, ensuring required policies like AmazonEKSWorkerNodePolicy and AmazonEKS_CNI_Policy are included.

- [Minimum IAM policies](minimum-iam-policies.md "minimum-iam-policies.md")
  - Manage AWS EC2 resources, including load balancers, auto-scaling groups, and CloudWatch monitoring
  - Create and manage AWS CloudFormation stacks
  - Manage Amazon Elastic Kubernetes Service (EKS) clusters, node groups, and related resources like IAM roles and policies
