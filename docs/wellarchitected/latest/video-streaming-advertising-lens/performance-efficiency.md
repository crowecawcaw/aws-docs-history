# Performance efficiency

The performance efficiency pillar includes the ability to use cloud
computing resources efficiently to meet system requirements and to
maintain that efficiency as demand changes and technologies evolve.

The performance efficiency pillar provides an overview of design
principles, best practices, and questions. You can find guidance on
implementation in the
[**Performance
Efficiency Pillar whitepaper**](../performance-efficiency-pillar/welcome.md "../performance-efficiency-pillar/welcome.md").

## Design principles

The following design principles can help you achieve and maintain
efficient advertising workloads in the cloud:

- **Design for optimized cost:** The
  key to cost optimization for advertising workloads is to
  minimize costs while you maintain a required level of performance and reliability.
- **Design for handling low latency,
  bursty, and spiky traffic:** Build a scalable
  architecture with automated scaling capacity to enable rapid
  increases and decreases of traffic gracefully. Cache
  application data content, when possible, to reduce response
  latency and the load on database clusters. Use containerized
  workloads and prebuilt container images for fast scaling and
  predictable performance. Choose server hardware optimized for
  memory and CPU for ultra-low latency needs.
- **Design for large data volumes and
  transactions:** Build a scalable distributed database
  for transactions while optimizing it for fast writes. Consider
  use of a distributed NoSQL database that can handle high write
  throughput with linear scalability. Consider compression
  techniques to optimize storage and an appropriate caching
  strategy to reduce database load for user profiles, target
  segments, and creatives. Use streaming services for ingestion
  and transportation of event data. Set up auto scaling
  databases to handle traffic spikes. Implement a data archive
  strategy to purge old ad impressions data to more cost optimized
  storage. Monitor database performance metrics, including
  latency, timeouts, and saturation, to identify and fix
  bottlenecks.
- **Design for data volume and query processing consideration for AWS Clean Rooms collaboration:** Large datasets can impact query performance. Consider data partition, aggregations, and filters to reduce result sets. Complex joins across multiple tables and number of collaborators can impact processing team. As a result, the optimal design for collaborators uses one to many collaboration channels, along with optimized pre-compiled query templates.
