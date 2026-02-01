# DSOPS02-BP02 Establish an automated path to compliance

Establish an automated path to effectively meet cybersecurity
standards, data privacy legislation, and industry-specific
regulations like HIPAA and PCI-DSS. Automation reduces the risk of
human error, speeds up the compliance process, and allows for
continuous monitoring and adaptation to changing regulations.

**Desired outcome:** Compliance is
built into every change through automated validation, detection, and
remediation, enabling faster deployments and audit-ready
documentation.

**Common anti-patterns:**

- Relying on periodic manual audits and spreadsheet-based tracking
  instead of continuous automated monitoring.
- Performing compliance validation only during audit periods
  rather than continuously.
- Failing to use a centralized tool for compliance reporting
  resulting in blind spots.
- Generating compliance alerts without automated remediation or
  clear escalation procedures.

**Benefits of establishing this best
practice:**

- Reduce human error in compliance monitoring, detection,
  analysis, and remediation.
- Maintain real-time regulatory posture with automated evidence
  collection and reporting, enabling audit-ready responses and
  regulatory confidence.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To establish an automated path to compliance, codify your
compliance requirements into compliance as code (CaC) policies.
Integrate compliance validation into your CI/CD pipelines, and
build compliance in to every change.

The most important components of this strategy are:

1. Defining compliance policies as code
2. Unit testing and validating compliance policies
3. Integrating compliance policies with CI/CD pipelines
4. Creating automated remediation workflows to address common
   compliance violations
5. Regularly testing compliance as code policies through
   controlled violations and performing automated remediation
   actions in sandbox, development or test environments

### Implementation steps

