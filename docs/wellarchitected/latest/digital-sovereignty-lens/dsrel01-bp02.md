# DSREL01-BP02 Develop mitigation plans for critical

risks

Proactive risk management is essential for maintaining business
continuity, regulatory adherence, and stakeholder trust. You need a
structured approach to manage critical risks. This assists in
reducing potential financial penalties, operational disruptions, and
reputational damage.

Your strategy should include robust mitigation plans. These plans
should demonstrate due diligence, protect sensitive data, and enable
effective incident response in cloud environments. With this
systematic approach to risk management, you can better safeguard
operations, adhere to regulatory requirements, and improve trust
with customers and stakeholders.

**Desired outcome:** Organizations
maintain prioritized, tested mitigation plans that enable rapid
response to critical risks while maintaining regulatory adherence.
Potential disruptions are reduced to acceptable levels through
actionable mitigation strategies. Business continuity and regulatory
adherence are sustained even during adverse events.

**Common anti-patterns:**

- Adopting a reactive approach that addresses risks only after
  incidents occur, missing opportunities for prevention.
- Operating in silos without cross-functional input, leading to
  fragmented risk ownership and uncoordinated mitigation efforts.
- Maintaining static, generic documentation that fails to reflect
  current AWS services or specific organizational risks.
- Conducting incomplete risk assessments that overlook critical
  areas such as compliance, operational risks, and third-party
  dependencies.
- Neglecting to validate mitigation strategies through regular
  testing, simulations, or tabletop exercises.
- Relying on manual processes and unclear communication protocols,
  hindering effective incident response and stakeholder
  notification.

**Benefits of establishing this best
practice:**

- Supports faster incident response and system recovery through
  pre-planned, documented mitigation strategies.
- Shows proactive risk management to auditors, regulators, and
  stakeholders. Supports adherence to frameworks like GDPR, HIPAA,
  and PCI-DSS.
- Enhances operational resilience and business continuity through
  improved system reliability and proactive risk management.
- Preserves institutional knowledge and ensures consistent
  response procedures regardless of personnel changes.
- Creates a culture of operational excellence through regular
  testing, updates, and continuous improvement.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Consider building mitigation plans by prioritizing high-risk items
in your risk register. Create a cross-functional team that
includes security, compliance, operations, and business
stakeholders. Use AWS tools and industry frameworks to identify,
prioritize, and design mitigations that align with AWS best
practices and regulatory requirements.

**Digital Sovereignty
considerations**: Include aspects related to data
residency, data privacy, and operator access restrictions when
designing your mitigation plans. Your recovery path must not
result in compliance violations.

### Implementation steps

Building a technical mitigation plan involves: understanding
your application components, their runtime characteristics, the
underlying fault isolation boundaries and their
inter-dependencies. Several AWS services support this process:

1. Use
   [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/") (Audit Manager) to discover potential
   reliability risks and mitigations. Audit Manager
   [common
   controls](https://aws.amazon.com/blogs/aws/simplify-risk-and-compliance-assessments-with-the-new-common-control-library-in-aws-audit-manager/ "https://aws.amazon.com/blogs/aws/simplify-risk-and-compliance-assessments-with-the-new-common-control-library-in-aws-audit-manager/") lists clear mitigation steps for commonly
   encountered high availability (HA) scenarios. A common
   control is a guideline that's not specific to one framework
   or AWS resource. Instead, it maps to domains such as HA and
   data protection.
2. Use
   [AWS Systems Manager Application Manager](../../../systems-manager/latest/userguide/application-manager.md "../../../systems-manager/latest/userguide/application-manager.md") and
   [resource
   groups](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md") to build a unified view of your applications
   and their underlying AWS resources.
3. Use
   [AWS Resilience Hub](../../../resilience-hub/latest/userguide/what-is.md "../../../resilience-hub/latest/userguide/what-is.md") to define your resilience goals,
   assess your resilience posture against those goals, and
   implement recommendations for improvement based on the AWS
   Well-Architected Framework.
4. Map service dependencies using
   [AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") and trace requests through distributed
   applications. Use X-Ray to discover how microservices and
   components interact at runtime, especially for serverless
   and containerized workloads.
5. Implement compliance and preventive controls. Use
   [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/") to set preventive, proactive and
   detective guardrails. When you enable a control in Control
   Tower, it also shows you the compliance framework that the
   control maps to.
6. Automate your recovery using
   [Systems
   Manager Automation runbooks](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md"),
   [Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md") for monitoring and troubleshooting AWS
   resources in communication applications, and
   [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") to run one-off recovery tasks.
7. Implement continuous improvement and effective reporting
   with
   [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/").

## Resources

**Related best practices:**

- [OPS01-BP04
  Evaluate compliance requirements](../operational-excellence-pillar/ops_priorities_compliance_reqs.md "../operational-excellence-pillar/ops_priorities_compliance_reqs.md")
- [SEC01-BP07
  Identify threats and prioritize mitigations using a threat
  model](../security-pillar/sec_securely_operate_threat_model.md "../security-pillar/sec_securely_operate_threat_model.md")
- [SEC10-BP02
  Develop incident management plans](../security-pillar/sec_incident_response_develop_management_plans.md "../security-pillar/sec_incident_response_develop_management_plans.md")
- [OPS07-BP05
  Make informed decisions to deploy systems and changes](../operational-excellence-pillar/ops_ready_to_support_informed_deploy_decisions.md "../operational-excellence-pillar/ops_ready_to_support_informed_deploy_decisions.md")

**Related documents:**

- [Compliance
  validation for AWS Cloud Map](../../../cloud-map/latest/dg/cloud-map-compliance.md "../../../cloud-map/latest/dg/cloud-map-compliance.md")
- [Use
  AWS Chatbot in Slack to remediate security findings from AWS Security Hub](https://aws.amazon.com/blogs/security/use-aws-chatbot-in-slack-to-remediate-security-findings-from-aws-security-hub/ "https://aws.amazon.com/blogs/security/use-aws-chatbot-in-slack-to-remediate-security-findings-from-aws-security-hub/")

**Related videos:**

- [AWS re:Inforce 2025 - Best practices for managing governance, risk
  and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE "https://www.youtube.com/watch?v=pCNIpnb9tvE")

**Related services:**

- [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [AWS Chatbot](https://aws.amazon.com/chatbot/ "https://aws.amazon.com/chatbot/")
- [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Resource Groups](https://aws.amazon.com/resource-groups/ "https://aws.amazon.com/resource-groups/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
