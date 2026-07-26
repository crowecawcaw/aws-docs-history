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
- Your user pool must use a multi-Region OIDC issuer to ensure consistent token
  validation across Regions. For more information, see [Amazon Cognito user pools as an OIDC issuer](federation-endpoints.md#user-pool-oidc-issuer "federation-endpoints.md#user-pool-oidc-issuer").
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
  administrator creation. New federated users can only sign in to a secondary user pool in
  the failover state if they have previously signed in to the primary user pool.
- Users can't reset their passwords or modify their profiles in secondary user pools.
  In a failover state, disable these operations in the user interface and make them
  available after your health check restores access to the primary user pool.
- You can have at most one secondary replica in an additional Region per user
  directory. Any user pool can have a secondary replica.
- TOTP MFA is not supported in secondary replicas. Users with TOTP MFA configured must
  authenticate when the user pool in the primary Region is servicing requests.
- The count of password-based authentication attempts before lockout isn't
  synchronized across Regions. Each replica maintains its own count of failed
  authentication attempts.
- You can only configure automatic failover of multi-Region user pools with a [custom domain](cognito-user-pools-add-custom-domain.md "cognito-user-pools-add-custom-domain.md").

## Configuring multi-Region replication

Before you can enable multi-Region replication, ensure your user pool meets the
prerequisites: Essentials or Plus feature plan, multi-Region customer managed KMS key, and
multi-Region OIDC issuer configuration.

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

## Failover in multi-Region user pools

With multi-Region user pools, you can fail over managed login, federated login, and
direct API calls between two AWS Regions. Managed login and federation require a custom
domain configured with your primary user pool. You can't configure a different custom domain
with replica user pools.

### Failover for managed login, federation, and machine-to-machine authorization

Failover is available when your primary user pool has a [custom domain](cognito-user-pools-add-custom-domain.md "cognito-user-pools-add-custom-domain.md"). When both user
pools have a [prefix
domain](cognito-user-pools-assign-domain-prefix.md "cognito-user-pools-assign-domain-prefix.md"), you can manually test operations on the secondary replica by accessing
the secondary prefix domain directly. Custom domains can be served from either the primary
or additional replica and Region.

Your user pool requires a custom domain because that domain serves the OAuth 2.0
resources, including the [authorize](authorization-endpoint.md "authorization-endpoint.md") and [token](token-endpoint.md "token-endpoint.md") endpoints, and handles IdP responses from
third-party federation providers, including OIDC, SAML, and social providers.

To configure failover, set up a [health check](../../../Route53/latest/DeveloperGuide/dns-failover.md "../../../Route53/latest/DeveloperGuide/dns-failover.md") in Route 53.
You determine what triggers a healthy or unhealthy state. The health check isn't directly
tied to your DNS CNAME record, but it controls whether traffic routes to your primary or
replica user pool.

The DNS record for your custom domain can use Route 53 or any third-party DNS provider.
Ensure you have a valid CNAME record in your DNS provider pointing to your target alias,
which is a CloudFront distribution. You can find the alias target on the
**Domain** page in the Amazon Cognito console.

When the health check is in an unhealthy state, Amazon Cognito serves managed login pages and
authentication operations for the custom domain from the secondary replica user pool. When
the health check enters a healthy state, Amazon Cognito begins routing traffic back to the primary
replica.

Each user pool has its own prefix domain, as these are Region-isolated. You can still
directly call these endpoints to handle authentication. However, if federation is
configured with third-party IdPs, then there must be two application configurations for
each prefix endpoint. As a best practice, use a custom domain to ensure Amazon Cognito handles
routing to and from managed login automatically based on the Route 53 health check
status.

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
