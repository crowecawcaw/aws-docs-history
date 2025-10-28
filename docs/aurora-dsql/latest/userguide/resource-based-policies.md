# Resource-based policies for Aurora DSQL

Use resource-based policies for Aurora DSQL to restrict or grant access to your
clusters through JSON policy documents that attach directly to your cluster resources.
These policies provide fine-grained control over who can access your cluster and under
what conditions.

Aurora DSQL clusters are accessible from the public internet by default, with IAM
authentication as the primary security control. Resource-based policies enable you to
add access restrictions, particularly to block access from the public
internet.

Resource-based policies work alongside IAM identity-based policies. AWS evaluates
both types of policies to determine the final permissions for any access request to your
cluster. By default, Aurora DSQL clusters are accessible within an account. If an IAM user or role
has Aurora DSQL permissions, they can access clusters with no resource-based policy attached.

###### Note

Changes to resource-based policies are eventually consistent and typically take effect within one minute.

For more information about the differences between identity-based and resource-based policies, see [Identity-based policies and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the _IAM User Guide_.

## When to use resource-based policies

Resource-based policies are particularly useful in these scenarios:

- _Network-based access control_ — Restrict access based on the VPC or IP address that requests originate from, or block public internet access entirely. Use condition keys like `aws:SourceVpc` and `aws:SourceIp` to control network access.
- _Multiple teams or applications_ — Grant access to the same cluster for multiple teams or applications. Rather than managing individual IAM policies for each principal, you define access rules once on the cluster.
- _Complex conditional access_ — Control access based on multiple factors like network attributes, request context, and user attributes. You can combine multiple conditions in a single policy.
- _Centralized security governance_ — Enable cluster owners to control access using familiar AWS policy syntax that integrates with your existing security practices.

###### Note

Cross-account access is not yet supported for Aurora DSQL resource-based policies but will be available in future releases.

When someone tries to connect to your Aurora DSQL cluster, AWS evaluates your resource-based policy as part of the authorization context, along with any relevant IAM policies, to determine whether the request should be allowed or rejected.

Resource-based policies can grant access to principals within the same AWS
account as the cluster. For multi-Region clusters, each regional cluster has its own
resource-based policy, allowing for Region-specific access controls when
needed.

###### Note

Condition context keys may vary between Regions (such as VPC IDs).

###### Topics

- [Create with policies](rbp-create-cluster.md "rbp-create-cluster.md")
- [Add and edit policies](rbp-attach-policy.md "rbp-attach-policy.md")
- [View Policy](rbp-view-policy.md "rbp-view-policy.md")
- [Remove Policy](rbp-remove-policy.md "rbp-remove-policy.md")
- [Policy examples](rbp-examples.md "rbp-examples.md")
- [Block public access](rbp-block-public-access.md "rbp-block-public-access.md")
- [API Operations](rbp-api-operations.md "rbp-api-operations.md")
