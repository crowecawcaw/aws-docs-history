# Reliability

Reliable and resilient data infrastructure is critical for manufacturing organizations to
drive sustained innovation, operational excellence, and product quality. MIDA is designed with
reliability as a core principle, verifying that data is consistently available, processed
correctly, and recoverable even in the face of disruptions.

Manufacturing environments face unique reliability challenges due to their hybrid nature
and critical operational requirements. The integration of OT with IT systems, real-time
processing needs, and the necessity to maintain production continuity demand a sophisticated
approach to reliability. MIDA addresses these challenges through a comprehensive architecture
that spans from the shop floor to the cloud.

The architecture employs a hybrid edge-cloud model where edge components provide
resilient local processing for mission-critical applications while cloud infrastructure offers
scalable, fault-tolerant services for broader data management and analytics. This approach
means that manufacturing operations can continue even during network disruptions, maintaining
data consistency and enabling recovery across the entire system.

Through services like AWS IoT Greengrass, AWS IoT SiteWise, Amazon Kinesis, and
purpose-built databases, MIDA provides the foundation for highly available manufacturing
systems. The architecture incorporates automated failover, data replication, and comprehensive
monitoring capabilities to provide reliability at every layer, from sensor data collection to
enterprise-wide analytics.

###### Topics

- [Design principles](design-principles-rel.md "design-principles-rel.md")
- [Foundations](foundations.md "foundations.md")
- [Workload architecture](workload-architecture.md "workload-architecture.md")
- [Change management](change-management.md "change-management.md")
- [Failure management](failure-management.md "failure-management.md")
