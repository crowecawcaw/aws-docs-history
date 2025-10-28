# Using CloudWatch to monitor DB instance

performance in Neptune

You can use CloudWatch metrics in Neptune to monitor what is happening on
your DB instances and keep track of the query queue length as observed by the
database. The following metrics are particularly useful:

- **`CPUUtilization`**   –  
  Shows the percentage of CPU utilization.
- **`VolumeWriteIOPs`**   –  
  Shows the average number of disk I/O writes to the cluster volume, reported at 5-minute intervals.
- **`MainRequestQueuePendingRequests`**
    –   Shows the number of requests waiting in the input queue pending execution.
  You can also find out how many requests are pending on the server by using the
  [Gremlin query status endpoint](gremlin-api-status.md "gremlin-api-status.md") with the
  `includeWaiting` parameter. This will give you the status of all waiting
  queries.

The following indicators can help you adjust your Neptune provisioning
and query strategies to improve efficiency and performance:

- Consistent latency, high `CPUUtilization`, high
  `VolumeWriteIOPs` and low `MainRequestQueuePendingRequests`
  together show that the server is actively engaged processing concurrent write
  requests at a sustainable rate, with little I/O wait.
- Consistent latency, low `CPUUtilization`, low
  `VolumeWriteIOPs` and no `MainRequestQueuePendingRequests`
  together show that you have excess capacity on the primary DB instance
  for processing write requests.
- High `CPUUtilization` and high `VolumeWriteIOPs`
  but variable latency and `MainRequestQueuePendingRequests` together
  show that you are sending more work than the server can process in a given interval.
  Consider creating or resizing batch requests so as to do the same amount of work
  with less transactional overhead and/or scaling the primary instance up to increase
  the number of query threads capable of processing write requests
  concurrently.
- Low `CPUUtilization` with high `VolumeWriteIOPs`
  mean that query threads are waiting for I/O operations to the storage layer to
  complete. If you see variable latencies and some increase in
  `MainRequestQueuePendingRequests`, consider creating or resizing batch
  requests so as to do the same amount of work with less transactional overhead.
