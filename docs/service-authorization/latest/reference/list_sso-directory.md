

# Actions, resources, and condition keys for AWS IAM Identity Center directory
<a name="list_sso-directory"></a>

AWS IAM Identity Center directory (service prefix: `sso-directory`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sso-directory/sso-directory.json) for this service.

**Topics**
+ [Actions defined by AWS IAM Identity Center directory](#list_sso-directory-actions-as-permissions)
+ [Resource types defined by AWS IAM Identity Center directory](#list_sso-directory-resources-for-iam-policies)
+ [Condition keys for AWS IAM Identity Center directory](#list_sso-directory-policy-keys)

## Actions defined by AWS IAM Identity Center directory
<a name="list_sso-directory-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AddMemberToGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroupMembership.html)  | Grants permission to add a member to a group in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [CompleteVirtualMfaDeviceRegistration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to complete the creation process of a virtual MFA device |  |   | Write | 
|   [CompleteWebAuthnDeviceRegistration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to complete the registration process of a WebAuthn device |  |   | Write | 
|   [CreateAlias](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to create an alias for the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [CreateBearerToken](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to create a bearer token for a given provisioning tenant |  |   | Write | 
|   [CreateExternalIdPConfigurationForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to create an External Identity Provider configuration for the directory |  |   | Write | 
|   [CreateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroup.html)  | Grants permission to create a group in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [CreateProvisioningTenant](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to create a provisioning tenant for a given directory |  |   | Write | 
|   [CreateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateUser.html)  | Grants permission to create a user in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [DeleteBearerToken](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to delete a bearer token |  |   | Write | 
|   [DeleteExternalIdPCertificate](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to delete the given external IdP certificate |  |   | Write | 
|   [DeleteExternalIdPConfigurationForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to delete an External Identity Provider configuration associated with the directory |  |   | Write | 
|   [DeleteGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroup.html)  | Grants permission to delete a group from the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [DeleteMfaDeviceForUser](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to delete a MFA device by device name for a given user |  |   | Write | 
|   [DeleteProvisioningTenant](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to delete the provisioning tenant |  |   | Write | 
|   [DeleteUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteUser.html)  | Grants permission to delete a user from the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [DescribeDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to retrieve information about the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [DescribeGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html)  | Grants permission to query the group data, not including user and group members |  |   | Read | 
|   [DescribeGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html)  | Grants permission to retrieve information about groups from the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [DescribeProvisioningTenant](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to describes the provisioning tenant |  |   | Read | 
|   [DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html)  | Grants permission to retrieve information about a user from the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [DescribeUserByUniqueAttribute](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to describe user with a valid unique attribute represented for the user |  |   | Read | 
|   [DescribeUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html)  | Grants permission to retrieve information about user from the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [DisableExternalIdPConfigurationForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to disable authentication of end users with an External Identity Provider |  |   | Write | 
|   [DisableUser](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to deactivate a user in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [EnableExternalIdPConfigurationForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to enable authentication of end users with an External Identity Provider |  |   | Write | 
|   [EnableUser](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to activate user in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [GetAWSSPConfigurationForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to retrieve the AWS IAM Identity Center Service Provider configurations for the directory |  |   | Read | 
|   [GetGroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupId.html)  | Grants permission to retrieve ID information about group from the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [GetUserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetUserId.html)  | Grants permission to retrieve ID information about user from the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [GetUserPoolInfo](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | (Deprecated) Grants permission to get UserPool Info |  |   | Read | 
|   [ImportExternalIdPCertificate](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to import the IdP certificate used for verifying external IdP responses |  |   | Write | 
|   [IsMemberInGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html)  | Grants permission to check if a member is a part of the group in the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [IsMemberInGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html)  | Grants permission to check if a member is a part of multiple groups in the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [ListBearerTokens](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to list bearer tokens for a given provisioning tenant |  |   | Read | 
|   [ListExternalIdPCertificates](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to list the external IdP certificates of a given directory and IdP |  |   | Read | 
|   [ListExternalIdPConfigurationsForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to list all the External Identity Provider configurations created for the directory |  |   | Read | 
|   [ListGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroups.html)  | Grants permission to list groups from the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [ListGroupsForMember](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  | Grants permission to list groups of the target member |  |   | Read | 
|   [ListGroupsForUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  | Grants permission to list groups for a user from the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [ListMembersInGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMemberships.html)  | Grants permission to retrieve all members that are part of a group in the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [ListMfaDevicesForUser](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to list all active MFA devices and their MFA device metadata for a user |  |   | Read | 
|   [ListProvisioningTenants](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to list provisioning tenants for a given directory |  |   | Read | 
|   [ListUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.html)  | Grants permission to list users from the directory that AWS IAM Identity Center provides by default |  |   | Read | 
|   [RemoveMemberFromGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroupMembership.html)  | Grants permission to remove a member that is part of a group in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [SearchGroups](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to search for groups within the associated directory |  |   | Read | 
|   [SearchUsers](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to search for users within the associated directory |  |   | Read | 
|   [StartVirtualMfaDeviceRegistration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to begin the creation process of virtual mfa device |  |   | Write | 
|   [StartWebAuthnDeviceRegistration](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to begin the registration process of a WebAuthn device |  |   | Write | 
|   [UpdateExternalIdPConfigurationForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to update an External Identity Provider configuration associated with the directory |  |   | Write | 
|   [UpdateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateGroup.html)  | Grants permission to update information about a group in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [UpdateGroupDisplayName](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to update group display name update group display name response |  |   | Write | 
|   [UpdateMfaDeviceForUser](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to update MFA device information |  |   | Write | 
|   [UpdatePassword](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to update a password by sending password reset link via email or generating one time password for a user in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [UpdateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateUser.html)  | Grants permission to update user information in the directory that AWS IAM Identity Center provides by default |  |   | Write | 
|   [UpdateUserName](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to update user name update user name response |  |   | Write | 
|   [VerifyEmail](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  | Grants permission to verify an email address of an User |  |   | Write | 

## Resource types defined by AWS IAM Identity Center directory
<a name="list_sso-directory-resources-for-iam-policies"></a>

AWS IAM Identity Center directory does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS IAM Identity Center directory
<a name="list_sso-directory-policy-keys"></a>

AWS IAM Identity Center directory has no service-specific condition keys that can be used in the `Condition` element of policy statements.