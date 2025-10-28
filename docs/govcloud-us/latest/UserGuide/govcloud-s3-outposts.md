# Amazon S3 on Outposts in AWS GovCloud (US)

Amazon S3 on Outposts delivers object storage to your on-premises AWS Outposts environment
to help you meet your low latency, local data processing, and data residency needs. Using
the Amazon S3 APIs and features, Amazon S3 on Outposts makes it easier to store, secure, tag,
retrieve, report on, and control access to the data on your Outposts. AWS Outposts is a
fully managed service that extends AWS infrastructure, services, and tools to virtually
any data center, co-location space, or on-premises facility for a truly consistent hybrid
experience.

## How Amazon S3 on Outposts differs for

AWS GovCloud (US)

AWS CloudFormation is not supported.

## Documentation for Amazon S3 on Outposts

[S3 on Outposts documentation](../../../AmazonS3/latest/userguide/S3onOutposts.md "../../../AmazonS3/latest/userguide/S3onOutposts.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon S3 on Outposts metadata is not permitted to contain export-controlled data.
  This metadata includes all configuration data that you enter when creating and
  maintaining your Amazon S3 on Outposts buckets, such as bucket names. For example, do
  not enter export-controlled data in the following fields:
  - Outpost Bucket Name
  - Outpost Object Name
  - Resource tags
