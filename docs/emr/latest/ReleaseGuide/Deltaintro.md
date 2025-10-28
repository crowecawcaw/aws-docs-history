# Introduction to Delta Lake

Delta Lake is an open-source project that helps implement modern data lake architectures
commonly built on Amazon S3. Delta Lake offers the following capabilities:

- Atomic, consistent, isolated, durable (ACID) transactions on Spark. Readers
  see a consistent view of the table during a Spark job.
- Scalable metadata handling with distributed processing by Spark.
- Combines streaming and batch uses cases with the same Delta table.
- Automatic schema enforcement to avoid bad records during data
  ingestion.
- Time travel with data versioning.
- Supports merge, update, and delete operations for complex use cases like
  change data capture (CDC), streaming upserts, and more.
