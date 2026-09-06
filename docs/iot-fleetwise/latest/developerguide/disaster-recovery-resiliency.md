

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Resilience in AWS IoT FleetWise
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. Regions provide multiple physically separated and isolated Availability Zones, which are connected through low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

**Note**  
Data processed by AWS IoT FleetWise is stored in an Amazon Timestream database. Timestream supports backups to other AWS Availability Zones or Regions. However, you can write your own application using the Timestream SDK to query data and save it to the destination of your choice.   
For more information about Amazon Timestream, see the [* in the Amazon Timestream Developer Guide*](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html).  
Amazon Timestream is not available in the Asia Pacific (Mumbai) region.