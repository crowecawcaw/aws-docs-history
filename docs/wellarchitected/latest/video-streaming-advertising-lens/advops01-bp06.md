

# ADVOPS01-BP06 Implement a unified campaign management interface across linear and digital operations

 Establish a single, integrated campaign management system that provides unified visibility and control across linear TV scheduling and digital and CTV programmatic operations. This removes the need for parallel ad ops teams running disconnected workflows by converging campaign booking, trafficking, delivery monitoring, and reconciliation into one operational interface. 

 **Desired outcome:** 
+  Ad operations teams manage all campaign types (linear broadcast, digital programmatic, and CTV or streaming) from a single system with shared workflows, common data models, and unified reporting. 
+  Campaign setup, creative trafficking, delivery optimization, and billing reconciliation follow consistent processes regardless of delivery channel. 
+  Teams operate with a shared understanding of campaign health across all channels simultaneously through real-time unified dashboards. 

 **Common anti-patterns:** 
+  Operating separate campaign management systems for linear traffic/scheduling and digital ad server/DSP with manual data synchronization between them, leading to reconciliation errors and delayed fulfillment visibility. 
+  Maintaining parallel ad ops teams with distinct toolsets, processes, and KPIs that can't collaborate on cross-channel campaigns without manual handoffs and spreadsheet-based coordination. 
+  Relying on batch-processed reports (daily or weekly) to understand cross-channel campaign status rather than providing real-time unified visibility. 

 **Benefits of establishing this best practice:** 
+  Unified campaign management reduces redundant operational overhead and reduces human error from manual data transfer between systems. 
+  The architecture lets teams sell inventory across all channels and devices from one place, while placement algorithms optimize across channels to raise yield across direct and programmatic sales. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Linear TV and digital channels evolved with incompatible buying models. Linear TV operates on upfront and scatter buying with age-gender demographics, while digital channels use real-time bidding with audience-based targeting. Publishers must maintain parallel sales operations, separate ad servers, and disconnected inventory management systems that don't integrate by default. 

 Linear traffic systems denominate delivery in spots and gross rating points against program schedules, while digital ad servers count impressions against pacing goals. The two systems settle on different billing cycles with different reconciliation cadences. A cross-channel campaign booked into both systems creates two records that often drift out of alignment. A makegood on the linear side, or a revised flight date in the digital ad server, updates one record and not the other. The drift between these records surfaces later as a billing dispute. 

 Consolidate both workflows onto one system. Federating behind a shared data layer preserves each team's tooling but can preserve drift that the integration was meant to remove. Consolidation costs a single point of operational dependency and a migration that must happen while campaigns are in flight. Treat those as risks to plan for, not reasons to keep the systems separate. Unifying reporting before booking is a common first move that produces a dashboard showing discrepancies no single interface can correct. 

 Both teams must adopt the system for it to succeed, even though they perform the same work with differing syntax. Team members on the linear side think in breaks, rotations, and makegoods, while their digital counterparts think in line items, pacing, and discrepancy thresholds. Design shared workflows with both teams and adopt them incrementally. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a unified data lake on Amazon S3 with AWS Lake Formation governance:** Configure AWS Lake Formation with data catalog and fine-grained access controls. Ingest linear broadcast logs through AWS DataSync and AWS DMS, and digital ad events through Amazon Kinesis, into a common schema using AWS Glue ETL pipelines. Define the unified schema that supports both linear deal structures (daypart, demo, program, and GRP commitment) and digital deal structures (audience segment, placement, impression goal, and bid floor). 

1.  **Deploy Amazon Managed Grafana as the operational dashboard layer:** Configure Amazon Managed Grafana with data sources including CloudWatch, Amazon Managed Service for Prometheus, Amazon OpenSearch Service, and AWS X-Ray. Integrate CloudWatch as a data source with AWS Organizations for centralized dashboards from multiple accounts and regions. Build unified campaign delivery dashboards that display linear spot delivery alongside digital impression pacing in a single view. 

1.  **Implement AWS Step Functions workflows for campaign lifecycle management:** Create Step Functions state machines for campaign booking, trafficking, delivery monitoring, and reconciliation that span both linear and digital fulfillment paths. Configure Amazon EventBridge to route state changes between systems. When a linear campaign is booked, EventBridge triggers digital inventory reservation. When delivery completes, EventBridge triggers reconciliation workflows. 

1.  **Configure Quick for business-facing campaign performance reporting:** Build Quick dashboards with unified cross-channel metrics (combined GRP delivery and impression delivery against contracted values, and unified reach and frequency). Use Amazon Athena for ad-hoc querying of the converged data lake. Configure natural language query capabilities for business stakeholders who need to answer campaign questions without writing SQL. 

1.  **Integrate third-party ad tech systems using Amazon AppFlow:** Configure Amazon AppFlow connectors for SaaS ad tech systems (DSPs, SSPs, and traffic systems) to feed into the unified data layer without custom code. This enables campaign data from OpenX, Google Ad Manager, and linear traffic systems to converge in the unified data lake without maintaining custom API integrations for each system. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon Managed Grafana documentation](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) 
+  [AWS Step Functions workflow orchestration patterns](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-workflows.html) 

 **Related services:** 
+  [Amazon Managed Grafana](https://aws.amazon.com/grafana/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [AWS Lake Formation](https://aws.amazon.com/lake-formation/) 
+  [Amazon AppFlow](https://aws.amazon.com/appflow/) 