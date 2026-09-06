

# Actions, resources, and condition keys for AWS Identity and Access Management (IAM)
<a name="list_iam"></a>

AWS Identity and Access Management (IAM) (service prefix: `iam`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/IAM/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iam/iam.json) for this service.

**Topics**
+ [API operations defined by AWS Identity and Access Management (IAM)](#list_iam-operations)
+ [Actions defined by AWS Identity and Access Management (IAM)](#list_iam-actions-as-permissions)
+ [Permission-only actions for AWS Identity and Access Management (IAM)](#list_iam-permission-only-actions)
+ [Resource types defined by AWS Identity and Access Management (IAM)](#list_iam-resources-for-iam-policies)
+ [Condition keys for AWS Identity and Access Management (IAM)](#list_iam-policy-keys)

## API operations defined by AWS Identity and Access Management (IAM)
<a name="list_iam-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iam-actions-as-permissions).




- **   AcceptDelegationRequest  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AcceptDelegationRequest](#list_iam-action-AcceptDelegationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AcquireRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AttachRolePolicy](#list_iam-action-AttachRolePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:CreateRole](#list_iam-action-CreateRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:GetRole](#list_iam-action-GetRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:GetRoleTemplateVersion](#list_iam-action-GetRoleTemplateVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PutRolePermissionsBoundary](#list_iam-action-PutRolePermissionsBoundary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PutRolePolicy](#list_iam-action-PutRolePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:TagRole](#list_iam-action-TagRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AddClientIDToOpenIDConnectProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AddClientIDToOpenIDConnectProvider](#list_iam-action-AddClientIDToOpenIDConnectProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddRoleToInstanceProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AddRoleToInstanceProfile](#list_iam-action-AddRoleToInstanceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](#list_iam-action-PassRole)  / **Condition key:** [iam:PassedToService](#list_iam-iam_PassedToService) / **Possible value(s):** ec2.amazonaws.com / **Access level:** Write

- **   AddUserToGroup  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AddUserToGroup](#list_iam-action-AddUserToGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateDelegationRequest  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AssociateDelegationRequest](#list_iam-action-AssociateDelegationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachGroupPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AttachGroupPolicy](#list_iam-action-AttachGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AttachRolePolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AttachRolePolicy](#list_iam-action-AttachRolePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AttachUserPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:AttachUserPolicy](#list_iam-action-AttachUserPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ChangePassword  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ChangePassword](#list_iam-action-ChangePassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccessKey  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateAccessKey](#list_iam-action-CreateAccessKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccountAlias  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateAccountAlias](#list_iam-action-CreateAccountAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDelegationRequest  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateDelegationRequest](#list_iam-action-CreateDelegationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGroup  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateGroup](#list_iam-action-CreateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInstanceProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateInstanceProfile](#list_iam-action-CreateInstanceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:TagInstanceProfile](#list_iam-action-TagInstanceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLoginProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateLoginProfile](#list_iam-action-CreateLoginProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateOpenIDConnectProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateOpenIDConnectProvider](#list_iam-action-CreateOpenIDConnectProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:TagOpenIDConnectProvider](#list_iam-action-TagOpenIDConnectProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreatePolicy](#list_iam-action-CreatePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:TagPolicy](#list_iam-action-TagPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePolicyVersion  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreatePolicyVersion](#list_iam-action-CreatePolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CreateRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateRole](#list_iam-action-CreateRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:TagRole](#list_iam-action-TagRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSAMLProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateSAMLProvider](#list_iam-action-CreateSAMLProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:TagSAMLProvider](#list_iam-action-TagSAMLProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceLinkedRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateServiceLinkedRole](#list_iam-action-CreateServiceLinkedRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PutRolePolicy](#list_iam-action-PutRolePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateServiceSpecificCredential  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateServiceSpecificCredential](#list_iam-action-CreateServiceSpecificCredential) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUser  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateUser](#list_iam-action-CreateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:TagUser](#list_iam-action-TagUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVirtualMFADevice  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateVirtualMFADevice](#list_iam-action-CreateVirtualMFADevice)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:TagMFADevice](#list_iam-action-TagMFADevice)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeactivateMFADevice  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeactivateMFADevice](#list_iam-action-DeactivateMFADevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccessKey  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteAccessKey](#list_iam-action-DeleteAccessKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccountAlias  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteAccountAlias](#list_iam-action-DeleteAccountAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccountPasswordPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteAccountPasswordPolicy](#list_iam-action-DeleteAccountPasswordPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteGroup  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteGroup](#list_iam-action-DeleteGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGroupPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteGroupPolicy](#list_iam-action-DeleteGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteInstanceProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteInstanceProfile](#list_iam-action-DeleteInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoginProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteLoginProfile](#list_iam-action-DeleteLoginProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOpenIDConnectProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteOpenIDConnectProvider](#list_iam-action-DeleteOpenIDConnectProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeletePolicy](#list_iam-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeletePolicyVersion  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeletePolicyVersion](#list_iam-action-DeletePolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteRole](#list_iam-action-DeleteRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRolePermissionsBoundary  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteRolePermissionsBoundary](#list_iam-action-DeleteRolePermissionsBoundary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteRolePolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteRolePolicy](#list_iam-action-DeleteRolePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteSAMLProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteSAMLProvider](#list_iam-action-DeleteSAMLProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSSHPublicKey  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteSSHPublicKey](#list_iam-action-DeleteSSHPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServerCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteServerCertificate](#list_iam-action-DeleteServerCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceLinkedRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteServiceLinkedRole](#list_iam-action-DeleteServiceLinkedRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceSpecificCredential  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteServiceSpecificCredential](#list_iam-action-DeleteServiceSpecificCredential) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSigningCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteSigningCertificate](#list_iam-action-DeleteSigningCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteUser](#list_iam-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserPermissionsBoundary  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteUserPermissionsBoundary](#list_iam-action-DeleteUserPermissionsBoundary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteUserPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteUserPolicy](#list_iam-action-DeleteUserPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteVirtualMFADevice  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DeleteVirtualMFADevice](#list_iam-action-DeleteVirtualMFADevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachGroupPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DetachGroupPolicy](#list_iam-action-DetachGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DetachRolePolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DetachRolePolicy](#list_iam-action-DetachRolePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DetachUserPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DetachUserPolicy](#list_iam-action-DetachUserPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DisableOutboundWebIdentityFederation  **
  - **SDK client:** iam
  - **IAM action:**  [iam:DisableOutboundWebIdentityFederation](#list_iam-action-DisableOutboundWebIdentityFederation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableMFADevice  **
  - **SDK client:** iam
  - **IAM action:**  [iam:EnableMFADevice](#list_iam-action-EnableMFADevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableOutboundWebIdentityFederation  **
  - **SDK client:** iam
  - **IAM action:**  [iam:EnableOutboundWebIdentityFederation](#list_iam-action-EnableOutboundWebIdentityFederation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateCredentialReport  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GenerateCredentialReport](#list_iam-action-GenerateCredentialReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GenerateOrganizationsAccessReport  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GenerateOrganizationsAccessReport](#list_iam-action-GenerateOrganizationsAccessReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GenerateServiceLastAccessedDetails  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GenerateServiceLastAccessedDetails](#list_iam-action-GenerateServiceLastAccessedDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccessKeyLastUsed  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetAccessKeyLastUsed](#list_iam-action-GetAccessKeyLastUsed) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountAuthorizationDetails  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetAccountAuthorizationDetails](#list_iam-action-GetAccountAuthorizationDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountPasswordPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetAccountPasswordPolicy](#list_iam-action-GetAccountPasswordPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountProperties  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetAccountProperties](#list_iam-action-GetAccountProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountSummary  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetAccountSummary](#list_iam-action-GetAccountSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetContextKeysForCustomPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetContextKeysForCustomPolicy](#list_iam-action-GetContextKeysForCustomPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContextKeysForPrincipalPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetContextKeysForPrincipalPolicy](#list_iam-action-GetContextKeysForPrincipalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCredentialReport  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetCredentialReport](#list_iam-action-GetCredentialReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDelegationRequest  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetDelegationRequest](#list_iam-action-GetDelegationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroup  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetGroup](#list_iam-action-GetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroupPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetGroupPolicy](#list_iam-action-GetGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHumanReadableSummary  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetHumanReadableSummary](#list_iam-action-GetHumanReadableSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstanceProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetInstanceProfile](#list_iam-action-GetInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLoginProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetLoginProfile](#list_iam-action-GetLoginProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetMFADevice  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetMFADevice](#list_iam-action-GetMFADevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOpenIDConnectProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetOpenIDConnectProvider](#list_iam-action-GetOpenIDConnectProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOrganizationsAccessReport  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetOrganizationsAccessReport](#list_iam-action-GetOrganizationsAccessReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOutboundWebIdentityFederationInfo  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetOutboundWebIdentityFederationInfo](#list_iam-action-GetOutboundWebIdentityFederationInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetPolicy](#list_iam-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicyVersion  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetPolicyVersion](#list_iam-action-GetPolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetRole](#list_iam-action-GetRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRolePolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetRolePolicy](#list_iam-action-GetRolePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRoleTemplateVersion  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetRoleTemplateVersion](#list_iam-action-GetRoleTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSAMLProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetSAMLProvider](#list_iam-action-GetSAMLProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSSHPublicKey  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetSSHPublicKey](#list_iam-action-GetSSHPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServerCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetServerCertificate](#list_iam-action-GetServerCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceLastAccessedDetails  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetServiceLastAccessedDetails](#list_iam-action-GetServiceLastAccessedDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceLastAccessedDetailsWithEntities  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetServiceLastAccessedDetailsWithEntities](#list_iam-action-GetServiceLastAccessedDetailsWithEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceLinkedRoleDeletionStatus  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetServiceLinkedRoleDeletionStatus](#list_iam-action-GetServiceLinkedRoleDeletionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUser  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetUser](#list_iam-action-GetUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUserPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:GetUserPolicy](#list_iam-action-GetUserPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessKeys  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListAccessKeys](#list_iam-action-ListAccessKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccountAliases  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListAccountAliases](#list_iam-action-ListAccountAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttachedGroupPolicies  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListAttachedGroupPolicies](#list_iam-action-ListAttachedGroupPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttachedRolePolicies  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListAttachedRolePolicies](#list_iam-action-ListAttachedRolePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttachedUserPolicies  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListAttachedUserPolicies](#list_iam-action-ListAttachedUserPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDelegationRequests  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListDelegationRequests](#list_iam-action-ListDelegationRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEntitiesForPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListEntitiesForPolicy](#list_iam-action-ListEntitiesForPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupPolicies  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListGroupPolicies](#list_iam-action-ListGroupPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroups  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListGroups](#list_iam-action-ListGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupsForUser  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListGroupsForUser](#list_iam-action-ListGroupsForUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstanceProfileTags  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListInstanceProfileTags](#list_iam-action-ListInstanceProfileTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstanceProfiles  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListInstanceProfiles](#list_iam-action-ListInstanceProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstanceProfilesForRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListInstanceProfilesForRole](#list_iam-action-ListInstanceProfilesForRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMFADeviceTags  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListMFADeviceTags](#list_iam-action-ListMFADeviceTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMFADevices  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListMFADevices](#list_iam-action-ListMFADevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOpenIDConnectProviderTags  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListOpenIDConnectProviderTags](#list_iam-action-ListOpenIDConnectProviderTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOpenIDConnectProviders  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListOpenIDConnectProviders](#list_iam-action-ListOpenIDConnectProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicies  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListPolicies](#list_iam-action-ListPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPoliciesGrantingServiceAccess  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListPoliciesGrantingServiceAccess](#list_iam-action-ListPoliciesGrantingServiceAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyTags  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListPolicyTags](#list_iam-action-ListPolicyTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyVersions  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListPolicyVersions](#list_iam-action-ListPolicyVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRolePolicies  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListRolePolicies](#list_iam-action-ListRolePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoleTags  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListRoleTags](#list_iam-action-ListRoleTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoles  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListRoles](#list_iam-action-ListRoles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSAMLProviderTags  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListSAMLProviderTags](#list_iam-action-ListSAMLProviderTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSAMLProviders  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListSAMLProviders](#list_iam-action-ListSAMLProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSSHPublicKeys  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListSSHPublicKeys](#list_iam-action-ListSSHPublicKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServerCertificateTags  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListServerCertificateTags](#list_iam-action-ListServerCertificateTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServerCertificates  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListServerCertificates](#list_iam-action-ListServerCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceSpecificCredentials  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListServiceSpecificCredentials](#list_iam-action-ListServiceSpecificCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSigningCertificates  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListSigningCertificates](#list_iam-action-ListSigningCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserPolicies  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListUserPolicies](#list_iam-action-ListUserPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserTags  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListUserTags](#list_iam-action-ListUserTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsers  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListUsers](#list_iam-action-ListUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVirtualMFADevices  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ListVirtualMFADevices](#list_iam-action-ListVirtualMFADevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAccountProperties  **
  - **SDK client:** iam
  - **IAM action:**  [iam:CreateServiceLinkedRole](#list_iam-action-CreateServiceLinkedRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PutAccountProperties](#list_iam-action-PutAccountProperties)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutGroupPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:PutGroupPolicy](#list_iam-action-PutGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutRolePermissionsBoundary  **
  - **SDK client:** iam
  - **IAM action:**  [iam:PutRolePermissionsBoundary](#list_iam-action-PutRolePermissionsBoundary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutRolePolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:PutRolePolicy](#list_iam-action-PutRolePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutUserPermissionsBoundary  **
  - **SDK client:** iam
  - **IAM action:**  [iam:PutUserPermissionsBoundary](#list_iam-action-PutUserPermissionsBoundary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutUserPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:PutUserPolicy](#list_iam-action-PutUserPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RejectDelegationRequest  **
  - **SDK client:** iam
  - **IAM action:**  [iam:RejectDelegationRequest](#list_iam-action-RejectDelegationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveClientIDFromOpenIDConnectProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:RemoveClientIDFromOpenIDConnectProvider](#list_iam-action-RemoveClientIDFromOpenIDConnectProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveRoleFromInstanceProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:RemoveRoleFromInstanceProfile](#list_iam-action-RemoveRoleFromInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveUserFromGroup  **
  - **SDK client:** iam
  - **IAM action:**  [iam:RemoveUserFromGroup](#list_iam-action-RemoveUserFromGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetServiceSpecificCredential  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ResetServiceSpecificCredential](#list_iam-action-ResetServiceSpecificCredential) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResyncMFADevice  **
  - **SDK client:** iam
  - **IAM action:**  [iam:ResyncMFADevice](#list_iam-action-ResyncMFADevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendDelegationToken  **
  - **SDK client:** iam
  - **IAM action:**  [iam:SendDelegationToken](#list_iam-action-SendDelegationToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetDefaultPolicyVersion  **
  - **SDK client:** iam
  - **IAM action:**  [iam:SetDefaultPolicyVersion](#list_iam-action-SetDefaultPolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SetSecurityTokenServicePreferences  **
  - **SDK client:** iam
  - **IAM action:**  [iam:SetSecurityTokenServicePreferences](#list_iam-action-SetSecurityTokenServicePreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SimulateCustomPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:SimulateCustomPolicy](#list_iam-action-SimulateCustomPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SimulatePrincipalPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:SimulatePrincipalPolicy](#list_iam-action-SimulatePrincipalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagInstanceProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagInstanceProfile](#list_iam-action-TagInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagMFADevice  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagMFADevice](#list_iam-action-TagMFADevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagOpenIDConnectProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagOpenIDConnectProvider](#list_iam-action-TagOpenIDConnectProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagPolicy](#list_iam-action-TagPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagRole](#list_iam-action-TagRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagSAMLProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagSAMLProvider](#list_iam-action-TagSAMLProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagServerCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagServerCertificate](#list_iam-action-TagServerCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TagUser  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagUser](#list_iam-action-TagUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagInstanceProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UntagInstanceProfile](#list_iam-action-UntagInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagMFADevice  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UntagMFADevice](#list_iam-action-UntagMFADevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagOpenIDConnectProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UntagOpenIDConnectProvider](#list_iam-action-UntagOpenIDConnectProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UntagPolicy](#list_iam-action-UntagPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UntagRole](#list_iam-action-UntagRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagSAMLProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UntagSAMLProvider](#list_iam-action-UntagSAMLProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagServerCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UntagServerCertificate](#list_iam-action-UntagServerCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagUser  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UntagUser](#list_iam-action-UntagUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccessKey  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateAccessKey](#list_iam-action-UpdateAccessKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccountPasswordPolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateAccountPasswordPolicy](#list_iam-action-UpdateAccountPasswordPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssumeRolePolicy  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateAssumeRolePolicy](#list_iam-action-UpdateAssumeRolePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateGroup  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateGroup](#list_iam-action-UpdateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLoginProfile  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateLoginProfile](#list_iam-action-UpdateLoginProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOpenIDConnectProviderThumbprint  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateOpenIDConnectProviderThumbprint](#list_iam-action-UpdateOpenIDConnectProviderThumbprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRole  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateRole](#list_iam-action-UpdateRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRoleDescription  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateRoleDescription](#list_iam-action-UpdateRoleDescription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSAMLProvider  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateSAMLProvider](#list_iam-action-UpdateSAMLProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSSHPublicKey  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateSSHPublicKey](#list_iam-action-UpdateSSHPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServerCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateServerCertificate](#list_iam-action-UpdateServerCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceSpecificCredential  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateServiceSpecificCredential](#list_iam-action-UpdateServiceSpecificCredential) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSigningCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateSigningCertificate](#list_iam-action-UpdateSigningCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUser  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UpdateUser](#list_iam-action-UpdateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UploadSSHPublicKey  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UploadSSHPublicKey](#list_iam-action-UploadSSHPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UploadServerCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:TagServerCertificate](#list_iam-action-TagServerCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:UploadServerCertificate](#list_iam-action-UploadServerCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UploadSigningCertificate  **
  - **SDK client:** iam
  - **IAM action:**  [iam:UploadSigningCertificate](#list_iam-action-UploadSigningCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Identity and Access Management (IAM)
<a name="list_iam-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcceptDelegationRequest.html)  **
  - **Description:** Accepts a delegation request resource, granting the requested temporary access
  - **Resource types (\*required):** [delegation-request\*](#list_iam-resource-delegation-request)
  - **Condition keys:** [iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner)
  - **Access level:** Write

- **   [AddClientIDToOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddClientIDToOpenIDConnectProvider.html)  **
  - **Description:** Grants permission to add a new client ID (audience) to the list of registered IDs for the specified IAM OpenID Connect (OIDC) provider resource
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddRoleToInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddRoleToInstanceProfile.html)  **
  - **Description:** Grants permission to add an IAM role to the specified instance profile
  - **Resource types (\*required):** [instance-profile\*](#list_iam-resource-instance-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddUserToGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddUserToGroup.html)  **
  - **Description:** Grants permission to add an IAM user to the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AssociateDelegationRequest.html)  **
  - **Description:** Associates a delegation request resource with the calling identity
  - **Resource types (\*required):** [delegation-request\*](#list_iam-resource-delegation-request)
  - **Condition keys:** [iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner)
  - **Access level:** Write

- **   [AttachGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachGroupPolicy.html)  **
  - **Description:** Grants permission to attach a managed policy to the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:** [iam:PolicyARN](#list_iam-iam_PolicyARN)
  - **Access level:** Permissions management, Write

- **   [AttachRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachRolePolicy.html)  **
  - **Description:** Grants permission to attach a managed policy to the specified IAM role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:PolicyARN](#list_iam-iam_PolicyARN)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:RoleTemplateARN](#list_iam-iam_RoleTemplateARN)
  - **Access level:** Permissions management, Write

- **   [AttachUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachUserPolicy.html)  **
  - **Description:** Grants permission to attach a managed policy to the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:PolicyARN](#list_iam-iam_PolicyARN)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ChangePassword](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html)  **
  - **Description:** Grants permission to an IAM user to change their own password
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccessKey.html)  **
  - **Description:** Grants permission to create access key and secret access key for the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAccountAlias](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccountAlias.html)  **
  - **Description:** Grants permission to create an alias for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateDelegationRequest.html)  **
  - **Description:** Creates an IAM delegation request resource for temporary access delegation
  - **Resource types (\*required):** [delegation-request\*](#list_iam-resource-delegation-request)
  - **Condition keys:** [iam:DelegationDuration](#list_iam-iam_DelegationDuration)<br />[iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner)<br />[iam:NotificationChannel](#list_iam-iam_NotificationChannel)<br />[iam:TemplateArn](#list_iam-iam_TemplateArn)
  - **Access level:** Write

- **   [CreateGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateGroup.html)  **
  - **Description:** Grants permission to create a new group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateInstanceProfile.html)  **
  - **Description:** Grants permission to create a new instance profile
  - **Resource types (\*required):** [instance-profile\*](#list_iam-resource-instance-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html)  **
  - **Description:** Grants permission to create a password for the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html)  **
  - **Description:** Grants permission to create an IAM resource that describes an identity provider (IdP) that supports OpenID Connect (OIDC)
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html)  **
  - **Description:** Grants permission to create a new managed policy
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [CreatePolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicyVersion.html)  **
  - **Description:** Grants permission to create a new version of the specified managed policy
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html)  **
  - **Description:** Grants permission to create a new role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:RoleTemplateARN](#list_iam-iam_RoleTemplateARN)
  - **Access level:** Write

- **   [CreateSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateSAMLProvider.html)  **
  - **Description:** Grants permission to create an IAM resource that describes an identity provider (IdP) that supports SAML 2.0
  - **Resource types (\*required):** [saml-provider\*](#list_iam-resource-saml-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html)  **
  - **Description:** Grants permission to create an IAM role that allows an AWS service to perform actions on your behalf
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:AWSServiceName](#list_iam-iam_AWSServiceName)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceSpecificCredential.html)  **
  - **Description:** Grants permission to create a new service-specific credential for an IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:ServiceSpecificCredentialAgeDays](#list_iam-iam_ServiceSpecificCredentialAgeDays)<br />[iam:ServiceSpecificCredentialServiceName](#list_iam-iam_ServiceSpecificCredentialServiceName)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateUser.html)  **
  - **Description:** Grants permission to create a new IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateVirtualMFADevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateVirtualMFADevice.html)  **
  - **Description:** Grants permission to create a new virtual MFA device
  - **Resource types (\*required):** [mfa\*](#list_iam-resource-mfa)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Write

- **   [DeactivateMFADevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeactivateMFADevice.html)  **
  - **Description:** Grants permission to deactivate the specified MFA device and remove its association with the IAM user for which it was originally enabled
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccessKey.html)  **
  - **Description:** Grants permission to delete the access key pair that is associated with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAccountAlias](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccountAlias.html)  **
  - **Description:** Grants permission to delete the specified AWS account alias
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccountPasswordPolicy.html)  **
  - **Description:** Grants permission to delete the password policy for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeleteCloudFrontPublicKey](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html)  **
  - **Description:** Grants permission to delete an existing CloudFront public key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteGroup.html)  **
  - **Description:** Grants permission to delete the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteGroupPolicy.html)  **
  - **Description:** Grants permission to delete the specified inline policy from its group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeleteInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteInstanceProfile.html)  **
  - **Description:** Grants permission to delete the specified instance profile
  - **Resource types (\*required):** [instance-profile\*](#list_iam-resource-instance-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteLoginProfile.html)  **
  - **Description:** Grants permission to delete the password for the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteOpenIDConnectProvider.html)  **
  - **Description:** Grants permission to delete an OpenID Connect identity provider (IdP) resource object in IAM
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to delete the specified managed policy and remove it from any IAM entities (users, groups, or roles) to which it is attached
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeletePolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeletePolicyVersion.html)  **
  - **Description:** Grants permission to delete a version from the specified managed policy
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteRole.html)  **
  - **Description:** Grants permission to delete the specified role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRolePermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteRolePermissionsBoundary.html)  **
  - **Description:** Grants permission to remove the permissions boundary from a role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteRolePolicy.html)  **
  - **Description:** Grants permission to delete the specified inline policy from the specified role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSAMLProvider.html)  **
  - **Description:** Grants permission to delete a SAML provider resource in IAM
  - **Resource types (\*required):** [saml-provider\*](#list_iam-resource-saml-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSSHPublicKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSSHPublicKey.html)  **
  - **Description:** Grants permission to delete the specified SSH public key
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServerCertificate.html)  **
  - **Description:** Grants permission to delete the specified server certificate
  - **Resource types (\*required):** [server-certificate\*](#list_iam-resource-server-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceLinkedRole.html)  **
  - **Description:** Grants permission to delete an IAM role that is linked to a specific AWS service, if the service is no longer using it
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceSpecificCredential.html)  **
  - **Description:** Grants permission to delete the specified service-specific credential for an IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:ServiceSpecificCredentialServiceName](#list_iam-iam_ServiceSpecificCredentialServiceName)
  - **Access level:** Write

- **   [DeleteSigningCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSigningCertificate.html)  **
  - **Description:** Grants permission to delete a signing certificate that is associated with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserPermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteUserPermissionsBoundary.html)  **
  - **Description:** Grants permission to remove the permissions boundary from the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteUserPolicy.html)  **
  - **Description:** Grants permission to delete the specified inline policy from an IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteVirtualMFADevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteVirtualMFADevice.html)  **
  - **Description:** Grants permission to delete a virtual MFA device
  - **Resource types (\*required):** [mfa](#list_iam-resource-mfa) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [sms-mfa](#list_iam-resource-sms-mfa) / **Condition keys:**  
  - **Access level:** Write

- **   [DetachGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DetachGroupPolicy.html)  **
  - **Description:** Grants permission to detach a managed policy from the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:** [iam:PolicyARN](#list_iam-iam_PolicyARN)
  - **Access level:** Permissions management, Write

- **   [DetachRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DetachRolePolicy.html)  **
  - **Description:** Grants permission to detach a managed policy from the specified role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:PolicyARN](#list_iam-iam_PolicyARN)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DetachUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DetachUserPolicy.html)  **
  - **Description:** Grants permission to detach a managed policy from the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:PolicyARN](#list_iam-iam_PolicyARN)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DisableOrganizationsRootCredentialsManagement](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DisableOrganizationsRootCredentialsManagement.html)  **
  - **Description:** Grants permission to disable the management of member account root user credentials for an organization managed under the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableOrganizationsRootSessions](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DisableOrganizationsRootSessions.html)  **
  - **Description:** Grants permission to disable privileged root actions in member accounts for an organization managed under the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableOutboundWebIdentityFederation](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddClientIDToOpenIDConnectProvider.html)  **
  - **Description:** Disables the outbound identity federation feature for the callers account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableMFADevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableMFADevice.html)  **
  - **Description:** Grants permission to enable an MFA device and associate it with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:FIDO-certification](#list_iam-iam_FIDO-certification)<br />[iam:FIDO-FIPS-140-2-certification](#list_iam-iam_FIDO-FIPS-140-2-certification)<br />[iam:FIDO-FIPS-140-3-certification](#list_iam-iam_FIDO-FIPS-140-3-certification)<br />[iam:RegisterSecurityKey](#list_iam-iam_RegisterSecurityKey)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableOrganizationsRootCredentialsManagement](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableOrganizationsRootCredentialsManagement.html)  **
  - **Description:** Grants permission to enable the management of member account root user credentials for an organization managed under the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableOrganizationsRootSessions](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableOrganizationsRootSessions.html)  **
  - **Description:** Grants permission to enable privileged root actions in member accounts for an organization managed under the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableOutboundWebIdentityFederation](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableOutboundWebIdentityFederation.html)  **
  - **Description:** Enables the outbound identity federation feature for the callers account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GenerateCredentialReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateCredentialReport.html)  **
  - **Description:** Grants permission to generate a credential report for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GenerateOrganizationsAccessReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateOrganizationsAccessReport.html)  **
  - **Description:** Grants permission to generate an access report for an AWS Organizations entity
  - **Resource types (\*required):** [access-report\*](#list_iam-resource-access-report)
  - **Condition keys:** [iam:OrganizationsPolicyId](#list_iam-iam_OrganizationsPolicyId)
  - **Access level:** Read

- **   [GenerateServiceLastAccessedDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateServiceLastAccessedDetails.html)  **
  - **Description:** Grants permission to generate a service last accessed data report for an IAM resource
  - **Resource types (\*required):** [group\*](#list_iam-resource-group) / **Condition keys:**  
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [role\*](#list_iam-resource-role) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user\*](#list_iam-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAccessKeyLastUsed](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccessKeyLastUsed.html)  **
  - **Description:** Grants permission to retrieve information about when the specified access key was last used
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html)  **
  - **Description:** Grants permission to retrieve information about all IAM users, groups, roles, and policies in your AWS account, including their relationships to one another
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccountEmailAddress](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html)  **
  - **Description:** Grants permission to retrieve the email address that is associated with the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccountName](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html)  **
  - **Description:** Grants permission to retrieve the account name that is associated with the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html)  **
  - **Description:** Grants permission to retrieve the password policy for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccountProperties](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountProperties.html)  **
  - **Description:** Grants permission to retrieve account-level properties for IAM features
  - **Resource types (\*required):** 
  - **Condition keys:** [iam:AccountPropertyNamespaces](#list_iam-iam_AccountPropertyNamespaces)
  - **Access level:** Read

- **   [GetAccountSummary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountSummary.html)  **
  - **Description:** Grants permission to retrieve information about IAM entity usage and IAM quotas in the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetCloudFrontPublicKey](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html)  **
  - **Description:** Grants permission to retrieve information about the specified CloudFront public key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetContextKeysForCustomPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForCustomPolicy.html)  **
  - **Description:** Grants permission to retrieve a list of all of the context keys that are referenced in the specified policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetContextKeysForPrincipalPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForPrincipalPolicy.html)  **
  - **Description:** Grants permission to retrieve a list of all context keys that are referenced in all IAM policies that are attached to the specified IAM identity (user, group, or role)
  - **Resource types (\*required):** [group](#list_iam-resource-group) / **Condition keys:**  
  - **Resource types (\*required):** [role](#list_iam-resource-role) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user](#list_iam-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCredentialReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetCredentialReport.html)  **
  - **Description:** Grants permission to retrieve a credential report for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetDelegationRequest.html)  **
  - **Description:** Retrieves information about a specific delegation request
  - **Resource types (\*required):** [delegation-request\*](#list_iam-resource-delegation-request)
  - **Condition keys:** [iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner)
  - **Access level:** Read

- **   [GetGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroup.html)  **
  - **Description:** Grants permission to retrieve a list of IAM users in the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroupPolicy.html)  **
  - **Description:** Grants permission to retrieve an inline policy document that is embedded in the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetHumanReadableSummary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetHumanReadableSummary.html)  **
  - **Description:** Retrieves a human readable summary for a given entity. At this time, only delegation request are supported
  - **Resource types (\*required):** [delegation-request\*](#list_iam-resource-delegation-request)
  - **Condition keys:** [iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner)
  - **Access level:** Read

- **   [GetInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetInstanceProfile.html)  **
  - **Description:** Grants permission to retrieve information about the specified instance profile, including the instance profile's path, GUID, ARN, and role
  - **Resource types (\*required):** [instance-profile\*](#list_iam-resource-instance-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetLoginProfile.html)  **
  - **Description:** Grants permission to retrieve the user name and password creation date for the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetMFADevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetMFADevice.html)  **
  - **Description:** Grants permission to retrieve information about an MFA device for the specified user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOpenIDConnectProvider.html)  **
  - **Description:** Grants permission to retrieve information about the specified OpenID Connect (OIDC) provider resource in IAM
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOrganizationsAccessReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOrganizationsAccessReport.html)  **
  - **Description:** Grants permission to retrieve an AWS Organizations access report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOutboundWebIdentityFederationInfo](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOutboundWebIdentityFederationInfo.html)  **
  - **Description:** Retrieves the configuration information for the outbound identity federation feature for the callers account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicy.html)  **
  - **Description:** Grants permission to retrieve information about the specified managed policy, including the policy's default version and the total number of identities to which the policy is attached
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicyVersion.html)  **
  - **Description:** Grants permission to retrieve information about a version of the specified managed policy, including the policy document
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html)  **
  - **Description:** Grants permission to retrieve information about the specified role, including the role's path, GUID, ARN, and the role's trust policy
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:RoleTemplateARN](#list_iam-iam_RoleTemplateARN)
  - **Access level:** Read

- **   [GetRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRolePolicy.html)  **
  - **Description:** Grants permission to retrieve an inline policy document that is embedded with the specified IAM role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRoleTemplateVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRoleTemplateVersion.html)  **
  - **Description:** Grants permission to retrieve information about a specific version of a role template
  - **Resource types (\*required):** [role-template\*](#list_iam-resource-role-template)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html)  **
  - **Description:** Grants permission to retrieve the SAML provider metadocument that was uploaded when the IAM SAML provider resource was created or updated
  - **Resource types (\*required):** [saml-provider\*](#list_iam-resource-saml-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSSHPublicKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSSHPublicKey.html)  **
  - **Description:** Grants permission to retrieve the specified SSH public key, including metadata about the key
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServerCertificate.html)  **
  - **Description:** Grants permission to retrieve information about the specified server certificate stored in IAM
  - **Resource types (\*required):** [server-certificate\*](#list_iam-resource-server-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceLastAccessedDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetails.html)  **
  - **Description:** Grants permission to retrieve information about the service last accessed data report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceLastAccessedDetailsWithEntities](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetailsWithEntities.html)  **
  - **Description:** Grants permission to retrieve information about the entities from the service last accessed data report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceLinkedRoleDeletionStatus](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.html)  **
  - **Description:** Grants permission to retrieve an IAM service-linked role deletion status
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUser.html)  **
  - **Description:** Grants permission to retrieve information about the specified IAM user, including the user's creation date, path, unique ID, and ARN
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUserPolicy.html)  **
  - **Description:** Grants permission to retrieve an inline policy document that is embedded in the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccessKeys](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html)  **
  - **Description:** Grants permission to list information about the access key IDs that are associated with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAccountAliases](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccountAliases.html)  **
  - **Description:** Grants permission to list the account alias that is associated with the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAttachedGroupPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedGroupPolicies.html)  **
  - **Description:** Grants permission to list all managed policies that are attached to the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAttachedRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedRolePolicies.html)  **
  - **Description:** Grants permission to list all managed policies that are attached to the specified IAM role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAttachedUserPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedUserPolicies.html)  **
  - **Description:** Grants permission to list all managed policies that are attached to the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCloudFrontPublicKeys](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html)  **
  - **Description:** Grants permission to list all current CloudFront public keys for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDelegationRequests](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListDelegationRequests.html)  **
  - **Description:** Lists delegation requests based on the specified criteria
  - **Resource types (\*required):** 
  - **Condition keys:** [iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner)
  - **Access level:** List

