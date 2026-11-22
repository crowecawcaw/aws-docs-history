

# Performance efficiency

 The performance efficiency pillar covers the efficient use of computing resources to meet your requirements, and keeping that efficiency as demand changes and technologies evolve. In on-premises environments, sustained performance is hard to achieve because capacity is fixed when you buy it and slow to change. The cloud removes that constraint, and the practices in this pillar help you build a high-performing architecture and keep it that way as your workload and the available technologies change. 

 The pillar is organized into five capabilities, each with its own best practices: 

## Performance requirements
<a name="performance-requirements"></a>
+  [Validate workload performance requirements](perf01.md). Set the performance requirements and KPIs that reflect business needs, and define the tolerances and alerts that signal when performance drops. 

## Resource selection and configuration
<a name="resource-selection-and-configuration"></a>
+  [Compute and hardware](perf02.md). Select, configure, and scale the compute options and hardware accelerators that best match the workload. 
+  [Data management](perf03.md). Choose purpose-built data stores, configure them for the workload's access patterns, and use caching and query strategies to meet performance targets. 
+  [Networking and content delivery](perf04.md). Select the networking features, connectivity, load balancing, protocols, and workload location that meet your latency and throughput requirements. 

## Monitor, test, and improve
<a name="monitor-test-and-improve"></a>
+  [Monitor, test, and improve workload performance](perf05.md). Monitor performance where it matters most, test and evaluate the workload, and remediate issues before they affect users. 

 Take a data-driven approach to building a high-performing architecture. Gather data on all aspects of the architecture, from the high-level design to the selection and configuration of resource types, and review your choices regularly so you can take advantage of the evolving AWS Cloud. Monitor the workload so you notice any deviation from expected performance, and make deliberate trade-offs where they help, such as using compression or caching, or relaxing consistency requirements. 

 This guidance is written for the technology roles responsible for designing and running performant workloads, including chief technology officers (CTOs), architects, developers, DevOps and infrastructure engineers, and operations teams. After reading it, you will understand the AWS recommendations and strategies to apply when you design cloud architectures for performance efficiency, so you can meet your performance requirements and sustain them as demand grows and technologies change. 