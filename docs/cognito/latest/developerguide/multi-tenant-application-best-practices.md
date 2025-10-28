# Multi-tenant application best

practices

Amazon Cognito user pools operate with multi-tenant applications that generate a volume of requests that
must remain within Amazon Cognito quotas. To scale up this capacity when your customer base grows,
you can [purchase additional quota
capacity](quotas.md#managing-request-rate-quotas.title "quotas.md#managing-request-rate-quotas.title").

###### Note

Amazon Cognito [quotas](limits.md "limits.md") are applied per AWS account and AWS Region. These quotas are
shared across all tenants in your application. Review the Amazon Cognito service quotas, and make
sure that the quota meets the expected volume and the expected number of tenants in your
application.

This section describes methods that you can implement to separate tenants between Amazon Cognito
resources within the same Region and AWS account. You can also split your tenants across
more than one AWS account or Region, and give each of them their own quota. Other
advantages of multi-Region multi-tenancy include the highest possible level of isolation,
shortest network-transit time for globally distributed users, and adherence to existing
distribution models in your organization.

Single-Region multi-tenancy can also have advantages for your customers and
administrators.

The following list covers some of the advantages of multi-tenancy with shared
resources.

###### Advantages of multi-tenancy

**Common user directory**

Multi-tenancy supports models where customers have accounts in more than one
application. You can [link identities from
third-party providers](cognito-user-pools-identity-federation.md#cognito-user-pools-identity-federation.title "cognito-user-pools-identity-federation.md#cognito-user-pools-identity-federation.title") into a single consistent user pool profile. In
cases where user profiles are unique to their tenant, any multi-tenancy strategy
with a single user pool has one point of entry to user administration.

**Common security**

In a shared user pool, you can create a single standard for security and apply
the same [threat protection](cognito-user-pool-settings-threat-protection.md#cognito-user-pool-settings-threat-protection.title "cognito-user-pool-settings-threat-protection.md#cognito-user-pool-settings-threat-protection.title"), [multi-factor authentication](user-pool-settings-mfa.md#user-pool-settings-mfa.title "user-pool-settings-mfa.md#user-pool-settings-mfa.title") (MFA), and [AWS WAF](user-pool-waf.md#user-pool-waf.title "user-pool-waf.md#user-pool-waf.title") standards to all tenants.
Because an AWS WAF web ACL must be in the same AWS Region as the resource that
you associate it with, multi-tenancy offers shared access to a complex resource.
When you want to maintain consistent security configuration in multi-Region
Amazon Cognito applications, you must apply operational standards that replicate your
configuration between resources.

**Common customization**

You can customize user pools and identity pools with AWS Lambda. Configuration
of [Lambda
triggers](cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-working-with-lambda-triggers.title "cognito-user-pools-working-with-lambda-triggers.md#cognito-user-pools-working-with-lambda-triggers.title") in user pools and [Amazon Cognito
events](cognito-events.md#cognito-events.title "cognito-events.md#cognito-events.title") in identity pools can become complex. Lambda functions must be
in the same AWS Region as your user pool or identity pool. Shared Lambda
functions can enforce standards for custom authentication flows, user migration,
token generation, and other functions within a Region.

**Common messaging**

Amazon Simple Notification Service (Amazon SNS) requires additional configuration in a Region before you can
send [SMS messages](user-pool-sms-settings.md#user-pool-sms-settings.title "user-pool-sms-settings.md#user-pool-sms-settings.title") to your
users. You can send [email messages](user-pool-email.md#user-pool-email.title "user-pool-email.md#user-pool-email.title")
with Amazon Simple Email Service (Amazon SES) verified identities and domains that are contained within
a Region.

With multi-tenancy, you can share this configuration and maintenance overhead
between all of your tenants. Because Amazon SNS and Amazon SES aren't available in all
AWS Regions, splitting your resources between Regions requires additional
consideration.

When you use [custom messaging providers](user-pool-lambda-custom-sender-triggers.md#user-pool-lambda-custom-sender-triggers.title "user-pool-lambda-custom-sender-triggers.md#user-pool-lambda-custom-sender-triggers.title"), you gain the _common customization_ of a single Lambda function to manage your
message delivery.

[Managed login](cognito-user-pools-managed-login.md#cognito-user-pools-managed-login.title "cognito-user-pools-managed-login.md#cognito-user-pools-managed-login.title") sets a
session cookie in the browser so that it recognizes a user who has already authenticated.
When you authenticate _local users_ in a user pool, their
session cookie authenticates them for all app clients in the same user pool. A local user
exists exclusively in your user pool directory without federation through an external IdP.
The session cookie is valid for one hour. You can't change the session cookie duration.

There are two ways to prevent sign-in across app clients with a hosted UI session
cookie.

- Separate your users into per-tenant user pools.
- Replace hosted UI sign-in with Amazon Cognito user pools API sign-in.

###### Topics

- [User-pool multi-tenancy best
  practices](bp_user-pool-based-multi-tenancy.md "bp_user-pool-based-multi-tenancy.md")
- [App-client multi-tenancy best
  practices](application-client-based-multi-tenancy.md "application-client-based-multi-tenancy.md")
- [User group multi-tenancy best
  practices](group-based-multi-tenancy.md "group-based-multi-tenancy.md")
- [Custom-attribute multi-tenancy
  best practices](custom-attribute-based-multi-tenancy.md "custom-attribute-based-multi-tenancy.md")
- [Custom scope multi-tenancy best
  practices](scope-based-multi-tenancy.md "scope-based-multi-tenancy.md")
- [Multi-tenancy security
  recommendations](multi-tenancy-security-recommendations.md "multi-tenancy-security-recommendations.md")