- **   [ListEntitiesForPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListEntitiesForPolicy.html)  **
  - **Description:** Grants permission to list all IAM identities to which the specified managed policy is attached
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGroupPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupPolicies.html)  **
  - **Description:** Grants permission to list the names of the inline policies that are embedded in the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroups.html)  **
  - **Description:** Grants permission to list the IAM groups that have the specified path prefix
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroupsForUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupsForUser.html)  **
  - **Description:** Grants permission to list the IAM groups that the specified IAM user belongs to
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInstanceProfileTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListInstanceProfileTags.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified instance profile
  - **Resource types (\*required):** [instance-profile\*](#list_iam-resource-instance-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInstanceProfiles](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListInstanceProfiles.html)  **
  - **Description:** Grants permission to list the instance profiles that have the specified path prefix
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInstanceProfilesForRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListInstanceProfilesForRole.html)  **
  - **Description:** Grants permission to list the instance profiles that have the specified associated IAM role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMFADeviceTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListMFADeviceTags.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified virtual mfa device
  - **Resource types (\*required):** [mfa\*](#list_iam-resource-mfa)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMFADevices](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListMFADevices.html)  **
  - **Description:** Grants permission to list the MFA devices for an IAM user
  - **Resource types (\*required):** [user](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListOpenIDConnectProviderTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviderTags.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified OpenID Connect provider
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListOpenIDConnectProviders](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html)  **
  - **Description:** Grants permission to list information about the IAM OpenID Connect (OIDC) provider resource objects that are defined in the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationsFeatures](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOrganizationsFeatures.html)  **
  - **Description:** Grants permission to list the centralized root access features enabled for your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html)  **
  - **Description:** Grants permission to list all managed policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPoliciesGrantingServiceAccess](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPoliciesGrantingServiceAccess.html)  **
  - **Description:** Grants permission to list information about the policies that grant an entity access to a specific service
  - **Resource types (\*required):** [group\*](#list_iam-resource-group) / **Condition keys:**  
  - **Resource types (\*required):** [role\*](#list_iam-resource-role) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user\*](#list_iam-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicyTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicyTags.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified managed policy
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicyVersions](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicyVersions.html)  **
  - **Description:** Grants permission to list information about the versions of the specified managed policy, including the version that is currently set as the policy's default version
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRolePolicies.html)  **
  - **Description:** Grants permission to list the names of the inline policies that are embedded in the specified IAM role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRoleTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoleTags.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified IAM role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRoles](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoles.html)  **
  - **Description:** Grants permission to list the IAM roles that have the specified path prefix
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSAMLProviderTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSAMLProviderTags.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified SAML provider
  - **Resource types (\*required):** [saml-provider\*](#list_iam-resource-saml-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSAMLProviders](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSAMLProviders.html)  **
  - **Description:** Grants permission to list the SAML provider resources in IAM
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSSHPublicKeys](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSSHPublicKeys.html)  **
  - **Description:** Grants permission to list information about the SSH public keys that are associated with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSTSRegionalEndpointsStatus](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html)  **
  - **Description:** Grants permission to list the status of all active STS regional endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServerCertificateTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServerCertificateTags.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified server certificate
  - **Resource types (\*required):** [server-certificate\*](#list_iam-resource-server-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServerCertificates](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServerCertificates.html)  **
  - **Description:** Grants permission to list the server certificates that have the specified path prefix
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceSpecificCredentials](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServiceSpecificCredentials.html)  **
  - **Description:** Grants permission to list the service-specific credentials that are associated with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSigningCertificates](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSigningCertificates.html)  **
  - **Description:** Grants permission to list information about the signing certificates that are associated with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUserPolicies.html)  **
  - **Description:** Grants permission to list the names of the inline policies that are embedded in the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUserTags.html)  **
  - **Description:** Grants permission to list the tags that are attached to the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUsers](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html)  **
  - **Description:** Grants permission to list the IAM users that have the specified path prefix
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVirtualMFADevices](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListVirtualMFADevices.html)  **
  - **Description:** Grants permission to list virtual MFA devices by assignment status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutAccountProperties](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutAccountProperties.html)  **
  - **Description:** Grants permission to set account-level properties for IAM features
  - **Resource types (\*required):** 
  - **Condition keys:** [iam:AccountPropertyNamespaces](#list_iam-iam_AccountPropertyNamespaces)
  - **Access level:** Write

- **   [PutGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutGroupPolicy.html)  **
  - **Description:** Grants permission to create or update an inline policy document that is embedded in the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutRolePermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePermissionsBoundary.html)  **
  - **Description:** Grants permission to set a managed policy as a permissions boundary for a role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:RoleTemplateARN](#list_iam-iam_RoleTemplateARN)
  - **Access level:** Permissions management, Write

- **   [PutRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePolicy.html)  **
  - **Description:** Grants permission to create or update an inline policy document that is embedded in the specified IAM role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:RoleTemplateARN](#list_iam-iam_RoleTemplateARN)
  - **Access level:** Permissions management, Write

- **   [PutUserPermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutUserPermissionsBoundary.html)  **
  - **Description:** Grants permission to set a managed policy as a permissions boundary for an IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutUserPolicy.html)  **
  - **Description:** Grants permission to create or update an inline policy document that is embedded in the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RejectDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_RejectDelegationRequest.html)  **
  - **Description:** Rejects a delegation request, denying the requested temporary access
  - **Resource types (\*required):** [delegation-request\*](#list_iam-resource-delegation-request)
  - **Condition keys:** [iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner)
  - **Access level:** Write

- **   [RemoveClientIDFromOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveClientIDFromOpenIDConnectProvider.html)  **
  - **Description:** Grants permission to remove the client ID (audience) from the list of client IDs in the specified IAM OpenID Connect (OIDC) provider resource
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveRoleFromInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveRoleFromInstanceProfile.html)  **
  - **Description:** Grants permission to remove an IAM role from the specified EC2 instance profile
  - **Resource types (\*required):** [instance-profile\*](#list_iam-resource-instance-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveUserFromGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveUserFromGroup.html)  **
  - **Description:** Grants permission to remove an IAM user from the specified group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ResetServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResetServiceSpecificCredential.html)  **
  - **Description:** Grants permission to reset the password for an existing service-specific credential for an IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:ServiceSpecificCredentialServiceName](#list_iam-iam_ServiceSpecificCredentialServiceName)
  - **Access level:** Write

- **   [ResyncMFADevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResyncMFADevice.html)  **
  - **Description:** Grants permission to synchronize the specified MFA device with its IAM entity (user or role)
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendDelegationToken](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SendDelegationToken.html)  **
  - **Description:** Sends the exchange token for an accepted delegation request
  - **Resource types (\*required):** [delegation-request\*](#list_iam-resource-delegation-request)
  - **Condition keys:** [iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner)
  - **Access level:** Write

- **   [SetDefaultPolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetDefaultPolicyVersion.html)  **
  - **Description:** Grants permission to set the version of the specified policy as the policy's default version
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [SetSTSRegionalEndpointStatus](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html)  **
  - **Description:** Grants permission to activate or deactivate an STS regional endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetSecurityTokenServicePreferences](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetSecurityTokenServicePreferences.html)  **
  - **Description:** Grants permission to set the STS global endpoint token version
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SimulateCustomPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulateCustomPolicy.html)  **
  - **Description:** Grants permission to simulate whether an identity-based policy or resource-based policy provides permissions for specific API operations and resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SimulatePrincipalPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulatePrincipalPolicy.html)  **
  - **Description:** Grants permission to simulate whether an identity-based policy that is attached to a specified IAM entity (user or role) provides permissions for specific API operations and resources
  - **Resource types (\*required):** [group](#list_iam-resource-group) / **Condition keys:**  
  - **Resource types (\*required):** [role](#list_iam-resource-role) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user](#list_iam-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagInstanceProfile.html)  **
  - **Description:** Grants permission to add tags to an instance profile
  - **Resource types (\*required):** [instance-profile\*](#list_iam-resource-instance-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagMFADevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagMFADevice.html)  **
  - **Description:** Grants permission to add tags to a virtual mfa device
  - **Resource types (\*required):** [mfa\*](#list_iam-resource-mfa)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagOpenIDConnectProvider.html)  **
  - **Description:** Grants permission to add tags to an OpenID Connect provider
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagPolicy.html)  **
  - **Description:** Grants permission to add tags to a managed policy
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagRole.html)  **
  - **Description:** Grants permission to add tags to an IAM role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:RoleTemplateARN](#list_iam-iam_RoleTemplateARN)
  - **Access level:** Tagging, Write

- **   [TagSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagSAMLProvider.html)  **
  - **Description:** Grants permission to add tags to a SAML Provider
  - **Resource types (\*required):** [saml-provider\*](#list_iam-resource-saml-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagServerCertificate.html)  **
  - **Description:** Grants permission to add tags to a server certificate
  - **Resource types (\*required):** [server-certificate\*](#list_iam-resource-server-certificate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_TagUser.html)  **
  - **Description:** Grants permission to add tags to an IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagInstanceProfile.html)  **
  - **Description:** Grants permission to remove the specified tags from the instance profile
  - **Resource types (\*required):** [instance-profile\*](#list_iam-resource-instance-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagMFADevice](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagMFADevice.html)  **
  - **Description:** Grants permission to remove the specified tags from the virtual mfa device
  - **Resource types (\*required):** [mfa\*](#list_iam-resource-mfa)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagOpenIDConnectProvider.html)  **
  - **Description:** Grants permission to remove the specified tags from the OpenID Connect provider
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagPolicy.html)  **
  - **Description:** Grants permission to remove the specified tags from the managed policy
  - **Resource types (\*required):** [policy\*](#list_iam-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagRole.html)  **
  - **Description:** Grants permission to remove the specified tags from the role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagSAMLProvider.html)  **
  - **Description:** Grants permission to remove the specified tags from the SAML Provider
  - **Resource types (\*required):** [saml-provider\*](#list_iam-resource-saml-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagServerCertificate.html)  **
  - **Description:** Grants permission to remove the specified tags from the server certificate
  - **Resource types (\*required):** [server-certificate\*](#list_iam-resource-server-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UntagUser.html)  **
  - **Description:** Grants permission to remove the specified tags from the user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccessKey.html)  **
  - **Description:** Grants permission to update the status of the specified access key as Active or Inactive
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAccountEmailAddress](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html)  **
  - **Description:** Grants permission to update the email address that is associated with the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAccountName](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html)  **
  - **Description:** Grants permission to update the account name that is associated with the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccountPasswordPolicy.html)  **
  - **Description:** Grants permission to update the password policy settings for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAssumeRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAssumeRolePolicy.html)  **
  - **Description:** Grants permission to update the policy that grants an IAM entity permission to assume a role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateCloudFrontPublicKey](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html)  **
  - **Description:** Grants permission to update an existing CloudFront public key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateGroup.html)  **
  - **Description:** Grants permission to update the name or path of the specified IAM group
  - **Resource types (\*required):** [group\*](#list_iam-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateLoginProfile.html)  **
  - **Description:** Grants permission to change the password for the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOpenIDConnectProviderThumbprint](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateOpenIDConnectProviderThumbprint.html)  **
  - **Description:** Grants permission to update the entire list of server certificate thumbprints that are associated with an OpenID Connect (OIDC) provider resource
  - **Resource types (\*required):** [oidc-provider\*](#list_iam-resource-oidc-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateRole.html)  **
  - **Description:** Grants permission to update the description or maximum session duration setting of a role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRoleDescription](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateRoleDescription.html)  **
  - **Description:** Grants permission to update only the description of a role
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:PermissionsBoundary](#list_iam-iam_PermissionsBoundary)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSAMLProvider.html)  **
  - **Description:** Grants permission to update the metadata document for an existing SAML provider resource
  - **Resource types (\*required):** [saml-provider\*](#list_iam-resource-saml-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSSHPublicKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSSHPublicKey.html)  **
  - **Description:** Grants permission to update the status of an IAM user's SSH public key to active or inactive
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateServerCertificate.html)  **
  - **Description:** Grants permission to update the name or the path of the specified server certificate stored in IAM
  - **Resource types (\*required):** [server-certificate\*](#list_iam-resource-server-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html)  **
  - **Description:** Grants permission to update the status of a service-specific credential to active or inactive for an IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)<br />[iam:ServiceSpecificCredentialServiceName](#list_iam-iam_ServiceSpecificCredentialServiceName)
  - **Access level:** Write

- **   [UpdateSigningCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSigningCertificate.html)  **
  - **Description:** Grants permission to update the status of the specified user signing certificate to active or disabled
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateUser.html)  **
  - **Description:** Grants permission to update the name or the path of the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UploadCloudFrontPublicKey](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html)  **
  - **Description:** Grants permission to upload a CloudFront public key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UploadSSHPublicKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadSSHPublicKey.html)  **
  - **Description:** Grants permission to upload an SSH public key and associate it with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UploadServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadServerCertificate.html)  **
  - **Description:** Grants permission to upload a server certificate entity for the AWS account
  - **Resource types (\*required):** [server-certificate\*](#list_iam-resource-server-certificate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-aws_TagKeys)
  - **Access level:** Write

- **   [UploadSigningCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadSigningCertificate.html)  **
  - **Description:** Grants permission to upload an X.509 signing certificate and associate it with the specified IAM user
  - **Resource types (\*required):** [user\*](#list_iam-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Identity and Access Management (IAM)
<a name="list_iam-permission-only-actions"></a>

The following actions are defined by AWS Identity and Access Management (IAM) but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  **
  - **Description:** Grants permission to pass a role to a service
  - **Resource types (\*required):** [role\*](#list_iam-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:AssociatedResourceArn](#list_iam-iam_AssociatedResourceArn)<br />[iam:PassedToService](#list_iam-iam_PassedToService)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Identity and Access Management (IAM)
<a name="list_iam-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [access-report](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data-orgs.html)  | arn:${Partition}:iam::${Account}:access-report/${EntityPath} |   | 
|  [assumed-role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)  | arn:${Partition}:iam::${Account}:assumed-role/${RoleName}/${RoleSessionName} |   | 
|  [delegation-request](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation.html)  | arn:${Partition}:iam::${Account}:delegation-request/${DelegationRequestId} | [iam:DelegationRequestOwner](#list_iam-iam_DelegationRequestOwner) | 
|  [federated-user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html)  | arn:${Partition}:iam::${Account}:federated-user/${UserName} |   | 
|  [group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)  | arn:${Partition}:iam::${Account}:group/${GroupNameWithPath} |   | 
|  [instance-profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)  | arn:${Partition}:iam::${Account}:instance-profile/${InstanceProfileNameWithPath} | [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_) | 
|  [mfa](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)  | arn:${Partition}:iam::${Account}:mfa/${MfaTokenIdWithPath} | [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_) | 
|  [oidc-provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)  | arn:${Partition}:iam::${Account}:oidc-provider/${OidcProviderName} | [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_) | 
|  [policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html)  | arn:${Partition}:iam::${Account}:policy/${PolicyNameWithPath} | [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_) | 
|  [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)  | arn:${Partition}:iam::${Account}:role/${RoleNameWithPath} | [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_) | 
|  [role-template](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_role-template.html)  | arn:${Partition}:iam::aws:role-template/${AWSServicePrincipal}/${RoleTemplateName}:${RoleTemplateMajorVersion} |   | 
|  [saml-provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html)  | arn:${Partition}:iam::${Account}:saml-provider/${SamlProviderName} | [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_) | 
|  [server-certificate](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)  | arn:${Partition}:iam::${Account}:server-certificate/${CertificateNameWithPath} | [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_) | 
|  [sms-mfa](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)  | arn:${Partition}:iam::${Account}:sms-mfa/${MfaTokenIdWithPath} |   | 
|  [user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)  | arn:${Partition}:iam::${Account}:user/${UserNameWithPath} | [aws:ResourceTag/${TagKey}](#list_iam-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_iam-iam_ResourceTag___TagKey_) | 

## Condition keys for AWS Identity and Access Management (IAM)
<a name="list_iam-policy-keys"></a>

AWS Identity and Access Management (IAM) defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 
|   [iam:AWSServiceName](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_AWSServiceName)  | Filters access by the AWS service to which this role is attached | String | 
|   [iam:AccountPropertyNamespaces](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_AccountPropertyNamespaces)  | Filters access by the account property namespaces being read or modified | ArrayOfString | 
|   [iam:AssociatedResourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_AssociatedResourceArn)  | Filters access by the resource that the role will be used on behalf of | ARN | 
|   [iam:DelegationDuration](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_DelegationDuration)  | Filters access based on the requested delegation duration | String | 
|   [iam:DelegationRequestOwner](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_DelegationRequestOwner)  | Filters access based on the delegation request owner | ARN | 
|   [iam:FIDO-FIPS-140-2-certification](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_FIDO-FIPS-140-2-certification)  | Filters access by the MFA device FIPS-140-2 validation certification level at the time of registration of a FIDO security key | String | 
|   [iam:FIDO-FIPS-140-3-certification](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_FIDO-FIPS-140-3-certification)  | Filters access by the MFA device FIPS-140-3 validation certification level at the time of registration of a FIDO security key | String | 
|   [iam:FIDO-certification](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_FIDO-certification)  | Filters access by the MFA device FIDO certification level at the time of registration of a FIDO security key | String | 
|   [iam:NotificationChannel](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_NotificationChannel)  | Filters access based on the requested notification channel | String | 
|   [iam:OrganizationsPolicyId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_OrganizationsPolicyId)  | Filters access by the ID of an AWS Organizations policy | String | 
|   [iam:PassedToService](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_PassedToService)  | Filters access by the AWS service to which this role is passed | String | 
|   [iam:PermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_PermissionsBoundary)  | Filters access if the specified policy is set as the permissions boundary on the IAM entity (user or role) | ARN | 
|   [iam:PolicyARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_PolicyARN)  | Filters access by the ARN of an IAM policy | ARN | 
|   [iam:RegisterSecurityKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_RegisterSecurityKey)  | Filters access by the current state of MFA device enablement | String | 
|   [iam:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_ResourceTag)  | Filters access by the tags attached to an IAM entity (user or role) | String | 
|   [iam:RoleTemplateARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_RoleTemplateARN)  | Filters access by the role template ARN used in the request | ARN | 
|   [iam:ServiceSpecificCredentialAgeDays](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_ServiceSpecificCredentialAgeDays)  | Filters access by the duration until the credential's expiration | Numeric | 
|   [iam:ServiceSpecificCredentialServiceName](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_ServiceSpecificCredentialServiceName)  | Filters access by the service associated with the credential | String | 
|   [iam:TemplateArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_TemplateArn)  | Filters access based on the requested template ARN | ARN | 