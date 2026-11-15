

# ADVPERF05-BP04 Provide dedicated network connection between your on-premises, multicloud environment and AWS
<a name="advperf05-bp04"></a>

 Use a dedicated private connection to provide stable and high-speed data communication between on-premises advertising infrastructure and the cloud. Advertising platforms move data at volumes and under regulatory constraints that make public internet transfers inadequate. Behavioral data falls under private network path requirements. Hybrid architectures need on-premises bid decisioning to query cloud-hosted audience data without internet latency variability. For cross-cloud workflows, equivalent private connectivity links separate cloud environments. 

 **Desired outcome:** 
+  Your on-premises advertising infrastructure connects to AWS over a dedicated private network connection sized for peak advertising data transfer events, not average throughput. 
+  Audience segment synchronization, ML training data movement, and campaign data transfers complete within their maintenance windows at predictable throughput rather than being subject to public internet congestion. 
+  Private network paths for user behavioral data and audience segment transfers keep this data off the public internet, supporting your regulatory and advertiser data contract obligations without relying on compensating controls. 
+  On-premises DSP or DMP infrastructure queries AWS-hosted audience data with consistent low latency, enabling hybrid migration architectures where cloud-based bidding runs alongside legacy on-premises systems. 
+  Cross-cloud advertising data flows (publisher first-party segments on Google Cloud, third-party measurement providers on Azure, or attribution partners on other clouds) travel over private connections rather than the public internet, giving cross-cloud transfers the same private-path controls that help support regulatory and advertiser data contract obligations for on-premises transfers. 

 **Common anti-patterns:** 
+  Connecting on-premises advertising infrastructure to AWS over a site-to-site VPN that traverses the public internet, so audience segment synchronization jobs miss their maintenance windows to public-internet latency variability and throughput limits. 
+  Sizing Direct Connect connections based on average data transfer volume rather than peak advertising calendar events (end-of-month reporting exports, pre-season audience rebuilds, major campaign launches), which causes congestion precisely when data transfer is most business-critical. 
+  Treating Direct Connect as a compliance-only requirement while continuing to run performance-sensitive advertising data pipelines over public internet, so campaign freshness and bidding quality never see the throughput and latency improvements Direct Connect delivers. 
+  Assuming on-premises to AWS latency is acceptable for hybrid architectures where on-premises bid decisioning queries AWS-hosted audience data on the auction critical path. 
+  Routing cross-cloud advertising data flows over the public internet when AWS Interconnect – multicloud provides a private, provisioned-in-minutes alternative that applies the same private-path data handling controls as Direct Connect. 

 **Benefits of establishing this best practice:** 
+  Audience segment databases at advertising scale (hundreds of millions to billions of records) require terabyte-scale daily transfers between on-premises DMPs and AWS. Direct Connect provides consistent throughput that keeps these transfers within maintenance windows and audience data current for the following day's campaigns. 
+  Direct Connect keeps user behavioral data and audience segment movement on private network paths, which helps improve your adherence to regulatory and advertiser data contract obligations that public internet transfers can meet only with compensating controls that add operational complexity. 
+  Hybrid DSP/DMP migration architectures become viable when on-premises bid decisioning can query AWS-hosted audience data over a private, low-latency connection rather than the public internet, enabling incremental cloud migration without rebuilding the entire bidding stack simultaneously. 
+  The ad tech ecosystem spans multiple cloud providers by design. AWS Interconnect – multicloud enables private connectivity for these cross-cloud advertising data flows, provisioned in minutes through the AWS console rather than through long-running colocation cross-connect arrangements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A large DSP or DMP synchronizing audience segment data daily moves terabytes. A 500-million-record user profile database with behavioral signals is typically 2–5 TB per full refresh. At a 1 Gbps Direct Connect connection, a 2 TB transfer takes approximately 4.5 hours. At 10 Gbps, the same transfer completes in 27 minutes. Sizing determines whether audience data is current for the next day's campaigns or stale from a transfer that ran past its maintenance window. Size connections based on your largest planned transfer within the required completion window, with headroom for growth. 

 Several predictable high-volume events drive peak transfer requirements, such as: 
