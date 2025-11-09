# Rotation schedules

Secrets Manager rotates your secret on a schedule during a rotation window that you set. To set the schedule and window, you use a **cron()** or **rate()** expression along with a window duration. Secrets Manager rotates your secret at any time during the rotation window. You can rotate a secret as often as every four hours within a rotation window as small as one hour.

To turn on rotation, see:

- [Managed rotation for AWS Secrets Manager secrets](rotate-secrets_managed.md "rotate-secrets_managed.md")
- [Set up automatic rotation for Amazon RDS, Amazon Aurora, Amazon Redshift, or Amazon DocumentDB secrets](rotate-secrets_turn-on-for-db.md "rotate-secrets_turn-on-for-db.md")
- [Set up automatic rotation for
  non-database AWS Secrets Manager secrets](rotate-secrets_turn-on-for-other.md "rotate-secrets_turn-on-for-other.md")
  Secrets Manager rotation schedules use UTC time zone.

## Rotation windows

A Secrets Manager rotation window is similar to a maintenance window. You set the rotation window when you want your secret rotated, and Secrets Manager rotates your secret at some time during the rotation window.

Secrets Manager rotation windows always start on the hour. For a rotation schedule that uses a `rate()` expression in days, the rotation window starts at midnight. You can set the start time for the rotation window by using a `cron()` expression. For examples, see [Cron expressions](#rotate-secrets_schedule-cron "#rotate-secrets_schedule-cron").

By default, the rotation window closes after one hour for a rotation schedule in _hours_, and at the end of the day for a rotation schedule in _days_.

To change the length of the rotation window, set the **Window duration**. You can set the rotation window as small as one hour. The rotation window must not extend into the next rotation window. In other words, for a rotation schedule in _hours_, confirm that the rotation window is less than or equal to the number of hours between rotations. For a rotation schedule in _days_, confirm that the start hour plus the window duration is less than or equal to 24 hours.

## Rate expressions

Secrets Manager rate expressions have the following format, where
`Value` is a positive integer and
`Unit` can be `hour`, `hours`, `day`, or `days`:

```
rate(`Value` `Unit`)
```

You can rotate a secret as often as every four hours. The maximum rotation period is 999 days. Examples:

- `rate(4 hours)` means the secret is rotated every four hours.
- `rate(1 day)` means the secret is rotated every day.
- `rate(10 days)` means the secret is rotated every 10 days.

## Cron expressions

Secrets Manager cron expressions have the following format:

```
cron(`Minutes` `Hours` `Day-of-month` `Month` `Day-of-week` `Year`)
```

A cron expression that includes increments of hours resets each day. For example, `cron(0 4/12 * * ? *)` means 4:00 AM, 4:00 PM, and then the next day 4:00 AM, 4:00 PM. Secrets Manager rotation schedules use UTC time zone.

| Example schedule                                                                                                                                     | Expression                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Every eight hours starting at midnight.                                                                                                              | `cron(0 /8<br>• ? *)`        |
| Every eight hours starting at 8:00 AM.                                                                                                               | `cron(0 8/8<br>• ? *)`       |
| Every ten hours, starting at 2:00 AM.<br>The rotation windows will start at 2:00, 12:00, and 22:00, and then the next day at 2:00, 12:00, and 22:00. | `cron(0 2/10<br>• ? *)`      |
| Every day at 10:00 AM.                                                                                                                               | `cron(0 10<br>• ? *)`        |
| Every Saturday at 6:00 PM.                                                                                                                           | `cron(0 18 ?<br>• SAT *)`    |
| The first day of every month at 8:00 AM.                                                                                                             | `cron(0 8 1<br>• ? *)`       |
| Every three months on the first Sunday at 1:00 AM.                                                                                                   | `cron(0 1 ? 1/3 SUN#1 *)`    |
| The last day of every month at 5:00 PM.                                                                                                              | `cron(0 17 L<br>• ? *)`      |
| Monday through Friday at 8:00 AM.                                                                                                                    | `cron(0 8 ?<br>• MON-FRI *)` |
| First and 15th day of every month at 4:00 PM.                                                                                                        | `cron(0 16 1,15<br>• ? *)`   |
| First Sunday of every month at midnight.                                                                                                             | `cron(0 0 ?<br>• SUN#1 *)`   |
| Starting in January, every 11 months on the first Monday at midnight.                                                                                | `cron(0 0 ? 1/11 2#1 *)`     |

### Cron expression requirements in Secrets Manager

Secrets Manager has some restrictions on what you can use for cron expressions. A cron expression for Secrets Manager must have **0** in the minutes field because Secrets Manager rotation windows start on the hour. It must have **\*** in the year field, because Secrets Manager does not support rotation schedules that are more than a year apart. The following table shows the options you can use.

| **Fields**   | **Values**      | **Wildcards**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minutes      | Must be 0       | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Hours        | 0–23            | Use \*_/_<br>• (forward slash) to specify increments. For example `2/10` means every 10 hours beginning at 2:00 AM. You can rotate a secret as often as every four hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Day-of-month | 1–31            | Use **,\*<br>• (comma) to include additional values. For example `1,15` means the first and 15th day of the month.<br>Use **-\*<br>• (dash) to specify a range. For example `1–15` means days 1 through 15 of the month.<br>Use **\*_<br>• (asterisk) to includes all values in the<br>field. For example `_` means every<br>day of the month.<br>The **?_<br>• (question mark) wildcard specifies one or another.<br>You can't specify the `Day-of-month` and `Day-of-week`<br>fields in the same cron expression. If you specify a value in one of the fields,<br>you must use a \*\*?_<br>• (question mark) in the other.<br>Use **/\*<br>• (forward slash) to specify increments. For example, `1/2` means every two days starting on day 1, in other words, day 1, 3, 5, and so on.<br>Use **L*<br>• to specify the last day of the month.<br>Use \*\*`DAY`L*<br>• to specify the last named day of the<br>month. For example `SUNL` means the last Sunday of the month.       |
| Month        | 1–12 or JAN–DEC | Use **,\*<br>• (comma) to include additional values. For example, `JAN,APR,JUL,OCT` means January, April,<br>July, and October.<br>Use **-\*<br>• (dash) to specify a range. For example `1–3` means months 1 through 3 of the year.<br>Use **\*_<br>• (asterisk) to includes all values in the<br>field. For example `_` means every month.<br>Use **/\*<br>• (forward slash) to specify increments. For example, `1/3` means every third month, starting on month 1, in other words month 1, 4, 7, and 10.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Day-of-week  | 1–7 or SUN–SAT  | Use **#\*<br>• to<br>specify the day of the week within a month. For example, `TUE#3`<br>means the third Tuesday of the month.<br>Use **,_<br>• (comma) to include additional values. For example `1,4` means the first and fourth day of the week.<br>Use \*\*-_<br>• (dash) to specify a range. For example `1–4` means days 1 through 4 of the week.<br>Use **\*_<br>• (asterisk) to includes all values in the<br>field. For example `_` means every<br>day of the week.<br>The **?_<br>• (question mark) wildcard specifies one or another.<br>You can't specify the `Day-of-month` and `Day-of-week`<br>fields in the same cron expression. If you specify a value in one of the fields,<br>you must use a \*\*?_<br>• (question mark) in the other.<br>Use **/\*<br>• (forward slash) to specify increments. For example, `1/2` means every second day of the week, starting on the first day, so day 1, 3, 5, and 7.<br>Use **L\*<br>• to specify the last day of the week. |
| Year         | Must be `*`     | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
