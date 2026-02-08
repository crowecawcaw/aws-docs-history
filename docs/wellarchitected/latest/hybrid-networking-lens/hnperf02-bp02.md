# HNPERF02-BP02 Choose the right physical PoP location for

dedicated connectivity

Points of Presence (PoPs) serve as strategic interconnection
locations between on-premises and cloud environments. These physical
connection points are distributed across various geographic
locations to enable low-latency private network connectivity.
Organizations should understand how PoP locations impact network
performance, as the distance between your infrastructure and these
interconnection points directly affects latency and overall
application performance. For mission-critical applications requiring
consistent, high-performance connectivity, leveraging multiple PoPs
can provide both reduced latency and enhanced reliability

**Desired outcome:**

- Select appropriate termination endpoints that align with current
  and future network requirements
- Balance performance needs with cost considerations
- Maintain network isolation while enabling necessary connectivity
- Support scalable network growth without major architectural
  changes

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Delivers substantial operational performance advantages for
  hybrid architectures.
- Achieve consistently low network latency, which is crucial for
  latency-sensitive applications and real-time data processing.

## Implementation guidance

- Assessment of workload requirements and geographical
  distribution of resources.
- Select dedicated connection locations that minimize the
  physical distance to your on-premises infrastructure while
  ensuring adequate port capacity is available.
- Connect to cloud network through preferred PoP.
- Consider latency you get when choosing dedicated connection as
  your hybrid connectivity option is dependent on two factors –
  the distance between your data center and the dedicated
  connection location.

## Resources

- [AWS direct connect locations](https://aws.amazon.com/directconnect/locations/ "https://aws.amazon.com/directconnect/locations/")
- [Point
  of presence](../../../whitepapers/latest/aws-fault-isolation-boundaries/points-of-presence.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/points-of-presence.md")
