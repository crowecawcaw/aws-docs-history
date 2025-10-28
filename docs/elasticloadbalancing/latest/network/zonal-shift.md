# Zonal shift for your Network Load Balancer

Zonal shift is a capability in Amazon Application Recovery Controller (ARC). With zonal shift,
you can shift a Network Load Balancer resource away from an impaired Availability Zone
with a single action. This way, you can continue operating from other healthy
Availability Zones in an AWS Region.

When you start a zonal shift, your Network Load Balancer stops routing traffic to targets in
the affected Availability Zone. Existing connections to targets in the affected
Availability Zone are not terminated by zonal shift. It might take several minutes
for these connections to complete gracefully.

###### Contents

- [Before you begin](#zonal-shift-before-you-begin "#zonal-shift-before-you-begin")
- [Administrative override](#admin-override "#admin-override")
- [Enable zonal shift](enable-zonal-shift.md "enable-zonal-shift.md")
- [Start a zonal shift](start-zonal-shift.md "start-zonal-shift.md")
- [Update a zonal shift](update-zonal-shift.md "update-zonal-shift.md")
- [Cancel a zonal shift](cancel-zonal-shift.md "cancel-zonal-shift.md")

## Before you begin a zonal shift

- Zonal shift is disabled by default and must be enabled on each Network Load Balancer. For more information, see
  [Enable zonal shift for your Network Load Balancer](enable-zonal-shift.md "enable-zonal-shift.md").
- You can start a zonal shift for a specific Network Load Balancer only for a single
  Availability Zone. You can't start a zonal shift for
  multiple Availability Zones.
- AWS proactively removes zonal Network Load Balancer IP addresses from DNS when
  multiple infrastructure issues impact services. Always check current Availability
  Zone capacity before you start a zonal shift. If you use a zonal shift on your Network Load Balancer,
  the Availability Zone affected by the zonal shift also loses target capacity.
- During zonal shift on Network Load Balancers with cross-zone load balancing enabled, the zonal load
  balancer IP addresses are removed from DNS. Existing connections to targets in the
  impaired Availability Zone persist until they organically close, while new connections
  are no longer routed to targets in the impaired Availability Zone.

For more information, see [Best practices for zonal shifts in ARC](../../../r53recovery/latest/dg/route53-arc-best-practices.md "../../../r53recovery/latest/dg/route53-arc-best-practices.md") in the _Amazon Application Recovery Controller (ARC)
Developer Guide_.

## Zonal shift administrative override

Targets that belong to a Network Load Balancer will include a new status `AdministrativeOverride`, which is independent from the
`TargetHealth` state.

When a zonal shift is started for a Network Load Balancer, all targets within the zone being shifted away from are
considered administratively overridden. The Network Load Balancer stops routing new traffic to administratively overridden
targets. Existing connections remain intact until they are organically closed.

The possible `AdministrativeOverride` states are:

**unknown**

State cannot be propagated due to an internal error

**no_override**

No override is currently active on target

**zonal_shift_active**

Zonal shift is active in target Availability Zone

**zonal_shift_delegated_to_dns**

This target's zonal shift state is not available through `DescribeTargetHealth`
but can be viewed directly through the AWS ARC - Zonal Shift API or console.
