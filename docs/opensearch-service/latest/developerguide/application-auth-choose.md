

# Choosing an authentication method for OpenSearch UI
<a name="application-auth-choose"></a>

Every OpenSearch UI application authenticates its users through AWS Identity and Access Management (IAM), so you control who reaches the interface with IAM policies. With OpenSearch UI, you can choose from more than one authentication method on top of that foundation. The right choice depends on the size of your team, the identity provider you already use, and how your users access the application.

## Comparing the methods
<a name="application-auth-choose-comparison"></a>

The following table compares the three authentication methods that OpenSearch UI supports.


| Criteria | IAM authentication | AWS IAM Identity Center | SAML federation through IAM | 
| --- | --- | --- | --- | 
| Best for | Programmatic access, AWS CLI users, and single-account setups | Single sign-on for teams and organizations with multiple users | Organizations that already use a SAML identity provider without AWS IAM Identity Center | 
| Sign-in experience | A Signature Version 4 presigned URL, or federated console access | A single sign-on portal with a user name and password | Federated console sign-in through your identity provider | 
| Setup effort | Low—an IAM policy only | Medium—an AWS IAM Identity Center instance, an IAM role, and a trust policy | Medium to high—identity provider configuration, an IAM role, and a SAML trust policy | 
| Prerequisites | An IAM role with the required permissions | An AWS IAM Identity Center instance, and an IAM role with both a permissions policy and a trust policy | A configured SAML identity provider, and an IAM role with a SAML trust policy | 
| Support for multiple users | Manual—each user needs IAM credentials or assumes a role | Built in—users are managed in AWS IAM Identity Center or synchronized from your identity provider | Through your identity provider | 
| Multi-factor authentication | Through your IAM multi-factor authentication settings | Built in through AWS IAM Identity Center or an upstream identity provider | Through your SAML identity provider | 

## When to choose IAM authentication
<a name="application-auth-choose-iam"></a>

Choose IAM authentication in any of the following cases:
+ You work alone or in a small team.
+ You need programmatic or AWS CLI access to the application.
+ You want the simplest possible setup.
+ You build automation that generates presigned URLs.

This method requires the following:
+ An AWS account with the base IAM permissions.
+ At least one OpenSearch domain or serverless collection in the AWS Region.
+ The AWS CLI configured with credentials.

For instructions on setting up IAM authentication, see [IAM authentication for OpenSearch UI](application-auth-iam.md).

## When to choose AWS IAM Identity Center
<a name="application-auth-choose-idc"></a>

Choose AWS IAM Identity Center in any of the following cases:
+ Your organization uses single sign-on.
+ You have multiple users who need access.
+ You want a browser-based sign-in experience without presigned URLs.
+ You already use AWS IAM Identity Center for other AWS services.

This method requires the following:
+ An AWS account with the base and AWS IAM Identity Center IAM permissions.
+ AWS IAM Identity Center enabled in your account or organization.
+ An IAM role with both the required permissions policy and a trust policy for `sso.amazonaws.com`.
+ At least one OpenSearch domain or serverless collection in the AWS Region.

For instructions on setting up AWS IAM Identity Center authentication, see [AWS IAM Identity Center authentication for OpenSearch UI](application-auth-idc.md).

## When to choose SAML federation
<a name="application-auth-choose-saml"></a>

Choose SAML federation when you use a SAML identity provider and you want your users to sign in through your existing identity provider portal. There are two paths:

1. Your identity provider synchronizes users into AWS IAM Identity Center, which handles the OpenSearch UI integration. This is the recommended path.

1. Your identity provider federates directly into an IAM role.

**Important**  
OpenSearch UI is a standalone AWS resource, not a feature inside an OpenSearch domain. Direct SAML integration, as configured for OpenSearch Dashboards, is not supported. SAML access must go through IAM or AWS IAM Identity Center.

For instructions on setting up SAML federation, see [Enabling SAML federation with AWS Identity and Access Management](application-enable-SAML-identity-federation.md).

## Deciding between the methods
<a name="application-auth-choose-decide"></a>

Answer the following questions in order:

Do you need single sign-on with an identity provider?  
If not, use IAM authentication. If you do, continue to the next question.

Is AWS IAM Identity Center enabled in your account?  
If it is, use AWS IAM Identity Center. If it isn't but you can enable it, enable it and then use AWS IAM Identity Center. If you can't enable it, use SAML federation through IAM.

For more information about the permissions that each method requires, see [IAM policy reference for OpenSearch UI](application-iam-policy-reference.md).