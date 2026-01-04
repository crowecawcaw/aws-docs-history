# Configure a client-side timeout (Valkey and Redis OSS)

**Configuring the client-side timeout**

Configure the client-side timeout appropriately to allow the server sufficient time to process the request and generate the response. This also allows it to fail fast if the connection to the server can't be established.
Certain Valkey or Redis OSS commands can be more computationally expensive than others. For example, Lua scripts or MULTI/EXEC transactions that contain multiple commands that must be run atomically. In general, a higher client-side timeout is
recommended to avoid a time out of the client before the response is received from the server, including the following:

- Running commands across multiple keys
- Running MULTI/EXEC transactions or Lua scripts that consist of multiple individual Valkey or Redis OSS commands
- Reading large values
- Performing blocking operations such as BLPOP
  In case of a blocking operation such as BLPOP, the best practice is to set the command timeout to a number lower than the socket timeout.

The following are code examples for implementing a client-side timeout in redis-py, PHPRedis, and Lettuce.

**Timeout configuration sample 1: redis-py**

The following is a code example with redis-py:

```
# connect to Redis server with a 100 millisecond timeout
# give every Redis command a 2 second timeout
client = redis.Redis(connection_pool=redis.BlockingConnectionPool(host=HOST, max_connections=10,socket_connect_timeout=0.1,socket_timeout=2))

res = client.set("key", "value") # will timeout after 2 seconds
print(res)                       # if there is a connection error

res = client.blpop("list", timeout=1) # will timeout after 1 second
                                      # less than the 2 second socket timeout
print(res)
```

**Timeout config sample 2: PHPRedis**

The following is a code example with PHPRedis:

```
// connect to Redis server with a 100ms timeout
// give every Redis command a 2s timeout
$client = new Redis();
$timeout = 0.1; // 100 millisecond connection timeout
$retry_interval = 100; // 100 millisecond retry interval
$client = new Redis();
if($client->pconnect($HOST, $PORT, 0.1, NULL, 100, $read_timeout=2) != TRUE){
	return; // ERROR: connection failed
}
$client->set($key, $value);

$res = $client->set("key", "value"); // will timeout after 2 seconds
print "$res\n";                      // if there is a connection error

$res = $client->blpop("list", 1); // will timeout after 1 second
print "$res\n";                   // less than the 2 second socket timeout
```

**Timeout config sample 3: Lettuce**

The following is a code example with Lettuce:

```
// connect to Redis server and give every command a 2 second timeout
public static void main(String[] args)
{
	RedisClient client = null;
	StatefulRedisConnection<String, String> connection = null;
	try {
		client = RedisClient.create(RedisURI.create(HOST, PORT));
		client.setOptions(ClientOptions.builder()
	.socketOptions(SocketOptions.builder().connectTimeout(Duration.ofMillis(100)).build()) // 100 millisecond connection timeout
	.timeoutOptions(TimeoutOptions.builder().fixedTimeout(Duration.ofSeconds(2)).build()) // 2 second command timeout
	.build());

		// use the connection pool from above example

		commands.set("key", "value"); // will timeout after 2 seconds
		commands.blpop(1, "list"); // BLPOP with 1 second timeout
	} finally {
		if (connection != null) {
			connection.close();
		}

		if (client != null){
			client.shutdown();
		}
	}
}
```
