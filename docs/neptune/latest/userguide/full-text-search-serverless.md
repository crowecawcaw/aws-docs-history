# Replication to OpenSearch Serverless

Starting with [engine release 1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md"),
Amazon Neptune supports using [Amazon OpenSearch Service Serverless](../../../opensearch-service/latest/developerguide/serverless.md "../../../opensearch-service/latest/developerguide/serverless.md")
for full-text search in Gremlin and SPARQL queries. Using OpenSearch Serverless requires you to
[enable IAM authentication](iam-auth-enable.md "iam-auth-enable.md")
on your Neptune Database cluster. Neptune Database clusters with IAM authentication
disabled are not supported with OpenSearch Serverless.

## Changes required for poller AWS Lambda function

If you are replicating to OpenSearch Serverless, add the Lambda stream poller execution
role to the data access policy for the OpenSearch Serverless collection. The ARN for the
Lambda stream poller execution role has this format:

```
arn:aws:iam::`(account ID)`:role/stack-name-NeptuneOSReplication-NeptuneStreamPollerExecu-`(uuid)`
```

## Changes required for bulk import utility

If you are using [export-neptune-to-elasticsearch](https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch "https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch") to synchronize existing data to OpenSearch Serverless, add the
`LambdaExecutionRole` from the CloudFormation stack to the data access policy for the OpenSearch Serverless
collection. The ARN for the `LambdaExecutionRole` has this format:

```
arn:aws:iam::`012345678901`:role/stack-name-LambdaExecutionRole-`(id)`
```

For more information, see [Data
access control for Amazon OpenSearch Serverless](../../../opensearch-service/latest/developerguide/serverless-data-access.md "../../../opensearch-service/latest/developerguide/serverless-data-access.md").

## Changes needed to the IAM role used to query Neptune

The IAM entity (User or Role) used for connecting to the Neptune database
should have permissions both for Neptune and the OpenSearch Serverless collection.
This means that your user or role must have an OpenSearch Serverless policy like
this attached:

See [Creating custom IAM policy statements to access data in Amazon Neptune](iam-data-access-policies.md "iam-data-access-policies.md")
for more information.
