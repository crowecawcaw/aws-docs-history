AWS Systems Manager Incident Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Incident Manager,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Creating incidents automatically or manually in

Incident Manager

Incident Manager, a tool in AWS Systems Manager, helps you manage and quickly respond to incidents. You
can configure Amazon CloudWatch and Amazon EventBridge to automatically create incidents based on CloudWatch alarms
and EventBridge events. You can also create incidents manually on the incident list page or by
using the [StartIncident](../APIReference/API_StartIncident.md "../APIReference/API_StartIncident.md")
API action from the AWS CLI or the AWS SDK. Incident Manager deduplicates incidents created from
the same CloudWatch alarm or EventBridge event into the same incident.

For incidents automatically created by CloudWatch alarms or EventBridge events, Incident Manager attempts to
create an incident in the same AWS Region as the event rule or alarm. In the event that
Incident Manager is not available in the AWS Region, CloudWatch or EventBridge automatically create the
incident in one of the available Regions specified in your replication set. For more
information, see [Managing incidents across
AWS accounts and Regions in Incident Manager](incident-manager-cross-account-cross-region.md "incident-manager-cross-account-cross-region.md").

When the system creates an incident, Incident Manager automatically collects information about
the AWS resources involved in the incident and adds this information to the
**Related items** tab. If you specified a runbook in your response
plan, when the system creates an incident, Incident Manager can send the information about the
AWS resources involved in the incident to the runbook. The system can then target those
resources when it initiates the runbook and attempts to remediate the issue.

