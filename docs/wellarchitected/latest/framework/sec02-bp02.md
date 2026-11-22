

# SEC02-BP02 Use temporary credentials

 Long-term credentials persist until someone removes them, which gives an unauthorized party durable access if the credentials are inadvertently disclosed. Temporary credentials expire automatically, which shrinks the window in which exposed credentials are useful. Use short-lived credentials for both human and machine access wherever a workload supports them, and reserve long-term credentials for the few cases that cannot avoid them. 

 **Desired outcome:** 
+  Your human users authenticate through federation and receive temporary credentials rather than holding long-term access keys. 
+  Your machine identities obtain short-lived credentials from assigned roles instead of embedded static keys. 
+  You inventory, tightly scope, monitor, and rotate any remaining long-term credentials on a defined schedule. 
+  Your codebases, mobile apps, and repositories contain no embedded long-term access keys. 

 **Common anti-patterns:** 
+  Developers use long-term access keys from IAM users instead of requesting temporary credentials through federation. 
+  Developers embed long-term access keys in source code and push it to public repositories. 
+  Developers embed long-term access keys in mobile apps that ship to app stores. 
+  Users share long-term access keys with each other, or leave the organization while still holding them. 
+  Teams use long-term access keys for machine identities in cases where temporary credentials would work. 

 **Benefits of establishing this best practice:** 
+  Automatic expiration limits how long inadvertently disclosed credentials remain usable. 
+  Federation and roles remove the operational burden of distributing and rotating static keys. 
+  Fewer long-term secrets mean a smaller attack surface across code, devices, and repositories. 
+  Scoped, monitored exceptions keep the remaining long-term credentials auditable and containable. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Nearly every request to an AWS service is signed with [access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), and those keys are either temporary or long-term. Temporary credentials are issued on demand and expire, usually within hours. Long-term credentials, the access keys attached to an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) or the [account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html), stay valid until you delete them. When you federate or assume an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html), AWS generates temporary credentials automatically, so most access needs no static key. 

 The risk of a long-term key is proportional to how long it lives and how widely it travels. A key checked into a repository, pasted into a script, or shipped inside a mobile app can circulate for years before anyone notices. Because the key does not expire, a single exposure stays usable until someone finds and revokes it. Temporary credentials are worthless once expired, even if inadvertently disclosed. So federate workforce users and assign roles to workloads, keeping IAM users only where you cannot avoid them. 

 Machine identities work the same way by assuming roles. Compute services obtain credentials from a role attached to the runtime, so no key is stored on the workload. Workloads outside AWS are harder, because there is no AWS runtime to supply a role. A certificate-based trust or a token exchange from an external provider gives these systems temporary credentials without a static AWS key. 

 Some integrations cannot use temporary credentials, such as a third-party tool that accepts only a static key or a legacy database login. Treat these as exceptions with compensating controls. Scope each exception to the narrowest set of actions, restrict the source networks that can use it, monitor its usage, and rotate it on a schedule. A managed secrets service handles storage and rotation for the credentials that must persist. A token-vending pattern can hand out short-lived credentials to callers that would otherwise need a static key. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Federate human users to a central identity provider:** Require workforce users to [federate and access AWS with temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) instead of using IAM users. Set up either [direct federation](https://aws.amazon.com/identity/federation/) to each account or [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) with your chosen provider. Users can then request temporary credentials from the command line through [SAML federation](https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/) or [IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html). 

1.  **Grant third parties access through roles:** For SaaS providers and partners, use [cross-account roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) and [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) instead of issuing access keys. For business-to-business integrations, the [Amazon Cognito OAuth 2.0 client credentials grant](https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoints-oauth-grants.html) provides scoped machine access. 

1.  **Issue temporary credentials to external application users:** For customer-facing web, mobile, and client applications, use [Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) to vend temporary credentials backed by IAM roles. Define a separate limited role for unauthenticated guest users. 

1.  **Assign roles to machine identities:** Require workloads to [use temporary credentials through IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles). Use [roles for Amazon EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html), [Lambda execution roles](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html), the [AWS IoT Core credential provider](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html) for devices, and [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) for systems outside AWS. 

1.  **Contain the credentials that must remain long-term:** Where temporary credentials are not supported, grant least-privilege permissions, restrict the allowed source networks in the role trust policy, and monitor usage with alerts for misuse. Consider limiting an IAM user to the AssumeRole action for a single role, and enforce [permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html). 

1.  **Store and rotate remaining secrets centrally:** Manage database logins and other non-AWS secrets in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), which supports [rotation and service integration](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating.html). For multi-cloud callers, exchange source-provider credentials for temporary AWS credentials with [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html), and [rotate](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) any keys that persist. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC02-BP03 Store and use secrets securely](sec02-bp03.md) 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 
+  [SEC02-BP05 Audit and rotate credentials periodically](sec02-bp05.md) 
+  [SEC03-BP04 Share resources securely within your organization](sec03-bp04.md) 

 **Related documents:** 
+  [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) 
+  [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) 
+  [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [IAM identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) 
+  [The AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) 
+  [Security partner solutions](https://aws.amazon.com/security/partner-solutions/) 
+  [Access AWS using a Google Cloud Platform native workload identity](https://aws.amazon.com/blogs/security/access-aws-using-a-google-cloud-platform-native-workload-identity/) 
+  [How to access AWS resources from Microsoft Entra ID tenants using AWS STS](https://aws.amazon.com/blogs/security/how-to-access-aws-resources-from-microsoft-entra-id-tenants-using-aws-security-token-service/) 

 **Related videos:** 
+  [IAM Core Workshop (Formerly: IAM Immersion Day)](https://studio.us-east-1.prod.workshops.aws/workshops/public/18b3622c-5d4c-45c9-9834-6a7091109072) 

 **Related services:** 
+  [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 
+  [Amazon EC2](https://aws.amazon.com/pm/ec2/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 