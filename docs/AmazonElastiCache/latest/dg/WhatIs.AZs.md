# AWS Regions and Availability Zones

Amazon cloud computing resources are housed in highly available data center facilities in different areas of the world (for example, North America, Europe, or Asia).
Each data center location is called an AWS Region.

Each AWS Region contains multiple distinct locations called Availability Zones, or AZs. Each Availability Zone is engineered to be isolated from
failures in other Availability Zones. Each is engineered to provide inexpensive, low-latency network connectivity to other Availability Zones in
the same AWS Region. By launching instances in separate Availability Zones, you can protect your applications from the failure of a single location.
For more information, see [Choosing regions and availability zones](RegionsAndAZs.md "RegionsAndAZs.md").

You can create your cluster in several Availability Zones, an option called a Multi-AZ deployment. When you choose this option, Amazon automatically provisions and maintains a secondary standby node instance in a different Availability Zone. Your primary node instance is asynchronously replicated across Availability Zones to the secondary instance. This approach helps provide data redundancy and failover support, eliminate I/O freezes, and minimize latency spikes during system backups.
For more information, see [Minimizing downtime in ElastiCache for Valkey and Redis OSS with Multi-AZ](AutoFailover.md "AutoFailover.md").
