# Data retrieval APIs for Amazon Keyspaces (for Apache Cassandra)

Amazon Keyspaces (for Apache Cassandra) provides the following APIs for data retrieval.

| Actions                                                                                                    | Description                                                                         | Access level |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------ |
| [GetRecords](../../../keyspaces/latest/devguide.md "../../../keyspaces/latest/devguide.md")                | Retrieve the CDC stream records from a given shard                                  | Read         |
| [GetShardIterator](../../../keyspaces/latest/devguide.md "../../../keyspaces/latest/devguide.md")          | Return a shard iterator                                                             | Read         |
| [GetStream](../../../keyspaces/latest/devguide.md "../../../keyspaces/latest/devguide.md")                 | Return information about a CDC stream, including the composition of its shards      | Read         |
| [ListStreams](../../../keyspaces/latest/devguide.md "../../../keyspaces/latest/devguide.md")               | Return an array of CDC stream ARNs associated with the current account and endpoint | List         |
| [Select](../../../keyspaces/latest/devguide.md "../../../keyspaces/latest/devguide.md")                    | SELECT data from a table                                                            | Read         |
| [SelectMultiRegionResource](../../../keyspaces/latest/devguide.md "../../../keyspaces/latest/devguide.md") | SELECT data from a multiregion table                                                | Read         |
