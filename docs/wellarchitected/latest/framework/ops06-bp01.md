

# OPS06-BP01 Create actionable alerts

 When each alert maps to a defined response, operators know what to do when it fires, and important signals aren't lost in low-value noise. 

 **Desired outcome:** 
+  Your alerts fire on conditions that represent problems, such as an objective at risk, not on every raw metric deviation. 
+  Each of your alerts maps to a specific, documented response, and where possible you automate that response. 
+  Each of your alerts has a clear owner and a defined escalation path, so no notification is left unattended. 
+  Your alerts link to current runbooks or playbooks, so any operator can respond the same way. 
+  Your alert volume stays low enough that operators treat each alert as meaningful rather than background noise. 

 **Common anti-patterns:** 
+  Teams raise alerts that describe a symptom but carry no defined response, so operators improvise during incidents. 
+  Monitoring generates so many low-value alerts that operators overlook the ones that matter. 
+  Alerts have no assigned owner, so handling depends on whoever happens to notice. 
+  Operators respond to the same alert differently each time because no shared response process exists. 
+  Alerts fire on raw metrics without correlation, producing a burst of notifications for a single underlying problem. 

 **Benefits of establishing this best practice:** 
+  Operators experience less alert fatigue because only actionable alerts reach them. 
+  Mean time to resolution (MTTR) drops because each alert carries a known response. 
+  Mean time to investigate (MTTI) drops, which further reduces MTTR. 
+  Operational responses scale because responses are documented and often automated. 
+  Incident handling stays consistent and reliable across teams and shifts. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 An actionable alert tells an operator what is wrong and what to do about it. Monitoring can emit a signal for almost any state change, but few of those signals need human attention. If an alert fires, someone or something must act. Signals that carry no response belong on a dashboard or in a log. The alerting signal can be a metric, a service level objective, or a recurring log signal turned into a metric ([OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md)). 

 Alert fatigue is the dominant failure mode, where operators receive hundreds of notifications a day and learn to ignore them. Then, the one alert that signals a real incident is lost with the rest. The usual cause is alerting on raw metrics. Instead, alert on conditions that represent actual problems. A single failing dependency can trip a dozen metric thresholds, producing many alerts for one root cause. Aggregating related signals into a composite condition reduces alert fatigue and produces one actionable alert. 

 Every threshold is a trade-off between sensitivity and precision. A tight threshold can miss early warnings of a developing problem, while a loose one can bury operators in false positives. Tune thresholds against historical data, and revisit them as the workload changes. An alert that is useful at launch can become useless a year later depending on changes to your workload. Some metrics have no fixed threshold, and their normal range might shift with time of day or day of week. Anomaly detection alarms learn each metric's normal band and fire on deviations. 

 For workloads instrumented with OpenTelemetry, [CloudWatch Omni alerts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-alerts.html) add timing controls such as a pending duration, so a single spike does not send an alert, and a recovery duration, so a flapping signal does not resolve and fire again. One Omni alert also contains warning and critical tiers, each routable to a destination, so the same condition can warn a team channel before its critical tier reaches an on-call engineer. Omni alerts are separate from CloudWatch alarms, which continue to work unchanged. 

 Alert conditions form a hierarchy, and you should start at the top. Business outcome metrics, for example the KPIs from [OPS02-BP01 Develop key performance indicators](ops02-bp01.md), and RED metrics (rate, errors, duration) are closest to what users experience. They move only when something important is at stake, so they produce the least noise. Where service-level objectives exist, alarm on the error budget burn rate, or how fast the service is consuming its allowance for failure. A fast burn demands interruption, and a slow burn can wait for review. The alert carries its own urgency, and its threshold reflects the objective (for more detail, see [OPS02-BP05 Regularly analyze workload traces](ops02-bp05.md)). 

 Work down the stack deliberately. Application metrics, then infrastructure metrics, then the metrics of the underlying compute and storage each add diagnostic detail. Each layer down fires more often and means less on its own — a busy processor does not comprise a problem unless something above it slows down. Alert at the top of the hierarchy by default, and keep the lower layers on dashboards for diagnosis. Alert low in the stack only where a hard limit is real, such as a disk that must not fill. 

![Pyramid diagram showing monitoring layers stacked from application metrics at the top down to infrastructure metrics and then compute and storage metrics at the base.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/metrics-pyramid.png)

*Monitoring metrics pyramid from application down to compute and storage*


 Each alert needs an owner and an escalation path for when the first responder cannot resolve it. Link each alert to a current runbook or playbook so any operator can respond the same way, keeping handling consistent across shifts. Recurring incidents point at a problem worth removing (for more detail, see [OPS07-BP01 Perform post-incident analysis](ops07-bp01.md)). 

 You can automate the first minutes after an alert. Configure an alarm to start a [CloudWatch investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) when it fires; the investigation correlates related telemetry and recent changes into a probable-cause hypothesis before the responder arrives. [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) can be triggered from a ticket, a webhook, or its own monitoring, and it then investigates autonomously and returns root cause analyses and mitigation plans to the channel that raised the alert. The alert's named owner remains accountable for the response. 

 Provider-side service events and planned lifecycle changes — such as a required version upgrade before automatic enforcement — can affect availability even when your code is unchanged. Track these events through an authoritative health signal, and route them into the same response process as internal alerts. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Alert on the objectives users feel:** Where Application Signals tracks your [service level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html), create alarms on error budget burn rate over more than one look-back window: a short window that catches a fast burn and interrupts the on-call, and a long window that surfaces a slow steady burn as a work item. A burn-rate alert is actionable by construction, because it fires only when the objective is at risk. 

