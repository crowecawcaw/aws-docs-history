

# Actions, resources, and condition keys for AWS IAM Identity Center
<a name="list_iam-identity-center"></a>

AWS IAM Identity Center (service prefix: `sso`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sso/sso.json) for this service.

**Topics**
+ [API operations defined by AWS IAM Identity Center](#list_iam-identity-center-operations)
+ [Actions defined by AWS IAM Identity Center](#list_iam-identity-center-actions-as-permissions)
+ [Resource types defined by AWS IAM Identity Center](#list_iam-identity-center-resources-for-iam-policies)
+ [Condition keys for AWS IAM Identity Center](#list_iam-identity-center-policy-keys)

## API operations defined by AWS IAM Identity Center
<a name="list_iam-identity-center-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iam-identity-center-actions-as-permissions).




- **   AddRegion  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:AddRegion](#list_iam-identity-center-action-AddRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachCustomerManagedPolicyReferenceToPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:AttachCustomerManagedPolicyReferenceToPermissionSet](#list_iam-identity-center-action-AttachCustomerManagedPolicyReferenceToPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AttachManagedPolicyToPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:AttachManagedPolicyToPermissionSet](#list_iam-identity-center-action-AttachManagedPolicyToPermissionSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [sso:PutPermissionsPolicy](#list_iam-identity-center-action-PutPermissionsPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateAccountAssignment  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:AssociateProfile](#list_iam-identity-center-action-AssociateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:CreateAccountAssignment](#list_iam-identity-center-action-CreateAccountAssignment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:CreateApplicationInstance](#list_iam-identity-center-action-CreateApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:CreateProfile](#list_iam-identity-center-action-CreateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:CreateTrust](#list_iam-identity-center-action-CreateTrust)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:GetApplicationInstance](#list_iam-identity-center-action-GetApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:GetProfile](#list_iam-identity-center-action-GetProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:GetTrust](#list_iam-identity-center-action-GetTrust)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:UpdateProfile](#list_iam-identity-center-action-UpdateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:UpdateTrust](#list_iam-identity-center-action-UpdateTrust)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateApplication  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:CreateApplication](#list_iam-identity-center-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:CreateApplicationInstance](#list_iam-identity-center-action-CreateApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:CreateManagedApplicationInstance](#list_iam-identity-center-action-CreateManagedApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:PutApplicationAssignmentConfiguration](#list_iam-identity-center-action-PutApplicationAssignmentConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:TagResource](#list_iam-identity-center-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateApplicationAssignment  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:AssociateProfile](#list_iam-identity-center-action-AssociateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:CreateApplicationAssignment](#list_iam-identity-center-action-CreateApplicationAssignment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateInstance  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:CreateInstance](#list_iam-identity-center-action-CreateInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:TagResource](#list_iam-identity-center-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateInstanceAccessControlAttributeConfiguration  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:CreateInstanceAccessControlAttributeConfiguration](#list_iam-identity-center-action-CreateInstanceAccessControlAttributeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:CreatePermissionSet](#list_iam-identity-center-action-CreatePermissionSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:TagResource](#list_iam-identity-center-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTrustedTokenIssuer  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:CreateTrustedTokenIssuer](#list_iam-identity-center-action-CreateTrustedTokenIssuer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:TagResource](#list_iam-identity-center-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccountAssignment  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteAccountAssignment](#list_iam-identity-center-action-DeleteAccountAssignment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:DeleteProfile](#list_iam-identity-center-action-DeleteProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteApplication  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteApplication](#list_iam-identity-center-action-DeleteApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:DeleteApplicationInstance](#list_iam-identity-center-action-DeleteApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:DeleteManagedApplicationInstance](#list_iam-identity-center-action-DeleteManagedApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteApplicationAccessScope  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteApplicationAccessScope](#list_iam-identity-center-action-DeleteApplicationAccessScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationAssignment  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteApplicationAssignment](#list_iam-identity-center-action-DeleteApplicationAssignment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:DisassociateProfile](#list_iam-identity-center-action-DisassociateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteApplicationAuthenticationMethod  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteApplicationAuthenticationMethod](#list_iam-identity-center-action-DeleteApplicationAuthenticationMethod) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplicationGrant  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteApplicationGrant](#list_iam-identity-center-action-DeleteApplicationGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInlinePolicyFromPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteInlinePolicyFromPermissionSet](#list_iam-identity-center-action-DeleteInlinePolicyFromPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInstance  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteInstance](#list_iam-identity-center-action-DeleteInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:StartSSO](#list_iam-identity-center-action-StartSSO)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteInstanceAccessControlAttributeConfiguration  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteInstanceAccessControlAttributeConfiguration](#list_iam-identity-center-action-DeleteInstanceAccessControlAttributeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeletePermissionSet](#list_iam-identity-center-action-DeletePermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePermissionsBoundaryFromPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeletePermissionsBoundaryFromPermissionSet](#list_iam-identity-center-action-DeletePermissionsBoundaryFromPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteTrustedTokenIssuer  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DeleteTrustedTokenIssuer](#list_iam-identity-center-action-DeleteTrustedTokenIssuer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountAssignmentCreationStatus  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeAccountAssignmentCreationStatus](#list_iam-identity-center-action-DescribeAccountAssignmentCreationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAccountAssignmentDeletionStatus  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeAccountAssignmentDeletionStatus](#list_iam-identity-center-action-DescribeAccountAssignmentDeletionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApplication  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeApplication](#list_iam-identity-center-action-DescribeApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:GetApplicationInstance](#list_iam-identity-center-action-GetApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:GetManagedApplicationInstance](#list_iam-identity-center-action-GetManagedApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeApplicationAssignment  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeApplicationAssignment](#list_iam-identity-center-action-DescribeApplicationAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApplicationProvider  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeApplicationProvider](#list_iam-identity-center-action-DescribeApplicationProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:GetApplicationTemplate](#list_iam-identity-center-action-GetApplicationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeInstance  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeInstance](#list_iam-identity-center-action-DescribeInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:GetSharedSsoConfiguration](#list_iam-identity-center-action-GetSharedSsoConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:ListDirectoryAssociations](#list_iam-identity-center-action-ListDirectoryAssociations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeInstanceAccessControlAttributeConfiguration  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeInstanceAccessControlAttributeConfiguration](#list_iam-identity-center-action-DescribeInstanceAccessControlAttributeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribePermissionSet](#list_iam-identity-center-action-DescribePermissionSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:GetPermissionSet](#list_iam-identity-center-action-GetPermissionSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribePermissionSetProvisioningStatus  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribePermissionSetProvisioningStatus](#list_iam-identity-center-action-DescribePermissionSetProvisioningStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegion  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeRegion](#list_iam-identity-center-action-DescribeRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrustedTokenIssuer  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DescribeTrustedTokenIssuer](#list_iam-identity-center-action-DescribeTrustedTokenIssuer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetachCustomerManagedPolicyReferenceFromPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DetachCustomerManagedPolicyReferenceFromPermissionSet](#list_iam-identity-center-action-DetachCustomerManagedPolicyReferenceFromPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DetachManagedPolicyFromPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:DetachManagedPolicyFromPermissionSet](#list_iam-identity-center-action-DetachManagedPolicyFromPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   GetApplicationAccessScope  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetApplicationAccessScope](#list_iam-identity-center-action-GetApplicationAccessScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationAssignmentConfiguration  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetApplicationAssignmentConfiguration](#list_iam-identity-center-action-GetApplicationAssignmentConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationAuthenticationMethod  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetApplicationAuthenticationMethod](#list_iam-identity-center-action-GetApplicationAuthenticationMethod) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationGrant  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetApplicationGrant](#list_iam-identity-center-action-GetApplicationGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationSessionConfiguration  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetApplicationSessionConfiguration](#list_iam-identity-center-action-GetApplicationSessionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInlinePolicyForPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetInlinePolicyForPermissionSet](#list_iam-identity-center-action-GetInlinePolicyForPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPermissionsBoundaryForPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetPermissionsBoundaryForPermissionSet](#list_iam-identity-center-action-GetPermissionsBoundaryForPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccountAssignmentCreationStatus  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListAccountAssignmentCreationStatus](#list_iam-identity-center-action-ListAccountAssignmentCreationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccountAssignmentDeletionStatus  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListAccountAssignmentDeletionStatus](#list_iam-identity-center-action-ListAccountAssignmentDeletionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccountAssignments  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListAccountAssignments](#list_iam-identity-center-action-ListAccountAssignments)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso:ListProfileAssociations](#list_iam-identity-center-action-ListProfileAssociations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListAccountAssignmentsForPrincipal  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListAccountAssignmentsForPrincipal](#list_iam-identity-center-action-ListAccountAssignmentsForPrincipal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAccountsForProvisionedPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetApplicationInstance](#list_iam-identity-center-action-GetApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:ListAccountsForProvisionedPermissionSet](#list_iam-identity-center-action-ListAccountsForProvisionedPermissionSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso:ListApplicationInstances](#list_iam-identity-center-action-ListApplicationInstances)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListApplicationAccessScopes  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListApplicationAccessScopes](#list_iam-identity-center-action-ListApplicationAccessScopes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplicationAssignments  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListApplicationAssignments](#list_iam-identity-center-action-ListApplicationAssignments)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso:ListProfileAssociations](#list_iam-identity-center-action-ListProfileAssociations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListApplicationAssignmentsForPrincipal  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListApplicationAssignmentsForPrincipal](#list_iam-identity-center-action-ListApplicationAssignmentsForPrincipal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplicationAuthenticationMethods  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListApplicationAuthenticationMethods](#list_iam-identity-center-action-ListApplicationAuthenticationMethods) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplicationGrants  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListApplicationGrants](#list_iam-identity-center-action-ListApplicationGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplicationProviders  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetApplicationTemplate](#list_iam-identity-center-action-GetApplicationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:ListApplicationProviders](#list_iam-identity-center-action-ListApplicationProviders)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso:ListApplicationTemplates](#list_iam-identity-center-action-ListApplicationTemplates)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListApplications  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetApplicationInstance](#list_iam-identity-center-action-GetApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:ListApplicationInstances](#list_iam-identity-center-action-ListApplicationInstances)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso:ListApplicationProviders](#list_iam-identity-center-action-ListApplicationProviders)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso:ListApplications](#list_iam-identity-center-action-ListApplications)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListCustomerManagedPolicyReferencesInPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListCustomerManagedPolicyReferencesInPermissionSet](#list_iam-identity-center-action-ListCustomerManagedPolicyReferencesInPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstances  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListInstances](#list_iam-identity-center-action-ListInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedPoliciesInPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListManagedPoliciesInPermissionSet](#list_iam-identity-center-action-ListManagedPoliciesInPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPermissionSetProvisioningStatus  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListPermissionSetProvisioningStatus](#list_iam-identity-center-action-ListPermissionSetProvisioningStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPermissionSets  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListPermissionSets](#list_iam-identity-center-action-ListPermissionSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPermissionSetsProvisionedToAccount  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:GetProfile](#list_iam-identity-center-action-GetProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso:ListPermissionSetsProvisionedToAccount](#list_iam-identity-center-action-ListPermissionSetsProvisionedToAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso:ListProfiles](#list_iam-identity-center-action-ListProfiles)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListRegions  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListRegions](#list_iam-identity-center-action-ListRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListTagsForResource](#list_iam-identity-center-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTrustedTokenIssuers  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ListTrustedTokenIssuers](#list_iam-identity-center-action-ListTrustedTokenIssuers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ProvisionPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:ProvisionPermissionSet](#list_iam-identity-center-action-ProvisionPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutApplicationAccessScope  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:PutApplicationAccessScope](#list_iam-identity-center-action-PutApplicationAccessScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutApplicationAssignmentConfiguration  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:PutApplicationAssignmentConfiguration](#list_iam-identity-center-action-PutApplicationAssignmentConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutApplicationAuthenticationMethod  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:CreateManagedApplicationInstance](#list_iam-identity-center-action-CreateManagedApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:PutApplicationAuthenticationMethod](#list_iam-identity-center-action-PutApplicationAuthenticationMethod)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutApplicationGrant  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:CreateManagedApplicationInstance](#list_iam-identity-center-action-CreateManagedApplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:PutApplicationGrant](#list_iam-identity-center-action-PutApplicationGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutApplicationSessionConfiguration  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:PutApplicationSessionConfiguration](#list_iam-identity-center-action-PutApplicationSessionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutInlinePolicyToPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:PutInlinePolicyToPermissionSet](#list_iam-identity-center-action-PutInlinePolicyToPermissionSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:PutPermissionsPolicy](#list_iam-identity-center-action-PutPermissionsPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   PutPermissionsBoundaryToPermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:PutPermissionsBoundaryToPermissionSet](#list_iam-identity-center-action-PutPermissionsBoundaryToPermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RemoveRegion  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:RemoveRegion](#list_iam-identity-center-action-RemoveRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:TagResource](#list_iam-identity-center-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:UntagResource](#list_iam-identity-center-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:PutApplicationAssignmentConfiguration](#list_iam-identity-center-action-PutApplicationAssignmentConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:UpdateApplication](#list_iam-identity-center-action-UpdateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:UpdateApplicationInstanceDisplayData](#list_iam-identity-center-action-UpdateApplicationInstanceDisplayData)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:UpdateApplicationInstanceStatus](#list_iam-identity-center-action-UpdateApplicationInstanceStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso:UpdateManagedApplicationInstanceStatus](#list_iam-identity-center-action-UpdateManagedApplicationInstanceStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateInstance  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:UpdateInstance](#list_iam-identity-center-action-UpdateInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInstanceAccessControlAttributeConfiguration  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:UpdateInstanceAccessControlAttributeConfiguration](#list_iam-identity-center-action-UpdateInstanceAccessControlAttributeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePermissionSet  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:UpdatePermissionSet](#list_iam-identity-center-action-UpdatePermissionSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateTrustedTokenIssuer  **
  - **SDK client:** sso-admin
  - **IAM action:**  [sso:UpdateTrustedTokenIssuer](#list_iam-identity-center-action-UpdateTrustedTokenIssuer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IAM Identity Center
<a name="list_iam-identity-center-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AddRegion.html)  **
  - **Description:** Grants permission to add a region to an IAM Identity Center instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [AssociateDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to connect a directory to be used by AWS IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to create an association between a directory user or group and a profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AttachCustomerManagedPolicyReferenceToPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AttachCustomerManagedPolicyReferenceToPermissionSet.html)  **
  - **Description:** Grants permission to attach a customer managed policy reference to a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [AttachManagedPolicyToPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AttachManagedPolicyToPermissionSet.html)  **
  - **Description:** Grants permission to attach an AWS managed policy to a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [CreateAccountAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateAccountAssignment.html)  **
  - **Description:** Grants permission to assign access to a Principal for a specified AWS account using a specified permission set
  - **Resource types (\*required):** [Account\*](#list_iam-identity-center-resource-Account) / **Condition keys:**  
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [ApplicationProvider\*](#list_iam-identity-center-resource-ApplicationProvider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [CreateApplicationAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html)  **
  - **Description:** Grants permission to create an application assignment
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [CreateApplicationInstance](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to add an application instance to AWS IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateApplicationInstanceCertificate](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to add a new certificate for an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateInstance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateInstance.html)  **
  - **Description:** Grants permission to create an identity center instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [CreateInstanceAccessControlAttributeConfiguration](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateInstanceAccessControlAttributeConfiguration.html)  **
  - **Description:** Grants permission to enable the instance for ABAC and specify the attributes
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [CreateManagedApplicationInstance](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to add a managed application instance to AWS IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreatePermissionSet.html)  **
  - **Description:** Grants permission to create a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to create a profile for an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateTrust](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to create a federation trust in a target account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateTrustedTokenIssuer](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateTrustedTokenIssuer.html)  **
  - **Description:** Grants permission to create a trusted token issuer for an instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [TrustedTokenIssuer\*](#list_iam-identity-center-resource-TrustedTokenIssuer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteAccountAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteAccountAssignment.html)  **
  - **Description:** Grants permission to delete a Principal's access from a specified AWS account using a specified permission set
  - **Resource types (\*required):** [Account\*](#list_iam-identity-center-resource-Account) / **Condition keys:**  
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteApplicationAccessScope](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAccessScope.html)  **
  - **Description:** Grants permission to delete an access scope to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteApplicationAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAssignment.html)  **
  - **Description:** Grants permission to delete an application assignment
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteApplicationAuthenticationMethod](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAuthenticationMethod.html)  **
  - **Description:** Grants permission to delete an authentication method to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteApplicationGrant](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationGrant.html)  **
  - **Description:** Grants permission to delete a grant from an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteApplicationInstance](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to delete the application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApplicationInstanceCertificate](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to delete an inactive or expired certificate from the application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInlinePolicyFromPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInlinePolicyFromPermissionSet.html)  **
  - **Description:** Grants permission to delete the inline policy from a specified permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteInstance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInstance.html)  **
  - **Description:** Grants permission to delete an identity center instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteInstanceAccessControlAttributeConfiguration](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInstanceAccessControlAttributeConfiguration.html)  **
  - **Description:** Grants permission to disable ABAC and remove the attributes list for the instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteManagedApplicationInstance](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to delete the managed application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeletePermissionSet.html)  **
  - **Description:** Grants permission to delete a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DeletePermissionsBoundaryFromPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeletePermissionsBoundaryFromPermissionSet.html)  **
  - **Description:** Grants permission to remove permissions boundary from a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [DeleteProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to delete the profile for an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTrustedTokenIssuer](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteTrustedTokenIssuer.html)  **
  - **Description:** Grants permission to delete a trusted token issuer for an instance
  - **Resource types (\*required):** [TrustedTokenIssuer\*](#list_iam-identity-center-resource-TrustedTokenIssuer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [DescribeAccountAssignmentCreationStatus](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeAccountAssignmentCreationStatus.html)  **
  - **Description:** Grants permission to describe the status of the assignment creation request
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeAccountAssignmentDeletionStatus](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeAccountAssignmentDeletionStatus.html)  **
  - **Description:** Grants permission to describe the status of an assignment deletion request
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplication.html)  **
  - **Description:** Grants permission to obtain information about an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeApplicationAssignment](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplicationAssignment.html)  **
  - **Description:** Grants permission to retrieve an application assignment
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeApplicationProvider](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplicationProvider.html)  **
  - **Description:** Grants permission to describe an application provider
  - **Resource types (\*required):** [ApplicationProvider\*](#list_iam-identity-center-resource-ApplicationProvider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInstance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstance.html)  **
  - **Description:** Grants permission to obtain information about an identity center instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeInstanceAccessControlAttributeConfiguration](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstanceAccessControlAttributeConfiguration.html)  **
  - **Description:** Grants permission to get the list of attributes used by the instance for ABAC
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribePermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribePermissionSet.html)  **
  - **Description:** Grants permission to describe a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribePermissionSetProvisioningStatus](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribePermissionSetProvisioningStatus.html)  **
  - **Description:** Grants permission to describe the status for the given Permission Set Provisioning request
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeRegion.html)  **
  - **Description:** Grants permission to retrieve configuration details for a specific IAM Identity Center instance region
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeRegisteredRegions](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to obtain the regions where your organization has enabled AWS IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTrustedTokenIssuer](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeTrustedTokenIssuer.html)  **
  - **Description:** Grants permission to describe a trusted token issuer for an instance
  - **Resource types (\*required):** [TrustedTokenIssuer\*](#list_iam-identity-center-resource-TrustedTokenIssuer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [DetachCustomerManagedPolicyReferenceFromPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DetachCustomerManagedPolicyReferenceFromPermissionSet.html)  **
  - **Description:** Grants permission to detach a customer managed policy reference from a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [DetachManagedPolicyFromPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DetachManagedPolicyFromPermissionSet.html)  **
  - **Description:** Grants permission to detach the attached AWS managed policy from the specified permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [DisassociateDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to disassociate a directory to be used by AWS IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to disassociate a directory user or group from a profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetApplicationAccessScope](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAccessScope.html)  **
  - **Description:** Grants permission to get an access scope to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [GetApplicationAssignmentConfiguration](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAssignmentConfiguration.html)  **
  - **Description:** Grants permission to read assignment configurations for an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [GetApplicationAuthenticationMethod](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAuthenticationMethod.html)  **
  - **Description:** Grants permission to get an authentication method to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [GetApplicationGrant](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationGrant.html)  **
  - **Description:** Grants permission to obtain details about a grant belonging to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [GetApplicationInstance](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve details for an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApplicationSessionConfiguration](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationSessionConfiguration.html)  **
  - **Description:** Grants permission to get session configuration for an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [GetApplicationTemplate](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve application template details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInlinePolicyForPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetInlinePolicyForPermissionSet.html)  **
  - **Description:** Grants permission to obtain the inline policy assigned to the permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [GetManagedApplicationInstance](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve details for an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMfaDeviceManagementForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve Mfa Device Management settings for the directory
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve details of a permission set
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPermissionsBoundaryForPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetPermissionsBoundaryForPermissionSet.html)  **
  - **Description:** Grants permission to get permissions boundary for a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [GetProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve a profile for an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSSOStatus](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to check if AWS IAM Identity Center is enabled
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSharedSsoConfiguration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve shared configuration for the current SSO instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSsoConfiguration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve configuration for the current SSO instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTrust](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve the federation trust in a target account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportApplicationInstanceServiceProviderMetadata](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update the application instance by uploading an application SAML metadata file provided by the service provider
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListAccountAssignmentCreationStatus](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentCreationStatus.html)  **
  - **Description:** Grants permission to list the status of the AWS account assignment creation requests for a specified SSO instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListAccountAssignmentDeletionStatus](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentDeletionStatus.html)  **
  - **Description:** Grants permission to list the status of the AWS account assignment deletion requests for a specified SSO instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListAccountAssignments](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignments.html)  **
  - **Description:** Grants permission to list the assignee of the specified AWS account with the specified permission set
  - **Resource types (\*required):** [Account\*](#list_iam-identity-center-resource-Account) / **Condition keys:**  
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListAccountAssignmentsForPrincipal](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentsForPrincipal.html)  **
  - **Description:** Grants permission to list accounts assigned to user or group
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListAccountsForProvisionedPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountsForProvisionedPermissionSet.html)  **
  - **Description:** Grants permission to list all the AWS accounts where the specified permission set is provisioned
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListApplicationAccessScopes](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAccessScopes.html)  **
  - **Description:** Grants permission to list access scopes to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListApplicationAssignments](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAssignments.html)  **
  - **Description:** Grants permission to list application assignments
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListApplicationAssignmentsForPrincipal](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAssignmentsForPrincipal.html)  **
  - **Description:** Grants permission to list applications assigned to user or group
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListApplicationAuthenticationMethods](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAuthenticationMethods.html)  **
  - **Description:** Grants permission to list authentication methods to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListApplicationGrants](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationGrants.html)  **
  - **Description:** Grants permission to list grants from an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListApplicationInstanceCertificates](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve all of the certificates for a given application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListApplicationInstances](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve all application instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApplicationProviders](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationProviders.html)  **
  - **Description:** Grants permission to list application providers
  - **Resource types (\*required):** [ApplicationProvider\*](#list_iam-identity-center-resource-ApplicationProvider)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApplicationTemplates](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve all supported application templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApplications](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to retrieve all applications associated with the instance of IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomerManagedPolicyReferencesInPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListCustomerManagedPolicyReferencesInPermissionSet.html)  **
  - **Description:** Grants permission to list the customer managed policy references that are attached to a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListDirectoryAssociations](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve details about the directory connected to AWS IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListInstances](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html)  **
  - **Description:** Grants permission to list the SSO Instances that the caller has access to
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedPoliciesInPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListManagedPoliciesInPermissionSet.html)  **
  - **Description:** Grants permission to list the AWS managed policies that are attached to a specified permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListPermissionSetProvisioningStatus](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSetProvisioningStatus.html)  **
  - **Description:** Grants permission to list the status of the Permission Set Provisioning requests for a specified SSO instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListPermissionSets](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSets.html)  **
  - **Description:** Grants permission to retrieve all permission sets
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListPermissionSetsProvisionedToAccount](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSetsProvisionedToAccount.html)  **
  - **Description:** Grants permission to list all the permission sets that are provisioned to a specified AWS account
  - **Resource types (\*required):** [Account\*](#list_iam-identity-center-resource-Account) / **Condition keys:**  
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListProfileAssociations](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve the directory user or group associated with the profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListProfiles](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve all profiles for an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegions](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListRegions.html)  **
  - **Description:** Grants permission to list all regions configured for an IAM Identity Center instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags that are attached to a specified resource
  - **Resource types (\*required):** [Application](#list_iam-identity-center-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [Instance](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [TrustedTokenIssuer](#list_iam-identity-center-resource-TrustedTokenIssuer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Read

- **   [ListTrustedTokenIssuers](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListTrustedTokenIssuers.html)  **
  - **Description:** Grants permission to list trusted token issuers for an instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** List

- **   [ProvisionPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ProvisionPermissionSet.html)  **
  - **Description:** Grants permission to provision a specified permission set to the specified target
  - **Resource types (\*required):** [Account\*](#list_iam-identity-center-resource-Account) / **Condition keys:**  
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [PutApplicationAccessScope](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAccessScope.html)  **
  - **Description:** Grants permission to create/update an access scope to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [PutApplicationAssignmentConfiguration](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAssignmentConfiguration.html)  **
  - **Description:** Grants permission to add assignment configurations to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [PutApplicationAuthenticationMethod](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAuthenticationMethod.html)  **
  - **Description:** Grants permission to create/update an authentication method to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [PutApplicationGrant](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationGrant.html)  **
  - **Description:** Grants permission to create/update a grant to an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [PutApplicationSessionConfiguration](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationSessionConfiguration.html)  **
  - **Description:** Grants permission to put session configuration for an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [PutInlinePolicyToPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutInlinePolicyToPermissionSet.html)  **
  - **Description:** Grants permission to attach an IAM inline policy to a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [PutMfaDeviceManagementForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to put Mfa Device Management settings for the directory
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutPermissionsBoundaryToPermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutPermissionsBoundaryToPermissionSet.html)  **
  - **Description:** Grants permission to add permissions boundary to a permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [PutPermissionsPolicy](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to add a policy to a permission set
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RemoveRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_RemoveRegion.html)  **
  - **Description:** Grants permission to remove a region from an IAM Identity Center instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [SearchGroups](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to search for groups within the associated directory
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SearchUsers](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to search for users within the associated directory
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartSSO](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to initialize AWS IAM Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to associate a set of tags with a specified resource
  - **Resource types (\*required):** [Application](#list_iam-identity-center-resource-Application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [Instance](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [TrustedTokenIssuer](#list_iam-identity-center-resource-TrustedTokenIssuer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iam-identity-center-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate a set of tags from a specified resource
  - **Resource types (\*required):** [Application](#list_iam-identity-center-resource-Application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [Instance](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [TrustedTokenIssuer](#list_iam-identity-center-resource-TrustedTokenIssuer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iam-identity-center-aws_TagKeys)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update an application
  - **Resource types (\*required):** [Application\*](#list_iam-identity-center-resource-Application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [UpdateApplicationInstanceActiveCertificate](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to set a certificate as the active one for this application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplicationInstanceDisplayData](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update display data of an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplicationInstanceResponseConfiguration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update federation response configuration for the application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplicationInstanceResponseSchemaConfiguration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update federation response schema configuration for the application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplicationInstanceSecurityConfiguration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update security details for the application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplicationInstanceServiceProviderConfiguration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update service provider related configuration for the application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplicationInstanceStatus](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update the status of an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateInstance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateInstance.html)  **
  - **Description:** Grants permission to update an identity center instance
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [UpdateInstanceAccessControlAttributeConfiguration](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateInstanceAccessControlAttributeConfiguration.html)  **
  - **Description:** Grants permission to update the attributes to use with the instance for ABAC
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write

- **   [UpdateManagedApplicationInstanceStatus](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update the status of a managed application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePermissionSet](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdatePermissionSet.html)  **
  - **Description:** Grants permission to update the permission set
  - **Resource types (\*required):** [Instance\*](#list_iam-identity-center-resource-Instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Resource types (\*required):** [PermissionSet\*](#list_iam-identity-center-resource-PermissionSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [UpdateProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update the profile for an application instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSSOConfiguration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update the configuration for the current SSO instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateTrust](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update the federation trust in a target account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateTrustedTokenIssuer](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateTrustedTokenIssuer.html)  **
  - **Description:** Grants permission to update a trusted token issuer for an instance
  - **Resource types (\*required):** [TrustedTokenIssuer\*](#list_iam-identity-center-resource-TrustedTokenIssuer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion)
  - **Access level:** Write



## Resource types defined by AWS IAM Identity Center
<a name="list_iam-identity-center-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Account](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html)  | arn:${Partition}:sso:::account/${AccountId} |   | 
|  [Application](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Application.html)  | arn:${Partition}:sso::${AccountId}:application/${InstanceId}/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:ApplicationAccount](#list_iam-identity-center-sso_ApplicationAccount)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion) | 
|  [ApplicationProvider](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ApplicationProvider.html)  | arn:${Partition}:sso::aws:applicationProvider/${ApplicationProviderId} |   | 
|  [Instance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_InstanceMetadata.html)  | arn:${Partition}:sso:::instance/${InstanceId} | [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion) | 
|  [PermissionSet](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html)  | arn:${Partition}:sso:::permissionSet/${InstanceId}/${PermissionSetId} | [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion) | 
|  [TrustedTokenIssuer](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TrustedTokenIssuerMetadata.html)  | arn:${Partition}:sso::${AccountId}:trustedTokenIssuer/${InstanceId}/${TrustedTokenIssuerId} | [aws:ResourceTag/${TagKey}](#list_iam-identity-center-aws_ResourceTag___TagKey_)<br />[sso:PrimaryRegion](#list_iam-identity-center-sso_PrimaryRegion) | 

## Condition keys for AWS IAM Identity Center
<a name="list_iam-identity-center-policy-keys"></a>

AWS IAM Identity Center defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging.html)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging.html)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [identitycenter:ApplicationArn](https://docs.aws.amazon.com/singlesignon/latest/userguide/API_Application.html)  | Filters access by the ARN of the IAM Identity Center application | ARN | 
|   [identitycenter:InstanceArn](https://docs.aws.amazon.com/singlesignon/latest/userguide/API_InstanceMetadata.html)  | Filters access by the ARN of the IAM Identity Center instance | ARN | 
|   [sso:ApplicationAccount](https://docs.aws.amazon.com/singlesignon/latest/userguide/API_Application.html)  | Filters access by the account which creates the application. This condition key is not supported for customer managed SAML applications | String | 
|   [sso:PrimaryRegion](https://docs.aws.amazon.com/singlesignon/latest/userguide/API_InstanceMetadata.html)  | Filters access by the primary region of the IAM Identity Center instance | String | 