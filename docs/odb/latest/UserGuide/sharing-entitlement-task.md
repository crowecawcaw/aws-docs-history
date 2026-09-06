

# Sharing Oracle Database@AWS entitlements across accounts
<a name="sharing-entitlement-task"></a>

To enable collaboration while optimizing costs, share Oracle Database@AWS entitlements with other AWS accounts within the same AWS organization. This topic explains how to share entitlements using AWS License Manager.

## Prerequisites for sharing entitlements
<a name="sharing-entitlements-prerequisites"></a>

Before you share Oracle Database@AWS entitlements, make sure that you have the following:
+ An active Oracle Database@AWS subscription (you must be the buyer account that accepted a private offer or public offer through AWS Marketplace)
+ The IDs of the AWS accounts in your organization that you want to share entitlements with
+ Necessary permissions for grantor and grantee to use AWS License Manager resources and operations (for more information, see [Identity and access management for License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html) in the *AWS License Manager User Guide*)
+ Permissions listed below for you (grantor) and entitlement recipient (grantee)

## Permissions required for entitlement sharing
<a name="sharing-entitlements-permissions"></a>

In addition to AWS License Manager permissions, Oracle Database@AWS requires the following permissions:

### Grantor permissions
<a name="sharing-entitlements-permissions-grantor"></a>
+ `odb:CreateGrantShare`
+ `odb:UpdateGrantShare`
+ `odb:DeleteGrantShare`

### Grantee permissions
<a name="sharing-entitlements-permissions-grantee"></a>
+ `odb:UpdateGrantShare`
+ `odb:DeleteGrantShare`
+ `license-manager:ListReceivedGrants`

## Sharing Oracle Database@AWS entitlements with another account using AWS License Manager
<a name="sharing-entitlements"></a>

To share entitlements with another AWS account, you create a grant using AWS License Manager. For more information, see [Distribute License Manager entitlements](https://docs.aws.amazon.com/license-manager/latest/userguide/distribute-entitlement.html) in the *AWS License Manager User Guide*.

After you create the grant, the recipient (grantee) must:
+ Accept and activate the grant. For more information, see [ Grant acceptance and activation in License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/grant-acceptance.html) in the *AWS License Manager User Guide*.
+ Follow the [initialization instructions](https://docs.aws.amazon.com/odb/latest/UserGuide/initialize-service-task.html#initialize-service-overview) for Oracle Database@AWS.

After initialization completes, the grantee can provision Oracle Database@AWS resources using the shared entitlement.