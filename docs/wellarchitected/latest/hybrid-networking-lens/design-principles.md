# Design principles

The following design principles can help you deploy and maintain efficient hybrid network
connectivity between AWS and your on-premises locations:

- **Deploy connectivity for scalability:** Hybrid network
  connectivity scales dynamically with your business and application needs. Your application
  performance requirements will determine which network factors to prioritized: bandwidth,
  latency, jitter, and packet loss. Bandwidth determines your connection's data transfer rate.
  Latency measures packet travel time between endpoints and increases with distance due to the
  speed of light. Jitter indicates how consistent your network latency remains over time.
  Packet loss quantifies what percentage of network traffic fails to reach its destination. As
  your business evolves, performance requirements may shift. You might need to prioritize
  different factors or implement solutions that address multiple performance considerations
  simultaneously.
- **Deploy connectivity for flexibility:** Hybrid network
  connectivity empowers organizations to maximize the strengths of diverse environments,
  balancing performance, cost, and provisioning timelines. Your connectivity choice—whether
  internet-based, dedicated, or partner-hosted connections—directly impacts deployment
  timeframes, which can range from hours to months depending on on-premises locations and
  existing network infrastructure. When planning your hybrid architecture, consider how
  provisioning constraints and evolving performance needs might affect your ability to scale
  connectivity. Start with your immediate requirements, but design for future growth,
  recognizing that initial connectivity decisions will shape your options for network
  expansion.
- **Deploy secure connectivity:** Hybrid networks require robust
  security measures to protect sensitive data across diverse environments. Your connectivity
  strategy must align with security requirements and policies, whether you need internet-based
  or private network connections, and whether encryption in transit is mandatory. Segregating
  network segments is essential to contain potential security breaches by limiting the impact
  of compromised resources. Security posture is improved through isolation and granular
  security controls across different environments. By implementing these secure connectivity
  strategies, you can establish protected communication channels of your hybrid connectivity
  while maintaining compliance with your security policies.
- **Deploy resilient connectivity:** Resiliency must be
  determined based off of business outcomes and will determine architecture decisions. Network
  reliability, measured through availability and resiliency, requires tailoring your
  connectivity design to specific SLAs. This involves deploying redundant components to
  eliminate single points of failure, designing appropriate failover time, applying traffic
  engineering across connections, and provisioning sufficient capacity. The required
  reliability level varies by workload criticality, with critical applications possibly
  warranting maximum resiliency across multiple locations, while less critical workloads may
  only need single-site redundancy. Since increasing reliability increases costs, evaluate
  your business requirements to find the right balance.
- **Optimize cost:** Hybrid networks can optimize resource
  utilization by leveraging the most cost-effective environment for specific workloads.
  Understanding the cost components of hybrid networking is essential for effective
  optimization. The cost structure of hybrid networking includes provisioned resources cost
  representing the cost of maintaining hybrid connectivity infrastructure, usage cost covers
  data transfer and processing between environments, and connectivity cost from service
  providers to connect your network location to network points of presence. Effective cost
  optimization in hybrid networks requires a balance between performance, reliability, and
  capacity. By implementing targeted cost optimization strategies, you can create a more
  efficient hybrid network architecture that aligns with your business and technical
  requirements while minimizing wasted expenditure.
