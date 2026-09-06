

# Data retrieval APIs for Amazon Keyspaces (for Apache Cassandra)
<a name="amazonkeyspacesforapachecassandra"></a>

Amazon Keyspaces (for Apache Cassandra) provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="cassandra-GetRecords"></a>[GetRecords](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | Retrieve the CDC stream records from a given shard | Read | 
| <a name="cassandra-GetShardIterator"></a>[GetShardIterator](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | Return a shard iterator | Read | 
| <a name="cassandra-GetStream"></a>[GetStream](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | Return information about a CDC stream, including the composition of its shards | Read | 
| <a name="cassandra-ListStreams"></a>[ListStreams](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | Return an array of CDC stream ARNs associated with the current account and endpoint | List | 
| <a name="cassandra-Select"></a>[Select](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | SELECT data from a table | Read | 
| <a name="cassandra-SelectMultiRegionResource"></a>[SelectMultiRegionResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/) | SELECT data from a multiregion table | Read | 