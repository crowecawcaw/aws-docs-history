

# Replication to OpenSearch Serverless
<a name="full-text-search-serverless"></a>

Starting with [engine release 1.3.0.0](engine-releases-1.3.0.0.md), Amazon Neptune supports using [Amazon OpenSearch Service Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html) for full-text search in Gremlin and SPARQL queries. Using OpenSearch Serverless requires you to [enable IAM authentication](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-enable.html) on your Neptune Database cluster. Neptune Database clusters with IAM authentication disabled are not supported with OpenSearch Serverless.

## Changes required for poller AWS Lambda function
<a name="full-text-changes-required"></a>

If you are replicating to OpenSearch Serverless, add the Lambda stream poller execution role to the data access policy for the OpenSearch Serverless collection. The ARN for the Lambda stream poller execution role has this format:

```
arn:aws:iam::{{(account ID)}}:role/stack-name-NeptuneOSReplication-NeptuneStreamPollerExecu-{{(uuid)}}
```

## Changes required for bulk import utility
<a name="full-text-changes-bulk-import"></a>

 If you are using [ export-neptune-to-elasticsearch](https://github.com/awslabs/amazon-neptune-tools/tree/master/export-neptune-to-elasticsearch) to synchronize existing data to OpenSearch Serverless, add the `LambdaExecutionRole` from the CloudFormation stack to the data access policy for the OpenSearch Serverless collection. The ARN for the `LambdaExecutionRole` has this format: 

```
arn:aws:iam::{{012345678901}}:role/stack-name-LambdaExecutionRole-{{(id)}}
```

For more information, see [Data access control for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html).

## Changes needed to the IAM role used to query Neptune
<a name="full-text-IAM"></a>

The IAM entity (User or Role) used for connecting to the Neptune database should have permissions both for Neptune and the OpenSearch Serverless collection. This means that your user or role must have an OpenSearch Serverless policy like this attached:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowOpenSearchServerlessAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{111122223333}}:root"
      },
      "Action": "aoss:APIAccessAll",
      "Resource": "arn:aws:aoss:{{us-east-1}}:{{111122223333}}:collection/{{collection-id}}"
    }
  ]
}
```

------

See [Creating custom IAM policy statements to access data in Amazon Neptune](iam-data-access-policies.md) for more information.