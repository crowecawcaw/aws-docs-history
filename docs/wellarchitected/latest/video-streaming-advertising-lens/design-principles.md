# Design principles

The following design principles can help you achieve and maintain efficient advertising
workloads in the cloud.

- **Design for low latency and rapid changes in traffic volume:**
  Build a scalable architecture with automated scaling capacity to enable rapid increases and
  decreases of traffic gracefully. Use load balancers to distribute traffic to new nodes
  available to scale horizontally. Implement auto scaling based on application node
  metrics. Cache application data content, when possible, to reduce response latency and the
  load on database clusters. Use containerized workloads and prebuilt container images
  for fast scaling and predictable performance. Choose server hardware optimized for memory
  and CPU for ultra-low latency needs.
- **Design for rapid growth, very large data volumes, high QPS (queries
  per second), and low latency transactions across multiple Regions:** Build a
  scalable distributed database for transactions while optimizing it for fast writes. Consider
  use of a distributed NoSQL database that can handle high write throughput with linear
  scalability. Consider compression techniques to optimize storage and an appropriate caching
  strategy to reduce database load for user profiles, target segments, and creatives. Use
  streaming services for ingestion and transportation of event data. Set up auto scaling
  databases to handle traffic spikes. Implement a data archive strategy to purge old ad
  impressions data to less expensive storage. Monitor database performance metrics, including
  latency, timeouts, and saturation, to identify and fix bottlenecks.
- **Design for cost optimization to reduce costs while maintaining
  performance:** The key to cost optimization for advertising workloads is to
  minimize costs while you maintain performance and reliability. Optimization efforts should
  focus on minimizing unnecessary traffic charges and providing sufficient but not excessive
  capacity through auto scaling. The main drivers of advertisement costs are data transfer,
  compute, storage, and networking. Considering the large amounts of traffic involved in
  campaigns, even small changes can yield significant cost optimization.
- **Design for scaled, cost-optimized, and performant data pipelines:** Use event-driven architecture and pre-compute data where possible to reduce real-time compute needs. Design for horizontal scalability rather than optimizing within a single host. For large-scale systems, consider distributed service-oriented architecture to allow components to innovate independently. Use caching solutions at scale, with multiple replicas for high availability and data recovery. Implement real-time introspection and debugging capabilities for system transparency. When dealing with massive data volumes, consider batching and direct writing to object storage instead of using intermediary services. Use a combination of real-time streaming and batch analytics processing for data processing, based on specific use cases. Implement a centralized data lake for aggregating data from various sources with a data catalog. Use tiered storage solutions to balance cost and performance for data storage. Reuse compute resources like analytics clusters, to reduce costs and startup times. Retain all event-level data and logs for less than 30 days.
- **Design for privacy-enhanced collaboration:** Consider the following strategies to address third-party signal loss through linked first-party data, browser and OS-mediated data, and unlinked first-party data. Use linked first-party data design, where advertiser and publisher data are connected through privacy-enhancing technologies (PETs), enabling personalized customer engagement and targeting while maintaining privacy. Use browser and OS-mediated data design where web browsers or operating systems act as intermediaries for user data collection and sharing. It protects user privacy by limiting direct access to personal information, instead of providing aggregated or anonymized data to advertisers and websites. Use contextual targeting to deliver relevant ads without relying on user data and seller-defined audience solutions which allow publishers to create targetable segments based on their first-party data. Implement first-party and third-party identity matching and identity transcoding that use trusted and compliant runtime environments like data clean rooms and confidential computing environments. Design for robust access controls, audit trails, and secured data exchange mechanisms for your organization and partners. Design for alignment on file formats, APIs, communication protocols, and data schemas, ideally with standardized industry formats as defined by the Interactive Advertising Bureau (IAB).
- **Design for advertising regulatory, security, and privacy needs:** Design for robust access control and network security measures, complemented by industry-standard ad fraud detection software and anti-fraud tools. Design for monitoring and assessment of ads to facilitate policy compliance and malicious content detection, while maintaining strong consumer privacy protection, and managing consent and data rights. Consider regulatory standards involved for ad formats and creative standards (IAB), measurement standards (MRC, IAB), privacy and consent standards (IAB, regional regulations for example, China, CCPA, and GDPR), programmatic advertising standards (IAB, openRTB consortium), brand safety and fraud prevention (TAG, IAB), identity and attribution (U-ID2.0, rampID, ID5, MTA) and specific ad standards published by Google, Meta, and Amazon.
