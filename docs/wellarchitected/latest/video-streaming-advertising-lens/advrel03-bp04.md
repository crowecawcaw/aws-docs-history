# ADVREL03-BP04 Reserve appropriate capacity of services in the supported Regions

Manage service capacity across multiple Regions. Perform regular
load testing at five times your baseline RTB traffic levels to
validate capacity requirements. Validate that appropriate
reservations are made to handle normal operations, peak loads, and
potential disruptions.

## Implementation guidance

If your application is designed to scale out over multiple
Regions, service could be disrupted by temporary resource
constraints or other issues impacting a single Availability Zone
or Region. Regularly perform load tests with at least five times
the baseline of RTB traffic expectations to validate that
allocated capacity meets low water mark, mean, and peak capacity
projections. Based on the results of your load tests, make
capacity reservation.

## Key AWS services

- [Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/")
- [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")

## Resources

- [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
- [Quotas
  and constraints for Amazon RDS](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")
- [What
  to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/ "https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/")
- [Creating
  a Multi-Region Application with AWS Services – Part 1, Compute, Networking, and Security](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-1-compute-and-security/index.html "https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-1-compute-and-security/index.html")
