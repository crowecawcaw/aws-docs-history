# Best practices for AWS KMS grants

AWS KMS recommends the following best practices when creating, using, and managing
grants.

- Limit the permissions in the grant to those that the grantee principal requires. Use
  the principle of [least privileged access](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege").
- Use a specific grantee principal, such as an IAM role, and give the grantee principal
  permission to use only the API operations that they require.
- Use the encryption context [grant
  constraints](grants.md#terms-grant-constraint "grants.md#terms-grant-constraint") to ensure that callers are using the KMS key for the intended
  purpose. For details about how to use the encryption context in a request to secure your
  data, see [How to Protect the Integrity of Your Encrypted Data by Using AWS Key Management Service and
  EncryptionContext](https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/ "https://aws.amazon.com/blogs/security/how-to-protect-the-integrity-of-your-encrypted-data-by-using-aws-key-management-service-and-encryptioncontext/") in the _AWS Security
  Blog_.

###### Tip

Use the [EncryptionContextEqual](create-grant-overview.md#grant-constraints "create-grant-overview.md#grant-constraints") grant
constraint whenever possible. The [EncryptionContextSubset](create-grant-overview.md#grant-constraints "create-grant-overview.md#grant-constraints") grant constraint is more difficult to use correctly.
If you need to use it, read the documentation carefully and test the grant constraint to
make sure it works as intended.

- Delete duplicate grants. Duplicate grants have the same key ARN, API actions, grantee
  principal, encryption context, and name. If you retire or revoke the original grant but
  leave the duplicates, the leftover duplicate grants constitute unintended escalations of
  privilege. To avoid duplicating grants when retrying a `CreateGrant` request,
  use the [Name parameter](create-grant-overview.md#grant-create "create-grant-overview.md#grant-create"). To detect
  duplicate grants, use the [ListGrants](../APIReference/API_ListGrants.md "../APIReference/API_ListGrants.md")
  operation. If you accidentally create a duplicate grant, retire or revoke it as soon as
  possible.

###### Note

Grants for [AWS managed keys](concepts.md#aws-managed-key "concepts.md#aws-managed-key") might look like
duplicates but have different grantee principals.

The `GranteePrincipal` field in the `ListGrants` response usually
contains the grantee principal of the grant. However, when the grantee principal in the
grant is an AWS service, the `GranteePrincipal` field contains the [service
principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), which might represent several different grantee principals.

- Remember that grants do not automatically expire. [Retire
  or revoke the grant](grant-delete.md "grant-delete.md") as soon as the permission is no longer needed. Grants that
  are not deleted might create a security risk for encrypted resources.
