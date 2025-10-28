# Recommendations for using Gremlin write-requests in Lambda

If your Lambda function modifies graph data, consider adopting a back-off-and-retry
strategy to handle the following exceptions:

- **`ConcurrentModificationException`**   –  
  The Neptune transaction semantics mean that write requests sometimes fail
  with a `ConcurrentModificationException`. In these situations, try
  an exponential back-off-based retry mechanism.
- **`ReadOnlyViolationException`**   –  
  Because the cluster topology can change at any moment as a result of planned or
  unplanned events, write responsibilities may migrate from one instance in the
  cluster to another. If your function code attempts to send a write request to
  an instance that is no longer the primary (writer) instance, the request fails
  with a `ReadOnlyViolationException`. When this happens, close the
  existing connection, reconnect to the cluster endpoint, and then retry the request.
  Also, if you use a back-off-and-retry strategy to handle write request issues,
  consider implementing idempotent queries for create and update requests (for example,
  using [fold().coalesce().unfold()](http://kelvinlawrence.net/book/Gremlin-Graph-Guide.html#upsert "http://kelvinlawrence.net/book/Gremlin-Graph-Guide.html#upsert").
