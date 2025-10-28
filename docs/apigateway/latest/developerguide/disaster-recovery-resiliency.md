# Resilience in Amazon API Gateway

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide
multiple physically separated and isolated Availability Zones, which are connected with low-latency,
high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications
and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

As a fully
managed Regional service, API Gateway operates in multiple Availability Zones in each Region, using the
redundancy of Availability Zones to minimize infrastructure failure as a category of availability risk. API Gateway is
designed to automatically recover from the failure of an Availability Zone.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

To prevent your APIs from being overwhelmed by too many requests, API Gateway throttles requests
to your APIs. Specifically, API Gateway sets a limit on a steady-state rate and a burst of request
submissions against all APIs in your account. You can configure custom throttling for your
APIs. To learn more, see [Throttle requests to your REST APIs for better throughput in API Gateway](api-gateway-request-throttling.md "api-gateway-request-throttling.md").

You can use Route 53 health checks to control DNS failover from an API Gateway API in a primary region to an API Gateway API in a secondary region. For an example, see [Configure custom health checks for DNS failover for an API Gateway API](dns-failover.md "dns-failover.md").
