# Apache Flink Stream Processing

Apache Flink on Amazon Kinesis Data Analytics provides the real-time stream processing engine for the telemetry pipeline. The guidance deploys five specialized Flink applications written in Java, each handling specific business logic for connected vehicle data processing.

**Flink Runtime Configuration**:

- **Runtime Environment**: FLINK-1_18 (Apache Flink 1.18.x)
- **Language**: Java 11 with Maven build system
- **Deployment**: Amazon Kinesis Data Analytics for Apache Flink (managed service)
- **Parallelism**: 1 task per KPU (Kinesis Processing Unit) with auto-scaling enabled
- **Checkpointing**: 60-second intervals with 5-second minimum pause between checkpoints
- **Monitoring**: APPLICATION-level metrics with DEBUG logging to CloudWatch

**Java Application Architecture**:

All Flink applications are built from a single Maven project (`modules/flink`) that produces a unified JAR file (`cms-telemetry-processor-1.0.0.jar`). The JAR contains multiple processor classes, and the specific processor is selected at runtime via the `PROCESSOR_TYPE` environment variable.

**Build and Deployment Process**:

The Makefile automates the complete build and deployment workflow:

```
# Build JAR from source
cd modules/flink
export JAVA_HOME=/opt/homebrew/opt/openjdk@11
mvn clean package -DskipTests

# Upload to S3
aws s3 cp target/cms-telemetry-processor-1.0.0.jar \
  s3://${BUCKET_NAME}/jars/cms-telemetry-processor-1.0.0.zip

# Update Flink application with new JAR
aws kinesisanalyticsv2 update-application \
  --application-name cms-dev-flink-trip-processor \
  --current-application-version-id ${VERSION} \
  --application-configuration-update file://flink-jar-update.json
```

**Modifying and Redeploying Processors**:

To modify a Flink processor and redeploy:

1. **Edit Java Source**: Modify processor code in `modules/flink/src/main/java/`
2. **Build JAR**: Run `make configure-flink` or manually build with Maven
3. **Upload JAR**: JAR is automatically uploaded to S3 bucket
4. **Update Applications**: All Flink applications are updated with new JAR version
5. **Restart Applications**: Applications must be stopped and restarted to load new code
   The Makefile handles all steps automatically:

```
# Complete rebuild and redeploy
make configure-flink AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev
```

**Flink Application 1: Event-Driven Telemetry Processor**:

**Purpose**: Real-time telemetry validation and storage

**Processor Class**: `EventDrivenTelemetryProcessor.java`

**Processing Logic**: \* Consumes from `cms-telemetry-raw` Kafka topic \* Validates JSON schema and required fields (vehicle_id, timestamp, location, speed) \* Enriches with metadata (processing_timestamp, region) \* Writes validated telemetry directly to DynamoDB telemetry table \* Handles malformed messages with error logging

**Configuration**:

```
{
  "PROCESSOR_TYPE": "EventDrivenTelemetryProcessor",
  "bootstrap.servers": "b-1.cluster.kafka.us-east-1.amazonaws.com:9098",
  "security.protocol": "SASL_SSL",
  "sasl.mechanism": "AWS_MSK_IAM",
  "group.id": "cms-event-driven-telemetry-processor-consumer",
  "TABLE_NAME": "cms-dev-storage-telemetry",
  "auto.offset.reset": "earliest"
}
```

**Output**: DynamoDB telemetry table (real-time writes)

**Flink Application 2: Telemetry Enhanced Processor**:

**Purpose**: Advanced telemetry processing with analytics and archival

**Processor Class**: `TelemetryDataProcessor.java`

**Processing Logic**: \* Consumes from `cms-telemetry-raw` Kafka topic \* Performs advanced validation and data quality checks \* Calculates derived metrics (acceleration, heading changes, fuel efficiency) \* Writes enhanced telemetry to DynamoDB \* Archives raw telemetry to S3 data lake in Parquet format \* Publishes to `telemetry-processed` topic for downstream consumers

**Configuration**:

```
{
  "PROCESSOR_TYPE": "TelemetryDataProcessor",
  "group.id": "cms-telemetry-enhanced-processor-consumer",
  "TABLE_NAME": "cms-dev-storage-telemetry",
  "S3_DATALAKE_BUCKET": "cms-dev-storage-datalake",
  "REDIS_ENDPOINT": "cms-dev-redis.cache.amazonaws.com:6379"
}
```

**Output**: DynamoDB telemetry table, S3 data lake, `telemetry-processed` Kafka topic

**Flink Application 3: Trip Processor**:

**Purpose**: Aggregate individual telemetry messages into complete trip records

**Processor Class**: `TripProcessor.java`

**Processing Logic**: \* Consumes from `cms-telemetry-raw` Kafka topic \* Detects trip start events (ignition on, speed > 0) \* Maintains stateful session windows per vehicle (timeout: 30 minutes) \* Aggregates telemetry during trip: distance, duration, average speed, max speed \* Generates route polylines from GPS coordinates \* Calculates fuel consumption and emissions \* Detects trip end events (ignition off, speed = 0 for 5 minutes) \* Writes completed trips to DynamoDB trips table \* Publishes to `trips` Kafka topic

