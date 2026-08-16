**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Overview of local Amazon EKS clusters on AWS Outposts configured with EC2 instance store

You can use local clusters to run your entire Amazon EKS cluster locally on AWS Outposts. This helps mitigate the risk of application downtime that might result from temporary network disconnects to the cloud and can help address data residency requirements. Because the entire Kubernetes cluster runs locally on Outposts, applications remain available, and you can perform cluster operations during network disconnects from the cloud.

Local clusters are generally available for use with Outposts racks.

## Amazon EKS local clusters with EC2 instance store Outposts

Amazon EKS local clusters supports AWS Outposts configured with EC2 instance store. When you run local clusters on Outposts with EC2 instance store, Amazon EKS deploys an updated local clusters architecture that provides greater parity with Amazon EKS cloud clusters.

The updated architecture used with EC2 instance store-backed Outposts adds the following:

- **Managed control plane.** The Kubernetes control plane runs in an AWS-managed service account on your Outpost. Amazon EKS manages the control plane lifecycle, including Amazon EKS platform version updates and `etcd` backups.
- **Greater feature parity with Amazon EKS in the cloud.** Use [Amazon EKS add-ons](eks-outposts-instance-store-local-cluster-addons.md "eks-outposts-instance-store-local-cluster-addons.md"), [IAM Roles for Service Accounts](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md"), [EKS Pod Identity](pod-identities.md "pod-identities.md"), [OIDC authentication](authenticate-oidc-identity-provider.md "authenticate-oidc-identity-provider.md"), and [Grant IAM users access to Kubernetes with EKS access entries](access-entries.md "access-entries.md"). Use [Bottlerocket](https://aws.amazon.com/bottlerocket/ "https://aws.amazon.com/bottlerocket/") as the worker node operating system, in addition to Amazon Linux 2023-based worker nodes.
- **Aligned with the Amazon EKS Kubernetes version lifecycle.** New Kubernetes versions and Amazon EKS platform versions become available for local clusters on the same cadence as Amazon EKS in the cloud. Extended support Kubernetes versions are available with the same pricing as cloud clusters.
- **Available in all commercial AWS Regions that support AWS Outposts racks.**

###### Note

If your Outpost is configured with Amazon EBS instead of EC2 instance store, the architecture described in this topic isn’t available for your Outpost. Outposts configured with EBS will continue to use the existing local clusters implementation. For more information, see [Create local Amazon EKS clusters on AWS Outposts for high availability](eks-outposts-local-cluster-overview.md "eks-outposts-local-cluster-overview.md").

If you are interested in creating a local cluster on an EBS-backed Outpost using the updated local clusters architecture, contact your AWS account team.

For a feature-by-feature comparison of local clusters and extended clusters, see [Comparing the deployment options](eks-outposts.md#outposts-overview-comparing-deployment-options "eks-outposts.md#outposts-overview-comparing-deployment-options").

## Get started

To create a local cluster on an Outpost configured with EC2 instance store, see [Deploy an Amazon EKS local cluster on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-local-cluster-create.md "eks-outposts-instance-store-local-cluster-create.md").

Before you create a cluster, review:

- [Create a VPC and subnets for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-vpc-subnet-requirements.md "eks-outposts-instance-store-vpc-subnet-requirements.md") — VPC and subnet configuration for local clusters.
- [Select instance types and placement for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-capacity-considerations.md "eks-outposts-instance-store-capacity-considerations.md") — Control plane and `etcd` instance type selection and placement.
- [Prepare local Amazon EKS clusters on AWS Outposts configured with EC2 instance store for network disconnects](eks-outposts-instance-store-network-disconnects.md "eks-outposts-instance-store-network-disconnects.md") — Authentication, observability, and operational considerations during disconnects.
- [Amazon EKS add-ons for local clusters on AWS Outposts configured with EC2 instance store](eks-outposts-instance-store-local-cluster-addons.md "eks-outposts-instance-store-local-cluster-addons.md") — The validated set of Amazon EKS add-ons for local clusters.

###### Topics
