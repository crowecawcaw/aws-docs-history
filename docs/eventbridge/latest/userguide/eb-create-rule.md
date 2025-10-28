# Creating rules that react to events in Amazon EventBridge

To take action on events received by Amazon EventBridge, you can
create [rules](eb-rules.md "eb-rules.md"). When an event matches the [event pattern](eb-event-patterns.md "eb-event-patterns.md") defined in your rule, EventBridge sends the
event to the specified [target](eb-targets.md "eb-targets.md") and triggers the action
defined in the rule.

The following video explores creating different kinds of
rules, and how to test them:

The following steps walk you through how to create a rule that EventBridge uses to match events as they are sent to the specified event bus.

###### Steps

- [Define the rule](#eb-create-rule-define "#eb-create-rule-define")
- [Build the event pattern](#eb-create-rule-event-pattern "#eb-create-rule-event-pattern")
- [Select targets](#eb-create-rule-target "#eb-create-rule-target")
- [Configure tags and review rule](#eb-create-rule-review "#eb-create-rule-review")

## Define the rule

First, enter a name and description for your rule to identify it. You must also define
the event bus where your rule looks for events to match to an event pattern.

###### To define the rule detail

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a **Name** and, optionally, a
   **Description** for the rule.

A rule can't have the same name as another rule in the same AWS Region and
on the same event bus. 5. For **Event bus**, choose the event bus to associate with
this rule. If you want this rule to match events that come from your account,
select **AWS default event bus**. When an AWS service in
your account emits an event, it always goes to your account’s default event
bus. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**.

## Build the event pattern

Next, build the event pattern. To do this, specify the event source, choose the basis
for the event pattern, and define the attributes and values to match on. You can also
generate the event pattern in JSON and test it against a sample event.

###### To build the event pattern

1. For **Event source**, choose **AWS events or EventBridge
   partner events**.
2. (Optional) In the **Sample events** section, choose a
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

3. Choose a **Creation method**. You can create an event pattern
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

4. Choose **Next**.

## Select targets

Choose one or more targets to receive events that match the specified pattern. Targets
can include an EventBridge event bus, EventBridge API destinations, including SaaS partners such as
Salesforce, or another AWS service.

###### To select targets

1. For **Target type**, choose one of the following
   target types:

Event bus

    1. Select **EventBridge event bus**.
    2. Choose the event bus to use as the target.




    	* To use an event bus in the same AWS Region as this rule:





    		1. Select **Event bus in the same account and
    		 Region**.
    		2. For **Event bus for
    		 target**, choose the dropdown box and enter the
    		 name of the event bus. You can also select the event bus from the
    		 dropdown list.


    		For more information, see [Sending events between event buses in
    		 the same account and Region in Amazon EventBridge](eb-bus-to-bus.md "eb-bus-to-bus.md").
    	* To use an event bus in a different AWS Region or account as this rule:




    		1. Select **Event bus in a different account or Region**.
    		2. For **Event bus as target**, enter the ARN of the event bus you want to use.


    		For more information, see:





    			+ [Sending and receiving events between AWS accounts in Amazon EventBridge](eb-cross-account.md "eb-cross-account.md")
    			+ [Sending and receiving events between AWS Regions in Amazon EventBridge](eb-cross-region.md "eb-cross-region.md")
    3. For many target types,
     EventBridge needs permissions to send events to the target.
     In these cases, EventBridge can create the IAM role needed for your rule to run.


    For **Execution role**, do one of the following:




    	* To create a new execution role for this rule:




    		1. Select **Create
    		 a new role for this specific resource**.
    		2. Either enter
    		 a name for this execution role, or use the name generated by
    		 EventBridge.
    	* To use an existing execution role for this rule:




    		1. Select **Use existing role**.
    		2. Enter or select the name of the execution role to use
    		 from the dropdown list.
    4. (Optional) For **Additional settings**, specify any of the optional settings available for your target type:


    (Optional) For **Dead-letter queue**, choose whether to use a standard
     Amazon SQS queue as a dead-letter queue. EventBridge sends events that match this rule to
     the dead-letter queue if they are not successfully delivered to the target. Do
     one of the following:




    	* Choose **None** to not use a dead-letter
    	 queue.
    	* Choose **Select an Amazon SQS queue in the current AWS
    	 account to use as the dead-letter queue** and then select
    	 the queue to use from the drop-down list.
    	* Choose **Select an Amazon SQS queue in an other AWS
    	 account as a dead-letter queue** and then enter
    	 the ARN of the queue to use. You must attach a
    	 resource-based policy to the queue that grants EventBridge
    	 permission to send messages to it.


    	For more information, see [Granting permissions to the dead-letter queue](eb-rule-dlq.md#eb-dlq-perms "eb-rule-dlq.md#eb-dlq-perms").

API destination

    1. Select **EventBridge API destination**.
    2. Choose a new or existing API destination:




    	* To use an existing API destination, select **Use an existing API destination**. Then select an API destination from
    	 the dropdown list.
    	* To create a new API destination, select **Create a new
    	 API destination**. Then, provide the following
    	 details for the destination:




    		+ **Name** – Enter a name for
    		 the destination.


    		Names must be unique within your
    		 AWS account. Names can have up to 64 characters. Valid
    		 characters are **A-Z**,
    		 **a-z**, **0-9**, and **.**
    		**\_**
    		**-** (hyphen).
    		+ (Optional) **Description** –
    		 Enter a description for the destination.


    		Descriptions
    		 can have up to 512 characters.
    		+ **API destination endpoint** –
    		 The URL endpoint for the target.


    		The endpoint URL must
    		 start with `https`. You can include
    		 the `*` as a path parameter
    		 wildcard. You can set path parameters from the target's
    		 `HttpParameters` attribute.
    		+ **HTTP method** – Select the
    		 HTTP method used when you invoke the endpoint.
    		+ (Optional) **Invocation rate limit per
    		 second** – Enter the maximum number
    		 of invocations accepted for each second for this
    		 destination.


    		This value must be greater than zero. By
    		 default, this value is set to 300.
    		+ **Connection** – Choose to use a new or existing connection:





    			- To use an
    			 existing connection, select **Use an existing
    			 connection** and select the connection from
    			 the dropdown list.
    			- To create a new connection for this
    			 destination select **Create a new
    			 connection**, then define the connection's
    			 **Name**, **Destination
    			 type**, and **Authorization
    			 type**. You can also add an optional
    			 **Description** for this
    			 connection.
    3. For many target types,
     EventBridge needs permissions to send events to the target.
     In these cases, EventBridge can create the IAM role needed for your rule to run.


    For **Execution role**, do one of the following:




    	* To create a new execution role for this rule:




    		1. Select **Create
    		 a new role for this specific resource**.
    		2. Either enter
    		 a name for this execution role, or use the name generated by
    		 EventBridge.
    	* To use an existing execution role for this rule:




    		1. Select **Use existing role**.
    		2. Enter or select the name of the execution role to use
    		 from the dropdown list.
    4. (Optional) For **Additional settings**, specify any of the optional settings available for your target type:


    Note that EventBridge may not display all of the following fields for a given AWS service.




    	1. (Optional) For Configure target input, choose how you want to customize the text
    	 sent to the target for matching events. Choose one of the following:




    		* **Matched events** – EventBridge sends the entire
    		 original source event to the target. This is the default.
    		* **Part of the matched events** – EventBridge only sends
    		 the specified portion of the original source event to the target.


    		Under **Specify the part of the matched event**, specify
    		 a JSON path that defines the part of the event you want EventBridge to send to the
    		 target.
    		* **Constant (JSON text)** – EventBridge sends only the
    		 specified JSON text to the target. No part of the original source event is
    		 sent.


    		Under **Specify the constant in JSON**, specify the JSON
    		 text that you want EventBridge to send to the target instead of the event.
    		* **Input transformer** – Configure an input
    		 transformer to customize the text you want EventBridge send to the target. For more
    		 information, see [Amazon EventBridge input transformation](eb-transform-target-input.md "eb-transform-target-input.md").




    			1. Select **Configure input transformer**.
    			2. Configure the input transformer following the steps in [Configuring an input transformer when creating a rule in EventBridge](eb-transform-input-rule.md "eb-transform-input-rule.md").
    	2. (Optional) Under **Retry policy**,
    	 specify how EventBridge should retry sending an event to a target
    	 after an error occurs.




    		* **Maximum age of event** –
    		 Enter the maximum amount of time (in hours, minutes,
    		 and seconds) for EventBridge to retain unprocessed events.
    		 The default is 24 hours.
    		* **Retry attempts** – Enter
    		 the maximum number of times EventBridge should retry
    		 sending an event to the target after an error
    		 occurs. The default is 185 times.
    	3. (Optional) For **Dead-letter queue**,
    	 choose whether to use a standard Amazon SQS queue as a
    	 dead-letter queue. EventBridge sends events that match this rule to
    	 the dead-letter queue if they are not successfully delivered
    	 to the target. Do one of the following:




    		* Choose **None** to not use a
    		 dead-letter queue.
    		* Choose **Select an Amazon SQS queue in the
    		 current AWS account to use as the dead-letter
    		 queue** and then select the queue to use
    		 from the drop-down list.
    		* Choose **Select an Amazon SQS queue in an other
    		 AWS account as a dead-letter queue**
    		 and then enter the ARN of the queue to use. You must
    		 attach a resource-based policy to the queue that
    		 grants EventBridge permission to send messages to it.


    		For more information, see [Granting permissions to the dead-letter queue](eb-rule-dlq.md#eb-dlq-perms "eb-rule-dlq.md#eb-dlq-perms").

For more information, see [API destinations as targets in Amazon EventBridge](eb-api-destinations.md "eb-api-destinations.md").

AWS service

    1. Select **AWS service**.
    2. For **Select a target**, select an
     AWS service to use as the target.
    3. If you choose an AWS service that supports cross-account targets, you can select a target in the same account as the event bus, or a different account.




    	* For a target in the same account, for **Target type** select **Target in this account**.




    		1. Provide the information
    		 requested for the service you select.


    		###### Note

    		The fields displayed vary depending on the service selected. For more information about available targets, see
    		 [Event bus targets available in the EventBridge
    		 console](eb-targets.md#eb-console-targets "eb-targets.md#eb-console-targets").
    		2. For many target types,
    		 EventBridge needs permissions to send events to the target.
    		 In these cases, EventBridge can create the IAM role needed for your rule to run.


    		For **Execution role**, do one of the following:




    			+ To create a new execution role for this rule:




    				1. Select **Create
    				 a new role for this specific resource**.
    				2. Either enter
    				 a name for this execution role, or use the name generated by
    				 EventBridge.
    			+ To use an existing execution role for this rule:




    				1. Select **Use existing role**.
    				2. Enter or select the name of the execution role to use
    				 from the dropdown list.
    	* For a target in a different account, for **Target type** select **Target in another AWS account**.




    		1. Enter the ARN of the target resource to which you want to send events.
    		2. Provide any additional information
    		 requested for the service you select.
    		3. Select the name of the execution role to use
    		 from the dropdown list.
    4. (Optional) For **Additional settings**, specify any of the optional settings available for your target type:




    	1. (Optional) For Configure target input, choose how you want to customize the text
    	 sent to the target for matching events. Choose one of the following:




    		* **Matched events** – EventBridge sends the entire
    		 original source event to the target. This is the default.
    		* **Part of the matched events** – EventBridge only sends
    		 the specified portion of the original source event to the target.


    		Under **Specify the part of the matched event**, specify
    		 a JSON path that defines the part of the event you want EventBridge to send to the
    		 target.
    		* **Constant (JSON text)** – EventBridge sends only the
    		 specified JSON text to the target. No part of the original source event is
    		 sent.


    		Under **Specify the constant in JSON**, specify the JSON
    		 text that you want EventBridge to send to the target instead of the event.
    		* **Input transformer** – Configure an input
    		 transformer to customize the text you want EventBridge send to the target. For more
    		 information, see [Amazon EventBridge input transformation](eb-transform-target-input.md "eb-transform-target-input.md").




    			1. Select **Configure input transformer**.
    			2. Configure the input transformer following the steps in [Configuring an input transformer when creating a rule in EventBridge](eb-transform-input-rule.md "eb-transform-input-rule.md").
    	2. (Optional) Under **Retry policy**,
    	 specify how EventBridge should retry sending an event to a target
    	 after an error occurs.




    		* **Maximum age of event** –
    		 Enter the maximum amount of time (in hours, minutes,
    		 and seconds) for EventBridge to retain unprocessed events.
    		 The default is 24 hours.
    		* **Retry attempts** – Enter
    		 the maximum number of times EventBridge should retry
    		 sending an event to the target after an error
    		 occurs. The default is 185 times.
    	3. (Optional) For **Dead-letter queue**,
    	 choose whether to use a standard Amazon SQS queue as a
    	 dead-letter queue. EventBridge sends events that match this rule to
    	 the dead-letter queue if they are not successfully delivered
    	 to the target. Do one of the following:




    		* Choose **None** to not use a
    		 dead-letter queue.
    		* Choose **Select an Amazon SQS queue in the
    		 current AWS account to use as the dead-letter
    		 queue** and then select the queue to use
    		 from the drop-down list.
    		* Choose **Select an Amazon SQS queue in an other
    		 AWS account as a dead-letter queue**
    		 and then enter the ARN of the queue to use. You must
    		 attach a resource-based policy to the queue that
    		 grants EventBridge permission to send messages to it.


    		For more information, see [Granting permissions to the dead-letter queue](eb-rule-dlq.md#eb-dlq-perms "eb-rule-dlq.md#eb-dlq-perms").

2. (Optional) Choose **Add another target** to add another target for
   this rule.
3. Choose **Next**.

## Configure tags and review rule

Finally, enter any desired tags for the rule, then review and create the rule.

###### To configure tags, and review and create the rule

1. (Optional) Enter one or more tags for the rule. For more information, see
   [Tagging resources in Amazon EventBridge](eb-tagging.md "eb-tagging.md").
2. Choose **Next**.
3. Review the details for the new rule. To make changes to any section, choose
   the **Edit** button next to that section.

When satisfied with the rule details, choose **Create
rule**.
