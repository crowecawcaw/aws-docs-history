

# Configure alarm mute rules
<a name="alarm-mute-rules-configure"></a>

 The steps in this section explain how to use the CloudWatch console to create an alarm mute rule. You can also use the API or AWS CLI to create an alarm mute rule. For more information, see [PutAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutAlarmMuteRule.html). 

**To create an alarm mute rule**

1.  Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/). 

1.  In the navigation pane, choose **Alarms**, and then choose **Mute Rules** tab 

1.  Click **Create Alarm Mute Rule** button, which would open a wizard 

1.  Under **Alarm mute rule details** section, enter a name and optional description for your alarm mute rule 

1.  Under **Schedule pattern** section, choose one time or recurring schedule 

   1.  If you choose one-time occurrence, 

      1.  Select the Timezone to apply the mute schedules 

      1.  Choose a start date and time, to define when the mute rule should become active 

      1.  Choose end date and time, to define when the mute rule should expire 

   1.  If you choose Recurring schedule, you will have two options. Either to use the Console form or use cron expression to configure the recurring time schedules. 

      1.  Under **Schedule creation type** choose "Specify date, time and recurrence" to use the Console form 

         1.  Choose the Timezone to apply the mute rule 

         1.  Choose **Start date and time**, to define when the mute rule should become active 

         1.  Choose **Duration**, to define how long the mute rule should last once becomes active 

         1.  Choose **Repeat**, to define how the schedule should repeat like every day, every month, every weekend or on specific days during the week. 

         1.  Choose optional **Until**, to define when the mute schedule should expire. Default option is "Indefinitely" 

      1.  Under **Schedule creation type** choose "Set from a cron expression" to configure schedules using cron expressions 

         1.  Under **Cron expression** section enter the desired cron expression values. 

         1.  Choose **Duration**, to define how long the mute rule should last once becomes active 

         1.  Under optional **Timeframe** section, enter optional start and end date and time to define when the mute schedule should become active and expire. 

1.  Under **Target alarms** section, choose the alarms from the drop down to which you want to apply this mute rule 

1.  Under **Set tags for your mute rule** section, attach tags to your alarm mute rule. A tag is a key-value pair applied to a resource to hold metadata about that resource. For more information see [What are tags?](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html) 

1.  Select **Create alarm mute rule** button to create the mute rule 

## Quick mutes
<a name="quick-mutes"></a>

 Alarms could be added for a short time period as follows, 

1.  Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/). 

1.  In the navigation pane, choose **Alarms** 

1.  Select the alarms that you want to mute from the list 

1.  Under **Actions** menu choose **Mute** 

1.  Under the **Quick mute** section choose the predefined time periods 15min, 1h, 3h or select **Mute until** to set desired time period 

1.  Click **Confirm** to mute the alarms immediately until the chosen time period 

## Add alarms to existing mute rules
<a name="add-alarms-to-existing-rules"></a>

 Alarms could be added to existing mute rules as follows, 

1.  Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/). 

1.  In the navigation pane, choose **Alarms** 

1.  Select the alarms that you want to mute from the list 

1.  Under **Actions** menu choose **Mute** 

1.  Choose **Apply existing mute rules**, which should open a wizard 

1.  Select the mute rules from the drop down to which you want to add the alarms 

1.  Click **Apply** 

**Note**  
 Quick mute and adding an alarm to existing mute rules options are also available from the alarm details page. **Mute rules** tab in the details page displays all mute rules associated with the alarm. 