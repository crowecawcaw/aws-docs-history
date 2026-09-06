

# Amazon Elastic Container Service (Amazon ECS) in AWS GovCloud (US)
<a name="govcloud-ecs"></a>

Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster of Amazon EC2 instances.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Elastic Container Service differs
<a name="govcloud-ecs-diffs"></a>

The following differences apply to Amazon Elastic Container Service:
+ The Amazon ECS-optimized AMI variant of the Bottlerocket operating system is not available when launching Amazon ECS container instances.

## Documentation
<a name="govcloud-ecs-docs"></a>
+  [Amazon Elastic Container Service documentation](https://docs.aws.amazon.com/documentation/ecs/) 

## Export-controlled content
<a name="ecs-itar-boundary"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Do not enter export-controlled data in the following fields:
  + Cluster name
  + Service name
  + Attribute name
  + Attribute value
  + Task definitions
  + Task group
  + Task overrides
  + Task started by
  + Placement constraints