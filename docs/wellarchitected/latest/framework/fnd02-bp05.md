

# FND02-BP05 Grant least privilege access

 Grant principals only the access they need to perform specific actions on specific resources under defined conditions. Use group and attribute memberships to set permissions at scale instead of managing individual user permissions. For example, you can give a group of developers access only to resources for their project. When a developer leaves the project, their access is removed automatically without changing the underlying policies. 

 **Desired outcome:** 
+  Your principals have only the minimum permissions required for their specific job functions, adhering to the principle of least privilege. 
+  You use separate AWS accounts to isolate different environments, providing strong security boundaries between development, testing, and production workloads. 
+  When access to any environment is needed for specific tasks, you grant limited and controlled access only for the duration of those tasks and revoke it immediately after completion. 
+  Group membership and attributes from your centralized identity provider govern user permissions and propagate automatically to your AWS environments, reducing individual-user administration. 
+  Administrator privileges are restricted to a small, trusted group, and machine or system accounts have only the minimum permissions required to perform their intended tasks. 

 **Common anti-patterns:** 
+  Granting users administrator permissions or using the root user account unnecessarily for daily activities. 
+  Managing permissions for individual users and duplicating them across many users rather than using groups and attributes. 
+  Creating overly permissive policies without proper scoping, or defining groups at too high a level. 
+  Not managing groups, attributes, and memberships through a standardized identity provider integrated with AWS environments. 
+  Creating overly restrictive access policies without an established process for permission refinement, forcing users to work around security controls or delaying business operations. 
+  Relying solely on attribute-based access control for environment isolation instead of account boundaries. 

 **Benefits of establishing this best practice:** 
+  Reduced scope of impact from security incidents by limiting the access available to any exposed credential. 
+  Simplified permission management at scale by using groups and attributes from your centralized identity provider. 
+  Improved auditability and compliance posture through clearly defined, scoped permissions that provide clearer evidence of regulatory adherence. 
+  Reduced risk of accidental or intentional misuse of resources because principals can only perform actions relevant to their specific job functions and projects. 
+  Faster onboarding and offboarding through attribute-based and group-based access controls that automatically adjust permissions as roles and project assignments change. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The principle of [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) limits the impact of any security incident. When credentials are exposed through phishing, insider threat, or system vulnerability, the scope of impact is bounded by the permissions granted to that identity. Restrict each identity to the actions its role requires, so a compromise stays contained to one account. In AWS, IAM users and roles have no default permissions. The root user has full access, so reserve it for [tasks that require root access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) and closely monitor its use. 

 Traditional per-user permission management does not scale. Managing individual user permissions across hundreds or thousands of users leads to permission drift, orphaned access, and security gaps. Assign permissions to groups and attributes that reflect your organizational structure instead of to individual users. When a developer joins a project, their project attribute changes and their permissions adjust automatically. When they leave, those permissions are removed without manual intervention. 

 AWS policies attach to principals (users, roles, or resources) or to IAM groups when you manage multiple users together. Policies specify actions, resources, and conditions for access. Conditions scope access further. For example, the aws:PrincipalOrgID [condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) denies actions when the requestor is outside your AWS Organization. The aws:CalledVia condition key controls requests that AWS services make on your behalf, such as AWS CloudFormation creating an AWS Lambda function. 

 Combine policy types to establish defense-in-depth. [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) at the organization or organizational unit level set maximum permissions that apply across accounts. [Permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) cap the maximum permissions that identity-based policies can grant to a specific IAM user or role. Use permissions boundaries when you delegate IAM policy creation to workload teams but need to prevent privilege escalation beyond a defined limit. Identity policies and resource policies then define the specific permissions within those limits. 

 Account isolation provides the strongest security boundary in AWS. Separate accounts for development, testing, and production make sure that a developer with full administrative access in development cannot accidentally or intentionally affect production systems. Combined with SCPs that block cross-environment actions, this architecture prevents entire classes of security incidents. 

 Attribute-based access control (ABAC) defines permissions from attributes (implemented as tags) attached to both principals and resources. When users change roles or projects, attribute updates replace policy rewrites. For example, you can grant developers access only to resources tagged with their project ID, and permissions adjust as project assignments change. Don't rely on ABAC alone for environment isolation, because external parties can manipulate tags in ways that grant unintended access. Use account boundaries for environment isolation, and use ABAC for access refinement within an environment. 

