

# Key concepts
<a name="msk-data-delivery-s3-concepts"></a>

This section describes the key concepts behind Amazon MSK Data Delivery.
+ **Record converters** — The S3 destination supports JSON, ByteArray, and String converters and does not require a schema registry.
+ **Object layout** — Delivered objects are named using a configurable output key template with time-based placeholders (for example, `year=!{yyyy}/month=!{MM}/day=!{dd}/hour=!{HH}`), plus compression (NONE, GZIP, or ZSTD) and storage class options.
+ **Data freshness** — Data freshness is configured between 5 and 15 minutes (`DataFreshnessInSeconds`, 300–900, default 600).
+ **Batching** — The Channel writes multiple records into each S3 object (a batch).
+ **No backfill** — only records produced after enablement are delivered.
+ **Dead-letter queue** — both destinations require a DLQ S3 bucket. The Channel writes the identifiers (sequence numbers) of unprocessable records, along with error context — not the full record payloads.