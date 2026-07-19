# The normalization pattern

The following eight-step architecture describes the evergreen shape of a production telemetry normalization system. It is service-agnostic at the conceptual level and maps to named AWS services in the subsection below.

1. **Multi-source ingestion** — Heterogeneous vendor schemas arrive over a common transport. Apache Kafka is the dominant real-world choice for this tier; Amazon MSK is the AWS-managed option.
2. **Per-source schema normalization** — One decode/adapter path per vendor schema, converging on a shared event model. Each source requires its own mapping logic (field renames, nested-path extraction, type coercion, unit conversions), but all paths emit the same canonical record type downstream.
3. **Windowing and aggregation** — Rolling per-entity baselines are computed using tumbling or sliding windows over a keyed stream. This produces the baseline profiles (rolling averages, recent maximums, rate-of-change metrics) that later steps compare against.
4. **Stateful processing** — Per-entity history is tracked across events. In a keyed stream processor, this means maintaining per-VIN (or per-sensor, per-asset) state that survives individual records and is updated continuously as new telemetry arrives.
5. **Pattern detection** — Systematic data quality issues are identified against recent history: flatline detection (the same value repeated beyond a plausible physical dwell time), duplicate suppression (identical records from retry/replay), and drift detection (gradual sensor offset against the per-entity baseline).
6. **Anomaly and threshold detection** — Individual readings are compared against expected ranges derived from reference data. Readings outside the expected band for that entity’s class, model, or operating context are flagged for downstream consumers.
7. **Reference-data enrichment** — The normalized stream is joined against slowly-changing dimensions: asset specifications (vehicle model, sensor operating ranges, equipment class), fleet metadata, and customer-defined thresholds. These dimensions inform both the anomaly detection step and the richness of the analytical sink.
8. **Low-latency baseline store** — Per-entity baseline profiles and expected-value ranges are written to a low-latency key-value store (Amazon ElastiCache for Redis or Valkey) for sub-millisecond lookups by downstream consumers — REST APIs, safety processors, real-time dashboards — without querying the durable analytical layer on every request.

## AWS service pairing

The named AWS service mapping for this pattern:

- **Amazon MSK** (Apache Kafka) or **Amazon Kinesis Data Streams** — multi-source ingestion transport, one topic or stream shard per vendor schema (or per vendor + entity-class combination for higher-volume deployments)
- **Amazon Managed Service for Apache Flink** — stateful keyed processing for steps 2 through 6: per-source normalization, windowing, stateful history, pattern detection, anomaly detection; Flink’s keyed state backend carries per-entity history without external coordination
- **Amazon ElastiCache for Redis / Valkey** — baseline store (step 8): sub-millisecond reads of per-entity profiles and expected-value ranges; also used as the latest-state cache for REST API consumers
- **Durable analytical sink** — Apache Iceberg on Amazon S3 via the platform foundation’s existing data-product pattern, or a customer’s own Glue/Athena configuration; this is where the quality-scored, reference-enriched telemetry lands for governed consumption
