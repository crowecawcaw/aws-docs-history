**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an access entry using Kubernetes groups with the AWS CLI

Create Amazon EKS access entries that use Kubernetes groups for authorization and require manual RBAC configuration.

###### Note

For most use cases, we recommend using EKS Access Policies instead of the Kubernetes groups approach described on this page. EKS Access Policies provide a simpler, more AWS-integrated way to manage access without requiring manual RBAC configuration. Use the Kubernetes groups approach only when you need more granular control than what EKS Access Policies offer.

## Overview

Access entries define how IAM identities (users and roles) access your Kubernetes clusters. The Kubernetes groups approach grants IAM users or roles permission to access your EKS cluster through standard Kubernetes RBAC groups. This method requires creating and managing Kubernetes RBAC resources (Roles, RoleBindings, ClusterRoles, and ClusterRoleBindings) and is recommended when you need highly customized permission sets, complex authorization requirements, or want to maintain consistent access control patterns across hybrid Kubernetes environments.

This topic does not cover creating access entries for IAM identities used for Amazon EC2 instances to join EKS clusters.

## Prerequisites

- The _authentication mode_ of your cluster must be configured to enable _access entries_. For more information, see [Change authentication mode to use access entries](setting-up-access-entries.md "setting-up-access-entries.md").
- Install and configure the AWS CLI, as described in [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the AWS Command Line Interface User Guide.
- Familiarity with Kubernetes RBAC is recommended. For more information, see [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "https://kubernetes.io/docs/reference/access-authn-authz/rbac/") in the Kubernetes documentation.

## Step 1: Define access entry

1. Find the ARN of the IAM identity, such as a user or role, that you want to grant permissions to.
   - Each IAM identity can have only one EKS access entry.

2. Determine which Kubernetes groups you want to associate with this IAM identity.
   - You will need to create or use existing Kubernetes `Role`/`ClusterRole` and `RoleBinding`/`ClusterRoleBinding` resources that reference these groups.

3. Determine if the auto-generated username is appropriate for the access entry, or if you need to manually specify a username.
   - AWS auto-generates this value based on the IAM identity. You can set a custom username. This is visible in Kubernetes logs.
   - For more information, see [Set a custom username for EKS access entries](set-custom-username.md "set-custom-username.md").

## Step 2: Create access entry with Kubernetes groups

After planning the access entry, use the AWS CLI to create it with the appropriate Kubernetes groups.

```
aws eks create-access-entry --cluster-name <cluster-name> --principal-arn <iam-identity-arn> --type STANDARD --kubernetes-groups <groups>
```

Replace:

- `<cluster-name>` with your EKS cluster name
- `<iam-identity-arn>` with the ARN of the IAM user or role
- `<groups>` with a comma-separated list of Kubernetes groups (e.g., "system:developers,system:readers")

[View the CLI reference for all configuration options](../../../cli/latest/reference/eks/create-access-entry.md "../../../cli/latest/reference/eks/create-access-entry.md").

## Step 3: Configure Kubernetes RBAC

For the IAM principal to have access to Kubernetes objects on your cluster, you must create and manage Kubernetes role-based access control (RBAC) objects:

1. Create Kubernetes `Role` or `ClusterRole` objects that define the permissions.
2. Create Kubernetes `RoleBinding` or `ClusterRoleBinding` objects on your cluster that specify the group name as a `subject` for `kind: Group`.

For detailed information about configuring groups and permissions in Kubernetes, see [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "https://kubernetes.io/docs/reference/access-authn-authz/rbac/") in the Kubernetes documentation.

## Next steps

- [Create a kubeconfig so you can use kubectl with an IAM identity](create-kubeconfig.md "create-kubeconfig.md")
