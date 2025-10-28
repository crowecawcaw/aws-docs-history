# FSIPERF06: How do you make trade-offs in your architecture?

Financial services workloads often have to make trade-offs in their architecture to
meet their most important goals and KPIs, where performance of the system is deemed more
important than other factors, or vice-versa.

## FSIPERF06-BP01 Understand your priorities and architect to meet them

For example, a low-latency trading system needs to preserve the performance of the
system above all other factors, and be prepared to compromise on the cost of
infrastructure to meet their goals. In this situation it is still important not to
compromise on availability, and this may require significant investment in parallel,
independent, deployments for example an independent deployment of the application stack
in multiple AWS Availability Zones or Regions rather than a failover architecture.

Within the workload it may be necessary to trade-off between persistent capacity
and elasticity to make sure that the application always has the ability to handle peak
workloads without needing timed or reactive scaling up. Consider how much of your peak
workload you need to be able to service at any time.

When choosing services consider performance determinism. AWS serverless services
like AWS Lambda and AWS Fargate can bring significant performance benefits due to their
ability to scale elastically on demand, without intervention, but this is often coupled
with less fine control over the underlying environment, for example CPU clock speed, and
this can introduce an element of variability into workload performance. Where the
workload performance must be as consistent as possible, consider using Amazon EC2, where you
get the widest choice, and greatest level of control, over the production environment.
For example, using Amazon EC2 directly enables the use of [ENA Express](../../../AWSEC2/latest/UserGuide/ena-express.md "../../../AWSEC2/latest/UserGuide/ena-express.md"), to increase
network throughput and reduce latency, but brings restrictions on the Amazon EC2 instances
that support this feature.

Consider trade-offs in your application architecture. For example, to preserve
network latency you may choose to use certain services and configurations that are more
complex to implement and maintain, but offer better performance, such as using [VPC Peering instead of AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-and-considerations-to-migrate-from-vpc-peering-to-aws-transit-gateway/ "https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-and-considerations-to-migrate-from-vpc-peering-to-aws-transit-gateway/") to minimize the number of network hops for
your most critical traffic. For optimal connectivity to on-premises workloads consider
the best position for your AWS Direct Connect Gateway to bring it closest to the most
sensitive workloads.
