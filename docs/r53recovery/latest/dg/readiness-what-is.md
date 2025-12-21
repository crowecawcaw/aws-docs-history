# What is readiness check in Amazon Application Recovery Controller (ARC)?

A readiness check in ARC continually (at one-minute intervals) audits for mismatches in AWS provisioned capacity, service quotas, throttle
limits, and configuration and version discrepancies for the resources included in the check. Readiness checks can notify you of these
differences so that you can make sure that each replica has the same configuration setup and the same runtime state. Although
readiness checks ensure that your configured capacities across replicas are consistent, you should not expect them
to decide on your behalf what the capacity of your replica should be. For example, you should understand your application requirements
so that you size your Auto Scaling groups with enough buffer capacity in each replica to manage if another cell is unavailable.

For quotas,
when ARC detects a mismatch with a readiness check, it can take steps to align the quotas for the replicas by increasing the
lower quota to match the higher quota. When the quotas match, the readiness check status shows `READY`. (Note
that this isn't an immediate update process, and the total time depends on the specific resource type and other factors.)

The first step is setting up readiness checks to create a [recovery group](recovery-readiness.md "recovery-readiness.md")
that represents your application.
Each recovery group includes _cells_ for each individual failure-containment unit or _replica_ of
your application. Next, you create [resource sets](recovery-readiness.recovery-groups.md "recovery-readiness.recovery-groups.md")
for each resource type in your application, and associate
_readiness checks_ with the resource sets. Finally, you associate the resources with _readiness scopes_,
so you can get readiness status about the resources in a recovery group (your application) or individual cells (replicas, which are
Regions or Availability Zones (AZs)).

Readiness (that is, `READY` or `NOT READY`) is based on the resources that are in the scope of the readiness
check and the set of rules for a resource type. There are [sets of readiness rules](recovery-readiness.md#recovery-readiness.list-rules "recovery-readiness.md#recovery-readiness.list-rules")
for each resource type, which ARC checks use to audit resources for readiness. Whether a resource is `READY` or not
is based on how each readiness rule is defined. All readiness rules evaluate resources, but some compare resources to each other
and some look at specific information about each resource in the resource set.

By adding readiness checks, you can monitor readiness status, in one of several ways: with EventBridge, in the AWS Management Console, or by using
ARC API actions. You can also monitor readiness status of resources in different contexts, including the readiness of cells and the readiness of your
application. Use the [cross-account authorization](recovery-readiness.md "recovery-readiness.md")
feature in ARC to make it easier to set up and monitor distributed resources from a single AWS account.

## Monitoring application replicas with readiness checks

ARC audits your application replicas by using _readiness
checks_ to ensure that each one has the same configuration setup and the same runtime state.
A readiness check continually audits AWS resource capacity,
configuration, AWS quotas, and routing policies for an application, information that
you can use to help make sure that replicas are ready for failover. Readiness checks help you to ensure that
your recovery environment is scaled and configured to fail over to when needed.

The following sections provide more details about how readiness check works.

### Readiness checks and your application replicas

To be prepared for recovery, you must maintain sufficient spare capacity in replicas at all times, to absorb failover traffic from another
Availability Zone or Region. ARC continually (once a minute) inspects your application to ensure that your provisioned capacity matches across all
Availability Zones or Regions.

The capacity that ARC inspects includes, for example, Amazon EC2 instance counts, Aurora read and write capacity units,
and Amazon EBS volume size. If you scale up the capacity in your primary replica for resource values but forget to also increase the corresponding values in
your standby replica, ARC detects the mismatch so that you can increase the values in the standby.

###### Important

Readiness checks are most useful for verifying, on an ongoing basis, that application replica
configurations and runtime states are aligned. Readiness checks shouldn't be used to indicate whether your
production replica is healthy, nor should you rely on readiness checks as a primary trigger for failover
during a disaster event.

In an active-standby configuration, you should make decisions about whether to fail away from or to a cell based on your monitoring and health check
systems, and consider readiness checks as a complementary service to those systems. ARC readiness checks are not highly available, so you should
not depend on the checks being accessible during an outage. In addition, the resources that are checked might also not be available during a disaster
event.

You can monitor the readiness status for your application's resources in specific cells (AWS Regions or Availability Zones)
or for your overall application. You can be notified when a readiness check status changes, for example, to `Not ready`,
by creating rules in EventBridge. For more information, see [Using readiness check in ARC with Amazon EventBridge](eventbridge-readiness.md "eventbridge-readiness.md"). You can also view
readiness status in the AWS Management Console, or by using API operations, such as `get-recovery-readiness`. For more information,
see [Readiness check API operations](actions.md "actions.md").

### How readiness check works

ARC audits your application replicas by using _readiness
checks_ to ensure that each one has the same configuration setup and the same runtime state.

To be prepared for recovery, for example, you must maintain sufficient spare capacity at all times to absorb failover traffic from another
Availability Zone or Region. ARC continually (once a minute) inspects your application to ensure that your provisioned capacity matches across all
Availability Zones or Regions. The capacity that ARC inspects includes, for example, Amazon EC2 instance counts, Aurora read and write capacity units,
and Amazon EBS volume size. If you scale up the capacity in your primary replica for resource values but forget to also increase the corresponding values in
your standby replica, ARC detects the mismatch so that you can increase the values in the standby.

###### Important

Readiness checks are most useful for verifying, on an ongoing basis, that application replica
configurations and runtime states are aligned. Readiness checks shouldn't be used to indicate whether your
production replica is healthy, nor should you rely on readiness checks as a primary trigger for failover
during a disaster event.

In an active-standby configuration, you should make decisions about whether to fail away from or to a cell based on your monitoring and health check
systems, and consider readiness checks as a complementary service to those systems. ARC readiness checks are not highly available, so you should
not depend on the checks being accessible during an outage. In addition, the resources that are checked might also not be available during a disaster
event.

You can monitor the readiness status for your application's resources in specific cells (AWS Regions or Availability Zones)
or for your overall application. You can be notified when a readiness check status changes, for example, to `Not ready`,
by creating rules in EventBridge. For more information, see [Using readiness check in ARC with Amazon EventBridge](eventbridge-readiness.md "eventbridge-readiness.md"). You can also view
readiness status in the AWS Management Console, or by using API operations, such as `get-recovery-readiness`. For more information,
see [Readiness check API operations](actions.md "actions.md").