**State Management**: \* Uses Flink’s RocksDB state backend for active trip state \* Maintains up to 24 hours of active trip state per vehicle \* State TTL automatically expires old trips

**Configuration**:

```
{
  "PROCESSOR_TYPE": "TripProcessor",
  "group.id": "cms-trip-processor-consumer",
  "TRIPS_TABLE_NAME": "cms-dev-storage-trips"
}
```

**Output**: DynamoDB trips table, `trips` Kafka topic

**Flink Application 4: Safety Event Detector**:

**Purpose**: Real-time detection of harsh driving behaviors and safety violations

**Processor Class**: `SafetyProcessor.java`

**Processing Logic**: \* Consumes from `cms-telemetry-raw` Kafka topic \* Calculates acceleration/deceleration from speed changes \* Detects harsh braking (deceleration > 0.4g) \* Detects rapid acceleration (acceleration > 0.3g) \* Detects sharp cornering (lateral acceleration > 0.5g calculated from GPS heading changes) \* Detects speeding violations (speed > posted limit + threshold) \* Calculates driver safety scores (rolling 30-day window) \* Writes safety events to DynamoDB safety_events table \* Publishes to `safety-events` Kafka topic for real-time alerts

**Windowing**: \* 5-second tumbling windows for event detection \* 30-day sliding windows for safety score calculation

**Configuration**:

```
{
  "PROCESSOR_TYPE": "SafetyProcessor",
  "group.id": "cms-safety-processor-consumer",
  "SAFETY_EVENTS_TABLE_NAME": "cms-dev-storage-safety-events"
}
```

**Output**: DynamoDB safety_events table, `safety-events` Kafka topic

**Flink Application 5: Maintenance Alert Generator**:

**Purpose**: Predictive maintenance alerts based on telemetry patterns and anomalies

**Processor Class**: `MaintenanceProcessor.java`

**Processing Logic**: \* Consumes from `cms-telemetry-raw` Kafka topic \* Monitors engine temperature, oil pressure, battery voltage, tire pressure \* Detects anomalies using statistical thresholds (mean ± 3 standard deviations) \* Tracks cumulative metrics (mileage, engine hours, battery cycles) \* Integrates with NHTSA recall database (checks VIN against active recalls) \* Generates maintenance recommendations based on OEM schedules \* Calculates remaining useful life for components (battery, brakes, tires) \* Writes maintenance alerts to DynamoDB maintenance_events table \* Publishes to `maintenance-alerts` Kafka topic

**ML Integration**: \* Can invoke Amazon SageMaker endpoints for advanced anomaly detection \* Supports custom ML models for predictive maintenance

**Configuration**:

```
{
  "PROCESSOR_TYPE": "MaintenanceProcessor",
  "group.id": "cms-maintenance-processor-consumer",
  "MAINTENANCE_TABLE_NAME": "cms-dev-storage-maintenance-events"
}
```

**Output**: DynamoDB maintenance_events table, `maintenance-alerts` Kafka topic

**Common Configuration Across All Applications**:

All Flink applications share common configuration for MSK connectivity and AWS integration:

```
{
  "bootstrap.servers": "b-1.cluster.kafka.us-east-1.amazonaws.com:9098,b-2.cluster.kafka.us-east-1.amazonaws.com:9098",
  "security.protocol": "SASL_SSL",
  "sasl.mechanism": "AWS_MSK_IAM",
  "sasl.jaas.config": "software.amazon.msk.auth.iam.IAMLoginModule required;",
  "sasl.client.callback.handler.class": "software.amazon.msk.auth.iam.IAMClientCallbackHandler",
  "auto.offset.reset": "earliest",
  "enable.auto.commit": "false",
  "aws.region": "us-east-1"
}
```

**IAM Authentication for MSK**:

Flink applications use IAM authentication (port 9098) to connect to MSK, eliminating the need for SCRAM credentials:

- **IAM Role**: `FlinkExecutionRole` with comprehensive MSK permissions
- **Kafka Cluster Actions**: Connect, DescribeCluster, CreateTopic, ReadData, WriteData
- **Topic-Level Actions**: Read from source topics, write to destination topics
- **Consumer Group Actions**: AlterGroup, DescribeGroup for offset management

**VPC Configuration**:

All Flink applications are deployed in the same VPC as the MSK cluster for secure, low-latency connectivity:

- **VPC**: Same VPC as MSK cluster (10.0.0.0/16)
- **Subnets**: Private subnets in 2 Availability Zones
- **Security Groups**: MSK security group allows inbound on port 9098 from Flink
- **Network Interfaces**: Kinesis Data Analytics creates ENIs in private subnets

**Scalability and Elasticity**:

- **Auto-Scaling**: Kinesis Data Analytics automatically scales parallelism based on message backlog
- **Parallelism Units (KPUs)**: Each KPU provides 1 vCPU and 4 GB memory; scale from 1 to 128 KPUs
- **Elastic Scaling**: Automatically adds KPUs when CPU > 75% or backlog > 1 minute
- **Scale-Down**: Reduces KPUs when utilization < 25% for cost optimization
- **Throughput**: Each KPU processes ~10K messages/second; 128 KPUs = 1.28M messages/second

