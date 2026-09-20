

# DSSEC05-BP02 Empower regional teams
<a name="dssec05-bp02"></a>

 Regulatory requirements change on local timelines, and a central team can't track every jurisdiction's changes fast enough to keep regional workloads compliant. Regional teams that understand their local regulations can respond faster, but only if they have authority to act within boundaries that protect the organization's security baseline. The balance to strike is delegating enough autonomy to move quickly while keeping the controls that must stay consistent, such as security baselines and data residency, non-negotiable. 

 **Desired outcome:** 
+  Regional teams make decisions quickly and drive innovation within their jurisdictions while maintaining adherence to jurisdiction-specific regulatory requirements. 
+  Clear accountability structures and knowledge sharing mechanisms enable cross-region collaboration without compromising local compliance obligations. 
+  Operational bottlenecks are reduced through distributed decision-making authority. 

 **Common anti-patterns**: 
+  Maintaining excessive centralized control and creating delayed decision-making processes that block regional teams from responding to regional requirements. 
+  Lacking clear regional authority boundaries and proper governance frameworks, creating confusion about decision-making responsibilities. 
+  Implementing inconsistent compliance standards across regions with insufficient cross-region communication channels, resulting in knowledge silos and duplicated efforts. 
+  Failing to develop adequate local expertise and effective knowledge transfer mechanisms, creating dependencies on central resources. 

 **Benefits of establishing this best practice**: 
+  Faster response to jurisdiction-specific regulatory changes through local expertise and decision-making authority. 
+  Localized expertise and accountability structures support better regulatory adherence across jurisdictions. 
+  Reduced operational bottlenecks through distributed authority with better resource utilization and regional optimization. 
+  Efficient knowledge sharing and best practice distribution across regions enable cross-regional learning. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Establish a balanced governance model that delegates appropriate authority to regional teams while maintaining organizational consistency. Assess current centralization levels, define regional autonomy boundaries, and implement frameworks that enable local decision-making within global standards. Regional autonomy should not extend to weakening security controls. 

 Consider digital sovereignty requirements when establishing regional governance models. Verify regional teams operate within approved jurisdictional boundaries, implement location-specific compliance and regulatory frameworks, maintain data residency requirements through regional controls, and enable regional teams to respond to jurisdiction-specific regulatory changes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish governance boundaries:** Define global security baselines that regional teams can't override, and delegate regional authority within those boundaries. For detailed guidance on SCPs, Region deny controls, and OU structure, see [DSSEC07-BP01 Enhance your digital sovereignty governance posture](dssec07-bp01.html). 

1.  **Configure regional access and compliance controls:** Set up region-specific IAM roles, regional compliance monitoring, and regional KMS keys. For data access controls and data perimeters, see [DSSEC02-BP01 Protect data through layered access controls within sovereign boundaries](dssec02-bp01.html). For AWS Control Tower digital sovereignty controls, see DSSEC07-BP01. 

1.  **Deploy regional operations capabilities:** Create regional operations playbooks using [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html). Set up local monitoring with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and regional incident response using [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html). Enable regional teams to operate independently within the governance boundaries established in Step 1. 

1.  **Enable knowledge sharing:** 
   +  Create a central documentation repository for compliance patterns, architecture decisions, and lessons learned. 
   +  Establish cross-region communities of practice where teams share solutions to common regulatory challenges. 
   +  Maintain a shared library of reusable compliance artifacts such as [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html), [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) rules, and [AWS Config conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) that regional teams can adapt to local requirements. 
   +  Run regular cross-region reviews where teams present how they addressed jurisdiction-specific challenges, creating a feedback loop that benefits the entire organization. 

1.  **Develop regional expertise:** Improve local cloud and compliance expertise using resources like [AWS Skill Builder](https://skillbuilder.aws/) and [AWS Training and Certification](https://aws.amazon.com/training/). Establish knowledge-sharing mechanisms between central and regional teams to transfer institutional knowledge while building local self-sufficiency. 

## Resources
<a name="resources"></a>

 **Related best practices**: 
+  [SEC02-BP01 Use strong sign-in mechanisms](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_enforce_mechanisms.html) 
+  [SEC02-BP04 Rely on a centralized identity provider](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_identity_provider.html) 
+  [SEC03-BP01 Define access requirements](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define.html) 
+  [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) 
+  [SEC03-BP08 Share resources securely within your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_securely.html) 
+  [SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html) 
+  [SEC04-BP02 Capture logs, findings, and metrics in standardized locations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_logs.html) 
+  [OPS01-BP03 Evaluate governance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.html) 
+  [OPS02-BP01 Resources have identified owners](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_resource_owners.html) 
+  [OPS02-BP02 Processes and procedures have identified owners](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_proc_owners.html) 
+  [OPS11-BP04 Perform knowledge management](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_knowledge_management.html) 

 **Related documents**: 
+  [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) 
+  [AWS Identity and Access Management Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) 

 **Related videos**: 
+  [AWS re:Invent 2024 - New governance capabilities for multi-account environments (COP378-NEW)](https://www.youtube.com/watch?v=Zw8iRP0v0zA) 

 **Related services**: 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 
+  [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) 
+  [Service Catalog](https://aws.amazon.com/servicecatalog/) 
+  [AWS Resource Access Manager (RAM)](https://aws.amazon.com/ram/) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS Artifact](https://aws.amazon.com/artifact/) 