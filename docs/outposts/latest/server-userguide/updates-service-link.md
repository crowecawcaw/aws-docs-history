# Updates and the service link

AWS maintains a secure network connection between your Outposts server and its parent AWS
Region. This network connection, called the service link, is essential in managing the Outpost
by providing intra-VPC traffic between the Outpost and AWS Region. [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") best practices recommend
deploying applications across two Outposts parented to different Availability Zones with an
active-active design. For more information, see [AWS Outposts High Availability Design and Architecture Considerations](../../../whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.md "../../../whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.md").

The service link is regularly updated to maintain operational quality and performance.
During maintenance, you might observe brief periods of latency and packet loss on this network
resulting in impact on workloads that are dependent on VPC connectivity to resources hosted
in-region. However, traffic traversing the [Local Network Interfaces
(LNI)](local-network-interface.md "local-network-interface.md") will not be impacted. You can avoid impact to your application by following
[AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/")
best practices and by ensuring your applications are [resilient to
failures](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md") or maintenance activities affecting a single Outposts server.
