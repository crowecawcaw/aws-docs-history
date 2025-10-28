# Using Amazon Cognito user pools security features

You might want to secure your application against network intrusion, password guessing, user
impersonation, and malicious sign-up and sign-in. Your configuration of Amazon Cognito user pools security
features can be a key component in your security architecture. The security of your application
is _Customer responsibility "Security in the cloud"_ as
described in the AWS [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"). The tools in this chapter contribute to the ability of
your application security design to be in line with these goals.

An important decision that you must make when you configure your user pool is whether to
permit public sign-up and sign-in. Some user pool option like confidential clients,
administrative creation and confirmation of users, and user pools without a domain, are subject
to a smaller degree to attacks over the internet. However, a common use case is public clients
that accept sign-up from anyone on the internet and send all operations directly to your user
pool. In any configuration, but especially in the case of these public configurations, we
recommend that you plan and deploy your user pool with security features in mind. Insufficient
security can also affect your AWS bill when unwanted sources create new active users or
attempt to exploit existing users.

MFA and threat protection apply to [local users](cognito-terms.md#terms-localuser "cognito-terms.md#terms-localuser").
Third-party IdPs are responsible for the security posture of [federated users](cognito-terms.md#terms-federateduser "cognito-terms.md#terms-federateduser").

###### User pools security features

**Multi-factor authentication (MFA)**

Request a code that your user pool send by email (with the Essentials or Plus feature
plan) or SMS message, or from an authenticator app, to confirm user pool sign-in.

**Threat protection**

Monitor sign-in for indicators of risk and apply MFA or block sign-in. Add custom
claims and scopes to access tokens. Send MFA codes by email.

**AWS WAF web ACLs**

Inspect incoming traffic to your [user pool
endpoints and authentication API](authentication-flows-public-server-side.md#user-pools-API-operations "authentication-flows-public-server-side.md#user-pools-API-operations") for unwanted activity at the network and
application layers.

**Case sensitvity**

Prevent creation of users whose email address or preferred username is identical to
another user except for character case.

**Deletion protection**

Prevent automated systems from accidentally deleting your user pools. Require
additional confirmation of user pool deletion in the AWS Management Console.

**User existence errors**

Guard against disclosure of existing usernames and aliases in your user pool. Return a
generic error in response to unsuccessful authentication, whether the username is valid or
not.

###### Topics

- [Adding MFA to a user pool](user-pool-settings-mfa.md "user-pool-settings-mfa.md")
- [Advanced security with threat
  protection](cognito-user-pool-settings-threat-protection.md "cognito-user-pool-settings-threat-protection.md")
- [Associate an AWS WAF web ACL with a user pool](user-pool-waf.md "user-pool-waf.md")
- [User pool case sensitivity](user-pool-case-sensitivity.md "user-pool-case-sensitivity.md")
- [User pool deletion protection](user-pool-settings-deletion-protection.md "user-pool-settings-deletion-protection.md")
- [Managing user existence error
  responses](cognito-user-pool-managing-errors.md "cognito-user-pool-managing-errors.md")
