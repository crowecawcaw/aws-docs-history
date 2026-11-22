

# Configuring DynamoDB caching

You configure DynamoDB caching when you install the Amazon ElastiCache integration client in your application. The client install operation takes connection arguments plus an optional client configuration. Optional cache policy overrides control what the client caches and for how long.

**Note**  
The settings and options below use the Python client names. Names in other languages (for example, Node.js or Java) might differ slightly because of each language's case conventions. For the names and defaults in your language, see the client library READMEs on GitHub ([elasticache-integration-client](https://github.com/awslabs/elasticache-integration-client)).

## Client installation arguments
<a name="ddb-caching-configuration.connection"></a>

You pass the following arguments to the client's install operation.


**Client installation arguments**  

| Argument | Required | Default | Description | 
| --- | --- | --- | --- | 
| `client` | Yes | None | The DynamoDB client from the AWS SDK. | 
| `endpoint` | Yes | None | The cache endpoint (host:port). | 
| `cache_name` | Yes | None | The name of the serverless cache. | 
| `ca_certs` | No | System trust store | The path to a certificate authority (CA) bundle used to verify the cache's TLS certificate. | 
| `client_configuration` | No | All defaults | The client configuration options. | 
| `user_id` | No | `default.iam-user` | The ElastiCache IAM user to authenticate as. | 

## Client configuration options
<a name="ddb-caching-configuration.behavior"></a>

Client configuration options are used to control client behavior.


**Client configuration options**  

| Option | Default | Description | 
| --- | --- | --- | 
| `cache_policy_overrides` | None | The tables, operations, and entry lifetimes to cache. See the following table. | 
| `cache_policy_timeout` | 3600 | The time the client keeps using a cache policy that the cache has not confirmed, in seconds. | 
| `cache_request_timeout` | 5000 | The time to wait for the cache to answer a request, in milliseconds. | 
| `connection_timeout` | 5000 | The time to try connecting at startup, and the time a request waits for a lost connection to return, in milliseconds. | 
| `fallback_duration` | No limit | The time that requests can go to DynamoDB directly while the cache is unreachable, in seconds. A value of 0 means requests never fall back to DynamoDB. | 
| `iam_token_refresh_delay` | 300 | The time after an IAM token is issued before a replacement is signed in the background, in seconds. Valid values are 1–879. | 

## Cache policy overrides
<a name="ddb-caching-configuration.overrides"></a>

Cache policy overrides control what the client caches and for how long.


**Cache policy override options**  

| Option | Default | Description | 
| --- | --- | --- | 
| `cached_operations` | All operations | The DynamoDB operations to cache, such as GetItem or Query. Empty or absent means all supported operations. | 
| `cached_tables` | All tables | The DynamoDB tables to cache. Empty or absent means all tables. | 
| `item_negative_ttl` | 60 | How long negative item cache entries (a cached "item does not exist" result) live, in seconds. | 
| `item_ttl` | 300 | How long item cache entries live, in seconds. | 
| `item_write_behavior` | UPDATE\_CACHED | How write requests affect cached entries.+ `INVALIDATE_ONLY`: Invalidates (deletes) cached item projections instead of updating them.<br />+ `UPDATE_CACHED`: Updates any cached item projections.<br />+ `UPDATE_CACHED_AND_STORE_FULL_ITEM`: Caches the complete item and updates any cached item projections. | 
| `query_ttl` | 300 | How long query cache entries live, in seconds. | 
| `scan_ttl` | 300 | How long scan cache entries live, in seconds. | 
| `table_overrides` | None | Cache policy overrides for specific tables. Per-table settings override global cache policy settings. | 

For the full configuration reference for your preferred language, see [elasticache-integration-client](https://github.com/awslabs/elasticache-integration-client) on GitHub.