+  End-of-month campaign performance data exports 
+  Quarterly audience segment rebuilds for seasonal targeting 
+  Pre-event staging for major advertising periods (upfront buying season, Black Friday and Cyber Monday campaigns) 
+  Daily ML training data pipelines that grow as model complexity increases. 

 Public internet connections that appear adequate under average load fail under these peak events. Direct Connect sizing must account for these burst events. 

 Many regulatory frameworks require that personal data transfers maintain appropriate technical safeguards, such as GDPR and CCPA. Advertiser data contracts frequently require that audience data and behavioral signals not traverse public networks, a contractual requirement that public internet transfers violate regardless of encryption. Direct Connect provides the private network path to help improve your adherence to these requirements, reducing the need for compensating controls (such as data masking or tokenization before transfer) that add pipeline complexity and reduce data utility. Under the AWS Shared Responsibility Model, AWS provides the private network infrastructure, but you remain responsible for your overall compliance posture. Consult your compliance and legal teams to confirm the architecture meets your specific regulatory obligations. 

 For advertising companies running hybrid architectures (on-premises legacy DSPs or DMPs alongside cloud-based bidding infrastructure), Direct Connect makes incremental migration viable. An on-premises bid evaluator querying AWS-hosted audience data over a 10 ms Direct Connect connection can meet auction deadlines. The same query over a 40–80 ms public internet round-trip can't. 

 Cross-cloud advertising data flows are a distinct connectivity scenario Direct Connect doesn't address. A publisher running their DMP on Google Cloud sending first-party audience segments to an advertiser's AWS Clean Rooms collaboration, or a third-party measurement provider on Google Cloud receiving impression logs from an AWS-hosted DSP, requires cloud-to-cloud private connectivity. AWS Interconnect – multicloud provides managed private Layer 3 connections between AWS VPCs and other cloud environments, provisioned in minutes through the AWS console by attaching to an existing Direct Connect Gateway. A 500 Mbps tier (one local interconnect per customer, per AWS Region, per generally available cloud provider) covers smaller cross-cloud data flows (such as attribution signals or measurement pixels) on the AWS side, with the other cloud provider charging its side independently. Dedicated speeds are available for higher-volume audience segment transfers. The same regulatory and advertiser data contract considerations that drive Direct Connect adoption for on-premises transfers apply to cross-cloud advertising data flows. Interconnect – multicloud provides the private cloud-to-cloud path that supports these obligations, with the same shared-responsibility caveat that it is a supporting control. We always recommend that you verify your compliance posture with your compliance and legal teams. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Size your Direct Connect connection based on peak advertising calendar events, not average throughput:** Identify your three largest planned transfer events (audience segment rebuilds, ML training data pipelines, campaign reporting exports) and calculate the required completion window for each. Divide the transfer volume by the required window duration to establish the minimum connection speed. Add 40% headroom for growth and concurrent transfers. For advertising workloads with daily audience segment synchronization at terabyte scale, 10 Gbps connections are typically the appropriate starting point. 1 Gbps connections are adequate only for smaller deployments or less frequent synchronization cycles. 

1.  **Configure Direct Connect Gateway for Multi-Region advertising architecture access:** If your advertising architecture spans multiple AWS Regions (common for systems with geographic audience segmentation or regional bidding infrastructure), deploy a Direct Connect Gateway that provides access to all connected Regions through a single on-premises connection. This removes the need for separate Direct Connect connections per Region while enabling on-premises systems to reach audience data, ML training infrastructure, and campaign management systems in each Region. 

1.  **Implement redundant Direct Connect connections for auction-critical hybrid workloads:** For on-premises bid decisioning or DMP systems that query AWS-hosted audience data on the auction critical path, deploy redundant Direct Connect connections in different Direct Connect locations. A single connection failure that forces fallback to public internet latency will cause auction deadline misses for hybrid bidding architectures. Configure BGP routing with appropriate priorities so that failover to the secondary connection is automatic and instantaneous, with the primary connection resuming automatically when restored. 

1.  **Evaluate AWS Interconnect – multicloud for cross-cloud advertising data flows:** Identify advertising data flows that cross cloud boundaries: publisher first-party segment transfers from Google Cloud to AWS Clean Rooms, impression log delivery to Google Cloud-hosted measurement providers, or attribution signal exchange with Azure-hosted partners. For each flow, evaluate whether AWS Interconnect – multicloud provides a viable private path. Use the no-cost 500 Mbps tier for lower-volume flows (measurement signals, attribution pixels) to establish private connectivity without additional cost. For higher-volume flows (audience segment transfers, daily impression log pipelines), provision dedicated bandwidth based on the transfer volume and completion window calculation used in Step 1. Confirm that the Interconnect PoP serving your AWS region has a corresponding entry point for the partner cloud environment before provisioning. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) 
+  [AWS Direct Connect Resiliency Recommendations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) 
+  [Build resilient and scalable multicloud connectivity architectures with AWS Interconnect – multicloud](https://aws.amazon.com/blogs/networking-and-content-delivery/build-resilient-and-scalable-multicloud-connectivity-architectures-with-aws-interconnect-multicloud/) 

 **Related services:** 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [AWS Interconnect – multicloud](https://aws.amazon.com/interconnect/multicloud/) 