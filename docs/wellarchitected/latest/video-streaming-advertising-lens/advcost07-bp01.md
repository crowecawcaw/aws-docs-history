

# ADVCOST07-BP01 Consolidate inventory data into a unified data lakehouse to reduce redundant storage and ETL pipelines
<a name="advcost07-bp01"></a>

 Publishers maintaining separate data pipelines for linear logs, digital impressions, and audience data run redundant ETL jobs, duplicate storage, and parallel analytics infrastructure. A unified data lakehouse consolidates these into a single processing and storage layer, reducing 40–60% of ETL compute. 

 **Desired outcome:** 
+  All advertising inventory data (linear TV avails, digital impressions, CTV streams, and FAST channels) resides in a single data lakehouse with a unified schema. 
+  Duplicate ETL pipelines are reduced. 
+  Cross-system analytics queries run against a single data lake without data movement. 

 **Common anti-patterns:** 
+  Maintaining separate ETL pipelines for linear TV inventory (Nielsen-based traffic systems) and digital inventory (ad server impression logs) that independently ingest, transform, and aggregate overlapping data, which duplicates 40–60% of compute costs for pipelines that could be consolidated into a single ingestion path. 
+  Copying data between siloed linear and digital systems for cross-system reporting rather than querying a unified repository, so redundant storage costs and stale snapshots drift out of sync and require reconciliation effort. 
+  Running analytics infrastructure that stays constantly on (dedicated warehouses, provisioned clusters) for cross-system inventory queries that occur intermittently, which pays ongoing compute costs when serverless query engines like Amazon Athena would charge only per query executed. 
+  Implementing point-to-point integrations between each linear traffic system and each digital ad server for data sharing, so O(n²) integration complexity grows with each new system instead of centralizing all inventory data in a single lakehouse that all systems can query. 
+  Deferring data lakehouse migration indefinitely because linear and digital teams operate independently, which allows duplicate pipelines and siloed systems to accumulate technical debt and compounding costs that grow harder to address over time. 

 **Benefits of establishing this best practice:** 
+  Reduce 40–60% of ETL compute by removing redundant linear and digital ingestion pipelines 
+  Reduce storage costs by removing duplicate data copies across siloed systems 
+  Enable cross-system yield analysis without additional data movement 
+  Single query engine reduces licensing costs compared to separate tools for linear and digital analytics 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Publishers with both linear TV and digital advertising typically operate separate data pipelines that evolved independently. Linear systems ingest Nielsen panel data, set-top box logs, and traffic schedules. Digital systems ingest ad server impression logs, SSP reports, and DMP audience feeds. Both pipelines perform overlapping transformations: deduplication, audience enrichment, time-window aggregation, and delivery reconciliation. Running these transformations independently duplicates 40–60% of ETL compute because much of the underlying data (audience identity, content metadata, and time-based aggregation) is structurally identical across systems. 

 A unified data lakehouse consolidates all inventory data into a single storage and processing layer. A *lakehouse* combines the low-cost storage of a data lake (object storage in [Amazon S3](https://aws.amazon.com/s3/)) with the query performance and ACID transaction guarantees of a data warehouse, using open table formats like Apache Iceberg. In this architecture, a single [Athena](https://aws.amazon.com/athena/) query joins linear avail data with digital impression data without copying data between systems. 

 Schema design must reconcile linear and digital inventory models. Linear inventory is described in dayparts, demographics, programs, and GRP commitments. Digital inventory uses audience segments, placements, devices, impression goals, and bid floors. The unified schema must represent both without losing the specifics that make each useful. Polymorphic table design with a shared base (campaign, time window, audience) and type-specific extensions (linear attributes, digital attributes) handles this. 

 Point-to-point integrations between linear and digital systems create O(n²) complexity that grows with each new system (CTV, FAST, and retail media). Every new source requires new integration code to every existing destination. A centralized lakehouse inverts this. Each source writes once to the lakehouse, and all consumers query from it. Adding a new system requires one ingestion pipeline rather than N integrations. 

 The main obstacle is usually organizational rather than technical. Linear and digital teams often report to different executives, use different tooling, and have separate operational processes. A data lakehouse migration requires cross-team coordination that might not have organizational support. Starting with read-only cross-system queries against existing data (without requiring either team to change their ingestion processes initially) can demonstrate value before asking teams to consolidate pipelines. Governance through [AWS Lake Formation](https://aws.amazon.com/lake-formation/) keeps access controls in place through consolidation, addressing team concerns about losing control of their data. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit existing data pipelines and identify overlap:** Catalog all linear TV inventory systems (traffic, scheduling, and makegoods) and digital systems (ad server logs, SSP reports, and DMP feeds). Map overlapping data and duplicate transformations. Quantify the compute cost of redundant pipelines. 

1.  **Design a unified inventory schema in AWS Glue Data Catalog:** Create a schema that represents both linear avails (daypart, demographic, program, and GRP commitment) and digital impressions (audience placement, device, impression goal, and bid floor) using Apache Iceberg table format on S3. 

1.  **Build consolidated Glue ETL jobs:** Create a single orchestrated workflow that ingests from both linear and digital sources into the unified S3 lakehouse. Use EventBridge to trigger ingestion on schedule and on source system events. 

1.  **Decommission redundant ETL pipelines:** After validating data quality from the unified pipeline, decommission separate linear and digital ETL jobs. Update downstream consumers to query the unified lakehouse through Athena. Calculate and document cost savings from reduced compute. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Guidance for Building an Advertising Data Lake for Publishers on AWS](https://aws.amazon.com/solutions/guidance/building-an-advertising-data-lake-for-publishers-on-aws/) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [AWS Lake Formation](https://aws.amazon.com/lake-formation/) 