# Amazon ECS in AWS GovCloud (US)

Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster of Amazon EC2 instances.

## How Amazon Elastic Container Service differs for AWS GovCloud (US)

- The Amazon ECS-optimized AMI variant of the Bottlerocket operating system is not available when launching Amazon ECS container instances.
- Attaching Amazon EBS volumes to Amazon ECS tasks is not supported.

## Documentation for Amazon Elastic Container Service

[Amazon Elastic Container Service documentation](https://aws.amazon.com/documentation/ecs/ "https://aws.amazon.com/documentation/ecs/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Do not enter export-controlled data in the following fields:
  - Cluster name
  - Service name
  - Attribute name
  - Attribute value
  - Task definitions
  - Task group
  - Task overrides
  - Task started by
  - Placement constraints
