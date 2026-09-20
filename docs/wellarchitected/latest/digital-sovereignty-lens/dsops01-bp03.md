

# DSOPS01-BP03 Implement compliance training and awareness
<a name="dsops01-bp03"></a>

 When teams operate across jurisdictions with delegated compliance responsibilities, they need targeted knowledge to make sound decisions within their scope. Generic security training doesn't prepare teams for the jurisdiction-specific decisions they face daily. 

 **Desired outcome:** 
+  Teams across jurisdictions can independently design, build, and maintain systems that meet both common and jurisdiction-specific compliance requirements. 
+  Team members understand the regulations that apply to their jurisdiction, the compliance tooling available to them, and the boundaries of their delegated authority. 

 **Common anti-patterns:** 
+  Training covers global compliance frameworks but not jurisdiction-specific regulatory differences that affect day-to-day architecture and operational decisions. 
+  Regional teams are trained on compliance tools but not on the boundaries of their delegated authority, leading to either overreach or inaction. 
+  Training content isn't updated when regulations change or when new jurisdictions are onboarded. 
+  Compliance knowledge is siloed within specialized teams rather than distributed to the developers and operators who build and run the systems. 
+  Training is measured by completion rates rather than by reduction in compliance gaps or time to remediate findings. 

 **Benefits of establishing this best practice:** 
+  Reduced need for late-stage remediation because teams address compliance requirements during design and development. 
+  Faster remediation of compliance findings because regional teams understand the tools and their delegated authority. 
+  Shorter audit cycles because teams can independently explain and demonstrate their compliance controls. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Digital sovereignty training differs from general compliance training because the knowledge required is jurisdiction-specific and subject to change from regulatory, geopolitical, and commercial forces acting simultaneously. Teams need to understand how data sovereignty concepts (localization, residency, access controls, and portability) apply in their operating jurisdiction, how regulations interact with architecture decisions (such as Region selection, replication boundaries, and operator access models), and how sovereignty controls can conflict with disaster recovery and operational support patterns. 

 Measuring training by completion rates creates a false sense of readiness. A team can complete every module and still make incorrect architecture decisions because sovereignty training is contextual. Measure instead by outcome: whether teams can independently detect and remediate sovereignty-related findings and explain their controls to auditors. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess knowledge gaps across sovereignty dimensions:** Survey teams in each jurisdiction to determine their current understanding of data sovereignty concepts (localization, residency, access controls, and portability), the applicable regulatory environment, relevant influencing factors, and continuity constraints. Identify knowledge gaps and map them to specific roles. 

1.  **Develop training content structured around sovereignty dimensions:** Create role-specific learning paths that cover data sovereignty concepts as they apply in each operating jurisdiction, the regulatory frameworks that govern them, the influencing factors that may cause requirements to change, and the continuity tensions that arise from sovereignty controls. Cover how architecture decisions (such as Region selection, encryption key management, replication boundaries, and operator access models) interact with these dimensions. Consider building searchable knowledge bases of jurisdiction-specific requirements using [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) so that teams can retrieve contextual answers at the point of decision. 

1.  **Integrate sovereignty validation into development workflows:** Include jurisdiction-specific checks in architecture reviews and code reviews, for example verifying data residency tags, confirming replication boundaries, or validating operator access configurations. Incorporate automated validation into Continuous Integration/Continuous Delivery (CI/CD) pipelines using [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) to enforce sovereignty rules in infrastructure templates before deployment. 

1.  **Establish update triggers for regulatory and influencing factor changes:** Define a process for reviewing and updating training content when regulations change, new jurisdictions are onboarded, or influencing factors shift (such as new trade agreements, updated regional sovereignty guidances, or vendor licensing changes). Assign accountability for monitoring these triggers. When something changes, communicate the update to affected teams with clear guidance on what changed and how it affects their operating jurisdiction. 

1.  **Measure training effectiveness against sovereignty outcomes:** Define success criteria tied to sovereignty compliance outcomes, not completion rates. Track metrics such as reduction in sovereignty-related findings from [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), improvement in mean time to remediate jurisdiction-specific gaps, and reduction in audit preparation time. Correlate trends with training delivery to identify content gaps and gather feedback from teams on training relevance across each sovereignty dimension. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS01-BP02 Enable distributed compliance execution](dsops01-bp02.html) 
+  [SEC11-BP01 Train for application security](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_train_for_application_security.html) 
+  [OPS03-BP06 Team members are encouraged to maintain and grow their skill sets](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.html) 
+  [OPS11-BP04 Perform knowledge management](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_knowledge_management.html) 

 **Related documents:** 
+  [AWS Cloud Adoption Framework: Security Perspective - Security assurance](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/security-assurance.html) 
+  [Safe and sound in the cloud: Your AWS security training guide](https://aws.amazon.com/blogs/training-and-certification/safe-and-sound-in-the-cloud-training/) 
+  [Building Security from the Ground up with Secure by Design](https://d1.awsstatic.com/partner-network/AWS-SANS-Secure-by-Design-Whitepaper-2024.pdf) 
+  [AWS Security Ramp-Up Guide](https://aws.amazon.com/blogs/security/updated-aws-ramp-up-guide-available-for-security-identity-and-compliance/) 
+  [AWS Compliance Resources](https://aws.amazon.com/compliance/resources/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Use new IAM Access Analyzer features on your journey to least privilege (SEC238)](https://www.youtube.com/watch?v=JpemUkU8INA) 

 **Related examples:** 
+  [AWS Threat Modeling Workshop](https://catalog.workshops.aws/threatmodel/en-US) 
+  [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/) 
+  [AWS Cloud Quest for Security](https://aws.amazon.com/training/digital/aws-cloud-quest/) 

 **Related tools:** 
+  [AWS Skill Builder](https://skillbuilder.aws/) 
+  [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) 
+  [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 