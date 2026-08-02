# Prerequisites

1. An Amazon MSK Provisioned cluster with Express brokers.
2. A Kafka topic producing data in a supported format for your destination.
3. An S3 bucket for the dead-letter queue (DLQ) — **required**.
4. An IAM service role (see [IAM permissions for Channel](msk-data-delivery-iam.md "msk-data-delivery-iam.md")).
5. **(Iceberg only)** A schema registered in AWS Glue Schema Registry that matches the topic data, and an S3 Table bucket in the same AWS Region as the cluster.
6. **(S3 only)** A general-purpose S3 bucket for data delivery.
7. (Optional) A customer-managed KMS key for encryption at rest.
