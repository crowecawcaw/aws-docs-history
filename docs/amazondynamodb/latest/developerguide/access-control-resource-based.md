# Using resource-based policies for DynamoDB

DynamoDB supports resource-based policies for tables, indexes, and streams. Resource-based
policies let you define access permissions by specifying who has access to each resource, and
the actions they are allowed to perform on each resource.

You can attach a resource-based policy to DynamoDB resources, such as a table or a stream. In
this policy, you specify permissions for Identity and Access Management (IAM) [principals](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal") that can perform speciﬁc actions on these DynamoDB resources. For example,
the policy attached to a table will contain permissions for access to the table and its indexes.
As a result, resource-based policies can help you simplify access control for your DynamoDB tables,
indexes, and streams, by defining permissions at the resource level. The maximum size of a
policy you can attach to a DynamoDB resource is 20 KB.

A significant benefit of using resource-based policies is to simplify cross-account access
control for providing cross-account access to IAM principals in different AWS accounts. For
more information, see [Resource-based policy for cross-account
access](rbac-examples.md#rbac-examples-cross-account "rbac-examples.md#rbac-examples-cross-account").

Resource-based policies also support integrations with [IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") external access
analyzer and [Block Public Access (BPA)](rbac-bpa-rbp.md "rbac-bpa-rbp.md") capabilities.
IAM Access Analyzer reports cross-account access to external entities specified in resource-based
policies. It also provides visibility to help you refine permissions and conform to the least
privilege principle. BPA helps you prevent public access to your DynamoDB tables, indexes, and
streams, and is automatically enabled in the resource-based policies creation and modification
workflows.

###### Topics

- [Create a table with a resource-based policy](rbac-create-table.md "rbac-create-table.md")
- [Attach a policy to an DynamoDB existing
  table](rbac-attach-resource-based-policy.md "rbac-attach-resource-based-policy.md")
- [Attach a resource-based policy to a
  DynamoDB stream](rbac-attach-resource-policy-streams.md "rbac-attach-resource-policy-streams.md")
- [Remove a resource-based policy from a
  DynamoDB table](rbac-delete-resource-based-policy.md "rbac-delete-resource-based-policy.md")
- [Cross-account access with resource-based policies
  in DynamoDB](rbac-cross-account-access.md "rbac-cross-account-access.md")
- [Blocking public access with resource-based policies in
  DynamoDB](rbac-bpa-rbp.md "rbac-bpa-rbp.md")
- [DynamoDB API operations supported by resource-based
  policies](rbac-iam-actions.md "rbac-iam-actions.md")
- [Authorization with IAM identity-based
  policies and DynamoDB resource-based policies](rbac-auth-iam-id-based-policies-DDB.md "rbac-auth-iam-id-based-policies-DDB.md")
- [DynamoDB resource-based policy examples](rbac-examples.md "rbac-examples.md")
- [DynamoDB resource-based policy considerations](rbac-considerations.md "rbac-considerations.md")
- [DynamoDB resource-based policy best practices](rbac-best-practices.md "rbac-best-practices.md")