**Important**  
 If you require IAM role chaining from IAM roles assumed through IAM Identity Center, session values like source-identity and principal tags will not propagate. Design your ABAC strategy to avoid role chaining dependencies, or grant the required permissions directly in IAM Identity Center permission sets. 

 Permission management at scale requires continuous analysis. [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) can [generate policies based on actual access activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) captured in AWS CloudTrail logs, so policies match real usage. [Unused access analysis](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) identifies roles, access keys, passwords, and permissions not used within a threshold period, so you can remove access that is no longer needed. 

 Overly restrictive policies force users to request permissions for routine tasks, which encourages workarounds and shadow IT. Refine permissions using data from access-analysis tools instead of loosening them. Give teams autonomy within defined boundaries, and provide a governed process for expansion when their work requires it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement least privilege policies:** Assign access policies with least privilege to [IAM groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) and [roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that reflect the user role or function you have defined. Start from the minimum set of actions required to complete a task and expand only when access analysis demonstrates genuine need. Avoid attaching policies directly to individual users. Assign them to groups and roles so that access changes are centralized and auditable. Review [IAM policies and permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for the policy types available and how they combine during authorization evaluation. 

1.  **Isolate environments through separate AWS accounts:** Use separate AWS accounts for development and production environments, and control access between them using [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html), [resource policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based), and [identity policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_id-based). 

1.  **Remove root user credentials from member accounts:** For multiple AWS accounts managed through [AWS Organizations](https://aws.amazon.com/organizations/), remove root user credentials from member accounts to help prevent unauthorized use. For more information, see [Centrally manage root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management). 

1.  **Generate policies based on access activity:** Determine necessary permissions by analyzing [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) logs. [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) can [automatically generate](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) an IAM policy based on access activity. Use IAM Access Advisor, a feature available in the IAM console and API, to [track last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html) for users, groups, roles, and policies. 

1.  **Identify and remediate unused access:** Enable [IAM Access Analyzer unused access analysis](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) at the organization level to monitor for unused roles, access keys, passwords, and permissions. Review findings and revoke permissions that are no longer needed. Establish an ongoing review cadence for permission reduction as part of your continuous refinement process. 

1.  **Use AWS managed policies for common job functions:** Start with [pre-defined policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) for roles like billing, database administration, and data science and move toward creating fine-grained permissions. These are helpful templates for customization. 

1.  **Limit access to production environments:** Grant users access to production environments only with a valid task, after which access must be revoked. Consider using [temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and break-glass procedures that trigger alerts and require approval. 

1.  **Implement permissions boundaries:** Use [permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) as managed policies that cap the maximum permissions an identity-based policy can grant to an IAM entity. An entity can only perform actions allowed by both its identity-based policies and its permissions boundaries. 

1.  **Refine access using ABAC and resource tags:** Use [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) with resource tags to fine-tune permissions where supported. Only use ABAC for access control when both principals and resources are owned by your AWS Organization. External parties might use identical tag names and values, potentially leading to unintended permissions if relied upon solely for access control. 

1.  **Use service control policies (SCPs):** [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) centrally control the maximum permissions for member accounts in your organization and can restrict root user permissions in member accounts. Consider using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html), which provides prescriptive managed controls alongside custom controls. 

1.  **Use resource control policies (RCPs):** [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) centrally restrict access to resources in member accounts, including access from principals outside your organization. RCPs complement SCPs by governing what any principal can do with your resources, not what your principals can do. AWS Control Tower includes managed RCPs that implement common resource protection patterns such as restricting public access to resources and enforcing encryption. 

1.  **Maintain a job role matrix:** Visualize roles and access levels across your AWS environment, and regularly review group and attribute structures to align with evolving organizational needs. 

1.  **Define groups and attributes in your identity provider:** Rely on a centralized identity provider for workforce, and define groups and attributes based on job role and scope of access required. Propagate groups and attributes from your IdP using SCIM or SAML 2.0. If you define roles within IAM Identity Center, [enable the attribute-based access control (ABAC) feature](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-abac.html) and define attributes that align with your organization's structure or resource tagging strategy. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP03 Employ a centralized identity provider](fnd02-bp03.md) 
+  [FND02-BP04 Establish controls to manage access based on lifecycle](fnd02-bp04.md) 
+  [FND02-BP06 Define permission guardrails for your organization](fnd02-bp06.md) 
+  [FND02-BP09 Establish a process to continually review and refine permissions](fnd02-bp09.md) 
+  [FND02-BP10 Establish workload and machine identity federation](fnd02-bp10.md) 

 **Related documents:** 
+  [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) 
+  [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) 
+  [IAM Access Analyzer findings - unused access, external access, and internal access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) 
+  [Refine unused access using IAM Access Analyzer recommendations](https://aws.amazon.com/blogs/security/refine-unused-access-using-iam-access-analyzer-recommendations/) 
+  [Strategies for achieving least privilege at scale – Part 1](https://aws.amazon.com/blogs/security/strategies-for-achieving-least-privilege-at-scale-part-1/) 
+  [Strategies for achieving least privilege at scale – Part 2](https://aws.amazon.com/blogs/security/strategies-for-achieving-least-privilege-at-scale-part-2/) 
+  [Refine permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html) 
+  [Policies and permissions in AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) 
+  [IAM policy testing with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) 
+  [Enable and configure attributes for access control in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-abac.html) 
+  [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - IAM policy best practices for security, access, and governance (SEC234)](https://www.youtube.com/watch?v=0fHpWfkaHzA) 
+  [AWS re:Invent 2023 - Navigating privileges: A journey through IAM policies (SEC230)](https://www.youtube.com/watch?v=RqrZm0xPfM4) 