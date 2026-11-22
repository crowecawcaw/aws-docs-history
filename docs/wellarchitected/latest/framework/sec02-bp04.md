

# SEC02-BP04 Rely on a centralized identity provider for users and machines

 When each application manages its own identities, users juggle multiple logins and security teams lose a single view of who has access. A centralized identity provider makes one system the source of truth for authentication, authorization, and lifecycle management across your workloads. This applies to machine identities as well as people, so service-to-service calls authenticate through the same governed system. 

 **Desired outcome:** 
+  Your workloads authenticate users against one identity provider that serves as the source of truth. 
+  Your provider supports industry-standard protocols and consistent authorization controls across applications. 
+  Your users sign in once and reach the applications they are entitled to, and your security team sees authentication centrally. 
+  Your machine identities authenticate and authorize through the same centralized system as your users. 
+  Your user lifecycle events, from creation to deactivation, propagate from the provider without manual per-application work. 

 **Common anti-patterns:** 
+  Teams build a separate authentication system for each application. 
+  Teams store credentials directly in application databases. 
+  Teams manage users through manual, per-application processes. 
+  Teams use different identifiers for the same user across applications. 
+  Teams skip token validation and accept tokens without checking signature, expiry, or audience. 
+  Teams ignore the full user lifecycle, so accounts remain active after a user's access ends. 
+  Teams manage machine identities ad hoc and hard-code service credentials in code or configuration. 

 **Benefits of establishing this best practice:** 
+  Uniform controls across workloads close the gaps that per-application identity systems create. 
+  Automated lifecycle management lowers administrative effort and human error. 
+  Single sign-on reduces credential fatigue and improves the user experience. 
+  Centralized authentication logging improves threat detection and incident response. 
+  One identifier per user keeps records consistent even when personal details change. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Document the identity types in your workload, their permission needs, and where each identity originates. That inventory tells you whether you need a customer directory, workforce federation, machine-to-machine authentication, or all three. 

