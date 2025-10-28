# Use EventBridge rules with Image Builder pipelines

Events from a wide range of AWS and partner services are streamed to Amazon EventBridge
event buses in near real-time. You can also generate custom events, and send events
from your own applications to EventBridge. The event buses use rules to determine where to
route event data.

Image Builder pipelines are available as EventBridge rule targets, which means that you can run
an Image Builder pipeline based on rules that you create to respond to events on the bus,
or on a schedule.

For a summary of system generated events that Image Builder sends to EventBridge, see
[Event messages that Image Builder sends](integ-eventbridge.md#integ-eb-event-summary "integ-eventbridge.md#integ-eb-event-summary").

###### Note

Event buses are specific to a Region. The rule and the target must be in the same
Region.

###### Contents

- [EventBridge terms](#ev-terms "#ev-terms")
- [View EventBridge rules for your Image Builder pipeline](#ev-rules-pipeline-tab "#ev-rules-pipeline-tab")
- [Use EventBridge rules to schedule a pipeline build](#ev-rules-schedule-pipeline "#ev-rules-schedule-pipeline")

## EventBridge terms

This section contains a summary of terms to help you understand
how EventBridge integrates with your Image Builder pipelines.

Event

Describes a change in an environment that might affect
one or more application resources. The environment can be
an AWS environment, a SaaS partner service or application,
or one of your applications or services. You can also set up
scheduled events on a timeline.

Event bus

A pipeline that receives event data from applications and services.

Source

The service or application that sent the event to the
event bus.

Target

A resource or endpoint that EventBridge invokes when it matches
a rule, delivering data from the event to the target.

Rule

A rule matches incoming events and sends them to targets
for processing. A single rule can send an event to multiple
targets, which can then run in parallel. Rules are based either
on an event pattern or a schedule.

Pattern

An event pattern defines the event structure and the fields that
a rule matches in order to initiate the target action.

Schedule

Schedule rules perform an action on a schedule, such as running an Image Builder pipeline to
refresh an image on a quarterly basis. There are two types of schedule
expressions:

- **Cron expressions** – Match specific scheduling
  criteria using the cron syntax that can outline simple criteria; for
  example, running weekly on a specific day. You can also establish
  more complex criteria, such as running quarterly on the fifth day of
  the month, between 2 AM and 4 AM.
- **Rate expressions** –
  Specify a regular interval when the target is invoked, such as
  every 12 hours.

## View EventBridge rules for your Image Builder pipeline

The **EventBridge rules** tab in the Image Builder **Image
pipelines** detail page displays EventBridge event buses that your
account has access to, and the rules for the selected event bus that
apply to the current pipeline. This tab also links directly to the
EventBridge console for creating new resources.

###### Actions that link to the EventBridge console

- **Create event bus**
- **Create rule**

To learn more about EventBridge, see the following topics in the
_Amazon EventBridge User Guide_.

- [What is Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")
- [Amazon EventBridge event buses](../../../eventbridge/latest/userguide/eb-event-bus.md "../../../eventbridge/latest/userguide/eb-event-bus.md")
- [Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md")
- [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md")

## Use EventBridge rules to schedule a pipeline build

For this example, we create a new schedule rule for the default
event bus, using a rate expression. The rule in this example generates
an event on the event bus every 90 days. The event initiates a pipeline
build to refresh the image.

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. To see a list of the image pipelines created under your
   account, choose **Image pipelines**
   from the navigation pane.

###### Note

The list of image pipelines includes an indicator for
the type of output image that is created by the pipeline
– AMI or Docker. 3. To view details or edit a pipeline, choose the
**Pipeline name** link. This opens the
detail view for the pipeline.

###### Note

You can also select the check box next to the
**Pipeline name**, then choose
**View detail**. 4. Open the **EventBridge rules** tab. 5. Keep the default event bus that is pre-selected in
the **Event Bus** panel. 6. Choose **Create rule**. This takes
you to the **Create rule** page in the
Amazon EventBridge console. 7. Enter a name and description for the rule. The rule
name must be unique within the event bus for the
selected Region. 8. In the **Define pattern** panel,
choose the **Schedule** option. This
expands the panel, with the **Fixed rate
every** option selected. 9. Enter `90` in the first box, and select
**Days** from the drop-down list. 10. Perform the following actions in the **Select
targets** panel:

    1. Select `EC2 Image Builder` from the
     **Target** drop-down list.
    2. To apply the rule to an Image Builder pipeline, select the
     target pipeline from the **Image Pipeline**
     drop-down list.
    3. EventBridge needs permission to initiate a build for the
     selected pipeline. For this example, keep the default
     option to **Create a new role for this specific
     resource**.
    4. Choose **Add target**.

11. Choose **Create**

###### Note

To learn more about settings for rate expression rules that are
not covered in this example, see
[Rate
expressions](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-rate-expressions "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-rate-expressions") in the _Amazon EventBridge User Guide_.
