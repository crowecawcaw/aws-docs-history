

# Reliability
<a name="reliability-rise"></a>

Reliability is one of the six pillars of SAP Lens - AWS Well-Architected Framework. For more information, see [Reliability](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/reliability.html).

 AWS cloud offers reliability with multiple Availability Zones within an AWS Region. This enables your SAP applications on AWS to be more resilient. Each Region is further isolated from other Regions, providing the greatest possible fault tolerance and stability. Within each AWS Region, there are a minimum of three, isolated, physically separate Availability Zones. For more information, see [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).

![Diagram that shows the fault tolerance of Regions and Availability Zones.](http://docs.aws.amazon.com/sap/latest/general/images/rise-aws-global-infra.png)


Availability Zones enable you to operate production applications and databases that are more highly available than would be possible from a single data center. Distributing your applications across multiple Availability Zones provides the ability to remain resilient in the face of most failure modes, including natural disasters or system failures.

Each Availability Zone can be multiple data centers. At full scale, it can contain hundreds of thousands of servers. They are fully isolated partitions of AWS Global Infrastructure. An Availability Zone is physically separated from any other zones with its own separate power and networking resources. There is a distance of several kilometers, although all are within 100 km (60 miles) of each other. This distance provides isolation from the most common disasters that could affect data centers, such as floods, fire, severe storms, earthquakes, etc.

All Availability Zones within a Region are interconnected with high-bandwidth and low-latency networking, over fully redundant and dedicated metro fiber. This ensures high-throughput, low-latency networking between Availability Zones. The network performance is sufficient to accomplish synchronous replication.

![Network design diagram for Availability Zones.](http://docs.aws.amazon.com/sap/latest/general/images/rise-aws-network-design.png)


Availability Zones enable you to run your applications in a highly-available manner, with synchronous data replication and automated failover between Availability Zones. RISE with SAP can offer such high available designs for your workload in every AWS Region.