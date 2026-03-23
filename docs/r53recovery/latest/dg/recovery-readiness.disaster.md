# Readiness checks and disaster recovery scenarios

ARC readiness checks give you insights into whether your applications and resources are ready for recovery
by helping you make sure that your applications are scaled to handle failover traffic. Readiness check statuses should
not be used as a signal to indicate that a production replica is healthy.
You can, however, use readiness checks as a supplement to your application and infrastructure monitoring
or health checker systems to determine whether to fail away from or to a replica.

In an urgent situation or an outage, use a combination of health checks and other information to determine that
your standby is scaled up, healthy, and ready for you to fail over production traffic. For example, check to see if canaries
that run against your standby cell are meeting your success criteria, in addition to verifying that readiness check
statuses for the standby are `READY`.

Be aware that ARC readiness checks are hosted in a single AWS
Region, US West (Oregon), and during an outage or disaster, readiness check information could
become stale or the checks could become unavailable. For more information, see [Data and control planes for routing control](data-and-control-planes.md "data-and-control-planes.md").
