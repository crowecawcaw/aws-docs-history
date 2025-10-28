# EventBridge rule

groups and templates for monitoring your AWS media workflow

CloudWatch uses Amazon EventBridge rules to send notifications. You begin by creating an event template
group. In that event template group, you create event templates that
determine what conditions create a notification and who is notified.

This section covers the creation of EventBridge rules using workflow monitor. For more
information about how the EventBridge service uses rules, see: [EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the _Amazon EventBridge User Guide_

## Creating

event template groups

Event template groups allow you to sort and classify events based on your use case.

###### To create an event template group

1. From the workflow monitor console's navigation pane, select **EventBridge rule
   templates**.
2. Select **Create event template group**.
3. Give the alarm template group a unique **Group name**
   and optional **Description**.
4. Select **Create**, You will be taken to the newly
   created alarm template group's details page.

## Creating event templates

You can send notifications based on event templates you create.

###### To create an event template

1. From the event template group's details page, select **Create
   event template**.
2. Give the event template a unique **Template
   name** and optional
   **Description**.
3. In the **Rule settings** section:
   1. Select an **Event type**. When selecting
      an event type, you can choose between several events
      created by AWS or select **Signal map active
      alarm** to use an alarm created by an alarm
      template.
   2. Select a **Target service**. This determines
      how you would like to be notified of this event. You can select
      Amazon Simple Notification Service or CloudWatch logs.
   3. After selecting a target service, select a
      **Target**. This will be a Amazon SNS topic or a
      CloudWatch log group, depending on your target service selection.

4. Select **Create** to complete the process.
