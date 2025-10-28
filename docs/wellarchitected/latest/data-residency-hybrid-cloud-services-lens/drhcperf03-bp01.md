# DRHCPERF03-BP01 Engineer optimal traffic flow for the edge solution

Design network routing for data residency requirements.

**Desired outcome:** You use the
most optimal network path.

**Benefits of establishing this best
practice:** Optimal routing helps provide the best user
experience for applications while working within data residency
requirements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Within a multi-VPC configuration, use
[VPC
peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") over
[AWS Transit Gateway](../../../local-zones/latest/ug/local-zones-connectivity-transit-gateway-lzs.md "../../../local-zones/latest/ug/local-zones-connectivity-transit-gateway-lzs.md") to keep inter-VPC traffic within AWS Outposts and AWS Local Zones. For traffic that needs to leave
the Outposts and Local Zones, engineer network traffic flow to
align the network path to the desired performance profile. You
can identify latency to AWS Regions and Local Zones using a tool
like [AWS latency test](https://aws-latency-test.com/ "https://aws-latency-test.com/"). AWS Outposts rack customers should
[use
the local gateway path](../../../whitepapers/latest/aws-outposts-high-availability-design/applicationworkload-routing.md#recommended-practices-for-applicationworkload-routing "../../../whitepapers/latest/aws-outposts-high-availability-design/applicationworkload-routing.md#recommended-practices-for-applicationworkload-routing") instead of the service link path
where possible. AWS Outposts servers should use the
[local
network interface](../../../outposts/latest/server-userguide/local-network-interface.md "../../../outposts/latest/server-userguide/local-network-interface.md") instead of the service link path where
possible.
