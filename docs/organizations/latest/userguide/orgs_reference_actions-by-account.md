

# API operations by account type
<a name="orgs_reference_actions-by-account"></a>

This page lists all AWS Organizations API operations, grouped by the account that can call them. Choose any API operation to learn more about using it. 

## Operations you can call from only the organization's management account
<a name="actions-management-account"></a>
+ [CancelHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CancelHandshake.html)
+ [CreateAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html)
+ [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) (only under specific conditions)
+ [CreateOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateOrganization.html) (the AWS account that calls this operation becomes the management account of the organization after the operation completes)
+ [CreateOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateOrganizationalUnit.html)
+ [DeleteOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeleteOrganization.html)
+ [DeleteOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeleteOrganizationalUnit.html)
+ [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html)
+ [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)
+ [EnableAllFeatures](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAllFeatures.html)
+ [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)
+ [InviteAccountToOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_InviteAccountToOrganization.html)
+ [MoveAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_MoveAccount.html)
+ [RegisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html)
+ [RemoveAccountFromOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RemoveAccountFromOrganization.html)
+ [UpdateOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdateOrganizationalUnit.html)

## Operations you can call from only the organization's management account or a member account designated as a delegated administrator
<a name="actions-management-or-delegated-admin"></a>
+ [AttachPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AttachPolicy.html)
+ [CreatePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreatePolicy.html)
+ [DeletePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeletePolicy.html)
+ [DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html)
+ [DescribeCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeCreateAccountStatus.html)
+ [DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html)
+ [DescribeOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganizationalUnit.html)
+ [DescribePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribePolicy.html)
+ [DescribeResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeResourcePolicy.html)
+ [DetachPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DetachPolicy.html)
+ [DisablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisablePolicyType.html)
+ [EnablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html)
+ [ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)
+ [ListAccountsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccountsForParent.html)
+ [ListAWSServiceAccessForOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAWSServiceAccessForOrganization.html)
+ [ListChildren](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListChildren.html)
+ [ListCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListCreateAccountStatus.html)
+ [ListDelegatedAdministrators](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListDelegatedAdministrators.html)
+ [ListDelegatedServicesForAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListDelegatedServicesForAccount.html)
+ [ListHandshakesForOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListHandshakesForOrganization.html)
+ [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html)
+ [ListParents](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListParents.html)
+ [ListPolicies](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListPolicies.html)
+ [ListPoliciesForTarget](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListPoliciesForTarget.html)
+ [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html)
+ [ListTagsForResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTagsForResource.html)
+ [ListTargetsForPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTargetsForPolicy.html)
+ [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)
+ [UpdatePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdatePolicy.html)

## Operations you can call from only a member account in the organization
<a name="actions-member-account"></a>
+ [AcceptHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AcceptHandshake.html) (can be called from only the account that received the handshake/invitation)
+ [DeclineHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeclineHandshake.html) (can be called from only the account that received the handshake/invitation)
+ [LeaveOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_LeaveOrganization.html)

## Operations you can call from any account in the organization
<a name="actions-any-account"></a>

These operations can be called from any account in the organization.
+ [DescribeHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeHandshake.html)
+ [DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html) (A member account can call this operation only if the `TargetId` parameter is set to the member account's own ID - it can't target another account.)
+ [DescribeOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganization.html)
+ [ListHandshakesForAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListHandshakesForAccount.html)