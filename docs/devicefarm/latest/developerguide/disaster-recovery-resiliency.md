# Resilience in AWS Device Farm

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide
multiple physically separated and isolated Availability Zones, which are connected with low-latency,
high-throughput, and highly redundant networking. With Availability Zones, you can design and operate
applications and databases that automatically fail over between zones without interruption. Availability Zones
are more highly available, fault tolerant, and scalable than traditional single or multiple data center
infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

Because Device Farm is available in the `us-west-2` Region only, we strongly recommend that you implement
backup and recovery processes. Device Farm should not be the only source of any uploaded content.

Device Farm makes no guarantees of the availability of public devices. These devices are taken in and out of the
public device pool depending on a variety of factors, such as failure rate and quarantine status. We do not
recommend that you depend on the availability of any one device in the public device pool.
