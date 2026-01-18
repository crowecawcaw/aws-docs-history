# Run Configuration Checks

Use the following steps to evaluate the SAP configuration of a Systems Manager for SAP application, which is either of type SAP HANA or SAP ABAP.

See also [support restrictions for Systems Manager for SAP](supported-versions.md "supported-versions.md").

###### Topics

- [To access configuration checks](#access-configuration-checks "#access-configuration-checks")
- [To evaluate configuration checks](#evaluate-configuration-checks "#evaluate-configuration-checks")
- [To view and analyze check results](#view-analyze-check-results "#view-analyze-check-results")
- [Schedule Configuration Checks using AWS EventBridge Scheduler console](#schedule-configuration-checks-eventbridge "#schedule-configuration-checks-eventbridge")

## To access configuration checks

1. Open the AWS Systems Manager console at https://console.aws.amazon.com/systems-manager/
2. In the navigation pane, choose **Application Tools**, then choose **Application Manager**
3. From the list of registered applications, choose the SAP application you want to evaluate
4. Choose **Actions**, then choose **SAP Configuration Checks**

## To evaluate configuration checks

1. Select one or more checks you want to evaluate
2. Choose **Run**
3. Monitor the task status using either the operation ID provided in the notification banner or by choosing **Actions** > **View operations**

## To view and analyze check results

1. Select a single check to view its details
2. Expand individual subchecks to see detailed rules
3. Sort subchecks by Rule Status, Description, or Component
4. Filter results by rule status using the status totals or the filter box
5. Clear filters by selecting the cancel indicator
6. View previous results by selecting a different evaluation date from the dropdown list
7. Access additional information through the provided Documentation links

## Schedule Configuration Checks using AWS EventBridge Scheduler console

1. Sign in to the AWS Management Console, then choose the following link to open the EventBridge Scheduler section of the EventBridge console: https://console.aws.amazon.com/scheduler/home . You can switch your AWS Region by using the AWS Management Console’s Region selector.
2. On the **Schedules** page, choose **Create schedule**.
3. On the **Specify schedule detail** page, in the **Schedule name and description** section, do the following:
   1. For **Schedule name**, enter a name for your schedule. For example, `SAPConfigurationChecksSchedule`
   2. For **Description - optional**, enter a description for your schedule.
   3. For **Schedule group**, choose a schedule group from the drop down options. If you haven’t previously made any schedule groups, you can choose the `default` group for your schedule. To create a new schedule group, choose the **create your own schedule** link in the console description. You use schedule groups to add tags to groups of schedules.

4. In the **Schedule pattern** section, do the following:
   1. For **Occurrence**, choose one of the following pattern options. The configuration options change depending on which pattern that you select.
      1. **One-time schedule** – A one-time schedule invokes a target only once at the date and time that you specify. For **Date and time**, enter a valid date in `YYYY/MM/DD` format. Then, specify a timestamp in 24-hour `hh:mm` format. Finally, choose a timezone from the drop down options.
      2. **Recurring schedule** – A recurring schedule invokes a target at a rate that you specify using a **cron** expression or rate expression. Choose **Cron-based schedule** to configure a schedule by using a **cron** expression. To use a rate expression, choose **Rate-based schedule** and enter a positive number for **Value**, then choose a **Unit** from the drop down options.

      For more information on using cron and rate expressions, see [Schedule types in EventBridge Scheduler](../../../scheduler/latest/UserGuide/schedule-types.md "../../../scheduler/latest/UserGuide/schedule-types.md").

   2. For **Flexible time window**, choose **Off** to turn off the option, or choose one of the pre-defined time windows from the drop down list. For example, if you choose **15 minutes** and you set a recurring schedule to invoke its target once every hour, the schedule runs within 15 minutes after the start of every hour.

5. If you chose **Recurring schedule** in the previous step, in the **Timeframe** section, specify a timezone, and optionally set a start date and time, and an end date and time for the schedule. A recurring schedule without a start date will begin as soon as it is created and available. A recurring schedules without an end date will continue to invoke it’s target indefinitely.
6. Choose **Next**.
7. On the **Select target** page, do the following:
   1. Select **All APIs** option, and Find service "Systems Manager for SAP" from the search box.
   2. Find the **Target** action "StartConfigurationChecks" and provide the json payload based on the [StartConfigurationChecks API](../../../ssmsap/latest/APIReference/API_StartConfigurationChecks.md "../../../ssmsap/latest/APIReference/API_StartConfigurationChecks.md") action (ApplicationId string input, and optionally, ConfigurationCheckIds array string)

8. Choose **Next**, then on the **Settings - optional** page, follow the steps described in [EventBridge console Getting Started guide](../../../scheduler/latest/UserGuide/getting-started.md#getting-started-console "../../../scheduler/latest/UserGuide/getting-started.md#getting-started-console") (Step 9 onwards), to change the default settings of the desired schedule.
9. In the Permissions section, in order for the Scheduler to execute the StartConfigurationCheck operation successfully, an IAM role needs to be created with the AWSSystemsManagerForSAPFullAccess managed policy, using the steps below:
   1. In the AWS IAM Console, Create a new role, using a “Custom trust Policy“, and the following trust relationship:

   ```
    {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "scheduler.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

   2. On the Next page, Add Permissions by searching for and selecting the AWSSystemsManagerForSAPFullAccess managed policy
   3. Next, provide the Role name and Description, (and tags if any), before creating the role for the scheduler.
   4. Select this new Role in the Permissions section of the schedule on the AWS EventBridge Console, while creating the schedule

10. Choose **Create schedule** to finish creating your new schedule. You can view a list of your new and existing schedules on the **Schedules** page. Under the **Status** column, verify that your new schedule is **Enabled**.
11. To verify that your schedule invokes the Systems Manager for SAP service’s StartConfigurationChecks target, follow the steps listed at [To view and analyze check results](#view-analyze-check-results "#view-analyze-check-results").
