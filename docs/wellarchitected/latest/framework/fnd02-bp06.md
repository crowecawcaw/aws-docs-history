

# FND02-BP06 Define permission guardrails for your organization

 Use permission guardrails to reduce the scope of permissions that can be granted to principals. During authorization, the permission evaluation chain applies your guardrails to determine a principal's *effective permissions*. Define guardrails using a layer-based approach. Apply some broadly across your organization, and others to specific accounts or temporary sessions. 

 **Desired outcome:** 
+  You have clear isolation of environments using separate AWS accounts. 
+  You have organization-wide permission guardrails in place through service control policies (SCPs) and resource control policies (RCPs), with broader guardrails closer to the organization root and stricter guardrails closer to individual accounts. 
+  You apply least privilege through resource policies that grant only the conditions and actions principals need to access a resource. 
+  You have permissions boundaries on principals that manage workload permissions, so permission management can be delegated to individual workload owners without risk of privilege escalation. 

 **Common anti-patterns:** 
+  Creating member AWS accounts within an [AWS Organization](https://aws.amazon.com/organizations/), but not using SCPs to restrict the use and permissions available to their root credentials. 
+  Assigning permissions based on least privilege, but not placing guardrails on the maximum set of permissions that can be granted. 
+  Relying on the *implicit deny* foundation of AWS IAM to restrict permissions, trusting that policies will not grant an undesired *explicit allow* permission. 
+  Running multiple workload environments in the same AWS account, and then relying on mechanisms such as VPCs, tags, or resource policies to enforce permission boundaries. 

 **Benefits of establishing this best practice:** 
+  Defense-in-depth protection through multiple layers of permission controls that prevent undesired permissions from being granted, even when individual policies are misconfigured or overly permissive. 
+  Reduced security risk by limiting the scope of impact from exposed credentials, policy errors, or insider threats through organization-wide permission boundaries that cannot be circumvented by individual account administrators. 
+  Simplified permission management at scale through a reduced maximum scope of permissions teams need to consider, so workload teams can manage their own permissions within defined guardrails without central approval for every change. 
+  Stronger compliance and audit posture through clear, enforceable organizational policies that demonstrate governance controls are in place across all accounts and workloads. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A layer-based approach to permission guardrails systematically reduces the maximum set of possible permissions as each layer is applied. This strategy addresses a core challenge in cloud environments, where organizations scale, the risk of policy misconfiguration increases, and the potential impact of overly permissive policies grows. Permission guardrails help to contain the scope of impact when individual policies fail to implement least privilege correctly. 

 The foundation is account-level isolation. Principals in one account cannot access resources in another account without explicit permission, even for accounts in the same AWS Organization or [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html). OUs group accounts you administer as a single unit. The account boundary holds even when policies inside an account are misconfigured. 

 Organization-wide controls build on this foundation. [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) provide principal-centric governance that limits what identities within your organization can do, regardless of what identity policies grant. Use SCPs to enforce common access controls, such as restricting access to specific AWS Regions, preventing resource deletion, or disabling risky service actions. SCPs applied to the organization root affect member accounts but not the management account. SCPs govern only principals within your organization, not external principals accessing your resources. 

 [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) complement SCPs by providing resource-centric protection. Although SCPs limit what your principals can do, RCPs govern what any principal (including those external to your organization) can do with your resources. Shared resources such as Amazon S3 buckets and AWS KMS keys often use resource policies to grant cross-account access. Use RCPs to keep those external principals subject to your organization's protection policies and as a boundary for resource access when resource policies grant unintended access to external principals. 

 If you are using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), its [controls](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) and [landing zones](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html) provide the foundation for your permission guardrails and multi-account environment. The landing zone provides a pre-configured, secure baseline with separate accounts for different workloads. Controls enforce security, operations, and compliance through a combination of SCPs, RCPs, declarative policies, and AWS Config rules. Controls come in three kinds (preventive, detective, and proactive) and three categories (mandatory, strongly recommended, and elective). [Drift detection](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html) alerts you when governed accounts or OUs deviate from the landing zone baseline. A Controls-Only experience supports adopting managed controls without a full landing zone deployment. A lightweight ConfigBaseline provides detective controls without requiring the full AWSControlTowerBaseline. When using AWS Control Tower guardrails alongside custom Organization SCPs, follow [AWS Control Tower guidance for AWS Organizations](https://docs.aws.amazon.com/controltower/latest/userguide/orgs-guidance.html) to avoid conflicts. 

 Resource policies provide more granular access control. [IAM resource policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based) are grant-based. They define which principals can access a specific resource, under what conditions, and which actions they can take. Policies can be broad, permitting all actions from principals in your organization using the PrincipalOrgId [condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html). They can also be narrow, permitting only specific actions by a specific IAM role. Similar conditions apply in IAM role trust policies. Within the same account, a resource or role trust policy that names a principal grants access on its own, without a matching identity policy. Cross-account access always requires both a resource policy and an identity policy grant. Use RCPs (rather than resource policies) to enforce coarse-grained, resource-centric guardrails such as PrincipalOrgId across your organization. For services that don't support RCPs, enforce security invariants through resource policies. 

 To delegate permission management to workload teams safely, use [IAM permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html). They define the maximum permissions an IAM role can have, regardless of the identity policies attached. Attach a boundary to any IAM role that workload teams use to create other IAM roles. Teams can then manage their own permissions without granting themselves privileges beyond the boundary. 

 For elevated access, privileged access management (PAM) techniques such as [MFA-protected API access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) require MFA authentication before sensitive actions. Temporary elevated access management (TEAM) extends this with time-limited permission grants approved through a workflow and automatically revoked after a defined window. TEAM solutions temporarily add principals to role trust policies or apply [session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) that narrow permissions during approved timeframes. Session policies can only further restrict permissions, never expand them beyond what the role's identity-based policies already allow. For validated TEAM solutions, see [Temporary elevated access](https://docs.aws.amazon.com/singlesignon/latest/userguide/temporary-elevated-access.html). 

 The permission evaluation chain combines all these layers (account boundaries, SCPs, RCPs, resource policies, identity policies, permissions boundaries, and session policies) to calculate effective permissions. SCPs, RCPs, permissions boundaries, and session policies act as guardrails. They can only reduce the permissions that identity and resource policies grant, never expand them. Cross-account access requires both an identity-based grant and a resource-based grant. This layered model is what makes the approach effective: even if one policy is misconfigured, the surrounding guardrails continue to enforce boundaries. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Isolate workloads and environments into separate AWS accounts:** Establish account-level boundaries as the first layer of permission guardrails. Create separate accounts for each workload, environment, and administrative function. Use [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to manage accounts centrally and group them into [organizational units (OUs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) that reflect your organizational structure. 

1.  **Implement service control policies (SCPs):** Use SCPs to reduce the maximum set of permissions that can be granted to principals within member accounts. Attach SCPs at the OU level rather than to individual accounts so policies apply consistently as accounts move between OUs. Choose between an *allow list* or *deny list* approach based on your organization's requirements. The allow list strategy explicitly specifies allowed access and implicitly blocks all others, and the deny list strategy explicitly specifies what isn't allowed and allows all other access by default. Pair SCPs with [centralized root access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) so member accounts have no persistent root credentials, and add an SCP that denies all root actions except the specific [root-only tasks](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) your environment actually requires. For more detail, see [Strategy for using SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_evaluation.html#strategy_using_scps) and [service control policy examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html). 

1.  **Implement resource control policies (RCPs):** Use [RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) to centrally restrict access to resources in your member accounts, including access from principals external to your organization. Review [RCP examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_examples.html) for patterns such as requiring encryption for data at rest or restricting public access to resources. 

1.  **Configure resource policies and RCPs with organizational boundaries:** Apply [IAM resource policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based) to grant access to critical resources such as Amazon S3 buckets, AWS KMS keys, and AWS Lambda functions, and use conditions in IAM role trust policies to restrict who can assume roles. Use the aws:PrincipalOrgId [condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in [RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) to enforce the organization boundary as a guardrail across all supported resources, rather than relying on individual resource policies to carry the condition. Define granular conditions that principals must meet, such as requiring MFA or originating from specific IP ranges. 

1.  **Assign IAM permissions boundaries for delegated administration:** Create [IAM permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) that cap the maximum permissions workload teams can grant when creating and managing IAM roles. Configure the boundary to require that any IAM roles the team creates also have the same boundary attached, preventing privilege escalation. 

1.  **Evaluate privileged access management (PAM) solutions:** For operations requiring elevated privileges, implement [MFA-protected API access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) to require multi-factor authentication before privileged actions. Configure IAM policies with the aws:MultiFactorAuthPresent condition key to enforce MFA for sensitive operations. 

1.  **Evaluate temporary elevated access management (TEAM) solutions:** For time-limited elevated access, review [temporary elevated access](https://docs.aws.amazon.com/singlesignon/latest/userguide/temporary-elevated-access.html) guidance and consider solutions like the [IAM Identity Center TEAM sample](https://aws-samples.github.io/iam-identity-center-team/) or [validated AWS Security Partners](https://docs.aws.amazon.com/singlesignon/latest/userguide/temporary-elevated-access.html#validatedpartners). 

1.  **Establish a review and refinement cycle:** Use [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to identify resources shared externally and verify alignment with intended access patterns. Review [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) logs to identify denied actions that indicate either legitimate needs for broader guardrails or attempts to circumvent restrictions. Refine guardrails based on organizational changes, new service releases, and evolving threats. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP05 Grant least privilege access](fnd02-bp05.md) 
+  [FND02-BP07 Implement data perimeter controls to help prevent unintended access](fnd02-bp07.md) 
+  [FND01-BP01 Establish management account and organizational structure](fnd01-bp01.md) 
+  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md) 

 **Related documents:** 
+  [Data perimeters on AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/) 
+  [Establish permissions guardrails using data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html) 
+  [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) 
+  [AWS Control Tower guidance for AWS Organizations](https://docs.aws.amazon.com/controltower/latest/userguide/orgs-guidance.html) 
+  [Strategy for using SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_evaluation.html#strategy_using_scps) 

 **Related examples:** 
+  [Service control policy examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html) 
+  [Resource control policy examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_examples.html) 

 **Related tools:** 
+  [Temporary elevated access management (TEAM)](https://aws-samples.github.io/iam-identity-center-team/) 
+  [Validated AWS Security Partners for temporary elevated access](https://docs.aws.amazon.com/singlesignon/latest/userguide/temporary-elevated-access.html#validatedpartners) 

 **Related services:** 
+  [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 