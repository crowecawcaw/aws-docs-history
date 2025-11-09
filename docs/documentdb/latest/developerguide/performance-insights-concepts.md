# Performance Insights concepts

###### Topics

- [Average active
  sessions](#performance-insights-concepts-sessions "#performance-insights-concepts-sessions")
- [Dimensions](#performance-insights-concepts-dimensions "#performance-insights-concepts-dimensions")
- [Max vCPU](#performance-insights-concepts-maxvcpu "#performance-insights-concepts-maxvcpu")

## Average active

sessions

Database load (DB load) measures the level of activity in your database. The key
metric in Performance Insights is `DB Load`, which is collected every
second. The unit for the `DBLoad` metric is the _Average Active Sessions (AAS)_ for an Amazon DocumentDB instance.

An _active_ session is a connection that has
submitted work to the Amazon DocumentDB instance and is waiting for a response. For
example, if you submit a query to an Amazon DocumentDB instance, the database session is
active while the instance is processing the query.

To obtain the average active sessions, Performance Insights samples the number of
sessions concurrently running a query. The AAS is the total number of sessions
divided by the total number of samples. The following table shows five consecutive
samples of a running query.

| Sample | Number of sessions running query | AAS | Calculation             |
| ------ | -------------------------------- | --- | ----------------------- |
| 1      | 2                                | 2   | 2 sessions / 1 sample   |
| 2      | 0                                | 1   | 2 sessions / 2 samples  |
| 3      | 4                                | 2   | 6 sessions / 3 samples  |
| 4      | 0                                | 1.5 | 6 sessions / 4 samples  |
| 5      | 4                                | 2   | 10 sessions / 5 samples |

In the preceding example, the DB Load for the time interval from 1-5 is 2 AAS. An
increase in DB load means that, on average, more sessions are running on the
database.

## Dimensions

The `DB Load` metric is different from the other time-series metrics
because you can break it into subcomponents called dimensions. You can think of
dimensions as categories for the different characteristics of the `DB
 Load` metric. When you are diagnosing performance issues, the most useful
dimensions are **wait states** and **top query**.

###### wait states

A _wait state_ causes a query statement to
wait for a specific event to happen before it can continue running. For example,
a query statement might wait until a locked resource is unlocked. By combining
`DB Load` with wait states, you can get a complete picture of the
session state. Here are various Amazon DocumentDB wait states:

| Amazon DocumentDB wait state | Wait State Description                                                                                                                                                                                                                                                                                                                                |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Latch                        | The Latch wait state occurs when the session is waiting to<br>page the buffer pool. Frequent paging in and out of the buffer<br>pool can happen more often when there are frequent large queries<br>being processed by the system, collection scans, or when the<br>buffer pool is too small to handle the working set.                               |
| CPU                          | The CPU wait state occurs when the session is waiting on<br>CPU.                                                                                                                                                                                                                                                                                      |
| CollectionLock               | The CollectionLock wait state occurs when the session is<br>waiting to acquire a lock on the collection. These events occur<br>when there are DDL operations on the collection.                                                                                                                                                                       |
| DocumentLock                 | The DocumentLock wait state occurs when the session is waiting<br>to acquire a lock on a document. High number of concurrent<br>writes to the same document will contribute to more DocumentLock<br>wait states on that document.                                                                                                                     |
| SystemLock                   | The SystemLock wait state occurs when the session is waiting<br>on the system. This can occur when there are frequent long<br>running queries, long running transactions, or high concurrency<br>on the system.                                                                                                                                       |
| IO                           | The IO wait state occurs when the session waiting on IO to<br>complete.                                                                                                                                                                                                                                                                               |
| BufferLock                   | The BufferLock wait state occurs when the session is waiting<br>to acquire a lock on a shared page in the buffer. BufferLock<br>wait states can be prolonged if other processes are holding open<br>cursors on the requested pages.                                                                                                                   |
| LowMemThrottle               | The LowMemThrottle wait state occurs when the session is<br>waiting due to heavy memory pressure on the Amazon DocumentDB<br>instance. If this state persists for a long time, consider<br>scaling up the instance to provide additional memory. For more<br>information, see [Resource Governor](how-it-works.md "how-it-works.md").                 |
| BackgroundActivity           | The BackgroundActivity wait state occurs when the session is<br>waiting on internal system processes.                                                                                                                                                                                                                                                 |
| Other                        | The Other wait state is an internal wait state. If this state<br>persists for a long time, consider terminating this query. For<br>more information, see [How Do I Find and Terminate Long Running or Blocked<br>Queries?](user_diagnostics.md#user_diagnostics-query_terminating.html "user_diagnostics.md#user_diagnostics-query_terminating.html") |

###### Top queries

Whereas wait states show bottlenecks, top queries show which queries are
contributing the most to DB load. For example, many queries might be currently
running on the database, but a single query might consume 99% of the DB load. In
this case, the high load might indicate a problem with the query.

## Max vCPU

In the dashboard, the **Database load** chart
collects, aggregates, and displays session information. To see whether active
sessions are exceeding the maximum CPU, look at their relationship to the **Max vCPU** line. The **Max
vCPU** value is determined by the number of vCPU (virtual CPU) cores
for your Amazon DocumentDB instance.

If the DB load is often above the **Max vCPU** line,
and the primary wait state is CPU, the CPU is overloaded. In this case, you might
want to throttle connections to the instance, tune any queries with a high CPU load,
or consider a larger instance class. High and consistent instances of any wait state
indicate that there might be bottlenecks or resource contention issues to resolve.
This can be true even if the DB load doesn't cross the **Max
vCPU** line.
