# Amazon Kinesis Video Streams Tiered Storage

Amazon Kinesis Video Streams Tiered Storage enables you to optimize costs associated with storing and consuming media based on
expected consumption needs, data access frequency, and retention length. KVS offers two storage tiers
to help you balance cost and performance requirements.

###### Topics

- [Overview](#tiered-storage-overview "#tiered-storage-overview")
- [Key Concepts](#tiered-storage-overview-key-concept "#tiered-storage-overview-key-concept")
- [Setting up Tiered Storage](#tiered-storage-create-stream-warm-tier "#tiered-storage-create-stream-warm-tier")
- [Best practices](#tiered-storage-best-practices "#tiered-storage-best-practices")

## Overview

Kinesis Video Streams offers 2 storage tiers:

- **Kinesis Video Streams Standard (Hot) Tier** – Provides immediate access with lowest latency for frequently
  accessed media.
- **Kinesis Video Streams Warm Tier** – Cost-effective for use cases where media is stored for a longer duration,
  and is accessed less frequently, but requires rapid access when needed.

## Key Concepts

Understanding these concepts will help you configure optimal storage policies:

- **Storage cost** – Warm tier is cheaper than the Hot tier.
- **Ingestion cost** – Warm tier charges per 1000 fragments while Hot tier charges per 1 GB of media ingested.
- **Minimum Storage duration** – Warm tier storage is charged for a minimum storage duration of 30 days.
  If media is deleted or moved before this 30-day period, you will incur the normal storage usage charge plus a pro-rated charge for the remainder of the minimum storage duration.
  Media stored for longer than the minimum storage duration will not incur a minimum charge.
- **Latency** – Slight increase (milliseconds) in ingestion, and consumption latency when media is stored in the Warm tier.

## Setting up Tiered Storage

**Create a new stream with Warm Tier Ingestion**

1. Open the console at [https://console.aws.amazon.com//kinesisvideo/home](https://console.aws.amazon.com//kinesisvideo/home "https://console.aws.amazon.com//kinesisvideo/home").
2. On the **Video streams** page, choose
   **Create video stream**.
3. On the **Create a new video stream** page, enter
   `YourStreamName` for
   the stream name.
4. Choose **Custom configuration**. Set a **Data Retenion** (e.g `31 days`).
   Set **Storage tier** as `Warm tier`.
5. Choose **Create video stream**.
6. After Amazon Kinesis Video Streams creates the stream, review the details on the
   **YourStreamName** page.

**Your stream will now ingest media directly into the Warm Tier, providing immediate access with lowest latency.**

## Best practices

- Analyze your media access patterns before selecting storage tiers
- Use Hot tier for frequently accessed media requiring immediate access
- Configure Warm tier for media accessed occasionally with acceptable slight latency
- Consider total cost of ownership including storage and retrieval costs
