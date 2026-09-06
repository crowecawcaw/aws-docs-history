

# Utility Volt-VAR Management Framework
<a name="utility-volt-var-management"></a>

Publication date: **February 22, 2022 ([Diagram history](#vvo-history))**

With this architecture, you can build highly scalable distribution grid management applications such as Volt-VAR Optimization (VVO). You can also build sensor and controller abnormality detection and grid analytics applications. The solution uses an event-driven, microservices-oriented framework with [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/) for streaming, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for serverless compute, and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for machine learning (ML).

## Utility Volt-VAR Management Framework diagram
<a name="vvo-diagram"></a>

![Reference architecture diagram showing how to build Volt-VAR management applications by using Amazon MSK, Lambda, SageMaker AI, and Amazon EventBridge.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/utility-volt-var-management/images/utility-volt-var-management.png)


The following steps describe the data ingestion, processing, and application components for this architecture:

1. Integrate with existing utility Operations Technology (OT) systems and third-party systems to activate the distribution Volt-VAR management framework. Connect the Advanced Metering Infrastructure (AMI) head-end, power quality sensors, Geographic Information Systems (GIS), Outage Management Systems (OMS), SCADA, and other data acquisition systems.

1. Connect to AWS through a VPN with high reliability. For guaranteed bandwidth, use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) with IEEE 802.1AE (MACSec) encryption.

1. Ingest API-based data by using serverless technologies such as [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) and Lambda. This provides cost-effective and highly scalable data ingestion from measurement and topology source systems.

1. Ingest data and issue controls through existing on-premises supervisory control and data acquisition (SCADA) systems with protocol-based integration. Maintain supervisory control of AWS-based applications through the existing SCADA system.

1. Stream all measurement data by using the technology or service of your choice. Trade off ease of use against real-time streaming needs with [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/) or Amazon MSK.

1. 6A. Load real-time data streams reliably into a data lake by using [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/). Store data durably and cost-effectively in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for your data lake. Automate the extract, transform, and load (ETL) process with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) to clean and transform data into business-ready formats.

   6B. Derive valuable insights from your curated data lake by using AI/ML services such as SageMaker AI and [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/). Retrain ML models every few hours or days and publish an inference endpoint for use by real-time applications.

1. Activate event-driven architectural patterns with a serverless event bus by using [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) or a combination of [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) and [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/). Use Amazon EventBridge for integration with third-party SaaS offerings such as Distributed Energy Resource Management Systems (DERMS).

1. Develop event-driven VVO applications. Use real-time operational data streams as input. Build cost-effective, highly scalable microservices with serverless Lambda. Use high performance computing (HPC)-optimized [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances for power-flow-based calculations. Choose from a broad selection of database services for application-specific data access patterns. Run online inferences on pre-trained ML models by using SageMaker AI endpoints.

1. Create real-time operational dashboards by using [Amazon Managed Service for Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/). Create BI dashboards by using [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html). Accelerate custom web application UI development and hosting with [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/). Query petabytes of data across your data warehouse and data lake by using standard SQL with [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/).

1. Log all account activity with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/). Monitor cloud resources and applications by using [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) to collect and track metrics, monitor log files, and set alarms. Search, analyze, and visualize logs for real-time insights with [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/). Analyze and debug distributed, microservices-based VVO applications by using [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/).

1. Govern cloud resources and apply security controls at scale from a centralized location by using services such as [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/), [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/), AWS Systems Manager, [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html), and [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/).

1. Control access with [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/) and [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/). Monitor network traffic for malicious activity by using [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/). Encrypt all data at rest with [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) and data in transit by using Transport Layer Security (TLS) encryption. Use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/) to assess all cloud configurations and any changes.

## Further reading
<a name="vvo-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="vvo-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#vvo-history) | Reference architecture diagram first published. | February 22, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.