1.  **Let alarms learn what normal looks like:** Create [anomaly detection alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html) for metrics whose normal shifts with traffic, so the alarm follows the learned band. Anomalies in trace data alert through [X-Ray insights notifications](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-insights.html). Keep static thresholds for limits that do not move, and revisit both as the workload changes. 

1.  **Reduce noise with composite alarms:** Group related alarms into [composite alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) in Amazon CloudWatch so that a single root cause produces one meaningful alert rather than many. Base each composite condition on the failure it represents, not on individual metrics. For OpenTelemetry workloads monitored in CloudWatch Omni, an [Omni alert](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-alerts.html) tracks each service as a contributor when it receives one result per service. As a result, one alert covers the fleet, and the alert's detail view identifies the services that are breaching. 

1.  **Track provider-side events with AWS Health:** Use [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) as the authoritative source for service events and upcoming changes that can affect your resources. 

   1.  Route [purpose-fit Health notifications](https://docs.aws.amazon.com/health/latest/ug/) to email and chat channels, and integrate programmatically [through Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html). 

   1.  Track events that need action in the change management or ITSM tools you already use, such as [Jira](https://docs.aws.amazon.com/smc/latest/ag/cloud-sys-health.html) or [ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-aws-health.html). 

   1.  If you use AWS Organizations, enable organizational view to [aggregate Health events across accounts](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html). 

1.  **Create work items automatically from alarms:** Configure CloudWatch alarms to [create OpsItems in AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html) so that a threshold breach starts a tracked response without manual handoff. If your organization runs incidents in the tooling from step 7, route the alarm there instead. The principle is that no alert lands without a work item. 

1.  **Create work items from events with EventBridge:** [Create EventBridge rules that open OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-automatically-create-OpsItems-2.html) for operational events that need action but arrive without an alarm. 

1.  **Route alerts into the tools your organization already uses:** Send [alarm notifications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.html) to your paging tools, such as [Opsgenie](https://support.atlassian.com/opsgenie/docs/integrate-opsgenie-with-amazon-cloudwatch/) and [PagerDuty](https://docs.pagerduty.com/integrations/amazon-cloudwatch-integration-guide), track the response in the incident management tooling your teams already work in, such as [ServiceNow](https://www.servicenow.com/docs/r/zurich/integrate-applications/integration-hub/amazon-cloudwatch.html) or [Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/integrate-with-amazon-cloudwatch/), and relay alerts into [chat channels](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) where teams live in Slack or Microsoft Teams. An alert that arrives in an unmonitored tool is not actionable, however good its condition. 

1.  **Hand the first minutes to assistants:** Configure alarms to [create investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-configure-alarms.html), so CloudWatch investigations correlates related telemetry and recent changes into a hypothesis of the probable cause while responders are still being notified. Use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) for autonomous incident response: triggered from your ticketing system, a webhook, or its own proactive monitoring, it investigates and returns root cause analyses and mitigation plans to the originating ticket. Once your Omni space is connected to DevOps Agent, you can start the investigation yourself from a firing Omni alert, which arrives seeded with the alert's context. Assistants complement the response plans in these steps, while the owner named in each alert is accountable for the response. 

1.  **Compose the full path for new incidents:** A single alarm can do all of the first minute's work: [notify](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.html) the on-call, open the incident ticket, and [start an investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Start-Investigation-Alarm.html) in the same action. An [EventBridge rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/) matching the investigation's status changes then writes its findings into the ticket as they arrive, so the person that picks up the ticket finds a root cause hypothesis within. This is how AWS and Amazon run their own operations, and every part of it is available to your workload. 

1.  **Document a response plan for each alert type:** For each class of alert, record the owner, the escalation path, and the expected actions alongside the runbooks and playbooks that [OPS05-BP01 Develop and test runbooks to perform procedures](ops05-bp01.md) develops. Escalation paths themselves are the practice of [OPS06-BP03 Define escalation paths](ops06-bp03.md). 

1.  **Attach automation runbooks to the response:** Associate [Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) with your work items so that [common remediation runs](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-remediating.html) as soon as one opens. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS06-BP02 Automate responses to events](ops06-bp02.md) 
+  [OPS06-BP03 Define escalation paths](ops06-bp03.md) 
+  [OPS05-BP01 Develop and test runbooks to perform procedures](ops05-bp01.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md) 
+  [OPS02-BP05 Regularly analyze workload traces](ops02-bp05.md) 
+  [OPS07-BP01 Perform post-incident analysis](ops07-bp01.md) 

 **Related documents:** 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 
+  [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) 
+  [Service level objectives (SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) 
+  [Create a CloudWatch alarm based on anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html) 
+  [CloudWatch Omni alerts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-alerts.html) 
+  [Configure alarms to create investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-configure-alarms.html) 
+  [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) 
+  [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/) 

 **Related videos:** 
+  [Incident Investigation with AWS DevOps Agent - AWS Tech Tales](https://www.youtube.com/watch?v=PcbOQAtT13I) 
+  [AWS re:Invent 2025 - Version lifecycle management at scale with AWS Health (SPS326)](https://www.youtube.com/watch?v=lt7wcPDgZhk) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US/intro) 

 **Related services:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 