AWS provides several capabilities required to establish a mature
compliance posture. Consider using the three lines of defense
model developed by
[Institute
of Internal Auditors (IIA)](https://na.theiia.org/Pages/IIAHome.aspx "https://na.theiia.org/Pages/IIAHome.aspx") to select and provision AWS
services that best fit your needs.

In the three lines model, the first-line function manages risk,
the second-line function oversees risk, and the third-line
function provides objective and independent assurance of risk
management. Aligning with this model, consider the following:

1. **First line: risk
   management:** Manage risks by applying
   [secure
   by design (SBD)](https://aws.amazon.com/blogs/security/new-whitepaper-available-building-security-from-the-ground-up-with-secure-by-design/ "https://aws.amazon.com/blogs/security/new-whitepaper-available-building-security-from-the-ground-up-with-secure-by-design/") principles, provisioning automated
   guardrails, and implementing automated remediations.
   - Start by defining compliance metrics (including
     deviations, thresholds, and risk tolerance levels)
     working together with your security consultants, data
     protection office, and workload owners. Metrics guide
     decisions on automation priorities and tool selection.
   - Apply a set of
     [controls](../../../prescriptive-guidance/latest/aws-security-controls/security-control-types.md "../../../prescriptive-guidance/latest/aws-security-controls/security-control-types.md")
     expressed as compliance as code and aligned to best
     practices and compliance frameworks. Examples include
     [AWS Foundational Security Best Practices](../../../securityhub/latest/userguide/fsbp-standard.md "../../../securityhub/latest/userguide/fsbp-standard.md") and
     [NIST
     SP 800-53 Rev. 5](../../../securityhub/latest/userguide/nist-standard.md "../../../securityhub/latest/userguide/nist-standard.md"). AWS Control Tower provides
     [700
     plus](../../../controltower/latest/controlreference/controls-reference.md "../../../controltower/latest/controlreference/controls-reference.md") preventative, proactive, and detective
     controls mapped to several
     [frameworks](../../../controltower/latest/controlreference/frameworks-supported.md "../../../controltower/latest/controlreference/frameworks-supported.md").
     When you enable Control Tower controls, it automatically
     starts enforcing compliance as code policies and also
     detects compliance drifts.
   - Adopt a multi-account strategy similar to the guidance
     provided in the
     [AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/security-tooling.md "../../../prescriptive-guidance/latest/security-reference-architecture/security-tooling.md"). With
     account-level isolation, you can better control the
     impact of potential compliance issues.
   - Provide pre-approved, compliance-aligned infrastructure
     templates (for example, VPCs or EC2 instances) to enable
     developers to provision standardized resources. Consider
     using
     [Service Catalog](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md") to enable provisioning,
     administration, and management of standardized AWS CloudFormation or Terraform Cloud products.
   - Reduce potential information exposure risks by applying
     principle of
     [least
     privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") and
     [just-in-time
     access](../../../singlesignon/latest/userguide/temporary-elevated-access.md "../../../singlesignon/latest/userguide/temporary-elevated-access.md").
   - Provide
     [automated
     runbooks](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md") to remediate compliance violations. The
     [AWS Systems Manager Automation Runbook Reference](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md")
     provides a catalog of runbooks. You can also create your
     [own
     runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md").

2. **Second line: risk
   oversight:** Aim to identify compliance drifts on a
   continuous basis and prioritize remediations based on
   calculated risk scores. Use
   [AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") or an equivalent Cloud Security
   Posture Management (CSPM) solution to gain continuous risk
   oversight.
   - Enable Security Hub CSPM to
     [accept
     findings](../../../securityhub/latest/userguide/securityhub-integration-enable.md "../../../securityhub/latest/userguide/securityhub-integration-enable.md") from AWS services and third-party
     providers.
   - Enable
     [consolidated
     controls view and consolidated controls findings](../../../securityhub/latest/userguide/asff-changes-consolidation.md "../../../securityhub/latest/userguide/asff-changes-consolidation.md")
     in Security Hub CSPM. This reduces findings noise by
     producing a single finding for a control, even if the
     control applies to multiple enabled standards.
   - Log API activity with
     [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") across accounts and store logs in a
     central S3 bucket. Log network flows, especially logs
     generated at the edge of the network. Require
     applications to log user actions. For example, user X
     changed document Y at time Z. When you log user actions
     (commands) and correlate them with system generated logs
     (for example firewall logs), you gain a holistic
     understanding of activity in your workload.
   - Enable encryption and log integrity validation. If you
     are using Amazon Security Lake as a long-term storage
     for your security and compliance logs, apply
     [these
     measures](../../../security-lake/latest/userguide/data-protection.md "../../../security-lake/latest/userguide/data-protection.md") to protect data. Consider enforcing the
     [write
     once read many (WORM)](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md") model when storing logs in
     S3 to protect chain of evidence.

3. **Third line: risk assessment and
   compliance reporting:** Aim to support continuous
   risk assessment of your entire environment by automatically
   collecting, aggregating, and analyzing logs.
   - Source logs audit logs, network flow logs, firewall logs
     and application. Example sources include:
     - Amazon CloudTrail
       [Data
       and Management Event Logs](../../../awscloudtrail/latest/userguide/cloudtrail-events.md "../../../awscloudtrail/latest/userguide/cloudtrail-events.md") for API activity
       tracking
     - [VPC
       Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") for network traffic analysis
     - [AWS WAF Logs](../../../waf/latest/developerguide/logging.md "../../../waf/latest/developerguide/logging.md") for web application firewall
       monitoring
     - [Amazon EKS Audit Logs](../../../eks/latest/best-practices/auditing-and-logging.md "../../../eks/latest/best-practices/auditing-and-logging.md") for Kubernetes cluster
       activity
     - [Route 53 resolver query logs](../../../Route53/latest/DeveloperGuide/resolver-query-logs.md "../../../Route53/latest/DeveloperGuide/resolver-query-logs.md") for DNS query
       monitoring
     - Application-specific logs collected through
       [Amazon CloudWatch](../../../cloudwatch.md "../../../cloudwatch.md") or another application performance
       monitoring (APM) tool

   - Consolidate logs using Amazon Security Lake, or an
     equivalent security-focused data lake to enable
     efficient querying and analysis across terabytes of log
     data. Security Lake normalizes log files to a single
     open format known as the
     [Open
     Cybersecurity Schema Framework (OCSF)](https://github.com/ocsf "https://github.com/ocsf"). This
     standardization allows you to connect Security Lake with
     your existing security information and event management
     (SIEM) tooling as well as
     [Amazon OpenSearch Service](https://aws.amazon.com/blogs/aws/introducing-amazon-opensearch-service-zero-etl-integration-for-amazon-security-lake/ "https://aws.amazon.com/blogs/aws/introducing-amazon-opensearch-service-zero-etl-integration-for-amazon-security-lake/").
   - Generate audit-ready reports on-demand with
     [AWS Audit Manager](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md"). Audit Manager streamlines
     compliance reporting by collecting evidence aligned with
     [several
     frameworks](../../../audit-manager/latest/userguide/framework-overviews.md "../../../audit-manager/latest/userguide/framework-overviews.md") such as NIST 800-53 Rev 5 and PCI DSS
     4.0. It ingests results from AWS Config managed rule
     evaluations, CloudTrail management event logs, findings
     from Security Hub and can also make AWS API calls to
     generate snapshots of your environment. Audit Manager
     can generate
     [assessment
     reports](../../../audit-manager/latest/userguide/generate-assessment-report.md "../../../audit-manager/latest/userguide/generate-assessment-report.md") based on assessments you create.
   - Log in into your AWS Management Console and use the
     [AWS Artifact](https://aws.amazon.com/artifact/ "https://aws.amazon.com/artifact/") service to access AWS security and
     compliance reports plus select online agreements. You
     can download AWS compliance reports like SOC, ISO, and
     PCI directly to demonstrate AWS infrastructure
     compliance to auditors.

## Resources

**Related best practices:**

- [OPS05-BP01
  Use version control](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_version_control.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_version_control.md")
- [OPS05-BP02
  Test and validate changes](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_test_val_chg.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_test_val_chg.md")
- [OPS05-BP03
  Use configuration management systems](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_conf_mgmt_sys.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_conf_mgmt_sys.md")
- [OPS05-BP04
  Use build and deployment management systems](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_build_mgmt_sys.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_build_mgmt_sys.md")
- [OPS05-BP05
  Perform patch management](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_patch_mgmt.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_patch_mgmt.md")
- [OPS05-BP06
  Share design standards](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_share_design_stds.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_share_design_stds.md")
- [OPS05-BP07
  Implement practices to improve code quality](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_code_quality.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_code_quality.md")
- [OPS05-BP08
  Use multiple environments](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_multi_env.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_multi_env.md")
- [OPS05-BP09
  Make frequent, small, reversible changes](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_freq_sm_rev_chg.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_freq_sm_rev_chg.md")
- [OPS05-BP10
  Fully automate integration and deployment](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_auto_integ_deploy.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_auto_integ_deploy.md")

**Related documents:**

- [Introduction
  to the Three Lines Model](https://internalauditor.theiia.org/en/video/2020/august/the-iias-new-three-lines-model-part-1-the-basics/ "https://internalauditor.theiia.org/en/video/2020/august/the-iias-new-three-lines-model-part-1-the-basics/")
- [Integrate
  across the Three Lines Model (Part 1)](https://aws.amazon.com/blogs/mt/integrate-across-the-three-lines-model-part-1-build-a-custom-automation-of-aws-audit-manager-with-aws-security-hub/ "https://aws.amazon.com/blogs/mt/integrate-across-the-three-lines-model-part-1-build-a-custom-automation-of-aws-audit-manager-with-aws-security-hub/")
- [Integrate
  across the Three Lines Model (Part 2)](https://aws.amazon.com/blogs/mt/integrate-across-the-three-lines-model-part-2-transform-aws-config-conformance-packs-into-aws-audit-manager-assessments/ "https://aws.amazon.com/blogs/mt/integrate-across-the-three-lines-model-part-2-transform-aws-config-conformance-packs-into-aws-audit-manager-assessments/")
- [Implementing
  a compliance and reporting strategy for NIST SP 800-53
  Rev. 5](https://aws.amazon.com/blogs/security/implementing-a-compliance-and-reporting-strategy-for-nist-sp-800-53-rev-5/ "https://aws.amazon.com/blogs/security/implementing-a-compliance-and-reporting-strategy-for-nist-sp-800-53-rev-5/")
- [Consolidating
  controls in Security Hub: The new controls view and
  consolidated findings](https://aws.amazon.com/blogs/security/consolidating-controls-in-security-hub-the-new-controls-view-and-consolidated-findings/ "https://aws.amazon.com/blogs/security/consolidating-controls-in-security-hub-the-new-controls-view-and-consolidated-findings/")

**Related videos:**

- [How
  to implement compliance at scale with the Three Lines of
  Defense model: AWS AMER Summit Aug 2021](https://www.youtube.com/watch?v=G5oQwykobNw "https://www.youtube.com/watch?v=G5oQwykobNw")
- [AWS re:Invent 2025 - From Reactive to Proactive: Infrastructure
  governance by design (COP352)](https://www.youtube.com/watch?v=iXor74El2D8 "https://www.youtube.com/watch?v=iXor74El2D8")
- [AWS re:Invent 2025 - From Code to Policies: Accelerate Development
  w/ IAM Policy Autopilot (SEC351)](https://www.youtube.com/watch?v=vgA_sq99Kas "https://www.youtube.com/watch?v=vgA_sq99Kas")

**Related services:**

- [AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
- [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
- [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md")
- [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md")
- [Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md")
- [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/")
- [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/ "https://aws.amazon.com/firewall-manager/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [Amazon
  Security Lake](../../../security-lake/latest/userguide/what-is-security-lake.md "../../../security-lake/latest/userguide/what-is-security-lake.md")
