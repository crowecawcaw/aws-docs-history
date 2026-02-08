# HNPERF02-BP01 Use tradeoffs to improve network

performance

When deciding on which technology to choose (VPN vs dedicated
circuits) or which termination endpoint to choose, Consider how
performance, cost, and deployment effort compare across your
options. Understanding the tradeoffs will help you choose the right
tool for the right job. To avoid a one-size-fits-all solution in
your workload, use trade-offs to achieve the peak performance based
on your business and technical requirements.

**Desired outcome:**

- Well-balanced hybrid network architecture that effectively meets
  specific business requirements while optimizing cost,
  performance, and operational efficiency.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Optimized costs and improved performance
- Faster deployment where needed while ensuring high performance
  for critical workloads

## Implementation guidance

- Evaluate workload requirements including bandwidth needs,
  latency sensitivity, setup time constraints, and budget
  limitations.
- For rapid network connectivity needs, consider service like
  AWS Site-to-Site VPN solutions that can be quickly deployed.
- For critical workloads requiring high-performance networking
  with consistent low latency, such as real-time transactions or
  large-scale data processing, consider dedicated connection
  solutions such as AWS Direct Connect that provides reliability
  and speed.
- Monitor to validate that chosen solutions meet performance and
  cost objectives.

## Resources

- [Connect
  your VPC to remote networks using AWS Virtual Private Network](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md")
- [Network
  to Amazon VPC Connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md")
