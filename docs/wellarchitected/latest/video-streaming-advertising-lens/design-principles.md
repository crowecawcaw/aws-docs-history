

# Design principles

 These design principles underpin all six pillars of the Video Streaming Advertising (VSA) Lens. They describe how to think about designing, building, and operating advertising workloads in the cloud. Individual pillar-level design principles extend these lens-wide principles with domain-specific guidance. 

## Cross-cutting design principles
<a name="cross-cutting-design-principles"></a>
+  **Design for low latency and elastic scaling:** Advertising traffic swings by an order of magnitude with live events, campaign launches, and seasonal peaks, and much of it runs under real-time bidding deadlines. Build horizontally scalable, containerized services behind load balancers, drive auto scaling from application metrics, and cache hot data and content to keep latency low and reduce database load. Choose memory- and CPU-optimized hardware where ultra-low-latency bid paths require it. 
+  **Design for high-volume data and scalable pipelines:** Advertising generates large volumes of bid, impression, and event data at high write rates across regions. Favor distributed, write-optimized data stores, streaming ingestion, and event-driven precomputation over synchronous processing on the critical path. Combine real-time streaming with batch analytics, aggregate into a cataloged data lake, and apply compression, tiered storage, and archival policies to control cost, while monitoring latency, timeouts, and saturation to find bottlenecks. 
+  **Design for cost efficiency at advertising scale:** The main cost drivers are data transfer, compute, storage, and networking, and at campaign volumes even small per-request savings compound. Minimize wasted traffic and processing, and provide sufficient but not excessive capacity through auto scaling rather than static over-provisioning. 
+  **Design for privacy, security, and regulatory adherence:** Treat every partner as an independent trust domain with strong access control, encryption, and industry-standard fraud detection. Address third-party signal loss with privacy-enhancing technologies such as data clean rooms and confidential computing, first-party data, and contextual targeting. Manage consent and data rights, and treat regional and industry regulations (GDPR, CCPA, and programmatic advertising standards) as a design constraint rather than an afterthought. 
+  **Design for generative and agentic AI:** Use generative AI for creative optimization, contextual targeting, and personalized experiences at scale, and agentic workflows to automate decisions across campaign management, bid optimization, and audience segmentation. Adopt standardized industry frameworks (AdCP and ARTF from IAB Tech Lab), and apply responsible-AI practices with human oversight, bias detection, and explainability. 
+  **Design publisher monetization for automation and linear-digital convergence:** Automate the chain from content through ad insertion to revenue reporting, and keep auction, playout, and channel-assembly components stateless and horizontally scalable so they absorb traffic spikes without manual intervention. Converge linear and digital operations onto shared infrastructure and a unified data foundation for campaign planning, fulfillment, pacing, and cross-platform measurement. 

## Pillar-level design principles
<a name="pillar-level-design-principles"></a>

 For design principles specific to each Well-Architected pillar, see: 
+  [Operational Excellence design principles](ops-design-principles.md) 
+  [Security design principles](sec-design-principles.md) 
+  [Reliability design principles](rel-design-principles.md) 
+  [Performance Efficiency design principles](perf-design-principles.md) 
+  [Cost Optimization design principles](cost-design-principles.md) 
+  [Sustainability design principles](sus-design-principles.md) 