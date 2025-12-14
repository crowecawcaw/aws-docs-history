# OPS10-BP07 Automate responses to events

Automating event responses is key for fast, consistent, and error-free operational handling. Create streamlined processes and use tools to automatically manage and respond to events, minimizing manual interventions and enhancing operational effectiveness.

**Desired outcome:**

- Reduced human errors and faster resolution times through automation.
- Consistent and reliable operational event handling.
- Enhanced operational efficiency and system reliability.

**Common anti-patterns:**

- Manual event handling leads to delays and errors.
- Automation is overlooked in repetitive, critical tasks.
- Repetitive, manual tasks lead to alert fatigue and missing critical issues.

**Benefits of establishing this best
practice:**

- Accelerated event responses, reducing system downtime.
- Reliable operations with automated and consistent event handling.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Incorporate automation to create efficient operational workflows and minimize manual interventions.

### Implementation steps

1. **Identify automation opportunites:** Determine repetitive tasks for automation, such as issue remediation, ticket enrichment, capacity management, scaling, deployments, and testing.
2. **Identify automation prompts:**
   - Assess and define specific conditions or metrics that initiate automated responses using [Amazon CloudWatch alarm actions](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions").
   - Use [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") to respond to events in AWS services, custom workloads, and SaaS applications.
   - Consider initiation events such as [specific log entries](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md"), [performance metrics thresholds](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md"), or [state changes](../../../config/latest/developerguide/remediation.md "../../../config/latest/developerguide/remediation.md") in AWS resources.

3. **Implement event-driven automation:**
   - Use AWS Systems Manager Automation runbooks to simplify maintenance, deployment, and remediation tasks.
   - [Creating incidents in Incident Manager](../../../incident-manager/latest/userguide/incident-creation.md "../../../incident-manager/latest/userguide/incident-creation.md") automatically gathers and adds details about the involved AWS resources to the incident.
   - Proactively monitor quotas using [Quota Monitor for AWS](https://aws.amazon.com/solutions/implementations/quota-monitor/ "https://aws.amazon.com/solutions/implementations/quota-monitor/").
   - Automatically adjust capacity with [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/") to maintain availability and performance.
   - Automate development pipelines with [Amazon CodeCatalyst](https://codecatalyst.aws/explore "https://codecatalyst.aws/explore").
   - Smoke test or continually monitor endpoints and APIs [using synthetic monitoring](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md").

4. **Perform risk mitigation through automation:**
   - Implement [automated security responses](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/ "https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/") to swiftly address risks.
   - Use [AWS Systems Manager State Manager](../../../systems-manager/latest/userguide/systems-manager-state.md "../../../systems-manager/latest/userguide/systems-manager-state.md") to reduce configuration drift.
   - [Remediate noncompliant resources with AWS Config Rules](../../../config/latest/developerguide/remediation.md "../../../config/latest/developerguide/remediation.md").

**Level of effort for the implementation plan:** High

## Resources

**Related best practices:**

- [OPS08-BP04 Create actionable alerts](ops_workload_observability_create_alerts.md "ops_workload_observability_create_alerts.md")
- [OPS10-BP02 Have a process per alert](ops_event_response_process_per_alert.md "ops_event_response_process_per_alert.md")

**Related documents:**

- [Using Systems Manager Automation runbooks with Incident Manager](../../../incident-manager/latest/userguide/tutorials-runbooks.md "../../../incident-manager/latest/userguide/tutorials-runbooks.md")
- [Creating incidents in Incident Manager](../../../incident-manager/latest/userguide/incident-creation.md "../../../incident-manager/latest/userguide/incident-creation.md")
- [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
- [Monitor resource usage and send notifications when approaching quotas](../../../solutions/latest/quota-monitor-for-aws/solution-overview.md "../../../solutions/latest/quota-monitor-for-aws/solution-overview.md")
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [What is Amazon CodeCatalyst?](../../../codecatalyst/latest/userguide/welcome.md "../../../codecatalyst/latest/userguide/welcome.md")
- [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
- [Using Amazon CloudWatch alarm actions](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions")
- [Remediating Noncompliant Resources with AWS Config Rules](../../../config/latest/developerguide/remediation.md "../../../config/latest/developerguide/remediation.md")
- [Creating metrics from log events using filters](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md")
- [AWS Systems Manager State Manager](../../../systems-manager/latest/userguide/systems-manager-state.md "../../../systems-manager/latest/userguide/systems-manager-state.md")

**Related videos:**

- [Create Automation Runbooks with AWS Systems Manager](https://www.youtube.com/watch?v=fQ_KahCPBeU "https://www.youtube.com/watch?v=fQ_KahCPBeU")
- [How to automate IT Operations on AWS](https://www.youtube.com/watch?v=GuWj_mlyTug "https://www.youtube.com/watch?v=GuWj_mlyTug")
- [AWS Security Hub CSPM automation rules](https://www.youtube.com/watch?v=XaMfO_MERH8 "https://www.youtube.com/watch?v=XaMfO_MERH8")
- [Start your software project fast with Amazon CodeCatalyst blueprints](https://www.youtube.com/watch?v=rp7roaoPzFE "https://www.youtube.com/watch?v=rp7roaoPzFE")

**Related examples:**

- [Amazon CodeCatalyst Tutorial: Creating a project with the Modern three-tier web application blueprint](../../../codecatalyst/latest/userguide/getting-started-template-project.md "../../../codecatalyst/latest/userguide/getting-started-template-project.md")
- [One Observability Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US")
- [Respond to incidents using Incident Manager](https://catalog.workshops.aws/getting-started-with-com/en-US/operations-management/incident-manager "https://catalog.workshops.aws/getting-started-with-com/en-US/operations-management/incident-manager")
