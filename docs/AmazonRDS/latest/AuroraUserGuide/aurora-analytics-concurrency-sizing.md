

# Concurrency sizing
<a name="aurora-analytics-concurrency-sizing"></a>

Higher `query_mem` gives each query more memory but leaves room for fewer queries at once, so how many foreign table queries you can run concurrently depends on instance memory and per-query `query_mem`.

As a rough guide, with the default `shared_buffers`, keep the combined `query_mem` of concurrent queries within about 30 percent of instance memory (peak memory). You can estimate this as (instance memory x 0.3) / `query_mem` per query.

Rising query failure rates, memory usage above 90 percent, or query latencies that climb sharply as more queries run are signs that you are reaching this limit.

To stay within it, lower `query_mem` per query, move to a larger instance class, or limit how many foreign table queries run at the same time so they queue instead of competing for memory (for example, with a bounded worker pool or a concurrency limit in your application).