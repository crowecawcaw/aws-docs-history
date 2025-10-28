# Key concepts for database performance tuning

DevOps Guru for RDS assumes that you're familiar with a few key performance concepts. To learn more about these concepts,
see [Overview of Performance Insights](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md") in the _Amazon Aurora User Guide_
or [Overview of Performance Insights](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md") in the _Amazon RDS User Guide_.

###### Topics

- [Metrics](#working-with-rds.overview.tuning.metrics "#working-with-rds.overview.tuning.metrics")
- [Problem detection](#working-with-rds.overview.tuning.problems "#working-with-rds.overview.tuning.problems")
- [DB
  load](#working-with-rds.overview.tuning.db-load "#working-with-rds.overview.tuning.db-load")
- [Wait events](#working-with-rds.overview.tuning.waits "#working-with-rds.overview.tuning.waits")

## Metrics

A metric represents a time-ordered set of data points.
Think of a metric as a variable to monitor, and the data points as representing the values of that variable over time.
Amazon RDS provides metrics in real time for the database and for the operating system (OS) that your DB instance runs on.
You can view all the system metrics and process information for your Amazon RDS DB instances on the Amazon RDS console.
DevOps Guru for RDS monitors and provides insights for some of these metrics. For more information,
see [Monitoring metrics in an Amazon Aurora cluster](../../../AmazonRDS/latest/AuroraUserGuide/MonitoringAurora.md "../../../AmazonRDS/latest/AuroraUserGuide/MonitoringAurora.md")
or [Monitoring metrics in an Amazon Relational Database Service instance](../../../AmazonRDS/latest/UserGuide/CHAP_Monitoring.md "../../../AmazonRDS/latest/UserGuide/CHAP_Monitoring.md").

## Problem detection

DevOps Guru for RDS employs database and operating system (OS) metrics to detect critical database performance issues, whether those issues are impending or ongoing.
There are 2 primary ways DevOps Guru for RDS problem detection works:

- Using thresholds
- Using anomalies

### Detecting problems with thresholds

Thresholds are the bounding values against which the monitored metrics are evaluated.
You can think of a threshold as a horizontal line on a metric chart that separates normal behavior from potentially problematic behavior.
DevOps Guru for RDS monitors specific metrics
and creates thresholds by analyzing what levels are considered potentially problematic for a specified resource. DevOps Guru for RDS then creates insights in the DevOps Guru console
when new metric values cross a specified threshold over a given period of time on a consistent basis. The insights contain recommendations to prevent future database performance impact.

For example, DevOps Guru for RDS might monitor the number of temporary tables using disk over a period of 15 minutes and create an insight
when the rate of temporary tables using disk per second is abnormally high. Increased levels of on-disk temporary table usage might impact the database performance.
By exposing this situation before it becomes critical, DevOps Guru for RDS helps you take corrective actions to prevent problems.

### Detecting problems with anomalies

While thresholds provide a simple and effective way to detect database problems, in some situations they are not sufficient.
Consider a case where metric values are spiking and crossing into potentially problematic behavior on a regular basis because
of a known process, such as a daily reporting job. Since such spikes are expected, creating insights and notifications for each
of them would be counterproductive and would likely lead to alert fatigue.

However, it is still necessary to detect spikes that are highly unusual, since metrics that are much higher than the rest
or last much longer could represent real database performance issues. To address this concern, DevOps Guru for RDS monitors
certain metrics to detect when a metric’s behavior becomes highly unusual or anomalous. DevOps Guru then reports these anomalies
in insights.

For example, DevOps Guru for RDS might create an insight when DB load is not only high, but also significantly deviates from its usual behavior,
which indicates a major unexpected slowdown of database operations. By recognizing only the anomalous DB load spikes,
DevOps Guru for RDS lets you focus on the issues that are truly important.

## DB

load

The key concept for database tuning is the _database load (DB load)_ metric. The DB load represents how
busy your database is at any given time. An increase in DB load means an increase in database
activity.

A _database session_ represents an application's dialogue with a
relational database. An _active session_ is a session that is
in the process of running a database request. A session is active when it's
either running on CPU or waiting for a resource to become available so that it
can proceed. For example, an active session might wait for a page to be read
into memory, and then consume CPU while it reads data from the page.

The `DBLoad` metric in Performance Insights is measured in _average active sessions
(AAS)_. To calculate AAS, Performance Insights samples the number of active sessions every
second. For a specific time period, the AAS is the total number of active sessions divided by the total
number of samples. An AAS value of 2 means that, on average, 2 sessions were active in requests at any
given time.

An analogy for DB load is activity in a warehouse. Suppose that the warehouse employs 100
workers. If 1 order comes in, 1 worker fulfills the order while the other
workers are idle. If 100 or more orders come in, all 100 workers fulfill orders
simultaneously. If you periodically sample how many workers are active over a
given time period, you can calculate the average number of active workers. The
calculation shows that, on average, _N_ workers
are busy fulfilling orders at any given time. If the average was 50 workers
yesterday and 75 workers today, the activity level in the warehouse increased.
In the same way, DB load increases as session activity increases.

To learn more, see [Database load](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.md") in the
_Amazon Aurora User Guide_ or [Database load](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.md") in the
_Amazon RDS User Guide_.

## Wait events

A _wait event_ is a type of database instrumentation that tells you which resource
a database session is waiting for so it can proceed. When Performance Insights counts active sessions to
calculate database load, it also records the wait events that are causing the active sessions to wait.
This technique allows Performance Insights to show you which wait events are contributing to DB
load.

Every active session is either running on the CPU or waiting. For example, sessions
consume CPU when they search memory, perform a calculation, or run procedural
code. When sessions aren't consuming CPU, they might be waiting for a data file
to be read or a log to be written to. The more time that a session waits for
resources, the less time it runs on the CPU.

When you tune a database, you often try to find the resources that sessions are waiting for. For example, two or
three wait events might account for 90% of DB load. This measure means that, on average, active sessions
are spending most of their time waiting for a small number of resources. If you can find out the cause of
these waits, you can try to remedy the problem.

Consider the analogy of a warehouse worker. An order comes in for a book. The worker might be delayed in fulfilling
the order. For example, a different worker might be currently restocking the shelves, or a trolley might
not be available. Or the system used to enter the order status might be slow. The longer the worker
waits, the longer the order takes to fulfill. Waiting is a natural part of the warehouse workflow, but if
wait time become excessive, productivity decreases. In the same way, repeated or lengthy session waits
can degrade database performance.

For more information about wait events in Amazon Aurora, see [Tuning
with wait events for Aurora PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md") and [Tuning with wait events for Aurora MySQL](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.md") in the
_Amazon Aurora User Guide_.

For more information about wait events in other Amazon RDS databases, see [Tuning
with wait events for RDS for PostgreSQL](../../../AmazonRDS/latest/UserGuide/PostgreSQL.md "../../../AmazonRDS/latest/UserGuide/PostgreSQL.md") in the
_Amazon RDS User Guide_.
