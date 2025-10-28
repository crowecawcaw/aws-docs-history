# ADVPERF05-BP04 Provide dedicated network connection between your on-premises environment and AWS to offer high bandwidth and low latency

Use dedicated network connections to provide stable and high-speed
data communication between the on-premises data center and the AWS Cloud. This model is also applicable for connections between
multiple Regions, providing efficient and secure data
communication while effectively avoiding public network noise.

## Implementation guidance

For workloads that require high throughput or have strict
compliance requirements, consider implementing
[AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/"). AWS Direct Connect provides a dedicated
network connection between your on-premises environment and AWS,
offering high bandwidth, low latency, and enhanced security by
bypassing the public internet.

## Key AWS services

- [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/")

## Resources

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/ "https://aws.amazon.com/directconnect/resiliency-recommendation/")
- [Compliance
  validation for AWS Direct Connect](../../../directconnect/latest/UserGuide/DirectConnect-compliance.md "../../../directconnect/latest/UserGuide/DirectConnect-compliance.md")
- [Using
  the AWS Direct Connect Resiliency Toolkit to get started](../../../directconnect/latest/UserGuide/resiliency_toolkit.md "../../../directconnect/latest/UserGuide/resiliency_toolkit.md")
