

# Scenario 13: Implementation of unified AdSales for converged television on AWS

 Publishers operating both linear TV and digital/CTV advertising face incompatible buying models (upfront/scatter with GRP guarantees compared to programmatic with audience-based targeting), fragmented measurement, and duplicated tech stacks. This scenario addresses how to converge these operations into a unified architecture that enables cross-platform campaign management, unified measurement, and data-driven yield optimization. 

## Characteristics
<a name="s13-characteristics"></a>
+  Publisher sells advertising across linear TV (upfront/scatter, age-gender demographics) and digital/CTV (audience-based, impression-level) channels. 
+  Separate ad servers, inventory management systems, and reporting tools limit cross-platform yield optimization. 
+  Campaign under-delivery on one channel can't be detected and offset using inventory from another without unified visibility. 
+  Linear TV measurement (panel-based, household-level) and digital measurement (census-level, user-level) are incompatible without unified identity resolution. 
+  Data residency and consent requirements differ significantly between linear (panel agreements) and digital (GDPR, CCPA) data flows. 
+  The environment will be linear plus digital for a decade or longer, so converged procedures must span both domains indefinitely, not as a transition state. 

## Reference architecture
<a name="s13-reference-architecture"></a><a name="scenario-13-fig1"></a>

![Unified AdSales for converged television architecture on AWS showing the data convergence layer, unified campaign management system, cross-platform measurement infrastructure, and single-pane-of-glass observability across linear and digital advertising operations](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-13-unified-adsales-converged-tv.jpg)

*Unified AdSales for converged television architecture on AWS showing the data convergence layer, unified campaign management system, cross-platform measurement infrastructure, and single-pane-of-glass observability across linear and digital advertising operations*


 The architecture consists of the following components: 

1.  **Linear broadcast logs ingestion**: AWS DataSync or AWS Transfer Family ingests linear traffic logs (spot schedules, delivery confirmations, makegood records) from broadcast traffic systems. AWS Glue ETL transforms these batch files into the unified schema. Dead-letter prefix in S3 handles malformed files without blocking digital pipeline processing. 

1.  **Digital ad event streaming**: Amazon Kinesis Data Streams captures real-time digital impression events, click events, and conversion data. AWS Glue Streaming ETL or Amazon Managed Service for Apache Flink transforms and enriches events into the unified schema. 

1.  **Unified data lake (Amazon S3 \+ AWS Lake Formation)**: Both linear and digital data converge in Apache Iceberg tables on S3, governed by AWS Lake Formation. Unified schema represents both linear avails (daypart, demographic, program, and GRP commitment) and digital impressions (audience segment, placement, device, and impression goal). AWS Glue Data Catalog maintains the schema registry. AWS Glue Schema Registry manages schema evolution. 

1.  **Unified OMS (API Gateway \+ Lambda \+ DynamoDB)**: Unified campaign booking API that abstracts the buying model. DynamoDB stores both linear deal structures (daypart, GRP commitment, program) and digital deal structures (audience segment, impression goal, bid floor) using a polymorphic data model. Amazon EventBridge routes state changes to downstream linear and digital fulfillment systems. 

1.  **Campaign lifecycle orchestration (AWS Step Functions)**: Express Workflows orchestrate campaign booking, creative trafficking, delivery monitoring, and reconciliation across both linear and digital fulfillment paths. EventBridge Scheduler triggers pacing calculations and delivery reporting. 

1.  **Unified forecasting (Amazon SageMaker AI)**: Single ML pipeline trained on both linear viewership data (STB, ACR, and panel) and digital impression data from the unified data lake. SageMaker AI Serverless Inference endpoints scale to zero between forecast runs. SageMaker AI Pipelines triggers automated retraining only when new data arrives or accuracy degrades. 

1.  **Cross-platform identity resolution (AWS Entity Resolution)**: Matches linear household identifiers (STB IDs, ACR device fingerprints, panel IDs) with digital identifiers (device IDs, first-party IDs, CTV device IDs) into a unified audience graph. Output stored in Amazon Neptune (for household relationship traversal) and Amazon DynamoDB (for low-latency frequency cap lookups). 

1.  **Unified observability (Amazon Managed Grafana)**: Single-pane-of-glass dashboard pulling from CloudWatch, Amazon Managed Service for Prometheus, Amazon OpenSearch Service, and AWS X-Ray. Displays linear spot delivery pacing alongside digital impression pacing. CloudWatch Composite Alarms correlate cross-platform delivery health. Quick for business stakeholder reporting with natural language queries through Amazon Q. 

## Configuration notes
<a name="s13-configuration-notes"></a>

### Data convergence layer
<a name="data-convergence-layer"></a>

 Deploy linear and digital ingestion pipelines as fully independent systems with separate Lambda functions, Kinesis streams, and Glue ETL jobs (no shared resources). Run the convergence layer (Glue or Athena queries joining both sources) on a 30-minute EventBridge schedule that is independent of either pipeline completing. If linear logs are delayed, digital data continues to process and converge on available linear data. Tag each source with its latest update timestamp so consumers know data freshness. 

### Unified OMS design
<a name="unified-oms-design"></a>

 Use a polymorphic DynamoDB data model with a campaign type discriminator (channel\_type: LINEAR \| DIGITAL \| CTV). Both buying models (GRP-guaranteed linear and impression-based digital) coexist in the same tables. EventBridge routes booking events to channel-appropriate fulfillment systems (linear traffic system, digital ad server, CTV ad decisioning). Pre-stage campaign parameters in DynamoDB Global Tables so digital ad servers read from local replicas without synchronous dependency on the central OMS. 

### Cross-platform measurement compliance
<a name="cross-platform-measurement-compliance"></a>

 When linear and digital data are joined for cross-platform measurement, apply the intersection rule: only purposes consented to in both data sources may proceed. Linear panel data is governed by panelist agreements. Digital impression data is governed by GDPR and CCPA consent. Validate consent metadata before executing any cross-source join in the Glue ETL pipeline. Implement right-to-erasure cascades that propagate deletions across all derived datasets within 30 days. 

### Identity governance
<a name="identity-governance"></a>

 Use Availability Zone IDs (not Availability Zone names) when coordinating identity resolution infrastructure across accounts. Configure DynamoDB TTL on all cross-platform identity mapping records aligned to consent validity periods. When consent is withdrawn, trigger a Lambda function that identifies all affected identity mappings and schedules deletion. Track deletion completion within the regulatory time frame as an operational KPI. 

### Single-pane-of-glass observability
<a name="single-pane-of-glass-observability"></a>

 Deploy AWS Distro for OpenTelemetry (ADOT) collectors across both linear playout infrastructure and digital ad serving systems. Configure Amazon Managed Grafana with data sources for CloudWatch (infrastructure metrics), Managed Prometheus (application metrics), and OpenSearch (logs and traces). Build campaign delivery dashboards showing: linear spot delivery percentage compared to ordered, digital impression pacing compared to booked, and unified reach/frequency metrics normalized across both channels. Use CloudWatch Anomaly Detection for campaign pacing alerts rather than static thresholds. Campaign delivery patterns have natural variation that static thresholds can't model accurately. 

### Converged incident response
<a name="converged-incident-response"></a>

 Define a unified incident severity matrix using affected audience scope and revenue impact per minute as the two dimensions, regardless of whether the incident originates in linear playout or digital ad serving. Assign a Tier 2 cross-functional incident commander role with authority to bridge linear NOC and digital ad ops teams. Configure AWS Systems Manager Incident Manager to automatically create incidents from CloudWatch alarms monitoring both linear playout health and digital ad serving metrics. 