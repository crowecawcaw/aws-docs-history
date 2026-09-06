

# Actions, resources, and condition keys for AWS Organizations
<a name="list_organizations"></a>

AWS Organizations (service prefix: `organizations`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/organizations/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/organizations/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/organizations/organizations.json) for this service.

**Topics**
+ [API operations defined by AWS Organizations](#list_organizations-operations)
+ [Actions defined by AWS Organizations](#list_organizations-actions-as-permissions)
+ [Resource types defined by AWS Organizations](#list_organizations-resources-for-iam-policies)
+ [Condition keys for AWS Organizations](#list_organizations-policy-keys)

## API operations defined by AWS Organizations
<a name="list_organizations-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_organizations-actions-as-permissions).




- **   AcceptHandshake  **
  - **IAM action:**  [organizations:AcceptHandshake](#list_organizations-action-AcceptHandshake)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:LeaveOrganization](#list_organizations-action-LeaveOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AttachPolicy  **
  - **IAM action:**  [organizations:AttachPolicy](#list_organizations-action-AttachPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CancelHandshake  **
  - **IAM action:**  [organizations:CancelHandshake](#list_organizations-action-CancelHandshake) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CloseAccount  **
  - **IAM action:**  [organizations:CloseAccount](#list_organizations-action-CloseAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccount  **
  - **IAM action:**  [organizations:CreateAccount](#list_organizations-action-CreateAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:TagResource](#list_organizations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateGovCloudAccount  **
  - **IAM action:**  [organizations:CreateGovCloudAccount](#list_organizations-action-CreateGovCloudAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:TagResource](#list_organizations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOrganization  **
  - **IAM action:**  [organizations:CreateOrganization](#list_organizations-action-CreateOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateOrganizationalUnit  **
  - **IAM action:**  [organizations:CreateOrganizationalUnit](#list_organizations-action-CreateOrganizationalUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:TagResource](#list_organizations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePolicy  **
  - **IAM action:**  [organizations:CreatePolicy](#list_organizations-action-CreatePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:TagResource](#list_organizations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeclineHandshake  **
  - **IAM action:**  [organizations:DeclineHandshake](#list_organizations-action-DeclineHandshake) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOrganization  **
  - **IAM action:**  [organizations:DeleteOrganization](#list_organizations-action-DeleteOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOrganizationalUnit  **
  - **IAM action:**  [organizations:DeleteOrganizationalUnit](#list_organizations-action-DeleteOrganizationalUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicy  **
  - **IAM action:**  [organizations:DeletePolicy](#list_organizations-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [organizations:DeleteResourcePolicy](#list_organizations-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeregisterDelegatedAdministrator  **
  - **IAM action:**  [organizations:DeregisterDelegatedAdministrator](#list_organizations-action-DeregisterDelegatedAdministrator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccount  **
  - **IAM action:**  [organizations:DescribeAccount](#list_organizations-action-DescribeAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCreateAccountStatus  **
  - **IAM action:**  [organizations:DescribeCreateAccountStatus](#list_organizations-action-DescribeCreateAccountStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEffectivePolicy  **
  - **IAM action:**  [organizations:DescribeEffectivePolicy](#list_organizations-action-DescribeEffectivePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHandshake  **
  - **IAM action:**  [organizations:DescribeHandshake](#list_organizations-action-DescribeHandshake) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganization  **
  - **IAM action:**  [organizations:DescribeOrganization](#list_organizations-action-DescribeOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationalUnit  **
  - **IAM action:**  [organizations:DescribeOrganizationalUnit](#list_organizations-action-DescribeOrganizationalUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePolicy  **
  - **IAM action:**  [organizations:DescribePolicy](#list_organizations-action-DescribePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourcePolicy  **
  - **IAM action:**  [organizations:DescribeResourcePolicy](#list_organizations-action-DescribeResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResponsibilityTransfer  **
  - **IAM action:**  [organizations:DescribeResponsibilityTransfer](#list_organizations-action-DescribeResponsibilityTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetachPolicy  **
  - **IAM action:**  [organizations:DetachPolicy](#list_organizations-action-DetachPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DisableAWSServiceAccess  **
  - **IAM action:**  [organizations:DisableAWSServiceAccess](#list_organizations-action-DisableAWSServiceAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisablePolicyType  **
  - **IAM action:**  [organizations:DisablePolicyType](#list_organizations-action-DisablePolicyType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableAWSServiceAccess  **
  - **IAM action:**  [organizations:EnableAWSServiceAccess](#list_organizations-action-EnableAWSServiceAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableAllFeatures  **
  - **IAM action:**  [organizations:EnableAllFeatures](#list_organizations-action-EnableAllFeatures) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnablePolicyType  **
  - **IAM action:**  [organizations:EnablePolicyType](#list_organizations-action-EnablePolicyType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InviteAccountToOrganization  **
  - **IAM action:**  [organizations:InviteAccountToOrganization](#list_organizations-action-InviteAccountToOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:TagResource](#list_organizations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   InviteOrganizationToTransferResponsibility  **
  - **IAM action:**  [organizations:InviteOrganizationToTransferResponsibility](#list_organizations-action-InviteOrganizationToTransferResponsibility)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:TagResource](#list_organizations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   LeaveOrganization  **
  - **IAM action:**  [organizations:LeaveOrganization](#list_organizations-action-LeaveOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAWSServiceAccessForOrganization  **
  - **IAM action:**  [organizations:ListAWSServiceAccessForOrganization](#list_organizations-action-ListAWSServiceAccessForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccounts  **
  - **IAM action:**  [organizations:ListAccounts](#list_organizations-action-ListAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccountsForParent  **
  - **IAM action:**  [organizations:ListAccountsForParent](#list_organizations-action-ListAccountsForParent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccountsWithInvalidEffectivePolicy  **
  - **IAM action:**  [organizations:ListAccountsWithInvalidEffectivePolicy](#list_organizations-action-ListAccountsWithInvalidEffectivePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChildren  **
  - **IAM action:**  [organizations:ListChildren](#list_organizations-action-ListChildren) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCreateAccountStatus  **
  - **IAM action:**  [organizations:ListCreateAccountStatus](#list_organizations-action-ListCreateAccountStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDelegatedAdministrators  **
  - **IAM action:**  [organizations:ListDelegatedAdministrators](#list_organizations-action-ListDelegatedAdministrators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDelegatedServicesForAccount  **
  - **IAM action:**  [organizations:ListDelegatedServicesForAccount](#list_organizations-action-ListDelegatedServicesForAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEffectivePolicyValidationErrors  **
  - **IAM action:**  [organizations:ListEffectivePolicyValidationErrors](#list_organizations-action-ListEffectivePolicyValidationErrors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHandshakesForAccount  **
  - **IAM action:**  [organizations:ListHandshakesForAccount](#list_organizations-action-ListHandshakesForAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHandshakesForOrganization  **
  - **IAM action:**  [organizations:ListHandshakesForOrganization](#list_organizations-action-ListHandshakesForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInboundResponsibilityTransfers  **
  - **IAM action:**  [organizations:ListInboundResponsibilityTransfers](#list_organizations-action-ListInboundResponsibilityTransfers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationalUnitsForParent  **
  - **IAM action:**  [organizations:ListOrganizationalUnitsForParent](#list_organizations-action-ListOrganizationalUnitsForParent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOutboundResponsibilityTransfers  **
  - **IAM action:**  [organizations:ListOutboundResponsibilityTransfers](#list_organizations-action-ListOutboundResponsibilityTransfers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListParents  **
  - **IAM action:**  [organizations:ListParents](#list_organizations-action-ListParents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicies  **
  - **IAM action:**  [organizations:ListPolicies](#list_organizations-action-ListPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPoliciesForTarget  **
  - **IAM action:**  [organizations:ListPoliciesForTarget](#list_organizations-action-ListPoliciesForTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoots  **
  - **IAM action:**  [organizations:ListRoots](#list_organizations-action-ListRoots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [organizations:ListTagsForResource](#list_organizations-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTargetsForPolicy  **
  - **IAM action:**  [organizations:ListTargetsForPolicy](#list_organizations-action-ListTargetsForPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   MoveAccount  **
  - **IAM action:**  [organizations:MoveAccount](#list_organizations-action-MoveAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [organizations:PutResourcePolicy](#list_organizations-action-PutResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [organizations:TagResource](#list_organizations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RegisterDelegatedAdministrator  **
  - **IAM action:**  [organizations:RegisterDelegatedAdministrator](#list_organizations-action-RegisterDelegatedAdministrator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveAccountFromOrganization  **
  - **IAM action:**  [organizations:RemoveAccountFromOrganization](#list_organizations-action-RemoveAccountFromOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [organizations:TagResource](#list_organizations-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateResponsibilityTransfer  **
  - **IAM action:**  [organizations:TerminateResponsibilityTransfer](#list_organizations-action-TerminateResponsibilityTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [organizations:UntagResource](#list_organizations-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateOrganizationalUnit  **
  - **IAM action:**  [organizations:UpdateOrganizationalUnit](#list_organizations-action-UpdateOrganizationalUnit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePolicy  **
  - **IAM action:**  [organizations:UpdatePolicy](#list_organizations-action-UpdatePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateResponsibilityTransfer  **
  - **IAM action:**  [organizations:UpdateResponsibilityTransfer](#list_organizations-action-UpdateResponsibilityTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Organizations
<a name="list_organizations-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AcceptHandshake.html)  **
  - **Description:** Grants permission to send a response to the originator of a handshake agreeing to the action proposed by the handshake request
  - **Resource types (\*required):** [handshake\*](#list_organizations-resource-handshake)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AttachPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AttachPolicy.html)  **
  - **Description:** Grants permission to attach a policy to a root, an organizational unit, or an individual account
  - **Resource types (\*required):** [account](#list_organizations-resource-account) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [policy\*](#list_organizations-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Permissions management, Write

- **   [CancelHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CancelHandshake.html)  **
  - **Description:** Grants permission to cancel a handshake
  - **Resource types (\*required):** [handshake\*](#list_organizations-resource-handshake)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CloseAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CloseAccount.html)  **
  - **Description:** Grants permission to close an AWS account that is now a part of an Organizations, either created within the organization, or invited to join the organization
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html)  **
  - **Description:** Grants permission to create an AWS account that is automatically a member of the organization with the credentials that made the request
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html)  **
  - **Description:** Grants permission to create an AWS GovCloud (US) account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateOrganization.html)  **
  - **Description:** Grants permission to create an organization. The account with the credentials that calls the CreateOrganization operation automatically becomes the management account of the new organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateOrganizationalUnit.html)  **
  - **Description:** Grants permission to create an organizational unit (OU) within a root or parent OU
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreatePolicy.html)  **
  - **Description:** Grants permission to create a policy that you can attach to a root, an organizational unit (OU), or an individual AWS account
  - **Resource types (\*required):** [policy\*](#list_organizations-resource-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Write

- **   [DeclineHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeclineHandshake.html)  **
  - **Description:** Grants permission to decline a handshake request. This sets the handshake state to DECLINED and effectively deactivates the request
  - **Resource types (\*required):** [handshake\*](#list_organizations-resource-handshake)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeleteOrganization.html)  **
  - **Description:** Grants permission to delete the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeleteOrganizationalUnit.html)  **
  - **Description:** Grants permission to delete an organizational unit from a root or another OU
  - **Resource types (\*required):** [organizationalunit\*](#list_organizations-resource-organizationalunit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to delete a policy from your organization
  - **Resource types (\*required):** [policy\*](#list_organizations-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy from your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html)  **
  - **Description:** Grants permission to deregister the specified member AWS account as a delegated administrator for the AWS service that is specified by ServicePrincipal
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:ServicePrincipal](#list_organizations-organizations_ServicePrincipal)
  - **Access level:** Write

- **   [DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html)  **
  - **Description:** Grants permission to retrieve Organizations-related details about the specified account
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeCreateAccountStatus.html)  **
  - **Description:** Grants permission to retrieve the current status of an asynchronous request to create an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html)  **
  - **Description:** Grants permission to retrieve the effective policy for an account
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Read

- **   [DescribeHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeHandshake.html)  **
  - **Description:** Grants permission to retrieve details about a previously requested handshake
  - **Resource types (\*required):** [handshake\*](#list_organizations-resource-handshake)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganization.html)  **
  - **Description:** Grants permission to retrieve details about the organization that the calling credentials belong to
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganizationalUnit.html)  **
  - **Description:** Grants permission to retrieve details about an organizational unit (OU)
  - **Resource types (\*required):** [organizationalunit\*](#list_organizations-resource-organizationalunit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribePolicy.html)  **
  - **Description:** Grants permission to retrieve details about a policy
  - **Resource types (\*required):** [policy\*](#list_organizations-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Read

- **   [DescribeResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve information about a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeResponsibilityTransfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeResponsibilityTransfer.html)  **
  - **Description:** Grants permission to retrieve details about a previously responsibility transfer
  - **Resource types (\*required):** [responsibilitytransfer\*](#list_organizations-resource-responsibilitytransfer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Access level:** Read

- **   [DetachPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DetachPolicy.html)  **
  - **Description:** Grants permission to detach a policy from a target root, organizational unit, or account
  - **Resource types (\*required):** [account](#list_organizations-resource-account) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [policy\*](#list_organizations-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Permissions management, Write

- **   [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)  **
  - **Description:** Grants permission to disable integration of an AWS service (the service that is specified by ServicePrincipal) with AWS Organizations
  - **Resource types (\*required):** 
  - **Condition keys:** [organizations:ServicePrincipal](#list_organizations-organizations_ServicePrincipal)
  - **Access level:** Write

- **   [DisablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisablePolicyType.html)  **
  - **Description:** Grants permission to disable an organization policy type in a root
  - **Resource types (\*required):** [root\*](#list_organizations-resource-root)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Write

- **   [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)  **
  - **Description:** Grants permission to enable integration of an AWS service (the service that is specified by ServicePrincipal) with AWS Organizations
  - **Resource types (\*required):** 
  - **Condition keys:** [organizations:ServicePrincipal](#list_organizations-organizations_ServicePrincipal)
  - **Access level:** Write

- **   [EnableAllFeatures](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAllFeatures.html)  **
  - **Description:** Grants permission to start the process to enable all features in an organization, upgrading it from supporting only Consolidated Billing features
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html)  **
  - **Description:** Grants permission to enable a policy type in a root
  - **Resource types (\*required):** [root\*](#list_organizations-resource-root)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Write

- **   [InviteAccountToOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_InviteAccountToOrganization.html)  **
  - **Description:** Grants permission to send an invitation to another AWS account, asking it to join your organization as a member account
  - **Resource types (\*required):** [account](#list_organizations-resource-account)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)
  - **Access level:** Write

- **   [InviteOrganizationToTransferResponsibility](https://docs.aws.amazon.com/organizations/latest/APIReference/API_InviteOrganizationToTransferResponsibility.html)  **
  - **Description:** Grants permission to send an invitation to another AWS account, asking it to transfer a particular responsibility to your organization
  - **Resource types (\*required):** [account](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Access level:** Write

- **   [LeaveOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_LeaveOrganization.html)  **
  - **Description:** Grants permission to remove a member account from its parent organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListAWSServiceAccessForOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAWSServiceAccessForOrganization.html)  **
  - **Description:** Grants permission to retrieve the list of the AWS services for which you enabled integration with your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  **
  - **Description:** Grants permission to list all of the accounts in the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAccountsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccountsForParent.html)  **
  - **Description:** Grants permission to list the accounts in an organization that are contained by a root or organizational unit (OU)
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAccountsWithInvalidEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccountsWithInvalidEffectivePolicy.html)  **
  - **Description:** Grants permission to list accounts that have invalid effective policies for a specified policy type
  - **Resource types (\*required):** 
  - **Condition keys:** [organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** List

- **   [ListChildren](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListChildren.html)  **
  - **Description:** Grants permission to list all of the OUs or accounts that are contained in a parent OU or root
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListCreateAccountStatus.html)  **
  - **Description:** Grants permission to list the asynchronous account creation requests that are currently being tracked for the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDelegatedAdministrators](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListDelegatedAdministrators.html)  **
  - **Description:** Grants permission to list the AWS accounts that are designated as delegated administrators in this organization
  - **Resource types (\*required):** 
  - **Condition keys:** [organizations:ServicePrincipal](#list_organizations-organizations_ServicePrincipal)
  - **Access level:** List

- **   [ListDelegatedServicesForAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListDelegatedServicesForAccount.html)  **
  - **Description:** Grants permission to list the AWS services for which the specified account is a delegated administrator in this organization
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEffectivePolicyValidationErrors](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListEffectivePolicyValidationErrors.html)  **
  - **Description:** Grants permission to list validation errors found in the effective policy for a specific account and policy type
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** List

- **   [ListHandshakesForAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListHandshakesForAccount.html)  **
  - **Description:** Grants permission to list all of the handshakes that are associated with an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHandshakesForOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListHandshakesForOrganization.html)  **
  - **Description:** Grants permission to list the handshakes that are associated with the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInboundResponsibilityTransfers](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListInboundResponsibilityTransfers.html)  **
  - **Description:** Grants permission to list all responsibilities of a particular type transfered to your organization
  - **Resource types (\*required):** 
  - **Condition keys:** [organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Access level:** List

- **   [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html)  **
  - **Description:** Grants permission to list all of the organizational units (OUs) in a parent organizational unit or root
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListOutboundResponsibilityTransfers](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOutboundResponsibilityTransfers.html)  **
  - **Description:** Grants permission to list all responsibilities of a particular type transfered to another organization
  - **Resource types (\*required):** 
  - **Condition keys:** [organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Access level:** List

- **   [ListParents](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListParents.html)  **
  - **Description:** Grants permission to list the root or organizational units (OUs) that serve as the immediate parent of a child OU or account
  - **Resource types (\*required):** [account](#list_organizations-resource-account) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicies](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListPolicies.html)  **
  - **Description:** Grants permission to list all of the policies in an organization
  - **Resource types (\*required):** 
  - **Condition keys:** [organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** List

- **   [ListPoliciesForTarget](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListPoliciesForTarget.html)  **
  - **Description:** Grants permission to list all of the policies that are directly attached to a root, organizational unit (OU), or account
  - **Resource types (\*required):** [account](#list_organizations-resource-account) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** List

- **   [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html)  **
  - **Description:** Grants permission to list all of the roots that are defined in the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for the specified resource
  - **Resource types (\*required):** [account](#list_organizations-resource-account) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [policy](#list_organizations-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [resourcepolicy](#list_organizations-resource-resourcepolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [responsibilitytransfer](#list_organizations-resource-responsibilitytransfer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)<br />[organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** List

- **   [ListTargetsForPolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTargetsForPolicy.html)  **
  - **Description:** Grants permission to list all the roots, OUs, and accounts to which a policy is attached
  - **Resource types (\*required):** [policy\*](#list_organizations-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** List

- **   [MoveAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_MoveAccount.html)  **
  - **Description:** Grants permission to move an account from its current root or OU to another parent root or OU
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [organizationalunit\*](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [root\*](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create or update a resource policy
  - **Resource types (\*required):** [resourcepolicy\*](#list_organizations-resource-resourcepolicy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [RegisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html)  **
  - **Description:** Grants permission to register the specified member account to administer the Organizations features of the AWS service that is specified by ServicePrincipal
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:ServicePrincipal](#list_organizations-organizations_ServicePrincipal)
  - **Access level:** Write

- **   [RemoveAccountFromOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RemoveAccountFromOrganization.html)  **
  - **Description:** Grants permission to remove the specified account from the organization
  - **Resource types (\*required):** [account\*](#list_organizations-resource-account)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to the specified resource
  - **Resource types (\*required):** [account](#list_organizations-resource-account) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [policy](#list_organizations-resource-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [resourcepolicy](#list_organizations-resource-resourcepolicy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [responsibilitytransfer](#list_organizations-resource-responsibilitytransfer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)<br />[organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_organizations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Tagging, Write

- **   [TerminateResponsibilityTransfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_TerminateResponsibilityTransfer.html)  **
  - **Description:** Grants permission to end the transfer for a responsibility to or from your organization
  - **Resource types (\*required):** [responsibilitytransfer\*](#list_organizations-resource-responsibilitytransfer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from the specified resource
  - **Resource types (\*required):** [account](#list_organizations-resource-account) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [organizationalunit](#list_organizations-resource-organizationalunit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [policy](#list_organizations-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [resourcepolicy](#list_organizations-resource-resourcepolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Resource types (\*required):** [responsibilitytransfer](#list_organizations-resource-responsibilitytransfer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)<br />[organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Resource types (\*required):** [root](#list_organizations-resource-root) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_organizations-aws_TagKeys)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Tagging, Write

- **   [UpdateOrganizationalUnit](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdateOrganizationalUnit.html)  **
  - **Description:** Grants permission to rename an organizational unit (OU)
  - **Resource types (\*required):** [organizationalunit\*](#list_organizations-resource-organizationalunit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdatePolicy.html)  **
  - **Description:** Grants permission to update an existing policy with a new name, description, or content
  - **Resource types (\*required):** [policy\*](#list_organizations-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:PolicyType](#list_organizations-organizations_PolicyType)
  - **Access level:** Permissions management, Write

- **   [UpdateResponsibilityTransfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_UpdateResponsibilityTransfer.html)  **
  - **Description:** Grants permission to rename a responsibility transfer to or from your organization
  - **Resource types (\*required):** [responsibilitytransfer\*](#list_organizations-resource-responsibilitytransfer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_)<br />[organizations:TransferDirection](#list_organizations-organizations_TransferDirection)<br />[organizations:TransferType](#list_organizations-organizations_TransferType)
  - **Access level:** Write



## Resource types defined by AWS Organizations
<a name="list_organizations-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::${Account}:account/o-${OrganizationId}/${AccountId} | [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_) | 
|  [awspolicy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::aws:policy/${PolicyType}/p-${PolicyId} |   | 
|  [handshake](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::${Account}:handshake/o-${OrganizationId}/${HandshakeType}/h-${HandshakeId} |   | 
|  [organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::${Account}:organization/o-${OrganizationId} |   | 
|  [organizationalunit](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::${Account}:ou/o-${OrganizationId}/ou-${OrganizationalUnitId} | [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_) | 
|  [policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::${Account}:policy/o-${OrganizationId}/${PolicyType}/p-${PolicyId} | [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_) | 
|  [resourcepolicy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::${Account}:resourcepolicy/o-${OrganizationId}/rp-${ResourcePolicyId} | [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_) | 
|  [responsibilitytransfer](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::${Account}:transfer/o-${OrganizationId}/${TransferType}/${TransferDirection}/rt-${ResponsibilityTransferId} | [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_) | 
|  [root](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html)  | arn:${Partition}:organizations::${Account}:root/o-${OrganizationId}/r-${RootId} | [aws:ResourceTag/${TagKey}](#list_organizations-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Organizations
<a name="list_organizations-policy-keys"></a>

AWS Organizations defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [organizations:PolicyType](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html#orgs_permissions_conditionkeys)  | Filters access by the specified policy type names | String | 
|   [organizations:ServicePrincipal](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html#orgs_permissions_conditionkeys)  | Filters access by the specified service principal names | String | 
|   [organizations:TransferDirection](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html#orgs_permissions_conditionkeys)  | Filters access by the specified responsibility transfer by the direction | String | 
|   [organizations:TransferType](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html#orgs_permissions_conditionkeys)  | Filters access by the specified responsibility transfer type names | String | 