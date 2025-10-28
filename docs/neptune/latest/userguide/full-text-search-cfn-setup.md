# Amazon Neptune-to-OpenSearch replication

Amazon Neptune supports full-text search in Gremlin and SPARQL queries using Amazon OpenSearch Service (OpenSearch Service).
You can use an AWS CloudFormation stack to link an OpenSearch Service domain to Neptune. The AWS CloudFormation template
creates a streams-consumer application instance that provides Neptune-to-OpenSearch
replication.

Before you begin, you need an existing Neptune DB cluster with streams enabled
on it to serve as the source, and an OpenSearch Service domain to serve as the replication target.

If you already have an existing target OpenSearch Service domain that can be accessed by
Lambda in the VPC where your Neptune DB cluster is located, the template can use that one.
Otherwise, you need to create a new one.

###### Note

The OpenSearch cluster and Lambda function that you create must be located
in the same VPC as your Neptune DB cluster, and the OpenSearch cluster must be
configured in VPC mode (not Internet mode).

We recommend that you use a newly created Neptune instance to use with OpenSearch Service.
If you use an existing instance that already has data in it, you should perform an
OpenSearch Service data sync before making queries or there may be data inconsistencies.
This GitHub project provides an example of how to perform the synchronization: [Export
Neptune to OpenSearch](https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch "https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch") (https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch).

###### Important

When integrating with Amazon OpenSearch Service, Neptune requires Elasticsearch
version 7.1 or higher, and works with OpenSearch 2.3, 2.5 and future compatible
Opensearch versions.

###### Note

Starting with [engine release 1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md"),
Amazon Neptune supports using [Amazon OpenSearch Service Serverless](../../../opensearch-service/latest/developerguide/serverless.md "../../../opensearch-service/latest/developerguide/serverless.md")
for full-text search in Gremlin and SPARQL queries.

###### Topics

- [Using an AWS CloudFormation template to start Neptune-to-OpenSearch replication](full-text-search-cfn-create.md "full-text-search-cfn-create.md")
- [Enabling full text search on existing Neptune databases](full-text-search-cfn-enabling.md "full-text-search-cfn-enabling.md")
- [Updating the stream poller](full-text-search-cfn-update-poller.md "full-text-search-cfn-update-poller.md")
- [Disabling and re-enabling the stream poller process](full-text-search-using-pausing-poller.md "full-text-search-using-pausing-poller.md")
