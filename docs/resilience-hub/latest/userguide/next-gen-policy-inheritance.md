

# Policy inheritance and multi-level evaluation
<a name="next-gen-policy-inheritance"></a>

A service is evaluated against **all policies that apply to it**:
+ Its directly assigned policy (if any).
+ Policies inherited from user journeys it belongs to.

This enables separation of concerns:
+ Central SRE teams set DR policies at the user journey level for governance.
+ Service teams set performance policies at the service level for operational requirements.
+ Both policies apply simultaneously to services in the user journey.

For example:

```
User Journey: "Path to Trade"
  Policy: "Trading Platform DR Policy" (Multi-Region, RTO 15 min, RPO 5 min)
  └── Service: "Order Execution"
        Policy: "Order Execution Performance Policy" (Availability 99.99%, Error < 0.1%, p99 < 50ms)
```

The "Order Execution" service is evaluated against **both** policies. It must meet the DR requirements from the user journey policy and the performance requirements from its service-specific policy.

**Conflict resolution**

When multiple policies contain conflicting requirements for the same component, Next generation Resilience Hub automatically applies the **stricter value**. The following example shows how conflicting RTO values are resolved:


| Source | Component | Value | 
| --- | --- | --- | 
| User journey policy | RTO | 30 minutes | 
| Service policy | RTO | 15 minutes | 
| Applied value | RTO | 15 minutes (stricter) | 