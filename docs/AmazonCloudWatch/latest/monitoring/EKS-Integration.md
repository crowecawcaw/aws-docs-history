# Integration with Amazon EKS

CloudWatch investigations investigation groups can utilize information directly from your Amazon EKS cluster. To
get started, first grant access to the `Investigation Group` IAM role. We
recommend using the default AWS managed _access
policy_
`AmazonAIOpsAssistantPolicy` that grants CloudWatch investigations investigation groups access to
resources in the cluster. By using this policy you will automatically get policy updates
as needed.

###### Note

`AmazonAIOpsAssistantPolicy` is an access policy. The AWS managed
identity policy that authorizes the access associated with CloudWatch investigations investigation groups
is [`AIOpsAssistantPolicy`](../../../aws-managed-policy/latest/reference/AIOpsAssistantPolicy.md "../../../aws-managed-policy/latest/reference/AIOpsAssistantPolicy.md").

Use the **Advanced Configuration** option to scope down
the access provided by the access policy to a set of namespaces or the entire cluster.
Alternatively, you can further scope access down by associating the access entry to a
Kubernetes group RBAC permission. For more information, see [Creating access entries](../../../eks/latest/userguide/creating-access-entries.md "../../../eks/latest/userguide/creating-access-entries.md").

## Configuring the Amazon EKS access entry (Console)

To associate the `AmazonAIOpsAssistantPolicy` to the investigation role
using the AWS Management Console, follow these steps:

1. Open the CloudWatch console and navigate to the Investigations Configuration
   page.
2. In the Amazon EKS Access section, select the option to associate the
   `AmazonAIOpsAssistantPolicy` with your investigation
   role.
3. Review the policy details and confirm the association.

To further customize the access scope:

1. Click **Advanced Configuration** in the Amazon EKS Access
   section.
2. You will be redirected to the Amazon EKS console.
3. In the Amazon EKS console, you can:
   1. Scope the policy to specific namespaces
   2. Configure the group feature for more granular access
      control

## Configuring Amazon EKS Access Entries (CDK)

To configure Amazon EKS Access Entries using the AWS CDK, use the following code
example:

```

    const testAccessEntry = new AccessEntry(this, `test-access-entry`, {
        cluster: eksCluster,
        principal: investigationsIamRole.roleArn,
        accessPolicies: [
            AccessPolicy.fromAccessPolicyName('AmazonAIOpsAssistantPolicy', {
                accessScopeType: AccessScopeType.CLUSTER
            }),
        ],
    });

```

## AmazonAIOpsAssistantPolicy

The Amazon EKS Access Policy, `AmazonAIOpsAssistantPolicy`, provides
comprehensive Read Only access to resources in the cluster. Information from each
resource may not be currently utilized by CloudWatch investigations.

```

    - apiGroups: [""]
      resources:
        - pods
        - pods/log
        - services
        - nodes
        - namespaces
        - events
        - persistentvolumes
        - persistentvolumeclaims
        - configmaps
      verbs:
        - get
        - list

    - apiGroups: ["apps"]
      resources:
        - deployments
        - replicasets
        - statefulsets
        - daemonsets
      verbs:
        - get
        - list

    - apiGroups: ["batch"]
      resources:
        - jobs
        - cronjobs
      verbs:
        - get
        - list

    - apiGroups: ["events.k8s.io"]
      resources:
        - events
      verbs:
        - get
        - list

    - apiGroups: ["networking.k8s.io"]
      resources:
        - ingresses
        - ingressclasses
      verbs:
        - get
        - list

    - apiGroups: ["storage.k8s.io"]
      resources:
        - storageclasses
      verbs:
        - get
        - list

    - apiGroups: ["metrics.k8s.io"]
      resources:
        - pods
        - nodes
      verbs:
        - get
        - list

```

## Updates to AmazonAIOpsAssistantPolicy

| Change                                   | Description                                        | Date           |
| ---------------------------------------- | -------------------------------------------------- | -------------- |
| Add policy for CloudWatch investigations | Initial release of<br>`AmazonAIOpsAssistantPolicy` | August 9, 2025 |
