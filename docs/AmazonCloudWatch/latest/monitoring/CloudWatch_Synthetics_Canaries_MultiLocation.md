# Multilocation canaries

Amazon CloudWatch Synthetics lets you run the same canary across multiple AWS Regions
simultaneously from a single point of management. These are called
_multilocation canaries_. You create and manage the canary in one Region
(the _primary location_), and CloudWatch Synthetics automatically replicates it to
the additional Regions (the _replica locations_) that you choose. All
runs, metrics, and artifacts are consolidated in the primary Region, giving you a unified
view of your application's performance and availability worldwide.

Use multilocation canaries for the following benefits:

- **Make sure consistent user experience**—Run
  canaries from different parts of the world to verify that your users everywhere receive
  a consistent, high-quality experience.
- **Establish location-specific baselines**—
  Each Region might have different performance characteristics due to factors such as
  network latency and data center proximity. Running canaries from multiple locations
  creates performance baselines for each location, helping you distinguish normal
  variations from anomalies.
- **Identify regional performance issues**—
  Performance and availability can vary significantly across locations due to network
  latency, ISP throttling, or regional outages. Testing from diverse global locations
  helps pinpoint Region-specific bottlenecks that might not be apparent from a single
  location.
- **Validate third-party services and CDNs**—
  Verify that your third-party dependencies such as payment processors, content delivery
  networks, and advertisement services are working across all Regions. Use the data to
  hold vendors accountable for their SLAs.
- **Reduce false positives**—Configure alarms
  that activate only when issues are detected from multiple locations. This approach
  avoids unnecessary notifications caused by isolated transient network glitches, so that
  your teams can focus on critical problems.

###### How multilocation canaries work

A multilocation canary uses a primary and replica model. The canary in the primary
Region acts as the source of truth for configuration. CloudWatch Synthetics automatically
creates replicas in your chosen Regions, and each replica runs independently using the
same script, schedule, and environment variables. All mutating operations (create, update,
start, stop, delete) are performed from the primary Region and asynchronously propagated
to replicas. Run data from all locations is consolidated in the primary Region.

###### Prerequisites

Before you create a multilocation canary, consider the following requirements:

- Multilocation canaries require runtime version
  `syn-nodejs-puppeteer-16.0` or later, or
  `syn-nodejs-playwright-7.0` or later.
- Available in all AWS commercial Regions. Not available in AWS GovCloud (US)
  or China Regions.
- You can add up to 50 replica locations.
- Tags are not replicated to replica Regions. To add tags to a replica, navigate to
  the replica Region and add tags directly.
- Environment variables from the primary canary are applied to all replicas.
- All locations use the same script and schedule.
- Each replica requires its own VPC configuration if VPC connectivity is needed. VPC
  settings are not inherited from the primary Region.
- Cost scales linearly with the number of replicas. Each replica incurs the same cost
  as a standalone canary.

###### Topics

- [Permissions for multilocation canaries](CloudWatch_Synthetics_MultiLocation_Permissions.md "CloudWatch_Synthetics_MultiLocation_Permissions.md")
- [Managing multilocation canaries](CloudWatch_Synthetics_MultiLocation_Managing.md "CloudWatch_Synthetics_MultiLocation_Managing.md")
- [Monitoring and troubleshooting multilocation canaries](CloudWatch_Synthetics_MultiLocation_Monitoring.md "CloudWatch_Synthetics_MultiLocation_Monitoring.md")
- [Using log centralization with multilocation canaries](CloudWatch_Synthetics_MultiLocation_Log_Centralization.md "CloudWatch_Synthetics_MultiLocation_Log_Centralization.md")
