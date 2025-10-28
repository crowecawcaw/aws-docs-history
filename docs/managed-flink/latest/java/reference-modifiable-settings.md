Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Modifiable Flink configuration properties

Following are Flink configuration settings that you can modify using a [support case](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). You can modify more than one
property at a time, and for multiple applications at the same time by specifying the
application prefix. If there are other Flink configuration properties outside this list
you want to modify, specify the exact property in your case.

## Restart strategy

From Flink 1.19 and later, we use the `exponential-delay` restart
strategy by default. All previous versions use the `fixed-delay` restart
strategy by default.

`restart-strategy:`

`restart-strategy.fixed-delay.delay:`

`restart-strategy.exponential-delay.backoff-muliplier:`

`restart-strategy.exponential-delay.initial-backoff:`

`restart-strategy.exponential-delay.jitter-factor:`

`restart-strategy.exponential-delay.reset-backoff-threshold:`

## Checkpoints and state

backends

`state.backend:`

`state.backend.fs.memory-threshold:`

`state.backend.incremental:`

## Checkpointing

`execution.checkpointing.unaligned:`

`execution.checkpointing.interval-during-backlog:`

## RocksDB native metrics

RocksDB Native Metrics are not shipped to CloudWatch. Once enabled, these metrics can be accessed either from the Flink dashboard or the
Flink REST API with custom tooling.

Managed Service for Apache Flink enables customers to access the latest Flink [REST API](https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/ops/rest_api/ "https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/ops/rest_api/") (or
the supported version you are using) in read-only mode using the [CreateApplicationPresignedUrl](../apiv2/API_CreateApplicationPresignedUrl.md "../apiv2/API_CreateApplicationPresignedUrl.md") API.
This API is used by Flink’s own dashboard, but it can also be used by custom monitoring tools.

`state.backend.rocksdb.metrics.actual-delayed-write-rate:`

`state.backend.rocksdb.metrics.background-errors:`

`state.backend.rocksdb.metrics.block-cache-capacity:`

`state.backend.rocksdb.metrics.block-cache-pinned-usage:`

`state.backend.rocksdb.metrics.block-cache-usage:`

`state.backend.rocksdb.metrics.column-family-as-variable:`

`state.backend.rocksdb.metrics.compaction-pending:`

`state.backend.rocksdb.metrics.cur-size-active-mem-table:`

`state.backend.rocksdb.metrics.cur-size-all-mem-tables:`

`state.backend.rocksdb.metrics.estimate-live-data-size:`

`state.backend.rocksdb.metrics.estimate-num-keys:`

`state.backend.rocksdb.metrics.estimate-pending-compaction-bytes:`

`state.backend.rocksdb.metrics.estimate-table-readers-mem:`

`state.backend.rocksdb.metrics.is-write-stopped:`

`state.backend.rocksdb.metrics.mem-table-flush-pending:`

`state.backend.rocksdb.metrics.num-deletes-active-mem-table:`

`state.backend.rocksdb.metrics.num-deletes-imm-mem-tables:`

`state.backend.rocksdb.metrics.num-entries-active-mem-table:`

`state.backend.rocksdb.metrics.num-entries-imm-mem-tables:`

`state.backend.rocksdb.metrics.num-immutable-mem-table:`

`state.backend.rocksdb.metrics.num-live-versions:`

`state.backend.rocksdb.metrics.num-running-compactions:`

`state.backend.rocksdb.metrics.num-running-flushes:`

`state.backend.rocksdb.metrics.num-snapshots:`

`state.backend.rocksdb.metrics.size-all-mem-tables:`

## RocksDB options

`state.backend.rocksdb.compaction.style:`

`state.backend.rocksdb.memory.partitioned-index-filters:`

`state.backend.rocksdb.thread.num:`

## Advanced state

backends options

`state.storage.fs.memory-threshold:`

## Full TaskManager options

`task.cancellation.timeout:`

`taskmanager.jvm-exit-on-oom:`

`taskmanager.numberOfTaskSlots:`

`taskmanager.slot.timeout:`

`taskmanager.network.memory.fraction:`

`taskmanager.network.memory.max:`

`taskmanager.network.request-backoff.initial:`

`taskmanager.network.request-backoff.max:`

`taskmanager.network.memory.buffer-debloat.enabled:`

`taskmanager.network.memory.buffer-debloat.period:`

`taskmanager.network.memory.buffer-debloat.samples:`

`taskmanager.network.memory.buffer-debloat.threshold-percentages:`

## Memory configuration

`taskmanager.memory.jvm-metaspace.size:`

`taskmanager.memory.jvm-overhead.fraction:`

`taskmanager.memory.jvm-overhead.max:`

`taskmanager.memory.managed.consumer-weights:`

`taskmanager.memory.managed.fraction:`

`taskmanager.memory.network.fraction:`

`taskmanager.memory.network.max:`

`taskmanager.memory.segment-size:`

`taskmanager.memory.task.off-heap.size:`

## RPC / Akka

`akka.ask.timeout:`

`akka.client.timeout:`

`akka.framesize:`

`akka.lookup.timeout:`

`akka.tcp.timeout:`

## Client

`client.timeout:`

## Advanced cluster options

`cluster.intercept-user-system-exit:`

`cluster.processes.halt-on-fatal-error:`

## Filesystem

configurations

`fs.s3.connection.maximum:`

`fs.s3a.connection.maximum:`

`fs.s3a.threads.max:`

`s3.upload.max.concurrent.uploads:`

## Advanced fault

tolerance options

`heartbeat.timeout:`

`jobmanager.execution.failover-strategy:`

## Memory configuration

`jobmanager.memory.heap.size:`

## Metrics

`metrics.latency.interval:`

## Advanced options for the REST endpoint and

client

`rest.flamegraph.enabled:`

`rest.server.numThreads:`

## Advanced SSL security options

`security.ssl.internal.handshake-timeout:`

## Advanced scheduling options

`slot.request.timeout:`

## Advanced options for Flink web UI

`web.timeout:`
