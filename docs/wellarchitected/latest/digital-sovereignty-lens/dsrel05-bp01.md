# DSREL05-BP01 Establish sovereignty-aware failure detection

mechanisms

Establishing sovereignty-aware failure detection mechanisms is crucial for maintaining
compliance with data residency requirements in highly regulated industries. These mechanisms
verify that system monitoring and recovery processes operate strictly within designated
jurisdictions. Failure to implement proper sovereignty controls can result in serious compliance
violations, operational disruptions, and compromised customer trust.

**Desired outcome:** Failures are automatically detected and
responded to within sovereign boundaries. Monitoring data, alerts, and recovery processes remain
within designated jurisdictions. Teams have comprehensive visibility into system health without
compliance violations. Recovery procedures run without delays from compliance verification.

**Common anti-patterns:**

- Consolidating monitoring data from multiple regions into a single global dashboard
  without considering data residency requirements.
- Using notification services that route alerts through regions outside of regulatory
  boundaries.
- Aggregating application and system logs in regions that don't align with data
  sovereignty requirements.
- Implementing external monitoring solutions without verifying their data handling and
  storage practices.
- Focusing only on technical failures while ignoring compliance and sovereignty-related
  failure scenarios.
- Having disaster recovery processes that move workloads across jurisdictional boundaries
  without proper controls.
- Relying on reactive, human-driven checks instead of automated systems.

**Benefits of establishing this best practice:**

- Maintains adherence to data sovereignty laws during both normal operations and failure
  scenarios.
- Enables rapid response to failures without concern for inadvertent compliance
  violations.
- Verifies that monitoring and alerting data remains within appropriate jurisdictional
  boundaries for regulatory adherence.
- Reduces exposure to regulatory penalties by maintaining sovereignty controls during
  critical failure scenarios.
- Provides clear visibility into system health while respecting geographical and
  regulatory constraints.
- Enables immediate response to failures without delays caused by compliance verification
  processes.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Implement sovereignty-aware failure detection by designing monitoring architectures that
respect jurisdictional boundaries while maintaining comprehensive system visibility through
Region-specific infrastructure and compliant in-boundary and Region alerting mechanisms.

Use AWS services that provide built-in Regional isolation and sovereignty controls,
verifying that monitoring data flows and storage locations align with regulatory requirements.

Establish clear escalation procedures that operate within regulatory constraints and
enforce encryption and least privilege access principles.

- Deploy monitoring tools in the same AWS Region as regulated workloads.
- Encrypt logs/metrics at rest and in transit using AWS Key Management Service (KMS).
- Automate alerts and remediation with AWS serverless services like AWS Lambda.

### Implementation steps

1. Deploy Regional monitoring infrastructure within the same AWS Regions as
   regulated workloads. Create [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
   log groups, dashboards, and alarms in each AWS Region where regulated workloads
   operate to improve data residency adherence.
2. Configure [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") with Region-specific
   encryption keys for observability data at rest and in transit. Verify that sensitive
   monitoring data remains within appropriate jurisdictions to maintain data sovereignty.
3. Configure Regional alerting and automation systems within appropriate Regions to
   enable automated incident response and alert processing within the Region.
4. Establish jurisdiction-specific access controls and compliance monitoring roles
   with Region-specific permissions. Maintain regulatory adherence across different
   jurisdictions, and set up continuous compliance validation through [AWS IAM](../../../iam.md "../../../iam.md") and [AWS Config](../../../config.md "../../../config.md").

## Resources

**Related best practices:**

- [PERF05-BP02 Use monitoring solutions to understand the areas where
  performance is most critical](../performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.md "../performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.md")
- [PERF05-BP05 Use automation to proactively remediate
  performance-related issues](../performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.md "../performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.md")
- [OPS04-BP02 Implement application telemetry](../operational-excellence-pillar/ops_observability_application_telemetry.md "../operational-excellence-pillar/ops_observability_application_telemetry.md")
- [REL13-BP02 Use defined recovery strategies to meet the recovery
  objectives](../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md "../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md")
- [DRHCOPS03-BP04 Implement failover automation, and test your
  disaster recovery strategies](../data-residency-hybrid-cloud-services-lens/drhcops03-bp04.md "../data-residency-hybrid-cloud-services-lens/drhcops03-bp04.md")
- [OPS10-BP07 Automate responses to events](../operational-excellence-pillar/ops_event_response_auto_event_response.md "../operational-excellence-pillar/ops_event_response_auto_event_response.md")
- [SEC04-BP03 Automate response to events](../security-pillar/sec_detect_investigate_events_auto_response.md "../security-pillar/sec_detect_investigate_events_auto_response.md")
- [REL06-BP04 Automate responses (Real-time processing and
  alarming)](../reliability-pillar/rel_monitor_aws_resources_automate_response_monitor.md "../reliability-pillar/rel_monitor_aws_resources_automate_response_monitor.md")

**Related documents:**

- [How AWS is helping customers achieve their digital sovereignty and resilience
  goals](https://aws.amazon.com/blogs/security/how-aws-is-helping-customers-achieve-their-digital-sovereignty-and-resilience-goals/ "https://aws.amazon.com/blogs/security/how-aws-is-helping-customers-achieve-their-digital-sovereignty-and-resilience-goals/")
- [How AWS can help you navigate the complexity of digital sovereignty](https://aws.amazon.com/blogs/security/how-aws-can-help-you-navigate-the-complexity-of-digital-sovereignty/ "https://aws.amazon.com/blogs/security/how-aws-can-help-you-navigate-the-complexity-of-digital-sovereignty/")

**Related videos:**

- [AWS re:Invent 2024 - Digital
  sovereignty: Overcome complexity and enable future-readiness (SEC229)](https://www.youtube.com/watch?v=5M8SfFfGF-o "https://www.youtube.com/watch?v=5M8SfFfGF-o")
- [AWS re:Invent 2023 - Meet
  digital sovereignty needs with AWS Dedicated Local Zones (WPS214)](https://www.youtube.com/watch?v=nU4HkNmpG8w "https://www.youtube.com/watch?v=nU4HkNmpG8w")

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/")
- [Amazon SQS](https://aws.amazon.com/sqs/ "https://aws.amazon.com/sqs/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
