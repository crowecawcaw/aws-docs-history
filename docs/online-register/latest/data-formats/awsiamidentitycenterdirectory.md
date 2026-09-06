

# Data retrieval APIs for AWS IAM Identity Center directory
<a name="awsiamidentitycenterdirectory"></a>

AWS IAM Identity Center directory provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="sso-directory-DescribeDirectory"></a>[DescribeDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | Retrieve information about the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-DescribeGroup"></a>[DescribeGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html) | Query the group data, not including user and group members | Read | 
| <a name="sso-directory-DescribeGroups"></a>[DescribeGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html) | Retrieve information about groups from the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-DescribeProvisioningTenant"></a>[DescribeProvisioningTenant](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | Describes the provisioning tenant | Read | 
| <a name="sso-directory-DescribeUser"></a>[DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html) | Retrieve information about a user from the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-DescribeUserByUniqueAttribute"></a>[DescribeUserByUniqueAttribute](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | Describe user with a valid unique attribute represented for the user | Read | 
| <a name="sso-directory-DescribeUsers"></a>[DescribeUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html) | Retrieve information about user from the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-GetAWSSPConfigurationForDirectory"></a>[GetAWSSPConfigurationForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | Retrieve the AWS IAM Identity Center Service Provider configurations for the directory | Read | 
| <a name="sso-directory-GetGroupId"></a>[GetGroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupId.html) | Retrieve ID information about group from the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-GetUserId"></a>[GetUserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetUserId.html) | Retrieve ID information about user from the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-GetUserPoolInfo"></a>[GetUserPoolInfo](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | (Deprecated) Grants permission to get UserPool Info | Read | 
| <a name="sso-directory-IsMemberInGroup"></a>[IsMemberInGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html) | Check if a member is a part of the group in the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-IsMemberInGroups"></a>[IsMemberInGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html) | Check if a member is a part of multiple groups in the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-ListBearerTokens"></a>[ListBearerTokens](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | List bearer tokens for a given provisioning tenant | Read | 
| <a name="sso-directory-ListExternalIdPCertificates"></a>[ListExternalIdPCertificates](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | List the external IdP certificates of a given directory and IdP | Read | 
| <a name="sso-directory-ListExternalIdPConfigurationsForDirectory"></a>[ListExternalIdPConfigurationsForDirectory](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | List all the External Identity Provider configurations created for the directory | Read | 
| <a name="sso-directory-ListGroups"></a>[ListGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroups.html) | List groups from the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-ListGroupsForMember"></a>[ListGroupsForMember](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html) | List groups of the target member | Read | 
| <a name="sso-directory-ListGroupsForUser"></a>[ListGroupsForUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html) | List groups for a user from the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-ListMembersInGroup"></a>[ListMembersInGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMemberships.html) | Retrieve all members that are part of a group in the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-ListMfaDevicesForUser"></a>[ListMfaDevicesForUser](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | List all active MFA devices and their MFA device metadata for a user | Read | 
| <a name="sso-directory-ListProvisioningTenants"></a>[ListProvisioningTenants](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | List provisioning tenants for a given directory | Read | 
| <a name="sso-directory-ListUsers"></a>[ListUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.html) | List users from the directory that AWS IAM Identity Center provides by default | Read | 
| <a name="sso-directory-SearchGroups"></a>[SearchGroups](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | Search for groups within the associated directory | Read | 
| <a name="sso-directory-SearchUsers"></a>[SearchUsers](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample) | Search for users within the associated directory | Read | 