# DSOPS02-BP03 Develop and track key compliance metrics

In highly regulated industries, developing and tracking compliance
metrics is critical for demonstrating adherence to required
standards.

**Desired outcome:** Teams use
automated compliance metrics to reduce risk, accelerate remediation,
and improve overall regulatory posture.

**Common anti-patterns:**

- Limiting compliance metrics visibility to a small group instead
  of sharing with relevant stakeholders and decision makers.
- Collecting and reporting compliance metrics manually instead of
  through automation.
- Treating compliance metrics as informational only rather than
  using them to improve compliance posture or reduce risks.

**Benefits of establishing this best
practice:**

- Improved regulatory posture through data-driven decisions.
- Enhanced stakeholder confidence through transparent compliance
  reporting.
- Improved resource allocation based on data-driven compliance
  insights.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Developing and tracking compliance metrics requires a strategic
approach that aligns with your organizational risk profile and
regulatory requirements. Start by identifying a set of operational
and business metrics. Categorize metrics by facets such as AWS account IDs, Regions, resource types (for example, EC2, S3, and
Lambda), severity, owner, tags (for example, cost center or
business unit), and security standards. The following are example
metrics. Metrics and targets listed here are just for illustration
and neither exhaustive nor accurate.

| Category    | Metric                                          | Target                             | Actual |
| ----------- | ----------------------------------------------- | ---------------------------------- | ------ |
| Operational | Critical findings open for more than 24 hours   | 0                                  |        |
| Operational | High findings open for more than 7 days         | 0                                  |        |
| Operational | Mean time to remediation for Critical Findings  | <24 Hours                          |        |
| Business    | Audit preparation time                          | 50% reduction year over year (YoY) |        |
| Business    | Cost of compliance per workload                 | 5% reduction year over year (YoY)  |        |
| Business    | Time to attain full compliance for new services | Target <7 days                     |        |

### Implementation steps

The following steps provide instructions to activate AWS Security Hub CSPM and set up operational metrics within Security Hub. Refer to the equivalent documentation provided by the
vendor if you use a different Cloud Security Posture Management
(CSPM) tool.

1. **Enable AWS Security Hub CSPM and
   integrate compliance standards:**
   - Enable Security Hub in your AWS accounts:

   ```

   AWS securityhub enable-security-hub --region <your-region>

   ```

   - Enable compliance standards (for example, CIS, PCI-DSS,
     and HIPAA) in Security Hub:

   ```

   AWS securityhub enable-import-findings-for-product --product-arn arn:aws:securityhub:<region>::product/aws/securityhub --region <your-region>
   AWS securityhub batch-enable-standards --standards-subscription-requests StandardsArn="arn:aws:securityhub:::standards/cis-aws-foundations-benchmark/v/1.4.0" --region <your-region>

   ```

2. **Set up operational
   metrics**: The following implementation steps use
   AWS Security Hub. With Security Hub you can create
   [custom
   insights](../../../securityhub/latest/userguide/securityhub-custom-insight-create-api.md "../../../securityhub/latest/userguide/securityhub-custom-insight-create-api.md") to collect a specific set of findings and
   track issues that are unique to your environment. To get the
   number of open findings at a critical severity level for the
   last 30 days, follow these steps:
   - Create a custom insight using the AWS CLI:

   ```

   AWS securityhub create-insight --region <your-region> \
     --name "CriticalFindingsOver30Days" \
     --filters '{"SeverityLabel": [{"Value": "CRITICAL", "Comparison": "EQUALS"}], "RecordState": [{"Value": "ACTIVE", "Comparison": "EQUALS"}],"WorkflowStatus": [{"Value": "NEW", "Comparison": "EQUALS"}], "CreatedAt": [{"DateRange": {"Value": 30, "Unit": "DAYS"}}]}' \
     --group-by-attribute "ResourceType"

   ```

   - Use the ARN of the insight to create an Amazon Simple Notification Service (Amazon SNS) topic to receive
     notifications:

   ```

   # EventBridge Rule (CloudFormation snippet)
   Type: AWS::Events::Rule
   Properties:
     Name: CriticalFindingsOver30DaysRule
     EventPattern:
       |
         {"detail":{"insightName":["CriticalFindingsOver30Days"]},"detail-type":["Security Hub Insight Results"],"source":["aws.securityhub"]}
       |
     Targets:
         - Arn: arn:aws:sns:<region>:<account-id>:critical-alerts

   ```

3. **Monitor and optimize**:
   - **Build dashboards**: Use
     services to visualize metrics like Quick Suite or
     Amazon CloudWatch Dashboards.
   - **Review metrics
     regularly**: Periodically review AWS Security Hub's Findings Overview and custom reports.

## Resources

**Related best practices:**

- [SEC02-BP01
  Use strong sign-in mechanisms](../security-pillar/sec_identities_enforce_mechanisms.md "../security-pillar/sec_identities_enforce_mechanisms.md")
- [OPS01-BP03
  Evaluate governance requirements](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.md")
- [OPS01-BP04
  Evaluate compliance requirements](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.md")
- [OPS03-BP02
  Team members are empowered to take action when outcomes are at
  risk](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_emp_take_action.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_emp_take_action.md")
- [OPS03-BP03
  Escalation is encouraged](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_escalation.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_escalation.md")
- [OPS03-BP04
  Communications are timely, clear, and actionable](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_effective_comms.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_effective_comms.md")
- [OPS03-BP06
  Team members are encouraged to maintain and grow their skill
  sets](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.md")
- [[AG.ACG.1]
  Adopt a risk-based compliance framework](../devops-guidance/ag.acg.md "../devops-guidance/ag.acg.md")
- [[AG.ACG.3]
  Automate deployment of detective controls](../devops-guidance/ag.acg.md "../devops-guidance/ag.acg.md")
- [[AG.SAD.2]
  Delegate identity and access management
  responsibilities](../devops-guidance/ag.sad.md "../devops-guidance/ag.sad.md")
- [[O.DIP.2]
  Centralize logs for enhanced security investigations](../devops-guidance/o.dip.md "../devops-guidance/o.dip.md")

**Related documents:**

- [Visualize
  AWS Security Hub Findings using Analytics and Business
  Intelligence Tools](https://aws.amazon.com/blogs/architecture/visualize-aws-security-hub-findings-using-analytics-and-business-intelligence-tools/ "https://aws.amazon.com/blogs/architecture/visualize-aws-security-hub-findings-using-analytics-and-business-intelligence-tools/")
- [Understanding
  custom insights in Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-custom-insights.md "../../../securityhub/latest/userguide/securityhub-custom-insights.md")
- [Automate
  continuous compliance at scale in AWS](https://aws.amazon.com/blogs/mt/automate-cloud-foundational-services-for-compliance-in-aws/ "https://aws.amazon.com/blogs/mt/automate-cloud-foundational-services-for-compliance-in-aws/")

**Related examples:**

- **AWS Security Hub Automated Response
  & Remediation**:
  [GitHub: aws-solutions/automated-security-response-on-aws](https://github.com/aws-solutions/automated-security-response-on-aws "https://github.com/aws-solutions/automated-security-response-on-aws")

**Related services:**

- [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
- [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
- [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")
- [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md")
- [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md")
- [Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md")
