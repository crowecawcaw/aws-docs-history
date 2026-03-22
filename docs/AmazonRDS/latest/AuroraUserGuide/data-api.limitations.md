# Limitations for the Amazon RDS Data API

RDS Data API has the following limitations:

- You can only execute Data API queries on writer instances in a DB cluster. However, writer instances can accept both write and read queries.
- With Aurora global databases, you can enable Data API on both the primary and
  secondary DB clusters. However, a secondary cluster doesn't have a writer
  instance until it's promoted to be the primary. Data API requires access to the
  writer instance for query processing, even for read queries. As a result, read
  and write queries sent to the secondary cluster fail while it lacks a writer
  instance. Once a secondary cluster is promoted and has a writer instance
  available, Data API queries on that DB instance succeed.
- Data API isn't supported on T DB instance classes.
- For Aurora Serverless v2 and provisioned DB clusters, RDS Data API doesn't support
  some data types. For the list of supported types, see [Comparing Amazon RDS Data API behaviors for Aurora Serverless v2 and provisioned clusters with Aurora Serverless v1 clusters](data-api.differences.md "data-api.differences.md").
- For Aurora PostgreSQL version 14 and higher databases, Data API only supports
  `scram-sha-256` for password encryption.
- The response size limit is 1 MiB. If the call returns more than 1 MiB of response data, the call is terminated.
- For Aurora Serverless v1, the maximum number of requests per second is 1,000.
  For all other supported databases, there is no limit.
- The Data API size limit is 64 KB per row in the result set returned by the database.
  Make sure that each row in a result set is 64 KB or less.
