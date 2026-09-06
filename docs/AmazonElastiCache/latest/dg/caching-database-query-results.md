

# Caching database query results
<a name="caching-database-query-results"></a>

A common pattern to reduce database query latencies is query caching. Applications implement query caching by querying the cache for results associated with a database query, returning those results if they are cached. If no cached results are found, the query is executed on the database, the results are populated in the cache, and the results are then returned to the application initiating the query. Subsequent database queries will then return cached results as long as they remain in the cache.

## When to use query caching
<a name="caching-database-query-results-when-to-use"></a>

Query caching with ElastiCache is most effective for the following workload types:
+ **Read-heavy applications** where the same queries are executed repeatedly with data that changes infrequently.
+ **Expensive queries** such as non-indexed lookups, aggregations, or multi-table joins where query execution times are long.
+ **High-concurrency scenarios** where offloading reads to ElastiCache reduces database CPU pressure and improves overall throughput.

Query caching is not recommended for queries where strong consistency is required, or for queries inside multi-statement transactions that require read-after-write consistency.

## Using the AWS Advanced JDBC Wrapper
<a name="caching-database-query-results-jdbc-wrapper"></a>

If your application is using a JDBC driver to query a relational database, you can implement query caching with the [Remote Query Cache Plugin](https://github.com/aws/aws-advanced-jdbc-wrapper/blob/main/docs/using-the-jdbc-driver/using-plugins/UsingTheRemoteQueryCachePlugin.md) in the [AWS Advanced JDBC Wrapper](https://github.com/aws/aws-advanced-jdbc-wrapper). The plugin automatically caches selected SQL query result sets in ElastiCache, returning the result set from the cache instead of the database for future queries. Caching query results can reduce database load and lower average query latencies with minimal application code changes.

## How query caching works with the plugin
<a name="caching-database-query-results-how-it-works"></a>

The Remote Query Cache Plugin makes it easy for Java applications that query PostgreSQL, MySQL, or MariaDB databases to automatically cache query results in ElastiCache. You configure the plugin with your cache endpoint information and indicate which queries in your code to cache using query hints. When the plugin detects a hinted query, it returns the query result from the cache if present (a cache hit). If the results are not in the cache (a cache miss), the plugin executes the query on the database, stores the results in the cache, and returns the results to your application so the next time the query is executed the results can be served from the cache.

## Caching hints
<a name="caching-database-query-results-hints"></a>

You control which queries to cache by setting hints on each query. You can apply query hints directly to query strings in your application code with a comment prefix:

```
/* CACHE_PARAM(ttl=300s) */ SELECT * FROM my_table WHERE id = 42
```

where `ttl` is the time-to-live in seconds. You can also set query hints in prepared statements using common frameworks like Hibernate and Spring Boot.

## Prerequisites
<a name="caching-database-query-results-prerequisites"></a>

To use the Remote Query Cache Plugin in your application, you need an ElastiCache for Valkey or Redis OSS cache (both Serverless and node-based are supported) along with the following dependencies:
+ [AWS Advanced JDBC Wrapper](https://github.com/aws/aws-advanced-jdbc-wrapper) version 3.3.0 or later.
+ [Apache Commons Pool](https://commons.apache.org/proper/commons-pool/) version 2.11.1 or later.
+ [Valkey Glide](https://glide.valkey.io/) version 2.3.0 or later.

## Example: Caching a query with the plugin
<a name="caching-database-query-results-example"></a>

The following example shows how to enable the plugin and cache a query result for 300 seconds (5 minutes) with an ElastiCache for Valkey serverless cache:

```
import java.sql.*;
import java.util.Properties;

public class QueryCacheExample {
    public static void main(String[] args) throws SQLException {
        Properties props = new Properties();
        props.setProperty("user", "myuser");
        props.setProperty("password", "mypassword");

        // Enable the remote query cache plugin
        props.setProperty("wrapperPlugins", "remoteQueryCache");

        // Point to your ElastiCache endpoint
        props.setProperty("cacheEndpointAddrRw", "my-cache.serverless.use1.cache.amazonaws.com:6379");

        Connection conn = DriverManager.getConnection(
            "jdbc:aws-wrapper:postgresql://my-database.cluster-abc123.us-east-1.rds.amazonaws.com:5432/mydb",
            props
        );

        Statement stmt = conn.createStatement();

        // The SQL comment hint tells the plugin to cache this query for 300 seconds
        ResultSet rs = stmt.executeQuery(
            "/* CACHE_PARAM(ttl=300s) */ SELECT product_name, price FROM products WHERE category = 'electronics'"
        );

        while (rs.next()) {
            System.out.println(rs.getString("product_name") + ": $" + rs.getBigDecimal("price"));
        }

        rs.close();
        stmt.close();
        conn.close();
    }
}
```

The first time this query runs, the result is returned from the database and cached in ElastiCache. For the next 300 seconds, subsequent executions of that query are served directly from the cache.

## Related resources
<a name="caching-database-query-results-related"></a>

You can find more extensive examples and detailed information about plugin configuration in the [Remote Query Cache Plugin documentation](https://github.com/aws/aws-advanced-jdbc-wrapper/blob/main/docs/using-the-jdbc-driver/using-plugins/UsingTheRemoteQueryCachePlugin.md).