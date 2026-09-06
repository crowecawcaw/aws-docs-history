

# DRHCPERF03-BP01 Engineer optimal traffic flow for the edge solution
<a name="drhcperf03-bp01"></a>

 Design network routing for data residency requirements. 

 **Desired outcome:** You use the most optimal network path. 

 **Benefits of establishing this best practice:** Optimal routing helps provide the best user experience for applications while working within data residency requirements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-45"></a>

 Within a multi-VPC configuration, use [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) over [AWS Transit Gateway](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity-transit-gateway-lzs.html) to keep inter-VPC traffic within AWS Outposts and AWS Local Zones. For traffic that needs to leave the Outposts and Local Zones, engineer network traffic flow to align the network path to the desired performance profile. You can identify latency to AWS Regions and Local Zones using a tool like [AWS latency test](https://aws-latency-test.com/). AWS Outposts rack customers should [use the local gateway path](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/applicationworkload-routing.html#recommended-practices-for-applicationworkload-routing) instead of the service link path where possible. AWS Outposts servers should use the [local network interface](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) instead of the service link path where possible. 