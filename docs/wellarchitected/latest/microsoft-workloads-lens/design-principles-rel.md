# Design principles

- **Use Microsoft high availability patterns:** Implement SQL
  Server Always On Availability Groups across multiple Availability Zones, deploy Active
  Directory domain controllers with proper site topology, and use Exchange Database
  Availability Groups to maintain Microsoft workload resilience while benefiting from AWS
  infrastructure reliability.
- **Integrate with AWS managed services for Microsoft
  technologies:** Use Amazon RDS Multi-AZ for SQL Server, AWS Managed Microsoft AD for directory
  services, and Amazon FSx for Windows File Server to reduce operational overhead while maintaining Microsoft
  workload compatibility and using AWS managed reliability features.
- **Design for cross-AZ resilience with Microsoft-aware
  configurations:** Configure SQL Server listener endpoints across Availability
  Zones, establish Active Directory sites aligned with Availability Zones, implement
  SharePoint farm topology with cross-AZ redundancy, and verify that .NET applications
  handle Availability Zone failures gracefully through stateless design and proper load
  balancing.
  For general reliability design principles that apply to all workloads, see [Design principles for reliability](../reliability-pillar/design-principles.md "../reliability-pillar/design-principles.md").
