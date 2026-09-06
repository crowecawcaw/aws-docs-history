

# Customer pattern catalog
<a name="tn-pattern-catalog"></a>

This catalog grows over time. Each entry documents one recurring customer question and the AWS architectural answer. The structure is intentionally stable — new entries append at the end without changing earlier ones.

## Pattern: Multi-vendor commercial-fleet telemetry quality scoring
<a name="pattern-multi-vendor-commercial-fleet-telemetry-quality-scoring"></a>

Context  
A commercial-fleet OEM receives real-time telemetry from connected assets across multiple divisions/brands under one OEM umbrella. Telemetry arrives via three vendor telemetry stacks representing three generations of a connected-vehicle program: an open third-party telematics platform (factory-installed on new assets), a standards-aligned OEM platform (for example, one whose signal model aligns to the COVESA Vehicle Signal Specification), and a first-party diagnostic/event system that monitors hundreds of diagnostic codes via event-driven alerts rather than continuous sensor signals. All three stacks publish to Apache Kafka topics, but each uses a different schema, different field names, different units, and a different delivery model (continuous sensor stream vs. edge-triggered event vs. periodic aggregate).

What customers ask  
How do we normalize three vendor schemas into a single unified model, and — once we have a unified stream — how do we compute rolling per-asset and per-sensor baselines, detect systematic data quality issues (flatlines, duplicates, sensor drift), flag individual readings that fall outside expected operating ranges, and enrich those readings with reference data (asset model specifications, operating limits, fleet metadata)? We want sub-millisecond access to the per-asset baseline profiles from our REST API and real-time processing tier without querying the data lake on every call.

The AWS pattern  
The eight-step normalization architecture maps directly to this problem shape, with these emphases:  
+  **Step 2 (per-source normalization)** is the heaviest investment in this configuration. Three adapter paths are required — one for the continuous-sensor telematics platform, one for the VSS-aligned OEM platform (which may require resolving signal paths through a signal catalog), and one for the event-driven diagnostic system (which fires alerts, not periodic measurements, so the canonical record model must accommodate sparse/event-shaped payloads alongside dense sensor streams). Each adapter decodes its wire format and emits a common record type to a shared Kafka topic.
+  **Steps 3 and 4 (windowing and stateful processing)** are essential for the diagnostic/event source because that source does not produce a continuous baseline by itself. A stateful Flink job keyed by asset identifier builds the rolling baseline by accumulating events over a configurable window, enabling per-asset and per-sensor trend analysis even when the source only fires on condition change.
+  **Step 5 (pattern detection)** addresses the specific quality issues that arise in mixed-source fleets: flatlines (a sensor reporting the same value beyond a plausible physical dwell, indicating a stuck sensor or lost connection), duplicates (replay or retry producing repeated identical records), and drift (a sensor gradually offsetting from the per-asset baseline, distinguishable from a real physical change only by comparison with history).
+  **Step 6 (anomaly and threshold detection)** compares each reading against expected operating ranges, which vary by asset model and division. Reference data from step 7 supplies the model-specific ranges, so the same threshold logic works across the multi-brand fleet without hard-coding brand-specific constants in the processor.
+  **Step 8 (low-latency baseline store)** uses Amazon ElastiCache for Redis or Valkey to serve per-asset baseline profiles and expected-value ranges to the REST API and any real-time safety or alerting consumers. The baseline store is updated continuously by the Flink job as new telemetry arrives; the durable Iceberg sink on Amazon S3 holds the full history for governed analytical consumption.

Demonstrated in CMS  
The CMS `modules/flink/` Flink processors implement the keyed stateful processing, deduplication, and Redis-sink steps of this pattern for a two-source fleet (IoT FleetWise Edge and OEM cloud connectors). The multi-source adapter pattern (one processor per source, shared output topic) is directly analogous to the three-source configuration described here. Not yet demonstrated in a reference implementation: the event-driven diagnostic source adapter and the cross-brand reference-data join.

Open extensions  
A production deployment of this pattern would also need a signal-catalog service (a low-latency lookup layer that resolves signal IDs to canonical paths for the VSS-aligned source), a reference-data pipeline that keeps asset-model specifications and operating ranges current as fleet composition changes, an alerting/notification consumer that acts on quality flags from the pattern detection step, and a governance layer (Lake Formation row-level security or DataZone subscriptions) for controlled multi-tenant access to the quality-scored telemetry in the durable sink. Any of these can be a follow-on catalog entry or a separately-scoped implementation spec.