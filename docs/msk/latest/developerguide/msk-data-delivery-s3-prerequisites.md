

# Prerequisites
<a name="msk-data-delivery-s3-prerequisites"></a>

1. An Amazon MSK Provisioned cluster with Express brokers.

1. A Kafka topic producing data in a supported format for your destination.

1. An S3 bucket for the dead-letter queue (DLQ) — **required**.

1. An IAM service role (see [IAM permissions](msk-data-delivery-s3-iam.md)).

1. A general-purpose S3 bucket for data delivery.

1. (Optional) A customer-managed KMS key for encryption at rest.