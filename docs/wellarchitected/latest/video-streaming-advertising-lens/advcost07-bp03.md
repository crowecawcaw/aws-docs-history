

# ADVCOST07-BP03 Remove redundant order management systems by unifying campaign booking across buying models
<a name="advcost07-bp03"></a>

 Publishers maintaining separate OMS systems for linear and digital incur duplicate licensing, hosting, and integration maintenance costs. A unified OMS supporting both buying models reduces this duplication. 

 **Desired outcome:** 
+  A single campaign booking and OMS platform handles both guaranteed linear buys and digital programmatic buying. 
+  Duplicate OMS licensing and hosting costs are reduced. 
+  Campaign booking workflows follow consistent processes regardless of delivery channel. 

 **Common anti-patterns:** 
+  Operating separate order management systems for linear (legacy on-premises, GRP-based upfront and scatter) and digital (SaaS, impression-based programmatic) buying, which pays duplicate licensing fees, hosting costs, and integration maintenance for systems that manage the same underlying workflow: booking advertising inventory against campaigns. 
+  Building point-to-point integrations between the linear OMS and digital OMS to enable cross-channel packages, so brittle synchronization logic and manual reconciliation processes take the place of consolidating into a single system that natively supports both buying models. 
+  Deploying a custom unified OMS on persistent compute infrastructure for a workload with highly variable traffic patterns (campaign booking is bursty around upfront seasons and programmatic deal creation) when serverless architecture would reduce idle compute costs between peak periods. 
+  Attempting to migrate both linear and digital booking workflows simultaneously to a unified system, so project risk and timeline grow instead of migrating the linear workflows first, which have lower real-time requirements, and adding programmatic capabilities incrementally. 
+  Adding new channels (CTV, FAST, and retail media) as separate OMS instances or modules rather than extending the unified system, which perpetuates the duplication pattern with each new channel and compounds licensing, hosting, and integration costs over time. 

 **Benefits of establishing this best practice:** 
+  Reduce duplicate OMS licensing and hosting costs 
+  Reduce integration maintenance: one system connects to all downstream delivery systems 
+  Enable cross-channel packages (linear \+ digital bundles) without manual reconciliation 
+  Reduce operational headcount needed to manage two separate booking workflows 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Order management systems (OMS) for advertising book campaigns against available inventory, manage delivery commitments, and track fulfillment. Publishers operating in both linear TV and digital often run both a legacy on-premises system for GRP-based upfront and scatter linear buys, and a SaaS application for impression-based programmatic digital deals. Both OMS systems perform the same core workflow (accepting a campaign order, validating inventory availability, confirming the booking, and tracking delivery), but against different inventory models. 

 Duplicate OMS platforms mean duplicate licensing fees, hosting costs, integration maintenance, and operational teams. Each system requires its own connections to downstream delivery systems (traffic, ad servers, and billing), its own monitoring, and its own incident response. Cross-channel campaign packages (bundles that include linear and digital inventory) require manual reconciliation between systems because neither has visibility into the other's availability. 

 Campaign booking traffic spikes around upfront season (concentrated in May for US markets), scatter negotiation periods, and programmatic deal creation windows. Between these peaks, the system handles low-volume modifications and reporting queries. With persistent compute infrastructure, you pay for capacity sized to peak during months of low activity. Serverless architecture ([AWS Lambda](https://aws.amazon.com/lambda/) for request handling and [DynamoDB](https://aws.amazon.com/dynamodb/) for storage) reduces idle compute costs by charging per invocation and per request. 

 A single schema must represent both buying models. Linear deals are defined by daypart, demographic, program, and GRP commitment. Digital deals are defined by audience segment, placement, impression goal, and bid floor. A polymorphic schema with a shared campaign entity (common fields: advertiser, flight dates, budget, and status) and type-specific extensions (linear attributes, digital attributes) supports both. 

 Linear workflows have the highest migration risk because they tolerate less disruption during active selling seasons. Linear upfront negotiations involve contractual commitments worth millions of dollars, and system outages during negotiation windows reduce revenue. To reduce this risk, migrate linear workflows first during off-peak periods, and validate stability before adding digital programmatic capabilities. Digital booking has higher real-time requirements (programmatic deals execute continuously) but lower per-transaction financial risk, so it is safer to migrate second, after the system is proven stable. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Design a unified campaign booking API:** Use Amazon API Gateway and Lambda to create a booking interface that abstracts the buying model. Behind the unified API, route to the appropriate fulfillment logic based on campaign type (linear schedule execution compared to digital programmatic bidding). 

1.  **Implement campaign and order storage in DynamoDB:** Create a DynamoDB schema supporting both linear and digital deal structures. Linear: daypart, demo, program, GRP commitment. Digital: audience segment, placement, impression goal, bid floor. Use a polymorphic data model with a campaign type discriminator. 

1.  **Configure EventBridge for state change routing:** Route campaign booking events (created, modified, and canceled) through EventBridge to trigger downstream workflows (delivery systems, trafficking, and billing) for both linear and digital channels from a single event source. 

1.  **Migrate linear workflows first:** Start with linear upfront and scatter workflows (lower real-time requirements) before adding programmatic digital booking capabilities. Validate before expanding scope. 

## Resources
<a name="resources"></a>

 **Related services:** 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 