# Creating rules in Amazon EventBridge

## Prerequisites

Before you begin, ensure you have:

- Access to the Amazon EventBridge console
- Appropriate IAM permissions to create EventBridge rules
- Basic understanding of event-driven architectures

## Overview

To take action on events received by EventBridge, you can create rules. When an event matches the event pattern defined in your rule, EventBridge sends the event to the specified target.

This topic walks you through creating a rule that EventBridge uses to match events as they are sent to the specified event bus.

Creating EventBridge rules involves four main steps:

1. Choose the events you want to process
2. Configure event filtering and testing
3. Select and configure targets
4. Configure the rule settings

## Choose the events

First, choose the events you want to send to the target.

###### To select an event

1.  Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2.  In the navigation pane, choose **Rules**, and then choose **Create Rule**.
3.  In the **Events** tab, find the events you want to send to the target:
    1. Choose **AWS Service Events** or **Custom Events**.
    2. Use the Search box or browse the event list to find the events you want to send to the target.
    3. Drag one or more events into the **Build** canvas and drop it on **Triggering Events**.EventBridge displays the **Triggering Events** section. This section includes:
    - **Events**, which lists the event you chose.
    - **Schema**, which displays the schema of the selected event, if available.

    **Schema** contains three tabs:

        + **Tree**: A tree view of the event schema.
        + **Code**: The event schema in Open API spec or JSON format.
        + **Info**: Overview information about the schema.

    - **Sample event**, which displays a sample of a selected event, if available.
    - **Event pattern (filter)**, which contains an event pattern that selects all events you've chosen.

## Filter events to send only what you want

You probably won't want to send _all_ events of a specific type to a target. You can make your event pattern more specific so that it only selects events that contain the attributes and values you're interested in.

### Edit the event pattern (optional)

In the **Triggering events** pane, you can build the event pattern two ways:

- Visually, using the **Schema** tree view
- By directly editing the JSON in the **Event pattern** pane

###### To edit the event pattern using the Schema tree view

1. Choose the **Tree** tab of the **Schema** pane.
2. Add and edit filters to build out the event pattern.
   1. Choose the filter icon next to the attribute you want to add as a filter to the event pattern.
   2. Choose a comparison operator from the drop-down list.

   For more information on comparison operators, see [Creating event patterns](eb-create-pattern-operators.md "eb-create-pattern-operators.md"). 3. Enter the value you want to match. 4. Click the check mark to finish.EventBridge adds the filter you've created to the JSON in the **Event pattern** pane.

3. Add additional filters until you've constructed an event pattern that matches on all the event attributes you want.

### Test the event pattern

After you construct an event pattern that matches all the event attributes you want, test to ensure the event pattern performs as expected.

#### Test the event pattern (optional)

1.  Choose a sample event for testing, or use your own.
    - **Use sample events provided**
      1. Choose **Use sample events provided**.
      2. Under **Sample triggering event**, select the event to use for testing from the drop-down list.

    - **Use your own event**
      1. Choose **Use your own event**.

      EventBridge displays a generic event with an empty `details` element. 2. Edit the event JSON to create the event against which you want to test your event pattern.

      ###### Tip

      You can use the sample events provided as starting points for creating your own custom events to use in your testing:

          1. Choose **Use sample events provided**, choose an event from the **Sample triggering event**, and then choose **Copy**.
          2. Choose **Use your own event**.
          3. Select the entire event in the window, and paste the sample event over it.
          4. Edit the event as desired.

2.  Choose **Run Test**.

EventBridge displays a message stating whether the test event matches the event pattern.

## Select targets

Drag one (and up to five) targets into the **Build** canvas and drop it on **Targets** to receive events that match the specified event pattern. Targets can include:

- Other EventBridge event buses, in the same or a different AWS account
- EventBridge API destinations, including SaaS partners such as Salesforce
- A range of AWS service resources, such as Amazon SQS queues or Amazon SNS topics

###### To select targets

1. Select the target type from the **Targets** pane, and drop it onto the **Targets** shape in the Build canvas.

EventBridge displays the **Target** section in the Build, with the applicable configuration options based on the type of target you selected.

###### Tip

If you have specified more than one target, selecting the target shape displays the configuration section for that target. 2. Configure the target based on your target type. For detailed configuration steps, see [EventBridge Targets](eb-targets.md "eb-targets.md").

### Customize the event data sent to the target

If you select a target other than an EventBridge event bus or EventBridge API destination, you have the option of customizing what data actually gets delivered to the target.

#### Transform or replace the event data sent (optional)

1. In the Build design canvas, choose the **Input transformation** icon in the **Targets** shape.

EventBridge displays the **Input transformation** section. 2. Under **Input transformation configuration**, choose **Enable**. 3. Select the Transformation method to choose how you want to customize the text sent to the target for matching events:

    * **Part of the matched events** – EventBridge only sends the specified portion of the original source event to the target.
    * **Constant (JSON text)** – EventBridge sends only the specified JSON text to the target. No part of the original source event is sent.
    * **Input transformer** – Configure an input transformer to customize the text you want EventBridge to send to the target. For more information, see [Transforming target input](eb-transform-target-input.md "eb-transform-target-input.md").

## Configure the rule

Finally, configure and create the rule.

###### To configure the rule (console)

1. Choose **Configure**.
2. Enter a **Name** and, optionally, a **Description** for the rule.

A rule can't have the same name as another rule in the same AWS Region and on the same event bus. 3. For **Event bus**, choose the event bus to associate with this rule.

If you want this rule to match events that come from your account, select **AWS default event bus**. When an AWS service in your account sends an event, it always goes to your account's default event bus. 4. To enable the rule as soon as it is created, under **Activation** enable **Active**. 5. (Optional) Enter one or more tags for the rule. For more information, see [Tagging resources in Amazon EventBridge](eb-tagging.md "eb-tagging.md"). 6. Choose **Create**.

## Next steps

After creating your rule, you can:

- [Monitor rule performance using metrics](eb-monitoring.md "eb-monitoring.md")
- [Test your rule with sample events](eb-event-pattern-sandbox.md "eb-event-pattern-sandbox.md")
- [Modify event patterns as needed](eb-event-patterns.md "eb-event-patterns.md")
- [Add additional targets to existing rules](eb-targets.md "eb-targets.md")

## Additional resources

For more information about EventBridge rules, see:

- [EventBridge rules overview](eb-rules.md "eb-rules.md")
- [Creating event patterns](eb-event-patterns.md "eb-event-patterns.md")
- [EventBridge targets](eb-targets.md "eb-targets.md")
- [Troubleshooting EventBridge rules](eb-troubleshooting.md "eb-troubleshooting.md")
