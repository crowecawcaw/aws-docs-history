# AWS Glue access control policy examples

This section contains examples of both identity-based (IAM) access control policies
and AWS Glue resource policies.

###### Contents

- [Identity-based policy examples
  for AWS Glue](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
  - [Policy best
    practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices "security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices")
  - [Resource-level permissions
    only apply to specific AWS Glue objects](security_iam_id-based-policy-examples.md#glue-identity-based-policy-limitations "security_iam_id-based-policy-examples.md#glue-identity-based-policy-limitations")
  - [Using the AWS Glue
    console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console")
  - [Allow
    users to view their own permissions](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-own-permissions "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-own-permissions")
  - [Grant read-only permission to a table](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-read-only-table-access "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-read-only-table-access")
  - [Filter tables by GetTables permission](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-filter-tables "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-filter-tables")
  - [Grant full access to a table and all partitions](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-full-access-tables-partitions "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-full-access-tables-partitions")
  - [Control access by name prefix and explicit denial](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-deny-by-name-prefix "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-deny-by-name-prefix")
  - [Grant access using
    tags](security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-allow "security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-allow")
  - [Deny access using
    tags](security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-deny "security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-deny")
  - [Use tags with list
    and batch API operations](security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-list-batch "security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-list-batch")
  - [Control settings using
    condition keys or context keys](security_iam_id-based-policy-examples.md#glue-identity-based-policy-condition-keys "security_iam_id-based-policy-examples.md#glue-identity-based-policy-condition-keys")
    - [Control policies
      that control settings using condition keys](security_iam_id-based-policy-examples.md#glue-identity-based-policy-condition-key-vpc "security_iam_id-based-policy-examples.md#glue-identity-based-policy-condition-key-vpc")
    - [Control policies
      that control settings using context keys](security_iam_id-based-policy-examples.md#glue-identity-based-policy-context-key-glue "security_iam_id-based-policy-examples.md#glue-identity-based-policy-context-key-glue")

  - [Deny an identity the ability to create data preview sessions](security_iam_id-based-policy-examples.md#deny-data-preview-sessions-per-identity "security_iam_id-based-policy-examples.md#deny-data-preview-sessions-per-identity")

- [Resource-based policy
  examples for AWS Glue](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md")
  - [Considerations for using resource-based policies with AWS Glue](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-considerations "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-considerations")
  - [Use a resource
    policy to control access in the same account](security_iam_resource-based-policy-examples.md#glue-policy-resource-policies-example-same-account "security_iam_resource-based-policy-examples.md#glue-policy-resource-policies-example-same-account")
