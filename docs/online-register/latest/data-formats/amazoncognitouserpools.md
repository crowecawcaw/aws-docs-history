

# Data retrieval APIs for Amazon Cognito User Pools
<a name="amazoncognitouserpools"></a>

Amazon Cognito User Pools provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="cognito-idp-AdminGetDevice"></a>[AdminGetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.html) | Get information about any user's devices | Read | 
| <a name="cognito-idp-AdminGetUser"></a>[AdminGetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.html) | Look up any user by user name | Read | 
| <a name="cognito-idp-AdminGetUserAuthFactors"></a>[AdminGetUserAuthFactors](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUserAuthFactors.html) | Look up any user's configured auth factors | Read | 
| <a name="cognito-idp-AdminListDevices"></a>[AdminListDevices](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.html) | List any user's remembered devices | List | 
| <a name="cognito-idp-AdminListGroupsForUser"></a>[AdminListGroupsForUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListGroupsForUser.html) | List the groups that any user belongs to | List | 
| <a name="cognito-idp-AdminListUserAuthEvents"></a>[AdminListUserAuthEvents](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListUserAuthEvents.html) | Lists sign-in events for any user | Read | 
| <a name="cognito-idp-DescribeIdentityProvider"></a>[DescribeIdentityProvider](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.html) | Describe any user pool identity provider | Read | 
| <a name="cognito-idp-DescribeManagedLoginBranding"></a>[DescribeManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBranding.html) | Get the detailed information about the branding style of managed login | Read | 
| <a name="cognito-idp-DescribeManagedLoginBrandingByClient"></a>[DescribeManagedLoginBrandingByClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBrandingByClient.html) | Get the detailed information about the branding style of managed login associated with an appclient | Read | 
| <a name="cognito-idp-DescribeResourceServer"></a>[DescribeResourceServer](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeResourceServer.html) | Describe any OAuth 2.0 resource server | Read | 
| <a name="cognito-idp-DescribeRiskConfiguration"></a>[DescribeRiskConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeRiskConfiguration.html) | Describe the risk configuration settings of user pools and app clients | Read | 
| <a name="cognito-idp-DescribeTerms"></a>[DescribeTerms](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeTerms.html) | Get the detailed information about terms for an app client | Read | 
| <a name="cognito-idp-DescribeUserImportJob"></a>[DescribeUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserImportJob.html) | Describe any user import job | Read | 
| <a name="cognito-idp-DescribeUserPool"></a>[DescribeUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html) | Describe user pools | Read | 
| <a name="cognito-idp-DescribeUserPoolClient"></a>[DescribeUserPoolClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html) | Describe any user pool app client | Read | 
| <a name="cognito-idp-DescribeUserPoolDomain"></a>[DescribeUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.html) | Describe any user pool domain | Read | 
| <a name="cognito-idp-GetCSVHeader"></a>[GetCSVHeader](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetCSVHeader.html) | Generate headers for a user import .csv file | Read | 
| <a name="cognito-idp-GetDevice"></a>[GetDevice](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetDevice.html) | Get the device | Read | 
| <a name="cognito-idp-GetGroup"></a>[GetGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetGroup.html) | Describe a user pool group | Read | 
| <a name="cognito-idp-GetIdentityProviderByIdentifier"></a>[GetIdentityProviderByIdentifier](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetIdentityProviderByIdentifier.html) | Correlate a user pool IdP identifier to the IdP Name | Read | 
| <a name="cognito-idp-GetLogDeliveryConfiguration"></a>[GetLogDeliveryConfiguration](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetLogDeliveryConfiguration.html) | Get the detailed activity logging configuration for a user pool | Read | 
| <a name="cognito-idp-GetProvisionedLimit"></a>[GetProvisionedLimit](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetProvisionedLimit.html) | Get a provisioned limit for the AWS account | Read | 
| <a name="cognito-idp-GetSigningCertificate"></a>[GetSigningCertificate](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetSigningCertificate.html) | Look up signing certificates for user pools | Read | 
| <a name="cognito-idp-GetUICustomization"></a>[GetUICustomization](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUICustomization.html) | Get UI customization information for the hosted UI of any app client | Read | 
| <a name="cognito-idp-GetUser"></a>[GetUser](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUser.html) | Get the user attributes and metadata for a user | Read | 
| <a name="cognito-idp-GetUserAttributeVerificationCode"></a>[GetUserAttributeVerificationCode](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserAttributeVerificationCode.html) | Get the user attribute verification code for the specified attribute name | Read | 
| <a name="cognito-idp-GetUserPoolMfaConfig"></a>[GetUserPoolMfaConfig](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetUserPoolMfaConfig.html) | Look up the MFA configuration of user pools | Read | 
| <a name="cognito-idp-GetWebACLForResource"></a>[GetWebACLForResource](${UserGuideDocPage}user-pool-waf.html) | Get the AWS WAF web ACL that is associated with an Amazon Cognito user pool | Read | 
| <a name="cognito-idp-ListDevices"></a>[ListDevices](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListDevices.html) | List the devices | List | 
| <a name="cognito-idp-ListGroups"></a>[ListGroups](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListGroups.html) | List all groups in user pools | List | 
| <a name="cognito-idp-ListIdentityProviders"></a>[ListIdentityProviders](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListIdentityProviders.html) | List all identity providers in user pools | List | 
| <a name="cognito-idp-ListResourceServers"></a>[ListResourceServers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListResourceServers.html) | List all resource servers in user pools | List | 
| <a name="cognito-idp-ListResourcesForWebACL"></a>[ListResourcesForWebACL](${UserGuideDocPage}user-pool-waf.html) | List the user pools that are associated with an AWS WAF web ACL | List | 
| <a name="cognito-idp-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListTagsForResource.html) | List the tags that are assigned to an Amazon Cognito user pool | List | 
| <a name="cognito-idp-ListTerms"></a>[ListTerms](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListTerms.html) | List all terms for a user pool | List | 
| <a name="cognito-idp-ListUserImportJobs"></a>[ListUserImportJobs](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserImportJobs.html) | List all user import jobs | List | 
| <a name="cognito-idp-ListUserPoolClientSecrets"></a>[ListUserPoolClientSecrets](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClientSecrets.html) | List all secrets associated with a client | List | 
| <a name="cognito-idp-ListUserPoolClients"></a>[ListUserPoolClients](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.html) | List all app clients in user pools | List | 
| <a name="cognito-idp-ListUserPoolReplicas"></a>[ListUserPoolReplicas](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolReplicas.html) | List replicas of a user pool | List | 
| <a name="cognito-idp-ListUserPools"></a>[ListUserPools](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPools.html) | List all user pools | List | 
| <a name="cognito-idp-ListUsers"></a>[ListUsers](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html) | List all user pool users | List | 
| <a name="cognito-idp-ListUsersInGroup"></a>[ListUsersInGroup](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsersInGroup.html) | List the users in any group | List | 