

# Recommendations for using Gremlin write-requests in Lambda
<a name="lambda-functions-gremlin-write-recommendations"></a>

If your Lambda function modifies graph data, consider adopting a back-off-and-retry strategy to handle the following exceptions. For detailed guidance on developing a practical retry strategy, see [Exception Handling and Retries](transactions-exceptions.md).
+ **`ConcurrentModificationException`**   –   The Neptune transaction semantics mean that write requests sometimes fail with a `ConcurrentModificationException`. In these situations, try an exponential back-off-based retry mechanism.
+ **`ReadOnlyViolationException`**   –   Because the cluster topology can change at any moment as a result of planned or unplanned events, write responsibilities may migrate from one instance in the cluster to another. If your function code attempts to send a write request to an instance that is no longer the primary (writer) instance, the request fails with a `ReadOnlyViolationException`. When this happens, close the existing connection, reconnect to the cluster endpoint, and then retry the request.

Also, if you use a back-off-and-retry strategy to handle write request issues, consider implementing idempotent queries for create and update requests using [Making efficient upserts with Gremlin `mergeV()` and `mergeE()` steps](gremlin-efficient-upserts.md).