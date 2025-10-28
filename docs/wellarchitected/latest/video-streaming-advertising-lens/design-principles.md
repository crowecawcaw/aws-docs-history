# Design principles

The following design principles can help you achieve and maintain
efficient advertising workloads in the cloud.

- **Design for low latency and rapid changes in
  traffic volume:** Build a scalable architecture with
  automated scaling capacity to enable rapid increases and decreases
  of traffic gracefully. Use load balancers to distribute traffic to
  new nodes available to scale horizontally. Implement auto scaling
  based on application node metrics. Cache application data content,
  when possible, to reduce response latency and the load on database
  clusters. Use containerized workloads and prebuilt container images
  for fast scaling and predictable performance. Choose server hardware
  optimized for memory and CPU for ultra-low latency needs.
- **Design for rapid growth, very large data
  volumes, high QPS (queries per second), and low latency transactions across multiple
  Regions:** Build a scalable distributed database for
  transactions while optimizing it for fast writes. Consider use of a
  distributed NoSQL database that can handle high write throughput
  with linear scalability. Consider compression techniques to optimize
  storage and an appropriate caching strategy to reduce database load
  for user profiles, target segments, and creatives. Use streaming
  services for ingestion and transportation of event data. Set up auto
  scaling databases to handle traffic spikes. Implement a data archive
  strategy to purge old ad impressions data to less expensive storage.
  Monitor database performance metrics, including latency, timeouts,
  and saturation, to identify and fix bottlenecks.
- **Design for cost optimization to reduce costs
  while maintaining performance:** The key to cost
  optimization for advertising workloads is to minimize costs while
  you maintain performance and reliability. Optimization efforts
  should focus on minimizing unnecessary traffic charges and providing
  sufficient but not excessive capacity through auto scaling. The main
  drivers of advertisement costs are data transfer, compute, storage,
  and networking. Considering the large amounts of traffic involved in
  campaigns, even small changes can yield significant cost
  optimization.
