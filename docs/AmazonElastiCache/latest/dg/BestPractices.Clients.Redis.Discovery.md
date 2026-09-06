

# Cluster client discovery and exponential backoff (Valkey and Redis OSS)
<a name="BestPractices.Clients.Redis.Discovery"></a>

When connecting to an ElastiCache Valkey or Redis OSS cluster in cluster mode enabled, the corresponding client library must be cluster aware. The clients must obtain a map of hash slots to the corresponding nodes in the cluster in order to send requests to the right nodes and avoid the performance overhead of handing cluster redirections. As a result, the client must discover a complete list of slots and the mapped nodes in two different situations:
+ The client is initialized and must populate the initial slots configuration
+ A MOVED redirection is received from the server, such as in the situation of a failover when all slots served by the former primary node are taken over by the replica, or re-sharding when slots are being moved from the source primary to the target primary node

Client discovery is usually done via issuing a CLUSTER SLOTS or CLUSTER NODES command to the Valkey or Redis OSS server. We recommend the CLUSTER SLOTS method because it returns the set of slot ranges and the associated primary and replica nodes back to the client. This doesn't require additional parsing from the client and is more efficient.

Depending on the cluster topology, the size of the response for the CLUSTER SLOTS command can vary based on the cluster size. Larger clusters with more nodes produce a larger response. As a result, it's important to ensure that the number of clients doing the cluster topology discovery doesn't grow unbounded. For example, when the client application starts up or loses connection from the server and must perform cluster discovery, one common mistake is that the client application fires several reconnection and discovery requests without adding exponential backoff upon retry. This can render the Valkey or Redis OSS server unresponsive for a prolonged period of time, with the CPU utilization at 100%. The outage is prolonged if each CLUSTER SLOTS command must process a large number of nodes in the cluster bus. We have observed multiple client outages in the past due to this behavior across a number of different languages including Python (redis-py-cluster) and Java (Lettuce and Redisson).

In a serverless cache, many of the problems are automatically mitigated because the advertised cluster topology is static and consists of two entries: a write endpoint and a read endpoint. Cluster discovery is also automatically spread over multiple nodes when using the cache endpoint. The following recommendations are still useful, however.

To mitigate the impact caused by a sudden influx of connection and discovery requests, we recommend the following:
+ Implement a client connection pool with a finite size to bound the number of concurrent incoming connections from the client application.
+ When the client disconnects from the server due to timeout, retry with exponential backoff with jitter. This helps to avoid multiple clients overwhelming the server at the same time.
+ Use the guide at [Finding connection endpoints in ElastiCache](Endpoints.md) to find the cluster endpoint to perform cluster discovery. In doing so, you spread the discovery load across all nodes in the cluster (up to 90) instead of hitting a few hardcoded seed nodes in the cluster.

The following are some code examples for exponential backoff retry logic in redis-py, PHPRedis, and Lettuce.

**Backoff logic sample 1: redis-py**

redis-py has a built-in retry mechanism that supports exponential backoff with jitter. If no `retry` parameter is provided, redis-py defaults to `ExponentialWithJitterBackoff` with 3 retries. You can customize the retry behavior through the `retry` and `retry_on_error` arguments when creating a [Redis](https://redis.readthedocs.io/en/stable/retry.html) client.

```
from redis.backoff import ExponentialBackoff
from redis.retry import Retry
from redis.client import Redis
from redis.exceptions import ConnectionError, TimeoutError, BusyLoadingError

# Run 3 retries with exponential backoff strategy
retry = Retry(ExponentialBackoff(), 3)

# Redis client with retries
client = Redis(
    host="clustercfg.my-cluster.us-east-1.cache.amazonaws.com",
    port=6379,
    retry=retry,
    retry_on_error=[BusyLoadingError, ConnectionError, TimeoutError],
    ssl=True
)
```

For more information about retry configuration options, see [Retry Helpers](https://redis.readthedocs.io/en/stable/retry.html) in the redis-py documentation.

**Backoff logic sample 2: PHPRedis**

PHPRedis has a built-in retry mechanism that retries a (non-configurable) maximum of 10 times. There is a configurable delay between tries (with a jitter from the second retry onwards). For more information, see the following [sample code](https://github.com/phpredis/phpredis/blob/b0b9dd78ef7c15af936144c1b17df1a9273d72ab/library.c#L335-L368). We've submitted a pull request to natively implement exponential backoff in [PHPredis (\#1986)](https://github.com/phpredis/phpredis/pull/1986) that has since been merged and [documented](https://github.com/phpredis/phpredis/blob/develop/README.md#retry-and-backoff). For those on the latest release of PHPRedis, it won't be necessary to implement manually but we've included the reference here for those on previous versions. For now, the following is a code example that configures the delay of the retry mechanism:

```
$timeout = 0.1; // 100 millisecond connection timeout
$retry_interval = 100; // 100 millisecond retry interval
$client = new Redis();
if($client->pconnect($HOST, $PORT, $timeout, NULL, $retry_interval) != TRUE) {
	return; // ERROR: connection failed
}
$client->set($key, $value);
```

**Backoff logic sample 3: Lettuce**

Lettuce has built-in retry mechanisms based on the exponential backoff strategies described in the post [Exponential Backoff and Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/). The following is a code excerpt showing the full jitter approach:

```
public static void main(String[] args)
{
	ClientResources resources = null;
	RedisClient client = null;

	try {
		resources = DefaultClientResources.builder()
				.reconnectDelay(Delay.fullJitter(
			Duration.ofMillis(100),     // minimum 100 millisecond delay
			Duration.ofSeconds(5),      // maximum 5 second delay
			100, TimeUnit.MILLISECONDS) // 100 millisecond base
		).build();

		client = RedisClient.create(resources, RedisURI.create(HOST, PORT));
		client.setOptions(ClientOptions.builder()
	.socketOptions(SocketOptions.builder().connectTimeout(Duration.ofMillis(100)).build()) // 100 millisecond connection timeout
	.timeoutOptions(TimeoutOptions.builder().fixedTimeout(Duration.ofSeconds(5)).build()) // 5 second command timeout
	.build());

	    // use the connection pool from above example
	} finally {
		if (connection != null) {
			connection.close();
		}

		if (client != null){
			client.shutdown();
		}

		if (resources != null){
			resources.shutdown();
		}

	}
}
```