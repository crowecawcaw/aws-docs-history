

# Data retrieval APIs for Amazon DynamoDB
<a name="amazondynamodb"></a>

Amazon DynamoDB provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="dynamodb-BatchGetItem"></a>[BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html) | Return the attributes of one or more items from one or more tables | Read | 
| <a name="dynamodb-ConditionCheckItem"></a>[ConditionCheckItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ConditionCheck.html) | The ConditionCheckItem operation checks the existence of a set of attributes for the item with the given primary key | Read | 
| <a name="dynamodb-DescribeBackup"></a>[DescribeBackup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBackup.html) | Describe an existing backup of a table | Read | 
| <a name="dynamodb-DescribeContinuousBackups"></a>[DescribeContinuousBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContinuousBackups.html) | Check the status of the backup restore settings on the specified table | Read | 
| <a name="dynamodb-DescribeContributorInsights"></a>[DescribeContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContributorInsights.html) | Describe the contributor insights status and related details for a given table or global secondary index | Read | 
| <a name="dynamodb-DescribeEndpoints"></a>[DescribeEndpoints](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeEndpoints.html) | Return the regional endpoint information | Read | 
| <a name="dynamodb-DescribeExport"></a>[DescribeExport](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeExport.html) | Describe an existing Export of a table | Read | 
| <a name="dynamodb-DescribeGlobalTable"></a>[DescribeGlobalTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTable.html) | Return information about the specified global table | Read | 
| <a name="dynamodb-DescribeGlobalTableSettings"></a>[DescribeGlobalTableSettings](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTableSettings.html) | Return settings information about the specified global table | Read | 
| <a name="dynamodb-DescribeImport"></a>[DescribeImport](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeImport.html) | Describe an existing import | Read | 
| <a name="dynamodb-DescribeKinesisStreamingDestination"></a>[DescribeKinesisStreamingDestination](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeKinesisStreamingDestination.html) | Grant permission to describe the status of Kinesis streaming and related details for a given table | Read | 
| <a name="dynamodb-DescribeLimits"></a>[DescribeLimits](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeLimits.html) | Return the current provisioned-capacity limits for your AWS account in a region, both for the region as a whole and for any one DynamoDB table that you create there | Read | 
| <a name="dynamodb-DescribeReservedCapacity"></a>[DescribeReservedCapacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-prevent-purchase-reserved-capacity.html) | Describe one or more of the Reserved Capacity purchased | Read | 
| <a name="dynamodb-DescribeReservedCapacityOfferings"></a>[DescribeReservedCapacityOfferings](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-prevent-purchase-reserved-capacity.html) | Describe Reserved Capacity offerings that are available for purchase | Read | 
| <a name="dynamodb-DescribeStream"></a>[DescribeStream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html) | Return information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table | Read | 
| <a name="dynamodb-DescribeTable"></a>[DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html) | Return information about the table | Read | 
| <a name="dynamodb-DescribeTableReplicaAutoScaling"></a>[DescribeTableReplicaAutoScaling](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTableReplicaAutoScaling.html) | Describe the auto scaling settings across all replicas of the global table | Read | 
| <a name="dynamodb-DescribeTimeToLive"></a>[DescribeTimeToLive](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTimeToLive.html) | Give a description of the Time to Live (TTL) status on the specified table | Read | 
| <a name="dynamodb-GetAbacStatus"></a>[GetAbacStatus](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/abac-enable-ddb.html) | View the status of Attribute Based Access Control for the account | Read | 
| <a name="dynamodb-GetItem"></a>[GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html) | The GetItem operation that returns a set of attributes for the item with the given primary key | Read | 
| <a name="dynamodb-GetRecords"></a>[GetRecords](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetRecords.html) | Retrieve the stream records from a given shard | Read | 
| <a name="dynamodb-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetResourcePolicy.html) | View a resource-based policy for a resource | Read | 
| <a name="dynamodb-GetShardIterator"></a>[GetShardIterator](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html) | Return a shard iterator | Read | 
| <a name="dynamodb-ListBackups"></a>[ListBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBackups.html) | List backups associated with the account and endpoint | List | 
| <a name="dynamodb-ListContributorInsights"></a>[ListContributorInsights](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListContributorInsights.html) | List the ContributorInsightsSummary for all tables and global secondary indexes associated with the current account and endpoint | List | 
| <a name="dynamodb-ListExports"></a>[ListExports](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListExports.html) | List exports associated with the account and endpoint | List | 
| <a name="dynamodb-ListGlobalTables"></a>[ListGlobalTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListGlobalTables.html) | List all global tables that have a replica in the specified region | List | 
| <a name="dynamodb-ListImports"></a>[ListImports](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListImports.html) | List imports associated with the account and endpoint | List | 
| <a name="dynamodb-ListStreams"></a>[ListStreams](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_ListStreams.html) | Return an array of stream ARNs associated with the current account and endpoint | Read | 
| <a name="dynamodb-ListTables"></a>[ListTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html) | Return an array of table names associated with the current account and endpoint | List | 
| <a name="dynamodb-ListTagsOfResource"></a>[ListTagsOfResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTagsOfResource.html) | List all tags on an Amazon DynamoDB resource | Read | 
| <a name="dynamodb-PartiQLSelect"></a>[PartiQLSelect](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html) | Read a set of attributes for items from a table or index | Read | 
| <a name="dynamodb-Query"></a>[Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) | Use the primary key of a table or a secondary index to directly access items from that table or index | Read | 
| <a name="dynamodb-ReadDataForReplication"></a>[ReadDataForReplication](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_MA_security.html) | Read data from a multi account global table replica | Read | 
| <a name="dynamodb-Scan"></a>[Scan](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html) | Return one or more items and item attributes by accessing every item in a table or a secondary index | Read | 
| <a name="dynamodb-SearchVectors"></a>[SearchVectors](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SearchVectors.html) | Perform a vector similarity search on a vector index associated with an Amazon DynamoDB table | Read | 