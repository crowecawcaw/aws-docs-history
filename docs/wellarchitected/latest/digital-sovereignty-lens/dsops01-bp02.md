

# DSOPS01-BP02 Enable distributed compliance execution
<a name="dsops01-bp02"></a>

 Effective compliance at scale requires distributing responsibilities across teams while maintaining centralized oversight and standards. Traditional centralized compliance models create bottlenecks that slow business velocity and limit an organization's ability to respond quickly to regulatory changes across jurisdictions. 

 **Desired outcome:** 
+  Teams inherit a common compliance baseline (for example, from a [central enabling team](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/oa.std.1-organize-teams-into-distinct-topology-types-to-optimize-the-value-stream.html)) but are empowered to independently address jurisdiction-specific regulatory requirements. 
+  Regional admin roles hold delegated authority to define, implement, and remediate local controls within guardrails set by the central team. 
+  Delegation boundaries are clearly defined so that teams know what they can decide locally and what requires central coordination. 

 **Common anti-patterns:** 
+  Compliance responsibilities are concentrated in a central team that becomes a bottleneck for every jurisdiction-specific decision. 
+  Teams receive delegated authority without corresponding guardrails, leading to inconsistent controls and compliance gaps across jurisdictions. 
+  Regional teams lack the permissions or tooling to remediate compliance findings independently, creating delays while they wait for central team action. 
+  Delegation is informal and undocumented, making it difficult to demonstrate accountability during audits. 

 **Benefits of establishing this best practice:** 
+  Faster response to jurisdiction-specific regulatory changes because regional teams can act independently within defined guardrails. 
+  Reduced compliance bottlenecks through distributed decision-making authority. 
+  Teams inherit common guardrails and can add or customize workload-specific and jurisdiction-specific controls. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Compliance delegation in a sovereignty context means transferring decision-making authority, not just assigning tasks. When a central team delegates to a regional team, that team gains authority to define, implement, and remediate controls within their jurisdictional scope without waiting for central approval. Task assignment without authority creates the same bottleneck as centralized compliance. Effective delegation transfers both the responsibility to act and the authority to decide, while retaining accountability at the governance level through guardrails and reporting. 

 Guardrails make this delegation structurally safe by enforcing boundaries and replacing approval workflows. This shifts the model from requiring permission before acting to acting decisively within enforced boundaries. Region-scoped delegation limits teams to their jurisdictional boundaries and grants jurisdiction-specific permissions. It also reduces the scope of impact from a misconfiguration. 

 Delegation maturity typically progresses through stages. Teams initially receive authority to remediate findings identified by centralized monitoring (reactive delegation). As they demonstrate competence, they gain authority to define and implement jurisdiction-specific controls within guardrails (proactive delegation). At the highest maturity level, regional teams contribute back to the shared control library, proposing controls for broader adoption. 

 [AWS Identity and Access Management (IAM) permission boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) define the maximum permissions a delegated role can hold, preventing privilege escalation regardless of identity-based policies attached. [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) enforce guardrails at the organizational unit level, restricting which Regions and services teams can operate in. Together, the OU structure and SCPs scope each team's operational authority to their jurisdictional boundaries. Where a service requires organization-wide administration (such as Security Hub CSPM aggregation or Config rule deployment), register a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_admin.html) account to manage that service across the organization without requiring management account access. 

 In practice, the model works like this. A regional team deploys a resource that doesn't meet a jurisdiction-specific requirement (for example, a missing data residency tag). An [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) rule detects the non-compliance and generates a finding that [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) aggregates and routes to the regional team. The team remediates using a pre-approved [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) runbook within their delegated authority, and the finding resolves without central team involvement. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define delegation boundaries and document them:** Define what decisions regional teams can make independently (for example, remediating findings, implementing jurisdiction-specific controls, managing data residency tags) and what requires escalation to the central team. Document these boundaries so that teams know their scope and auditors can verify accountability. Align boundaries with the progressive maturity stages described in the guidance: start with reactive delegation and expand authority as teams demonstrate competence. 

1.  **Configure guardrails and delegated permissions:** Deploy [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) at the organizational unit level to restrict teams to their jurisdictional Regions. Attach [IAM permission boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) to delegated roles to define maximum permissions. Where organization-wide service administration is needed, register member accounts as [delegated administrators](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_admin.html) for those services. 

1.  **Provision self-service remediation tooling:** Publish pre-approved [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) runbooks that teams can use to remediate common compliance findings without waiting for central team approval. Publish compliance playbooks with step-by-step guidance for jurisdiction-specific tasks such as adding controls, responding to data subject requests, and remediating Security Hub CSPM findings. Use [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to observe actual permission usage and progressively scope down delegated permissions from broad development access to least-privilege production access. 

1.  **Measure delegation effectiveness and expand authority:** Track the percentage of compliance findings remediated without central team escalation and mean time to remediation per team as indicators of delegation maturity. As teams demonstrate consistent remediation within guardrails, expand their authority to define and implement jurisdiction-specific controls. Refer to [Indicators for secure access and delegation](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/indicators-for-secure-access-and-delegation.html) for additional metrics. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS01-BP03 Implement compliance training and awareness](dsops01-bp03.html) 
+  [[OA.STD.1] Organize teams into distinct topology types to optimize the value stream](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/oa.std.1-organize-teams-into-distinct-topology-types-to-optimize-the-value-stream.html) 
+  [[AG.SAD.2] Delegate identity and access management responsibilities](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.2-delegate-identity-and-access-management-responsibilities.html) 
+  [OPS03-BP02 Team members are empowered to take action when outcomes are at risk](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_emp_take_action.html) 
+  [OPS03-BP03 Escalation is encouraged](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_escalation.html) 
+  [OPS03-BP04 Communications are timely, clear, and actionable](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_effective_comms.html) 
+  [OPS03-BP06 Team members are encouraged to maintain and grow their skill sets](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.html) 

 **Related documents:** 
+  [Two-Pizza Teams Are Just the Start, Part 1: Accountability and Empowerment Are Key to High-Performing Agile Organizations](https://aws.amazon.com/blogs/enterprise-strategy/two-pizza-teams-are-just-the-start-accountability-and-empowerment-are-key-to-high-performing-agile-organizations-part-1/) 
+  [Two-Pizza Teams Are Just the Start, Part 2: Accountability and Empowerment Are Key to High-Performing Agile Organizations](https://aws.amazon.com/blogs/enterprise-strategy/two-pizza-teams-are-just-the-start-accountability-and-empowerment-are-key-to-high-performing-agile-organizations-part-2/) 
+  [Compliance validation for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_compliance-validation.html) 
+  [Delegating responsibility to others using permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html#access_policies_boundaries-delegate) 
+  [Delegated administrator for IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-delegated-administrator.html) 

 **Related videos:** 
+  [AWS re:Inforce 2022 - Deep dive into compliance and auditing at scale (GRC402)](https://www.youtube.com/watch?v=w6_xOwFYlk8&t=307s) 

 **Related examples:** 
+  [When and where to use IAM permissions boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/) 
+  [Example permissions boundary](https://github.com/aws-samples/example-permissions-boundary) 

 **Related services:** 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 
+  [AWS IAM](https://aws.amazon.com/iam/) 
+  [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Config](https://aws.amazon.com/config/) 