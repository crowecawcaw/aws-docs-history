# Multi-Region replication for user pools

With multi-Region replication (MRR), you can create a replica user pool in an additional
AWS Region to provide business continuity and disaster recovery capabilities for your
authentication infrastructure. With MRR, registered users can continue to authenticate with
your applications even when you lose connectivity to resources in a Region, ensuring your
applications remain available.

When you configure MRR, Amazon Cognito creates separate user pools with a shared user pool ID.
Each replica user pool hosts authentication services for a shared user directory. The primary
user pool serves as the authoritative source for administrative configuration and write operations
such as password resets and user sign-up. Secondary user pools can't create users. They inherit
most settings from the primary user pool and, in a failover state, can handle authentication
operations such as user sign-in and token generation.

###### Important

Multi-Region replication is not available for all user pools at this time.
Multi-Region replication requires the modern Amazon Cognito infrastructure with enhanced
capabilities and scalability. Some user pools are still on a previous infrastructure and
will be upgraded by AWS to the new infrastructure, which will unlock this feature. In the
Amazon Cognito console, eligible user pools display multi-Region replication configuration options,
and ineligible pools display exception messages. For more information, see [Amazon Cognito unlocks advanced capabilities with next-generation
infrastructure](https://aws.amazon.com/blogs/security/amazon-cognito-unlocks-advanced-capabilities-with-next-generation-infrastructure/ "https://aws.amazon.com/blogs/security/amazon-cognito-unlocks-advanced-capabilities-with-next-generation-infrastructure/") in the AWS Security Blog.

## Things to know about multi-Region replication

- Multi-Region replication has separate add-on costs and requires your user pool to be
  on the Essentials or Plus [feature
  plan](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md"). You can't enable MRR on user pools with the Lite feature plan.
- You must configure your user pool with a [multi-Region customer
  managed key](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") from AWS KMS before enabling replication. The key must be available
  in all AWS Regions that have user pool replicas. For more information, see [Data encryption](data-protection.md#data-encryption "data-protection.md#data-encryption").
- For consistent token validation across Regions, we recommend that you configure your
  user pool with an updated issuer. For more information, see [Amazon Cognito user pools as an OIDC issuer](federation-endpoints.md#user-pool-oidc-issuer "federation-endpoints.md#user-pool-oidc-issuer").
- New secondary user pools start in the `INACTIVE` state. Review and
  configure regional settings before activating the user pool for production use.
- Regional configurations can differ between replicas. You can configure the following
  settings independently in replicas. All other settings are set in the primary user pool
  and automatically synchronized to the secondary.

  - Email configuration
  - Email configuration for threat protection notifications
  - SMS configuration
  - Lambda triggers
  - Tags
  - Log export configuration
  - AWS WAF web ACLs

- Data replication between Regions might introduce brief delays. The primary user pool
  syncs settings and user-directory updates to the secondary, and this process is
  eventually consistent.

## Limitations of multi-Region replication

- You can't generate new users in secondary user pools, either by sign-up or by
  administrator creation. Federated users can only sign in to a secondary user pool in
  the failover state if they have previously signed in to the primary user pool.
- Users can't reset their passwords or modify their profiles in secondary user pools.
  In a failover state, disable these operations in the user interface and make them
  available after your health check restores access to the primary user pool.
- You can have at most one secondary replica in an additional Region per user
  directory. Any eligible user pool can have a secondary replica.
- TOTP MFA is not supported in secondary replicas. Users with TOTP MFA configured must
  authenticate when the user pool in the primary Region is servicing requests.
- The count of password-based authentication attempts before lockout isn't
  synchronized across Regions. Each replica maintains its own count of failed
  authentication attempts.

## Configuring multi-Region replication

Before you can enable multi-Region replication, ensure your user pool meets the
prerequisites: Essentials or Plus feature plan and multi-Region customer managed KMS
key.

AWS Management Console

###### To configure multi-Region replication for a user pool

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
2. Choose **User pools**.
3. Choose an existing user pool from the list, or [create a new user pool](getting-started-user-pools.md "getting-started-user-pools.md").
4. Choose the **Settings** tab.
5. In the left navigation menu, choose **Multi-Region
   replication**.
6. Choose **Create a replica user pool**.
7. For **Region**, select the AWS Region where you want to
   create the replica user pool.
8. Review the configuration summary and choose **Create
   replica**.
9. After the replica is created, review the regional configuration settings in
   the comparison table. Configure any Region-specific settings such as email
   configuration, SMS settings, or Lambda triggers as needed for your replica
   Region.
10. To configure a Route 53 health check for your domain, navigate to the
    **Domain services** menu, edit or add a custom domain, and
    configure a **Route 53 health check ID**.
11. When you're ready to use the replica for production traffic, change the
    replica status from **Inactive** to
    **Active**.

API
To create a replica user pool, use the [CreateUserPoolReplica](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolReplica.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolReplica.md") operation. The following example creates a replica in
the `us-west-2` Region for a primary user pool in
`us-east-1`.

```
{
 "UserPoolId": "`us-east-1_EXAMPLE`",
 "RegionName": "`us-west-2`",
 "UserPoolTags": {
    "Environment": "`Production`",
    "Application": "`MyApp`"
 }
}
```

The response includes the replica information:

```
{
 "Replica": {
    "RegionName": "`us-west-2`",
    "UserPoolArn": "arn:aws:cognito-idp:`us-west-2`:`111122223333`:userpool/`us-east-1_EXAMPLE`",
    "Status": "PENDING_CREATE",
    "Role": "SECONDARY"
 }
}
```

You must also configure your domain for failover. Set up a health check in Route 53
and apply it to your domain in an [UpdateUserPoolDomain](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.md") request:

```
{
 "CustomDomainConfig": {
    "CertificateArn": "arn:aws:acm:us-east-1:`111122223333`:certificate/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
 },
 "Domain": "`auth.example.com`",
 "ManagedLoginVersion": `2`,
 "Routing": {
    "Failover": {
       "SecondaryRegion": "`us-west-2`",
       "PrimaryRoute53HealthCheckId": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
    }
 },
 "UserPoolId": "`us-east-1_EXAMPLE`"
}
```

To activate the replica for production use, use the [UpdateUserPoolReplica](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolReplica.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolReplica.md") operation:

```
{
 "UserPoolId": "`us-east-1_EXAMPLE`",
 "RegionName": "`us-west-2`",
 "Status": "ACTIVE"
}
```

The response confirms the updated replica status:

```
{
 "Replica": {
    "RegionName": "`us-west-2`",
    "UserPoolArn": "arn:aws:cognito-idp:`us-west-2`:`111122223333`:userpool/`us-east-1_EXAMPLE`",
    "Status": "ACTIVE",
    "Role": "SECONDARY"
 }
}
```

## Supported API operations in secondary Regions

Amazon Cognito supports a subset of API operations in secondary Regions. The operations
available depend on the replica's status. Replicas in `INACTIVE` status support
a limited set of read and configuration operations. Replicas in `ACTIVE` status
support additional authentication and session management operations. Operations that aren't
listed here are only available in the primary Region.

### Operations for INACTIVE secondary Regions

Replica user pools in secondary Regions in `INACTIVE` status allow the following Amazon Cognito
API operations.

- [AdminGetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.md")
- [AdminGetUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.md")
- [AdminListDevices](../../../cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.md")
- [AdminListGroupsForUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminListGroupsForUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminListGroupsForUser.md")
- [AdminListUserAuthEvents](../../../cognito-user-identity-pools/latest/APIReference/API_AdminListUserAuthEvents.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminListUserAuthEvents.md")
- [AssociateWebACL](../../../cognito-user-identity-pools/latest/APIReference/API_AssociateWebACL.md "../../../cognito-user-identity-pools/latest/APIReference/API_AssociateWebACL.md")
- [CreateUserPoolDomain](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.md")
- [DeleteUserPoolDomain](../../../cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolDomain.md "../../../cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolDomain.md")
- [DeleteUserPoolReplica](../../../cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolReplica.md "../../../cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolReplica.md")
- [DescribeIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.md")
- [DescribeManagedLoginBranding](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBranding.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBranding.md")
- [DescribeManagedLoginBrandingByClient](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBrandingByClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBrandingByClient.md")
- [DescribeResourceServer](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeResourceServer.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeResourceServer.md")
- [DescribeRiskConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeRiskConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeRiskConfiguration.md")
- [DescribeTerms](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeTerms.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeTerms.md")
- [DescribeUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md")
- [DescribeUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md")
- [DescribeUserPoolDomain](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.md")
- [DisassociateWebACL](../../../cognito-user-identity-pools/latest/APIReference/API_DisassociateWebACL.md "../../../cognito-user-identity-pools/latest/APIReference/API_DisassociateWebACL.md")
- [GetGroup](../../../cognito-user-identity-pools/latest/APIReference/API_GetGroup.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetGroup.md")
- [GetLogDeliveryConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_GetLogDeliveryConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetLogDeliveryConfiguration.md")
- [GetSigningCertificate](../../../cognito-user-identity-pools/latest/APIReference/API_GetSigningCertificate.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetSigningCertificate.md")
- [GetUICustomization](../../../cognito-user-identity-pools/latest/APIReference/API_GetUICustomization.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUICustomization.md")
- [GetUserPoolMfaConfig](../../../cognito-user-identity-pools/latest/APIReference/API_GetUserPoolMfaConfig.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUserPoolMfaConfig.md")
- [ListIdentityProviders](../../../cognito-user-identity-pools/latest/APIReference/API_ListIdentityProviders.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListIdentityProviders.md")
- [ListGroups](../../../cognito-user-identity-pools/latest/APIReference/API_ListGroups.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListGroups.md")
- [ListResourceServers](../../../cognito-user-identity-pools/latest/APIReference/API_ListResourceServers.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListResourceServers.md")
- [ListTagsForResource](../../../cognito-user-identity-pools/latest/APIReference/API_ListTagsForResource.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListTagsForResource.md")
- [ListTerms](../../../cognito-user-identity-pools/latest/APIReference/API_ListTerms.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListTerms.md")
- [ListUserPoolClients](../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClients.md")
- [ListUserPoolClientSecrets](../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClientSecrets.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPoolClientSecrets.md")
- [ListUserPoolReplicas](../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPoolReplicas.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPoolReplicas.md")
- [ListUserPools](../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPools.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUserPools.md")
- [ListUsers](../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUsers.md")
- [ListUsersInGroup](../../../cognito-user-identity-pools/latest/APIReference/API_ListUsersInGroup.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListUsersInGroup.md")
- [SetLogDeliveryConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md")
- [SetRiskConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_SetRiskConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetRiskConfiguration.md")
- [SetUserPoolMfaConfig](../../../cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.md")
- [TagResource](../../../cognito-user-identity-pools/latest/APIReference/API_TagResource.md "../../../cognito-user-identity-pools/latest/APIReference/API_TagResource.md")
- [UntagResource](../../../cognito-user-identity-pools/latest/APIReference/API_UntagResource.md "../../../cognito-user-identity-pools/latest/APIReference/API_UntagResource.md")
- [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md")
- [UpdateUserPoolDomain](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.md")
- [UpdateUserPoolReplica](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolReplica.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolReplica.md")

### Additional operations for ACTIVE secondary Regions

Replica user pools in secondary Regions in `ACTIVE` status allow all of the preceding
operations, plus the following authentication and session management operations.

- [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md")
- [AdminRespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminRespondToAuthChallenge.md")
- [AdminUpdateAuthEventFeedback](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateAuthEventFeedback.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateAuthEventFeedback.md")
- [AdminUserGlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md")
- [GetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_GetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetDevice.md")
- [GetIdentityProviderByIdentifier](../../../cognito-user-identity-pools/latest/APIReference/API_GetIdentityProviderByIdentifier.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetIdentityProviderByIdentifier.md")
- [GetTokensFromRefreshToken](../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetTokensFromRefreshToken.md")
- [GetUser](../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md")
- [GetUserAuthFactors](../../../cognito-user-identity-pools/latest/APIReference/API_GetUserAuthFactors.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUserAuthFactors.md")
- [GlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.md")
- [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md")
- [ListDevices](../../../cognito-user-identity-pools/latest/APIReference/API_ListDevices.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListDevices.md")
- [ListWebAuthnCredentials](../../../cognito-user-identity-pools/latest/APIReference/API_ListWebAuthnCredentials.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListWebAuthnCredentials.md")
- [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md")
- [RevokeToken](../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md "../../../cognito-user-identity-pools/latest/APIReference/API_RevokeToken.md")
- [UpdateAuthEventFeedback](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateAuthEventFeedback.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateAuthEventFeedback.md")

## Failover in multi-Region user pools

With multi-Region user pools, you can fail over managed login, federated login, and
direct API calls between two AWS Regions. Managed login and federation failover is
available with either a custom domain or a prefix (Cognito) domain configured with your
user pool. You can't configure a different custom domain with replica user pools.

### Failover for managed login, federation, and machine-to-machine authorization

Failover is available when your primary user pool has a [custom domain](cognito-user-pools-add-custom-domain.md "cognito-user-pools-add-custom-domain.md") or a [prefix domain](cognito-user-pools-assign-domain-prefix.md "cognito-user-pools-assign-domain-prefix.md"). Your user pool
domain serves the OAuth 2.0 resources, including the [authorize](authorization-endpoint.md "authorization-endpoint.md") and [token](token-endpoint.md "token-endpoint.md") endpoints, and handles IdP responses from
third-party federation providers, including OIDC, SAML, and social providers.

To enable failover, set up a [health check](../../../Route53/latest/DeveloperGuide/dns-failover.md "../../../Route53/latest/DeveloperGuide/dns-failover.md") in Route 53
and set the `Routing` field on your domain. You determine what triggers a
healthy or unhealthy state. When the health check is in an unhealthy state, Amazon Cognito serves
managed login pages and authentication operations from the secondary replica user pool.
When the health check enters a healthy state, Amazon Cognito begins routing traffic back to the
primary replica.

The DNS record for your custom domain can use Route 53 or any third-party DNS provider.
Ensure you have a valid CNAME record in your DNS provider pointing to your target alias,
which is a CloudFront distribution. You can find the alias target on the
**Domain** page in the Amazon Cognito console.

###### To update the health check ID in the console

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
2. Choose **User pools**, and then choose your user pool.
3. Choose **Domain** under **Branding** from the menu.
4. Under the **Custom domain** section, choose the edit
   option and select **Edit multi-Region failover**.
5. Toggle the **Enable multi-Region failover** option.
6. Select your Route 53 health check ID from the available health checks.
7. Choose **Save changes**.

### Failover for Amazon Cognito APIs and SDKs

If you use the Amazon Cognito APIs or SDKs, there's no usage of a custom domain and your
application is responsible for routing traffic to the Amazon Cognito service regional endpoint to
handle authentication and other API calls.

If you only have an application frontend using a public client, such as a
single-page application (SPA) or mobile app, your application needs to be dynamic to route
the API calls accordingly. Consider a serverless application backend to help determine
which Region authentication with Amazon Cognito should begin against.

If you have an application with a backend, the logic to determine which user pool to
authenticate against can be determined here.

If you use both managed login endpoints and APIs, use the same Route 53
health check to determine which Region your application directs Amazon Cognito API calls to.
