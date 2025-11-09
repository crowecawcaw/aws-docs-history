# Controlling access to grants

You can control access to the operations that create and manage grants in key policies,
IAM policies, and in grants. Principals who get `CreateGrant` permission from a
grant have [more limited grant permissions](create-grant-overview.md#grant-creategrant "create-grant-overview.md#grant-creategrant").

| API operation       | Key policy or IAM policy                                                         | Grant |
| ------------------- | -------------------------------------------------------------------------------- | ----- |
| CreateGrant         | ✓                                                                                | ✓     |
| ListGrants          | ✓                                                                                | -     |
| ListRetirableGrants | ✓                                                                                | -     |
| Retire Grants       | (Limited. See [Retiring and revoking grants](grant-delete.md "grant-delete.md")) | ✓     |
| RevokeGrant         | ✓                                                                                | -     |

When you use a key policy or IAM policy to control access to operations that create and
manage grants, you can use one or more of the following policy conditions to limit the
permission. AWS KMS supports all of the following grant-related condition keys. For detailed
information and examples, see [AWS KMS condition keys](conditions-kms.md "conditions-kms.md").

[kms:GrantConstraintType](conditions-kms.md#conditions-kms-grant-constraint-type "conditions-kms.md#conditions-kms-grant-constraint-type")

Allows principals to create a grant only when the grant includes the specified [grant constraint](create-grant-overview.md#grant-constraints "create-grant-overview.md#grant-constraints").

[kms:GrantIsForAWSResource](conditions-kms.md#conditions-kms-grant-is-for-aws-resource "conditions-kms.md#conditions-kms-grant-is-for-aws-resource")

Allows principals to call `CreateGrant`, `ListGrants`, or
`RevokeGrant` only when [an AWS service that is
integrated with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration") sends the request on the principal's behalf.

[kms:GrantOperations](conditions-kms.md#conditions-kms-grant-operations "conditions-kms.md#conditions-kms-grant-operations")

Allows principals to create a grant, but limits the grant to the specified
operations.

[kms:GranteePrincipal](conditions-kms.md#conditions-kms-grantee-principal "conditions-kms.md#conditions-kms-grantee-principal")

Allows principals to create a grant only for the specified [grantee principal](grants.md#terms-grantee-principal "grants.md#terms-grantee-principal").

[kms:RetiringPrincipal](conditions-kms.md#conditions-kms-retiring-principal "conditions-kms.md#conditions-kms-retiring-principal")

Allows principals to create a grant only when the grant specifies a particular [retiring principal](grants.md#terms-retiring-principal "grants.md#terms-retiring-principal").
