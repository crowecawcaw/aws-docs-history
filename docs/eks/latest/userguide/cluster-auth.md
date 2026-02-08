**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Learn how access control works in Amazon EKS

Learn how to manage access to your Amazon EKS cluster. Using Amazon EKS requires knowledge of how both Kubernetes and AWS Identity and Access Management (AWS IAM) handle access control.

**This section includes:**

**[Grant IAM users and roles access to Kubernetes APIs](grant-k8s-access.md "grant-k8s-access.md")** — Learn how to enable applications or users to authenticate to the Kubernetes API. You can use access entries, the aws-auth ConfigMap, or an external OIDC provider.

**[View Kubernetes resources in the AWS Management Console](view-kubernetes-resources.md "view-kubernetes-resources.md")** — Learn how to configure the AWS Management Console to communicate with your Amazon EKS cluster. Use the console to view Kubernetes resources in the cluster, such as namespaces, nodes, and Pods.

**[Grant AWS services write access to Kubernetes APIs](mutate-kubernetes-resources.md "mutate-kubernetes-resources.md")** — Learn about the permissions required to modify Kubernetes resources.

**[Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md")** — Learn how to configure kubectl to communicate with your Amazon EKS cluster. Use the AWS CLI to create a kubeconfig file.

**[Grant Kubernetes workloads access to AWS using Kubernetes Service Accounts](service-accounts.md "service-accounts.md")** — Learn how to associate a Kubernetes service account with AWS IAM Roles. You can use Pod Identity or IAM Roles for Service Accounts (IRSA).

## Common Tasks

- Grant developers access to the Kubernetes API. View Kubernetes resources in the AWS Management Console.
  - Solution: [Use access entries](access-entries.md "access-entries.md") to associate Kubernetes RBAC permissions with AWS IAM Users or Roles.

- Configure kubectl to talk to an Amazon EKS cluster using AWS Credentials.
  - Solution: Use the AWS CLI to [create a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md").

- Use an external identity provider, such as Ping Identity, to authenticate users to the Kubernetes API.
  - Solution: [Link an external OIDC provider](authenticate-oidc-identity-provider.md "authenticate-oidc-identity-provider.md").

- Grant workloads on your Kubernetes cluster the ability to call AWS APIs.
  - Solution: [Use Pod Identity](pod-identities.md "pod-identities.md") to associate an AWS IAM Role to a Kubernetes Service Account.

## Background

- [Learn how Kubernetes Service Accounts work.](https://kubernetes.io/docs/concepts/security/service-accounts/ "https://kubernetes.io/docs/concepts/security/service-accounts/")
- [Review the Kubernetes Role Based Access Control (RBAC) Model](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "https://kubernetes.io/docs/reference/access-authn-authz/rbac/")
- For more information about managing access to AWS resources, see the [AWS IAM User Guide](../../../IAM/latest/UserGuide/intro-structure.md "../../../IAM/latest/UserGuide/intro-structure.md"). Alternatively, take a free [introductory training on using AWS IAM](https://explore.skillbuilder.aws/learn/course/external/view/elearning/120/introduction-to-aws-identity-and-access-management-iam "https://explore.skillbuilder.aws/learn/course/external/view/elearning/120/introduction-to-aws-identity-and-access-management-iam").

## Considerations for EKS Auto Mode

EKS Auto Mode integrates with EKS Pod Identity and EKS EKS access entries.

- EKS Auto Mode uses access entries to grant the EKS control plane Kubernetes permissions. For example, the access policies enable EKS Auto Mode to read information about network endpoints and services.
  - You cannot disable access entries on an EKS Auto Mode cluster.
  - You can optionally enable the `aws-auth`
    `ConfigMap`.
  - The access entries for EKS Auto Mode are automatically configured. You can view these access entries, but you cannot modify them.
  - If you use a NodeClass to create a custom Node IAM Role, you need to create an access entry for the role using the AmazonEKSAutoNodePolicy access policy.

- If you want to grant workloads permissions for AWS services, use EKS Pod Identity.
  - You do not need to install the Pod Identity agent on EKS Auto Mode clusters.
