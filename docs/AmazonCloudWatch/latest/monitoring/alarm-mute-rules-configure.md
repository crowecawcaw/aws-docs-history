# Configure alarm mute rules

The steps in this section explain how to use the CloudWatch console to create an alarm mute rule. You can also use the API or AWS CLI to create an alarm mute rule. For more information, see [PutAlarmMuteRule](../APIReference/API_PutAlarmMuteRule.md "../APIReference/API_PutAlarmMuteRule.md").

###### To create an alarm mute rule

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, and then choose **Mute Rules** tab
3. Click **Create Alarm Mute Rule** button, which would open a wizard
4. Under **Alarm mute rule details** section, enter a name and optional description for your alarm mute rule
5. Under **Schedule pattern** section, choose one time or recurring schedule
   1. If you choose one-time occurrence,
      1. Select the Timezone to apply the mute schedules
      2. Choose a start date and time, to define when the mute rule should become active
      3. Choose end date and time, to define when the mute rule should expire

   2. If you choose Recurring schedule, you will have two options. Either to use the Console form or use cron expression to configure the recurring time schedules.
      1. Under **Schedule creation type** choose "Specify date, time and recurrence" to use the Console form
         1. Choose the Timezone to apply the mute rule
         2. Choose **Start date and time**, to define when the mute rule should become active
         3. Choose **Duration**, to define how long the mute rule should last once becomes active
         4. Choose **Repeat**, to define how the schedule should repeat like every day, every month, every weekend or on specific days during the week.
         5. Choose optional **Until**, to define when the mute schedule should expire. Default option is "Indefinitely"

      2. Under **Schedule creation type** choose "Set from a cron expression" to configure schedules using cron expressions
         1. Under **Cron expression** section enter the desired cron expression values.
         2. Choose **Duration**, to define how long the mute rule should last once becomes active
         3. Under optional **Timeframe** section, enter optional start and end date and time to define when the mute schedule should become active and expire.

6. Under **Target alarms** section, choose the alarms from the drop down to which you want to apply this mute rule
7. Under **Set tags for your mute rule** section, attach tags to your alarm mute rule. A tag is a key-value pair applied to a resource to hold metadata about that resource. For more information see [What are tags?](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md")
8. Select **Create alarm mute rule** button to create the mute rule

## Quick mutes

Alarms could be added for a short time period as follows,

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**
3. Select the alarms that you want to mute from the list
4. Under **Actions** menu choose **Mute**
5. Under the **Quick mute** section choose the predefined time periods 15min, 1h, 3h or select **Mute until** to set desired time period
6. Click **Confirm** to mute the alarms immediately until the chosen time period

## Add alarms to existing mute rules

Alarms could be added to existing mute rules as follows,

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**
3. Select the alarms that you want to mute from the list
4. Under **Actions** menu choose **Mute**
5. Choose **Apply existing mute rules**, which should open a wizard
6. Select the mute rules from the drop down to which you want to add the alarms
7. Click **Apply**

###### Note

Quick mute and adding an alarm to existing mute rules options are also available from the alarm details page. **Mute rules** tab in the details page displays all mute rules associated with the alarm.
