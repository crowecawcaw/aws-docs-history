AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Migrating to AWS Systems Manager OpsCenter

This guide helps you understand key differences between Incident Manager and OpsCenter to decide if OpsCenter fits your operational needs and provides ways to migrate to OpsCenter from AWS Systems Manager Incident Manager.

[AWS Systems Manager OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md"), a capability of AWS Systems Manager, provides a central location where operations engineers and IT professionals can view, investigate, and resolve operational work items (OpsItems) related to AWS resources. OpsCenter is designed to reduce mean time to resolution (MTTR) for issues impacting AWS resources. OpsCenter aggregates and standardizes OpsItems across services while providing contextual investigation data about each OpsItem, related OpsItems, and related resources. OpsCenter integrates with Systems Manager Automation, allowing you to use Automation runbooks to investigate and resolve issues. You can view automatically-generated summary reports about OpsItems by status and source. You can also use [OpsCenter's cross-account](../../../systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.md "../../../systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.md") capability to centrally manage OpsItems across accounts.

###### Note

There are charges associated with the OpsCenter use. Please refer to the [AWS Systems Manager pricing page](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/") for more details.

Similar to Incident Manager, OpsCenter has integrations with Amazon CloudWatch and Amazon EventBridge. This means you can configure these services to automatically create an OpsItem in OpsCenter when a CloudWatch alarm enters the `ALARM` state or when EventBridge processes an event from any AWS service that publishes events. Configuring CloudWatch alarms and EventBridge events to automatically create OpsItems allows you to quickly diagnose and remediate issues with AWS resources from a single console.

## Understanding the differences

AWS Systems Manager Incident Manager provides incident response capabilities including automated response plans, responder engagement and escalation, on-call rotation management, runbook automation, chat-ops integration (Slack, Microsoft Teams, Amazon Chime), and post-incident analysis. These features help organizations coordinate and resolve critical, time-sensitive incidents affecting AWS-hosted applications.

In contrast, AWS Systems Manager OpsCenter focuses on managing operational work items (OpsItems) for day-to-day operational issues such as security alerts, performance degradation, resource failures, health notifications, and state changes. OpsCenter integrates with AWS resources through Amazon CloudWatch and Amazon EventBridge, enabling automated OpsItem creation and remediation using Systems Manager Automation runbooks. OpsCenter supports cross-account management of OpsItems within a region, allowing operations teams to view, investigate, and resolve issues across multiple AWS accounts. However, OpsCenter does not include paging or on-call rotation capabilities.

The key differences between these two AWS services lie in their focus and scope. Incident Manager is designed for critical, time-sensitive incident response, while OpsCenter is oriented towards the management of broader operational tasks and work items.

The following table compares key capabilities between Incident Manager and OpsCenter. Use this comparison to decide if OpsCenter fits your operational needs.

| Feature/Capability          | AWS Systems Manager Incident Manager                                                          | AWS Systems Manager OpsCenter                                                                    |
| --------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Primary Purpose             | Critical, time-sensitive incident response and coordination                                   | Day-to-day operational work item management                                                      |
| Use Cases                   | Application-impacting incidents; Security breaches; Service outages; Critical system failures | Security alerts; Performance degradation; Resource failures; Health notifications; State changes |
| Automated Paging            | Yes<br>• Built-in paging and responder engagement                                             | No<br>• Requires third-party integration (PagerDuty, ServiceNow, Jira)                           |
| On-Call Rotation Management | Yes<br>• Native on-call schedules and rotation                                                | No<br>• Not supported                                                                            |
| Escalation Policies         | Yes<br>• Automated escalation chains                                                          | No<br>• Manual escalation required                                                               |
| Chat-Ops Integration        | Yes<br>• Slack, Microsoft Teams, Amazon Chime                                                 | Limited<br>• Manual integration required                                                         |
| Runbook Automation          | Yes<br>• Automated execution via response plans                                               | Yes<br>• Manual execution of Systems Manager Automation runbooks                                 |
| Cross-Account Management    | Yes<br>• Cross-account incident sharing                                                       | Yes<br>• Cross-account OpsItem management within a region                                        |

## Migration options

If you have existing CloudWatch alarms and EventBridge rules integrated with Incident Manager, you'll need to update them to integrate with OpsCenter. You can migrate using one of the following approaches:

Automated migration using runbooks

Use [Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") runbooks to automatically migrate your CloudWatch alarms and EventBridge rules from Incident Manager to OpsCenter. This approach includes backup, configurable approval workflows, and detailed logging. You can choose to require manual approval before migration or skip the approval step for automated large-scale migrations. For step-by-step instructions, see [Using migration runbooks for OpsCenter](migration-opscenter-runbooks.md "migration-opscenter-runbooks.md").

Manual integration

Manually configure your CloudWatch alarms and EventBridge rules to integrate with OpsCenter. For instructions, see [Configuring CloudWatch alarms to create OpsItems](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md") and [Configuring EventBridge to create OpsItems](../../../systems-manager/latest/userguide/OpsCenter-automatically-create-OpsItems-2.md "../../../systems-manager/latest/userguide/OpsCenter-automatically-create-OpsItems-2.md") in the Systems Manager User Guide.

## Related resources

- [AWS Systems Manager OpsCenter User Guide](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md")
- [Exporting Incident Manager data](export-data.md "export-data.md")
- [Cleaning up Incident Manager Resources](migration-cleanup.md "migration-cleanup.md")
