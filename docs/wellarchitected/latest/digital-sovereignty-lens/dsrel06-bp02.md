# DSREL06-BP02 Maintain sovereign regulatory adherence during

failure states

For highly regulated organizations, maintaining data sovereignty and
regulatory adherence during system failures is a business-critical
requirement. Organizations must verify that their automated failover
mechanisms and disaster recovery procedures respect jurisdictional
boundaries and compliance mandates. Failures in maintaining
sovereign regulatory adherence during outages can result in
financial penalties, loss of operating licenses, and damaged
customer trust.

**Desired outcome:** Organizations
maintain resilient architectures with automated safeguards and
validated recovery processes. Data sovereignty requirements and
regulatory adherence are preserved across each failure scenario.
Business operations continue from single component failures to
regional disasters without compliance violations.

**Common anti-patterns:**

- Automatically failing over to non-compliant regions and allowing
  data replication across unauthorized jurisdictions without
  regulatory validation.
- Missing real-time compliance monitoring during incidents and
  relying on manual checks instead of automated enforcement.
- Treating data uniformly during recovery without proper
  classification and storing unencrypted backups in non-compliant
  regions.
- Insufficient testing of compliance controls during failure
  scenarios and inadequate documentation of compliance-related
  decisions.
- Delayed regulatory notifications and incomplete audit trails
  during emergency situations.

**Benefits of establishing this best
practice:**

- Reduces exposure to violations and associated penalties while
  maintaining regulatory standing through automated validation.
- Supports rapid business continuity with automated compliance
  checks while adhering to data residency laws.
- Maintains comprehensive audit trails and documented controls
  during emergency situations, simplifying audit processes.
- Demonstrates compliance reliability to regulators and customers
  while avoiding expensive penalties and business disruption
  costs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Organizations should implement a defense in depth approach to
sovereign regulatory adherence during failure states by designing
disaster recovery architectures that respect regulatory
boundaries. Use AWS services for compliance monitoring, data
residency enforcement, and automated recovery.

Design multi-Region resilient workloads with automated compliance
validation while maintaining detailed audit trails throughout each
scenario.

- Design multi-layered compliance validation that operates
  independently across approved AWS Regions
- Implement automated compliance checks and validation within
  disaster recovery procedures using IaC
- Configure region-specific encryption and key management for
  data protection at rest and in transit
- Establish Prescriptive escalation procedures and comprehensive
  testing frameworks that validate both technical and compliance
  aspects of recovery
- Create detailed audit trails and monitoring systems that
  maintain compliance visibility during emergencies

### Implementation steps

1. Deploy and configure monitoring to support improved
   governance and compliance across multiple Regions,
   maintaining sovereign regulatory adherence during failure
   states. Use
   [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md"),
   [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"),
   [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md"), and
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") for an AWS setup.
2. Create automation templates with
   [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md"), then implement
   [AWS CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md"). Next define
   [AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") automation runbooks. Set up
   [AWS Lambda](../../../lambda/latest/dg/lambda-security.md "../../../lambda/latest/dg/lambda-security.md") functions for compliance testing to automate
   the validation of compliance requirements across regions.
3. Deploy multi-Region keys using
   [AWS Key Management Service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") and configure
   [AWS CloudHSM](../../../cloudhsm/latest/userguide/introduction.md "../../../cloudhsm/latest/userguide/introduction.md") clusters. Implement TLS using
   [AWS Certificate Manager](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md") and set up
   [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") for credentials to protect data and
   maintain adherence during failure states.
4. Create fault injection simulations using
   [AWS Fault Injection Service](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md") experiments and implement
   regular failover testing schedules. Configure automated
   recovery validation checks and deploy
   [AWS Audit Manager](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md") assessments to validate technical and
   compliance controls, ensuring readiness for failure
   scenarios.

## Resources

**Related best practices:**

- [REL 13. How do you plan for disaster recovery (DR)?](../reliability-pillar/plan-for-disaster-recovery-dr.md "../reliability-pillar/plan-for-disaster-recovery-dr.md")
- [SEC 9. How do you protect your data in transit?](../security-pillar/protecting-data-in-transit.md "../security-pillar/protecting-data-in-transit.md")

**Related documents:**

- [Securing
  and automating compliance in the public sector with AWS](https://aws.amazon.com/blogs/publicsector/securing-and-automating-compliance-in-the-public-sector-with-aws/ "https://aws.amazon.com/blogs/publicsector/securing-and-automating-compliance-in-the-public-sector-with-aws/")
- [Automate
  continuous compliance at scale in AWS](https://aws.amazon.com/blogs/mt/automate-cloud-foundational-services-for-compliance-in-aws/ "https://aws.amazon.com/blogs/mt/automate-cloud-foundational-services-for-compliance-in-aws/")
- [Unlock
  the Power of AWS Config: Centralized Compliance and Resource
  Management](https://aws.amazon.com/blogs/mt/unlock-the-power-of-aws-config-centralized-compliance-and-resource-management/ "https://aws.amazon.com/blogs/mt/unlock-the-power-of-aws-config-centralized-compliance-and-resource-management/")

**Related videos:**

- [AWS re:Invent 2024 - How to maintain and automate compliance on
  AWS (SEC319)](https://www.youtube.com/watch?v=o93VHX4V7jY "https://www.youtube.com/watch?v=o93VHX4V7jY")
- [HDI
  Group's Innovative Approach: Automated Security and Compliance
  Remediation Using AWS Cloud Native Services](https://aws.amazon.com/awstv/watch/01c18611ed1/ "https://aws.amazon.com/awstv/watch/01c18611ed1/")

**Related services:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS Fault Injection Service](https://aws.amazon.com/fis/ "https://aws.amazon.com/fis/")
- [AWS Key Management Service](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
