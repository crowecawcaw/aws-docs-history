

# Programmatic Flink configuration properties
<a name="programmatic-configuration"></a>

Following are Flink configuration properties that you can modify directly in your application code. Starting with MSF 2.2, an exception will be thrown if you try to modify a property not listed on this page in your application code.

**Note**  
These properties are distinct from settings modified via AWS Support case. For infrastructure-level settings such as TaskManager memory, state backend, RocksDB tuning, and restart strategies, see [Modifiable Flink configuration properties](reference-modifiable-settings.md).

## Pipeline configuration
<a name="programmatic-configuration-pipeline"></a>

`execution.runtime-mode`

`pipeline.auto-generate-uids`

`pipeline.auto-watermark-interval`

`pipeline.cached-files`

`pipeline.classpaths`

`pipeline.closure-cleaner-level`

`pipeline.force-avro`

`pipeline.force-kryo`

`pipeline.generic-types`

`pipeline.global-job-parameters`

`pipeline.jars`

`pipeline.jobvertex-parallelism-overrides`

`pipeline.max-parallelism`

`pipeline.name`

`pipeline.object-reuse`

`pipeline.operator-chaining.chain-operators-with-different-max-parallelism`

`pipeline.operator-chaining.enabled`

`pipeline.serialization-config`

`pipeline.vertex-description-mode`

`pipeline.vertex-name-include-index-prefix`

`pipeline.watermark-alignment.allow-unaligned-source-splits`

## Network
<a name="programmatic-configuration-network"></a>

`taskmanager.network.adaptive-partitioner.enabled`

`taskmanager.network.adaptive-partitioner.max-traverse-size`

## Python API
<a name="programmatic-configuration-python"></a>

`python.execution-mode`

`python.operator-chaining.enabled`

`python.job-options`

`python.internal.archives-key-map`

`python.internal.files-key-map`

`python.internal.requirements-file-key`

## Table API / SQL
<a name="programmatic-configuration-table-api"></a>

`table.exec.async-lookup.buffer-capacity`

`table.exec.async-lookup.key-ordered-enabled`

`table.exec.async-lookup.output-mode`

`table.exec.async-lookup.timeout`

`table.exec.async-ml-predict.max-concurrent-operations`

`table.exec.async-ml-predict.output-mode`

`table.exec.async-ml-predict.timeout`

`table.exec.async-scalar.max-concurrent-operations`

`table.exec.async-scalar.max-attempts`

`table.exec.async-scalar.retry-delay`

`table.exec.async-scalar.retry-strategy`

`table.exec.async-scalar.timeout`

`table.exec.async-state.enabled`

`table.exec.async-table.max-concurrent-operations`

`table.exec.async-table.max-retries`

`table.exec.async-table.retry-delay`

`table.exec.async-table.retry-strategy`

`table.exec.async-table.timeout`

`table.exec.async-vector-search.max-concurrent-operations`

`table.exec.async-vector-search.output-mode`

`table.exec.async-vector-search.timeout`

`table.exec.deduplicate.insert-update-after-sensitive-enabled`

`table.exec.deduplicate.mini-batch.compact-changes-enabled`

`table.exec.delta-join.cache-enabled`

`table.exec.disabled-operators`

`table.exec.iceberg.use-v2-sink`

`table.exec.interval-join.min-cleanup-interval`

`table.exec.legacy-cast-behaviour`

`table.exec.local-hash-agg.adaptive.distinct-value-rate-threshold`

`table.exec.local-hash-agg.adaptive.enabled`

`table.exec.local-hash-agg.adaptive.sampling-threshold`

`table.exec.mini-batch.allow-latency`

`table.exec.mini-batch.enabled`

`table.exec.mini-batch.size`

`table.exec.operator-fusion-codegen.enabled`

`table.exec.simplify-operator-name-enabled`

`table.exec.sink.keyed-shuffle`

`table.exec.sink.nested-constraint-enforcer`

`table.exec.sink.not-null-enforcer`

`table.exec.sink.rowtime-inserter`

`table.exec.sink.type-length-enforcer`

`table.exec.sink.upsert-materialize`

`table.exec.sink.upsert-materialize-strategy.adaptive.threshold.high`

`table.exec.sink.upsert-materialize-strategy.adaptive.threshold.low`

`table.exec.sink.upsert-materialize-strategy.type`

`table.exec.sort.async-merge-enabled`

`table.exec.sort.default-limit`

`table.exec.sort.max-num-file-handles`

`table.exec.source.cdc-events-duplicate`

`table.exec.source.idle-timeout`

`table.exec.spill-compression.block-size`

`table.exec.spill-compression.enabled`

`table.exec.state.ttl`

`table.exec.uid.format`

`table.exec.uid.generation`

`table.exec.unbounded-over.version`

`table.exec.window-agg.buffer-size-limit`

`table.optimizer.agg-phase-strategy`

`table.optimizer.adaptive-broadcast-join.strategy`

`table.optimizer.bushy-join-reorder-threshold`

`table.optimizer.delta-join.strategy`

`table.optimizer.distinct-agg.split.bucket-num`

`table.optimizer.distinct-agg.split.enabled`

`table.optimizer.dynamic-filtering.enabled`

`table.optimizer.incremental-agg-enabled`

`table.optimizer.join-reorder-enabled`

`table.optimizer.multi-join.enabled`

`table.optimizer.multiple-input-enabled`

`table.optimizer.non-deterministic-update.strategy`

`table.optimizer.reuse-optimize-block-with-digest-enabled`

`table.optimizer.reuse-sink-enabled`

`table.optimizer.reuse-source-enabled`

`table.optimizer.reuse-sub-plan-enabled`

`table.optimizer.runtime-filter.enabled`

`table.optimizer.skewed-join-optimization.skewed-factor`

`table.optimizer.skewed-join-optimization.skewed-threshold`

`table.optimizer.skewed-join-optimization.strategy`

`table.optimizer.source.report-statistics-enabled`

`table.optimizer.union-all-as-breakpoint-enabled`

`table.builtin-catalog-name`

`table.builtin-database-name`

`table.catalog-modification.listeners`

`table.column-expansion-strategy`

`table.display.max-column-width`

`table.dml-sync`

`table.dynamic-table-options.enabled`

`table.generated-code.max-length`

`table.legacy-nested-row-nullability`

`table.local-time-zone`

`table.plan.compile.catalog-objects`

`table.plan.force-recompile`

`table.plan.restore.catalog-objects`

`table.rtas-ctas.atomicity-enabled`

`table.sql-dialect`