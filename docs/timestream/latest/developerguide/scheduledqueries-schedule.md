For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Schedule expressions for scheduled

queries

You can create scheduled queries on an automated schedule by using Amazon Timestream for LiveAnalytics scheduled
queries that use cron or rate expressions. All scheduled queries use the UTC time zone,
and the minimum possible precision for schedules is 1 minute.

Two ways to specify the schedule expressions are _cron_ and
_rate_. Cron expressions offer more fine grained schedule
control, while rate expressions are simpler to express but lack the fine-grained
control.

For example, with a cron expression, you can define a scheduled query that gets
triggered at a specified time on a certain day of each week or month, or a specified
minute every hour only on Monday - Friday, and so on. In contrast, rate expressions
initiate a scheduled query at a regular rate, such as once every minute, hour, or day,
starting from the exact time when the scheduled query is created.

###### Cron expression

- _Syntax_

```
cron(fields)
```

Cron expressions have six required fields, which are separated by white
space.

| Field        | Values          | Wildcards             |
| ------------ | --------------- | --------------------- |
| Minutes      | 0-59            | ,<br>• \<br>• /       |
| Hours        | 0-23            | ,<br>• \<br>• /       |
| Day-of-month | 1-31            | ,<br>• \<br>• ? / L W |
| Month        | 1-12 or JAN-DEC | ,<br>• \<br>• /       |
| Day-of-week  | 1-7 or SUN-SAT  | ,<br>• \<br>• ? L #   |
| Year         | 1970-2199       | ,<br>• \<br>• /       |

###### Wildcard characters

    + The \*,\* (comma) wildcard includes additional values. In the Month
     field, JAN,FEB,MAR would include January, February, and March.
    + The \*-\* (dash) wildcard specifies ranges. In the Day field, 1-15 would
     include days 1 through 15 of the specified month.
    + The \*\*\* (asterisk) wildcard includes all values in the field. In the
     Hours field, \*\*\* would include every hour. You cannot use \*\*\* in both
     the Day-of-month and Day-of-week fields. If you use it in one, you must
     use \*?\* in the other.
    + The \*/\* (forward slash) wildcard specifies increments. In the Minutes
     field, you could enter 1/10 to specify every 10th minute, starting from
     the first minute of the hour (for example, the 11th, 21st, and 31st
     minute, and so on).
    + The \*?\* (question mark) wildcard specifies one or another. In the
     Day-of-month field you could enter \*7\* and if you didn't care what day
     of the week the 7th was, you could enter \*?\* in the Day-of-week
     field.
    + The \*L\* wildcard in the Day-of-month or Day-of-week fields specifies
     the last day of the month or week.
    + The W wildcard in the Day-of-month field specifies a weekday. In the
     Day-of-month field, 3W specifies the weekday closest to the third day of
     the month.
    + The \*#\* wildcard in the Day-of-week field specifies a certain instance
     of the specified day of the week within a month. For example, 3#2 would
     be the second Tuesday of the month: the 3 refers to Tuesday because it
     is the third day of each week, and the 2 refers to the second day of
     that type within the month.

###### Note

If you use a '#' character, you can define only one expression in the
day-of-week field. For example, "3#1,6#3" is not valid because it is
interpreted as two expressions.

###### Limitations

    + You can't specify the Day-of-month and Day-of-week fields in the same
     cron expression. If you specify a value (or a \*) in one of the fields,
     you must use a \*?\* (question mark) in the other.
    + Cron expressions that lead to rates faster than 1 minute are not
     supported.

**Examples**

| Minutes | Hours | Day of month | Month | Day of week | Year | Meaning                                                                         |
| ------- | ----- | ------------ | ----- | ----------- | ---- | ------------------------------------------------------------------------------- |
| 0       | 10    | \*           | \*    | ?           | \*   | Run at 10:00 am (UTC) every day.                                                |
| 15      | 12    | \*           | \*    | ?           | \*   | Run at 12:15 pm (UTC) every day.                                                |
| 0       | 18    | ?            | \*    | MON-FRI     | \*   | Run at 6:00 pm (UTC) every Monday through Friday.                               |
| 0       | 8     | 1            | \*    | ?           | \*   | Run at 8:00 am (UTC) every first day of the month.                              |
| 0/15    | \*    | \*           | \*    | ?           | \*   | Run every 15 minutes.                                                           |
| 0/10    | \*    | \*           | \*    | MON-FRI     | \*   | Run every 10 minutes Monday through Friday.                                     |
| 0/5     | 8-17  | ?            | \*    | MON-FRI     | \*   | Run every 5 minutes Monday through Friday between 8:00 am and<br>5:55 pm (UTC). |

###### Rate expressions

- A rate expression starts when you create the scheduled event rule, and then
  runs on its defined schedule. Rate expressions have two required fields. Fields
  are separated by white space.

_Syntax_

```
rate(value unit)
```

    + `value`: A positive number.
    + `unit`: The unit of time. Different units are required for
     values of 1 (for example, minute) and values over 1 (for example,
     minutes). Valid values: minute | minutes | hour | hours | day |
     days
