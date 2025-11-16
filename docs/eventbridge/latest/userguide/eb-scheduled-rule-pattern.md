# Setting a schedule pattern for scheduled rules (legacy) in Amazon EventBridge

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

When you create a scheduled rule in EventBridge you can specify a schedule pattern that determines when EventBridge runs the rule:

- Use a _cron_ expression to run the rule at specific times and dates.
- Use a _rate_ expression to run the rule at regular intervals.

## Cron expressions

Cron expressions have six required fields, which are separated by white space.

**Syntax**

```
cron(*fields*)
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

###### Limitations

- You can't specify the Day-of-month and Day-of-week fields in the same cron
  expression. If you specify a value or a \* (asterisk) in one of the fields, you
  must use a **?** (question mark) in the other.
- Cron expressions that lead to rates faster than 1 minute are not
  supported.

###### Examples

You can use the following sample cron strings when creating a rule with
schedule.

| Minutes | Hours | Day of month | Month | Day of week | Year | Meaning                                                                                                                                                                        |
| ------- | ----- | ------------ | ----- | ----------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0       | 10    | \*           | \*    | ?           | \*   | Run at 10:00 am (UTC+0) every day                                                                                                                                              |
| 15      | 12    | \*           | \*    | ?           | \*   | Run at 12:15 pm (UTC+0) every day                                                                                                                                              |
| 0       | 18    | ?            | \*    | MON-FRI     | \*   | Run at 6:00 pm (UTC+0) every Monday through Friday                                                                                                                             |
| 0       | 8     | 1            | \*    | ?           | \*   | Run at 8:00 am (UTC+0) every 1st day of the month                                                                                                                              |
| 0/15    | \*    | \*           | \*    | ?           | \*   | Run every 15 minutes                                                                                                                                                           |
| 0/10    | \*    | ?            | \*    | MON-FRI     | \*   | Run every 10 minutes Monday through Friday                                                                                                                                     |
| 0/5     | 8-17  | ?            | \*    | MON-FRI     | \*   | Run every 5 minutes Monday through Friday between 8:00 am and 5:55<br>pm (UTC+0)                                                                                               |
| 0/30    | 20-2  | ?            | \*    | MON-FRI     | \*   | Run every 30 minutes Monday through Friday between 10:00 pm on the starting day to 2:00 am on the following day (UTC)<br>Run from 12:00 am to 2:00 am on Monday morning (UTC). |

The following example creates a rule that runs every day at 12:00pm UTC+0.

```
aws events put-rule --schedule-expression "cron(0 12 * * ? *)" --name `MyRule1`
```

The following example creates a rule that runs every day, at 2:05pm and 2:35pm
UTC+0.

```
aws events put-rule --schedule-expression "cron(5,35 14 * * ? *)" --name `MyRule2`
```

The following example creates a rule that runs at 10:15am UTC+0 on the last Friday of
each month during the years 2019 to 2022.

```
aws events put-rule --schedule-expression "cron(15 10 ? * 6L 2019-2022)" --name `MyRule3`
```

## Rate expressions

A _rate expression_ starts when you create the scheduled event
rule, and then it runs on a defined schedule.

Rate expressions have two required fields separated by white space.

**Syntax**

```
rate(*value* *unit*)
```

value

A positive number.

unit

The unit of time. Different units are required for values of 1, such as `minute`,
and values over 1, such as `minutes`.

Valid values: minute | minutes | hour | hours | day | days

###### Limitations

If the value is equal to 1, then the unit must be singular. If the value is
greater than 1, the unit must be plural. For example, rate(1 hours) and rate(5 hour)
aren't valid, but rate(1 hour) and rate(5 hours) are valid.

###### Examples

The following examples show how to use rate expressions with the AWS CLI
`put-rule` command. The first example triggers the rule every minute, the next
triggers it every five minutes, the third example triggers it once an hour, and the final example triggers it once per day.

```
aws events put-rule --schedule-expression "rate(1 minute)" --name `MyRule2`
```

```
aws events put-rule --schedule-expression "rate(5 minutes)" --name `MyRule3`
```

```
aws events put-rule --schedule-expression "rate(1 hour)" --name `MyRule4`
```

```
aws events put-rule --schedule-expression "rate(1 day)" --name `MyRule5`
```
