# Combining alarms

With CloudWatch, you can combine several alarms into one _composite alarm_ to
create a summarized, aggregated health indicator over a whole application or group of
resources. Composite alarms are alarms that determine their state by monitoring the states of
other alarms. You define rules to combine the status of those monitored alarms using Boolean
logic.

You can use composite alarms to reduce alarm noise by taking actions only at an aggregated
level. For example, you can create a composite alarm to send a notification to your web server
team if any alarm related to your web server triggers. When any of those alarms goes into the
ALARM state, the composite alarm goes itself in the ALARM state and sends a notification to
your team. If other alarms related to your web server also go into the ALARM state, your team
does not get overloaded with new notifications since the composite alarm has already notified
them about the existing situation.

You can also use composite alarms to create complex alarming conditions and take actions
only when many different conditions are met. For example, you can create a composite alarm
that combines a CPU alarm and a memory alarm, and would only notify your team if both the CPU
and the memory alarms have triggered.

**Using composite alarms**

When you use composite alarms, you have two options:

- Configure the actions you want to take only at the composite alarm level, and create
  the underlying monitored alarms without actions
- Configure a different set of actions at the composite alarm level. For example, the
  composite alarm actions could engage a different team in case of a widespread
  issue.
  Composite alarms can take only the following actions:

- Notify Amazon SNS topics
- Invoke Lambda functions
- Create OpsItems in Systems Manager Ops Center
- Create incidents in Systems Manager Incident Manager

###### Note

All the underlying alarms in your composite alarm must be in the same account and the
same Region as your composite alarm. However, if you set up a composite alarm in a CloudWatch
cross-account observability monitoring account, the underlying alarms can watch metrics in
different source accounts and in the monitoring account itself. For more information, see
[CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

A single composite alarm can monitor 100 underlying alarms, and 150 composite alarms
can monitor a single underlying alarm.

**Rule expressions**

All composite alarms contain rule expressions. Rule expressions tell composite alarms
which other alarms to monitor and determine their states from. Rule expressions can refer to
metric alarms and composite alarms. When you reference an alarm in a rule expression, you
designate a function to the alarm that determines which of the following three states the
alarm will be in:

- ALARM

ALARM ("alarm-name or alarm-ARN") is TRUE if the alarm is in ALARM state.

- OK

OK ("alarm-name or alarm-ARN") is TRUE if the alarm is in OK state.

- INSUFFICIENT_DATA

INSUFFICIENT_DATA (“alarm-name or alarm-ARN") is TRUE if the named alarm is in
INSUFFICIENT_DATA state.

###### Note

TRUE always evaluates to TRUE, and FALSE always evaluates to FALSE.

**Alarm references**

When referencing an alarm, using either the alarm name or ARN, the rule syntax can support
referencing the alarm with or without quotation marks (") around the alarm name or ARN.

- If specified without quotes, alarm names or ARNs must not contain spaces, round
  brackets, or commas.
- If specified within quotes, alarm names or ARNs that _include_ double quotes (") must enclose the " using backslash escape (\)
  characters for correct interpretation of the reference.
  **Syntax**

The syntax of the expression you use to combine several alarms into one composite alarm
uses boolean logic and functions. The following table describes the operators and functions
available in rule expressions:

| Operator/Function | Description                                                                                                                                                                                                                                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AND`             | Logical AND operator. Returns TRUE when all specified conditions are<br>TRUE.                                                                                                                                                                                                                                                                                           |
| `OR`              | Logical OR operator. Returns TRUE when at least one of the specified conditions<br>is TRUE.                                                                                                                                                                                                                                                                             |
| `NOT`             | Logical NOT operator. Returns TRUE when the specified condition is FALSE.                                                                                                                                                                                                                                                                                               |
| `AT_LEAST`        | Function that returns TRUE when a minimum number or percentage of specified<br>alarms are in the required state. Format: `AT_LEAST(M, STATE_CONDITION, (alarm1,<br>alarm2, ...alarmN))` where M can be an absolute number or percentage (for example,<br>50%), and STATE_CONDITION can be ALARM, OK, INSUFFICIENT_DATA, NOT ALARM, NOT OK, or<br>NOT INSUFFICIENT_DATA. |

You can use parentheses to group conditions and control the order of evaluation in complex
expressions.

**Example expressions**

The request parameter `AlarmRule` supports the use of the logical operators
`AND`, `OR`, and `NOT`, as well as the `AT_LEAST` function, so you can combine multiple
functions into a single expressions. The following example expressions show how you can
configure the underlying alarms in your composite alarm:

- `ALARM(CPUUtilizationTooHigh) AND ALARM(DiskReadOpsTooHigh)`

The expression specifies that the composite alarm goes into `ALARM` only if
`CPUUtilizationTooHigh` and `DiskReadOpsTooHigh` are in
`ALARM`.

- `AT_LEAST(2, ALARM, (WebServer1CPU, WebServer2CPU, WebServer3CPU, WebServer4CPU))`

The expression specifies that the composite alarm goes into `ALARM` when
at least 2 out of the 4 web server CPU alarms are in `ALARM` state. This allows you to trigger alerts based on a threshold of affected resources rather than requiring all or just one to be in alarm state.

- `AT_LEAST(50%, OK, (DatabaseConnection1, DatabaseConnection2, DatabaseConnection3, DatabaseConnection4))`

The expression specifies that the composite alarm goes into `ALARM` when
at least 50% of the database connection alarms are in `OK` state. Using percentages allows the rule to adapt dynamically as you add or remove monitored alarms.

- `ALARM(CPUUtilizationTooHigh) AND NOT ALARM(DeploymentInProgress)`

The expression specifies that the composite alarm goes into `ALARM` if
`CPUUtilizationTooHigh` is in `ALARM` and
`DeploymentInProgress` is not in `ALARM`. This is an example of a
composite alarm that reduces alarm noise during a deployment window.

- `AT_LEAST(2, ALARM, (AZ1Health, AZ2Health, AZ3Health)) AND NOT ALARM(MaintenanceWindow)`

The expression specifies that the composite alarm goes into `ALARM` when
at least 2 out of 3 availability zone health alarms are in `ALARM` state and the maintenance window alarm is not in `ALARM`. This combines the AT_LEAST function with other logical operators for more complex monitoring scenarios.

## Muting Composite Alarm Actions

Alarm mute rules allow you to automatically mute composite alarm actions during predefined time windows, such as maintenance periods or operational events. CloudWatch continues monitoring alarm states while preventing unwanted notifications. For more information, see [Alarm Mute Rules](alarm-mute-rules.md "alarm-mute-rules.md").

###### Topics

- [Create a composite alarm](Create_Composite_Alarm_How_To.md "Create_Composite_Alarm_How_To.md")
- [Suppressing composite alarm actions](Create_Composite_Alarm_Suppression.md "Create_Composite_Alarm_Suppression.md")
