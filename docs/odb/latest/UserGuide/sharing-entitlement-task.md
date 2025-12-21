# Sharing Oracle Database@AWS entitlements across accounts

To enable collaboration while optimizing costs, share Oracle Database@AWS entitlements with other AWS accounts within the same AWS organization.
This topic explains how to share entitlements using AWS License Manager.

## Prerequisites for sharing entitlements

Before you share Oracle Database@AWS entitlements, make sure that you have the following:

- An active Oracle Database@AWS subscription (you must be the buyer account that
  accepted the private offer through AWS Marketplace)
- The IDs of the AWS accounts in your organization that you want to share
  entitlements with
- Necessary permissions for grantor and grantee to use AWS License Manager resources
  and operations (for more information, see [Identity and access management for
  License Manager](../../../license-manager/latest/userguide/identity-access-management.md "../../../license-manager/latest/userguide/identity-access-management.md") in the _AWS License Manager User Guide_)
- Permissions listed below for you (grantor) and entitlement recipient (grantee)

## Permissions required for entitlement sharing

In addition to AWS License Manager permissions, Oracle Database@AWS requires the following permissions:

### Grantor permissions

- `odb:CreateGrantShare`
- `odb:UpdateGrantShare`
- `odb:DeleteGrantShare`

### Grantee permissions

- `odb:UpdateGrantShare`
- `odb:DeleteGrantShare`

## Sharing Oracle Database@AWS entitlements with another account using AWS License Manager

To share entitlements with another AWS account, you create a grant using AWS License Manager. For more information, see
[Distribute License Manager entitlements](../../../license-manager/latest/userguide/distribute-entitlement.md "../../../license-manager/latest/userguide/distribute-entitlement.md")
in the _AWS License Manager User Guide_.

After you create the grant, the recipient (grantee) must:

- Accept and activate the grant. For more information, see [Grant acceptance and activation in License Manager](../../../license-manager/latest/userguide/grant-acceptance.md "../../../license-manager/latest/userguide/grant-acceptance.md") in the _AWS License Manager User Guide_.
- Follow the [initialization instructions](initialize-service-task.md#initialize-service-overview "initialize-service-task.md#initialize-service-overview") for Oracle Database@AWS.

After initialization completes, the grantee can provision Oracle Database@AWS resources using the shared entitlement.
