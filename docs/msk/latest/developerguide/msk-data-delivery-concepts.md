# Key concepts

This section describes the key concepts behind Amazon MSK Data Delivery.

- **Data freshness vs. throughput (Iceberg)** — A Channel needs at least 2.4 MB/s of uncompressed throughput for the minimum 5-minute freshness. For lower-throughput topics, increase freshness (up to 15 minutes) so the service can accumulate enough data for efficient delivery and inline compaction.
- **Input formats (Iceberg)** — `JSON` (plain JSON; you provide a GSR schema ARN) and `JSON_SCHEMA_GSR` (GSR-serialized JSON with the schema ID embedded in each record) are supported. The AWS Glue Schema Registry (GSR) is the source of truth, and the Channel fails to create if the schema cannot be resolved.
- **Schema evolution (Iceberg)** — Not supported. Changing the schema after creation can cause delivery failures.
- **Record converters (S3 bucket)** — The S3 destination supports JSON, ByteArray, and String converters and does not require a schema registry.
- **Object layout (S3 bucket)** — Delivered objects are named using a configurable output key template with time-based placeholders (for example, `year=!{yyyy}/month=!{MM}/day=!{dd}/hour=!{HH}`), plus compression (NONE, GZIP, or ZSTD) and storage class options.
- **Partitioning (Iceberg)** — S3 Tables delivery supports time-based partitioning only.
- **No backfill** — only records produced after enablement are delivered.
- **New table per channel (Iceberg)** — each Channel creates its own Iceberg table.
- **Dead-letter queue** — both destinations require a DLQ S3 bucket. The Channel writes the identifiers (sequence numbers) of unprocessable records, along with error context — not the full record payloads.
