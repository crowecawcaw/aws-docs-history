# Query queuing in Amazon Neptune

When developing and tuning graph applications, it can be helpful to know the
implications of how queries are being queued by the database. In Amazon Neptune,
query queuing occurs as follows:

- The maximum number of queries that can be queued up per instance,
  regardless of the instance size, is 8,192. Any queries over that number are rejected
  and fail with a `ThrottlingException`.
- The maximum number of queries that can be executing at one time is
  determined by the number of worker threads assigned, which is generally set to
  twice the number of virtual CPU cores (vCPUs) that are available.
- Query latency includes the time a query spends in the queue as well
  as network round-tripping and the time it actually takes to execute.

## Determining how many queries are in your queue at a given moment

The `MainRequestQueuePendingRequests` CloudWatch metric records the
the number of requests waiting in the input queue at a five-minutes granularity (see [Neptune CloudWatch Metrics](cw-metrics.md "cw-metrics.md")).

For Gremlin, you can obtain a current count of queries in the queue using the
`acceptedQueryCount` value returned by the [Gremlin query status API](gremlin-api-status.md "gremlin-api-status.md"). Note, however, that the `acceptedQueryCount`
value returned by the [SPARQL query status API](sparql-api-status.md "sparql-api-status.md")
includes all queries accepted since the server was started, including completed queries.

## How query queuing can affect timeouts

As noted above, query latency includes the time a query spends in the queue as well
as the time it takes to execute.

Because a query's timeout period is generally measured starting from when it enters
the queue, a slow-moving queue can make many queries time out as soon as they are
dequeued. This is obviously undesirable, so it is good to avoid queuing up a large number
of queries unless they can be executed rapidly.
