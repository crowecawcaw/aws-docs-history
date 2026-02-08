# Alarm Mute Rules

Alarm Mute Rules is a CloudWatch feature that provides you a mechanism to automatically mute alarm actions during predefined time windows. When you create a mute rule, you define specific time periods and target alarms whose actions will be muted. CloudWatch will continue monitoring and evaluating alarm states while preventing unwanted notifications or automated alarm actions during expected operational events.

Alarm Mute Rules help you manage critical operational scenarios where alarm actions would be unnecessary or disruptive. For example, during planned maintenance windows, you can prevent automated alarm actions while your systems are intentionally offline or experiencing expected issues, allowing you to perform maintenance without interruptions. For operations during non-business hours such as weekends or holidays, you can mute non-critical alarm actions when immediate response is not required, reducing alarm noise and unnecessary notifications to your operations team. In testing environments, mute rules allow you to temporarily mute alarm actions during scenarios such as load testing where high resource usage or error rates are expected and don't require immediate attention. When your team is actively troubleshooting issues, mute rules allow you to prevent duplicate alarm actions from being triggered, helping you focus on resolution without being distracted by redundant alarm notifications.

## Defining alarm mute rules

Alarm mute rules can be defined using: **rules** and **targets**.

- **Rules** - define the time windows when alarm actions should be muted. Rules are composed of three attributes:
  - **Expression** – Defines when the mute period begins and how it repeats. You can use two types of expressions:
    - **Cron expressions** – Use standard cron syntax to create recurring mute windows. This approach is ideal for regular maintenance schedules, such as weekly system updates or daily backup operations. Cron expressions allow you to specify complex recurring patterns, including specific days of the week, months, or times.

    _Syntax for cron expression_

    ```

    ┌───────────── minute (0 - 59)
    │ ┌───────────── hour (0 - 23)
    │ │ ┌───────────── day of the month (1 - 31)
    │ │ │ ┌───────────── month (1 - 12) (or JAN-DEC)
    │ │ │ │ ┌───────────── day of the week (0 - 6) (0 or 7 is Sunday, or MON-SUN)
    │ │ │ │ │
    │ │ │ │ │
    * * * * *

    ```

        * The characters `*`, `,`, `-` will be supported in all fields.
        * English names can be used for the `month` (JAN-DEC) and `day of week` (SUN-SAT) fields

    - **At expressions** – Use at expressions for one-time mute windows. This approach works well for planned operational events that occur once at a known time.

    ```

    Syntax: `at(yyyy-MM-ddThh:mm)`

    ```

  - **Duration** – Specifies how long the mute rule lasts once activated. Duration must be specified in ISO-8601 format with a minimum of 1 minute (PT1M) and maximum of 15 days (P15D).
  - **Timezone** – Specifies the timezone in which the mute window will be applied according to the expressions, using standard timezone identifiers such as "America/Los_Angeles" or "Europe/London".

- **Targets** - specify the list of alarm names whose actions will be muted during the defined time windows. You can include both metric alarms and composite alarms in your target list.

You can optionally include start and end timestamps to provide additional boundaries for your mute windows. Start timestamps ensure that mute rules don't activate before a specific date and time, while end timestamps prevent rules from being applied beyond the specified date and time.

For more information about creating alarm mute rules programmatically, see [PutAlarmMuteRule](../APIReference/API_PutAlarmMuteRule.md "../APIReference/API_PutAlarmMuteRule.md").

###### Note

- The targeted alarms must be present in the same AWS account and same AWS Region in which the mute rule is created.
- A single alarm mute rule can target up to 100 alarms by alarm names.

The CloudWatch console includes a dedicated "Alarm Mute Rules" tab that provides centralized management of all your mute rules within your AWS account. You can search for specific mute rules using the mute rule attributes such as rule name.

## Mute Rule Status

Once created, an alarm mute rule can be in one of the below three statuses:

- **SCHEDULED** – The mute rule will become active at some time in the future according to the configured time window expression.
- **ACTIVE** – The mute rule is currently active as per the configured time window expression and actively muting targeted alarm actions.
- **EXPIRED** – The mute rule will not be SCHEDULED/ACTIVE anymore in the future. This occurs for one-time mute rules after the mute window has ended, or for recurring mute rules when an end timestamp is configured and that time has passed.

## Effects of mute rules on alarms

During an active mute window, when a targeted alarm changes state and has actions configured, CloudWatch mutes those actions from executing. Mutes are applied only to alarm actions, meaning that alarms continue to be evaluated and state changes are visible in the CloudWatch console, but configured actions such as Amazon Simple Notification Service notifications, Amazon Elastic Compute Cloud Auto Scaling actions, or Amazon EC2 actions are prevented from executing. CloudWatch continues to evaluate alarm states normally throughout the mute period, and you can view this information through alarm history.

When a mute window ends, if the targeted alarm(s) remains in an alarming state (OK/ALARM/INSUFFICIENT_DATA), CloudWatch automatically re-triggers the alarm actions that were muted during the window. This ensures that your alarm actions are executed for ongoing issues once the planned mute period ends, maintaining the integrity of your monitoring system.

