# Creating a scheduled rule (legacy) in Amazon EventBridge

###### Note

Scheduled rules are a legacy feature of EventBridge.

EventBridge
offers a more flexible and powerful way to create, run, and manage scheduled tasks
centrally, at scale: EventBridge Scheduler. With EventBridge Scheduler, you can create schedules using cron
and rate expressions for recurring patterns, or configure one-time invocations. You can set
up flexible time windows for delivery, define retry limits, and set the maximum retention
time for failed API invocations.

Scheduler is highly customizable, and offers improved scalability over scheduled rules, with a wider set of target API operations and AWS services.
We recommend that you use Scheduler to invoke targets on a schedule.

For more information, see [Create a schedule](using-eventbridge-scheduler.md#using-eventbridge-scheduler-create "using-eventbridge-scheduler.md#using-eventbridge-scheduler-create") or the _[EventBridge Scheduler User Guide](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md")_.

In EventBridge, you can create two types of scheduled rules:

- Rules that run at a regular rate

EventBridge runs these rules at regular intervals; for example, every 20 minutes.

To specify the rate for a scheduled rule, you define a _rate expression_.

- Rules that run at specific times

EventBridge runs these rules at specific times and dates; for example, 8:00 a.m. PST on the first Monday of every month.

To specify the time and dates a scheduled rule runs, you define a _cron expression_.
Rate expressions are simpler to define, while cron expressions offer detailed schedule
control. For example, with a cron expression, you can define a rule that runs at a specified
time on a certain day of each week or month. In contrast, rate expressions run a rule at a
regular rate, such as once every hour or once every day.

All scheduled events use UTC+0 time zone, and the minimum precision for a schedule is one
minute.

###### Note

EventBridge doesn't provide second-level precision in schedule expressions. The finest resolution
using a cron expression is one minute. Due to the distributed nature of EventBridge and the
target services, there can be a delay of several seconds between the time the scheduled
rule is triggered and the time the target service runs the target resource.

## Create a scheduled rule (legacy)

The following steps walk you through how to create an EventBridge rule that runs on a regular
schedule.

###### Note

You can only create scheduled rules using the default event bus.

###### Steps

- [Define the rule](#eb-create-scheduled-rule-define "#eb-create-scheduled-rule-define")
- [Define the schedule](#eb-create-scheduled-rule-schedule "#eb-create-scheduled-rule-schedule")
- [Select targets](#eb-create-scheduled-rule-target "#eb-create-scheduled-rule-target")
- [Configure tags and review rule](#eb-create-scheduled-rule-review "#eb-create-scheduled-rule-review")

### Define the rule

First, enter a name and description for your rule to identify it.

###### To define the rule detail

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, under **Scheduler**, choose **Scheduled rule (legacy)**.
3. Choose **Create scheduled rule**.
4. Enter a **Name** and, optionally, a
   **Description** for the rule.

A rule can't have the same name as another rule in the same AWS Region and
on the same event bus. 5. To have the rule take effect as soon as you create it, make sure the **Enable the
scheduled rule** option is enabled.

### Define the schedule

Next, define the schedule pattern.

###### To define the schedule pattern

- For **Schedule pattern**, choose whether you want the schedule to run at a specific time, or at a regular rate:

Specific time

    1. Choose **A fine-grained schedule that runs at a specific time, such as 8:00 a.m. PST on the first Monday of every month.**
    2. For **Cron expression**, specify fields to define the cron expresssion that EventBridge should use to determine when to execute this scheduled rule.


    Once you have specified all fields, EventBridge displays the
     next ten dates when EventBridge will execute this scheduled
     rule. You can choose whether to display those dates in
     **UTC** or **Local time
     zone**.


    For more information on constructing a cron expression, see [Cron expressions](eb-scheduled-rule-pattern.md#eb-cron-expressions "eb-scheduled-rule-pattern.md#eb-cron-expressions").

Regular rate

    1. Choose **A schedule that runs at a regular rate, such as every 10 minutes.**
    2. For **Rate expression**, specify the **Value** and **Unit** fields to define the rate at which EventBridge should execute this scheduled rule.


    For more information on constructing a rate expression, see [Rate expressions](eb-scheduled-rule-pattern.md#eb-rate-expressions "eb-scheduled-rule-pattern.md#eb-rate-expressions").

### Select targets

Choose one or more targets to receive events that match the specified pattern. Targets
can include an EventBridge event bus, EventBridge API destinations, including SaaS partners such as
Salesforce, or another AWS service.

###### To select targets

1. For **Target type**, choose one of the following
   target types:

Event bus
To select an EventBridge event bus, select **EventBridge event bus**, then do the following:

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

API destination
To use an EventBridge API destination, select **EventBridge API destination**, then do one of the following:

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

For more information, see [API destinations as targets in Amazon EventBridge](eb-api-destinations.md "eb-api-destinations.md").

AWS service
To use an AWS service, select **AWS service**,
then do the following:

    1. For **Select a target**, select an
     AWS service to use as the target. Provide the information
     requested for the service you select.


    ###### Note

    The fields displayed vary depending on the service selected. For more information about available targets, see
     [Event bus targets available in the EventBridge
     console](eb-targets.md#eb-console-targets "eb-targets.md#eb-console-targets").

2. For many target types,
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

3. (Optional) For **Additional settings**, specify any of the optional settings available for your target type:

Event bus
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

AWS service
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

4. (Optional) Choose **Add another target** to add another target for
   this rule.
5. Choose **Next**.

### Configure tags and review rule

Finally, enter any desired tags for the rule, then review and create the rule.

###### To configure tags, and review and create the rule

1. (Optional) Enter one or more tags for the rule. For more information, see
   [Tagging resources in Amazon EventBridge](eb-tagging.md "eb-tagging.md").
2. Choose **Next**.
3. Review the details for the new rule. To make changes to any section, choose
   the **Edit** button next to that section.

When satisfied with the rule details, choose **Create
rule**.