**State Management**:

- **RocksDB State Backend**: Stores application state (active trips, vehicle sessions) in embedded RocksDB
- **Incremental Checkpoints**: Saves state changes to S3 every 60 seconds for fault tolerance
- **State TTL**: Automatically expires old state (trips > 24 hours) to prevent unbounded growth
- **Savepoints**: Manual snapshots enable application upgrades without data loss

**Exactly-Once Processing**:

- **Kafka Transactions**: Flink uses Kafka transactions to ensure exactly-once semantics end-to-end
- **Two-Phase Commit**: Coordinates commits across Kafka (source), state backend, and Kafka (sink)
- **Idempotent Writes**: DynamoDB writes use conditional expressions to prevent duplicate records
- **Checkpoint Barriers**: Aligns checkpoints across parallel tasks for consistent state

**CloudWatch Monitoring**:

Each Flink application has a dedicated CloudWatch Log Group:

- `/aws/kinesis-analytics/cms-dev-flink-event-driven-telemetry-processor`
- `/aws/kinesis-analytics/cms-dev-flink-telemetry-enhanced-final`
- `/aws/kinesis-analytics/cms-dev-flink-trip-processor`
- `/aws/kinesis-analytics/cms-dev-flink-safety-processor`
- `/aws/kinesis-analytics/cms-dev-flink-maintenance-processor`

**Metrics**: \* `KPUs`: Current parallelism units \* `cpuUtilization`: CPU usage percentage \* `heapMemoryUtilization`: JVM heap usage \* `numRecordsInPerSecond`: Input message rate \* `numRecordsOutPerSecond`: Output message rate \* `millisBehindLatest`: Consumer lag in milliseconds

**Event-Driven Architecture**:

- **Event Time Processing**: Uses message timestamps (not processing time) for accurate windowing
- **Watermarks**: Handles out-of-order messages with configurable lateness (5 minutes)
- **Side Outputs**: Routes late messages to separate topics for offline processing
- **Complex Event Processing**: Detects patterns across multiple message types (e.g., trip + safety event)

**Development Workflow**:

1. **Local Development**:
   - Develop and test processors locally with embedded Kafka
   - Use Flink’s DataStream API for stream processing logic
   - Write unit tests with Flink’s testing utilities

2. **Build JAR**:
   [source,bash]

---

cd modules/flink
mvn clean package -DskipTests

---

3. **Deploy to AWS**:
   [source,bash]

---

## make configure-flink AWS_PROFILE=my-profile DEPLOYMENT_STAGE=dev

4. **Monitor Execution**:
   - Check CloudWatch Logs for application logs
   - Monitor CloudWatch Metrics for performance
   - Use Flink Dashboard (if enabled) for detailed execution graphs

5. **Update Application**:
   - Modify Java source code
   - Rebuild JAR with Maven
   - Run `make configure-flink` to update all applications
   - Stop and restart applications to load new code

**Extensibility**:

The Flink processing layer is highly extensible:

- **Custom Processors**: Add new processor classes to the JAR for domain-specific processing
- **ML Inference**: Integrate with SageMaker for real-time ML predictions on telemetry streams
- **Geofencing**: Add geofence detection for location-based alerts and analytics
- **Driver Behavior Scoring**: Implement sophisticated scoring algorithms combining multiple signals
- **Fuel Optimization**: Analyze driving patterns to provide fuel efficiency recommendations
- **Predictive Routing**: Use historical traffic and telemetry data for intelligent route suggestions
- **Custom Windowing**: Implement custom window functions for specialized aggregations
- **External Enrichment**: Join telemetry streams with external data sources (weather, traffic, POIs)

**Troubleshooting Common Issues**:

1. **Application Won’t Start**:
   - Verify JAR file exists in S3 bucket
   - Check IAM role has permissions to read from S3
   - Verify VPC configuration allows connectivity to MSK
   - Check CloudWatch Logs for startup errors

2. **High Consumer Lag**:
   - Increase parallelism (add more KPUs)
   - Optimize processing logic (reduce per-message overhead)
   - Check for bottlenecks in DynamoDB writes
   - Verify MSK cluster has sufficient capacity

3. **State Size Growing Unbounded**:
   - Configure state TTL to expire old state
   - Reduce session window timeout
   - Clear old checkpoints from S3

4. **Checkpoint Failures**:
   - Increase checkpoint interval (reduce frequency)
   - Check S3 permissions for checkpoint storage
   - Verify network connectivity to S3
   - Monitor checkpoint duration metrics

**Cost Optimization**:

- **Right-Size KPUs**: Start with 1 KPU per application, scale based on actual load
- **Checkpoint Frequency**: Balance fault tolerance with checkpoint overhead (60s recommended)
- **State Backend**: Use RocksDB for large state, heap for small state
- **Auto-Scaling**: Enable auto-scaling to reduce costs during low-traffic periods
- **Development vs Production**: Use smaller KPU counts for dev/test environments
