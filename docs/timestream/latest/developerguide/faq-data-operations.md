

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Writing and querying data FAQ for Amazon Timestream for InfluxDB 3
<a name="faq-data-operations"></a>

Questions about writing data to and querying data from Amazon Timestream for InfluxDB 3, including supported APIs, query languages, and authentication. For complete guides, see [Writing data to your Timestream for InfluxDB 3 cluster](writing-data-to-your-influxdb-3-cluster.md) and [Querying data from Timestream for InfluxDB 3](querying-data-from-influxdb-3.md).

**How do I write data to InfluxDB 3?**  
InfluxDB 3 supports multiple write methods: the native v3 write API, the InfluxDB v2 compatibility API, and the InfluxDB v1 compatibility API. All methods accept line protocol format. Official client libraries are available for Python, Go, Java, JavaScript, and C\#. For detailed write instructions, see the [InfluxDB 3 Enterprise write data guide](https://docs.influxdata.com/influxdb3/enterprise/write-data/).

**What query languages does InfluxDB 3 support?**  
InfluxDB 3 supports SQL and InfluxQL through the v3 HTTP query API. SQL is the primary query language, powered by the Apache DataFusion engine. InfluxQL is supported for backward compatibility. You can also query using the `influxdb3` CLI tool. For query syntax and examples, see the [InfluxDB 3 Enterprise query data guide](https://docs.influxdata.com/influxdb3/enterprise/query-data/).  
Example SQL query:  

```
SELECT time, temperature, location
FROM weather
WHERE time > now() - INTERVAL '1 hour'
ORDER BY time DESC
LIMIT 100
```

**How does authentication work for queries?**  
InfluxDB 3 uses token-based authentication. When you first set up your cluster, you create a master user account and password. In the Enterprise edition, you can create multiple tokens with different access levels:  
+ **Admin tokens** – Grant full access to all server actions, including CLI commands and API endpoints. The first admin token created is the operator token, which has full administrative privileges.
+ **Resource tokens** – Grant granular permissions on specific resources such as individual databases and tables. You can assign read-only, write-only, or read-write access per database, enabling fine-grained access control for different applications and users.
Tokens work with the v3 HTTP query API, the `influxdb3` CLI, and the v1/v2 compatibility APIs. For more details, see the [InfluxDB 3 Enterprise token management documentation](https://docs.influxdata.com/influxdb3/enterprise/admin/tokens/).

**Can I manage databases and tables through the data plane?**  
Yes. In InfluxDB 3 Enterprise, you can create, list, and delete databases and tables directly using the `influxdb3` CLI or the HTTP API. You can also manage Last Value Caches, Distinct Value Caches, and custom file indexes for query optimization. These data plane operations let you administer your cluster without using the AWS Management Console. For the full list of administrative operations, see the [InfluxDB 3 Enterprise administration guide](https://docs.influxdata.com/influxdb3/enterprise/admin/).

**Why is my query returning a 401 Unauthorized error?**  
A 401 error means your authentication token is missing, expired, or does not have the required permissions. Verify that you are passing the token in the `Authorization: Bearer` header (or via the `INFLUXDB3_AUTH_TOKEN` environment variable for the CLI). If using resource tokens, confirm the token has read permission on the target database. Regenerate the token if it may have been revoked.

**Why are my queries slow?**  
Common causes include scanning too many Parquet files (check `query-file-limit`), insufficient DataFusion threads for your instance size, or a cold Parquet memory cache after a restart. For Enterprise clusters, verify that compaction is running — without compaction, small files accumulate and degrade query performance. See [Detailed Parameter Reference](detailed-parameter-reference.md) for tuning guidance.

**What is line protocol?**  
Line protocol is a text-based format for writing time-series data to InfluxDB. Each line represents a single data point with a measurement name, optional tag set, field set, and optional timestamp. For the full specification, see the [InfluxDB 3 line protocol reference](https://docs.influxdata.com/influxdb3/enterprise/reference/line-protocol/).  
Example line protocol:  

```
weather,location=us-east,station=A1 temperature=82.0,humidity=71.2 1465839830100400200
weather,location=us-west,station=B2 temperature=68.5,humidity=45.8 1465839830100400200
```