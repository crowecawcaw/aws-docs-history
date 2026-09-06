

# Actions, resources, and condition keys for Amazon Cognito User Pools
<a name="list_cognito-idp"></a>

Amazon Cognito User Pools (service prefix: `cognito-idp`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cognito/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cognito/latest/developerguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cognito-idp/cognito-idp.json) for this service.

**Topics**
+ [API operations defined by Amazon Cognito User Pools](#list_cognito-idp-operations)
+ [Actions defined by Amazon Cognito User Pools](#list_cognito-idp-actions-as-permissions)
+ [Permission-only actions for Amazon Cognito User Pools](#list_cognito-idp-permission-only-actions)
+ [Resource types defined by Amazon Cognito User Pools](#list_cognito-idp-resources-for-iam-policies)
+ [Condition keys for Amazon Cognito User Pools](#list_cognito-idp-policy-keys)

## API operations defined by Amazon Cognito User Pools
<a name="list_cognito-idp-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cognito-idp-actions-as-permissions).




- **   AddCustomAttributes  **
  - **IAM action:**  [cognito-idp:AddCustomAttributes](#list_cognito-idp-action-AddCustomAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddUserPoolClientSecret  **
  - **IAM action:**  [cognito-idp:AddUserPoolClientSecret](#list_cognito-idp-action-AddUserPoolClientSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminAddUserToGroup  **
  - **IAM action:**  [cognito-idp:AdminAddUserToGroup](#list_cognito-idp-action-AdminAddUserToGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminConfirmSignUp  **
  - **IAM action:**  [cognito-idp:AdminConfirmSignUp](#list_cognito-idp-action-AdminConfirmSignUp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminCreateUser  **
  - **IAM action:**  [cognito-idp:AdminCreateUser](#list_cognito-idp-action-AdminCreateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminDeleteSoftwareToken  **
  - **IAM action:**  [cognito-idp:AdminDeleteSoftwareToken](#list_cognito-idp-action-AdminDeleteSoftwareToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminDeleteUser  **
  - **IAM action:**  [cognito-idp:AdminDeleteUser](#list_cognito-idp-action-AdminDeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminDeleteUserAttributes  **
  - **IAM action:**  [cognito-idp:AdminDeleteUserAttributes](#list_cognito-idp-action-AdminDeleteUserAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminDisableProviderForUser  **
  - **IAM action:**  [cognito-idp:AdminDisableProviderForUser](#list_cognito-idp-action-AdminDisableProviderForUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminDisableUser  **
  - **IAM action:**  [cognito-idp:AdminDisableUser](#list_cognito-idp-action-AdminDisableUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminEnableUser  **
  - **IAM action:**  [cognito-idp:AdminEnableUser](#list_cognito-idp-action-AdminEnableUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminForgetDevice  **
  - **IAM action:**  [cognito-idp:AdminForgetDevice](#list_cognito-idp-action-AdminForgetDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminGetDevice  **
  - **IAM action:**  [cognito-idp:AdminGetDevice](#list_cognito-idp-action-AdminGetDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   AdminGetUser  **
  - **IAM action:**  [cognito-idp:AdminGetUser](#list_cognito-idp-action-AdminGetUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   AdminGetUserAuthFactors  **
  - **IAM action:**  [cognito-idp:AdminGetUserAuthFactors](#list_cognito-idp-action-AdminGetUserAuthFactors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   AdminInitiateAuth  **
  - **IAM action:**  [cognito-idp:AdminInitiateAuth](#list_cognito-idp-action-AdminInitiateAuth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminLinkProviderForUser  **
  - **IAM action:**  [cognito-idp:AdminLinkProviderForUser](#list_cognito-idp-action-AdminLinkProviderForUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminListDevices  **
  - **IAM action:**  [cognito-idp:AdminListDevices](#list_cognito-idp-action-AdminListDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   AdminListGroupsForUser  **
  - **IAM action:**  [cognito-idp:AdminListGroupsForUser](#list_cognito-idp-action-AdminListGroupsForUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   AdminListUserAuthEvents  **
  - **IAM action:**  [cognito-idp:AdminListUserAuthEvents](#list_cognito-idp-action-AdminListUserAuthEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   AdminRemoveUserFromGroup  **
  - **IAM action:**  [cognito-idp:AdminRemoveUserFromGroup](#list_cognito-idp-action-AdminRemoveUserFromGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminResetUserPassword  **
  - **IAM action:**  [cognito-idp:AdminResetUserPassword](#list_cognito-idp-action-AdminResetUserPassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminRespondToAuthChallenge  **
  - **IAM action:**  [cognito-idp:AdminRespondToAuthChallenge](#list_cognito-idp-action-AdminRespondToAuthChallenge) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminSetUserMFAPreference  **
  - **IAM action:**  [cognito-idp:AdminSetUserMFAPreference](#list_cognito-idp-action-AdminSetUserMFAPreference) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminSetUserPassword  **
  - **IAM action:**  [cognito-idp:AdminSetUserPassword](#list_cognito-idp-action-AdminSetUserPassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminSetUserSettings  **
  - **IAM action:**  [cognito-idp:AdminSetUserSettings](#list_cognito-idp-action-AdminSetUserSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminUpdateAuthEventFeedback  **
  - **IAM action:**  [cognito-idp:AdminUpdateAuthEventFeedback](#list_cognito-idp-action-AdminUpdateAuthEventFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminUpdateDeviceStatus  **
  - **IAM action:**  [cognito-idp:AdminUpdateDeviceStatus](#list_cognito-idp-action-AdminUpdateDeviceStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminUpdateUserAttributes  **
  - **IAM action:**  [cognito-idp:AdminUpdateUserAttributes](#list_cognito-idp-action-AdminUpdateUserAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AdminUserGlobalSignOut  **
  - **IAM action:**  [cognito-idp:AdminUserGlobalSignOut](#list_cognito-idp-action-AdminUserGlobalSignOut) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateSoftwareToken  **
  - **IAM action:**  [cognito-idp:AssociateSoftwareToken](#list_cognito-idp-action-AssociateSoftwareToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ChangePassword  **
  - **IAM action:**  [cognito-idp:ChangePassword](#list_cognito-idp-action-ChangePassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfirmDevice  **
  - **IAM action:**  [cognito-idp:ConfirmDevice](#list_cognito-idp-action-ConfirmDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfirmForgotPassword  **
  - **IAM action:**  [cognito-idp:ConfirmForgotPassword](#list_cognito-idp-action-ConfirmForgotPassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfirmSignUp  **
  - **IAM action:**  [cognito-idp:ConfirmSignUp](#list_cognito-idp-action-ConfirmSignUp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGroup  **
  - **IAM action:**  [cognito-idp:CreateGroup](#list_cognito-idp-action-CreateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateIdentityProvider  **
  - **IAM action:**  [cognito-idp:CreateIdentityProvider](#list_cognito-idp-action-CreateIdentityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateManagedLoginBranding  **
  - **IAM action:**  [cognito-idp:CreateManagedLoginBranding](#list_cognito-idp-action-CreateManagedLoginBranding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateResourceServer  **
  - **IAM action:**  [cognito-idp:CreateResourceServer](#list_cognito-idp-action-CreateResourceServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTerms  **
  - **IAM action:**  [cognito-idp:CreateTerms](#list_cognito-idp-action-CreateTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUserImportJob  **
  - **IAM action:**  [cognito-idp:CreateUserImportJob](#list_cognito-idp-action-CreateUserImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUserPool  **
  - **IAM action:**  [cognito-idp:CreateUserPool](#list_cognito-idp-action-CreateUserPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cognito-idp:TagResource](#list_cognito-idp-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUserPoolClient  **
  - **IAM action:**  [cognito-idp:CreateUserPoolClient](#list_cognito-idp-action-CreateUserPoolClient)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUserPoolDomain  **
  - **IAM action:**  [cognito-idp:CreateUserPoolDomain](#list_cognito-idp-action-CreateUserPoolDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUserPoolReplica  **
  - **IAM action:**  [cognito-idp:CreateUserPoolReplica](#list_cognito-idp-action-CreateUserPoolReplica) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGroup  **
  - **IAM action:**  [cognito-idp:DeleteGroup](#list_cognito-idp-action-DeleteGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIdentityProvider  **
  - **IAM action:**  [cognito-idp:DeleteIdentityProvider](#list_cognito-idp-action-DeleteIdentityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteManagedLoginBranding  **
  - **IAM action:**  [cognito-idp:DeleteManagedLoginBranding](#list_cognito-idp-action-DeleteManagedLoginBranding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceServer  **
  - **IAM action:**  [cognito-idp:DeleteResourceServer](#list_cognito-idp-action-DeleteResourceServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTerms  **
  - **IAM action:**  [cognito-idp:DeleteTerms](#list_cognito-idp-action-DeleteTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [cognito-idp:DeleteUser](#list_cognito-idp-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserAttributes  **
  - **IAM action:**  [cognito-idp:DeleteUserAttributes](#list_cognito-idp-action-DeleteUserAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserPool  **
  - **IAM action:**  [cognito-idp:DeleteUserPool](#list_cognito-idp-action-DeleteUserPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserPoolClient  **
  - **IAM action:**  [cognito-idp:DeleteUserPoolClient](#list_cognito-idp-action-DeleteUserPoolClient) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserPoolClientSecret  **
  - **IAM action:**  [cognito-idp:DeleteUserPoolClientSecret](#list_cognito-idp-action-DeleteUserPoolClientSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserPoolDomain  **
  - **IAM action:**  [cognito-idp:DeleteUserPoolDomain](#list_cognito-idp-action-DeleteUserPoolDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserPoolReplica  **
  - **IAM action:**  [cognito-idp:DeleteUserPoolReplica](#list_cognito-idp-action-DeleteUserPoolReplica) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeIdentityProvider  **
  - **IAM action:**  [cognito-idp:DescribeIdentityProvider](#list_cognito-idp-action-DescribeIdentityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeManagedLoginBranding  **
  - **IAM action:**  [cognito-idp:DescribeManagedLoginBranding](#list_cognito-idp-action-DescribeManagedLoginBranding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeManagedLoginBrandingByClient  **
  - **IAM action:**  [cognito-idp:DescribeManagedLoginBrandingByClient](#list_cognito-idp-action-DescribeManagedLoginBrandingByClient) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourceServer  **
  - **IAM action:**  [cognito-idp:DescribeResourceServer](#list_cognito-idp-action-DescribeResourceServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRiskConfiguration  **
  - **IAM action:**  [cognito-idp:DescribeRiskConfiguration](#list_cognito-idp-action-DescribeRiskConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTerms  **
  - **IAM action:**  [cognito-idp:DescribeTerms](#list_cognito-idp-action-DescribeTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTermsByClient  **
  - **IAM action:**  [cognito-idp:DescribeTerms](#list_cognito-idp-action-DescribeTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUserImportJob  **
  - **IAM action:**  [cognito-idp:DescribeUserImportJob](#list_cognito-idp-action-DescribeUserImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUserPool  **
  - **IAM action:**  [cognito-idp:DescribeUserPool](#list_cognito-idp-action-DescribeUserPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUserPoolClient  **
  - **IAM action:**  [cognito-idp:DescribeUserPoolClient](#list_cognito-idp-action-DescribeUserPoolClient) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUserPoolDomain  **
  - **IAM action:**  [cognito-idp:DescribeUserPoolDomain](#list_cognito-idp-action-DescribeUserPoolDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ForgetDevice  **
  - **IAM action:**  [cognito-idp:ForgetDevice](#list_cognito-idp-action-ForgetDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ForgotPassword  **
  - **IAM action:**  [cognito-idp:ForgotPassword](#list_cognito-idp-action-ForgotPassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCSVHeader  **
  - **IAM action:**  [cognito-idp:GetCSVHeader](#list_cognito-idp-action-GetCSVHeader) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDevice  **
  - **IAM action:**  [cognito-idp:GetDevice](#list_cognito-idp-action-GetDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroup  **
  - **IAM action:**  [cognito-idp:GetGroup](#list_cognito-idp-action-GetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityProviderByIdentifier  **
  - **IAM action:**  [cognito-idp:GetIdentityProviderByIdentifier](#list_cognito-idp-action-GetIdentityProviderByIdentifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLogDeliveryConfiguration  **
  - **IAM action:**  [cognito-idp:GetLogDeliveryConfiguration](#list_cognito-idp-action-GetLogDeliveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProvisionedLimit  **
  - **IAM action:**  [cognito-idp:GetProvisionedLimit](#list_cognito-idp-action-GetProvisionedLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSigningCertificate  **
  - **IAM action:**  [cognito-idp:GetSigningCertificate](#list_cognito-idp-action-GetSigningCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTokensFromRefreshToken  **
  - **IAM action:**  [cognito-idp:GetTokensFromRefreshToken](#list_cognito-idp-action-GetTokensFromRefreshToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetUICustomization  **
  - **IAM action:**  [cognito-idp:GetUICustomization](#list_cognito-idp-action-GetUICustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUser  **
  - **IAM action:**  [cognito-idp:GetUser](#list_cognito-idp-action-GetUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUserAttributeVerificationCode  **
  - **IAM action:**  [cognito-idp:GetUserAttributeVerificationCode](#list_cognito-idp-action-GetUserAttributeVerificationCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUserPoolMfaConfig  **
  - **IAM action:**  [cognito-idp:GetUserPoolMfaConfig](#list_cognito-idp-action-GetUserPoolMfaConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GlobalSignOut  **
  - **IAM action:**  [cognito-idp:GlobalSignOut](#list_cognito-idp-action-GlobalSignOut) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InitiateAuth  **
  - **IAM action:**  [cognito-idp:InitiateAuth](#list_cognito-idp-action-InitiateAuth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListDevices  **
  - **IAM action:**  [cognito-idp:ListDevices](#list_cognito-idp-action-ListDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroups  **
  - **IAM action:**  [cognito-idp:ListGroups](#list_cognito-idp-action-ListGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentityProviders  **
  - **IAM action:**  [cognito-idp:ListIdentityProviders](#list_cognito-idp-action-ListIdentityProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceServers  **
  - **IAM action:**  [cognito-idp:ListResourceServers](#list_cognito-idp-action-ListResourceServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [cognito-idp:ListTagsForResource](#list_cognito-idp-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTerms  **
  - **IAM action:**  [cognito-idp:ListTerms](#list_cognito-idp-action-ListTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserImportJobs  **
  - **IAM action:**  [cognito-idp:ListUserImportJobs](#list_cognito-idp-action-ListUserImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserPoolClientSecrets  **
  - **IAM action:**  [cognito-idp:ListUserPoolClientSecrets](#list_cognito-idp-action-ListUserPoolClientSecrets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserPoolClients  **
  - **IAM action:**  [cognito-idp:ListUserPoolClients](#list_cognito-idp-action-ListUserPoolClients) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserPoolReplicas  **
  - **IAM action:**  [cognito-idp:ListUserPoolReplicas](#list_cognito-idp-action-ListUserPoolReplicas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserPools  **
  - **IAM action:**  [cognito-idp:ListUserPools](#list_cognito-idp-action-ListUserPools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsers  **
  - **IAM action:**  [cognito-idp:ListUsers](#list_cognito-idp-action-ListUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsersInGroup  **
  - **IAM action:**  [cognito-idp:ListUsersInGroup](#list_cognito-idp-action-ListUsersInGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ResendConfirmationCode  **
  - **IAM action:**  [cognito-idp:ResendConfirmationCode](#list_cognito-idp-action-ResendConfirmationCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RespondToAuthChallenge  **
  - **IAM action:**  [cognito-idp:RespondToAuthChallenge](#list_cognito-idp-action-RespondToAuthChallenge) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeToken  **
  - **IAM action:**  [cognito-idp:RevokeToken](#list_cognito-idp-action-RevokeToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetLogDeliveryConfiguration  **
  - **IAM action:**  [cognito-idp:SetLogDeliveryConfiguration](#list_cognito-idp-action-SetLogDeliveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetRiskConfiguration  **
  - **IAM action:**  [cognito-idp:SetRiskConfiguration](#list_cognito-idp-action-SetRiskConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetUICustomization  **
  - **IAM action:**  [cognito-idp:SetUICustomization](#list_cognito-idp-action-SetUICustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetUserMFAPreference  **
  - **IAM action:**  [cognito-idp:SetUserMFAPreference](#list_cognito-idp-action-SetUserMFAPreference) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetUserPoolMfaConfig  **
  - **IAM action:**  [cognito-idp:SetUserPoolMfaConfig](#list_cognito-idp-action-SetUserPoolMfaConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SetUserSettings  **
  - **IAM action:**  [cognito-idp:SetUserSettings](#list_cognito-idp-action-SetUserSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SignUp  **
  - **IAM action:**  [cognito-idp:SignUp](#list_cognito-idp-action-SignUp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartUserImportJob  **
  - **IAM action:**  [cognito-idp:StartUserImportJob](#list_cognito-idp-action-StartUserImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopUserImportJob  **
  - **IAM action:**  [cognito-idp:StopUserImportJob](#list_cognito-idp-action-StopUserImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [cognito-idp:TagResource](#list_cognito-idp-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [cognito-idp:UntagResource](#list_cognito-idp-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAuthEventFeedback  **
  - **IAM action:**  [cognito-idp:UpdateAuthEventFeedback](#list_cognito-idp-action-UpdateAuthEventFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDeviceStatus  **
  - **IAM action:**  [cognito-idp:UpdateDeviceStatus](#list_cognito-idp-action-UpdateDeviceStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGroup  **
  - **IAM action:**  [cognito-idp:UpdateGroup](#list_cognito-idp-action-UpdateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateIdentityProvider  **
  - **IAM action:**  [cognito-idp:UpdateIdentityProvider](#list_cognito-idp-action-UpdateIdentityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateManagedLoginBranding  **
  - **IAM action:**  [cognito-idp:UpdateManagedLoginBranding](#list_cognito-idp-action-UpdateManagedLoginBranding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProvisionedLimit  **
  - **IAM action:**  [cognito-idp:UpdateProvisionedLimit](#list_cognito-idp-action-UpdateProvisionedLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceServer  **
  - **IAM action:**  [cognito-idp:UpdateResourceServer](#list_cognito-idp-action-UpdateResourceServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTerms  **
  - **IAM action:**  [cognito-idp:UpdateTerms](#list_cognito-idp-action-UpdateTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUserAttributes  **
  - **IAM action:**  [cognito-idp:UpdateUserAttributes](#list_cognito-idp-action-UpdateUserAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUserPool  **
  - **IAM action:**  [cognito-idp:TagResource](#list_cognito-idp-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cognito-idp:UntagResource](#list_cognito-idp-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cognito-idp:UpdateUserPool](#list_cognito-idp-action-UpdateUserPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateUserPoolClient  **
  - **IAM action:**  [cognito-idp:UpdateUserPoolClient](#list_cognito-idp-action-UpdateUserPoolClient)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateUserPoolDomain  **
  - **IAM action:**  [cognito-idp:UpdateUserPoolDomain](#list_cognito-idp-action-UpdateUserPoolDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUserPoolReplica  **
  - **IAM action:**  [cognito-idp:UpdateUserPoolReplica](#list_cognito-idp-action-UpdateUserPoolReplica) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifySoftwareToken  **
  - **IAM action:**  [cognito-idp:VerifySoftwareToken](#list_cognito-idp-action-VerifySoftwareToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyUserAttribute  **
  - **IAM action:**  [cognito-idp:VerifyUserAttribute](#list_cognito-idp-action-VerifyUserAttribute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Cognito User Pools
<a name="list_cognito-idp-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddCustomAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddCustomAttributes.html)  **
  - **Description:** Grants permission to add user attributes to the user pool schema
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddUserPoolClientSecret](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddUserPoolClientSecret.html)  **
  - **Description:** Grants permission to add a new secret to a confidential client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminAddUserToGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminAddUserToGroup.html)  **
  - **Description:** Grants permission to add any user to any group
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.html)  **
  - **Description:** Grants permission to confirm any user's registration without a confirmation code
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminCreateUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html)  **
  - **Description:** Grants permission to create new users and send welcome messages via email or SMS
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminDeleteSoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteSoftwareToken.html)  **
  - **Description:** Grants permission to delete a user's software token
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminDeleteUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUser.html)  **
  - **Description:** Grants permission to delete any user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminDeleteUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteUserAttributes.html)  **
  - **Description:** Grants permission to delete attributes from any user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminDisableProviderForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDisableProviderForUser.html)  **
  - **Description:** Grants permission to unlink any user pool user from a third-party identity provider (IdP) user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminDisableUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDisableUser.html)  **
  - **Description:** Grants permission to deactivate any user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminEnableUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminEnableUser.html)  **
  - **Description:** Grants permission to activate any user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminForgetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminForgetDevice.html)  **
  - **Description:** Grants permission to deregister any user's devices
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminGetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.html)  **
  - **Description:** Grants permission to get information about any user's devices
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [AdminGetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.html)  **
  - **Description:** Grants permission to look up any user by user name
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [AdminGetUserAuthFactors](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUserAuthFactors.html)  **
  - **Description:** Grants permission to look up any user's configured auth factors
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [AdminInitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.html)  **
  - **Description:** Grants permission to authenticate any user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminLinkProviderForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.html)  **
  - **Description:** Grants permission to link any user pool user to a third-party IdP user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminListDevices](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.html)  **
  - **Description:** Grants permission to list any user's remembered devices
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [AdminListGroupsForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListGroupsForUser.html)  **
  - **Description:** Grants permission to list the groups that any user belongs to
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [AdminListUserAuthEvents](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListUserAuthEvents.html)  **
  - **Description:** Grants permission to lists sign-in events for any user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [AdminRemoveUserFromGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRemoveUserFromGroup.html)  **
  - **Description:** Grants permission to remove any user from any group
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminResetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminResetUserPassword.html)  **
  - **Description:** Grants permission to reset any user's password
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminRespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.html)  **
  - **Description:** Grants permission to respond to an authentication challenge during the authentication of any user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminSetUserMFAPreference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserMFAPreference.html)  **
  - **Description:** Grants permission to set any user's preferred MFA method
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminSetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.html)  **
  - **Description:** Grants permission to set any user's password
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminSetUserSettings](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserSettings.html)  **
  - **Description:** Grants permission to set user settings for any user
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminUpdateAuthEventFeedback](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateAuthEventFeedback.html)  **
  - **Description:** Grants permission to update advanced security feedback for any user's authentication event
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminUpdateDeviceStatus](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateDeviceStatus.html)  **
  - **Description:** Grants permission to update the status of any user's remembered devices
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminUpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html)  **
  - **Description:** Grants permission to updates any user's standard or custom attributes
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdminUserGlobalSignOut](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.html)  **
  - **Description:** Grants permission to sign out any user from all sessions
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateSoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AssociateSoftwareToken.html)  **
  - **Description:** Grants permission to return a unique generated shared secret key code for the user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ChangePassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ChangePassword.html)  **
  - **Description:** Grants permission to change the password for a specified user in a user pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ConfirmDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.html)  **
  - **Description:** Grants permission to confirm tracking of the device. This API call is the call that begins device tracking
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ConfirmForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.html)  **
  - **Description:** Grants permission to allow a user to enter a confirmation code to reset a forgotten password
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ConfirmSignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmSignUp.html)  **
  - **Description:** Grants permission to confirm registration of a user and handles the existing alias from a previous user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateGroup.html)  **
  - **Description:** Grants permission to create new user pool groups
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html)  **
  - **Description:** Grants permission to add identity providers to user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateManagedLoginBranding.html)  **
  - **Description:** Grants permission to create a branding settings for managed login and associate it with an app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateResourceServer.html)  **
  - **Description:** Grants permission to create and configure scopes for OAuth 2.0 resource servers
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTerms](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateTerms.html)  **
  - **Description:** Grants permission to create terms and associate it with an app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserImportJob.html)  **
  - **Description:** Grants permission to create user CSV import jobs
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html)  **
  - **Description:** Grants permission to create and set password policy for user pools
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cognito-idp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cognito-idp-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html)  **
  - **Description:** Grants permission to create user pool app clients
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.html)  **
  - **Description:** Grants permission to add user pool domains
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUserPoolReplica](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolReplica.html)  **
  - **Description:** Grants permission to create a replica of a user pool
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteGroup.html)  **
  - **Description:** Grants permission to delete any empty user pool group
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteIdentityProvider.html)  **
  - **Description:** Grants permission to delete any identity provider from user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteManagedLoginBranding.html)  **
  - **Description:** Grants permission to delete the managed login branding style for any app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteResourceServer.html)  **
  - **Description:** Grants permission to delete any OAuth 2.0 resource server from user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTerms](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteTerms.html)  **
  - **Description:** Grants permission to delete terms for an app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to allow a user to delete one's self
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserAttributes.html)  **
  - **Description:** Grants permission to delete the attributes for a user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPool.html)  **
  - **Description:** Grants permission to delete user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClient.html)  **
  - **Description:** Grants permission to delete any user pool app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserPoolClientSecret](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolClientSecret.html)  **
  - **Description:** Grants permission to delete a secret from a list of secrets associated with a client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolDomain.html)  **
  - **Description:** Grants permission to delete any user pool domain
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserPoolReplica](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolReplica.html)  **
  - **Description:** Grants permission to delete a replica of a user pool
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.html)  **
  - **Description:** Grants permission to describe any user pool identity provider
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBranding.html)  **
  - **Description:** Grants permission to get the detailed information about the branding style of managed login
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeManagedLoginBrandingByClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBrandingByClient.html)  **
  - **Description:** Grants permission to get the detailed information about the branding style of managed login associated with an appclient
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeResourceServer.html)  **
  - **Description:** Grants permission to describe any OAuth 2.0 resource server
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRiskConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeRiskConfiguration.html)  **
  - **Description:** Grants permission to describe the risk configuration settings of user pools and app clients
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTerms](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeTerms.html)  **
  - **Description:** Grants permission to get the detailed information about terms for an app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserImportJob.html)  **
  - **Description:** Grants permission to describe any user import job
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html)  **
  - **Description:** Grants permission to describe user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html)  **
  - **Description:** Grants permission to describe any user pool app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.html)  **
  - **Description:** Grants permission to describe any user pool domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ForgetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ForgetDevice.html)  **
  - **Description:** Grants permission to forget the specified device
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.html)  **
  - **Description:** Grants permission to send a message to the end user with a confirmation code that is required to change the user's password
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetCSVHeader](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetCSVHeader.html)  **
  - **Description:** Grants permission to generate headers for a user import .csv file
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetDevice.html)  **
  - **Description:** Grants permission to get the device
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetGroup.html)  **
  - **Description:** Grants permission to describe a user pool group
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdentityProviderByIdentifier](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetIdentityProviderByIdentifier.html)  **
  - **Description:** Grants permission to correlate a user pool IdP identifier to the IdP Name
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLogDeliveryConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetLogDeliveryConfiguration.html)  **
  - **Description:** Grants permission to get the detailed activity logging configuration for a user pool
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProvisionedLimit](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetProvisionedLimit.html)  **
  - **Description:** Grants permission to get a provisioned limit for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSigningCertificate](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetSigningCertificate.html)  **
  - **Description:** Grants permission to look up signing certificates for user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTokensFromRefreshToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.html)  **
  - **Description:** Grants permission to update user tokens with refresh tokens
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetUICustomization](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUICustomization.html)  **
  - **Description:** Grants permission to get UI customization information for the hosted UI of any app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUser.html)  **
  - **Description:** Grants permission to get the user attributes and metadata for a user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUserAttributeVerificationCode](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserAttributeVerificationCode.html)  **
  - **Description:** Grants permission to get the user attribute verification code for the specified attribute name
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUserPoolMfaConfig](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserPoolMfaConfig.html)  **
  - **Description:** Grants permission to look up the MFA configuration of user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GlobalSignOut](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.html)  **
  - **Description:** Grants permission to sign out users from all devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html)  **
  - **Description:** Grants permission to initiate the authentication flow
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListDevices](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListDevices.html)  **
  - **Description:** Grants permission to list the devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListGroups.html)  **
  - **Description:** Grants permission to list all groups in user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIdentityProviders](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListIdentityProviders.html)  **
  - **Description:** Grants permission to list all identity providers in user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListResourceServers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListResourceServers.html)  **
  - **Description:** Grants permission to list all resource servers in user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags that are assigned to an Amazon Cognito user pool
  - **Resource types (\*required):** [userpool](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTerms](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListTerms.html)  **
  - **Description:** Grants permission to list all terms for a user pool
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserImportJobs](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserImportJobs.html)  **
  - **Description:** Grants permission to list all user import jobs
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserPoolClientSecrets](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClientSecrets.html)  **
  - **Description:** Grants permission to list all secrets associated with a client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserPoolClients](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.html)  **
  - **Description:** Grants permission to list all app clients in user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserPoolReplicas](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolReplicas.html)  **
  - **Description:** Grants permission to list replicas of a user pool
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserPools](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPools.html)  **
  - **Description:** Grants permission to list all user pools
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUsers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html)  **
  - **Description:** Grants permission to list all user pool users
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUsersInGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsersInGroup.html)  **
  - **Description:** Grants permission to list the users in any group
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ResendConfirmationCode](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ResendConfirmationCode.html)  **
  - **Description:** Grants permission to resend the confirmation (for confirmation of registration) to a specific user in the user pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RespondToAuthChallenge](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.html)  **
  - **Description:** Grants permission to respond to the authentication challenge
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RevokeToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RevokeToken.html)  **
  - **Description:** Grants permission to revoke all of the access tokens generated by the specified refresh token
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetLogDeliveryConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.html)  **
  - **Description:** Grants permission to set up or modify the detailed activity logging configuration of a user pool
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetRiskConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetRiskConfiguration.html)  **
  - **Description:** Grants permission to set risk configuration for user pools and app clients
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetUICustomization](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUICustomization.html)  **
  - **Description:** Grants permission to customize the hosted UI for any app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetUserMFAPreference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserMFAPreference.html)  **
  - **Description:** Grants permission to set MFA preference for the user in the userpool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetUserPoolMfaConfig](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.html)  **
  - **Description:** Grants permission to set user pool MFA configuration
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetUserSettings](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserSettings.html)  **
  - **Description:** Grants permission to set the user settings like multi-factor authentication (MFA)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SignUp](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html)  **
  - **Description:** Grants permission to register the user in the specified user pool and creates a user name, password, and user attributes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StartUserImportJob.html)  **
  - **Description:** Grants permission to start any user import job
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StopUserImportJob.html)  **
  - **Description:** Grants permission to stop any user import job
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a user pool
  - **Resource types (\*required):** [userpool](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cognito-idp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cognito-idp-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a user pool
  - **Resource types (\*required):** [userpool](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cognito-idp-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAuthEventFeedback](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateAuthEventFeedback.html)  **
  - **Description:** Grants permission to update the feedback for the user authentication event
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDeviceStatus](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.html)  **
  - **Description:** Grants permission to update the device status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateGroup.html)  **
  - **Description:** Grants permission to update the configuration of any group
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.html)  **
  - **Description:** Grants permission to update the configuration of any user pool IdP
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateManagedLoginBranding.html)  **
  - **Description:** Grants permission to update the branding settings of a managed login
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProvisionedLimit](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateProvisionedLimit.html)  **
  - **Description:** Grants permission to update a provisioned limit for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateResourceServer.html)  **
  - **Description:** Grants permission to update the configuration of any OAuth 2.0 resource server
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTerms](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateTerms.html)  **
  - **Description:** Grants permission to update terms for an app client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.html)  **
  - **Description:** Grants permission to allow a user to update a specific attribute (one at a time)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html)  **
  - **Description:** Grants permission to updates the configuration of user pools
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cognito-idp-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cognito-idp-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolClient.html)  **
  - **Description:** Grants permission to update any user pool client
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.html)  **
  - **Description:** Grants permission to replace the certificate for any custom domain
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserPoolReplica](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolReplica.html)  **
  - **Description:** Grants permission to update a replica of a user pool
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifySoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifySoftwareToken.html)  **
  - **Description:** Grants permission to register a user's entered TOTP code and mark the user's software token MFA status as verified if successful
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [VerifyUserAttribute](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifyUserAttribute.html)  **
  - **Description:** Grants permission to verify a user attribute using a one time verification code
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for Amazon Cognito User Pools
<a name="list_cognito-idp-permission-only-actions"></a>

The following actions are defined by Amazon Cognito User Pools but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateWebACL](${UserGuideDocPage}user-pool-waf.html)  **
  - **Description:** Grants permission to associate the user pool with an AWS WAF web ACL
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [webacl\*](#list_cognito-idp-resource-webacl) / **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateWebACL](${UserGuideDocPage}user-pool-waf.html)  **
  - **Description:** Grants permission to disassociate the user pool with an AWS WAF web ACL
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetWebACLForResource](${UserGuideDocPage}user-pool-waf.html)  **
  - **Description:** Grants permission to get the AWS WAF web ACL that is associated with an Amazon Cognito user pool
  - **Resource types (\*required):** [userpool\*](#list_cognito-idp-resource-userpool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListResourcesForWebACL](${UserGuideDocPage}user-pool-waf.html)  **
  - **Description:** Grants permission to list the user pools that are associated with an AWS WAF web ACL
  - **Resource types (\*required):** [webacl\*](#list_cognito-idp-resource-webacl)
  - **Condition keys:**  
  - **Access level:** List



## Resource types defined by Amazon Cognito User Pools
<a name="list_cognito-idp-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [userpool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)  | arn:${Partition}:cognito-idp:${Region}:${Account}:userpool/${UserPoolId} | [aws:ResourceTag/${TagKey}](#list_cognito-idp-aws_ResourceTag___TagKey_) | 
|  [webacl](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html)  | arn:${Partition}:wafv2:${Region}:${Account}:${Scope}/webacl/${Name}/${Id} |   | 

## Condition keys for Amazon Cognito User Pools
<a name="list_cognito-idp-policy-keys"></a>

Amazon Cognito User Pools defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a key that is present in the request | ArrayOfString | 