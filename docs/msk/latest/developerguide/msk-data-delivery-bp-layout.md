# S3 object layout (S3 bucket)

- Choose an output key template with time-based placeholders that matches how you query the data downstream.
- Use GZIP or ZSTD compression to reduce storage costs for text-based payloads; choose the storage class (`STANDARD`, `INTELLIGENT_TIERING`, `GLACIER_IR`) based on access patterns.
