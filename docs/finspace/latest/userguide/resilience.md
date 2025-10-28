After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Resilience in Amazon FinSpace

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which
are connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that
automatically fail over between zones without interruption. Availability Zones are more
highly available, fault tolerant, and scalable than traditional single or multiple data
center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS global
infrastructure](http://aws.amazon.com/about-aws/global-infrastructure/ "http://aws.amazon.com/about-aws/global-infrastructure/").

While FinSpace is multi-AZ, it does not support backups to other AWS Availability Zones or
Regions. However, you can write your own application using the FinSpace SDK to query data and
save it to the destination of your choice.
