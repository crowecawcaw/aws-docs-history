# Schedule types in EventBridge Scheduler

The following topic describes the different schedule types that Amazon EventBridge Scheduler supports, as well as how EventBridge Scheduler handles daylight savings time, and scheduling in different time zones.
You can choose from three schedule types when configuring your schedule: _rate-based_, _cron-based_, and
_one-time_ schedules.

Both rate-based and cron-based schedules are recurring schedules. You configure each recurring schedule type using a _schedule expression_ for the
type of schedule you want to configure, and specifying a time zone in which EventBridge Scheduler evaluates the expression.

A one-time schedule is a schedule that invokes a target only once. You configure a one-time schedule when by specifying the time, date, and time zone in which EventBridge Scheduler evaluates the schedule.

###### Note

All schedule types on EventBridge Scheduler invoke their targets with 60 second precision. This means that if you set your schedule to run at
`1:00`, it will invoke the target API between `1:00:00` and `1:00:59`, assuming that a flexible
time window is not set.

Use the following sections to learn about configuring schedule expressions for each recurring schedule type, and how to set up a one-time schedule on EventBridge Scheduler.

###### Topics

- [Rate-based schedules](#rate-based "#rate-based")
- [Cron-based schedules](#cron-based "#cron-based")
- [One-time schedules](#one-time "#one-time")
- [Time zones on EventBridge Scheduler](#time-zones "#time-zones")
- [Daylight savings time on EventBridge Scheduler](#daylist-savings-time "#daylist-savings-time")

## Rate-based schedules

A rate-based schedule starts after the start date you specify for your schedule, and runs at a regular rate that you define until the schedule's end date. You can set up most common recurrent scheduling
use cases using a rate-based schedule. For example, if you want a schedule that invokes it's target every 15 minutes, once every two hours, or once every five days, you can use a rate-based schedule to achieve this.
You configure a rate-based schedule using a _rate expression_.

With rate-based schedules, you use the
[`StartDate`](../APIReference/API_CreateSchedule.md#scheduler-CreateSchedule-request-StartDate "../APIReference/API_CreateSchedule.md#scheduler-CreateSchedule-request-StartDate")
property to set the first occurrence of the schedule. If you do not provide a `StartDate` for a rate-based schedule, your schedule starts invoking
the target immediately.

Rate expressions have two required fields separated by a white space, as shown in the following.

### Syntax

```
rate(`value` `unit`)
```

value

A positive number.

unit

The unit of time you want your schedule to invoke it's target.

Valid inputs: `minutes` | `hours` | `days`

### Examples

The following example shows how to use rate expressions with the AWS CLI `create-schedule` command to configure a rate-based schedule.
This example creates a schedule that runs every five minutes and delivers a message to an Amazon SQS queue, using the templated `SqsParameters` target type.

Because this example does not set a value for the `--start-date` parameter, the schedule starts invoking its target immediately after you create and activate it.

```
`$` `aws scheduler create-schedule --schedule-expression 'rate(**5 minutes**)' --name `schedule-name` \
--target '{"RoleArn": "`role-arn`", "Arn": "`QUEUE_ARN`", "Input": "`TEST_PAYLOAD`" }' \
--flexible-time-window '{ "Mode": "OFF"}'`
```

## Cron-based schedules

A cron expression creates a fine-grained recurring schedule that runs at a specific time of your choosing. EventBridge Scheduler supports
configuring cron-based schedules in Universal Coordinated Time (UTC), or in the time zone that you specify when you create your schedule.
With cron-based schedules, you have more control over when and how often your schedule runs. Use cron-based schedules
when you need a customized recurrence schedule that is not supported by one of EventBridge Scheduler's rate expressions.
For example, you can create a cron-based schedule that runs at 8:00 a.m. PST on the first Monday of every month.
You configure a cron-based schedule using a _cron expression_.

A cron expression consists of five required fields separated by white space: minutes, hours, day-of-month, month,
day-of-week, and one optional field, year, as shown in the following.

### Syntax

```
cron(`minutes` `hours` `day-of-month` `month` `day-of-week` `year`)
```

| **Field**    | **Values**      | **Wildcards**         |
| ------------ | --------------- | --------------------- |
| Minutes      | 0-59            | ,<br>• \<br>• /       |
| Hours        | 0-23            | ,<br>• \<br>• /       |
| Day-of-month | 1-31            | ,<br>• \<br>• ? / L W |
| Month        | 1-12 or JAN-DEC | ,<br>• \<br>• /       |
| Day-of-week  | 1-7 or SUN-SAT  | ,<br>• \<br>• ? L #   |
| Year         | 1970-2199       | ,<br>• \<br>• /       |

###### Wildcards

- The **,** (comma) wildcard includes additional values. In the
  Month field, JAN,FEB,MAR includes January, February, and March.
- The **-** (dash) wildcard specifies ranges. In the Day field,
  1-15 includes days 1 through 15 of the specified month.
- The **\*** (asterisk) wildcard includes all values in the
  field. In the Hours field, **\*** includes every hour. You can't
  use **\*** in both the Day-of-month and Day-of-week fields. If
  you use it in one, you must use **?** in the other.
- The **/** (slash) wildcard specifies increments. In the
  Minutes field, you could enter 1/10 to specify every tenth minute, starting from
  the first minute of the hour (for example, the 11th, 21st, and 31st minute, and
  so on).
- The **?** (question mark) wildcard specifies any. In the
  Day-of-month field you could enter **7** and if any day of the
  week was acceptable, you could enter **?** in the Day-of-week
  field.
- The **L** wildcard in the Day-of-month or Day-of-week fields
  specifies the last day of the month or week.
- The `W` wildcard in the Day-of-month field specifies a
  weekday. In the Day-of-month field, `3W` specifies the
  weekday closest to the third day of the month.
- The **#** wildcard in the Day-of-week field specifies a
  certain instance of the specified day of the week within a month. For example,
  3#2 would be the second Tuesday of the month: the 3 refers to Tuesday because it
  is the third day of each week, and the 2 refers to the second day of that type
  within the month.

###### Note

If you use a '#' character, you can define only one expression in the
day-of-week field. For example, `"3#1,6#3"` is not valid because
it is interpreted as two expressions.

### Examples

The following example shows how to use cron expressions with the AWS CLI `create-schedule` command to configure a cron-based schedule.
This example creates a schedule that runs at 10:15am UTC+0 on the last Friday of each month during the years 2022 to 2023, and delivers a message to an Amazon SQS queue, using the templated `SqsParameters` target type.

```
`$` `aws scheduler create-schedule --schedule-expression "cron(**15 10 ? \* 6L 2022-2023**)" --name `schedule-name` \
--target '{"RoleArn": "`role-arn`", "Arn": "`QUEUE_ARN`", "Input": "`TEST_PAYLOAD`" }' \
--flexible-time-window '{ "Mode": "OFF"}'`
```

## One-time schedules

A one-time schedule will invoke a target only once at the date and time that you specify using a valid date, and a timestamp. EventBridge Scheduler supports
scheduling in Universal Coordinated Time (UTC), or in the time zone that you specify when you create your schedule.

###### Note

A one-time schedule still count against your account quota _after_ it has completed running and invoking it's target.
We recommend [deleting](managing-schedule-delete.md "managing-schedule-delete.md") your one-time schedules after they've completed running.

You configure a one-time schedule using an _at expression_. An at expression consists of the date and time at which you want
EventBridge Scheduler to invoke your schedule, as shown in the following.

### Syntax

```
at(`yyyy-mm-ddThh:mm:ss`)
```

When you configure a one-time schedule, EventBridge Scheduler ignores the `StartDate` and `EndDate` you specify for the schedule.

### Examples

The following example shows how to use at expressions with the AWS CLI `create-schedule` command to configure a one-time schedule.
This example creates a schedule that runs once at 1pm UTC-8 on November 20, 2022, and delivers a message to an Amazon SQS queue, using the templated `SqsParameters` target type.

```
`$` `aws scheduler create-schedule --schedule-expression "at(**2022-11-20T13:00:00**)" --name `schedule-name` \
--target '{"RoleArn": "`role-arn`", "Arn": "`QUEUE_ARN`", "Input": "`TEST_PAYLOAD`" }' \
--schedule-expression-timezone "America/Los_Angeles"
--flexible-time-window '{ "Mode": "OFF"}'`
```

## Time zones on EventBridge Scheduler

EventBridge Scheduler supports configuring cron-based and one-time schedules in any time zone that you specify. EventBridge Scheduler uses the [Time Zone Database](https://www.iana.org/time-zones "https://www.iana.org/time-zones") maintained by the
Internet Assigned Numbers Authority (IANA).

With the AWS CLI, you can set the time zone in which you want EventBridge Scheduler to evaluate your schedule using the `--schedule-expression-timezone` parameter. For example, the following command
creates a cron-based schedule that invokes a templated Amazon SQS `SendMessage` target in **America/New_York** every day at 8:30 a.m.

```
`$` `aws scheduler create-schedule --schedule-expression "cron(30 8 * * ? *)" --name schedule-in-est \
 --target '{"RoleArn": "`role-arn`", "Arn": "`QUEUE_ARN`", "Input": "This schedule runs in the America/New_York time zone." }' \
 **--schedule-expression-timezone "America/New\_York"**
 --flexible-time-window '{ "Mode": "OFF"}'`
```

## Daylight savings time on EventBridge Scheduler

EventBridge Scheduler automatically adjusts your schedule for daylight saving time. When time shifts _forward_ in the Spring, if a cron expression falls on a non-existent date and time, your schedule invocation is skipped.
When time shifts _backwards_ in the Fall, your schedule runs only once and does not repeat its invocation. The following invocations occur normally at the specified date and time.

EventBridge Scheduler adjusts your schedule depending on the time zone you specify when you create the schedule. If you configure a schedule in **America/New_York**, your schedule adjusts when
the time changes in that time zone, while a schedule in **America/Los_Angeles** is adjusted three hours later when the time changes on the west coast.

For rate-based schedules that use `days` as the unit, such as `rate(1 days)`, `days` represents a 24-hour duration on the clock. This means that when daylight savings time causes
a day to shorten to 23 hours, or extend to 25 hours, EventBridge Scheduler still evaluates the rate expression 24 hours after the schedule's last invocation.

###### Note

Some time zones do not observe daylight savings time, according to local rules and regulations. If you create a schedule in a time zone that does not observe daylight savings time,
EventBridge Scheduler does not adjust your schedule. Daylight-savings time adjustments do not apply to schedules in universal coordinated time (UTC).

###### Example

Consider a scenario where you create a schedule using the following cron expression in **America/Los_Angeles**: `cron(30 2 * * ? *)`.
This schedule runs every day at 2:30 a.m. in the specified time zone.

- **Spring-forward** – When time shifts forward in the Spring from 1:59 a.m. to 3:00 a.m., EventBridge Scheduler skips the schedule invocation on that day, and resumes running the schedule normally
  the following day.
- **Fall-back** – When time shifts backwards in the Fall from 2:59 a.m. to 2:00 a.m., EventBridge Scheduler runs the schedule only once at 2:30 a.m. before the shift occurs, but does not repeat the
  schedule invocation again at 2:30 a.m. after the time shift.
