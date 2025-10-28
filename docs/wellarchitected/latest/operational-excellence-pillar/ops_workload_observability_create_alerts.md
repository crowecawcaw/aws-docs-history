# OPS08-BP04 Create actionable alerts

Promptly detecting and responding to deviations in your
application's behavior is crucial. Especially vital is recognizing
when outcomes based on key performance indicators (KPIs) are at risk
or when unexpected anomalies arise. Basing alerts on KPIs ensures
that the signals you receive are directly tied to business or
operational impact. This approach to actionable alerts promotes
proactive responses and helps maintain system performance and
reliability.

**Desired outcome:** Receive timely,
relevant, and actionable alerts for rapid identification and
mitigation of potential issues, especially when KPI outcomes are at
risk.

**Common anti-patterns:**

- Setting up too many non-critical alerts, leading to alert
  fatigue.
- Not prioritizing alerts based on KPIs, making it hard to
  understand the business impact of issues.
- Neglecting to address root causes, leading to repetitive alerts
  for the same issue.

**Benefits of establishing this best
practice:**

- Reduced alert fatigue by focusing on actionable and relevant
  alerts.
- Improved system uptime and reliability through proactive issue
  detection and mitigation.
- Enhanced team collaboration and quicker issue resolution by
  integrating with popular alerting and communication tools.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To create an effective alerting mechanism, it's vital to use
metrics, logs, and trace data that flag when outcomes based on
KPIs are at risk or anomalies are detected.

### Implementation steps

1. **Determine key performance indicators
   (KPIs)**: Identify your application's KPIs. Alerts
   should be tied to these KPIs to reflect the business impact
   accurately.
