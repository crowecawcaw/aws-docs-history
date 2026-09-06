

# Amazon S3 on Outposts in AWS GovCloud (US)
<a name="govcloud-s3-outposts"></a>

Amazon S3 on Outposts delivers object storage to your on-premises AWS Outposts environment to help you meet your low latency, local data processing, and data residency needs. Using the Amazon S3 APIs and features, Amazon S3 on Outposts makes it easier to store, secure, tag, retrieve, report on, and control access to the data on your Outposts. AWS Outposts is a fully managed service that extends AWS infrastructure, services, and tools to virtually any data center, co-location space, or on-premises facility for a truly consistent hybrid experience.

## Region availability
<a name="region-availability"></a>

 Amazon S3 on Outposts is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-East) 
+  AWS GovCloud (US-West) 

## How Amazon S3 on Outposts differs
<a name="feature-diffs"></a>
+  AWS CloudFormation is not available.

## Documentation
<a name="documentation"></a>
+  [S3 on Outposts documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) 

## Export-controlled content
<a name="itar-boundary"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon S3 on Outposts metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your Amazon S3 on Outposts buckets, such as bucket names. For example, do not enter export-controlled data in the following fields:
  + Outpost Bucket Name
  + Outpost Object Name
  + Resource tags