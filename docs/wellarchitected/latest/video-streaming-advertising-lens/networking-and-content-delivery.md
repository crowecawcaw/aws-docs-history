# Networking and content delivery

The optimal networking solution for a workload varies based on
latency, throughput requirements, jitter, and bandwidth. Physical
constraints, such as user or on-premises resources,
determine location options. These constraints can be offset with
edge locations or resource placement. 

On AWS, networking is virtualized and is available in a number of
different types and configurations. This makes it easier to match
your networking needs. AWS offers product features (for example,
Enhanced Networking, Amazon EC2 networking optimized instances,
Amazon S3 transfer acceleration, and dynamic Amazon CloudFront) to
optimize network traffic.

AWS also offers networking features (for example, Amazon Route 53
latency routing, Amazon VPC endpoints, AWS Direct Connect, and AWS
Global Accelerator) to reduce network jitter.

This focus area shares guidance and best practices to design,
configure, and operate efficient
networking and content delivery solutions in the cloud.

| ADVPERF05: How do you build network architecture to provide efficient performance and improved user experience for your advertising workload? |
| --------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                               |

By using the various networking services provided by AWS, you
can build a high- performance, low-latency, and highly available
network architecture. For advertising workloads, a robust
network architecture is particularly important, as all ad
requests rely on a stable network to function properly.

Building a robust and efficient network architecture is crucial
for delivering optimal performance and an exceptional user
experience for advertising workloads on AWS.

Implementing best practices such as network segmentation,
monitoring, automatic scaling, and load balancing further
contributes to efficient performance and improved user
experience.

Regularly review and optimize your network
configuration, implement disaster recovery plans, and use
content delivery networks like Amazon CloudFront to provide reliable advertising servies to your customers.

###### Best practices

- [ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance](advperf05-bp01.md "advperf05-bp01.md")
- [ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration to reduce latency and improve user experience](advperf05-bp02.md "advperf05-bp02.md")
- [ADVPERF05-BP03 Use load balancers to improve high availability and load distribution in your workload](advperf05-bp03.md "advperf05-bp03.md")
- [ADVPERF05-BP04 Provide dedicated network connection between your on-premises environment and AWS to offer high bandwidth and low latency](advperf05-bp04.md "advperf05-bp04.md")
