# HNSUS02-BP01 Prioritize critical components

Break down your workload into individual components (for example,
microservices, databases, and APIs). Use metrics like CPU
utilization, request rates, and business impact to classify them as
critical or non-critical.

**Desired outcome:** Resource
allocation aligned with business value, minimizing waste in
low-impact areas.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Focuses optimization efforts on high-impact components
- Reduces energy consumption
- Maintains performance for mission-critical workloads

## Implementation guidance

- Map component dependencies and usage. For example, you can
  achieve this using AWS X-Ray.
- Apply tags to categorize components (for example,
  business-critical, dev-test).
- Right-size your resources during off-peak hours. For example,
  you can achieve this using AWS Auto Scaling.

## Resources

- [AWS X-Ray: Service Map Analysis](../../../xray/latest/devguide/xray-concepts.md "../../../xray/latest/devguide/xray-concepts.md")
- [Best
  Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md")
- [AWS Auto Scaling - application scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
