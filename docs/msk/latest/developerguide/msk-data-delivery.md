# Amazon MSK Data Delivery

With Amazon MSK data delivery, you can deliver Apache Kafka data from Amazon MSK Express brokers directly to Amazon S3, without connectors or additional infrastructure to manage. Amazon MSK Express automatically handles scaling, retries, and backpressure, and manages routine operations such as capacity scaling and version upgrades without introducing delivery gaps. Because these are native broker capabilities, they add no broker egress throughput, so you avoid the incremental infrastructure costs that scaling connector-based pipelines typically incurs and match capacity to actual workload demand rather than provisioning for peak. Each capability supports throughput of up to 10 GBps.

The two capabilities are:

- **Data delivery to streaming tables for Apache Iceberg** — With Amazon MSK Data Delivery, you can continuously materialize Apache Kafka topics as Apache Iceberg tables on Amazon S3 Tables. Intelligent inline compaction eliminates the performance impact of small files and keeps query performance predictable without sacrificing data freshness. Built-in coordination resolves concurrent writer conflicts across high-throughput consumers. Amazon S3 Tables automatically handles ongoing table maintenance, including compaction, snapshot expiration, and unreferenced file cleanup.
- **Data delivery to Amazon S3 general purpose buckets** — With Amazon MSK Data Delivery, you can deliver Apache Kafka data in the source format to Amazon S3 general purpose buckets for downstream processing, with end-to-end reliability for mission-critical workloads. Use it to land Kafka data in Amazon S3 for use cases such as log archival, compliance retention, Kafka replay, and training AI/ML models. This approach removes the need to build self-managed connector pipelines that grow costly and operationally complex as workloads scale.

###### Topics

- [data delivery for streaming tables to Apache Iceberg](msk-data-delivery-iceberg.md "msk-data-delivery-iceberg.md")
- [data delivery to Amazon S3 general purpose buckets](msk-data-delivery-s3.md "msk-data-delivery-s3.md")
