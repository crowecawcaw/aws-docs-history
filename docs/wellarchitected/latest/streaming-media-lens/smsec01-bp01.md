

# SMSEC01-BP01 Use an identity provider to authenticate viewers and access policies to implement least privilege access to protected content
<a name="smsec01-bp01"></a>

Protect content and infrastructure from access by outside personnel, as unauthorized access could lead to content theft. Even internal access should be controlled to reduce the risk of unauthorized access or accidental deletion or loss of data.

**Desired outcome:**
+ A well defined access policy restricts anyone from accessing content without permission and guarantees that new data and infrastructure is created with access control in mind
+ Only authenticated and authorized users can access protected streaming content
+ Access permissions are dynamically granted based on user identity, subscription status, and content licensing
+ Centralized identity management across all streaming applications and services

**Common anti-patterns:**
+ Organizations allow unauthenticated access to premium streaming content, relying solely on obscured URLs rather than identity verification.
+ Teams use a single shared API key or static credential for all viewer sessions instead of issuing per-user tokens with scoped permissions.
+ Organizations grant broad access permissions to all authenticated users without differentiating based on subscription tier, content licensing, or geographic entitlements.
+ Teams store viewer credentials in application code or client-side storage without encryption, enabling credential harvesting and account takeover.
+ Organizations fail to federate identity across streaming applications, forcing users to maintain separate credentials and blocking centralized access revocation.

**Benefits of establishing this best practice:**
+ Only paying subscribers and entitled viewers can access premium streams, directly blocking unauthorized consumption that erodes subscription and advertising revenue.
+ Granular access policies enforce geographic and temporal content restrictions required by licensing agreements, reducing legal exposure from unauthorized distribution.
+ Centralized identity management with federated authentication removes credential sprawl and enables immediate access revocation when accounts are compromised or subscriptions lapse.
+ A single identity provider across all streaming applications simplifies user provisioning, reduces support burden for password resets, and provides unified audit trails for access events.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Access to private content should be granted only to authenticated and authorized viewers using an identity provider (IdP). On AWS, Amazon Cognito can be used as an IdP to authenticate users and authorize access to content hosted on Amazon S3, or on a custom origin service built on Amazon EC2. You can also establish trust between identity providers to avoid sharing credentials and simplify the authentication flow for your media player. Amazon Cognito provides both temporary AWS credentials as AWS STS (Security Token Service) tokens, as well as JWTs (JSON Web Tokens), to access protected resources. You can also use Amazon Cognito to federate an identity pool or user pool with different identity providers, such as SAML providers like Active Directory Federation Services or Okta, OpenID Connect (OIDC) providers such as Auth0, and other public identity providers such as Google, Twitter, or Facebook.

In addition to leveraging an IdP, centralize resource access control based on the identity established by IdP through the application API layer. For example, Amazon API Gateway and AWS AppSync allow you to specify an Amazon Cognito User Pool as an IdP for the resources being protected, so that bearer tokens can be validated before granting access. Amazon API Gateway and AWS AppSync also allow you to create custom authorizers, so that you can perform additional application logic to allow or deny access to a resource based on claims in the access token, or if a non-supported token, such as SAML, is provided to the API.

Many services, such as AWS Elemental MediaPackage v2 allow you to define Identity and Access Management (IAM) policies and resources to allow or restrict ingest and egress.

### Implementation steps
<a name="implementation-steps"></a>

1. **Set up your identity provider:** [Configure Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html) for viewer authentication.

1. **Define access groups:** Define groups that should have access to specific actions and permissions.

1. **Create IAM policies:** [Create IAM policies](https://docs.aws.amazon.com/mediapackage/latest/userguide/security-iam.html) to control which users can perform the actions within specific groups.

1. **Apply IAM policies:** Apply IAM policies to AWS services.

1. **Create an Amazon Cognito user pool:** [Create an Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html) to define which users can access which parts of your infrastructure.

1. **Integrate the Cognito SDK:** Use the Amazon Cognito SDK to control authentication and connect it with your user pool.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC01-BP02 Restrict content origin access to allow only authorized content distribution networks](smsec01-bp02.html)

**Related documents**
+ [Getting Started with Amazon Cognito Identity Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html)
+ [AWS Organizations IAM Security](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_iam.html)
+ [AWS Elemental MediaPackage IAM Security](https://docs.aws.amazon.com/mediapackage/latest/userguide/security-iam.html)

**Related services**
+ [Amazon Cognito](https://aws.amazon.com/cognito/)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [AWS AppSync](https://aws.amazon.com/appsync/)
+ [AWS Elemental MediaPackage v2](https://aws.amazon.com/mediapackage/)