# Monitoring Channel

A Channel publishes data-delivery metrics to Amazon CloudWatch under the `AWS/Kafka` namespace. The metric set depends on the destination type: `DeliveryToIceberg.*` for S3 Tables and `DeliveryToS3.*` for S3 buckets.

###### Topics

- [Amazon CloudWatch metrics — S3 Tables (Iceberg) destination](msk-data-delivery-metrics-iceberg.md "msk-data-delivery-metrics-iceberg.md")
- [Amazon CloudWatch metrics — S3 bucket destination](msk-data-delivery-metrics-s3.md "msk-data-delivery-metrics-s3.md")
- [Metric dimensions](msk-data-delivery-metric-dimensions.md "msk-data-delivery-metric-dimensions.md")
- [Recommended alarms](msk-data-delivery-alarms.md "msk-data-delivery-alarms.md")
- [Viewing metrics in the console](msk-data-delivery-viewing-metrics.md "msk-data-delivery-viewing-metrics.md")
