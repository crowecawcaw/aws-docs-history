# API operations by account type

This page lists all AWS Organizations API operations, grouped by the account that can call them.
Choose any API operation to learn more about using it.

## Operations you can call from only the organization's management account

- [CancelHandshake](../APIReference/API_CancelHandshake.md "../APIReference/API_CancelHandshake.md")
- [CreateAccount](../APIReference/API_CreateAccount.md "../APIReference/API_CreateAccount.md")
- [CreateGovCloudAccount](../APIReference/API_CreateGovCloudAccount.md "../APIReference/API_CreateGovCloudAccount.md") (only under specific conditions)
- [CreateOrganization](../APIReference/API_CreateOrganization.md "../APIReference/API_CreateOrganization.md") (the AWS account that calls this operation
  becomes the management account of the organization after the operation
  completes)
- [CreateOrganizationalUnit](../APIReference/API_CreateOrganizationalUnit.md "../APIReference/API_CreateOrganizationalUnit.md")
- [DeleteOrganization](../APIReference/API_DeleteOrganization.md "../APIReference/API_DeleteOrganization.md")
- [DeleteOrganizationalUnit](../APIReference/API_DeleteOrganizationalUnit.md "../APIReference/API_DeleteOrganizationalUnit.md")
- [DeregisterDelegatedAdministrator](../APIReference/API_DeregisterDelegatedAdministrator.md "../APIReference/API_DeregisterDelegatedAdministrator.md")
- [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")
- [EnableAllFeatures](../APIReference/API_EnableAllFeatures.md "../APIReference/API_EnableAllFeatures.md")
- [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")
- [InviteAccountToOrganization](../APIReference/API_InviteAccountToOrganization.md "../APIReference/API_InviteAccountToOrganization.md")
- [MoveAccount](../APIReference/API_MoveAccount.md "../APIReference/API_MoveAccount.md")
- [RegisterDelegatedAdministrator](../APIReference/API_RegisterDelegatedAdministrator.md "../APIReference/API_RegisterDelegatedAdministrator.md")
- [RemoveAccountFromOrganization](../APIReference/API_RemoveAccountFromOrganization.md "../APIReference/API_RemoveAccountFromOrganization.md")
- [UpdateOrganizationalUnit](../APIReference/API_UpdateOrganizationalUnit.md "../APIReference/API_UpdateOrganizationalUnit.md")

## Operations you can call from only the organization's management account or a member account designated as a delegated administrator

- [AttachPolicy](../APIReference/API_AttachPolicy.md "../APIReference/API_AttachPolicy.md")
- [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")
- [DeletePolicy](../APIReference/API_DeletePolicy.md "../APIReference/API_DeletePolicy.md")
- [DescribeAccount](../APIReference/API_DescribeAccount.md "../APIReference/API_DescribeAccount.md")
- [DescribeCreateAccountStatus](../APIReference/API_DescribeCreateAccountStatus.md "../APIReference/API_DescribeCreateAccountStatus.md")
- [DescribeEffectivePolicy](../APIReference/API_DescribeEffectivePolicy.md "../APIReference/API_DescribeEffectivePolicy.md")
- [DescribeOrganizationalUnit](../APIReference/API_DescribeOrganizationalUnit.md "../APIReference/API_DescribeOrganizationalUnit.md")
- [DescribePolicy](../APIReference/API_DescribePolicy.md "../APIReference/API_DescribePolicy.md")
- [DescribeResourcePolicy](../APIReference/API_DescribeResourcePolicy.md "../APIReference/API_DescribeResourcePolicy.md")
- [DetachPolicy](../APIReference/API_DetachPolicy.md "../APIReference/API_DetachPolicy.md")
- [DisablePolicyType](../APIReference/API_DisablePolicyType.md "../APIReference/API_DisablePolicyType.md")
- [EnablePolicyType](../APIReference/API_EnablePolicyType.md "../APIReference/API_EnablePolicyType.md")
- [ListAccounts](../APIReference/API_ListAccounts.md "../APIReference/API_ListAccounts.md")
- [ListAccountsForParent](../APIReference/API_ListAccountsForParent.md "../APIReference/API_ListAccountsForParent.md")
- [ListAWSServiceAccessForOrganization](../APIReference/API_ListAWSServiceAccessForOrganization.md "../APIReference/API_ListAWSServiceAccessForOrganization.md")
- [ListChildren](../APIReference/API_ListChildren.md "../APIReference/API_ListChildren.md")
- [ListCreateAccountStatus](../APIReference/API_ListCreateAccountStatus.md "../APIReference/API_ListCreateAccountStatus.md")
- [ListDelegatedAdministrators](../APIReference/API_ListDelegatedAdministrators.md "../APIReference/API_ListDelegatedAdministrators.md")
- [ListDelegatedServicesForAccount](../APIReference/API_ListDelegatedServicesForAccount.md "../APIReference/API_ListDelegatedServicesForAccount.md")
- [ListHandshakesForOrganization](../APIReference/API_ListHandshakesForOrganization.md "../APIReference/API_ListHandshakesForOrganization.md")
- [ListOrganizationalUnitsForParent](../APIReference/API_ListOrganizationalUnitsForParent.md "../APIReference/API_ListOrganizationalUnitsForParent.md")
- [ListParents](../APIReference/API_ListParents.md "../APIReference/API_ListParents.md")
- [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")
- [ListPoliciesForTarget](../APIReference/API_ListPoliciesForTarget.md "../APIReference/API_ListPoliciesForTarget.md")
- [ListRoots](../APIReference/API_ListRoots.md "../APIReference/API_ListRoots.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [ListTargetsForPolicy](../APIReference/API_ListTargetsForPolicy.md "../APIReference/API_ListTargetsForPolicy.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

## Operations you can call from only a member account in the organization

- [AcceptHandshake](../APIReference/API_AcceptHandshake.md "../APIReference/API_AcceptHandshake.md") (can be called from only the account that received
  the handshake/invitation)
- [DeclineHandshake](../APIReference/API_DeclineHandshake.md "../APIReference/API_DeclineHandshake.md") (can be called from only the account that received
  the handshake/invitation)
- [LeaveOrganization](../APIReference/API_LeaveOrganization.md "../APIReference/API_LeaveOrganization.md")

## Operations you can call from any account in the organization

These operations can be called from any account in the organization.

- [DescribeHandshake](../APIReference/API_DescribeHandshake.md "../APIReference/API_DescribeHandshake.md")
- [DescribeEffectivePolicy](../APIReference/API_DescribeEffectivePolicy.md "../APIReference/API_DescribeEffectivePolicy.md") (A member account can call this operation
  only if the `TargetId` parameter is set to the member account's own
  ID - it can't target another account.)
- [DescribeOrganization](../APIReference/API_DescribeOrganization.md "../APIReference/API_DescribeOrganization.md")
- [ListHandshakesForAccount](../APIReference/API_ListHandshakesForAccount.md "../APIReference/API_ListHandshakesForAccount.md")
