

# Prerequisites
<a name="msk-data-delivery-iceberg-prerequisites"></a>

1. An Amazon MSK Provisioned cluster with Express brokers.

1. A Kafka topic producing data in a supported format for your destination.

1. An S3 bucket for the dead-letter queue (DLQ) — **required**.

1. An IAM service role (see [IAM permissions](msk-data-delivery-iceberg-iam.md)).

1. A schema registered in AWS Glue Schema Registry that matches the topic data, and an S3 Table bucket in the same AWS Region as the cluster.

1. (Optional) A customer-managed KMS key for encryption at rest.