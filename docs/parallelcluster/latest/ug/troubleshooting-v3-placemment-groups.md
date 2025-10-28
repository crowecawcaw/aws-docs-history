# Placement groups and instance launch issues

To get the lowest inter-node latency, use a _placement group_. A placement group ensures that your instances are on the
same networking backbone. If there aren't enough instances available when a request is made, an `InsufficientInstanceCapacity` error is
returned. To reduce the possibility of receiving this error when using cluster placement groups, set the [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") / [PlacementGroup](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") / [Enabled](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Enabled "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Enabled") parameter to `false`.

For additional control over capacity access, consider [launching instances with ODCR (On-Demand Capacity Reservations)](launch-instances-odcr-v3.md "launch-instances-odcr-v3.md").

For more information, see [Troubleshooting instance
launch issues](../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md "../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md") and [Placement
groups roles and limitations](../../../AWSEC2/latest/UserGuide/placement-groups.md#concepts-placement-groups "../../../AWSEC2/latest/UserGuide/placement-groups.md#concepts-placement-groups") in the _Amazon EC2 User Guide for Linux Instances_.
