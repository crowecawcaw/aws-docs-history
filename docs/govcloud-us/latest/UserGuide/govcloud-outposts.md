# AWS Outposts in AWS GovCloud (US)

AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. By providing local access to AWS managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs. Both AWS Outposts racks and servers are available in the AWS GovCloud (US) Region.

## How AWS Outposts differs for AWS GovCloud (US)

- Application Load Balancer is not supported.
- Amazon RDS is not supported.
- Amazon EMR is not supported.
- ElastiCache is not supported.
- Route 53 resolver is not supported.

## Documentation for AWS Outposts

[AWS Outposts documentation](../../../outposts.md "../../../outposts.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS Outposts metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when setting up and maintaining your topics.

For example, do not enter export-controlled data in the following fields:

    + Outpost Name
    + Outpost Description
    + Site Address
    + Site Name
    + Site Description
    + Site Notes
