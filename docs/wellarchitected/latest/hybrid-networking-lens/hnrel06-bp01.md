# HNREL06-BP01 Use multiple data centers for physical location

redundancy

Connect from multiple geographically separate data centers or
colocation sites to cloud for true physical location redundancy. Use
dynamically routed, Active/Active connections across these sites to
enable automatic load balancing and failover.

**Desired outcome:** Ensure network
connectivity to cloud remains available even if one location
experiences an outage or disaster.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Eliminates single points of failure at the physical site level
- Enables business continuity and disaster recovery
- Supports high availability and compliance requirements
- Improves resilience to disasters or unplanned events

## Implementation guidance

- Deploy dedicated connections from at least two geographically
  distinct facilities.
- Use dynamic routing BGP for automatic failover.
- Test failover regularly to validate resiliency.

## Resources

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/ "https://aws.amazon.com/directconnect/resiliency-recommendation/")
