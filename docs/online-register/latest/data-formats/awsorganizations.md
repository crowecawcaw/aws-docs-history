

# Data retrieval APIs for AWS Organizations
<a name="awsorganizations"></a>

AWS Organizations provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="organizations-DescribeAccount"></a>[DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html) | Retrieve Organizations-related details about the specified account | Read | 
| <a name="organizations-DescribeCreateAccountStatus"></a>[DescribeCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeCreateAccountStatus.html) | Retrieve the current status of an asynchronous request to create an account | Read | 
| <a name="organizations-DescribeEffectivePolicy"></a>[DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html) | Retrieve the effective policy for an account | Read | 
| <a name="organizations-DescribeHandshake"></a>[DescribeHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeHandshake.html) | Retrieve details about a previously requested handshake | Read | 
| <a name="organizations-DescribeOrganization"></a>[DescribeOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganization.html) | Retrieve details about the organization that the calling credentials belong to | Read | 
| <a name="organizations-DescribeOrganizationalUnit"></a>[DescribeOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganizationalUnit.html) | Retrieve details about an organizational unit (OU) | Read | 
| <a name="organizations-DescribePolicy"></a>[DescribePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribePolicy.html) | Retrieve details about a policy | Read | 
| <a name="organizations-DescribeResourcePolicy"></a>[DescribeResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeResourcePolicy.html) | Retrieve information about a resource policy | Read | 
| <a name="organizations-DescribeResponsibilityTransfer"></a>[DescribeResponsibilityTransfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeResponsibilityTransfer.html) | Retrieve details about a previously responsibility transfer | Read | 
| <a name="organizations-ListAWSServiceAccessForOrganization"></a>[ListAWSServiceAccessForOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAWSServiceAccessForOrganization.html) | Retrieve the list of the AWS services for which you enabled integration with your organization | List | 
| <a name="organizations-ListAccounts"></a>[ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html) | List all of the accounts in the organization | List | 
| <a name="organizations-ListAccountsForParent"></a>[ListAccountsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccountsForParent.html) | List the accounts in an organization that are contained by a root or organizational unit (OU) | List | 
| <a name="organizations-ListAccountsWithInvalidEffectivePolicy"></a>[ListAccountsWithInvalidEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccountsWithInvalidEffectivePolicy.html) | List accounts that have invalid effective policies for a specified policy type | List | 
| <a name="organizations-ListChildren"></a>[ListChildren](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListChildren.html) | List all of the OUs or accounts that are contained in a parent OU or root | List | 
| <a name="organizations-ListCreateAccountStatus"></a>[ListCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListCreateAccountStatus.html) | List the asynchronous account creation requests that are currently being tracked for the organization | List | 
| <a name="organizations-ListDelegatedAdministrators"></a>[ListDelegatedAdministrators](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListDelegatedAdministrators.html) | List the AWS accounts that are designated as delegated administrators in this organization | List | 
| <a name="organizations-ListDelegatedServicesForAccount"></a>[ListDelegatedServicesForAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListDelegatedServicesForAccount.html) | List the AWS services for which the specified account is a delegated administrator in this organization | List | 
| <a name="organizations-ListEffectivePolicyValidationErrors"></a>[ListEffectivePolicyValidationErrors](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListEffectivePolicyValidationErrors.html) | List validation errors found in the effective policy for a specific account and policy type | List | 
| <a name="organizations-ListHandshakesForAccount"></a>[ListHandshakesForAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListHandshakesForAccount.html) | List all of the handshakes that are associated with an account | List | 
| <a name="organizations-ListHandshakesForOrganization"></a>[ListHandshakesForOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListHandshakesForOrganization.html) | List the handshakes that are associated with the organization | List | 
| <a name="organizations-ListInboundResponsibilityTransfers"></a>[ListInboundResponsibilityTransfers](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListInboundResponsibilityTransfers.html) | List all responsibilities of a particular type transfered to your organization | List | 
| <a name="organizations-ListOrganizationalUnitsForParent"></a>[ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html) | List all of the organizational units (OUs) in a parent organizational unit or root | List | 
| <a name="organizations-ListOutboundResponsibilityTransfers"></a>[ListOutboundResponsibilityTransfers](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOutboundResponsibilityTransfers.html) | List all responsibilities of a particular type transfered to another organization | List | 
| <a name="organizations-ListParents"></a>[ListParents](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListParents.html) | List the root or organizational units (OUs) that serve as the immediate parent of a child OU or account | List | 
| <a name="organizations-ListPolicies"></a>[ListPolicies](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListPolicies.html) | List all of the policies in an organization | List | 
| <a name="organizations-ListPoliciesForTarget"></a>[ListPoliciesForTarget](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListPoliciesForTarget.html) | List all of the policies that are directly attached to a root, organizational unit (OU), or account | List | 
| <a name="organizations-ListRoots"></a>[ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html) | List all of the roots that are defined in the organization | List | 
| <a name="organizations-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTagsForResource.html) | List all tags for the specified resource | List | 
| <a name="organizations-ListTargetsForPolicy"></a>[ListTargetsForPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTargetsForPolicy.html) | List all the roots, OUs, and accounts to which a policy is attached | List | 