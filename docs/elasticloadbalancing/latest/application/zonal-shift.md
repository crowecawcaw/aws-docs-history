

# Zonal shift for your Application Load Balancer
<a name="zonal-shift"></a>

Zonal shift and zonal autoshift are features of Amazon Application Recovery Controller (ARC). With zonal shift, you can shift traffic away from an impaired Availability Zone with a single action. This way, you can continue operating from other healthy Availability Zones in an AWS Region.

With zonal autoshift, you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. AWS starts an autoshift when internal monitoring indicates that there is an Availability Zone impairment that could potentially impact customers. When AWS starts an autoshift, application traffic to resources that you've configured for zonal autoshift starts shifting away from the Availability Zone.

When you start a zonal shift, your load balancer stops sending new traffic for the resource to the affected Availability Zone. ARC creates the zonal shift immediately. However, it can take a short time for existing, in-progress connections in the Availability Zone to complete, depending on client behavior and connection reuse. Depending on your DNS settings and other factors, existing connections can complete in just a few minutes, or might take longer. For more information, see [Limit the time that clients stay connected to your endpoints](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.zonal-shifts.html#arc-zonal-shift.existing-connections) in the *Amazon Application Recovery Controller (ARC) Developer Guide*.

**Topics**
+ [Before you begin](#zonal-shift-before-you-begin)
+ [Cross-zone load balancing](#cross-zone-enabled)
+ [Administrative override](#admin-override)
+ [Enable zonal shift](enable-zonal-shift.md)
+ [Start a zonal shift](start-zonal-shift.md)
+ [Update a zonal shift](update-zonal-shift.md)
+ [Cancel a zonal shift](cancel-zonal-shift.md)

## Before you begin a zonal shift
<a name="zonal-shift-before-you-begin"></a>
+ Zonal shift is disabled by default and must be enabled on each Application Load Balancer. For more information, see [Enable zonal shift for your Application Load Balancer](enable-zonal-shift.md).
+ You can start a zonal shift for a specific load balancer only for a single Availability Zone. You can't start a zonal shift for multiple Availability Zones.
+ AWS proactively removes zonal load balancer IP addresses from DNS when multiple infrastructure issues impact services. Always check current Availability Zone capacity before you start a zonal shift. If your load balancers have cross-zone load balancing turned off and you use a zonal shift to remove a zonal load balancer IP address, the Availability Zone affected by the zonal shift also loses target capacity.

For more information, see [Best practices for zonal shifts in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.zonal-shifts.html) in the *Amazon Application Recovery Controller (ARC) Developer Guide*.

## Cross-zone load balancing
<a name="cross-zone-enabled"></a>

When a zonal shift is started on an Application Load Balancer with cross-zone load balancing enabled, all traffic to targets is blocked in the availability zone being impacted, and zonal IP addresses are removed from DNS.

**Benefits:**
+ Quicker recovery from availability zone failures.
+ The ability to move traffic to a healthy availability zone if failures are detected in an availability zone.
+ You can test application integrity by simulating and identifying failures to prevent unplanned downtime.

## Zonal shift administrative override
<a name="admin-override"></a>

Targets that belong to a Application Load Balancer include a new status `AdministrativeOverride`, which is independent from the `TargetHealth` state.

When a zonal shift is started for a Application Load Balancer, all targets within the zone being shifted away from are considered administratively overridden. The Application Load Balancer stops routing new traffic to administratively overridden targets. Existing connections remain intact until they are organically closed.

The possible `AdministrativeOverride` states are:

**unknown**  
State cannot be propagated due to an internal error

**no\_override**  
No override is currently active on target

**zonal\_shift\_active**  
Zonal shift is active in target Availability Zone