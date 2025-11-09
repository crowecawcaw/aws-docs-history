# Overview of the Performance Schema for Performance Insights on Amazon RDS for MariaDB or MySQL

The Performance Schema is an optional feature for monitoring Amazon RDS
for MariaDB or MySQL runtime performance at a low level of detail. The Performance Schema is designed to have minimal impact on
database performance. Performance Insights is a separate feature that you can use with or without the Performance Schema.

###### Topics

- [Overview of the Performance Schema](#USER_PerfInsights.EnableMySQL.overview "#USER_PerfInsights.EnableMySQL.overview")
- [Performance Insights and the Performance Schema](#USER_PerfInsights.effect-of-pfs "#USER_PerfInsights.effect-of-pfs")
- [Automatic management of the Performance Schema by Performance
  Insights](#USER_PerfInsights.EnableMySQL.options "#USER_PerfInsights.EnableMySQL.options")
- [Effect of a reboot on the Performance Schema](#USER_PerfInsights.EnableMySQL.reboot "#USER_PerfInsights.EnableMySQL.reboot")
- [Determining whether
  Performance Insights is managing the Performance Schema](USER_PerfInsights.EnableMySQL.md "USER_PerfInsights.EnableMySQL.md")
- [Turn on the Performance Schema for Amazon RDS for MariaDB or MySQL](USER_PerfInsights.EnableMySQL.md "USER_PerfInsights.EnableMySQL.md")

## Overview of the Performance Schema

The Performance Schema monitors events in MariaDB and MySQL databases. An _event_ is a database server action that consumes time and has been instrumented
so that timing information can be collected. Examples of events include the following:

- Function calls
- Waits for the operating system
- Stages of SQL execution
- Groups of SQL statements

The `PERFORMANCE_SCHEMA` storage engine is a mechanism for implementing the Performance Schema feature. This engine collects event
data using instrumentation in the database source code. The engine stores events in memory-only tables in the
`performance_schema` database. You can query `performance_schema` just as you can query any other tables. For
more information, see [MySQL Performance Schema](https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html") in the
_MySQL Reference Manual_.

## Performance Insights and the Performance Schema

Performance Insights and the Performance Schema are separate features, but they are connected. The behavior of Performance Insights for
Amazon RDS for MariaDB or MySQL depends on whether the
Performance Schema is turned on, and if so, whether Performance Insights manages the Performance Schema automatically. The following table
describes the behavior.

| Performance Schema turned on | Performance Insights management mode | Performance Insights behavior                                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes                          | Automatic                            | • Collects detailed, low-level monitoring information<br>• Collects active session metrics every second<br>• Displays DB load categorized by detailed wait events, which you can use to identify bottlenecks                                                                          |
| Yes                          | Manual                               | • Collects wait events and per-SQL metrics<br>• Collects active session metrics every second<br>• Reports user states such as inserting and sending, which don't help you identify bottlenecks                                                                                        |
| No                           | N/A                                  | • Doesn't collect wait events, per-SQL metrics, or other detailed, low-level monitoring information<br>• Collects active session metrics every five seconds instead of every second<br>• Reports user states such as inserting and sending, which don't help you identify bottlenecks |

## Automatic management of the Performance Schema by Performance

Insights

When you create an Amazon RDS for MariaDB or MySQL DB instance
with Performance Insights turned on, the Performance Schema is also turned on. In this case, Performance Insights automatically manages
your Performance Schema parameters. This is the recommended configuration.

When Performance Insights manages the Performance Schema automatically, the **Source** of `performance_schema` is `System
 default`.

###### Note

Automatic management of the Performance Schema isn't supported for the t4g.medium instance class.

If you change the `performance_schema` parameter value manually, and then later want to change to automatic management, see [Turn on the Performance Schema for Amazon RDS for MariaDB or MySQL](USER_PerfInsights.EnableMySQL.md "USER_PerfInsights.EnableMySQL.md").

###### Important

When Performance Insights turns on the Performance Schema, it doesn't change the parameter group values. However, the values are changed on
the DB instances that are running. The only way to see the changed values is to run the `SHOW GLOBAL VARIABLES`
command.

## Effect of a reboot on the Performance Schema

Performance Insights and the Performance Schema differ in their requirements for DB instance reboots:

**Performance Schema**

To turn this feature on or off, you must reboot the DB instance.

**Performance Insights**

To turn this feature on or off, you don't need to reboot the DB instance.

If the Performance Schema isn't currently turned on, and you turn on Performance Insights without rebooting the DB instance, the Performance
Schema won't be turned on.