###### Note

When you mute an alarm:

- All the actions associated with the targeted alarms are muted
- Actions associated with all alarm states (OK, ALARM, and INSUFFICIENT_DATA) are muted

## Viewing and managing muted alarms

**Viewing muted alarms:** You can easily identify which alarms are currently muted through the CloudWatch console. In both the alarms list view and individual alarm detail pages, a mute icon appears next to alarms whose actions are currently being muted by active mute rules. This visual indicator helps you quickly understand which alarms actions are being currently muted until the mute window expires.

![](images/alarm_mute_rules_icon.png)

**Alarms timeline:** The CloudWatch alarms console provides a comprehensive timeline view that shows when your alarm actions were muted. This timeline displays mute periods alongside alarm state changes, giving you a complete historical view of both alarm behaviour and muting activity. You can use this timeline to analyze the effectiveness of your mute rules and understand how they correlate with your operational activities.

![](images/alarm-mutes-timelineview.png)

**Programmatically checking alarm mute status:** To programmatically determine if an alarm is currently muted, you can use the [ListAlarmMuteRules](../APIReference/API_ListAlarmMuteRules.md "../APIReference/API_ListAlarmMuteRules.md") API with the alarm name as a filter criteria. This API returns all active mute rules that are affecting the specified alarm, allowing you to integrate mute status checks into your automation workflows, monitoring dashboards, or operational tools.

For example: To check if an alarm named "HighCPUAlarm" is currently muted, call the [ListAlarmMuteRules](../APIReference/API_ListAlarmMuteRules.md "../APIReference/API_ListAlarmMuteRules.md") API with the filter parameter set to the alarm name. The response will include all mute rules targeting that alarm, along with their current status (SCHEDULED, ACTIVE, or EXPIRED).

**Alarm history:** Whenever alarm actions are muted due to an active mute rule, CloudWatch writes a history entry to the alarm's history log. This provides a complete audit trail of when your alarms were muted, helping you understand the timeline of muting events and correlate them with operational activities. You can view this history through the CloudWatch console or retrieve it programmatically using the [DescribeAlarmHistory](../APIReference/API_DescribeAlarmHistory.md "../APIReference/API_DescribeAlarmHistory.md") API.

###### Note

- When multiple alarm mute rules are active simultaneously, the most recently created mute rule name is written to the alarm history along with the total number of other active mute rules.
- The timeline displays mute periods only when an alarm state transitions during an active mute window and actions were prevented from executing.

###### Tip

You can manage alarm mute rules programmatically using the CloudWatch API. For more information, see [PutAlarmMuteRule](../APIReference/API_PutAlarmMuteRule.md "../APIReference/API_PutAlarmMuteRule.md"), [GetAlarmMuteRule](../APIReference/API_GetAlarmMuteRule.md "../APIReference/API_GetAlarmMuteRule.md"), [ListAlarmMuteRules](../APIReference/API_ListAlarmMuteRules.md "../APIReference/API_ListAlarmMuteRules.md"), and [DeleteAlarmMuteRule](../APIReference/API_DeleteAlarmMuteRule.md "../APIReference/API_DeleteAlarmMuteRule.md").

## Example schedules for common use cases

The following examples show how to configure time window expressions for common use cases.

**Scenario 1: Muting alarm actions during scheduled maintenance windows** – Regular maintenance activities that occur on a predictable schedule, such as system or database updates when services are intentionally unavailable or operating in degraded mode.

- Cron expression `0 2 * * SUN` with duration `PT4H` - Mutes alarms every Sunday from 2:00 AM to 6:00 AM for weekly system maintenance.
- Cron expression `0 1 1 * *` with duration `PT6H` - Mutes alarms on the first day of each month from 1:00 AM to 7:00 AM for monthly database maintenance.

**Scenario 2: Muting non-critical alarms during non-business hours** – Reducing alert fatigue during weekends or holidays when immediate attention is not required.

- Cron expression `0 18 * * FRI` with duration `P2DT12H` - Mutes alarms every weekend from Friday 6:00 PM to Monday 6:00 AM.

**Scenario 3: Muting performance alarms during daily backup operations** – Daily automated backup processes that temporarily increase resource utilization and may trigger performance-related alarms during predictable time windows.

- Cron expression `0 23 * * *` with duration `PT2H` - Mutes alarms every day from 11:00 PM to 1:00 AM during nightly backup operations that temporarily increase disk I/O and CPU utilization.

**Scenario 4: Muting duplicate alarms during active troubleshooting sessions** – Temporary muting of alarm actions while teams are actively investigating and resolving issues, preventing notification noise and allowing focused problem resolution.

- At expression `at(2024-05-10T14:00)` with duration `PT4H` - Mutes alarms on May 10, 2024 from 2:00 PM to 6:00 PM during an active incident response session.

**Scenario 5: Muting alarm actions during planned company shutdowns** – One-time extended maintenance periods or company-wide shutdowns where all systems are intentionally offline for extended periods.

- At expression `at(2024-12-23T00:00)` with duration `P7D` - Mutes alarms for the entire week of December 23-29, 2024 during annual company shutdown.