### Customer identity
<a name="customer-identity"></a>

 [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) manages customer identities directly and also federates to external providers. For customer-facing applications, social sign-in through providers such as Amazon, Google, Facebook, or Apple lowers the barrier to registration. For internal applications, SAML or OpenID Connect federation to a corporate directory keeps workforce identity under existing governance. 

 Prefer managed authentication surfaces such as [user pool managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html) over custom flows. Or build on a library such as [AWS Amplify Auth](https://docs.amplify.aws/react/build-a-backend/auth/set-up-auth/), which handles token management and secure storage. Use an immutable identifier such as a UUID for each user. Identifiers such as email addresses and phone numbers can easily change, which makes them unreliable. Validate the signature, expiry, and audience on every token, and set token lifetimes to match the sensitivity of the application. 

### Machine identity
<a name="machine-identity"></a>

 Within AWS, services assume an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) to obtain temporary credentials, and systems outside AWS obtain temporary credentials through [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html). For custom service-to-service authentication, use [Amazon Cognito machine-to-machine authentication](https://aws.amazon.com/blogs/mt/configuring-machine-to-machine-authentication-with-amazon-cognito-and-amazon-api-gateway-part-2/) with the OAuth 2.0 client credentials flow to centralize service identities and scopes. Mutual TLS lets client and server authenticate each other. 

### Workforce identity
<a name="workforce-identity"></a>

 When your employees need access to AWS accounts and AWS-managed analytics applications, centralize that access through [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). Connect your existing identity source (such as your corporate IdP) once. Identity Center then becomes the single reference to your workforce that AWS services share. Workforce users receive single sign-on to the accounts and applications they are entitled to. Joiner, mover, and leaver changes continue to flow from your IdP. 

 Identity Center also supports [trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html), which attaches the signed-in user's identity to each request as AWS services hand it off. A service then authorizes access based on the user's group associations and records the user's identity in AWS CloudTrail. For analytics access to data lakes, services such as Amazon Redshift, AWS Quick, Amazon Athena, Amazon EMR, and AWS Glue can propagate the end-user identity to [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) and [Amazon S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html). Lake Formation and S3 Access Grants then grant fine-grained, user-level or group-level access to the data and vend temporary credentials, so permissions no longer live in a broad service role. 

### Observability
<a name="observability"></a>

 Route authentication events to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to detect suspicious patterns such as repeated failed logins, sign-ins from unusual locations, or unexpected privilege escalation. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Stand up your central user directory for customer identity:** Create an [Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html#what-is-amazon-cognito-user-pools) as the source of truth for users. Configure [password policies](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users-passwords.html), [MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html), and account recovery, and enable threat protection features that detect exposed credentials and adapt authentication to risk. 

1.  **Federate external identity providers:** Connect [social identity providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-social-idp.html) for consumer applications, and configure [SAML](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp.html) or [OIDC](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc-idp.html) federation for enterprise applications. Apply consistent [attribute mapping](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html) so profiles stay consistent across providers. 

1.  **Implement secure authentication flows:** Use the authorization code flow with [Proof Key for Code Exchange (PKCE)](https://docs.aws.amazon.com/cognito/latest/developerguide/using-pkce-in-authorization-code.html) for web and single-page applications that cannot store a client secret. Integrate a library such as [AWS Amplify Authentication](https://docs.amplify.aws/react/build-a-backend/auth/set-up-auth/) for token handling, and configure token expiration and refresh to match your security requirements. 

1.  **Design authorization:** Organize users with [groups](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html) and [custom attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html) that reflect roles. For centralized fine-grained authorization, evaluate [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html), which uses the Cedar policy language and integrates with Cognito identity data. 

1.  **Automate the user lifecycle:** Use [Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html) to customize authentication and user management, establish regular access reviews and account deactivation, and turn on account-takeover protection and risk-based adaptive authentication. 

1.  **Authenticate machine identities centrally:** For AWS service-to-service calls, use [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) with least-privilege permissions. For custom workloads, use [Amazon Cognito machine-to-machine authentication](https://aws.amazon.com/blogs/mt/configuring-machine-to-machine-authentication-with-amazon-cognito-and-amazon-api-gateway-part-2/) with the OAuth 2.0 client credentials flow, and define rotation and monitoring for service identities. 

1.  **Centralize workforce access with IAM Identity Center:** For employee access to AWS accounts and AWS-managed applications, enable [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html) and connect your existing [identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html) so workforce users sign in once against your corporate IdP. Where workforce users reach data through analytics services such as Amazon Redshift, AWS Quick, Amazon Athena, or Amazon EMR, enable [trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html) and manage fine-grained data permissions in [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) and [Amazon S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html) so access is authorized and audited against the end user's identity rather than a shared service role. 

1.  **Centralize identity monitoring:** Send Cognito authentication events to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), set alarms for suspicious activity, and build dashboards to track identity system health and usage. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC02-BP01 Identify principals and identity use-cases](sec02-bp01.md) 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 
+  [SEC01-BP04 Reduce security management scope](sec01-bp04.md) 

 **Related documents:** 
+  [Create an application in the Amazon Cognito console](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-user-pools-application.html) 
+  [Integrate Amazon Cognito authentication with web and mobile apps](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-integrate-apps.html) 
+  [Machine-to-machine identity management](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) 
+  [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) 
+  [Trusted identity propagation overview](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html) 
+  [Setting up AWS Lake Formation with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html) 
+  [Setting up Amazon S3 Access Grants with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-s3.html) 
+  [Simplify data lake access control with trusted identity propagation, Lake Formation, and S3 Access Grants](https://aws.amazon.com/blogs/big-data/simplify-data-lake-access-control-for-your-enterprise-users-with-trusted-identity-propagation-in-aws-iam-identity-center-aws-lake-formation-and-amazon-s3-access-grants/) 

 **Related examples:** 
+  [How to monitor, optimize, and secure Amazon Cognito machine-to-machine authorization](https://aws.amazon.com/blogs/security/how-to-monitor-optimize-and-secure-amazon-cognito-machine-to-machine-authorization/) 
+  [Configuring machine-to-machine authentication with Amazon Cognito and Amazon API Gateway – Part 1](https://aws.amazon.com/blogs/mt/configuring-machine-to-machine-authentication-with-amazon-cognito-and-amazon-api-gateway-part-1/) 
+  [Configuring machine-to-machine authentication with Amazon Cognito and Amazon API Gateway – Part 2](https://aws.amazon.com/blogs/mt/configuring-machine-to-machine-authentication-with-amazon-cognito-and-amazon-api-gateway-part-2/) 
+  [Simplify fine-grained authorization with Amazon Verified Permissions and Amazon Cognito](https://aws.amazon.com/blogs/security/simplify-fine-grained-authorization-with-amazon-verified-permissions-and-amazon-cognito/) 
+  [Code examples for Amazon Cognito using AWS SDKs](https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples.html) 
+  [Set up cross-account AWS Glue Data Catalog access with Lake Formation and IAM Identity Center (Redshift and QuickSight)](https://aws.amazon.com/blogs/big-data/set-up-cross-account-aws-glue-data-catalog-access-using-aws-lake-formation-and-aws-iam-identity-center-with-amazon-redshift-and-amazon-quicksight) 
+  [Access AWS services programmatically using trusted identity propagation](https://aws.amazon.com/blogs/security/access-aws-services-programmatically-using-trusted-identity-propagation/) 

 **Related workshops:** 
+  [Amazon Cognito workshop](https://catalog.workshops.aws/wyld-pets-cognito) 