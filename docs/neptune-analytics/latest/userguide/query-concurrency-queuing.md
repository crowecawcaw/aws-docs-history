

# Concurrency and query queuing in Neptune Analytics
<a name="query-concurrency-queuing"></a>

When developing and tuning graph applications, it can be helpful to know the implications of sending parallel requests to an Neptune Analytics graph and how queries are being queued.

## Concurrency
<a name="query-concurrency"></a>

All queries submitted to an Neptune Analytics graph enter a FIFO queue. The number of worker threads that process queries from this queue is determined by the graph size: specifically, the number of m-NCUs divided by four. For example, a 128 m-NCU graph has 32 worker threads, and a 16 m-NCU graph has 4.

The effective concurrency you can expect depends on the nature of your workload:
+ **Compute-bound workloads** (openCypher queries, graph algorithms) – Plan for approximately 1 concurrent query per 8 m-NCU. These workloads operate primarily on in-memory data and are CPU-intensive, so each query fully utilizes a vCPU for the duration of its execution.
+ **I/O-bound workloads** (bulk data loading from Amazon S3, `neptune.read()` operations) – Plan for up to 1 concurrent query per 4 m-NCU. These workloads spend significant time waiting on I/O, which allows the CPU to service other requests during wait periods.

Some operations can consume multiple worker threads. This is particularly important for queries that use graph algorithms. When an algorithm has a `concurrency` parameter greater than `1`, the request attempts to consume up to that many threads.

**Note**  
These are guidelines for planning and sizing purposes, not guarantees. Actual concurrency varies based on query complexity, graph structure, and data access patterns. Monitor query queue depth as the primary indicator of back pressure and adjust your graph size accordingly.

## Query queuing
<a name="query-queuing"></a>

Query queuing occurs when the number of concurrent requests exceeds the available worker threads (m-NCU / 4). Queued queries wait in FIFO order until a worker thread becomes available.

The maximum number of queries that can be queued per graph, regardless of graph size, is 8,192. Any queries beyond that limit are rejected with a `ThrottlingException`.

Query latency includes the time a query spends in the queue, network round-trip time, and the actual execution time.

## Monitoring ongoing and queued requests
<a name="query-monitoring-queued"></a>

Neptune Analytics provides a [ListQueries](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListQueries.html) API that you can use to see any active or queued queries. To see all actively executing queries and all queries in the queue, use the `state` parameter set to `ALL`. By default, the ListQueries API only displays actively running queries. The following is an example AWS CLI call:

```
aws neptune-graph list-queries --graph-identifier {{g-12345abcde}} \
    --state ALL \
    --max-results 100
```

Requests are marked with a status of `RUNNING`, `WAITING`, or `CANCELING`. Queries in a `WAITING` state are queued.

Queued requests can also be monitored using the `NumQueuedRequestsPerSec` CloudWatch metric. This metric reports the number of requests that were queued over time.

## How query queuing can affect timeouts
<a name="query-queuing-timeouts"></a>

Query latency includes the time a query spends in the queue as well as the time it takes to execute.

Because a query's timeout period is generally measured starting from when it enters the queue, a slow-moving queue can make many queries time out as soon as they are dequeued. To avoid this, don't queue a large number of queries unless they can be executed rapidly.