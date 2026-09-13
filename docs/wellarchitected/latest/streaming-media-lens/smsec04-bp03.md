

# SMSEC04-BP03 Use private connectivity when working with partners
<a name="smsec04-bp03"></a>

Using private connectivity from your location or other datacenters can help avoid transmission of data across unknown or unprotected networks, and allows content to be delivered directly to AWS.

**Desired outcome:**
+ Content delivered over Direct Connect or AWS PrivateLink is sent without traveling across open networks, and can be ingested to your workflow directly

**Common anti-patterns:**
+ Organizations transmit high-value source content and live contribution feeds to partner facilities over the public internet without dedicated private connectivity, exposing content to interception across multiple network hops.
+ Teams use VPN tunnels over public internet as a permanent solution for partner content exchange rather than establishing dedicated private connections, accepting the performance variability and shared infrastructure risks of public routing.
+ Organizations fail to implement network ACLs and routing restrictions on private connectivity endpoints, allowing any resource within the partner VPC to access the connection rather than limiting to specific authorized services.
+ Teams establish Direct Connect links without redundancy, creating a single point of failure that forces fallback to public internet paths during maintenance or outages.

**Benefits of establishing this best practice:**
+ Content traverses dedicated private connections rather than shared public internet paths, removing exposure to interception, packet sniffing, or man-in-the-middle attacks during partner content exchange.
+ Private connectivity provides predictable bandwidth and latency for high-bit rate contribution feeds, avoiding the congestion and variability of public internet routing.
+ Direct Connect and PrivateLink minimize the number of network hops and autonomous systems that content traverses, reducing the parties with physical access to the transmission layer.
+ PrivateLink endpoints enforce unidirectional traffic flow, so partner services can only receive requests from authorized consumer resources without gaining broader network access.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

You can use Direct Connect and Direct Connect Gateway to connect your network to an AWS Region and bypass public network paths between content source and cloud infrastructure. With Direct Connect, you establish a dedicated connection between a provider network and one of the Direct Connect locations. Established connections from an Direct Connect location to any other AWS Region around the world communicate over the AWS managed backbone, improving performance for geo-diverse media workloads while limiting the routers, networks, and parties involved in the physical transmission layer.

AWS PrivateLink is recommended to establish connectivity when working with partners that also use AWS. With AWS PrivateLink, a service provider can expose their service endpoint to you within Region, avoiding communication over the public networks. When a service provider provisions a PrivateLink endpoint in the consumer's VPC, traffic can never initiate from that endpoint, and only receive requests from the consumer's resources. Traffic flowing through the AWS PrivateLink VPC endpoint will adhere to routing rules and network access control lists placed on that subnet in which the endpoint resides.

### Implementation steps
<a name="implementation-steps"></a>

1. **Set up Direct Connect:** Consider setting up [Direct Connect](https://aws.amazon.com/directconnect/) within your network or with your provider.

1. **Use AWS PrivateLink:** Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to transmit traffic between VPCs and AWS services without exposing data to the internet.

1. **Configure routing and access controls:** Configure VPC routing tables and network access control lists (ACLs) to restrict traffic flow through private connectivity endpoints.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC04-BP02 Encrypt content ingest traffic using TLS](smsec04-bp02.html)

**Related documents**
+ [Getting Started with Direct Connect](https://aws.amazon.com/directconnect/getting-started/?pg=ln&sec=hs)
+ [AWS PrivateLink](https://aws.amazon.com/privatelink/)

**Related services**
+ [Direct Connect](https://aws.amazon.com/directconnect/)
+ [AWS VPC](https://aws.amazon.com/vpc/)
+ [AWS PrivateLink](https://aws.amazon.com/privatelink/)