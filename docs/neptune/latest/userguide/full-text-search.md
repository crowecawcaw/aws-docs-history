# Full text search in Amazon Neptune using Amazon OpenSearch Service

Neptune integrates with [Amazon OpenSearch Service (OpenSearch Service)](../../../opensearch-service/latest/developerguide.md "../../../opensearch-service/latest/developerguide.md") to
support full-text search in both Gremlin and SPARQL queries. This feature is available
starting in [Neptune engine release 1.0.2.1](engine-releases-1.0.2.md "engine-releases-1.0.2.md"),
although we recommend using it with engine release `1.0.4.2` or higher to take
advantage of the latest fixes.

Starting with [engine release 1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md"),
Amazon Neptune supports using [Amazon OpenSearch Service Serverless](../../../opensearch-service/latest/developerguide/serverless.md "../../../opensearch-service/latest/developerguide/serverless.md")
for full-text search in Gremlin and SPARQL queries.

###### Note

When integrating with Amazon OpenSearch Service, Neptune requires Elasticsearch version
7.1 or higher, and works with OpenSearch 2.3, 2.5 and above. Neptune also works
with [OpenSearch Serverless](full-text-search-serverless.md "full-text-search-serverless.md").

You can use Neptune with an existing OpenSearch Service cluster that has been populated
according to the [Neptune data model for OpenSearch data](full-text-search-model.md "full-text-search-model.md"). Or, you can create an OpenSearch Service domain linked with Neptune using an AWS CloudFormation stack.

###### Important

The Neptune to OpenSearch replication process described here does
not replicate blank nodes. This is an important limitation to note.

Also, if you enable [fine-grained access
control](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md") on your OpenSearch cluster, you need to [enable
IAM authentication](iam-auth-enable.md "iam-auth-enable.md") in your Neptune database as well.

![Neptune open search stream poller architecture layout.](images/poller-architecture.PNG)

###### Topics

- [Amazon Neptune-to-OpenSearch replication](full-text-search-cfn-setup.md "full-text-search-cfn-setup.md")
- [Replication to OpenSearch Serverless](full-text-search-serverless.md "full-text-search-serverless.md")
- [Querying from an OpenSearch cluster with Fine-grained access control (FGAC) enabled](full-text-search-fgac.md "full-text-search-fgac.md")
- [Using Apache Lucene query syntax in Neptune full-text search queries](full-text-search-lucene.md "full-text-search-lucene.md")
- [Neptune data model for OpenSearch data](full-text-search-model.md "full-text-search-model.md")
- [Neptune full-text search parameters](full-text-search-parameters.md "full-text-search-parameters.md")
- [Non-string OpenSearch indexing in Amazon Neptune](full-text-search-non-string-indexing.md "full-text-search-non-string-indexing.md")
- [Full-text-search query execution
  in Amazon Neptune](full-text-search-query-execution.md "full-text-search-query-execution.md")
- [Sample SPARQL queries using full-text search in Neptune](full-text-search-sparql-examples.md "full-text-search-sparql-examples.md")
- [Using Neptune full-text search in Gremlin queries](full-text-search-gremlin.md "full-text-search-gremlin.md")
- [Troubleshooting Neptune full-text search](streams-consumer-troubleshooting.md "streams-consumer-troubleshooting.md")