When the system creates an incident, it also creates a parent operational workitem
(OpsItem) in OpsCenter, a component of Systems Manager, and links it to the incident as a related
item. You can use this OpsItem to track related work and future incident analyses. Calls to
OpsCenter incur costs. For more information about OpsCenter pricing, see [Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

###### Important

Note the following important details.

- In the event that Incident Manager is not available, the system can only fail over
  and create incidents in other AWS Regions if you have specified at least two
  Regions in your replication set. For information about configuring a replication
  set, see [Getting started with Incident Manager](getting-started.md "getting-started.md").
- Incidents created by a cross-Region failover don't invoke runbooks specified in response plans.

## Creating incidents automatically with

CloudWatch alarms

CloudWatch uses your CloudWatch metrics to alert you about changes in your environment and to
automatically perform the start incident action. CloudWatch works with Systems Manager and Incident Manager
to create an incident from a response plan template when an alarm goes into alarm state.
This requires the following prerequisites:

- Incident Manager configured and replication set created. This step creates the
  Incident Manager service linked role in your account, providing the necessary
  permissions.
- A configured Incident Manager response plan. To learn how to configure Incident Manager
  response plans, see [Creating and configuring response plans in
  Incident Manager](response-plans.md "response-plans.md") in the _Incident
  preparation_ section of this guide.
- Configured CloudWatch metrics monitoring your application. For monitoring best
  practices, see [Monitoring](incident-response.md#incident-response-monitoring "incident-response.md#incident-response-monitoring") in the _Incident
  preparation_ section of this guide.

###### To create an alarm with a **Start incident** action

1. Create an alarm in CloudWatch. For more information, see [Using
   Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.
2. When choosing the action for the alarm to perform, select **Add Systems Manager
   action**.
3. Choose **Create incident** and select the **Response
   plan** for this incident.
4. Complete the remaining steps in your selected alarm type guide.

###### Tip

You can also add the create incident action to any existing alarm.

## Creating incidents automatically

with EventBridge events

EventBridge rules watch for event patterns. If the event matches the defined pattern,
Incident Manager creates an incident using the chosen response plan.

### Creating incidents using

SaaS partners events

You can configure EventBridge to receive events from software as a service (SaaS) partner
applications and services, allowing for third-party integration. After configuring
EventBridge to receive events from third-party partners, you can create rules that match on
partner events to create incidents. To see a list of third-party integrations, see
[Receiving
events from a SaaS partner](../../../eventbridge/latest/userguide/create-partner-event-bus.md "../../../eventbridge/latest/userguide/create-partner-event-bus.md").

###### Configure EventBridge to receive events from a SaaS integration.

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Partner event
   sources**.
3. Use the search bar to find the partner that you want and choose
   **Set up** for that partner.
4. Choose **Copy** to copy your account ID to the
   clipboard.

###### Note

To integrate with Salesforce use the steps described in the [Amazon AppFlow user guide](../../../appflow/latest/userguide/EventBridge.md "../../../appflow/latest/userguide/EventBridge.md"). 5. Go to the partner's website and follow the instructions to create a
partner event source. Use your account ID for this. The event source that
you create is available only on your account. 6. Go back to the EventBridge console and choose **Partner event
sources** in the navigation pane. 7. Select the button next to the partner event source, and choose
**Associate with event bus**.

###### Create a rule that triggers on events from a SaaS partner

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on
the same event bus. 5. For **Event bus**, choose the event bus that corresponds
to this partner. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose **AWS events or
EventBridge partner events**. 9. For **Event pattern**, choose **Event pattern
form**. 10. For **Event source**, choose **EventBridge
partners** 11. For **Partners**, choose the name of the partner. 12. For **Event type**, choose **All
Events** or choose the type of event to use for this rule. If
you choose **All Events**, all events emitted by this
partner event source will match the rule.

If you want to customize the event pattern, choose
**Edit**, make your changes, and then choose
**Save**. 13. Choose **Next**. 14. For **Select a target**, choose **Incident
Manager response plan**, and then choose a **Response
plan**.

###### Note

When selecting a response plan, all response plans that you own and
have been shared with your account appear in the **Response
plan** dropdown list. 15. EventBridge can create the IAM role needed for your rule to run:

    * To create an IAM role automatically, choose **Create a
     new role for this specific resource**.
    * To use an IAM role that you created before, choose **Use
     existing role**.

16. Choose **Next**.
17. (Optional) Enter one or more tags for the rule. For more information, see
    [Amazon EventBridge
    tags](../../../eventbridge/latest/userguide/eventbridge-tagging.md "../../../eventbridge/latest/userguide/eventbridge-tagging.md") in the _Amazon EventBridge User Guide_.
18. Choose **Next**.
19. Review your rule then choose **Create rule**.

### Creating incidents using

AWS service events

EventBridge also receives events from the AWS services listed in [Events
from Supported AWS Services](../../../eventbridge/latest/userguide/event-types.md "../../../eventbridge/latest/userguide/event-types.md"). Similar to how you configure rules for
SaaS partners, you can configure them for AWS services.

###### Create a rule that triggers on events from an AWS service

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on
the same event bus. 5. For **Event bus**, choose
**default**. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose **AWS events or
EventBridge partner events**. 9. For **Event pattern**, choose **Event pattern
form**. 10. For **Event source**, choose **AWS
services**. 11. For **Service name**, choose the service that monitors
for an incident. 12. For **Event type**, choose **All
Events** or choose the type of event to use for this rule. If
you choose **All Events**, all events emitted by this
partner event source will match the rule.

If you want to customize the event pattern, choose
**Edit**, make your changes, and then choose
**Save**. 13. Choose **Next**. 14. For **Select a target**, choose **Incident
Manager response plan**, and then choose a **Response
plan**.

###### Note

When selecting a response plan, all response plans that you own and
have been shared with your account appear in the **Response
plan** dropdown list. 15. EventBridge can create the IAM role needed for your rule to run:

    * To create an IAM role automatically, choose **Create a
     new role for this specific resource**.
    * To use an IAM role that you created before, choose **Use
     existing role**.

16. Choose **Next**.
17. (Optional) Enter one or more tags for the rule. For more information, see
    [Amazon EventBridge
    tags](../../../eventbridge/latest/userguide/eventbridge-tagging.md "../../../eventbridge/latest/userguide/eventbridge-tagging.md") in the _Amazon EventBridge User Guide_.
18. Choose **Next**.
19. Review your rule then choose **Create rule**.

## Creating incidents manually

Responders can manually track an incident using the Incident Manager console by using a
predefined response plan. Use the following steps to create an incident.

1. Open the [Incident Manager console](https://console.aws.amazon.com/systems-manager/incidents/home "https://console.aws.amazon.com/systems-manager/incidents/home").
2. Choose **Start incident**.
3. For **Response plan**, choose a response plan
   from the list.
4. (Optional) To override the title provided by the defined response plan, enter
   an **Incident title**.
5. (Optional) To override the impact provided by the defined response plan, enter
   the **Impact** of the incident.

### Required IAM permissions

for manually starting incidents

To manually start incidents, users need permissions to access the Incident Manager
console, view response plans, and start incidents. When a user starts an incident,
Incident Manager uses [forward access
sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") (FAS) to make the `StartEngagement` call as part of
`StartIncident`.

The following IAM policy provides the necessary permissions for manually
starting incidents, viewing the response plans that incidents can be created with,
and viewing and editing incidents after they are created.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm-incidents:StartIncident",
 "ssm-incidents:GetResponsePlan",
 "ssm-incidents:ListResponsePlans",
 "ssm-incidents:TagResource",
 "ssm-incidents:GetIncidentRecord",
 "ssm-incidents:ListIncidentRecords",
 "ssm-incidents:UpdateIncidentRecord"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm-contacts:StartEngagement"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "ssm-incidents.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:CreateOpsItem"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "ssm-incidents.amazonaws.com"
 }
 }
 }
 ]
}`

```

