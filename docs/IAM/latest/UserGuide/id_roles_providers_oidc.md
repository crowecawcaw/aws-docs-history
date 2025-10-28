# OIDC federation

Imagine that you are creating an application that accesses AWS resources, such as GitHub
Actions that uses workflows to access Amazon S3 and DynamoDB.

When you use these workflows, you make requests to AWS services that must be signed with
an AWS access key. However, we **strongly** recommend that you do
**not** store AWS credentials long-term in applications outside
AWS. Instead, configure your applications to request temporary AWS security credentials
dynamically when needed using _OIDC federation_. The supplied temporary
credentials map to an AWS role that only has permissions needed to perform the tasks required
by the application.

With OIDC federation, you don't need to create custom sign-in code or manage your own user
identities. Instead, you can use OIDC in applications, such as GitHub Actions or any other
[OpenID Connect (OIDC)](http://openid.net/connect/ "http://openid.net/connect/")-compatible IdP, to
authenticate with AWS. They receive an authentication token, known as a JSON Web Token (JWT),
and then exchange that token for temporary security credentials in AWS that map to an IAM
role with permissions to use specific resources in your AWS account. Using an IdP helps you
keep your AWS account secure because you don't have to embed and distribute long-term security
credentials with your application.

OIDC federation supports both machine-to-machine authentication (such as CI/CD pipelines,
automated scripts, and serverless applications) and human user authentication. For human user
authentication scenarios where you need to manage user sign-up, sign-in, and user profiles,
consider using [Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/") as an identity broker. For
details about using Amazon Cognito with OIDC, see [Amazon Cognito for mobile apps](id_federation_common_scenarios.md#id_roles_providers_oidc_cognito "id_federation_common_scenarios.md#id_roles_providers_oidc_cognito").

###### Note

JSON Web Tokens (JWTs) issued by OpenID Connect (OIDC) identity providers contain an
expiration time in the `exp` claim that specifies when the token expires. IAM
provides a five-minute window beyond the expiration time specified in the JWT to account for
clock skew, as allowed by the [OpenID Connect (OIDC) Core 1.0
standard](https://openid.net/specs/openid-connect-core-1_0.html "https://openid.net/specs/openid-connect-core-1_0.html"). This means OIDC JWTs received by IAM after the expiration time but
within this five-minute window are accepted for further evaluation and processing.

###### Topics

- [Additional resources for OIDC
  federation](#id_roles_providers_oidc_resources "#id_roles_providers_oidc_resources")
- [Create an OpenID Connect (OIDC) identity
  provider in IAM](id_roles_providers_create_oidc.md "id_roles_providers_create_oidc.md")
- [Obtain the thumbprint for an
  OpenID Connect identity provider](id_roles_providers_create_oidc_verify-thumbprint.md "id_roles_providers_create_oidc_verify-thumbprint.md")
- [Identity-provider controls for
  shared OIDC providers](id_roles_providers_oidc_secure-by-default.md "id_roles_providers_oidc_secure-by-default.md")

## Additional resources for OIDC

federation

The following resources can help you learn more about OIDC federation:

- Use OpenID Connect within your GitHub workflows by [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services "https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services")
- [Amazon Cognito Identity](https://docs.amplify.aws/lib/auth/advanced/q/platform/android/ "https://docs.amplify.aws/lib/auth/advanced/q/platform/android/") in the _Amplify Libraries for Android Guide_ and
  [Amazon Cognito Identity](https://docs.amplify.aws/lib/auth/advanced/q/platform/ios/ "https://docs.amplify.aws/lib/auth/advanced/q/platform/ios/")
  in the _Amplify Libraries for Swift Guide_.
- [How to
  use external ID when granting access to your AWS resources](https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/ "https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/") on the
  _AWS Security Blog_ provides guidance on securely configuring
  cross-account access and external identity federation.
