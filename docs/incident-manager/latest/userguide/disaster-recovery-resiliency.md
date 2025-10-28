AWS Systems Manager Incident Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Incident Manager,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Resilience in AWS Systems Manager Incident Manager

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which are
connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between zones without interruption. Availability Zones are more highly available,
fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

Incident Manager is a global-regional service and does not currently support Availability
Zones.

In addition to the AWS global infrastructure, Incident Manager offers several features to
help support your data resiliency and backup needs. During the Getting prepared wizard you're
asked to set up a replication set. This regional replication set ensures that your data and
resources are accessible from multiple Regions, making incident management across a
cloud-network more manageable. This replication also ensures that your data is safe and
accessible in the event that one of your Regions goes down.

For more information about using the Incident Manager replication set, see [Configuring the Incident Manager replication set](general-settings.md#replication "general-settings.md#replication").
