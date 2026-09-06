

# AWS Outposts in AWS GovCloud (US)
<a name="govcloud-outposts"></a>

AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. By providing local access to AWS managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs. Both AWS Outposts racks and servers are available in the AWS GovCloud (US) Region.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Outposts differs
<a name="govcloud-op-diffs"></a>

The following differences apply to AWS Outposts:
+  Application Load Balancer is not available.
+  Amazon RDS is not available.
+  Amazon EMR is not available.
+  ElastiCache is not available.
+  Route 53 resolver is not available.
+ Launching Amazon EC2 instances that use Local Boot with an encrypted AMI is not supported. As a workaround, use an unencrypted boot AMI.

## Documentation
<a name="govcloud-op-docs"></a>

 [AWS Outposts documentation](https://docs.aws.amazon.com/outposts/?id=docs_gateway).

## Export-controlled content
<a name="govcloud-op-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ AWS Outposts metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when setting up and maintaining your topics.

  For example, do not enter export-controlled data in the following fields:
  + Outpost Name
  + Outpost Description
  + Site Address
  + Site Name
  + Site Description
  + Site Notes