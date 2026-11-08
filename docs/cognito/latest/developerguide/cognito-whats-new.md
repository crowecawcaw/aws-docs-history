

# What's new in Amazon Cognito
<a name="cognito-whats-new"></a>

This page lists changes to Amazon Cognito that affect how your applications, users, or administrators work with the service. Changes are newest first. Each entry starts with a label line. The label line shows the type of change, the component it applies to, the feature plan it requires (when one applies), and the date the change became available.

Entries have one of the following types:

New  
A new feature or API operation.

Changed  
A change to existing behavior, a quota, a default, or a policy requirement. Each entry says what you need to do, if anything.

Deprecated  
A feature or service that is closing or being removed. Each entry gives the dates and what you need to do.

Pricing  
A change to how Amazon Cognito charges for use.

Region  
Amazon Cognito, or an existing Amazon Cognito feature, is now available in more AWS Regions.

For changes to this guide that don't change the service, see [Document history](cognito-document-history.md). For changes before January 2025, see [What's New with AWS](https://aws.amazon.com/new/) on the AWS website and the Document history.

## November 2026
<a name="whats-new-2026-11"></a>

### 99.99% Service Level Agreement for Plus feature plan
<a name="whats-new-2026-11-05-plus-sla"></a>

Changed · User pools · Plus · November 5, 2026

Starting November 1, 2026, the Amazon Cognito Service Level Agreement (SLA) commits to a Monthly Uptime Percentage of 99.99% for user pools on the Plus feature plan, up from 99.9%. User pools on the Essentials and Lite feature plans keep the 99.9% Service Commitment, with no change to their terms.

**What you need to do:** Nothing, if your user pool is on the Plus feature plan. It's covered automatically. To qualify for the 99.99% Service Commitment, switch your user pool to the Plus feature plan.

See [User pool feature plans](cognito-sign-in-feature-plans.md), the [Amazon Cognito SLA](https://aws.amazon.com/cognito/sla/), and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cognito-sla-update/).

### New custom attribute names must be SCIM-compatible
<a name="whats-new-2026-11-02-scim-attribute-names"></a>

Changed · User pools · November 2, 2026

When you add a custom attribute, its name must now comply with the attribute-name rule of the System for Cross-domain Identity Management (SCIM) protocol in RFC 7644. The name must start with a letter and contain only letters, digits, hyphens, and underscores. Existing custom attributes aren't affected.

**What you need to do:** If your scripts or templates add custom attributes with names that contain other characters, such as periods or colons, change the names before you deploy them.

See [SCIM-compatible custom attribute names](user-pool-settings-attributes.md#user-pool-settings-custom-attributes-scim).

## October 2026
<a name="whats-new-2026-10"></a>

### Multi-Region replication in AWS GovCloud (US)
<a name="whats-new-2026-10-21-mrr-govcloud"></a>

Region · User pools · Essentials, Plus · October 21, 2026

You can now use multi-Region replication for user pools in the AWS GovCloud (US) Regions. Multi-Region replication is an add-on and requires a multi-Region AWS KMS customer managed key.

See [Multi-Region replication](user-pool-multi-region.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/10/cognito-multi-region-us-govcloud/).

### Higher default quota for resource servers
<a name="whats-new-2026-10-02-resource-server-quota"></a>

Changed · User pools · October 2, 2026

The default quota for resource servers in each user pool is now 100, up from 25. You can request an increase up to 300.

**What you need to do:** Nothing. The higher default applies to your user pools automatically.

See [Resource quotas](quotas.md#resource-quotas-cup).

### AWS WAF custom block responses return `403`
<a name="whats-new-2026-10-01-waf-403"></a>

Changed · Managed login · October 1, 2026

When an AWS WAF web ACL blocks a request with a custom response, managed login and the classic hosted UI now return `403`. They previously returned `5xx`.

**What you need to do:** If your application, client, or monitoring detects AWS WAF blocks by looking for `5xx` responses from your user pool domain, update it to expect `403`.

See [Status codes in custom block responses](user-pool-waf.md#user-pool-waf-custom-response-status).

## August 2026
<a name="whats-new-2026-08"></a>

### Machine-to-machine access tokens with `GetClientToken`
<a name="whats-new-2026-08-31-getclienttoken"></a>

New · User pools, M2M · August 31, 2026

App clients can now get access tokens for machine-to-machine (M2M) authorization from the [GetClientToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetClientToken.html) API operation, without a user pool domain. The operation works with the AWS SDKs, AWS WAF, and VPC interface endpoints. The client-credentials grant at the token endpoint is still available.

See [GetClientToken](cognito-user-pools-define-resource-servers.md#get-client-token) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-get-client-token/).

### Administrator reset of TOTP authenticators
<a name="whats-new-2026-08-26-totp-reset"></a>

New · User pools · August 26, 2026

You can now remove a user's time-based one-time password (TOTP) authenticator as an administrator with [AdminDeleteSoftwareToken](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteSoftwareToken.html). Your user can register a new authenticator the next time they sign in, so you don't have to recreate the user to restore their access.

See [Removing TOTP authenticators](user-pool-settings-mfa-totp.md#user-pool-settings-mfa-totp-remove) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-totp-reset/).

### Multi-Region replication with prefix domains
<a name="whats-new-2026-08-13-mrr-prefix-domains"></a>

Changed · User pools · Essentials, Plus · August 13, 2026

Failover for managed login, federation, and machine-to-machine authorization in multi-Region user pools now works with a prefix domain. It previously required a custom domain.

**What you need to do:** To fail over a user pool with a prefix domain, set up a Route 53 health check and set the routing configuration on the domain.

See [Multi-Region replication](user-pool-multi-region.md).

### Amazon Cognito skill in Agent Toolkit for AWS
<a name="whats-new-2026-08-07-agent-skill"></a>

New · Tools · August 7, 2026

AI coding agents can now use the `aws-auth` skill in the Agent Toolkit for AWS to set up, configure, and troubleshoot Amazon Cognito. The skill covers user pools, app clients, managed login, and OAuth 2.0 flows. It also covers tokens, passkeys, threat protection, Lambda triggers, and identity pools.

See the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-auth-agent-skill/).

## July 2026
<a name="whats-new-2026-07"></a>

### Amazon Cognito Sync is closed to new customers
<a name="whats-new-2026-07-30-sync-closed"></a>

Deprecated · Amazon Cognito Sync · July 30, 2026

Amazon Cognito Sync is no longer open to new customers. If you already use Amazon Cognito Sync, you can continue to use it.

**What you need to do:** For new applications, use AWS AppSync or DynamoDB instead.

See [Amazon Cognito Sync availability change](cognito-sync-availability-change.md).

### Import users with password hashes
<a name="whats-new-2026-07-15-password-hash-import"></a>

New · User pools · July 15, 2026

You can now include password hashes when you import users from a comma-separated values (CSV) file, so your imported users can sign in with their existing password instead of resetting it. You can use bcrypt, scrypt, Argon2id, or PBKDF2 with SHA-256 hashes.

See [Importing users from a CSV file](cognito-user-pools-using-import-tool.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cognito-password-hash-import/).

### Self-service provisioned API rate limits
<a name="whats-new-2026-07-06-provisioned-limits"></a>

New · User pools · July 6, 2026

You can now raise or lower the provisioned API rate limits for your user pools from the Amazon Cognito console or the limit provisioning API operations. Changes take effect immediately, up to the account maximum. You no longer have to request increases in Service Quotas.

See [Quotas](quotas.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/07/cognito-provisioned-limits).

## June 2026
<a name="whats-new-2026-06"></a>

### Amazon Cognito Sync closes to new customers on July 30, 2026
<a name="whats-new-2026-06-30-sync-closing"></a>

Deprecated · Amazon Cognito Sync · June 30, 2026

Starting July 30, 2026, Amazon Cognito Sync isn't open to new customers. Existing customers can continue to use it.

**What you need to do:** If you plan to start using Amazon Cognito Sync, use AWS AppSync or DynamoDB instead.

See [Amazon Cognito Sync availability change](cognito-sync-availability-change.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/).

### Minimum TLS version for custom domains
<a name="whats-new-2026-06-29-tls-version"></a>

New · User pools · June 29, 2026

You can now set the minimum TLS version for a custom domain when you create or update a user pool domain with the Amazon Cognito API.

See [Using your own domain](cognito-user-pools-add-custom-domain.md).

### Customer managed keys for encryption at rest
<a name="whats-new-2026-06-23-cmk"></a>

New · User pools · Essentials, Plus · June 23, 2026

You can now encrypt user pool data at rest with your own AWS KMS customer managed key, on new or existing user pools, at no additional charge. You control the key's lifecycle and permissions, and you can audit its use in CloudTrail.

See [Data protection](data-protection.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cognito-customer-managed-key).

### Multi-Region replication for user pools
<a name="whats-new-2026-06-04-mrr"></a>

New · User pools · Essentials, Plus · June 4, 2026

You can now keep a near real-time copy of a user pool in a standby AWS Region. The copy includes users, credentials, configuration, and federation settings, so you can move traffic to the standby Region if your primary Region is disrupted. Multi-Region replication is an add-on.

See [Multi-Region replication](user-pool-multi-region.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cognito-multi-region/).

## March 2026
<a name="whats-new-2026-03"></a>

### Amazon Cognito in Asia Pacific (Taipei) and Asia Pacific (New Zealand)
<a name="whats-new-2026-03-09-taipei-nz"></a>

Region · All components · March 9, 2026

Amazon Cognito is now available, with all features and feature plans, in the Asia Pacific (Taipei) and Asia Pacific (New Zealand) Regions.

See [Regional availability](what-is-amazon-cognito.md#getting-started-regional-availability) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/03/cognito-taipei-and-new-zealand-regions/).

## February 2026
<a name="whats-new-2026-02"></a>

### Client secret rotation and custom client secrets
<a name="whats-new-2026-02-26-client-secret-rotation"></a>

New · User pools · February 26, 2026

An app client can now have up to two client secrets at the same time, so you can rotate secrets without downtime. You can also provide your own secret value in place of a generated one.

See [App clients](user-pool-settings-client-apps.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-cognito-client-secret-lifecycle/).

## January 2026
<a name="whats-new-2026-01"></a>

### Inbound federation Lambda trigger
<a name="whats-new-2026-01-29-inbound-federation-trigger"></a>

New · User pools · January 29, 2026

A new Lambda trigger lets you transform the attributes of federated users while they authenticate, before Amazon Cognito writes them to the user profile.

See [Inbound federation Lambda trigger](user-pool-lambda-inbound-federation.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-cognito-inbound-federation-lambda-trigger/).

### Resource control policies for Amazon Cognito
<a name="whats-new-2026-01-22-rcp"></a>

New · User pools, Identity pools · January 22, 2026

You can now use AWS Organizations resource control policies (RCPs) to set the maximum permissions for Amazon Cognito resources across your organization. For example, an RCP can block identities outside your organization from accessing your resources.

See [Policy evaluation for VPC endpoints and RCPs](vpc-interface-endpoints.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2026/01/aws-expands-resource-control-policies).

## December 2025
<a name="whats-new-2025-12"></a>

### AWS PrivateLink for identity pools
<a name="whats-new-2025-12-11-privatelink-identity-pools"></a>

New · Identity pools · December 11, 2025

You can now send requests to identity pool API operations through VPC interface endpoints.

See [Using VPC interface endpoints](vpc-interface-endpoints.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-cognito-identity-pools-private-connectivity-aws-privatelink).

## November 2025
<a name="whats-new-2025-11"></a>

### AWS PrivateLink for user pools
<a name="whats-new-2025-11-07-privatelink-user-pools"></a>

New · User pools · November 7, 2025

You can now send requests to user pool API operations through VPC interface endpoints.

See [Using VPC interface endpoints](vpc-interface-endpoints.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-cognito-user-pools-private-connectivity-aws-privatelink).

### No charge per M2M app client
<a name="whats-new-2025-11-03-m2m-pricing"></a>

Pricing · M2M · November 3, 2025

Amazon Cognito no longer charges for each machine-to-machine (M2M) app client. You're charged only for successful M2M token requests each month.

See [Pricing](what-is-amazon-cognito.md#pricing-for-amazon-cognito) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-cognito-removes-machine-machine-app-client-price-dimension).

## October 2025
<a name="whats-new-2025-10"></a>

### Resource indicators (RFC 8707)
<a name="whats-new-2025-10-27-resource-indicators"></a>

New · Managed login · Essentials, Plus · October 27, 2025

Applications can now request access tokens for a specific resource server with the `resource` parameter. The resource server can then confirm from the `aud` claim that the token was issued for it.

See [Resource binding](cognito-user-pools-define-resource-servers.md#cognito-user-pools-resource-binding) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-cognito-resource-indicators-protection-oauth-2-0-resources).

### Quota for JSON web key document requests
<a name="whats-new-2025-10-13-jwks-quota"></a>

Changed · User pools · October 13, 2025

A new quota limits requests for user pool `jwks.json` documents to 50,000 requests per second for each AWS account in each AWS Region. This quota isn't adjustable.

**What you need to do:** Cache the JSON web key set in your applications and APIs instead of requesting it for every token you verify.

See [Managed login and endpoint quotas](quotas.md#category_operations-managedlogin).

### Terms of use and privacy policy links in managed login
<a name="whats-new-2025-10-02-terms-documents"></a>

New · Managed login · Essentials, Plus · October 2, 2025

You can now add links to your terms of use and privacy policy to managed login sign-up pages.

See [Terms documents](cognito-user-pools-managed-login.md#managed-login-terms-documents) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-cognito-terms-use-privacy-policy-documents-managed-login).

## August 2025
<a name="whats-new-2025-08"></a>

### New requirement for identity pool role trust policies
<a name="whats-new-2025-08-01-iam-trust"></a>

Changed · Identity pools · August 1, 2025

When the principal in an IAM role trust policy is the identity pools service principal, you can create or change the trust policy only if it includes a condition that limits the audience to one or more identity pools.

**What you need to do:** Before you change the trust policy for an identity pool role, add a condition on the `aud` claim with your identity pool IDs.

See [Set up a trust policy](iam-roles.md#trust-policies).

## July 2025
<a name="whats-new-2025-07"></a>

### Amazon Cognito in Mexico (Central) and Asia Pacific (Thailand)
<a name="whats-new-2025-07-29-mexico-thailand"></a>

Region · All components · July 29, 2025

Amazon Cognito is now available in the Mexico (Central) and Asia Pacific (Thailand) Regions, with all feature plans.

See [Regional availability](what-is-amazon-cognito.md#getting-started-regional-availability) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-cognito-thailand-and-mexico-central-regions/).

## June 2025
<a name="whats-new-2025-06"></a>

### AWS WAF web ACLs for managed login
<a name="whats-new-2025-06-26-waf-managed-login"></a>

New · Managed login · Essentials, Plus · June 26, 2025

You can now apply AWS WAF web ACL rules to app clients that use managed login branding.

See [Associating an AWS WAF web ACL](user-pool-waf.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-cognito-aws-waf-managed-login).

## May 2025
<a name="whats-new-2025-05"></a>

### OIDC `prompt` parameter
<a name="whats-new-2025-05-16-prompt"></a>

New · Managed login · Essentials, Plus · May 16, 2025

You can now control whether users with an existing managed login session must sign in again by passing the `prompt` parameter in authorization requests.

See [Authorize endpoint](authorization-endpoint.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-cognito-oidc-prompt-parameter/).

## April 2025
<a name="whats-new-2025-04"></a>

### Client metadata in M2M token requests
<a name="whats-new-2025-04-30-m2m-client-metadata"></a>

New · M2M · Essentials, Plus · April 30, 2025

You can now pass client metadata in client-credentials requests. Amazon Cognito passes it to the pre token generation Lambda trigger, so you can customize M2M access tokens based on request context.

See [Token endpoint](token-endpoint.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-cognito-context-machine-to-machine-flows/).

### Refresh token rotation
<a name="whats-new-2025-04-22-rtr"></a>

New · User pools · Essentials, Plus · April 22, 2025

When you turn on refresh token rotation for an app client, each refresh-token request returns a new refresh token and invalidates the original.

See [Refresh token rotation](amazon-cognito-user-pools-using-the-refresh-token.md#using-the-refresh-token-rotation) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-cognito-refresh-token-rotation/).

### AWS CDK L2 construct for identity pools
<a name="whats-new-2025-04-02-cdk-identity-pools"></a>

New · Identity pools, Tools · April 2, 2025

The AWS CDK L2 construct for identity pools is generally available. You can now define identity pools and their identity providers as infrastructure as code.

See the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/04/aws-cdk-l2-construct-cognito-identity-pools/).

## March 2025
<a name="whats-new-2025-03"></a>

### Feature plans, managed login, and passwordless in AWS GovCloud (US)
<a name="whats-new-2025-03-10-govcloud-features"></a>

Region · User pools, Managed login · Essentials, Plus · March 10, 2025

The Essentials and Plus feature plans, managed login, and passwordless sign-in with passkeys, email, and SMS are now available in the AWS GovCloud (US) Regions.

See [Feature plans](cognito-sign-in-feature-plans.md) and the What's New posts for [feature plans](https://aws.amazon.com/about-aws/whats-new/2025/03/new-feature-tiers-essentials-plus-amazon-cognito-aws-govcloud-us-regions), [managed login](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-cognito-managed-login-rich-branding-end-user-journeys-aws-govcloud-us-regions), and [passwordless sign-in](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-cognito-passwordless-authentication-low-friction-secure-logins-aws-govcloud-us-regions).

### Amazon Cognito in AWS GovCloud (US-East)
<a name="whats-new-2025-03-10-govcloud-east"></a>

Region · All components · March 10, 2025

Amazon Cognito is now available, with all features and feature plans, in the AWS GovCloud (US-East) Region.

See [Regional availability](what-is-amazon-cognito.md#getting-started-regional-availability) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-cognito-aws-govcloud-us-east-region).

### Amazon Cognito in Asia Pacific (Malaysia)
<a name="whats-new-2025-03-10-malaysia"></a>

Region · All components · March 10, 2025

Amazon Cognito is now available, with all features and feature plans, in the Asia Pacific (Malaysia) Region.

See [Regional availability](what-is-amazon-cognito.md#getting-started-regional-availability) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-cognito-asia-pacific-malaysia-region).

### Access token customization for M2M
<a name="whats-new-2025-03-03-m2m-token-customization"></a>

New · M2M · Essentials, Plus · March 3, 2025

Version 3 of the pre token generation Lambda trigger event can now change the claims and scopes in M2M access tokens. Not available in the AWS GovCloud (US) Regions.

See [Pre token generation Lambda trigger](user-pool-lambda-pre-token-generation.md) and the [What's New post](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-cognito-access-token-m2m-authorization-flows/).

## February 2025
<a name="whats-new-2025-02"></a>

### `AmazonCognitoPowerUser` managed policy update
<a name="whats-new-2025-02-27-poweruser-policy"></a>

Changed · User pools · February 27, 2025

The `AmazonCognitoPowerUser` AWS managed policy now includes an AWS End User Messaging SMS operation.

**What you need to do:** Nothing, unless you review changes to the permissions your roles get from AWS managed policies.

See [AWS managed policies](security-iam-awsmanpol.md).