2. **Implement anomaly
   detection**:
   - **Use Amazon CloudWatch anomaly
     detection**: Set up
     [Amazon CloudWatch anomaly detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") to automatically
     detect unusual patterns, which helps you only generate
     alerts for genuine anomalies.
   - **Use AWS X-Ray Insights**:
     1. Set up
        [X-Ray
        Insights](../../../xray/latest/devguide/xray-console-insights.md "../../../xray/latest/devguide/xray-console-insights.md") to detect anomalies in trace data.
     2. Configure
        [notifications
        for X-Ray Insights](../../../xray/latest/devguide/xray-console-insights.md#xray-console-insight-notifications "../../../xray/latest/devguide/xray-console-insights.md#xray-console-insight-notifications") to be alerted on detected
        issues.

   - **Integrate with Amazon DevOps Guru**:
     1. Leverage
        [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/ "https://aws.amazon.com/devops-guru/") for its machine learning
        capabilities in detecting operational anomalies with
        existing data.
     2. Navigate to the
        [notification
        settings](../../../devops-guru/latest/userguide/update-notifications.md#navigate-to-notification-settings "../../../devops-guru/latest/userguide/update-notifications.md#navigate-to-notification-settings") in DevOps Guru to set up anomaly
        alerts.

3. **Implement actionable
   alerts**: Design alerts that provide adequate
   information for immediate action.
   1. Monitor
      [AWS Health events with Amazon EventBridge rules](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md"), or
      integrate programatically with the AWS Health API to
      automate actions when you receive AWS Health events.
      These can be general actions, such as sending all
      planned lifecycle event messages to a chat interface, or
      specific actions, such as the initiation of a workflow
      in an IT service management tool.

4. **Reduce alert fatigue**:
   Minimize non-critical alerts. When teams are overwhelmed
   with numerous insignificant alerts, they can lose oversight
   of critical issues, which diminishes the overall
   effectiveness of the alert mechanism.
5. **Set up composite alarms**:
   Use
   [Amazon CloudWatch composite alarms](https://aws.amazon.com/bloprove-monitoring-efficiency-using-amazon-cloudwatch-composite-alarms-2/ "https://aws.amazon.com/bloprove-monitoring-efficiency-using-amazon-cloudwatch-composite-alarms-2/") to consolidate multiple
   alarms.
6. **Integrate with alert
   tools**: Incorporate tools like
   [Ops
   Genie](https://www.atlassian.com/software/opsgenie "https://www.atlassian.com/software/opsgenie") and
   [PagerDuty](https://www.pagerduty.com/ "https://www.pagerduty.com/").
7. **Engage Amazon Q Developer in chat applications**:
   Integrate
   [Amazon Q Developer in chat applications](https://aws.amazon.com/chatbot/ "https://aws.amazon.com/chatbot/") to relay alerts to Amazon Chime, Microsoft Teams,
   and Slack.
8. **Alert based on logs**: Use
   [log
   metric filters](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md") in CloudWatch to create alarms based
   on specific log events.
9. **Review and iterate**:
   Regularly revisit and refine alert configurations.

**Level of effort for the implementation
plan:** Medium

## Resources

**Related best practices:**

- [OPS04-BP01 Identify key performance indicators](ops_observability_identify_kpis.md "ops_observability_identify_kpis.md")
- [OPS04-BP02 Implement application telemetry](ops_observability_application_telemetry.md "ops_observability_application_telemetry.md")
- [OPS04-BP03 Implement user experience telemetry](ops_observability_customer_telemetry.md "ops_observability_customer_telemetry.md")
- [OPS04-BP04 Implement dependency telemetry](ops_observability_dependency_telemetry.md "ops_observability_dependency_telemetry.md")
- [OPS04-BP05 Implement distributed tracing](ops_observability_dist_trace.md "ops_observability_dist_trace.md")
- [OPS08-BP01 Analyze workload metrics](ops_workload_observability_analyze_workload_metrics.md "ops_workload_observability_analyze_workload_metrics.md")
- [OPS08-BP02 Analyze workload logs](ops_workload_observability_analyze_workload_logs.md "ops_workload_observability_analyze_workload_logs.md")
- [OPS08-BP03 Analyze workload traces](ops_workload_observability_analyze_workload_traces.md "ops_workload_observability_analyze_workload_traces.md")

**Related documents:**

- [Using
  Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
- [Create
  a composite alarm](../../../AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.md")
- [Create
  a CloudWatch alarm based on anomaly detection](../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md")
- [DevOps Guru Notifications](../../../devops-guru/latest/userguide/update-notifications.md "../../../devops-guru/latest/userguide/update-notifications.md")
- [X-ray
  insights notifications](../../../xray/latest/devguide/xray-console-insights.md#xray-console-insight-notifications "../../../xray/latest/devguide/xray-console-insights.md#xray-console-insight-notifications")
- [Monitor,
  operate, and troubleshoot your AWS resources with interactive
  ChatOps](https://aws.amazon.com/chatbot/ "https://aws.amazon.com/chatbot/")
- [Amazon CloudWatch Integration Guide | PagerDuty](https://support.pagerduty.com/docs/amazon-cloudwatch-integration-guide "https://support.pagerduty.com/docs/amazon-cloudwatch-integration-guide")
- [Integrate
  Opsgenie with Amazon CloudWatch](https://support.atlassian.com/opsgenie/docs/integrate-opsgenie-with-amazon-cloudwatch/ "https://support.atlassian.com/opsgenie/docs/integrate-opsgenie-with-amazon-cloudwatch/")

**Related videos:**

- [Create
  Composite Alarms in Amazon CloudWatch](https://www.youtube.com/watch?v=0LMQ-Mu-ZCY "https://www.youtube.com/watch?v=0LMQ-Mu-ZCY")
- [Amazon Q Developer in chat applications Overview](https://www.youtube.com/watch?v=0jUSEfHbTYk "https://www.youtube.com/watch?v=0jUSEfHbTYk")
- [AWS On Air ft. Mutative Commands in Amazon Q Developer in chat applications](https://www.youtube.com/watch?v=u2pkw2vxrtk "https://www.youtube.com/watch?v=u2pkw2vxrtk")

**Related examples:**

- [Alarms,
  incident management, and remediation in the cloud with Amazon CloudWatch](https://aws.amazon.com/bloarms-incident-management-and-remediation-in-the-cloud-with-amazon-cloudwatch/ "https://aws.amazon.com/bloarms-incident-management-and-remediation-in-the-cloud-with-amazon-cloudwatch/")
- [Tutorial:
  Creating an Amazon EventBridge rule that sends notifications
  to Amazon Q Developer in chat applications](../../../chatbot/latest/adminguide/create-eventbridge-rule.md "../../../chatbot/latest/adminguide/create-eventbridge-rule.md")
- [One
  Observability Workshop](https://catalog.workshops.aws/observability/en-US/intro "https://catalog.workshops.aws/observability/en-US/intro")
