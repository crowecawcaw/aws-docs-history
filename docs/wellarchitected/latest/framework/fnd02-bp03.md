

# FND02-BP03 Employ a centralized identity provider

 For workforce identities (employees and contractors), rely on an identity provider you can use to manage identities in a centralized place. This lets you manage access across multiple applications and systems from a single location, because you are creating, assigning, managing, revoking, and auditing access in one place. 

 **Desired outcome:** 
+  You have a centralized identity provider where you centrally manage workforce users, authentication policies (such as requiring multi-factor authentication (MFA)), and authorization to systems and applications (such as assigning access based on a user's group membership or attributes). 
+  Your workforce users sign in to the central identity provider and federate (single sign-on) to internal and external applications, removing the need for users to remember multiple credentials. 
+  Your identity provider is integrated with your human resources (HR) systems so that personnel changes are automatically synchronised to your identity provider. When a user leaves your organization, access to federated applications and systems (including AWS) is automatically revoked. 
+  You have enabled detailed audit logging in your identity provider and are monitoring these logs for unusual user behavior. 

 **Common anti-patterns:** 
+  Workforce users create separate accounts and credentials in multiple applications instead of using federation and single sign-on. 
+  Identity lifecycle for workforce users is not automated through integration with HR systems, so role changes and departures require manual updates across multiple applications and systems. 
+  Permission sets are assigned to individual users rather than groups, creating administrative burden and inconsistency. 
+  IAM users remain in AWS accounts after federation is implemented, creating parallel authentication paths that bypass centralized controls. 

 **Benefits of establishing this best practice:** 
+  Single place to manage workforce user identities and policies, with the ability to assign access to applications by user or group and monitor sign-in activity. 
+  Role changes synchronised automatically from HR systems update assigned applications and permissions without manual intervention. 
+  Automatic access revocation when a user leaves your organization, because disabling their identity in the centralized provider removes access to federated applications and systems. 
+  Consistent authentication policies (MFA, password complexity, session duration) applied across AWS accounts rather than managed per-account. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A centralized identity provider is a centralized source for workforce identities across your organization. Without it, you must manage disparate user accounts, deal with orphaned credentials when employees leave, and lack a unified view of employee access to resources. Centralization covers the full identity lifecycle (onboarding through role changes to offboarding) and enables single sign-on across federated applications. 

 Organizations that already operate an identity provider such as Okta, Microsoft Entra ID, or Ping Identity get the most value by extending it to AWS through federation rather than creating a separate identity silo. This preserves existing identity governance and keeps access consistent across cloud and on-premises resources. [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) can be the centralized source for organizations without a prior identity provider, though that typically only makes sense when AWS is the primary application landscape. 

 Federation to AWS happens at two levels: 
+  IAM Identity Center is the recommended approach for organizations using [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html). You configure SAML and SCIM integration once, and it scales across your entire AWS organization. 
+  Direct IAM federation configures SAML 2.0 or OIDC identity providers in individual AWS accounts, providing per-account control. However, you lose the efficiency of centralized management as your account count grows. 
+  The integration uses SCIM for user and group provisioning, and SAML for authentication. [SCIM](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html) synchronizes the lifecycle of users and groups from your IdP to AWS. When you create a user in your IdP, SCIM creates the corresponding user in IAM Identity Cente. Then, when you remove them, SCIM also removes them. SAML handles the sign-in flow, where users authenticate with your IdP's credentials (including MFA) and receive an assertion that grants access to AWS accounts through their assigned permission sets. 

 [Permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) in IAM Identity Center are templates of IAM policies. When you assign a user or group to a permission set for an AWS account, Identity Center creates the corresponding IAM role in that account with the right trust relationship. You define access policies once rather than creating identical IAM roles in every account. Assign permission sets to groups rather than individual users. This creates a clear audit trail and lets you update access for many users at once. 

 For CLI and API access, users configure the [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) to authenticate with IAM Identity Center and obtain temporary credentials. For direct IAM federation, programmatic credentials come from [AWS STS AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html) after the SAML assertion is exchanged. 

 Once federation is working, delete IAM users created for human access. These users bypass your centralized authentication policies and lifecycle management, creating a parallel access path that your identity governance cannot track. Use [IAM credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) and [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to [find unused credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html), migrate human users to federation, and then [delete the IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_remove.html) and [groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_delete.html). Apply an [SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) that prevents creation of new IAM users and long-lived credentials to enforce federation. Document and monitor any explicit exceptions (break-glass IAM users for emergency access when federation is unavailable, and service accounts where federation isn't supported). 

**Note**  
 Rotate SCIM access tokens before they expire, following the cadence your identity provider defines (typically 90 days). For more detail, see the [automatic provisioning documentation](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html). Rotate the certificates supporting your identity federation on the cadence your certificate lifecycle policy defines. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose your identity federation approach:** Determine whether to use [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) for centralized multi-account access or [direct IAM federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) for individual AWS accounts. For most organizations with multiple AWS accounts, IAM Identity Center is the recommended approach. Refer to [AWS SRA identity management guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) to design your identity architecture. 

1.  **Enable IAM Identity Center (recommended approach):** If using IAM Identity Center, [enable it for your organization](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html) in your management account. Choose your [AWS Region](https://docs.aws.amazon.com/singlesignon/latest/userguide/regions.html) based on data residency requirements, proximity to your primary user base, and disaster recovery needs. IAM Identity Center is a Regional service, and changing Regions later requires reconfiguration. Configure your [identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html). 

1.  **Connect your external identity provider:** Configure IAM Identity Center to use your centralized identity provider as the identity source. For SAML-based providers like Okta or Microsoft Entra ID, follow the guidance to [connect to an external SAML 2.0 identity provider](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html). For Microsoft Active Directory, [connect to your Active Directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-ad.html) using [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html). Then configure [automatic provisioning using SCIM](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html) to synchronise users and groups from your identity provider to IAM Identity Center. 

1.  **Create and assign permission sets:** Define [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) in IAM Identity Center that grant least privilege access to AWS accounts. [Create permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) using AWS managed policies or customer managed policies. [Assign users and groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html) from your identity provider to permission sets for specific AWS accounts. Favor group-based assignments over individual user assignments. 

1.  **Set up the AWS access portal:** Configure the [AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html) where your workforce users will sign in. Customize the portal URL and [configure the portal's sign-in experience](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps.html). Test access by having users sign in through your identity provider and verify they can access assigned AWS accounts. 

1.  **Configure CLI and SDK access:** Enable your users to use federated credentials with the AWS CLI and SDKs. Provide guidance on [configuring the AWS CLI to use IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html). Users can run aws configure sso to set up their CLI profiles with IAM Identity Center authentication. 

1.  **Implement direct IAM federation (alternative approach):** If federating directly to individual AWS accounts, [create SAML 2.0 identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) or [OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) in each AWS account. [Create IAM roles for SAML federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_saml.html) with appropriate trust policies and permissions. Configure your identity provider to [enable console access through SAML](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html). 

1.  **Identify and audit existing IAM users:** Use [IAM credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) to [identify unused credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html) across your AWS accounts. Use [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to identify IAM users and roles not used recently. Document which IAM users are still needed for service accounts or emergency access (break-glass scenarios). 

1.  **Remove unnecessary IAM users and groups:** Once federation is working, [delete IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_remove.html) that have been replaced by federated identities. [Delete unused IAM groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_delete.html). Before deletion, verify that users can access AWS through federation. For any break-glass IAM users retained for emergency access when federation is unavailable, require MFA, use strong passwords stored in a secure secret management system, restrict access to specific source IP addresses where possible, and enable CloudTrail alerts for any use. Document a formal break-glass procedure that includes post-use review and credential rotation, and record the justification for each remaining IAM user. 

1.  **Enforce federation with preventive controls:** Apply a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to your organization to [prevent creation of new IAM users](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html) and long-lived credentials. This enforces the practice where all workforce access to AWS uses federated identities. 

1.  **Monitor and audit federation activity:** Monitor [IAM Identity Center CloudTrail logs](https://docs.aws.amazon.com/singlesignon/latest/userguide/understanding-sso-entries.html) to track authentication events and permission set assignments. Set up alerts for unusual authentication patterns or failed authentication attempts. Regularly review permission set assignments and verify least privilege principles. Establish a process for rotating [SCIM access tokens](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html) and federation certificates. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP02 Use strong sign-in mechanisms](fnd02-bp02.md) 
+  [FND02-BP04 Establish controls to manage access based on lifecycle](fnd02-bp04.md) 
+  [FND02-BP05 Grant least privilege access](fnd02-bp05.md) 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 

 **Related documents:** 
+  [Identity federation in AWS](https://aws.amazon.com/identity/federation/) 
+  [Security best practices in IAM - Require human users to use federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) 
+  [AWS Identity and Access Management best practices](https://aws.amazon.com/iam/resources/best-practices/) 
+  [Delegating permission set management and account assignment in IAM Identity Center](https://aws.amazon.com/blogs/security/delegating-permission-set-management-and-account-assignment-in-aws-iam-identity-center/) 
+  [AWS CLI v2: IAM Identity Center credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Dive deep into IAM Identity Center](https://www.youtube.com/watch?v=3HejqmJcDoQ) 
+  [AWS re:Inforce 2024 - Securing human access to AWS at scale](https://www.youtube.com/watch?v=N82s9TF_b9w) 

 **Related examples:** 
+  [Workshop: Using IAM Identity Center to achieve strong identity management](https://catalog.us-east-1.prod.workshops.aws/workshops/590f8439-42c7-46a1-8e70-28ee41498b3a/en-US) 

 **Related tools:** 
+  [AWS Security Competency Partners](https://aws.amazon.com/security/partner-solutions/) 

 **Related services:** 
+  [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 