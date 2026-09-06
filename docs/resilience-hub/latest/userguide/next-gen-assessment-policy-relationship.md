

# Relationship to resilience policies
<a name="next-gen-assessment-policy-relationship"></a>

Failure mode assessments evaluate your application against the targets defined in your resilience policies. Each finding maps to specific policy requirements, showing you exactly which resilience targets are at risk. For example:

```
Finding: "RDS database is not configured for Multi-AZ"
  -> Policy requirement: Multi-Region DR (RTO 15 min)
  -> Impact: Regional failover would require manual database restoration,
     exceeding the 15-minute RTO target

Finding: "No health check configured on ALB target group"
  -> Policy requirement: Availability SLO (99.99%)
  -> Impact: Unhealthy instances continue receiving traffic,
     degrading availability below target
```