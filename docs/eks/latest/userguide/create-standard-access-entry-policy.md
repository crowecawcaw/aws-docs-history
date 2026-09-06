

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an access entry for an IAM role or user using an access policy and the AWS CLI
<a name="create-standard-access-entry-policy"></a>

Create Amazon EKS access entries that use AWS-managed EKS access policies to grant IAM identities standardized permissions for accessing and managing Kubernetes clusters.

## Overview
<a name="_overview"></a>

Access entries in Amazon EKS define how IAM identities (users and roles) can access and interact with your Kubernetes clusters. By creating access entries with EKS access policies, you can:
+ Grant specific IAM users or roles permission to access your EKS cluster
+ Control permissions using AWS-managed EKS access policies that provide standardized, predefined permission sets
+ Scope permissions to specific namespaces or cluster-wide
+ Simplify access management without modifying the `aws-auth` ConfigMap or creating Kubernetes RBAC resources
+ Use AWS-integrated approach to Kubernetes access control that covers common use cases while maintaining security best practices

This approach is recommended for most use cases because it provides AWS-managed, standardized permissions without requiring manual Kubernetes RBAC configuration. EKS access policies eliminate the need to manually configure Kubernetes RBAC resources and offer predefined permission sets that cover common use cases.

## Prerequisites
<a name="_prerequisites"></a>
+ The *authentication mode* of your cluster must be configured to enable *access entries*. For more information, see [Change authentication mode to use access entries](setting-up-access-entries.md).
+ Install and configure the AWS CLI, as described in [Installing](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the AWS Command Line Interface User Guide.

## Step 1: Define access entry
<a name="ap1-s1"></a>

1. Find the ARN of IAM identity, such as a user or role, that you want to grant permissions to.
   + Each IAM identity can have only one EKS access entry.

1. Determine if you want the Amazon EKS access policy permissions to apply to only a specific Kubernetes namespace, or across the entire cluster.
   + If you want to limit the permissions to a specific namespace, make note of the namespace name.

1. Select the EKS access policy you want for the IAM identity. This policy gives in-cluster permissions. Note the ARN of the policy.
   + For a list of policies, see [available access policies](access-policy-permissions.md).

1. Determine if the auto-generated username is appropriate for the access entry, or if you need to manually specify a username.
   +  AWS auto-generates this value based on the IAM identity. You can set a custom username. This is visible in Kubernetes logs.
   + For more information, see [Set a custom username for EKS access entries](set-custom-username.md).

## Step 2: Create access entry
<a name="ap1-s2"></a>

After planning the access entry, use the AWS CLI to create it.

The following example covers most use cases. [View the CLI reference for all configuration options](https://docs.aws.amazon.com/cli/latest/reference/eks/create-access-entry.html).

You will attach the access policy in the next step.

```
aws eks create-access-entry --cluster-name <cluster-name> --principal-arn <iam-identity-arn> --type STANDARD
```

## Step 3: Associate access policy
<a name="_step_3_associate_access_policy"></a>

The command differs based on whether you want the policy to be limited to a specified Kubernetes namespace.

You need the ARN of the access policy. Review the [available access policies](access-policy-permissions.md).

### Create policy without namespace scope
<a name="_create_policy_without_namespace_scope"></a>

```
aws eks associate-access-policy --cluster-name <cluster-name> --principal-arn <iam-identity-arn> --access-scope type=cluster --policy-arn <access-policy-arn>
```

### Create with namespace scope
<a name="_create_with_namespace_scope"></a>

```
aws eks associate-access-policy --cluster-name <cluster-name> --principal-arn <iam-identity-arn> \
    --access-scope type=namespace,namespaces=my-namespace1,my-namespace2 --policy-arn <access-policy-arn>
```

## Next steps
<a name="_next_steps"></a>
+  [Create a kubeconfig so you can use kubectl with an IAM identity](create-kubeconfig.md) 