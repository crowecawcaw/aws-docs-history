# Online cluster resizing

_Resharding_ involves adding and removing shards or nodes to your
cluster and redistributing key spaces. As a result, multiple things have an
impact on the resharding operation, such as the load on the cluster, memory utilization,
and overall size of data. For the best experience, we recommend that you follow overall
cluster best practices for uniform workload pattern distribution. In addition, we
recommend taking the following steps.

Before initiating resharding, we recommend the following:

- **Test your application** –
  Test your application behavior during resharding in a staging environment if possible.
- **Get early notification for scaling issues** –
  Resharding is a compute-intensive operation. Because of this, we recommend keeping CPU
  utilization under 80 percent on multicore instances and less than 50 percent on
  single core instances during resharding. Monitor ElastiCache for Redis OSS metrics and initiate
  resharding before your application starts observing scaling issues. Useful
  metrics to track are `CPUUtilization`, `NetworkBytesIn`,
  `NetworkBytesOut`, `CurrConnections`,
  `NewConnections`, `FreeableMemory`,
  `SwapUsage`, and `BytesUsedForCacheItems`.
- **Ensure sufficient free memory is available before scaling in**
  – If you're scaling in, ensure that free memory available on the
  shards to be retained is at least 1.5 times the memory used on the shards you
  plan to remove.
- **Initiate resharding during off-peak hours** – This
  practice helps to reduce the latency and throughput impact on the client during
  the resharding operation. It also helps to complete resharding faster as more
  resources can be used for slot redistribution.
- **Review client timeout behavior** – Some clients might
  observe higher latency during online cluster resizing. Configuring your client library
  with a higher timeout can help by giving the system time to connect even under
  higher load conditions on server. In some cases, you might open a large number of connections to
  the server. In these cases, consider adding exponential backoff to reconnect logic. Doing this can help prevent a
  burst of new connections hitting the server at the same time.
- **Load your Functions on every shard** – When scaling out your cluster,
  ElastiCache will automatically replicate the Functions loaded in one of the existing nodes (selected at random) to the new node(s).
  If your cluster has Valkey 7.2 and above, or Redis OSS 7.0 or above, and your application uses [Functions](https://valkey.io/topics/functions-intro/ "https://valkey.io/topics/functions-intro/"), we recommend
  loading all of your functions to all the shards before scaling out so that your cluster does not end up with different functions on different shards.

After resharding, note the following:

- Scale-in might be partially successful if insufficient memory is available on target shards. If such a result occurs, review available memory and retry the operation, if necessary. The data on the target shards will not be deleted.
- `FLUSHALL` and `FLUSHDB` commands are not supported inside Lua scripts during a
  resharding operation. Prior to Redis OSS 6, the `BRPOPLPUSH` command is not supported if it operates on the slot being migrated.
