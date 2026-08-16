# Best practices for AWS KMS grants

AWS KMS recommends the following best practices when creating, using, and managing
grants.

- Limit the permissions in the grant to those that the grantee requires. Use the
  principle of [least
  privileged access](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege"). Be as specific as possible in all grant parameters:

  - Specify only the [grant operations](grants.md#terms-grant-operations "grants.md#terms-grant-operations")
    that the grantee needs.
  - Use a specific [grantee principal](grants.md#terms-grantee-principal "grants.md#terms-grantee-principal"),
    such as an IAM role, or a specific [grantee service principal](grants.md#terms-grantee-service-principal "grants.md#terms-grantee-service-principal").
  - Use [grant constraints](grants.md#terms-grant-constraint "grants.md#terms-grant-constraint") to further
    restrict the grant.

- Use the encryption context [grant
  constraints](grants.md#terms-grant-constraint "grants.md#terms-grant-constraint") to ensure that callers are using the KMS key for the intended
  purpose. For details about how to use the encryption context in a request to secure your
  data, see [How to Protect the Integrity of Your Encrypted Data by Using AWS Key Management Service and
  EncryptionContext](https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/ "https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/") in the _AWS Security
  Blog_.

###### Tip

Use the [EncryptionContextEqual](create-grant-overview.md#grant-constraints "create-grant-overview.md#grant-constraints") grant
constraint whenever possible. The [EncryptionContextSubset](create-grant-overview.md#grant-constraints "create-grant-overview.md#grant-constraints")
grant constraint is more difficult to use correctly. If you need to use it, read the documentation
carefully and test the grant constraint to make sure it works as intended.

- When creating grants for supported AWS services, use the [SourceArn grant constraint](create-grant-overview.md#terms-source-arn-constraint "create-grant-overview.md#terms-source-arn-constraint") to restrict the grant
  to a specific resource.
- Be aware of duplicate grants. Duplicate grants have the same parameters except for
  the grant name. Needless duplication can cause you to reach the [Grants per KMS key
  quota](resource-limits.md#grants-per-key "resource-limits.md#grants-per-key").
  To avoid duplicating grants when retrying a
  `CreateGrant` request, use the [Name
  parameter](create-grant-overview.md#grant-create "create-grant-overview.md#grant-create"). To detect duplicate grants, use the [ListGrants](../APIReference/API_ListGrants.md "../APIReference/API_ListGrants.md") operation.

###### Note

Some AWS services create grants for different resources that might appear to be
duplicates. These grants have lifecycles tied to the different resources. Deleting
grants created by an AWS service can be disruptive and requires extra precaution.

- Remember that grants do not automatically expire. [Retire
  or revoke the grant](grant-delete.md "grant-delete.md") as soon as the permission is no longer needed. Grants that
  are not deleted might create a security risk for encrypted resources.
