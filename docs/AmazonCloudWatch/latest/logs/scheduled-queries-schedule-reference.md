# Schedule expression reference

Use these reference tables to construct schedule expressions for your scheduled
queries. All times are in UTC.

**Cron expression syntax**

Format: `cron(minute hour day-of-month month day-of-week year)`

| Use Case              | Cron Expression                    | Description                                        | Use When             |
| --------------------- | ---------------------------------- | -------------------------------------------------- | -------------------- |
| **Daily Schedules**   | `cron(0 9<br>• ? *)`               | Every day at 9:00 AM UTC                           | Daily reports        |
|                       | `cron(0 */6<br>• ? *)`             | Every 6 hours (00:00, 06:00, 12:00, 18:00 UTC)     | Frequent monitoring  |
|                       | `cron(30 2<br>• ? *)`              | Every day at 2:30 AM UTC                           | Off-peak analysis    |
| **Business Hours**    | `cron(0 9-17 ?<br>• MON-FRI *)`    | Every hour from 9 AM to 5 PM, Monday to Friday UTC | Business monitoring  |
|                       | `cron(0 18 ?<br>• MON-FRI *)`      | Weekdays at 6:00 PM UTC                            | End of business day  |
|                       | `cron(0 8,12,17 ?<br>• MON-FRI *)` | 8 AM, noon, and 5 PM on weekdays UTC               | Key business times   |
| **Weekly Schedules**  | `cron(0 12 ?<br>• SUN *)`          | Every Sunday at noon UTC                           | Weekly summaries     |
|                       | `cron(0 9 ?<br>• MON *)`           | Every Monday at 9:00 AM UTC                        | Week start reports   |
|                       | `cron(0 23 ?<br>• FRI *)`          | Every Friday at 11:00 PM UTC                       | Week end cleanup     |
| **Monthly Schedules** | `cron(0 0 1<br>• ? *)`             | First day of every month at midnight UTC           | Monthly reports      |
|                       | `cron(0 9 L<br>• ? *)`             | Last day of every month at 9:00 AM UTC             | Month end processing |
|                       | `cron(0 10 1 1,4,7,10 ? *)`        | First day of each quarter at 10:00 AM UTC          | Quarterly analysis   |
| **High Frequency**    | `cron(*/15<br>• ? *)`              | Every 15 minutes                                   | Real-time monitoring |
|                       | `cron(0,30<br>• ? *)`              | Every 30 minutes (at :00 and :30)                  | Frequent checks      |
|                       | `cron(0 */2<br>• ? *)`             | Every 2 hours                                      | Regular intervals    |
| **Special Cases**     | `cron(30 8 1 1 ? *)`               | January 1st at 8:30 AM UTC                         | Annual reports       |
|                       | `cron(0 6<br>• SAT,SUN *)`         | Weekends at 6:00 AM UTC                            | Weekend processing   |
|                       | `cron(0 0 ?<br>• MON#1 *)`         | First Monday of every month at midnight UTC        | Monthly planning     |

**Cron expression field reference**

| Field              | Values          | Wildcards              | Examples                                                        |
| ------------------ | --------------- | ---------------------- | --------------------------------------------------------------- |
| Minute (1st)       | 0-59            | `<br>• ,<br>• /`       | `0` (top of hour), `*/15` (every 15 min), `0,30` (twice hourly) |
| Hour (2nd)         | 0-23            | `<br>• ,<br>• /`       | `9` (9 AM), `*/2` (every 2 hrs), `9-17` (business hours)        |
| Day-of-month (3rd) | 1-31, L, W      | `<br>• ,<br>• / ?`     | `1` (1st day), `L` (last day), `?` (when using day-of-week)     |
| Month (4th)        | 1-12 or JAN-DEC | `<br>• ,<br>• /`       | `1` (January), `JAN`, `1,4,7,10` (quarterly)                    |
| Day-of-week (5th)  | 1-7 or SUN-SAT  | `<br>• ,<br>• / ? # L` | `MON-FRI` (weekdays), `SUN`, `MON#1` (1st Monday)               |
| Year (6th)         | 1970-2199       | `<br>• ,<br>• /`       | `*` (every year), `2024` (specific year), `2024-2026` (range)   |

**Wildcard characters and special expressions**

**`*` (asterisk)**

Matches all values in the field. Example: `*` in the hour field means every hour.

**`?` (question mark)**

No specific value. Use in day-of-month or day-of-week when the other is specified. Example: Use `?` in day-of-month when specifying `MON-FRI` in day-of-week.

**`-` (dash)**

Range of values. Example: `MON-FRI` (Monday through Friday), `9-17` (9 AM through 5 PM).

**`,` (comma)**

Multiple specific values. Example: `MON,WED,FRI` (Monday, Wednesday, Friday), `8,12,17` (8 AM, noon, 5 PM).

**`/` (slash)**

Step values or increments. Example: `0/15` in minutes means every 15 minutes starting at minute 0 (0, 15, 30, 45). `*/2` in hours means every 2 hours.

**`L` (last)**

Last day of month or last occurrence of weekday. Example: `L` in day-of-month means last day of month. `FRIL` means last Friday of month.

**`W` (weekday)**

Nearest weekday. Example: `15W` means nearest weekday to the 15th of the month.

**`#` (nth occurrence)**

Nth occurrence of weekday in month. Example: `MON#1` means first Monday of month, `FRI#2` means second Friday of month.

**Common patterns and best practices**

- **For business applications:** Use `MON-FRI` and business hours (e.g., `9-17`) to avoid running queries during weekends or off-hours.
- **For high-frequency monitoring:** Use increments like `*/15` (every 15 minutes) but be mindful of query concurrency limits.
- **For resource efficiency:** Schedule resource-intensive queries during off-peak hours using early morning times like `2-6` UTC.
- **For monthly reports:** Use `L` for last day of month or specific dates like `1` for first day to ensure consistent timing.
