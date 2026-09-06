

# Set up scheduling notifications in Connect Customer
<a name="scheduling-notifications"></a>

You can create rules that automatically send notifications when schedule changes occur. These rules use the Rules engine and are configured under the **Scheduling** category. You can set up notifications for three types of scheduling events.

The following list describes the notification event types:

New schedule is published  
Triggers when a scheduler publishes a schedule. You can target specific forecast groups, staffing groups, or agents.

Published schedule is updated  
Triggers when a published schedule is modified, such as when shifts are added, removed, edited, copied, or replaced. You can target specific forecast groups, staffing groups, agents, or shift activities. At least one of forecast group, staffing group, agents, or shift activities is required.

Time-off request status is updated  
Triggers when a time-off request is created or its status changes. You can target specific forecast groups, staffing groups, agents, or time-off activities. At least one of forecast group, staffing group, agents, or time-off activities is required.

When a rule is triggered, it can perform one of the following actions:
+ Send an email notification
+ Create a task in Connect Customer
+ Generate an event

For email notifications, you can configure the following recipient types:
+ Supervisors of agents affected by the scheduling change
+ The specific agents whose schedules were affected
+ Manually selected users

You can also exclude specific supervisors or agents from receiving notifications.

**To create a scheduling notification rule**

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Scheduling**, **Schedule manager - Edit** and **Rules**. For more information, see [Assign permissions](required-optimization-permissions.md).

1. On the navigation menu, choose **Analytics and optimization**, **Rules**.

1. Choose **Create a rule**, and then select **Scheduling**.

1. For **Event source**, choose one of the following: **New schedule is published**, **Published schedule is updated**, or **Time-off request status is updated**.

1. Configure the conditions for the rule. Depending on the event source, you can specify forecast groups, staffing groups, agents, shift activities, or time-off activities.

1. Under **Actions**, choose the action to perform when the rule is triggered: **Send email notification**, **Create task**, or **Generate an EventBridge event**.

1. If you chose **Send email notification**, configure the recipients. You can choose **Supervisors**, **Agents**, or select specific users. Optionally, exclude specific supervisors or agents.

1. Choose **Save** to save the rule as a draft, or **Save and publish** to activate it.