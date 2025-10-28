# Managing data consistency in CloudTrail

CloudTrail uses a distributed computing model called [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency "https://en.wikipedia.org/wiki/Eventual_consistency").
Any change that you make to your CloudTrail configuration (or other AWS services), including tags used in [attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"), takes time to become visible from all
possible endpoints. Some of the delay results from the time it takes to send the data from
server to server, and from Region to Region
around the world. CloudTrail also uses caching to improve performance, but in some cases this can
add time. The change might not be visible until the previously cached data times out.

You must design your applications to account for these potential delays. Ensure that they work
as expected, even when a change made in one location is not instantly visible at another. Such changes
include [enabling an opt-in Region](cloudtrail-multi-region-trails.md#cloudtrail-multi-region-trails-optin "cloudtrail-multi-region-trails.md#cloudtrail-multi-region-trails-optin"), creating or updating trails or event data stores, updating event selectors, and
starting or stopping logging. When you create or update a trail or event data store, CloudTrail delivers logs to the S3 bucket
or event data store based on the last known configuration until the changes propagate to all locations.

For more information about how this affects other AWS services, see the following resources:

- **Amazon DynamoDB**: [What is the consistency model of DynamoDB?](https://aws.amazon.com/dynamodb/faqs/ "https://aws.amazon.com/dynamodb/faqs/") in the _DynamoDB FAQ_,
  and [Read consistency](../../../amazondynamodb/latest/developerguide/HowItWorks.md "../../../amazondynamodb/latest/developerguide/HowItWorks.md") in the _Amazon DynamoDB Developer Guide_.
- **Amazon EC2**: [Eventual consistency](../../../AWSEC2/latest/APIReference/query-api-troubleshooting.md#eventual-consistency "../../../AWSEC2/latest/APIReference/query-api-troubleshooting.md#eventual-consistency")
  in the _Amazon Elastic Compute Cloud API Reference_.
- **Amazon EMR**: [Ensuring Consistency When Using Amazon S3 and Amazon Elastic MapReduce for ETL Workflows](https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/ "https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/")
  in the _AWS Big Data Blog_.
- **AWS Identity and Access Management (IAM)**: [Changes that I make are not always immediately visible](../../../IAM/latest/UserGuide/troubleshoot_general.md#troubleshoot_general_eventual-consistency "../../../IAM/latest/UserGuide/troubleshoot_general.md#troubleshoot_general_eventual-consistency") in the
  _IAM User Guide_.
- **Amazon Redshift**: [Managing data consistency](../../../redshift/latest/dg/managing-data-consistency.md "../../../redshift/latest/dg/managing-data-consistency.md")
  in the _Amazon Redshift Database Developer Guide_.
- **Amazon S3**: [Amazon S3 data consistency model](../../../AmazonS3/latest/userguide/Welcome.md#ConsistencyModel "../../../AmazonS3/latest/userguide/Welcome.md#ConsistencyModel")
  in the _Amazon Simple Storage Service User Guide_.
