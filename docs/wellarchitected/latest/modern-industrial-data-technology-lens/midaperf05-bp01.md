# MIDAPERF05-BP01 Implement edge data pre-processing

In manufacturing settings, industrial devices and sensors often generate massive volumes
of raw data that may not all be valuable for cloud-based analytics. Implementing edge
pre-processing capabilities enables local summarization, filtering, and aggregation of data
before transmission, significantly reducing bandwidth requirements, cloud processing needs,
and storage costs while still preserving analytical value.

**Desired outcome:** A manufacturing data architecture that optimally distributes processing between edge and
cloud, performing appropriate data reduction, summarization, and filtering at the edge while
preserving essential information for cloud-based analytics and long-term storage.

**Common anti-patterns:**

- Sending all sensor data unfiltered to the cloud without edge processing, creating massive bandwidth waste and storage costs
- Using fixed sampling rates regardless of operational context or equipment state, missing critical events during high-activity periods while wasting resources during stable operations
- Designing systems that cannot function locally during connectivity disruptions, losing valuable operational data and halting local decision-making
- Deploying edge devices with insufficient CPU, memory, or storage capacity to handle required pre-processing, creating bottlenecks and system failures
- Sending data without contextual filtering or prioritization, treating routine operational data the same as critical alerts or anomalies
- Failing to implement temporary storage at the edge, resulting in permanent data loss during network outages or connectivity issues
- Performing all data analysis in the cloud instead of leveraging edge capabilities for real-time local decisions and immediate responses
- Excessive data summarization that loses critical analytical value or masks important operational insights needed for maintenance and optimization
- Applying identical pre-processing logic across all equipment types and operational contexts without considering specific requirements or characteristics
- Not implementing immediate local processing for time-sensitive data that requires instant action or real-time operational adjustments
- Ignoring the compound effect of raw data storage costs over time, failing to implement appropriate data lifecycle and retention policies
- Designing systems assuming unlimited or cheap network bandwidth without considering actual connectivity constraints in industrial environments

**Benefits of establishing this best practice:**

1. [Reduces network bandwidth requirements by 60-90% in typical manufacturing deployments](https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-2015.pdf "https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-2015.pdf")
2. Decreases cloud storage costs proportionally to reduction in data volume
3. Lowers data ingestion and processing costs in cloud environments
4. Minimizes latency for local decision-making through edge processing
5. Improves overall system resilience by enabling continued local operation during
   connectivity disruptions

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Evaluate existing data pipelines to identify compression and aggregation opportunities that preserve analytical insights. Use Amazon Managed Service for Apache Flink to perform real-time stream processing for averaging high-frequency sensor data, use AWS IoT Device SDK to implement delta-based transmission protocols that only send data when values exceed defined thresholds, and deploy AWS Lambda functions to calculate KPIs and derived metrics at the edge before transmission to reduce payload sizes.
- Architect distributed computing capabilities at plant locations using ruggedized hardware optimized for industrial environments. Deploy AWS IoT Greengrass on industrial-grade edge devices to enable local compute, messaging, and ML inference capabilities, utilize Amazon EC2 instances or AWS Outposts for locations requiring substantial remote processing power, and implement AWS Systems Manager for remote device management and software deployment across manufacturing sites.
- Configure intelligent data collection systems that adapt based on operational states and process conditions. Use AWS IoT Device Defender and AWS IoT Events to create rules-based filtering that correlates equipment status with data collection requirements, implement Amazon DynamoDB at the edge using AWS IoT Greengrass to store operational context and filtering rules, and leverage AWS IoT Core message routing to direct different data streams based on production state classifications.
- Develop dynamic data acquisition systems that automatically adjust collection frequencies based on real-time equipment health and process stability indicators. Implement AWS IoT Greengrass ML Inference to run anomaly detection models locally that trigger increased sampling rates, use Amazon CloudWatch metrics and alarms to define operational state thresholds, and deploy AWS Lambda functions that dynamically reconfigure sampling parameters based on equipment condition scores and process variables.
- Implement resilient data buffering and intelligent transmission systems that maintain data integrity during network disruptions. Configure AWS IoT Greengrass local storage capabilities with Amazon DynamoDB local tables for temporary data persistence, implement Amazon Data Firehose for reliable data delivery with automatic retry mechanisms, and use AWS IoT Core device shadows to maintain synchronization state and prioritize critical alarm data transmission over historical trend data during bandwidth-constrained conditions.

## Key AWS services

- AWS IoT Greengrass for edge processing and analytics
- AWS IoT SiteWise for equipment modeling and edge processing
- AWS IoT Core for secure device connectivity
- Amazon Kinesis for data streaming from edge to cloud
- AWS Lambda for custom edge processing functions
- Amazon S3 for storing pre-processed data

## Resources

- [Processing Data at the Edge with AWS IoT Greengrass](../../../greengrass/latest/developerguide/stream-manager.md "../../../greengrass/latest/developerguide/stream-manager.md")
- [Edge Processing with AWS IoT SiteWise Edge](../../../iot-sitewise/latest/userguide/edge.md "../../../iot-sitewise/latest/userguide/edge.md")
