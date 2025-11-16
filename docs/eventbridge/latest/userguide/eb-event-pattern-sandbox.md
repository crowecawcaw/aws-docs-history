# Testing event patterns using the EventBridge Sandbox

Defining an event pattern is typically part of the larger process of [creating a new rule](eb-create-rule-visual.md "eb-create-rule-visual.md") or editing an existing one. Using
the Sandbox in EventBridge, however, you can quickly define an event pattern and use a sample event
to confirm the pattern matches the desired events, without having to create or edit a
rule. Once you've got your event pattern tested, EventBridge give you the option of creating a new rule using that event pattern directly from the sandbox.

For more information about event patterns, see [Amazon EventBridge event patterns](eb-event-patterns.md "eb-event-patterns.md").

###### Important

In EventBridge, it is possible to create rules that can lead to higher-than-expected charges
and throttling. For example, you can inadvertently create a rule that leads to an
infinite loop, where a rule is fired recursively without end. Suppose you created a rule
to detect that ACLs have changed on an Amazon S3 bucket, and trigger software to change them
to the desired state. If the rule is not written carefully, the subsequent change to the
ACLs fires the rule again, creating an infinite loop.

For guidance on how to write precise rules and event patterns to minimize such unexpected results,
see [Best practices for rules](eb-rules-best-practices.md "eb-rules-best-practices.md") and [Best practices](eb-patterns-best-practices.md "eb-patterns-best-practices.md").

###### To test an event pattern using the EventBridge sandbox

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Developer resources,** then select **Sandbox**,
   and on the **Sandbox** page choose the **Event pattern** tab.
3. For **Event source**, choose **AWS events or EventBridge
   partner events**.
4. (Optional) In the **Sample events** section, choose a
   **Sample event type** against which you want to test your event pattern.

The following sample event types are available:

    * **AWS events** – Select from events emitted
     from supported AWS services.
    * **EventBridge partner events** – Select from events
     emitted from third-party services that support EventBridge, such as
     Salesforce.
    * **Enter my own** – Enter your own event in
     JSON text.


    You can also use an AWS or partner event as the starting point for creating your own custom event.




    	1. Select **AWS events** or **EventBridge partner events**.
    	2. Use the **Sample events** dropdown to select the event you want to use as a starting point for your custom event.


    	EventBridge displays the sample event.
    	3. Select **Copy**.
    	4. Select **Enter my own** for **Event type.**
    	5. Delete the sample event structure in the JSON editing pane, and paste the AWS or partner event in its place.
    	6. Edit the event JSON to create your own sample event.

5. Choose a **Creation method**. You can create an event pattern
   from an EventBridge schema or template, or you can create a custom event
   pattern.

Existing schema
To use an existing EventBridge schema to create the event pattern, do
the following:

    1. In the **Creation method** section, for
     **Method**, select **Use
     schema**.
    2. In the **Event pattern** section, for
     **Schema type**, select
     **Select schema from Schema
     registry**.
    3. For **Schema registry**, choose the
     dropdown box and enter the name of a schema registry, such
     as `aws.events`. You can also select an option
     from the dropdown list that appears.
    4. For **Schema**, choose the dropdown box and
     enter the name of the schema to use. For example,
     `aws.s3@ObjectDeleted`. You can also select an
     option from the dropdown list that appears.
    5. In the **Models** section, choose the
     **Edit** button next to any attribute to
     open its properties. Set the **Relationship**
     and **Value** fields as needed, then choose
     **Set** to save the attribute.


    ###### Note

    For information about an attribute's definition,
     choose the **Info** icon next to the
     attribute's name. For a reference on how to set
     attribute properties in your event, open the
     **Note** section of the attribute
     properties dialog box.

    To delete an attribute's properties, choose the
     **Edit** button for that attribute,
     then choose **Clear**.
    6. Choose **Generate event pattern in JSON**
     to generate and validate your event pattern as JSON text.
    7. (Optional) To test the sample event against your test pattern, choose **Test pattern**.


    EventBridge displays a message box stating whether your sample event matches the event pattern.


    You can also choose any of the following options:




    	* **Copy** – Copy the event
    	 pattern to your device's clipboard.
    	* **Prettify** – Makes the
    	 JSON text easier to read by adding line breaks,
    	 tabs, and spaces.

Custom schema
To write a custom schema and convert it to an event pattern, do the
following:

    1. In the **Creation method** section, for
     **Method**, choose **Use
     schema**.
    2. In the **Event pattern** section, for
     **Schema type**, choose **Enter
     schema**.
    3. Enter your schema into the text box. You must format the
     schema as valid JSON text.
    4. In the **Models** section, choose the
     **Edit** button next to any attribute to
     open its properties. Set the **Relationship**
     and **Value** fields as needed, then choose
     **Set** to save the attribute.


    ###### Note

    For information about an attribute's definition,
     choose the **Info** icon next to the
     attribute's name. For a reference on how to set
     attribute properties in your event, open the
     **Note** section of the attribute
     properties dialog box.

    To delete an attribute's properties, choose the
     **Edit** button for that attribute,
     then choose **Clear**.
    5. Choose **Generate event pattern in JSON**
     to generate and validate your event pattern as JSON text.
    6. (Optional) To test the sample event against your test pattern, choose **Test pattern**.


    EventBridge displays a message box stating whether your sample event matches the event pattern.


    You can also choose any of the following options:




    	* **Copy** – Copy the event
    	 pattern to your device's clipboard.
    	* **Prettify** – Makes the
    	 JSON text easier to read by adding line breaks,
    	 tabs, and spaces.

Event pattern
To write a custom event pattern in JSON format, do the
following:

    1. In the **Creation method** section, for
     **Method**, choose **Custom pattern
     (JSON editor)**.
    2. For **Event pattern**, enter your custom
     event pattern in JSON-formatted text.
    3. (Optional) To test the sample event against your test pattern, choose **Test pattern**.


    EventBridge displays a message box stating whether your sample event matches the event pattern.


    You can also choose any of the following options:




    	* **Copy** – Copy the event
    	 pattern to your device's clipboard.
    	* **Prettify** – Makes the
    	 JSON text easier to read by adding line breaks,
    	 tabs, and spaces.
    	* **Event pattern form** –
    	 Opens the event pattern in Pattern Builder. If the
    	 pattern can't be rendered in Pattern Builder as-is,
    	 EventBridge warns you before it opens Pattern
    	 Builder.

6. (Optional) To create a rule with this event pattern, and assign the rule to a specific event bus, choose **Create rule with pattern**.

EventBridge takes you to **Step 1** of **Create rule**,
which you can use to create a rule and assign it to the event bus of your choice.

Note that **Step 2 - Build event pattern** contains the event
pattern information you've already specified, and which you can accept or update.

For more on how to create rules, see [Creating rules in Amazon EventBridge](eb-create-rule-visual.md "eb-create-rule-visual.md").
