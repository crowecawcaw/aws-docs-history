

# FND02-BP04 Establish controls to manage access based on lifecycle

 Monitor and adjust the permissions you grant to principals (users, roles, and groups) as their relationship with your organization changes. Update group memberships as people change roles, and remove access when someone leaves the organization. 

 **Desired outcome:** 
+  You monitor and adjust permissions throughout the lifecycle of principals within the organization, reducing risk of unnecessary privileges. 
+  You grant appropriate access when you create a user and modify access as the user's responsibilities change. 
+  You remove access when the user is no longer active or has left the organization. 
+  You centrally manage changes to your users, roles, and groups. 
+  You use automation to propagate changes to your AWS environments. 

 **Common anti-patterns:** 
+  Granting excessive or broad access privileges to identities upfront, beyond what is initially required. 
+  Not reviewing and adjusting access privileges as identities' roles and responsibilities change over time. 
+  Leaving inactive or terminated identities with active access privileges, increasing the risk of unauthorized access. 
+  Not using automation to manage the lifecycle of identities. 
+  Relying on manual processes to synchronize identity changes between authoritative sources and AWS environments. 

 **Benefits of establishing this best practice:** 
+  Reduced security risk from privilege creep and orphaned accounts that could be misused by unauthorized parties. 
+  Improved compliance posture with accurate records of who has access to what resources and when those permissions change. 
+  Operational efficiency through automated synchronization with identity providers, reducing administrative overhead and human error during onboarding and offboarding. 
+  Faster role transitions as users move within the organization, with quicker access adjustments that reduce disruption to productivity. 
+  Smaller attack surface because users hold only the permissions necessary for their current role at any given time. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Access privileges must reflect an identity's current relationship with your organization. That relationship progresses through onboarding, role or responsibility changes, and offboarding. Onboarding risks granting excessive privileges that violate least privilege principles. Role changes accumulate unnecessary permissions when old access is not removed. Offboarding creates the highest security risk when accounts remain active after termination. Adherence to the principle of least privilege at every phase reduces the risk of excessive or unnecessary access privileges. 

 Manage this lifecycle through automated synchronization between your authoritative identity source and your AWS environment. When you manage workforce identities through a centralized identity provider, you create a single source of truth. Changes in your identity provider propagate to AWS automatically, removing manual, error-prone processes for maintaining parallel identity stores. IAM Identity Center supports this synchronization through the [System for Cross-domain Identity Management](https://docs.aws.amazon.com/singlesignon/latest/developerguide/what-is-scim.html) (SCIM) protocol, an open standard for automated identity provisioning and deprovisioning. 

 Separate identity information from authorization logic. Your identity provider maintains the authoritative record of who exists and which groups they belong to. IAM Identity Center receives this information through SCIM synchronization and stores it in its Identity Store. Authorization is managed through [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) that represent job functions rather than individual users. When a user's role changes, you update their group membership in the identity provider, SCIM automatically synchronizes that change to IAM Identity Center, and the appropriate permission sets take effect across all relevant accounts. 

 IAM users created directly within AWS accounts lack the centralized identity source that supports automated synchronization. Their lifecycle must be managed through explicit IAM API calls or console actions within each account, which increases administrative burden and the likelihood of inconsistent access. For organizations using direct IAM users, migrating to IAM Identity Center is preferred. Where migration is not immediately feasible, use strict processes for creating, modifying, and deleting IAM users, combined with preventive controls such as SCPs that restrict IAM user management operations, to limit drift and inconsistency. 

 Effective lifecycle management requires organizational processes that define when and how access changes. These processes must account for trigger events such as a new hire completing onboarding, a promotion or transfer, an extended leave of absence, or termination. Each trigger must initiate a workflow that updates the identity provider, verifies the change synchronized to IAM Identity Center, validates the new permission set assignments, and confirms that old permissions were removed. 

 Measure your lifecycle management maturity by the degree of automation and the latency between identity changes and AWS access updates. Less mature organizations process access requests manually through ticketing systems, with delays of hours or days. Mature organizations achieve near-real-time synchronization, where a role change in the identity provider automatically triggers permission updates in AWS within minutes. This maturity requires technical implementation, organizational alignment on access policies, well-defined permission sets that map to job functions, and regular reviews to verify that identity and permission information remain accurate. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define an access management lifecycle process:** Document procedures for granting initial access, periodic reviews, and offboarding. Specify trigger events (new hire, role change, termination), responsible parties for each action, expected timelines, and escalation procedures. Socialize the process with HR, security, and IT teams to confirm alignment and clear handoffs. 

1.  **Implement IAM roles, groups, and permissions boundaries:** Use [IAM roles, groups, and permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) to manage access collectively and enforce maximum permissible access levels. For IAM Identity Center, define groups in your identity provider that align with job functions. For direct IAM users, use IAM groups for common roles and permissions boundaries to cap the permissions any individual user can be granted. 

1.  **Integrate with a federated identity provider:** Connect a [federated identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) (such as Microsoft Entra ID, Okta, or Ping Identity) as the authoritative source for user and group information, either through IAM Identity Center or directly to individual accounts. If your organization has no external identity provider, you can use the IAM Identity Center built-in identity store, though this limits your ability to maintain a single identity source across all systems. 

1.  **Configure SCIM synchronization:** Use the [SCIM](https://docs.aws.amazon.com/singlesignon/latest/developerguide/what-is-scim.html) protocol to synchronize user and group information from the identity provider into IAM Identity Center's Identity Store. Configure SCIM to synchronize both user attributes and group memberships, because group memberships drive permission set assignments. 

1.  **Create permission sets for job roles:** Create [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) that represent distinct job functions (developers, security auditors, network administrators) rather than individual users. Each permission set must grant only the permissions necessary for that role. Assign permission sets to groups rather than individual users to simplify lifecycle management. 

1.  **Establish access request and approval workflows:** Define who can approve each type of access and how quickly approvals must be processed. Require additional approval levels for sensitive or administrative permissions. Use your identity provider's native workflow capabilities or integrate with ticketing systems to track approvals. Document the workflows so requesters can obtain access through approved channels rather than workarounds that bypass controls. 

1.  **Implement regular access reviews:** Establish a cadence for reviewing whether current assignments remain appropriate. Use [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to identify unused permissions and over-provisioned roles. Schedule quarterly or semi-annual reviews where managers verify that their team members' access aligns with current responsibilities. Automate the collection of access information to make reviews efficient. Document a remediation process for removing access identified as unnecessary. 

1.  **Configure automated offboarding:** Implement mechanisms that automatically remove AWS access when users leave or become inactive. If your identity provider integrates with your HR system, use that integration to trigger SCIM deprovisioning when employment status changes. Otherwise, establish a notification process so IT security immediately disables or deletes departed users in the identity provider. For direct IAM users, establish a process to remove those users across all accounts they had access to. Consider using SCPs to enforce centralized control over IAM user management. 

1.  **Monitor and audit lifecycle events:** Enable logging of all identity lifecycle events to verify that access changes occur as expected. Configure [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to log IAM Identity Center administrative events. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to alert on high-risk events such as new administrative permission assignments or changes to SCIM configuration. 

1.  **Provide training and awareness:** Educate employees on access management best practices and their responsibilities in the lifecycle process, including how to request access, what to expect during onboarding, and the obligation to report role changes. Train managers on access reviews and the importance of prompt termination notifications. Provide regular refreshers as processes evolve or audit findings reveal gaps. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP03 Employ a centralized identity provider](fnd02-bp03.md) 
+  [FND02-BP05 Grant least privilege access](fnd02-bp05.md) 
+  [FND02-BP09 Establish a process to continually review and refine permissions](fnd02-bp09.md) 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 

 **Related documents:** 
+  [Manage your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html) 
+  [Manage identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html) 
+  [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 
+  [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) 

 **Related videos:** 
+  [AWS re:Inforce 2023 - Manage temporary elevated access with IAM Identity Center (IAM323)](https://www.youtube.com/watch?v=a1Na2G7TTQ0) 
+  [AWS re:Inforce 2024 - Securing human access to AWS at scale](https://www.youtube.com/watch?v=N82s9TF_b9w) 