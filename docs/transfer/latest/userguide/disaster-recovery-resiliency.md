# Resilience in AWS Transfer Family

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which
are connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between Availability Zones without interruption. Availability Zones are more
highly available, fault tolerant, and scalable than traditional single or multiple data
center infrastructures.

AWS Transfer Family supports up to 3 Availability Zones and is backed by an auto scaling, redundant
fleet for your connection and transfer requests.

For all Transfer Family endpoints:

- Availability Zone-level redundancy is built into the service.
- There are redundant fleets for each AZ.
- This redundancy is provided automatically.

###### Note

For endpoints in a Virtual Private Cloud (VPC), it is possible to provide a single
subnet. However, we recommend that you create endpoints in multiple availability zones
within your VPC, to reduce the risk of service disruptions during Availability Zone
outages.

See also

- For details on how to create Transfer Family servers in a VPC, see [Create a server in a virtual private cloud](create-server-in-vpc.md "create-server-in-vpc.md").
- For more information about AWS Regions and Availability Zones, see [AWS global
  infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").
- For an example on how to build for higher
  redundancy and minimize network latency by using Latency-based routing, see the blog post
  [Minimize
  network latency with your AWS Transfer Family servers](https://aws.amazon.com/blogs/storage/minimize-network-latency-with-your-aws-transfer-for-sftp-servers/ "https://aws.amazon.com/blogs/storage/minimize-network-latency-with-your-aws-transfer-for-sftp-servers/").
