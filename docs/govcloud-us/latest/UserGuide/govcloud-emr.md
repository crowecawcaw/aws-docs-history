# Amazon EMR in AWS GovCloud (US)

Amazon EMR is a cloud big data platform for running large-scale distributed data processing jobs, interactive SQL queries, and machine learning (ML) applications using open-source analytics frameworks such as Apache Spark, Apache Hive, and Presto.

For information related to Release history, refer to [Amazon EMR Release Information](../../../emr/latest/ReleaseGuide/emr-whatsnew-history.md "../../../emr/latest/ReleaseGuide/emr-whatsnew-history.md").

## How Amazon EMR differs for AWS GovCloud (US)

- MapR distributions are currently not supported.
- In AWS GovCloud (US) Regions, you launch all Amazon EMR job flows in Amazon Virtual Private Cloud (Amazon VPC). For information about configuring an Amazon VPC that can run a job flow, see [Set up a VPC to host clusters](../../../emr/latest/ManagementGuide/emr-vpc-host-job-flows.md "../../../emr/latest/ManagementGuide/emr-vpc-host-job-flows.md").
- Launching a job flow with debugging is not currently supported.
- Auto-termination for idle clusters using an auto-termination policy is not available.
- Shuffle-optimized disks in Amazon EMR Serverless are not available.
- Amazon EMR on EKS on Fargate is not available.
- Amazon EMR with AWS Lake Formation is not available.

## Documentation for Amazon EMR

[Amazon EMR documentation](https://aws.amazon.com/documentation/elastic-mapreduce/ "https://aws.amazon.com/documentation/elastic-mapreduce/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon EMR metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your job flows.
- Do not enter export-controlled data in Amazon EMR when doing the following:
  - Naming a job flow
  - Specifying a file location
  - Naming a bootstrap action
  - Providing arguments
  - Resource tags

- (Amazon EMR metadata and logs are not permitted to contain export-controlled data.) If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
