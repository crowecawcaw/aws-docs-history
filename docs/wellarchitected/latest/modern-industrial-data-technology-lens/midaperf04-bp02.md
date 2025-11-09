# MIDAPERF04-BP02 Decouple data ingestion from processing in manufacturing systems

In manufacturing environments, tightly coupled data pipelines create single points of
failure that can lead to data loss and operational disruptions. Implementing a decoupled
architecture that separates ingestion from processing enhances system resilience, enables
independent scaling of components, and provides the foundation for reliable data processing
even during partial system failures common in industrial settings.

**Desired outcome:** A resilient manufacturing data architecture where ingestion and processing components
operate independently, enabling continuous data capture during processing failures, supporting
reprocessing capabilities when ingestion recovers from outages, and maintaining overall system
performance through appropriate component scaling.

**Common anti-patterns:**

- Tightly coupling data ingestion directly to processing components - Creates single
  points of failure that can cause complete system shutdowns and data loss during processing
  failures
- Implementing synchronous processing without buffering - Forces ingestion to wait for
  processing completion, creating bottlenecks and reducing overall system throughput
- Using shared scaling policies for ingestion and processing - Leads to
  over-provisioning or under-provisioning of resources since components have different load
  patterns and scaling requirements
- Designing non-idempotent processing operations - Causes data corruption and
  inconsistencies during replay scenarios, requiring expensive cleanup operations that
  impact performance
- Failing to implement dead-letter queues or error handling - Results in infinite retry
  loops that consume resources and degrade system performance during data quality issues
- Configuring insufficient buffer retention periods - Forces data loss during extended
  outages, requiring expensive data recovery operations and potential reprocessing from
  external sources
- Omitting queue depth monitoring for scaling decisions - Causes reactive rather than
  proactive scaling, leading to buffer overflows and performance degradation during traffic
  spikes
- Creating processing components without replay capabilities - Requires rebuilding
  entire datasets during recovery, consuming significant computational resources and
  extending downtime
- Using inadequate buffer storage capacity planning - Results in data loss during peak
  ingestion periods or extended processing outages, requiring expensive data reconstruction
- Implementing blocking operations in ingestion pipelines - Creates cascading failures
  where upstream data collection stops when downstream processing experiences issues
- Designing stateful processing without proper checkpointing - Forces complete
  reprocessing from the beginning during failures, wasting computational resources and
  extending recovery times
- Configuring overly aggressive retry policies without backoff - Overwhelms failing
  components and prevents recovery while consuming network and computational resources
  unnecessarily

**Benefits of establishing this best practice:**

1. Helps prevent critical production data loss during equipment shutdowns or unplanned
   downtime – Continually captures sensor readings, alarm states, and process variables even
   when historians, SCADA systems, or edge devices require maintenance or experience hardware
   failures.
2. Allows dynamic resource allocation to match plant operational cycles and data volumes

- Enables scaling data ingestion during high-production periods or maintenance windows
  while independently adjusting processing power for complex analytics like predictive
  maintenance algorithms or real-time quality control calculations.

3. Provides data replay capabilities for root cause analysis and process optimization -
   Supports reprocessing historical operational data after system outages, calibration
   changes, or when new analytics models are deployed to backfill insights for compliance
   reporting or process improvement initiatives.
4. Maintains data pipeline integrity despite industrial network instabilities and
   equipment faults – Continually operates through common industrial challenges like network
   congestion, PLC communication errors, fieldbus disruptions, or temporary sensor
   malfunctions that frequently impact manufacturing environments.
5. Minimizes production impact during system upgrades and reduces maintenance windows -
   Enables rolling updates of data processing systems without disrupting critical real-time
   monitoring, trending, or automated control loops, allowing maintenance activities during
   normal production hours rather than costly scheduled downtime.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

1. Implement Durable Ingestion Buffers - Deploy Amazon Kinesis Data Streams or Amazon MSK (Kafka) for high-throughput streaming data with configurable retention periods up to
   365 days. For batch workloads, use Amazon SQS with extended message retention and DLQ
   configuration, combined with Amazon S3 for long-term storage overflow when queue limits
   are approached.
2. Design Idempotent Processing - Leverage Amazon DynamoDB conditional writes or
   Amazon RDS with upsert operations for processing idempotency. Implement AWS Lambda with
   event source mapping deduplication features or use Amazon Managed Service for Apache Flink for
   exactly-once processing semantics. Store processing state in DynamoDB with composite
   keys to track message processing status.
3. Configure Dead-Letter Handling - Set up Amazon SQS Dead Letter Queues with Amazon CloudWatch alarms for message count thresholds. Use Amazon SNS to trigger notifications
   when DLQ thresholds are exceeded. Store failed messages in Amazon S3 with lifecycle
   policies for cost optimization and use AWS Step Functions for orchestrating retry logic
   and failure investigation workflows.
4. Implement Replay Capabilities - Utilize Kinesis Data Streams' time-based replay
   functionality or Amazon MSK's offset management for streaming data replay. For batch
   data, implement S3-based data lake architecture with AWS Glue ETL jobs that can
   reprocess partitioned data based on timestamps. Use AWS Batch for large-scale
   reprocessing jobs with automatic retry and scaling capabilities.
5. Establish Independent Scaling - Configure Amazon EC2 Auto Scaling Groups with
   custom CloudWatch metrics for queue depth monitoring. Use AWS Application Auto Scaling
   for Kinesis shard scaling based on incoming records and iterator age metrics. Implement
   AWS Lambda concurrent execution limits and reserved concurrency to help prevent
   downstream system overload while allowing independent scaling of processing components.

## Key Services

- Amazon Kinesis Data Streams for scalable data ingestion
- Amazon SQS for durable message queuing
- Amazon MSK (Managed Streaming for Apache Kafka) for high-throughput streaming
- Amazon S3 for durable data landing and replay capabilities
- AWS Lambda for serverless processing of ingested data
- Amazon EventBridge for event-based processing orchestration

## Resources

- [Resilience in AWS Data Pipelines](../../../datapipeline/latest/DeveloperGuide/disaster-recovery-resiliency.md "../../../datapipeline/latest/DeveloperGuide/disaster-recovery-resiliency.md")
- [AWS Prescriptive Guidance Patterns](../../../prescriptive-guidance/latest/patterns/decouple-microservices-using-amazon-sqs-and-aws-lambda.md "../../../prescriptive-guidance/latest/patterns/decouple-microservices-using-amazon-sqs-and-aws-lambda.md")
- [Amazon EventBridge features](https://aws.amazon.com/eventbridge/features/ "https://aws.amazon.com/eventbridge/features/")