This policy includes the following permissions:

- [ssm-incidents:StartIncident](../APIReference/API_StartIncident.md "../APIReference/API_StartIncident.md") - Allows users to manually start an
  incident using the console or API. This creates a new incident record from a
  response plan.
- [ssm-incidents:GetResponsePlan](../APIReference/API_GetResponsePlan.md "../APIReference/API_GetResponsePlan.md") - Allows users to retrieve
  information about a specific response plan.
- [ssm-incidents:ListResponsePlans](../APIReference/API_ListResponsePlans.md "../APIReference/API_ListResponsePlans.md") - Allows users to list all
  response plans in their account.
- [ssm-incidents:TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") - Allows adding tags to Incident Manager
  resources, including incidents and response plans.
- [ssm-incidents:GetIncidentRecord](../APIReference/API_GetIncidentRecord.md "../APIReference/API_GetIncidentRecord.md") - Allows users to retrieve
  detailed information about a specific incident.
- [ssm-incidents:ListIncidentRecords](../APIReference/API_ListIncidentRecords.md "../APIReference/API_ListIncidentRecords.md") - Allows users to list all
  incidents in their account.
- [ssm-incidents:UpdateIncidentRecord](../APIReference/API_UpdateIncidentRecord.md "../APIReference/API_UpdateIncidentRecord.md") - Allows users to update the
  details of an existing incident.
- [ssm-contacts:StartEngagement](../APIReference/API_SSMContacts_StartEngagement.md "../APIReference/API_SSMContacts_StartEngagement.md") (with condition) - Allows
  Incident Manager to start engagements with contacts. The condition ensures this
  can only be called via Incident Manager.
- [ssm:CreateOpsItem](../../../systems-manager/latest/APIReference/API_CreateOpsItem.md "../../../systems-manager/latest/APIReference/API_CreateOpsItem.md") (with condition) - Allows Incident Manager to
  create an OpsItem in OpsCenter. The condition ensures this can only be
  called via Incident Manager.

The [aws:CalledViaFirst](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledviafirst "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledviafirst") condition key ensures that certain permissions (like
`StartEngagement`) can only be used when the request comes through
the Incident Manager service. This approach uses FAS instead of service-linked roles,
which prevents potential cross-account calls that could pose security risks.
