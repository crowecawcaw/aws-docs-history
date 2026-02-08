# HNPERF01-BP01 Determine and define your performance

requirements using bandwidth, latency and jitter values.

Before you design the best performing architecture, define what
performance means for you and the parameters involved. Typically,
performance metrics are based around bandwidth (rate of data
transfer), latency (round trip time for a network packet to travel
form source to destination), and jitter (variation in latency).
Start by estimating the bandwidth and latency requirements of your
hybrid networking applications.  Match these estimates with the
options available from cloud providers such as dedicated connection
vs internet-based connection to determine which technology you
should choose, and the appropriate configuration.

**Desired outcome:**

- Establish clear, quantifiable performance requirements that
  guide the selection of hybrid networking services.
- Provide seamless user experiences and efficient data transfer
  between on-premises and cloud environments.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Make informed decisions about networking technology selection
  and ensure appropriate resource allocation.
- Improve application performance, enhanced user experience, and
  more efficient use of networking resources.

## Implementation guidance

- Consider leverage existing monitoring systems to gather
  detailed performance data and engage stakeholders to define
  performance expectations.
- Consider both average and peak performance needs
- Document specific bandwidth, latency, and jitter requirements
  for each workload and map these requirements to available
  cloud networking options.

## Resources

- [Example
  Corp. Automotive use case](../../../whitepapers/latest/hybrid-connectivity/example-corp.md "../../../whitepapers/latest/hybrid-connectivity/example-corp.md")
- [Network
  to Amazon VPC Connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md")
