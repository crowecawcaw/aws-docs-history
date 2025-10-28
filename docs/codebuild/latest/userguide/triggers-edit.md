# Edit AWS CodeBuild triggers

You can edit a trigger on a project to schedule a build once every hour, day, or week.
You can also edit a trigger to use a custom rule with an Amazon CloudWatch cron expression. For
example, using a cron expression, you can schedule a build at a specific time on every
weekday. For information about creating a trigger, see [Create AWS CodeBuild triggers](build-triggers.md#trigger-create "build-triggers.md#trigger-create").

###### Topics

- [Edit AWS CodeBuild triggers (console)](#triggers-edit-console "#triggers-edit-console")
- [Edit AWS CodeBuild triggers programmatically](#trigger-edit-code "#trigger-edit-code")

## Edit AWS CodeBuild triggers (console)

Use the following procedure to edit triggers using the AWS Management Console.

###### To edit a trigger

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. In the navigation pane, choose **Build projects**.
3. Choose the link for the build project you want to change, and then choose the
   **Build triggers** tab.

###### Note

By default, the 100 most recent build projects are displayed. To view
more build projects, choose the gear icon, and then choose a different value for **Projects per
page** or use the back and forward arrows. 4. Choose the radio button next to the trigger you want to change, and then
choose **Edit**. 5. From the **Frequency** drop-down list, choose the frequency for your trigger.
If you want to create a frequency using a cron expression, choose **Custom**. 6. Specify the parameters for the frequency of your trigger. You can enter the first few characters of your
selections in the text box to filter drop-down menu items.

###### Note

Start hours and minutes are zero-based. The start minute is a number between
zero and 59. The start hour is a number between zero and 23. For example, a daily trigger that starts every day
at 12:15 P.M. has a start hour of 12 and a start minute of 15. A daily trigger that starts every day at midnight
has a start hour of zero and a start minute of zero. A daily trigger that starts every day at
11:59 P.M. has a start hour of 23 and a start minute of 59.

| Frequency | Required Parameters               | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hourly    | Start minute                      | Use the **Start minute** drop-down menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Daily     | Start minute Start hour           | Use the **Start minute** drop-down menu. Use the **Start hour** drop-down menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Weekly    | Start minute Start hour Start day | Use the **Start minute** drop-down menu. Use the **Start hour** drop-down menu. Use the **Start day** drop-down menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Custom    | Cron expression                   | Enter a cron expression in **Cron expression**. A cron expression has six required fields that are separated by white space. The fields specify a start value for minute, hour, day of month, month, day of week, and year. You can use wildcards to specify a range, additional values, and more. For example, the cron expression `0 9 ? * MON-FRI *` schedules a build every weekday at 9:00 A.M. For more information, see [Cron Expressions](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions") in the _Amazon CloudWatch Events User Guide_. | 7. Select **Enable this trigger**. ###### Note You can use the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/") to edit source version, timeout, and other options that are not available in AWS CodeBuild. ## Edit AWS CodeBuild triggers programmatically CodeBuild uses Amazon EventBridge rules for build triggers. You can use the EventBridge API to programmatically edit the build triggers for your CodeBuild projects. See [Amazon EventBridge API Reference](../../../eventbridge/latest/APIReference.md "../../../eventbridge/latest/APIReference.md") for more information. |
